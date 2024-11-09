label prisoner_rewrites:

    # note: mostly just re-writing the "leave the cabin with the head" ending so that the skeptic, a dumbass, does not pick up on the princess' game

    #making this more sure, unless you still want him to be doubtful?
    voice "audio/_pristine/voice/cage/skeptic/1.flac"
    skeptic "Huh. So I guess that's it. What a way to go. But she is gone, isn't she?\n"

    # starting in response to: Of course. The Princess is slain, and the world is saved. Whenever you're ready you can proceed to your reward.
    voice "audio/_pristine/voice/cage/skeptic/2.flac"
    skeptic "Now hold on. She's dead. So what's the rush? What's your angle?\n"
    voice "audio/_pristine/voice/cage/narrator/1.flac"
    n "I don't have an angle. I'm just looking forward to putting all this behind us, I'm sure you can understand that.\n"
    voice "audio/_pristine/voice/cage/skeptic/3.flac"
    skeptic "Look, I'm just not ready to put my guard down. It's best to keep sharp. She wouldn't have done all that without some kind of reason, she's left us with this dangling thread and I need to know {i}why{/i}.\n"
    voice "audio/_pristine/voice/cage/narrator/2.flac"
    n "You're just wasting your energy. The danger has passed, and now we can all relax and enjoy your reward!\n"

    # skeptic "Did you see that? I could have sworn she moved.\n" ->
    voice "audio/_pristine/voice/cage/hero/1.flac"
    hero "Did you see that? I could have sworn she moved.\n"
    voice "audio/_pristine/voice/cage/skeptic/4.flac"
    skeptic "We probably just jostled her a little.\n"

label cage_start:

    $ gallery_cage.unlock_gallery()
    $ renpy.save_persistent()

    stop music
    stop sound
    stop secondary
    $ current_princess = "cage"
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 3
    $ quick_menu = False
    $ config.menu_include_disabled = False
    $ cage_encountered = True
    $ trait_skeptic = True

    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    scene chapter cage with fade
    show text _("{color=#FFFFFF00}Chapter Three. The Cage.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    scene bg black
    $ quick_menu = False

    if prisoner_give_skeptic_blade:
        # player handed skeptic the blade
        $ trait_broken= True

    elif prisoner_heart_stop:
        # player killed again their will
        $ trait_cheated = True

    else:
        # player killed self
        $ trait_paranoid = True

    $ gallery_cage.unlock_item(1)
    $ renpy.save_persistent()
    $ blade_held = True
    $ default_mouse = "blade"
    play music "audio/_pristine/music/cage/The Cage Intro.flac"
    queue music "audio/_pristine/music/cage/The Cage Loop.flac" loop
    play sound "audio/_pristine/sfx/Cage_AMB metal world_3_loop.flac" loop

    scene farback cage woods onlayer farback at Position(ypos=1125)
    show bg cage woods onlayer back at Position(ypos=1125)
    show mid cage woods onlayer front at Position(ypos=1125)
    show fore cage woods onlayer inyourface at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/_pristine/voice/cage/narrator/3.flac"
    n "You're on a path in the woo—\n{w=1.25}{nw}"
    show screen disableclick(0.5)
    if trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/1.flac"
        cheated "Are you fucking kidding me? We had everything we ever could have wanted and you killed us?\n"
        voice "audio/_pristine/voice/cage/skeptic/5.flac"
        skeptic "We didn't have 'everything we ever could have wanted.' That's just what He told us. I want the truth, not some made-up eternal happiness.\n"
        voice "audio/_pristine/voice/cage/cheated/2.flac"
        cheated "But it was nice! Who gives a shit about truth?\n"
        voice "audio/_pristine/voice/cage/skeptic/6.flac"
        skeptic "I do. He said we were happy, but what does happiness like that even mean? It was just another prison.\n"
        voice "audio/_pristine/voice/cage/cheated/3.flac"
        cheated "And this isn't?! There are chains everywhere.\n"
        voice "audio/_pristine/voice/cage/skeptic/7.flac"
        skeptic "That just means we're on the right track, you numbskull. That we're finally starting to see reality for what it is.\n"
        voice "audio/_pristine/voice/cage/hero/2.flac"
        hero "Can you two stop fighting? It's not very productive.\n"
        voice "audio/_pristine/voice/cage/narrator/4.flac"
        n "No. It isn't, is it? So let's focus up.\n"
    elif trait_broken:
        voice "audio/_pristine/voice/cage/hero/3.flac"
        hero "See? All done. That wasn't so bad, was it, buddy?\n"
        voice "audio/_pristine/voice/cage/broken/1.flac"
        broken "But it was so bad. I don't like dying. I don't like being cold and alone in the dark.\n"
        voice "audio/_pristine/voice/cage/hero/4.flac"
        hero "I don't think anybody likes dying, but hey, at least it's over. We got better! And now we can move on. Things will work out this time, I know it.\n"
        voice "audio/_pristine/voice/cage/skeptic/8a.flac"
        skeptic "Oh, don't coddle him. For all we know we'll have to die hundreds of times to get to the bottom of things. Maybe even thousands. He needs to toughen up.\n"
        if prisoner_decapitation_watch:
            voice "audio/_pristine/voice/cage/broken/2.flac"
            broken "Toughen up?! You're both freaks! I'm having a rational reaction to what just happened. I'm normal, a normal person gets traumatized from dying! And from watching someone cut her own head off!\n"
        else:
            voice "audio/_pristine/voice/cage/broken/3.flac"
            broken "Toughen up?! You're both freaks! I'm normal, a normal person gets traumatized from dying. And from having to listen to someone cut her own head off! Those... sounds... are still echoing in my ears...\n"
        voice "audio/_pristine/voice/cage/hero/5.flac"
        hero "Hold on, did you say {i}thousands{/i}? How can it possibly take us thousands of lives to find a way out of here?\n"
        voice "audio/_pristine/voice/cage/skeptic/9.flac"
        skeptic "Obviously we need a large sample size... i-in order to figure out our optimal plan. We need statistical significance!\n"
        voice "audio/_pristine/voice/cage/narrator/5.flac"
        n "I'll have you know that my reality is not a datapoint in your misguided attempt at an experiment.\n"
    elif trait_paranoid:
        voice "audio/_pristine/voice/cage/paranoid/1.flac"
        paranoid "Chains everywhere. This is different. This is new.\n"
        voice "audio/_pristine/voice/cage/hero/6.flac"
        hero "It's worse, is what it is.\n"
        voice "audio/_pristine/voice/cage/skeptic/10.flac"
        skeptic "We're finally starting to see reality for what it is. This place is a prison, and she's not the only inmate.\n"
        voice "audio/_pristine/voice/cage/paranoid/2a.flac"
        paranoid "You're acting like reality is this static... thing, but this world is constantly changing around us. How can you be so sure that you aren't breathing the prison into existence? That by feeling the walls closing in on you that's exactly what they do?!\n"
        voice "audio/_pristine/voice/cage/skeptic/11a.flac"
        skeptic "What a crock of pretentious bullshit. Reality is as solid as the ground beneath our feet. And if we just examine it, if we apply enough scientific rigor, if we {i}think{/i} hard enough, we'll find a way out of here for good. Don't you see? We're already making progress!\n"
        #voice "audio/_pristine/voice/cage/skeptic/11.flac"
        #skeptic "What a crock of pretentious bullshit. As long as there's ground beneath our feet, reality is real. And if we just examine it, if we apply enough scientific rigor, if we {i}think{/i} hard enough, we'll find a way out of here for good. Don't you see? We're already making progress!\n"
        voice "audio/_pristine/voice/cage/paranoid/3.flac"
        paranoid "And what if looking at it is enough to make it change? Where does that leave us?\n"
        voice "audio/_pristine/voice/cage/narrator/6.flac"
        n "It leaves you exactly where you are right now, and presumably exactly where you've been before.\n"
        voice "audio/_pristine/voice/cage/narrator/7.flac"
        n "{i}Sigh{/i}. I'll spare you my full introduction, since you've clearly already heard it at least once, but I would like to remind you that the people in my world are living, breathing, suffering entities and not pawns for you to sacrifice in pursuit of some vague truth.\n"

    if trait_paranoid == False:
        voice "audio/_pristine/voice/cage/narrator/8a.flac"
        n "{i}Sigh{/i} You've clearly already been here before, and judging by how deranged you all are, you've already been here more than once. I'll spare you my full introduction, but I would like remind you that the people in my world are living, breathing, suffering entities and not pawns for you to sacrifice in pursuit of some vague truth.\n"
    #voice "audio/_pristine/voice/cage/skeptic/12.flac"
    #skeptic "The truth only seems vague because we haven't found it yet. You keep getting in the way!\n"
    #voice "audio/_pristine/voice/cage/narrator/9.flac"
    #n "I'm not getting in anyone's way, and I've told you the truth already! The Princess poses an existential threat to reality, and you are the sole person capable of slaying her and burying that threat for good.\n"

label cage_woods_menu:
    default cage_death_n_known = False
    default cage_woods_blade_explore = False
    default cage_blade_thrown = False
    default cage_woods_last_time_comment = False
    menu:
        extend ""

        "{i}• (Explore) Should we talk about how we still have the blade? We've never started with the blade before.{/i}" if cage_woods_blade_explore == False:
            $ cage_woods_blade_explore = True
            voice "audio/_pristine/voice/cage/skeptic/13.flac"
            skeptic "Huh. I... hadn't actually noticed.\n"
            voice "audio/_pristine/voice/cage/hero/7.flac"
            hero "Holding it's starting to feel... natural, isn't it?\n"
            if trait_broken:
                voice "audio/_pristine/voice/cage/broken/4a.flac"
                broken "Holding a weapon shouldn't feel so natural. It's proof that we're being guided by an unfeeling lunatic. We need to try talking to her.\n"
                voice "audio/_pristine/voice/cage/skeptic/14.flac"
                skeptic "Oh, should we talk about our {i}feelings{/i}? That'll get us nowhere, trust me. They're too easy for her to manipulate, too illogical. We can't puzzle our way out of things if we listen to our heart.\n"
                voice "audio/_pristine/voice/cage/broken/5.flac"
                broken "I don't think I even need to comment on that. What a sorry, sorry voice you are.\n"
            if trait_paranoid:
                voice "audio/_pristine/voice/cage/paranoid/4.flac"
                paranoid "Of course it feels natural. We've had it with us every time. We've made it part of us.\n"
                voice "audio/_pristine/voice/cage/skeptic/15.flac"
                skeptic "Don't be weird, it's just a tool, not some mystical object. Though starting with it feels like an indication that we're on the right track.\n"
                #voice "audio/_pristine/voice/cage/skeptic/15a.flac"
                #skeptic "Don't be weird, it's just a tool, not some mystical object.\n"
            if trait_cheated:
                voice "audio/_pristine/voice/cage/cheated/4.flac"
                cheated "It doesn't matter if we spawn with it or have to trudge all the way up to the cabin to get it. It's not even a 'blade' really, it's just a dinky little knife. The real threat here can kill us without it anyway.\n"
                voice "audio/_pristine/voice/cage/skeptic/16.flac"
                skeptic "I didn't. Kill us. Without reason.\n"
                voice "audio/_pristine/voice/cage/cheated/5.flac"
                cheated "Well you still killed us!\n"
            voice "audio/_pristine/voice/cage/narrator/10.flac"
            n "This is strange, you're not supposed to start with the blade. It says right here that you're supposed to find it at the cabin. Oh, well! I suppose that doesn't make much sense, anyway... it's better if you start with a weapon, so this is probably for the best.\n"
            jump cage_woods_menu

        "{i}• (Explore) She died last time, and the way you decided to thank us was locking us away in a happiness void forever.{/i}" if prisoner_happy_seen and cage_woods_last_time_comment == False:
            $ cage_woods_last_time_comment = True
            if trait_broken:
                voice "audio/_pristine/voice/cage/narrator/13.flac"
                n "So I didn't mishear you earlier... that doesn't make any sense, though. She's not supposed to be suicidal!\n"
                voice "audio/_pristine/voice/cage/narrator/15.flac"
                n "More importantly, if she did 'cut her own head off,' why are you here?! You shouldn't have died. You should be enjoying your reward.\n"
            else:
                voice "audio/_pristine/voice/cage/narrator/11.flac"
                n "So you actually managed to slay her, yet you still found your way back here? Absolutely unbelievable. What on earth is wrong with you?\n"
            voice "audio/_pristine/voice/cage/skeptic/17a.flac"
            skeptic "We weren't satisfied with your happy little prison.\n"
            voice "audio/_pristine/voice/cage/narrator/12.flac"
            n "But it has happy right there in the name!\n"
            voice "audio/_pristine/voice/cage/hero/8.flac"
            hero "It wasn't actually very happy.\n"
            if trait_cheated:
                voice "audio/_pristine/voice/cage/cheated/6.flac"
                cheated "I was fine with it, but that spiteful bastard gave us a heart attack and killed us. For no reason!\n"
                voice "audio/_pristine/voice/cage/skeptic/18.flac"
                skeptic "I had a great reason, we were stuck with no answers! And now we're not. You're welcome.\n"
                jump cage_woods_cheated_expl_join
            elif trait_paranoid:
                voice "audio/_pristine/voice/cage/paranoid/5.flac"
                paranoid "He's right. You can't just tell us we're happy and expect us to go along with it. You were trying to dictate our emotions, how are we supposed to trust someone who does that?\n" id cage_woods_menu_1e7a79a8
                voice "audio/_pristine/voice/cage/skeptic/19.flac"
                skeptic "Damn right. I have about as much trust for Him as I have for her.\n"
                voice "audio/_pristine/voice/cage/hero/9.flac"
                hero "Then who are we supposed to trust? We have to trust someone eventually, right?\n"
                voice "audio/_pristine/voice/cage/parskep.flac"
                parskep "No.\n"
            jump cage_woods_sigh_join

        "{i}• (Explore) Are you sure we even need to slay her? She cut her own head off last time.{/i}" if cage_woods_last_time_comment == False:
            $ cage_woods_last_time_comment = True
            if trait_broken:
                voice "audio/_pristine/voice/cage/narrator/13.flac"
                n "So I didn't mishear you earlier... that doesn't make any sense, though. She's not supposed to be suicidal!\n"
            else:
                label cage_woods_head_cut_join:
                    voice "audio/_pristine/voice/cage/narrator/14.flac"
                    n "She what?! Why would she ever do that? She's not supposed to be suicidal. That doesn't make any sense whatsoever.\n"
            voice "audio/_pristine/voice/cage/narrator/15.flac"
            n "More importantly, if she did 'cut her own head off,' why are you here?! You shouldn't have died. You should be enjoying your reward.\n"
            label cage_woods_explain_join:
                if trait_cheated:
                    voice "audio/_pristine/voice/cage/cheated/6.flac"
                    cheated "I was fine with it, but that spiteful bastard gave us a heart attack and killed us. For no reason!\n"
                    voice "audio/_pristine/voice/cage/skeptic/18.flac"
                    skeptic "I had a great reason, we were stuck with no answers! And now we're not. You're welcome.\n"
                    #voice "audio/_pristine/voice/cage/cheated/7.flac"
                    #cheated "That spiteful asshole gave us a heart attack and killed us.\n"
                    #voice "audio/_pristine/voice/cage/skeptic/20.flac"
                    #skeptic "And? We were stuck, and now we're not. You're welcome.\n"
                    label cage_woods_cheated_expl_join:
                        voice "audio/_pristine/voice/cage/cheated/8.flac"
                        cheated "And you don't think we're stuck now? We're still in a cage, it's just bigger.\n"
                        voice "audio/_pristine/voice/cage/hero/10a.flac"
                        hero "You know, if you think about it, isn't life just a really big cage?\n"
                        #voice "audio/_pristine/voice/cage/hero/10.flac"
                        #hero "If you think about it, isn't life a cage?\n"
                        #voice "audio/_pristine/voice/cage/narrator/16.flac"
                        #n "Enough! What's done is done, and you're here now. There's no use arguing. Just get to the cabin and settle this.\n"
                        voice "audio/_pristine/voice/cage/narrator/16a.flac"
                        n "Oh don't you start philosophizing! Just get to the cabin and settle this already!\n"
                elif trait_broken:
                    label cage_woods_broken_join:
                        voice "audio/_pristine/voice/cage/broken/6.flac"
                        broken "I don't think we were happy. I don't think we can be happy here.\n"
                        voice "audio/_pristine/voice/cage/skeptic/21.flac"
                        skeptic "Oh, so now you're on team 'dying was good?' Took you long enough.\n"
                        #voice "audio/_pristine/voice/cage/broken/7.flac"
                        #broken "No, dying was still bad. Dying is always bad. But now we have a chance to put things to rest. We just need to talk to her, which means we need you to stop steering us off course.\n"
                        jump cage_woods_sigh_join
                elif trait_paranoid:
                    voice "audio/_pristine/voice/cage/paranoid/6a.flac"
                    paranoid "We killed ourself. Obviously. You were insisting that we were happy, but we knew we weren't. We could see right through you.\n"
                    voice "audio/_pristine/voice/cage/skeptic/22.flac"
                    skeptic "Yeah, what he said. We weren't about to be stuck somewhere, being fed nonstop bullshit forever. We want answers, and we weren't gonna find them in your fake little paradise.\n"
                    voice "audio/_pristine/voice/cage/narrator/17.flac"
                    n "There are no answers to find! If she was dead, then that was it, that was the solution. All you managed to do was reset the board, and you put the pieces back all wrong while you were at it. This is probably worse for you, if I had to guess.\n"
                    voice "audio/_pristine/voice/cage/skeptic/23.flac"
                    skeptic "Ha. So there is a board.\n"
                    label cage_woods_sigh_join:
                        voice "audio/_pristine/voice/cage/narrator/18.flac"
                        n "{i}Sigh{/i}. Well, what's done is done, and you're here now. There's no use arguing. Just get to the cabin and settle this. Try not to kill yourself this time.\n"
                jump cage_woods_menu

        "{i}• (Explore) I was happy with eternal bliss last time.{/i}" if prisoner_happy_seen and cage_woods_last_time_comment == False:
            $ cage_woods_last_time_comment = True
            voice "audio/_pristine/voice/cage/narrator/19.flac"
            n "Eternal bliss? But you wouldn't have found eternal bliss unless you actually killed her.\n"
            if trait_broken:
                voice "audio/_pristine/voice/cage/narrator/20.flac"
                n "Or if she... killed herself? Now that I think about it I do seem to recall you saying something to that effect. I suppose that wasn't a joke, then.\n"
                voice "audio/_pristine/voice/cage/narrator/21.flac"
                n "You said she cut her own head off, didn't you?\n"
                voice "audio/_pristine/voice/cage/hero/11.flac"
                hero "Yeah, it was awful.\n"
                voice "audio/_pristine/voice/cage/narrator/22.flac"
                n "Well, as little sense as that makes, I have to ask, why are you here?! You shouldn't have died! You should be enjoying your reward.\n"
                #n "Well, as little sense as that makes, I have to ask, why are you still here?! You shouldn't be dead! You should be enjoying your reward.\n"
                jump cage_woods_explain_join
            else:
                voice "audio/_pristine/voice/cage/hero/12.flac"
                hero "Actually, she killed herself. Cut her own head off. It was awful.\n"
                voice "audio/_pristine/voice/cage/skeptic/24.flac"
                skeptic "It was convenient. Too convenient.\n"
                jump cage_woods_head_cut_join


        "{i}• (Explore) I'm not taking the blade again. [[Toss your weapon into the woods.]{/i}" if blade_held and cage_woods_blade_toss_attempt == False and cage_woods_blade_explore:
            voice "audio/_pristine/voice/cage/narrator/23.flac"
            n "Are you serious?! The blade is your implement. You're going to need it if you want to do things right.\n"
            if trait_broken:
                voice "audio/_pristine/voice/cage/broken/8.flac"
                broken "Do it. She can't talk to us at knife-point. That's no way to get a real conversation started.\n"
            if trait_paranoid:
                voice "audio/_pristine/voice/cage/paranoid/7a.flac"
                paranoid "We can't toss it! It's the only way we can protect ourself. It's an extension of us, and we shouldn't go around throwing our pieces away.\n"
                voice "audio/_pristine/voice/cage/skeptic/25.flac"
                skeptic "He's right. Weird, but right. Don't. You. Dare.\n"
            elif trait_cheated:
                voice "audio/_pristine/voice/cage/cheated/9.flac"
                cheated "You know what? Yeah. Screw this! We won't play along with any of you!\n"
            if trait_broken or trait_cheated:
                voice "audio/_pristine/voice/cage/skeptic/26.flac"
                skeptic "You're all being ridiculous. Why would we disarm ourselves at a time like this?! Don't. You. Dare.\n"
            label cage_woods_blade_toss_menu:
                default cage_woods_blade_toss_attempt = False
                menu:
                    extend ""

                    "{i}• [[Do it. Toss the blade.]{/i}" if cage_woods_blade_toss_attempt == False:
                        $ cage_woods_blade_toss_attempt = True
                        voice "audio/_pristine/voice/cage/skeptic/27.flac"
                        skeptic "Are you even listening to me? Does my opinion count for nothing?! We're never getting out of here if you don't listen! I'm intervening, we're not tossing the blade.\n"
                        if trait_broken:
                            voice "audio/_pristine/voice/cage/broken/9.flac"
                            broken "You don't have to listen to him. He hasn't gotten us anywhere.\n"
                        menu:
                            extend ""

                            "{i}• I'm in charge, and I say we're tossing the blade. You had your chance last time, and we all saw how that worked out for us.{/i}":
                                if trait_paranoid:
                                    voice "audio/_pristine/voice/cage/skeptic/28.flac"
                                    skeptic "Too bad. This is a mutiny.\n"
                                    voice "audio/_pristine/voice/cage/hero/_extra1a.flac"
                                    hero "Hey, you can't just do that! We're not supposed to be able to make our own decisions.\n"
                                    if prisoner_delayed_knife_comment:
                                        voice "audio/_pristine/voice/cage/skeptic/_extra1.flac"
                                        skeptic "Yeah? Well I did it last time.\n"
                                    voice "audio/_pristine/voice/cage/hero/_extra2b.flac"
                                    hero "What if I stop you? Maybe I can make choices too.\n"
                                    voice "audio/_pristine/voice/cage/skeptic/_extra2.flac"
                                    skeptic "Good luck with that. I've got backup this time, haven't I?\n"
                                    voice "audio/_pristine/voice/cage/paranoid/_extra1a.flac"
                                    paranoid "Yeah! Alliance of convenience! We're not throwing it away. It's important!\n"
                                    play audio "audio/one_shot/new/STP_strangershuffle_5.flac"
                                    voice "audio/_pristine/voice/cage/hero/_extra3.flac"
                                    hero "Hey, what are you— Are you serious? That's no fair, let me go!\n"
                                    voice "audio/_pristine/voice/cage/paranoid/_extra2a.flac"
                                    paranoid "Sorry! Has to be done.\n"
                                    #voice "audio/_pristine/voice/cage/hero/_extra4.flac"
                                    #hero "{i}Sigh.{/i} Sorry. I'd love to help, but I think my hands are tied on this one.\n"
                                    #voice "audio/_pristine/voice/cage/skeptic/_extra3.flac"
                                    #skeptic "Thatta boy. Trust us. We've got all our best interests at heart.\n"

                                    #voice "audio/_pristine/voice/cage/skeptic/28.flac"
                                    #skeptic "Too bad. This is a mutiny.\n"
                                    #voice "audio/_pristine/voice/cage/paranoid/8.flac"
                                    #paranoid "We're just trying to help. This blade keeps us safe, it gives us options. If someone tries to pull our strings, we'll be able to cut them. You understand?\n"
                                    #voice "audio/_pristine/voice/cage/hero/13.flac"
                                    #hero "Sorry. Feels like my hands are tied on this.\n"
                                    $ config.menu_include_disabled = True
                                    menu:
                                        extend ""

                                        "{i}• Are you seriously not letting me toss it?{/i}" if tower_false_choice:
                                            $ config.menu_include_disabled = False

                                        "{i}• Real mature.{/i}" if tower_false_choice:
                                            $ config.menu_include_disabled = False

                                        "{i}• When this goes sideways, it's on the two of you.{/i}" if tower_false_choice:
                                            $ config.menu_include_disabled = False

                                        "{i}• Fine. Then I guess we're keeping it.{/i}":
                                            $ config.menu_include_disabled = False
                                            voice "audio/_pristine/voice/cage/skeptic/29.flac"
                                            skeptic "Great. Was that so hard? We need to keep our wits {i}sharp{/i}.\n"
                                            voice "audio/_pristine/voice/cage/paranoid/9a.flac"
                                            paranoid "Yes. You've made the right choice. The blade is the only control we have in this world.\n"
                                            voice "audio/_pristine/voice/cage/narrator/24.flac"
                                            n "Yes, great. Now will you get to the cabin already? In case you've forgotten, the Princess, the fate of the entire world, et cetera et cetera.\n"
                                            jump cage_woods_menu

                                play secondary "audio/final/Razor_SwordSwish_1.flac"
                                queue secondary "audio/_pristine/sfx/blade_bounce_distant.flac"
                                $ blade_held = False
                                $ default_mouse = "default"
                                $ cage_blade_thrown = True
                                voice "audio/_pristine/voice/cage/narrator/25.flac"
                                n "Without another word, you foolishly hurl your only chance at victory far off into the woods, never to be seen again.\n"
                                voice "audio/_pristine/voice/cage/skeptic/30.flac"
                                skeptic "Never to be seen again? All we did was toss it into the woods, there's nothing stopping us from picking it back up.\n"
                                voice "audio/_pristine/voice/cage/narrator/26.flac"
                                n "Oh, but there is something stopping you from picking it back up: the fact that you already made your decision. As much as I'd like to turn back the clock, we'll all just have to suffer the consequences of what you've done. That's how decisions work.\n"
                                #voice "audio/_pristine/voice/cage/skeptic/31.flac"
                                #skeptic "That's nonsense. That's not how physical space works.\n"
                                #voice "audio/_pristine/voice/cage/narrator/27.flac"
                                #n "It's unfortunately the reality of the situation. The blade is gone, so you'd better figure out some other way to slay the Princess, or every single person in the world is going to die.\n"
                                if trait_broken:
                                    voice "audio/_pristine/voice/cage/broken/10.flac"
                                    broken "You did the right thing.\n"
                                else:
                                    voice "audio/_pristine/voice/cage/cheated/10.flac"
                                    cheated "Huh. That felt... good. Best thing we've done in ages. Whatever this bullshit world throws at us next, we'll always have this tiny victory.\n"
                                jump cage_woods_menu

                            "{i}• Fine. Have it your way. I'll keep it.{/i}":
                                jump cage_wood_blade_keep_join

                    "{i}• Fine. Have it your way. I'll keep it.{/i}":
                        label cage_wood_blade_keep_join:
                            $ cage_woods_blade_toss_attempt = True
                            if trait_broken:
                                voice "audio/_pristine/voice/cage/broken/11.flac"
                                broken "I did my best to warn you.\n"
                                voice "audio/_pristine/voice/cage/skeptic/32.flac"
                                skeptic "Good. We need to keep our wits {i}sharp{/i}.\n"
                            if trait_paranoid:
                                voice "audio/_pristine/voice/cage/paranoid/10.flac"
                                paranoid "Good. This blade keeps us safe, it gives us options. If someone tries to pull our strings, we'll be able to cut them.\n"
                                #voice "audio/_pristine/voice/cage/skeptic/33.flac"
                                #skeptic "At least we're on the same page. We have to keep our wits {i}sharp{/i}.\n"
                            voice "audio/_pristine/voice/cage/narrator/24.flac"
                            n "Yes, great. Now will you get to the cabin already? In case you've forgotten, the Princess, the fate of the entire world, et cetera et cetera.\n"
                        jump cage_woods_menu

        "{i}• No way out but through. Let's go see her. [[Proceed to the cabin.]{/i}":
            jump cage_cabin_exterior

        "{i}• [[Silently proceed to the cabin.]{/i}":
            jump cage_cabin_exterior

        "{i}• I'm done with this. Bye! [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
            if loops_finished >= 2:
                $ mound_can_attempt_flee = False
                voice "audio/voices/mound/bonus/flee.flac"
                mound "You have already committed to my completion. You cannot go further astray.\n"
                jump cage_woods_menu
            play audio "audio/one_shot/footsteps_hike_short.flac"
            $ caught_origin_current = "cage"
            $ caught_origin_ch3 = True
            voice "audio/_pristine/voice/cage/narrator/28.flac"
            $ quick_menu = False
            hide farback onlayer farback
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            scene farback cage woods onlayer farback at zoom_in, flip, Position(ypos=1125)
            show bg cage woods onlayer back at zoom_in, flip, Position(ypos=1125)
            show mid cage woods onlayer front at zoom_in, flip, Position(ypos=1125)
            show fore cage woods onlayer inyourface at zoom_in, flip, Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "Are you serious?! Fine. You walk away from the the cabin. Let's see how that goes for you.\n"

            jump caught_start

label cage_cabin_exterior:
    $ gallery_cage.unlock_item(2)
    $ renpy.save_persistent()
    play audio "audio/one_shot/footsteps_hike_short.flac"
    $ quick_menu = False
    hide farback onlayer farback
    hide bg onlayer back
    hide mid onlayer front
    hide fore onlayer inyourface
    with fade
    show farback cage cabin ext onlayer farback at Position(ypos=1125)
    show bg cage cabin ext onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/_pristine/voice/cage/narrator/29.flac"
    n "You stand at the edge of a cliff. An abyss yawns beneath you, empty and endless, the only path forward a rusted metal bridge. The cabin looms on its far side. I think you already know what waits for you within.\n"
    if trait_broken:
        voice "audio/_pristine/voice/cage/broken/12.flac"
        broken "It's dreary, but of course it is. We're dreary. And so is she.\n"
    if trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/11.flac"
        cheated "Great. A creaky old bridge and a bottomless ravine. Because getting to the cabin was too easy last time. I wonder what other sick jokes are waiting for us. Maybe that ravine doesn't even go anywhere! It'd be par for the course if we slipped and wound up falling forever.\n"
    if trait_paranoid:
        voice "audio/_pristine/voice/cage/paranoid/11a.flac"
        paranoid "It's like the world itself doesn't want us to reach her.\n"
    voice "audio/_pristine/voice/cage/skeptic/34.flac"
    skeptic "There's nothing to find out here. Time to check in with the missus.\n"
    voice "audio/_pristine/voice/cage/narrator/30.flac"
    n "I'm going to pretend you didn't just call her that.\n"
    menu:

        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            stop sound
            $ quick_menu = False
            play audio "audio/one_shot/door_bedroom.flac"
            hide farback onlayer farback
            hide bg onlayer back
            scene bg black
            with fade
            play sound "audio/_pristine/sfx/Cage_AMB Cabin Metal_1_loop.flac" loop
            play secondary "audio/_pristine/sfx/Cage_AMB metal world_6_loop.flac" loop
            scene farback cage cabin int onlayer farback at Position(ypos=1125, xpos=1025)
            show bg cage cabin int onlayer back at Position(ypos=1125, xpos=1025)
            show mirror cage cabin int p onlayer back at Position(ypos=1125, xpos=1025)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            jump cage_cabin


label cage_cabin:

    $ gallery_cage.unlock_item(3)
    $ renpy.save_persistent()
    default prisoner_mirror_interact = False
    if prisoner_1_cabin_mirror_ask or prisoner_1_cabin_mirror_approached:
        $ prisoner_mirror_interact = True
    voice "audio/_pristine/voice/cage/narrator/31b.flac"
    n "Every surface of the cabin is draped in chains, the air filled with the mock birdsong of metallic clinks. Where there should be walls, you can see only endless ropes of metal, with hooks dangling from their ends. A fitting cage for a monster destined to end the world.\n" id cage_cabin_a125c597
    if blade_held:
        voice "audio/_pristine/voice/cage/narrator/32.flac"
        n "There's nothing for you to do but step forward into the basement. You already have your weapon. Your objective awaits.\n"
    else:
        voice "audio/_pristine/voice/cage/narrator/33.flac"
        n "There's nothing for you to do but step forward into the basement. You already foolishly threw away your weapon. But still, your objective awaits.\n"

    if prisoner_mirror_interact == False:
        voice "audio/_pristine/voice/cage/hero/14a.flac"
        hero "And how are we supposed to get to the basement? I don't see a way down. All I see is a mirror.\n"

    if prisoner_mirror_interact:
        if trait_cheated:
            voice "audio/_pristine/voice/cage/cheated/12.flac"
            cheated "Oh, not the damn mirror again. I hate the mirror. It gets us nowhere!\n"
            voice "audio/_pristine/voice/cage/narrator/34.flac"
            n "'The... mirror'—\n"
            voice "audio/_pristine/voice/cage/cheated/13.flac"
            cheated "'What mirror? There is no mirror. Why would I lie about there being a mirror?' Whose fucking idea was this? It's awful.\n"
            voice "audio/_pristine/voice/cage/skeptic/35.flac"
            skeptic "I'm sure whoever put it there put it there for a reason. It's obviously important. It has to be.\n"

        else:
            voice "audio/_pristine/voice/cage/skeptic/36.flac"
            skeptic "Huh. That mirror's back again. Why?\n"
            voice "audio/_pristine/voice/cage/narrator/35.flac"
            n "What mirror? There is no mirror. The only thing of note here is the door to the basement.\n"
            if trait_broken:
                #voice "audio/_pristine/voice/cage/skeptic/37.flac"
                #skeptic "Don't you lie to us again! It's right there!\n"
                voice "audio/_pristine/voice/cage/broken/13a.flac"
                broken "It doesn't matter. What are we going to do, look at ourself? I've had enough introspection.\n"
                voice "audio/_pristine/voice/cage/skeptic/38.flac"
                skeptic "But it does matter! It's obviously important. It has to be. Otherwise it wouldn't be here.\n" id cage_cabin_5bdae8ff
            if trait_paranoid:
                #voice "audio/_pristine/voice/cage/paranoid/12.flac"
                #paranoid "Oh, shut up, will you? We can all see it there, plain as day, right in front of us! Just like we could all see it last time.\n"
                voice "audio/_pristine/voice/cage/skeptic/39.flac"
                skeptic "It clearly serves some purpose, but... what? Is there something about us we're supposed to see? Can it be a tool of some kind?\n"
                voice "audio/_pristine/voice/cage/paranoid/13a.flac"
                paranoid "Or is it a distraction? Something meant to confuse us?\n"
                voice "audio/_pristine/voice/cage/hero/15.flac"
                hero "Can we please stop talking about the mirror? I'd rather not spend more time in this room than I have to. It's creepy.\n"


    else:
        voice "audio/_pristine/voice/cage/narrator/35.flac"
        n "What mirror? There is no mirror. The only thing of note here is the door to the basement.\n"
        if trait_cheated:
            voice "audio/_pristine/voice/cage/cheated/14.flac"
            cheated "Oh, don't you lie to us! We can trust our eyes, and I am {i}not{/i} going to stand around arguing over a stupid mirror.\n"
        if trait_broken:
            #voice "audio/_pristine/voice/cage/skeptic/37.flac"
            #skeptic "Don't you lie to us! It's right there!\n"
            voice "audio/_pristine/voice/cage/broken/13.flac"
            broken "It doesn't matter. What are we going to do, look at ourself? I've had enough introspection, I want to see someone else. I want to see her.\n"
            voice "audio/_pristine/voice/cage/skeptic/38.flac"
            skeptic "But it does matter! It's obviously important. It has to be. Otherwise it wouldn't be here.\n" id cage_cabin_5bdae8ff_1
        if trait_paranoid:
            #voice "audio/_pristine/voice/cage/paranoid/14.flac"
            #paranoid "Oh, shut up, will you? We can all see it there, plain as day, right in front of us!\n"
            voice "audio/_pristine/voice/cage/skeptic/39.flac"
            skeptic "It clearly serves some purpose, but... what? Is there something about us we're supposed to see? Can it be a tool of some kind?\n"
            voice "audio/_pristine/voice/cage/paranoid/13a.flac"
            paranoid "Or is it a distraction? Something meant to confuse us?\n"
            voice "audio/_pristine/voice/cage/hero/15.flac"
            hero "Can we please stop talking about the mirror? I'd rather not spend more time in this room than I have to. It's creepy.\n"
    if trait_paranoid == False:
        voice "audio/_pristine/voice/cage/narrator/36.flac"
        n "{i}Sigh{/i}. I'm not going to waste time arguing with you. Just get to the basement, okay? The door's on the other side of the room.\n"
        voice "audio/_pristine/voice/cage/hero/16.flac"
        hero "Then I guess there's nowhere for us to go but forward.\n"

    menu:
        extend ""

        "{i}• [[Approach the mirror.]{/i}":
            jump cage_stairs_start



label cage_stairs_start:
    stop music
    #scene farback cage cabin int onlayer farback at cage_zoom
    show bg cage cabin int onlayer back at cage_zoom
    show mirror cage cabin int p onlayer back at cage_zoom
    voice "audio/_pristine/voice/cage/narrator/37.flac"
    play audio "audio/_pristine/sfx/Cage Step Chain falling_1.flac"

    n "You step out onto the floor. Or what should have been a floor.\n"
    voice "audio/_pristine/voice/cage/hero/17a.flac"
    hero "Should have been?\n"
    voice "audio/_pristine/voice/cage/narrator/38.flac"
    play tertiary "audio/_pristine/sfx/Cage_chain floor breaks fall LONG_2.flac"
    play audio "audio/_pristine/sfx/Cage Step Chain falling_9.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide mirror onlayer back
    scene bg black
    n "Yes, unfortunately. You realize, too late, that there is no floor beneath the metal. There is only a loose web of chains suspended over some unseen space. An unseen space that you are now rapidly plummeting through.\n"
    if trait_broken:
        voice "audio/_pristine/voice/cage/broken/14.flac"
        play tertiary "audio/final/Nightmare_Falling_1_Loop.flac" loop
        show farback cage falling onlayer farback at sway, Position(ypos=1125)
        show bg cage fall onlayer back at cage_big_sway, Position(ypos=1125)
        show mid cage fall onlayer front at sway, Position(ypos=1125)
        show fore cage fall onlayer inyourface at cage_sway, Position(ypos=1125)
        with fade
        broken "She's bringing us back to her.\n"
        voice "audio/_pristine/voice/cage/skeptic/40.flac"
        skeptic "Or we just happened to fall through an unstable floor. She's a prisoner here, how much agency do you think she has?\n"
        voice "audio/_pristine/voice/cage/broken/15.flac"
        broken "More than you'd like, I'm sure.\n"
    if trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/15.flac"
        play tertiary "audio/final/Nightmare_Falling_1_Loop.ogg" loop
        show farback cage falling onlayer farback at sway, Position(ypos=1125)
        show bg cage fall onlayer back at cage_big_sway, Position(ypos=1125)
        show mid cage fall onlayer front at sway, Position(ypos=1125)
        show fore cage fall onlayer inyourface at cage_sway, Position(ypos=1125)
        with fade
        cheated "Now this is just absolute bullshit. Can't even walk across a room now without being plunged into an abyss!\n"
        voice "audio/_pristine/voice/cage/skeptic/41.flac"
        skeptic "You're too emotional. It makes us sloppy. We have to focus on details right now, and we can't focus on details if you're raging about every little thing that happens.\n"
        voice "audio/_pristine/voice/cage/hero/18.flac"
        hero "Are we supposed to focus on details while we're falling into a bottomless pit?\n"
        voice "audio/_pristine/voice/cage/skeptic/42.flac"
        skeptic "Don't be ridiculous, it obviously has a bottom!\n"
    if trait_paranoid:
        voice "audio/_pristine/voice/cage/paranoid/15a.flac"
        play tertiary "audio/final/Nightmare_Falling_1_Loop.ogg" loop
        show farback cage falling onlayer farback at sway, Position(ypos=1125)
        show bg cage fall onlayer back at cage_big_sway, Position(ypos=1125)
        show mid cage fall onlayer front at sway, Position(ypos=1125)
        show fore cage fall onlayer inyourface at cage_sway, Position(ypos=1125)
        with fade
        paranoid "Nothing's solid here, is it? It's all just a shifting mass waiting for us to drop our guard.\n"
        #voice "audio/_pristine/voice/cage/skeptic/43.flac"
        #skeptic "That doesn't mean it isn't dictated by rules. And as soon as we figure them out, all of this nonsense is finally going to click. I'm sure! It has to!\n"


label cage_basement_start:

    $ quick_menu = False
    play audio "audio/_pristine/sfx/cage_fall_broken.flac"
    stop tertiary
    hide farback onlayer farback
    hide bg onlayer back
    hide mid onlayer front
    hide fore onlayer inyourface
    scene bg black
    voice "audio/_pristine/voice/cage/narrator/39.flac"

    n "Your fall is suddenly, painfully halted as rusty chains pull taut against your skin, their hooks digging into your muscle.\n"
    play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
    voice "audio/_pristine/voice/cage/narrator/40.flac"
    show bg cage encounter onlayer farback at swayblur, Position(ypos=1125)
    show cage reveal onlayer farback at swayblur, Position(ypos=1125)
    show mid cage encounter onlayer back at swayblur, Position(ypos=1125)
    if blade_held:
        show player cage encounter blade onlayer front at cage_blur, Position(ypos=1125)
    else:
        show player cage encounter onlayer front at cage_blur, Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You find yourself suspended in what appears to be a vast, dark space, the glinting of yet more chains merely hinting at its full dimensions. You dangle a few feet off the bare concrete floor.\n"
    voice "audio/_pristine/voice/cage/narrator/41.flac"
    n "If the Princess lives here, slaying her would probably be doing her a favor.\n"
    $ gallery_cage.unlock_item(4)
    $ renpy.save_persistent()
    voice "audio/_pristine/voice/cage/narrator/42.flac"
    play music "audio/_pristine/music/cage/A Prison of Flesh Loop.flac" loop
    hide bg onlayer farback
    hide cage onlayer farback
    hide mid onlayer back
    hide player onlayer front
    show bg cage encounter onlayer farback at sway, Position(ypos=1125)
    show cage reveal onlayer farback at sway, Position(ypos=1125)
    show mid cage encounter onlayer back at sway, Position(ypos=1125)
    if blade_held:
        show player cage encounter blade onlayer front at cage_sway, Position(ypos=1125)
    else:
        show player cage encounter onlayer front at cage_sway, Position(ypos=1125)
    with dissolve
    n "As your eyes adjust to your new surroundings, you make out a figure standing in the gloom, obscured in shadow. She watches you with the stillness of the grave.\n"
    voice "audio/_pristine/voice/cage/skeptic/44.flac"
    skeptic "Easy now. We don't know what sort of situation we're dealing with. We should let her make the first move. Let observation give us an advantage.\n"
    menu:
        extend ""

        "{i}• ''Hello?''{/i}":
            jump cage_basement_second_menu

        "{i}• ''Are you mad at me?''{/i}":
            jump cage_basement_second_menu

        "{i}• ''So you can come back too.''{/i}":
            jump cage_basement_second_menu

        "{i}• ''Look, I'm sorry about what happened last time. I'm... supposed to be sorry, right?''{/i}":
            jump cage_basement_second_menu

        "{i}• ''Why the hell did you cut your head off?''{/i}":
            jump cage_basement_second_menu

        "{i}• [[Attack her.]{/i}" if blade_held:
            play audio "audio/final/Adversary_StabCut_9.flac"
            $ cage_action = True
            jump cage_encounter_start

        #"{i}• [[Push yourself to your feet.]{/i}":
        #    $ cage_action = True
        #    jump cage_encounter_start

        "{i}• [[Wait for her to make the first move.]{/i}":
            jump cage_second_menu_response

label cage_basement_second_menu:
    voice "audio/_pristine/voice/cage/narrator/43.flac"
    play audio "audio/_pristine/sfx/Cage_body dangling hooks_2.flac"
    n "But you are met with only silence, save for the creaks and groans of metal as it sways in the stale air around you. The hooks slowly shift in your skin, the pain coming in waves as you continue to dangle helplessly.\n"

    if trait_broken:
        voice "audio/_pristine/voice/cage/broken/16a.flac"
        broken "She won't even speak to us. We did this.\n"
        #voice "audio/_pristine/voice/cage/skeptic/45.flac"
        #skeptic "If you think about it, He did this. If He hadn't decided to intervene to begin with, I'm sure we could have had this all sorted by now!\n"
        #voice "audio/_pristine/voice/cage/broken/17.flac"
        #broken "We aren't in that reality, though, are we? We're here, where the decisions have been made. The only way forward is to fix it. We need to get her to talk to us.\n"
    if trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/16.flac"
        cheated "Screw this. This is making me bloody anxious. It's like... it's like she knows how unfair this all is, and now she's having fun with it! She's mocking us.\n"
        voice "audio/_pristine/voice/cage/hero/19.flac"
        hero "By not saying anything?\n"
        voice "audio/_pristine/voice/cage/cheated/17.flac"
        cheated "Yes!\n"
    if trait_paranoid:
        voice "audio/_pristine/voice/cage/paranoid/16.flac"
        paranoid "What if the chains don't have to be real? What if they aren't real?\n"
        voice "audio/_pristine/voice/cage/skeptic/46.flac"
        skeptic "Augh, they feel plenty real to me! Yeah, it would be nice if we could just tell ourselves the chains aren't lodged in all our joints and they'd magically go away, but I'm afraid that's wishful thinking.\n"
        #if cage_woods_blade_toss_attempt:
        default paranoid_can_free_cage = False
        $ paranoid_can_free_cage = True
        voice "audio/_pristine/voice/cage/paranoid/17a.flac"
        paranoid "Well maybe wishful thinking is what we need. Maybe they're real but maybe... maybe we can cut through them.\n"
        #voice "audio/_pristine/voice/cage/paranoid/17.flac"
        #paranoid "Well maybe wishful thinking is what we need. Maybe they're real but maybe... maybe we can cut through them. Remember what I said about strings?\n"
        voice "audio/_pristine/voice/cage/hero/20.flac"
        hero "It's... worth a try.\n"
        #else:
        #    paranoid "Shit. Shit!\n"

    menu:
        extend ""

        "{i}• (Explore) ''Hello?''{/i}":
            jump cage_second_menu_response

        "{i}• (Explore) ''I'm talking to you.''{/i}":
            jump cage_second_menu_response

        "{i}• (Explore) ''I'm sorry, okay? I'm sorry!''{/i}":
            jump cage_second_menu_response

        "{i}• (Explore) ''Look, I'm sorry about what happened last time. I'm... supposed to be sorry, right?''{/i}":
            jump cage_second_menu_response

        "{i}• (Explore) ''Screw it.'' [[Attack her.]{/i}" if blade_held:
            $ cage_action = True
            voice "audio/_pristine/voice/cage/skeptic/47.flac"
            skeptic "What? But she's so far away.\n"
            voice "audio/_pristine/voice/cage/narrator/44.flac"
            play audio "audio/final/Adversary_StabCut_9.flac"
            n "And you're bound. You do your best to swing your blade arm towards the Princess. But, unsurprisingly, the act gets you nowhere.\n"
            jump cage_encounter_start

        "{i}• (Explore) [[Try to slip free.]{/i}" if paranoid_can_free_cage == False:
            default cage_action = False
            play audio "audio/final/Adversary_StabCut_9.flac"
            $ cage_action = True
            jump cage_encounter_start

        "{i}• (Explore) [[Try to cut yourself free.]{/i}" if paranoid_can_free_cage:
            default cage_cut_route = False
            $ cage_cut_route = True
            voice "audio/_pristine/voice/cage/narrator/45.flac"
            play audio "audio/one_shot/new/STP_swordscrape_1.flac"
            show player cage cutting onlayer front at cage_sway
            with Dissolve(1.0)
            n "You clumsily rotate the blade in your palm, pressing it against the chains lodged in your wrist.\n"
            voice "audio/_pristine/voice/cage/paranoid/18.flac"
            paranoid "And it slices through them, right? Right?\n"
            voice "audio/_pristine/voice/cage/hero/21.flac"
            hero "Y-yeah, what he said. It slices through!\n"
            voice "audio/_pristine/voice/cage/skeptic/48.flac"
            skeptic "Now hold on. Let's not rush to conclusions. How would that ever work?\n"
            voice "audio/_pristine/voice/cage/paranoid/19.flac"
            paranoid "It just does?\n"
            voice "audio/_pristine/voice/cage/narrator/46.flac"
            n "It doesn't.\n"
            voice "audio/_pristine/voice/cage/paranoid/20.flac"
            paranoid "Maybe the only reason it isn't working is because {i}someone{/i} doesn't believe we can do it!\n"
            #voice "audio/_pristine/voice/cage/paranoid/20a.flac"
            #paranoid "Maybe the only reason it's not working is because you're holding us back.\n"
            voice "audio/_pristine/voice/cage/skeptic/49.flac"
            skeptic "They're metal chains, and nothing we've done has worked so far. Maybe if you gave me a good reason to believe we should try again, I'd believe it was worth trying again. But until then, I'm going to believe our eyes. This isn't getting us anywhere.\n"
            voice "audio/_pristine/voice/cage/paranoid/21a.flac"
            paranoid "Erm... you should believe it because you... should? We don't have anything better to do!\n" id cage_basement_second_menu_ecad3bb6
            #voice "audio/_pristine/voice/cage/skeptic/50.flac"
            #skeptic "No.\n"
            voice "audio/_pristine/voice/cage/hero/22.flac"
            hero "Um, um... maybe they're... rusty. He did say they were rusty, didn't he?\n"
            voice "audio/_pristine/voice/cage/skeptic/51.flac"
            skeptic "He did, didn't he? All right, I'm game. We cut again.\n"
            voice "audio/_pristine/voice/cage/narrator/47a.flac"
            play tertiary "audio/final/chain_break_low.flac"
            show player cage arm free onlayer front at cage_sway
            with dissolve
            n "You bring your blade against the chains again, and this time you manage to cut into the metal. Its hook remains embedded in your flesh, but your arm falls from the mass of chains, free from the Princess' bindings.\n"
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
            voice "audio/_pristine/voice/cage/hero/23.flac"
            hero "Yes! Will you look at that.\n"
            voice "audio/_pristine/voice/cage/skeptic/52.flac"
            skeptic "That... worked?\n"
            voice "audio/_pristine/voice/cage/paranoid/22.flac"
            paranoid "And why shouldn't the rest be the same, then?\n"
            jump cage_encounter_start

        "{i}• (Explore) [[Remain silent.]{/i}":
            jump cage_second_menu_response

    label cage_second_menu_response:
        play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
        jump cage_encounter_start

    label cage_action_join:
        if cage_cut_route == False:
            voice "audio/_pristine/voice/cage/narrator/48.flac"
            n "As you attempt to writhe your way free, the Princess takes a confident step forward, chains rattling behind her.\n"

label cage_encounter_start:
    default cage_strangle_count = 0
    if cage_cut_route:
        voice "audio/_pristine/voice/cage/narrator/49.flac"
        play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
        play tertiary "audio/final/Witch_TreeWrap_4.flac"
        show bg cage encounter onlayer farback at swayblur
        show cage approach 1 onlayer farback at swayblur
        show mid cage encounter onlayer back at swayblur
        show player cage arm free onlayer front at cage_blur
        with dissolve
        n "But before you can make much progress, the Princess takes a step forward. As she moves, the heavy chains shift, tightening and tearing at your flesh, your joints screaming in agony as the rusted hooks dig deeper. Stars dance in your eyes as the chain wrapped around your neck threatens to choke you.\n"
    elif cage_action:
        voice "audio/_pristine/voice/cage/narrator/50.flac"
        play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
        play tertiary "audio/final/Witch_TreeWrap_4.flac"
        show bg cage encounter onlayer farback at swayblur
        show cage approach 1 onlayer farback at swayblur
        show mid cage encounter onlayer back at swayblur
        if blade_held:
            show player cage encounter blade onlayer front at cage_blur
        else:
            show player cage encounter onlayer front at cage_blur
        with dissolve
        n "As you attempt to move, the Princess takes a slow step forward. As she does so, the heavy chains shift, tightening and tearing at your flesh, your joints screaming in agony as the rusted hooks dig deeper. Stars dance in your eyes as the chain wrapped around your neck threatens to choke you.\n"
    else:
        voice "audio/_pristine/voice/cage/narrator/51.flac"
        play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
        play tertiary "audio/final/Witch_TreeWrap_4.flac"
        show bg cage encounter onlayer farback at swayblur
        show cage approach 1 onlayer farback at swayblur
        show mid cage encounter onlayer back at swayblur
        if blade_held:
            show player cage encounter blade onlayer front at cage_blur
        else:
            show player cage encounter onlayer front at cage_blur
        with dissolve
        n "The Princess takes a slow step forward. As she does so, the heavy chains shift, tightening and tearing at your flesh, your joints screaming in agony as the rusted hooks dig deeper. Stars dance in your eyes as the chain wrapped around your neck threatens to choke you.\n"
    voice "audio/_pristine/voice/cage/narrator/52.flac"
    hide bg onlayer farback
    hide cage onlayer farback
    hide mid onlayer back
    hide player onlayer front
    show bg cage encounter onlayer farback at sway, Position(ypos=1125)
    show cage approach 1 onlayer farback at sway, Position(ypos=1125)
    show mid cage encounter onlayer back at sway, Position(ypos=1125)
    if cage_cut_route:
        show player cage arm free onlayer front at cage_sway, Position(ypos=1125)
    elif blade_held:
        show player cage encounter blade onlayer front at cage_sway, Position(ypos=1125)
    else:
        show player cage encounter onlayer front at cage_sway, Position(ypos=1125)
    with Dissolve(1.0)
    n "As your vision comes back into focus, your eyes fall on the body of the Princess, finally emerged from the shadows.\n"
    voice "audio/_pristine/voice/cage/hero/24.flac"
    hero "'The body of the Princess' is a weird way to describe a person.\n"
    voice "audio/_pristine/voice/cage/narrator/53.flac"
    n "It's only accurate. The form in front you is a body. Draped in raiments of chains, her head dragging along behind her in an iron cage.\n"
    voice "audio/_pristine/voice/cage/narrator/54.flac"
    n "The head stares up at you, but says nothing. And the chains squeeze ever tighter.\n"
    if trait_broken:
        voice "audio/_pristine/voice/cage/skeptic/53.flac"
        skeptic "So much for talking it out. Doesn't seem like she's too interested, does it?\n"
        if blade_held:
            voice "audio/_pristine/voice/cage/hero/25.flac"
            hero "We still have that blade! Maybe there's something we can do to get out of this.\n"
            voice "audio/_pristine/voice/cage/broken/19.flac"
            broken "What good would it do us? We should have gotten rid of it. She'll never trust us now, not after everything we've done.\n"
        else:
            voice "audio/_pristine/voice/cage/broken/20.flac"
            broken "It's not too late. You threw away that blade for a reason. Now talk to her.\n"
    if trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/18b.flac"
        cheated "Oh, we're being strangled already? You haven't given us a chance to do a damned thing. What's the point of any of this if we don't even get to make a single choice?\n"
        voice "audio/_pristine/voice/cage/narrator/55a.flac"
        n "I'm not here to 'give you chances.' I'm here to set the stage, and to dictate to you what happens. I can advise you on the correct course of action, but there are limits to my direct involvement. The 'choices,' if that's what you'd like to call them, have always been yours.\n"
        #voice "audio/_pristine/voice/cage/narrator/55.flac"
        #n "I'm not here to 'give you chances.' I'm here to set the stage, and to dictate to you what happens. The 'choices,' if that's what you'd like to call them, have always been yours.\n"
        voice "audio/_pristine/voice/cage/skeptic/54.flac"
        skeptic "A riddle while we're dying, isn't that just like you? Now to figure out what exactly you mean by 'choices'...\n"
        voice "audio/_pristine/voice/cage/hero/26.flac"
        hero "Oh, for the love of— STOP THINKING AND DO SOMETHING!\n"
    if trait_paranoid:
        if cage_cut_route:
            voice "audio/_pristine/voice/cage/paranoid/23.flac"
            paranoid "Just keep going. She's a head in a cage. We're not going to be able to talk our way out of this. The only thing we can do is keep sawing our way to freedom.\n"
        #else:
        #    voice "audio/_pristine/voice/cage/paranoid/24.flac"
        #    paranoid "Everything here is an enemy. She's an enemy, He's an enemy, the world's an enemy... are we... are we also an enemy?\n"
            #voice "audio/_pristine/voice/cage/skeptic/55.flac"
            #skeptic "Pull yourself together! Of course we can't be our own enemy. We're trying to get out of here, and we will get out of here as soon as you all let me focus.\n"
    default cage_1_silence = False
    default cage_1_help = False
    default cage_no_blade_mentioned = False
    menu:
        extend ""

        "{i}• (Explore) ''What is your problem with me? I've only ever tried to help you.''{/i}":
            $ cage_1_help = True
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_2.flac"
            voice "audio/_pristine/voice/cage/princess/1a.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 1 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "What makes you think I have a problem with you? Because I'm a head in a cage? Don't be silly. That's what I've always been.\n"
            voice "audio/_pristine/voice/cage/princess/2.flac"
            sp "It's not like you're any different.\n"

        "{i}• (Explore) ''Let me down! Killing me isn't going to fix anything.''{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_2.flac"
            voice "audio/_pristine/voice/cage/princess/3.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 1 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "In another life I would have said it was cute that you think I have a say here. I don't have a say. Neither do you. You of all people should know that.\n"

        "{i}• (Explore) ''Look, I didn't even bring a knife. I just wanted to talk to you.''{/i}" if blade_held == False:
            $ cage_no_blade_mentioned = True
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_2.flac"
            voice "audio/_pristine/voice/cage/princess/4.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 1 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "You're pleading with me as if I have a say over anything that happens here. Shouldn't you know by now that I don't?\n"
            voice "audio/_pristine/voice/cage/princess/5.flac"
            sp "And neither do you.\n"

        "{i}• (Explore) ''What... happened to you?''{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_2.flac"
            voice "audio/_pristine/voice/cage/princess/6.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 1 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "Nothing happened. I think I've always been like this. Outside of everything. A helpless observer to the things that are done to me.\n"
            voice "audio/_pristine/voice/cage/princess/7.flac"
            sp "The only difference is that my eyes are finally open.\n"

        "{i}• (Explore) ''You cut your own head off last time. You can't be mad at me about that!''{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_2.flac"
            voice "audio/_pristine/voice/cage/princess/8a.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 1 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "Mad at you? I'm not mad at you. I know you didn't have anything to do with that. Not outside of your designated role, of course.\n"
            #voice "audio/_pristine/voice/cage/skeptic/56.flac"
            #skeptic "'Designated role?' What, like we're actors? Wouldn't that be convenient. Then we could just kill the director and be done with it.\n"

        "{i}• (Explore) [[Attempt to cut yourself free.]{/i}" if blade_held and cage_cut_route == False:
            voice "audio/_pristine/voice/cage/narrator/58.flac"
            play tertiary "audio/final/Adversary_StabCut_9.flac"
            queue tertiary "audio/one_shot/STP_knifle cobblestone single_1.flac"
            n "You try to move your arm, but the hooks buried deep in your wrist and elbow keep you firmly, painfully, in place. You do your best to rotate the knife in your palm, but it only clinks against the metal chain, unable to so much as leave a scratch.\n"

        "{i}• (Explore) [[Swing your blade.]{/i}" if blade_held:
            voice "audio/_pristine/voice/cage/narrator/59.flac"
            play audio "audio/final/Adversary_StabCut_9.flac"
            n "You try to move your arm, but do little more than rotate the hook planted firmly in your wrist. It is an excruciating and fruitless attempt, which the Princess doesn't so much as acknowledge.\n"

        "{i}• (Explore) [[Keep cutting.]{/i}" if blade_held and cage_cut_route:
            default cage_cut_2 = False
            $ cage_cut_2 = True
            voice "audio/_pristine/voice/cage/paranoid/25.flac"
            play audio "audio/one_shot/new/STP_swordscrape_1.flac"
            show player cage cut 2 onlayer front at cage_sway
            with Dissolve(1.0)
            paranoid "Yes. The links are weak. They can't handle the strain. Isn't that right?\n"
            voice "audio/_pristine/voice/cage/narrator/56.flac"
            n "You know, it's rather annoying for you to dictate what I'm going to say next.\n"
            voice "audio/_pristine/voice/cage/skeptic/57.flac"
            skeptic "But is that what happens? Do the links break?\n"
            voice "audio/_pristine/voice/cage/narrator/57a.flac"
            play audio "audio/one_shot/new/STP_swordscrape_1.flac"
            play tertiary "audio/final/chain_break_low.flac"
            show player cage legs onlayer front at cage_sway
            with dissolve
            n "Yes. Luckily for you, they were too thoroughly rusted to hold much longer. Your other arm breaks free.\n"
            #voice "audio/_pristine/voice/cage/hero/27.flac"
            #hero "Whatever you're doing, keep doing it!\n"
            #voice "audio/_pristine/voice/cage/hero/27a.flac"
            #hero "Yes, yes yes! Keep going!\n"

        "{i}• (Explore) [[Remain silent.]{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_2.flac"
            $ cage_1_silence = True
            voice "audio/_pristine/voice/cage/hero/28.flac"
            hero "Are... you sure we don't want to say anything?\n"
            voice "audio/_pristine/voice/cage/skeptic/58.flac"
            skeptic "No, that's great! It's smart. We can't think our way out of this if we're talking.\n"
            if trait_broken:
                voice "audio/_pristine/voice/cage/broken/21.flac"
                broken "Thinking just closes us off. We can't get out of here alone, and she can't read our mind.\n"
                #voice "audio/_pristine/voice/cage/broken/21a.flac"
                #broken "Silence just closes us off. We can't get out of here alone, and she can't read our mind.\n"
            if trait_paranoid:
                voice "audio/_pristine/voice/cage/paranoid/26a.flac"
                paranoid "We're just wasting time. She has the complete upper hand, and we're just letting ourselves dangle here until she's done with us. Then what do you think will happen? Do you want to die again?!\n"
                voice "audio/_pristine/voice/cage/skeptic/59.flac"
                skeptic "Quiet! You're not helping. I can do this, I just need to concentrate.\n"
            if trait_cheated:
                voice "audio/_pristine/voice/cage/cheated/19.flac"
                cheated "Yeah, because thinking our way out of things has worked for us. Ever.\n"
                #voice "audio/_pristine/voice/cage/skeptic/60.flac"
                #skeptic "You've been no help at all. Why don't you come up with something to do instead of just grousing?\n"
                #voice "audio/_pristine/voice/cage/cheated/20.flac"
                #cheated "Sure. I say we let her kill us. See how {i}you{/i} like dying against {i}your{/i} will. Plus, maybe we can respawn with better stuff next time. Oh, like a sword maybe...\n"

    jump cage_menu_2_start

label cage_menu_2_start:

    voice "audio/_pristine/voice/cage/narrator/60.flac"
    play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
    play tertiary "audio/final/Witch_TreeWrap_4.flac"
    show bg cage encounter onlayer farback at swayblur
    show cage approach 2 onlayer farback at swayblur
    show mid cage encounter onlayer back at swayblur
    if cage_cut_2:
        show player cage legs onlayer front at cage_blur
    elif cage_cut_route:
        show player cage arm free onlayer front at cage_blur
    elif blade_held:
        show player cage approach 2 blade onlayer front at cage_blur
    else:
        show player cage approach 2 onlayer front at cage_blur
    with Dissolve(1.0)
    n "The body takes another step towards you, the chains around you tightening, the hooks boring deeper into your flesh. They constrict dangerously around your throat. You find it harder to breathe.\n"
    voice "audio/_pristine/voice/cage/princess/9.flac"
    hide bg onlayer farback
    hide cage onlayer farback
    hide mid onlayer back
    hide player onlayer front
    show bg cage encounter onlayer farback at sway, Position(ypos=1125)
    show cage approach 2 onlayer farback at sway, Position(ypos=1125)
    show mid cage encounter onlayer back at sway, Position(ypos=1125)
    if cage_cut_2:
        show player cage legs onlayer front at cage_sway, Position(ypos=1125)
    elif cage_cut_route:
        show player cage arm free onlayer front at cage_sway, Position(ypos=1125)
    elif blade_held:
        show player cage approach 2 blade onlayer front at cage_sway, Position(ypos=1125)
    else:
        show player cage approach 2 onlayer front at cage_sway, Position(ypos=1125)
    with Dissolve(1.0)
    sp "I don't think she's happy you're here. But what do I know? I'm just a set of eyes and ears. I don't make choices. At least not any that matter.\n"
    #voice "audio/_pristine/voice/cage/hero/29.flac"
    #hero "What the hell is she talking about? She's going to kill us! After everything we've been through, she's going to kill us. Again!\n"
    if trait_paranoid:
        if cage_cut_2:
            voice "audio/_pristine/voice/cage/paranoid/27a.flac"
            paranoid "She won't kill us if we just... keep... cutting. We just have to get our neck free.\n"
        else:
            voice "audio/_pristine/voice/cage/hero/29a.flac"
            hero "I don't want to die like this. I don't want to die like this! Somebody do something before she kills us! ... Please!\n"
            voice "audio/_pristine/voice/cage/paranoid/28a.flac"
            paranoid "We're stuck here! What are any of us supposed to do? Reason with her? I don't think she's acting rationally! I think she's lost it!\n"
    elif trait_broken:
        voice "audio/_pristine/voice/cage/broken/22a.flac"
        broken "The poor thing... she thinks it's easier to be detached. But buried pain is still pain, whether she knows it or not.\n"
    if trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/21.flac"
        cheated "Oh, well isn't that just {i}convenient{/i}?\n"
        voice "audio/_pristine/voice/cage/skeptic/61a.flac"
        skeptic "It makes sense to me. She's a severed head. What control could she possibly have over her body? There's no connections. No nerves. Huh. So bodies can work on their own.\n"
        voice "audio/_pristine/voice/cage/cheated/22a.flac"
        cheated "You know, I wouldn't mind that actually. Maybe when the chain pops our useless head off, we'll get to run around without it!\n"
    if cage_cut_2 == False:
        voice "audio/_pristine/voice/cage/narrator/61.flac"
        n "This was all doomed from the start, wasn't it?\n"
    menu:
        extend ""

        "{i}• [[Cut yourself free.]{/i}" if cage_cut_2:
            default cage_cut_3 = False
            $ cage_cut_3 = True
            voice "audio/_pristine/voice/cage/narrator/62.flac"
            play audio "audio/one_shot/new/STP_swordscrape_1.flac"
            show player cage cut 3 onlayer front at cage_sway
            with dissolve
            n "You continue your efforts, furiously working to sever the chain strangling your neck.\n"
            voice "audio/_pristine/voice/cage/princess/10a.flac"
            sp "Look at you scurry. As if anything you do is going to change the outcome. Don't you get it? This is all the same.\n"

        "{i}• (Explore) ''None of this is my fault. I haven't done anything to you except give you my weapon, twice.''{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
            voice "audio/_pristine/voice/cage/princess/11.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 2 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "And when the time comes, you'll 'give it to me' again, and then she'll do something horrible with it. I wonder what it'll be this time.\n"

        "{i}• (Explore) '''She?' Are you talking about your body as if it's a separate person? It's you.''{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
            voice "audio/_pristine/voice/cage/princess/12.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 2 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "That's what I used to think, but time alone has taught me the truth. I'm not my body. I'm just the thing that watches it.\n"
            voice "audio/_pristine/voice/cage/princess/13a.flac"
            sp "There's so much pain that comes from tricking yourself into thinking you have a choice. But none of us have choices. And knowing that has made me feel so... free.\n"

        "{i}• (Explore) ''Nothing that's happened to you is my fault. Again, I keep trying to help you.''{/i}" if cage_1_help:
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
            voice "audio/_pristine/voice/cage/princess/14.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 2 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "And where has all that trying gotten us? I'm still here. And now I'm a head, dragged along by a tired body. And you're just as stuck as I am.\n"

        "{i}• (Explore) ''What do you mean, you're just a watcher? You cut your own head off last time. You made that decision.''{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
            voice "audio/_pristine/voice/cage/princess/15.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 2 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "What's the point of making a choice if it all ends the same way? I'm still stuck, and you're just as stuck as I am.\n"

        "{i}• (Explore) ''You've made choices. And you've never stopped. You're choosing violence right now.''{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
            voice "audio/_pristine/voice/cage/princess/16.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 2 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "You're not looking at things right. Your eyes are fixed on the distraction, instead of on the hand working the illusion.\n"
            voice "audio/_pristine/voice/cage/skeptic/62.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 2 onlayer farback at sway
            show mid cage encounter onlayer back at sway
            skeptic "I see... you know, maybe she's on to something, maybe being a head means you can really focus on figuring out the {i}truth{/i}.\n"
            voice "audio/_pristine/voice/cage/narrator/63.flac"
            n "Oh, don't you start!\n"

        "{i}• (Explore) [[Drop the blade.]{/i}" if blade_held:
            voice "audio/_pristine/voice/cage/princess/17.flac"
            $ blade_held = False
            $ default_mouse = "default"
            play audio "audio/one_shot/knife_bounce_several.flac"
            if cage_cut_route == False:
                show player cage approach 2 onlayer front at cage_sway, Position(ypos=1125)
            with dissolve
            sp "You're a step ahead of me. That means you finally get it. I'm happy for you. I really am.\n"

        "{i}• (Explore) [[Say nothing.]{/i}":
            play audio "audio/_pristine/sfx/Cage_body dangling hooks_1.flac"
            voice "audio/_pristine/voice/cage/princess/18.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 2 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "Silence. Then maybe you finally get it.\n"

label cage_decap_menu_3:
    voice "audio/_pristine/voice/cage/princess/19.flac"
    show bg cage encounter onlayer farback at sway
    show cage approach 2 talk onlayer farback at sway
    show mid cage encounter onlayer back at sway
    with Dissolve(0.5)
    sp "Everything we witness is just another shade of the same, endless cycle. I wake up in chains.\n"
    if cage_cut_3:
        voice "audio/_pristine/voice/cage/narrator/64.flac"
        play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
        play tertiary "audio/one_shot/new/STP_swordscrape_1.flac"
        show bg cage encounter onlayer farback at swayblur
        show cage approach 3 onlayer farback at swayblur
        show mid cage encounter onlayer back at swayblur
        show player cage cut 3 onlayer front at cage_blur
        with dissolve
        n "The body steps forward. Your bindings tighten again, but you've almost sawn through the first layer of links.\n"
    else:
        voice "audio/_pristine/voice/cage/narrator/65.flac"
        play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
        play tertiary "audio/final/Witch_TreeWrap_3.flac"
        show bg cage encounter onlayer farback at swayblur
        show cage approach 3 onlayer farback at swayblur
        show mid cage encounter onlayer back at swayblur
        if cage_cut_2:
            show player cage legs onlayer front at cage_blur
        elif cage_cut_route:
            show player cage arm free onlayer front at cage_blur
        elif blade_held:
            show player cage approach 3 blade onlayer front at cage_blur
        else:
            show player cage approach 3 onlayer front at cage_blur
        with dissolve
        n "The body steps forward. Your bindings tighten again.\n"
    voice "audio/_pristine/voice/cage/princess/20.flac"
    hide bg onlayer farback
    hide cage onlayer farback
    hide mid onlayer back
    hide player onlayer front
    show bg cage encounter onlayer farback at sway, Position(ypos=1125)
    show cage approach 3 talk onlayer farback at sway, Position(ypos=1125)
    show mid cage encounter onlayer back at sway, Position(ypos=1125)
    if cage_cut_3:
        show player cage cut 3 onlayer front at cage_sway, Position(ypos=1125)
    elif cage_cut_2:
        show player cage legs onlayer front at cage_sway, Position(ypos=1125)
    elif cage_cut_route:
        show player cage arm free onlayer front at cage_sway, Position(ypos=1125)
    elif blade_held:
        show player cage approach 3 blade onlayer front at cage_sway, Position(ypos=1125)
    else:
        show player cage approach 3 onlayer front at cage_sway, Position(ypos=1125)
    with dissolve
    sp "You come to me, knife in hand.\n"
    if cage_blade_thrown:
        show bg cage encounter onlayer farback at sway, Position(ypos=1125)
        show cage approach 3 onlayer farback at sway, Position(ypos=1125)
        show mid cage encounter onlayer back at sway, Position(ypos=1125)
        if cage_cut_3:
            show player cage cut 3 onlayer front at cage_sway, Position(ypos=1125)
        elif cage_cut_2:
            show player cage legs onlayer front at cage_sway, Position(ypos=1125)
        elif cage_cut_route:
            show player cage arm free onlayer front at cage_sway, Position(ypos=1125)
        elif blade_held:
            show player cage approach 3 blade onlayer front at cage_sway, Position(ypos=1125)
        else:
            show player cage approach 3 onlayer front at cage_sway, Position(ypos=1125)
        with dissolve
        jump cage_free_menu
    if cage_cut_3:
        voice "audio/_pristine/voice/cage/narrator/66.flac"
        play tertiary "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
        play audio "audio/final/chain_break_low.flac"
        show bg cage encounter onlayer farback at swayblur
        show cage approach 4 onlayer farback at swayblur
        show mid cage encounter onlayer back at swayblur
        show player cage legs onlayer front at cage_blur
        with dissolve
        n "The body steps forward as the first links break, but the pressure on your neck is becoming unbearable.\n"
        voice "audio/_pristine/voice/cage/paranoid/29.flac"
        play audio "audio/one_shot/new/STP_swordscrape_1.flac"
        show player cage cut 3 onlayer front at cage_blur, Position(ypos=1125)
        with dissolve
        paranoid "Come on, come on, come on!\n"
    else:
        voice "audio/_pristine/voice/cage/narrator/67.flac"
        play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
        play tertiary "audio/final/Witch_TreeWrap_4.flac"
        show bg cage encounter onlayer farback at swayblur
        show cage approach 4 onlayer farback at swayblur
        show mid cage encounter onlayer back at swayblur
        if cage_cut_2:
            show player cage legs onlayer front at cage_blur
        elif cage_cut_route:
            show player cage arm free onlayer front at cage_blur
        elif blade_held:
            show player cage approach 4 knife onlayer front at cage_blur
        else:
            show player cage approach 4 onlayer front at cage_blur
        with dissolve
        n "The body steps forward. The pressure on your limbs is becoming unbearable.\n"
    voice "audio/_pristine/voice/cage/princess/21.flac"
    hide bg onlayer farback
    hide cage onlayer farback
    hide mid onlayer back
    hide player onlayer front
    show bg cage encounter onlayer farback at sway, Position(ypos=1125)
    show cage approach 4 talk onlayer farback at sway, Position(ypos=1125)
    show mid cage encounter onlayer back at sway, Position(ypos=1125)
    if cage_cut_3:
        show player cage cut 3 onlayer front at cage_sway, Position(ypos=1125)
    elif cage_cut_2:
        show player cage legs onlayer front at cage_sway, Position(ypos=1125)
    elif cage_cut_route:
        show player cage arm free onlayer front at cage_sway, Position(ypos=1125)
    elif blade_held:
        show player cage approach 4 knife onlayer front at cage_sway, Position(ypos=1125)
    else:
        show player cage approach 4 onlayer front at cage_sway, Position(ypos=1125)
    with dissolve
    sp "You give me your implement.\n"
    if cage_cut_3:
        jump cage_slay_join
    if blade_held:
        $ default_mouse = "default"
        $ blade_held = False
        voice "audio/_pristine/voice/cage/narrator/68.flac"
        play audio "audio/one_shot/knife_bounce_several.flac"
        play tertiary "audio/final/Witch_TreeWrap_4.flac"
        if cage_cut_route == False:
            show player cage approach 4 onlayer front at cage_sway
        with dissolve
        n "The pressure is finally too much. Your fist unfolds as your joints swell with trapped blood, and your pristine blade tumbles helplessly to the ground.\n"
    else:
        $ gallery_cage.unlock_item(5)
        $ renpy.save_persistent()
        voice "audio/_pristine/voice/cage/princess/22.flac"
        show bg cage encounter onlayer farback at sway
        show cage approach 4 talk onlayer farback at sway
        show mid cage encounter onlayer back at sway
        with dissolve
        sp "See? You already did that one.\n"
        voice "audio/_pristine/voice/cage/narrator/69.flac"
        show bg cage encounter onlayer farback at sway
        show cage approach 4 onlayer farback at sway
        show mid cage encounter onlayer back at sway
        with dissolve
        n "You begin to black out.\n"
    voice "audio/_pristine/voice/cage/princess/23.flac"
    show bg cage encounter onlayer farback at sway
    show cage approach 4 talk onlayer farback at sway
    show mid cage encounter onlayer back at sway
    with dissolve
    sp "I cut myself 'free.'\n"
    if trait_paranoid:
        voice "audio/_pristine/voice/cage/paranoid/30b.flac"
        show bg cage encounter onlayer farback at sway
        show cage approach 4 onlayer farback at sway
        show mid cage encounter onlayer back at sway
        with dissolve
        paranoid "Hahahaha. She's not insane, is she? No, she's... she's just right. It's all... it's all been the same, hahahaha, the whole time it's all been the same. We never had a say.\n"
        #voice "audio/_pristine/voice/cage/paranoid/30.flac"
        #paranoid "She's not insane. She's right. It's... all been the same, the whole time. We never had a say.\n"
    elif trait_broken:
        voice "audio/_pristine/voice/cage/broken/23.flac"
        show bg cage encounter onlayer farback at sway
        show cage approach 4 onlayer farback at sway
        show mid cage encounter onlayer back at sway
        with dissolve
        broken "She's right. We're trapped in a cycle. And I think it's too late for us to get out.\n"
    elif trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/23.flac"
        show bg cage encounter onlayer farback at sway
        show cage approach 4 onlayer farback at sway
        show mid cage encounter onlayer back at sway
        with dissolve
        cheated "Ahahahahahaha. Well at least she gets it. This whole damn thing's a pile of flaming bullshit and there's nothing we can do to put it out!\n"
    menu:
        extend ""

        "{i}• (Explore) ''I didn't want to take the knife with me. I was {b}forced{/b} to.''{/i}" if trait_paranoid and cage_woods_blade_toss_attempt:
            voice "audio/_pristine/voice/cage/princess/24.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 4 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "So you understand exactly how unfair this all is. Give in with me. None of this is up to us.\n"

        "{i}• (Explore) ''You're setting me up to fail. I can't make real choices strung up like this, and you're refusing to make any choices at all.''{/i}":
            voice "audio/_pristine/voice/cage/princess/25.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 4 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "You're just starting to see the walls. And you don't have to struggle against something inevitable. You can give in with me. None of this is up to us.\n"

        "{i}• (Explore) ''Us choosing the same moves every time we play isn't an indictment of anyone's free will. It's just how things happened to play out. I could have thrown away that knife in the woods if I wanted to. But I chose to come here with it.''{/i}" if cage_woods_blade_toss_attempt == False:
            voice "audio/_pristine/voice/cage/princess/26.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 4 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "Just because you refuse to see the walls doesn't mean they aren't there. Give in with me. It's so much easier to let the world happen to you.\n"

        "{i}• (Explore) ''What was I supposed to have done? Did you want me to carry your severed head out of the cabin with me? I thought you were {b}dead{/b}.''{/i}":
            voice "audio/_pristine/voice/cage/princess/27.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 4 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "That is what I wanted, but... you didn't do it. And I don't think you could have done it. The walls are what the walls are. So give in with me. None of this is up to us.\n"

        "{i}• (Explore) ''Please. Just stop walking forward. I'm going to die if you don't stop.''{/i}":
            voice "audio/_pristine/voice/cage/princess/28.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 4 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "We're both going to die. And dying won't stop us from doing this again. And again. And again.\n"
            voice "audio/_pristine/voice/cage/princess/29.flac"
            sp "It would be so much easier if you just gave in with me.\n"

        "{i}• (Explore) [[Say nothing.]{/i}":
            voice "audio/_pristine/voice/cage/princess/29.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 4 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "It would be so much easier if you just gave in with me.\n"
            jump cage_decapitated

label cage_decapitated:
    stop music
    play music "audio/final/fury_heart_loop.ogg" loop
    voice "audio/_pristine/voice/cage/narrator/70.flac"
    play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
    play tertiary "audio/final/Witch_TreeWrap_2.flac"
    show bg cage encounter onlayer farback at swayblur
    show cage approach 5 onlayer farback at swayblur
    show mid cage encounter onlayer back at swayblur
    if cage_cut_2:
        show player cage legs onlayer front at cage_blur
    elif cage_cut_route:
        show player cage arm free onlayer front at cage_blur
    else:
        show player cage approach 4 onlayer front at cage_blur
    show filter cage onlayer inyourface at Position(ypos=1125)
    with dissolve
    n "She steps forward yet again. And the chains dig into you, your nerves screaming, your heart pounding, your lungs desperate for air.\n"
    voice "audio/_pristine/voice/cage/hero/30.flac"
    hero "I don't think we can hold on to you much longer.\n"
    if trait_broken:
        voice "audio/_pristine/voice/cage/broken/24.flac"
        broken "I think we're about to break.\n"
    elif trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/24.flac"
        cheated "Like I said, the girl's right. This whole thing is rigged.\n"
    elif trait_paranoid:
        voice "audio/_pristine/voice/cage/paranoid/31.flac"
        paranoid "How many times will we have to do this? I'm tired.\n"
    #voice "audio/_pristine/voice/cage/narrator/71.flac"
    #n "Your vision swims.\n"
    #voice "audio/_pristine/voice/cage/skeptic/63.flac"
    #skeptic "No, no, no! Even if there's an underlying pattern, things have been different every time. We just have to work harder. There's a solution!\n"
    #voice "audio/_pristine/voice/cage/hero/31.flac"
    #hero "I think it's too late for that.\n"
    voice "audio/_pristine/voice/cage/princess/30.flac"
    show bg cage encounter onlayer farback at swayblur
    show cage approach 5 talk onlayer farback at swayblur
    show mid cage encounter onlayer back at swayblur
    sp "This is all getting so predictable, isn't it? Pop.{w=4.57}{nw}"
    show screen disableclick(0.5)
    stop music
    stop sound
    stop secondary
    stop tertiary
    play sound "audio/_pristine/sfx/cage_pop.flac"
    queue sound "audio/final/_prisoner_bounce.flac"
    queue sound "audio/_pristine/sfx/cage_chains_fall_pop.flac"
    $ default_mouse = "eye"
    hide bg onlayer farback
    hide cage onlayer farback
    hide mid onlayer back
    hide player onlayer front
    hide filter onlayer inyourface
    scene bg black
    truthmid "You're falling, the world is spinning. And then you hit the ground, your body light in a way that is sickeningly wrong, and roll to a stop. The sound of rattling chains and a heavy thud as the rest of what was once you falls to the ground somewhere nearby.\n"
    play sound "audio/_pristine/sfx/Cage_AMB Cabin Metal_1_loop.flac" fadein 5.0 loop
    play secondary "audio/_pristine/sfx/Cage_AMB metal world_6_loop.flac" fadein 5.0 loop
    scene bg cage pop onlayer farback at Position(ypos=1125)
    show mid cage pop onlayer farback at Position(ypos=1125)
    show cage pop begin onlayer farback at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(1.5)
    play tertiary "audio/one_shot/footstep_mines.flac"
    play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
    show cage pop approach onlayer farback
    with Dissolve(1.0)
    truth "You are unable to take action, unable to defend yourself, unable to even look around as the Princess' body steps towards you, one slow, rhythmic step after another.\n"
    play tertiary "audio/one_shot/footstep_mines.flac"
    play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
    show cage pop stoop onlayer farback
    with Dissolve(1.0)
    truth "It stoops down to pick you up and then—\n"
    $ gallery_cage.unlock_item(6)
    $ renpy.save_persistent()
    play audio "audio/one_shot/knife_pickup.flac"
    hide bg onlayer farback
    hide mid onlayer farback
    hide cage onlayer farback
    scene bg cage pop onlayer farback at Position(ypos=1125)
    show mid cage pop onlayer farback at Position(ypos=1125)
    show player cage stoop onlayer farback at Position(ypos=1125)
    show cage pop stoop onlayer farback at Position(ypos=1125)
    with Dissolve(0.5)
    truth "A shadow rises behind the body, blade glinting.\n"
    voice "audio/_pristine/voice/cage/princess/31.flac"
    show cage pop stoop talk onlayer farback
    with dissolve
    sp "And now, the cut.\n"
    play tertiary "audio/_pristine/sfx/cage_dropped.flac"
    #play audio "audio/_pristine/sfx/Fury Body Horror_3.flac"
    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
    hide player onlayer farback
    show cage pop fight start onlayer farback
    show head cage pop start onlayer farback at Position(ypos=1125)
    with fade
    truth "It strikes, and it strikes true, and the body drops its cage in pain.\n"
    play audio "audio/_pristine/sfx/cage_big_fight_sequence.flac"
    hide cage onlayer farback
    show panel1 cage pop fight onlayer farback at Position(ypos=1125)
    with Dissolve(1.0)
    truth "They descend on each other in a maelstrom of chains and hooks and feathers and blood, fighting their way deeper into the shadows until all you're left to witness are the sounds of violence.\n"
    voice "audio/_pristine/voice/cage/princess/32.flac"
    show head cage pop talk glance onlayer farback
    with dissolve
    sp "See? You only ever thought you were in control. Isn't it so much nicer to let go?\n"
    show head cage pop start onlayer farback
    play music "audio/_pristine/music/cage/An Open Door Intro.flac"
    queue music "audio/_pristine/music/cage/An Open Door Loop.flac" loop
    menu:
        extend ""

        "{i}• ''I didn't let go. You ripped my head off.''{/i}":
            voice "audio/_pristine/voice/cage/princess/33.flac"
            show head cage pop talk onlayer farback
            with dissolve
            sp "My body ripped your body's head off. I didn't have anything to do with it.\n"
            voice "audio/_pristine/voice/cage/princess/34.flac"
            show head cage pop talk glance onlayer farback
            with dissolve
            sp "You get it, it's not like you're responsible for what your body is doing to mine now. You and I just watch. Like we've been doing since the beginning.\n"

        "{i}• ''What are we supposed to do now?''{/i}":
            voice "audio/_pristine/voice/cage/princess/35.flac"
            show head cage pop talk glance onlayer farback
            with dissolve
            sp "We watch. Just like we've been doing since the beginning.\n"

        "{i}• ''You didn't cut yourself free. My body is still the one with the knife. Doesn't that mean this is different? Doesn't that mean I broke your pattern?''{/i}":
            voice "audio/_pristine/voice/cage/princess/36.flac"
            show head cage pop joke talk onlayer farback
            with dissolve
            sp "Huh. I guess you're right. Pattern must be wrong then.\n"
            voice "audio/_pristine/voice/cage/princess/37.flac"
            show head cage pop talk glance onlayer farback
            with dissolve
            sp "Maybe if we keep watching, we'll figure it out. And we've got nothing else to do but watch.\n"

        "{i}• ''This isn't nicer! I'm a severed head.''{/i}":
            voice "audio/_pristine/voice/cage/princess/38.flac"
            show head cage pop talk glance onlayer farback
            with dissolve
            sp "And what's wrong with that? It's really not that different from how it's always been. Just watching things play out. It's who we are. Only now we can be honest with ourselves.\n"

        "{i}• ''I thought that would be the end of me. I guess this isn't so bad.''{/i}":
            voice "audio/_pristine/voice/cage/princess/39.flac"
            show head cage pop talk glance onlayer farback
            with dissolve
            sp "I told you. It really isn't. And now nothing's stopping you from enjoying the show.\n"

        "{i}• [[Say nothing.]{/i}":
            truth "You say nothing, and the Princess smiles with a knowing silence.\n"

    play audio "audio/_pristine/sfx/Cage_chain crushing windpipe_4.flac"
    show head cage pop start onlayer farback
    show panel2 cage pop fight onlayer back at Position(ypos=1125)
    with dissolve
    truth "And so you and the Princess watch as your bodies weave in and out of the shadows, performing their lethal dance.\n"
    voice "audio/_pristine/voice/cage/princess/40.flac"
    show head cage pop talk glance onlayer farback
    with dissolve
    sp "Look at us go. Aren't we beautiful?\n"
    play audio "audio/_pristine/sfx/Cage Step Chain Fast_1.flac"
    play tertiary "audio/final/Razor_SwordHitSword_1.flac"
    queue tertiary "audio/final/Razor_SwordHitDrag_7.flac"
    queue tertiary "audio/final/Razor_ImpaleSwordBody_6.flac"
    show head cage pop start onlayer farback
    show panel3 cage pop fight onlayer front at Position(ypos=1175, xpos=825)
    with dissolve
    truth "The movement is gorgeous, primal, uninhibited. Steel crashing against steel and flesh rolling off of flesh.\n"
    voice "audio/_pristine/voice/cage/princess/41.flac"
    show head cage pop talk glance onlayer farback
    with dissolve
    sp "It's all going to come to a head soon.\n"
    show head cage pop start onlayer farback
    with dissolve
    sp "...\n"
    voice "audio/_pristine/voice/cage/princess/42.flac"
    show head cage pop joke talk onlayer farback
    with dissolve
    sp "Hah. Head.\n"
    stop music
    play audio "audio/_pristine/sfx/double_lethal.flac"
    hide panel1 onlayer farback
    hide panel2 onlayer back
    hide panel3 onlayer front
    show head cage pop start onlayer farback
    show panel4 cage pop fight onlayer inyourface at Position(ypos=1125)
    with dissolve
    truth "And at last, the climax plays out. Your body, wreathed in chains and shadows, makes its final move, but so does hers. Chain shatters spine and blade pierces heart.\n"
    #voice "audio/_pristine/voice/cage/princess/43.flac"
    #show head cage pop talk onlayer farback
    #with dissolve
    #sp "You know, from the right angle, this is kind of romantic.\n"
    voice "audio/_pristine/voice/cage/princess/44.flac"
    show head cage pop talk glance onlayer farback
    with dissolve
    sp "I guess I'll see you next time.\n"
    stop sound fadeout 30.0
    stop secondary fadeout 30.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
    play audio "audio/_pristine/sfx/double_collapse.flac"
    hide panel1 onlayer farback
    hide panel2 onlayer back
    hide panel3 onlayer front
    hide panel4 onlayer inyourface
    hide head onlayer farback
    show fight final cage pop onlayer farback at Position(ypos=1125)
    show quiet creep1 onlayer farback at Position(ypos=1125)
    show head cage pop start onlayer farback at Position(ypos=1125)
    with Dissolve(1.5)
    truth "Both hers and yours collapse, their dance complete.\n"
    show quiet creep2 onlayer farback
    show head cage pop cough onlayer farback
    with Dissolve(1.0)
    truth "Blood drips from the Princess' mouth, and she coughs.\n"
    $ gallery_cage.unlock_item(7)
    $ gallery_cage.unlock_item(8)
    $ gallery_cage.unlock_item(9)
    $ gallery_cage.unlock_item(10)
    $ renpy.save_persistent()
    voice "audio/_pristine/voice/cage/princess/45.flac"
    show quiet creep3 onlayer farback
    show head cage pop cold talk onlayer farback
    with dissolve
    sp "It's cold, but that's always been us, hasn't it? Cold isn't bad.\n"
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    hide head onlayer farback
    show hands cage pop 1 onlayer farback at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.75)
    show hands cage pop 2 onlayer farback at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.75)
    show hands cage pop 3 onlayer farback at Position(ypos=1125)
    with Dissolve(0.5)
    $ renpy.pause(0.5)
    show hands cage pop 4 onlayer farback at Position(ypos=1125)
    with Dissolve(0.4)
    $ renpy.pause(0.4)
    show hands cage pop 5 onlayer farback at Position(ypos=1125)
    with Dissolve(0.3)
    $ renpy.pause(0.3)
    show hands cage pop 6 onlayer farback at Position(ypos=1125)
    with Dissolve(0.2)
    $ renpy.pause(0.2)
    hide hands onlayer farback at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.125)
    $ blade_held = False
    $ default_mouse = "default"

    hide quiet onlayer farback
    hide bg onlayer farback
    hide fight onlayer farback
    hide mid onlayer farback
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
        truth "You do not get the chance to respond. Something has ripped her from you, and it's left something else in her place.\n"
    $ achievement.grant("ACH_CAGE_TRAP")
    $ cage_end = "stuck"
    $ current_princess = "cage"
    $ princess_kept += 1
    menu:
        extend ""

        "{i}• [[Say nothing.]{/i}":
            $ blade_held = False
            $ default_mouse = "default"
            hide mirror onlayer back
            show content m empty onlayer front at Position(ypos=1125)
            show mirror frame onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            truth "You approach the mirror.\n"
            menu:
                extend ""
                "{i}• [[Gaze into your reflection.]{/i}":
                    show player mirror onlayer front at Position(ypos=1125)
                    with dissolve

            jump mirror_sort
    # END


## THIS IS WHERE THE SPLIT HAPPENS
label cage_free_menu:
    if cage_no_blade_mentioned == False:
        voice "audio/_pristine/voice/cage/hero/32.flac"
        hero "But that's not right. We didn't bring the knife.\n"
    else:
        voice "audio/_pristine/voice/cage/hero/33a.flac"
        hero "But that's not right. We didn't bring the knife. We even told her that earlier!\n"
    #voice "audio/_pristine/voice/cage/skeptic/64.flac"
    #skeptic "Yeah, you made us toss it in the woods. Ha! Was that actually a good idea? We have an edge now.\n"
    #if trait_broken:
    #    voice "audio/_pristine/voice/cage/broken/25a.flac"
    #    broken "You thinking everything's 'an edge' is exactly how we got here. Sometimes the harder you push, the worse things get.\n"
    #    voice "audio/_pristine/voice/cage/skeptic/65b.flac"
    #    skeptic "Yeah? Well most of the time you have to push hard to actually get somewhere.\n"
    #elif trait_cheated:
    #    voice "audio/_pristine/voice/cage/cheated/25a.flac"
    #    cheated "Are you daft? It just means she's wrong. Do you actually think we can use 'logic' and 'reason' to convince her not to kill us? Do you really think that would work?\n"
    #    voice "audio/_pristine/voice/cage/skeptic/66.flac"
    #    skeptic "I mean... it'd work on me.\n"
    #    voice "audio/_pristine/voice/cage/hero/34.flac"
    #    hero "Have you all forgotten about the part where we're being strangled to death by a bunch of chains? Maybe we save the arguing for {i}after{/i} we get out.\n"
        #voice "audio/_pristine/voice/cage/cheated/26.flac"
        #cheated "Or maybe for after we inevitably die!\n"
        #voice "audio/_pristine/voice/cage/hero/35.flac"
        #hero "Yeah. Sure. Fine. Save it for woods, then!\n"
    menu:
        extend ""

        "{i}• ''Yeah, is that right? I bring you the knife? Where do you think it is?''{/i}":
            voice "audio/_pristine/voice/cage/princess/46.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 3 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "It's obviously right in your—\n"
            voice "audio/_pristine/voice/cage/princess/47.flac"
            sp "It's gone, isn't it? But that's not right.\n"

        "{i}• ''You clearly weren't listening to me earlier, because I already told you I threw away that knife. I ditched it before I even got to the cabin.''{/i}" if cage_no_blade_mentioned:
            voice "audio/_pristine/voice/cage/princess/48.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 3 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "Oh. Yeah. You did say that.\n"

        "{i}• ''There's no grand scheme guiding us along a predetermined path. We're both agents of chaos who make our own choices. And this time, I chose to talk to you. Unarmed.''{/i}":
            jump cage_free_penultimate_default_join

        "{i}• ''Your pattern's broken. I'm unarmed.''{/i}":
            label cage_free_penultimate_default_join:
                voice "audio/_pristine/voice/cage/princess/49.flac"
                show bg cage encounter onlayer farback at sway
                show cage approach 3 talk onlayer farback at sway
                show mid cage encounter onlayer back at sway
                with dissolve
                sp "But that's not right. That's not the reality I've been looking at.\n"
                voice "audio/_pristine/voice/cage/princess/50.flac"
                sp "You shouldn't have been able to do that.\n"

        "{i}• [[Silently wave your empty hands.]{/i}":
            default cage_free_silent_wave = False
            $ cage_free_silent_wave = True
            voice "audio/_pristine/voice/cage/princess/51.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 3 talk onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "No knife. But that's not right.\n"


label cage_free_final_menu:

    voice "audio/_pristine/voice/cage/narrator/72.flac"
    play audio "audio/_pristine/sfx/Cage Step Chain Slow_1.flac"
    show bg cage encounter onlayer farback at sway
    show cage approach 3 confused onlayer farback at sway
    show mid cage encounter onlayer back at sway
    with dissolve
    n "The body marching towards you comes to a lurching stop.\n"
    #if cage_free_silent_wave == False:
    #    voice "audio/_pristine/voice/cage/princess/52.flac"
    #    sp "Huh. She stopped. What is that supposed to mean? Has she been listening to you?\n"
    #else:
    voice "audio/_pristine/voice/cage/princess/53.flac"
    show bg cage encounter onlayer farback at sway
    show cage approach 3 introspection talk onlayer farback at sway
    show mid cage encounter onlayer back at sway
    with dissolve
    sp "Huh. She stopped. What is that supposed to mean?\n"
    show bg cage encounter onlayer farback at sway
    show cage approach 3 confused onlayer farback at sway
    show mid cage encounter onlayer back at sway
    with dissolve
    menu:
        extend ""

        "{i}• ''You've been the one listening to me. You made yourself stop. And now you can decide to finally let me down.''{/i}":
            label cage_final_default_join:
                voice "audio/_pristine/voice/cage/princess/54.flac"
                show bg cage encounter onlayer farback at sway
                show cage approach 3 confused onlayer farback at sway
                show mid cage encounter onlayer back at sway
                with dissolve
                sp "You make it sound so easy, but it can't be that easy. Not after all that violent repetition.\n"

        "{i}• ''What do you actually want? The only way we can get out of here is if you drop your guard. Just like I did.''{/i}":
            jump cage_final_default_join

        "{i}• ''I think you know what it's supposed to mean.''{/i}":
            voice "audio/_pristine/voice/cage/princess/55.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 3 confused onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "What? Like the answer's obvious? Like it's staring me right in the face? Just like you?\n"

        "{i}• ''Well? Are you ready to talk?''{/i}":
            voice "audio/_pristine/voice/cage/princess/56.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 3 confused onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "And is talking supposed to fix our problems? Is talking supposed to end all the violent repetition?\n"

        "{i}• [[Say nothing.]{/i}":
            voice "audio/_pristine/voice/cage/princess/57.flac"
            show bg cage encounter onlayer farback at sway
            show cage approach 3 confused onlayer farback at sway
            show mid cage encounter onlayer back at sway
            with dissolve
            sp "You're staring at me like the answer is self-evident. But it can't be. Not after all that violent repetition.\n"

    stop music
    voice "audio/_pristine/voice/cage/princess/58.flac"
    show bg cage encounter onlayer farback at sway
    show cage approach 3 introspection talk onlayer farback at sway
    show mid cage encounter onlayer back at sway
    with dissolve
    p "Oh.\n"
    voice "audio/_pristine/voice/cage/narrator/73a.flac"
    stop sound
    stop secondary
    stop tertiary
    play tertiary "audio/_pristine/sfx/cage_chains_fall_pop.flac"
    $ quick_menu = False
    hide bg onlayer farback
    hide cage onlayer farback
    hide mid onlayer back
    hide player onlayer front
    hide filter onlayer inyourface
    scene bg black
    with fade
    play sound "audio/_pristine/sfx/Cage_AMB Cabin Metal_1_loop.flac" fadein 5.0 loop
    play secondary "audio/_pristine/sfx/Cage_AMB metal world_6_loop.flac" fadein 5.0 loop
    show cg cage free start onlayer back at Position(ypos=1125)
    with fade
    $ renpy.pause(1.5)
    play audio "audio/one_shot/chain_1.flac"
    show cg cage free kneel onlayer back
    with Dissolve(0.5)
    if persistent.quick_menu:
        $ quick_menu = True
    voice sustain
    n "Suddenly, the chains loosen, the hooks sliding from your skin. You come crashing to the floor. And as the chains rain down around you, her body falls, too.\n"
    $ gallery_cage.unlock_item(11)
    $ renpy.save_persistent()
    voice "audio/_pristine/voice/cage/narrator/74.flac"
    play audio "audio/_pristine/sfx/cage_open.flac"
    show cg cage free open onlayer back
    with Dissolve(1.0)
    n "The room settles into comforting silence. No more rattling of chains, no more slow, deliberate footsteps from the Princess' body. Only the soft click of the latch as it opens the door of the cage.\n"
    play music "audio/_pristine/music/cage/An Open Door Intro.flac"
    queue music "audio/_pristine/music/cage/An Open Door Loop.flac" loop
    voice "audio/_pristine/voice/cage/princess/59.flac"
    show cg cage free open talk onlayer back
    with dissolve
    p "So that's... really all it took?\n"

    if trait_broken:
        voice "audio/_pristine/voice/cage/skeptic/67.flac"
        show cg cage free open onlayer back
        with dissolve
        skeptic "The truth was right there the whole time. We just needed to believe we were better than this. But... but that can't be it! It's supposed to be more complicated than that.\n"
        voice "audio/_pristine/voice/cage/broken/26a.flac"
        broken "I've been telling you that since the moment we got here. At least you finally decided to listen to me.\n"
        #voice "audio/_pristine/voice/cage/broken/26.flac"
        #broken "It's just like I was telling you. We've all been hurt here. All of us had to decide enough was enough.\n"
        voice "audio/_pristine/voice/cage/skeptic/68.flac"
        skeptic "I guess you were right. It's usually the most complicated problems that have the simplest solutions.\n"
    else:
        voice "audio/_pristine/voice/cage/skeptic/69.flac"
        show cg cage free open onlayer back
        with dissolve
        skeptic "The truth was right there the whole time. We just needed to believe we were better than this. I feel like a fool, really, but it's always the most complicated problems that tend to have the simplest solutions.\n"
    voice "audio/_pristine/voice/cage/narrator/75.flac"
    n "That is absolutely {i}not{/i} how this works!\n" id cage_final_default_join_66839095
    voice "audio/_pristine/voice/cage/skeptic/70.flac"
    skeptic "Looks like we've seen through your lies at last, Mr. The Narrator. If that even is your real name.\n"
    if trait_broken:
        voice "audio/_pristine/voice/cage/broken/27.flac"
        broken "Shhh. Hush. Let her talk.\n"
    elif trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/27.flac"
        cheated "Oh shut up. We got lucky. And you {i}especially{/i} got lucky.\n"
        voice "audio/_pristine/voice/cage/hero/36.flac"
        hero "{i}Both of you{/i} talk too much. Give her a chance to say what she wants to say. I'm sick of treating this like some puzzle or bullshit game.\n"
    voice "audio/_pristine/voice/cage/princess/60.flac"
    show cg cage free open talk onlayer back
    with dissolve
    p "I want you to take me out of this place. That's all I've ever wanted.\n"
    play audio "audio/one_shot/chain_1.flac"
    voice "audio/_pristine/voice/cage/narrator/76.flac"
    show cg cage free offer onlayer back
    with dissolve
    n "The Princess' body doesn't stand, instead holding the cage aloft, beckoning you to come near. If you take her out of there, if you carry her to freedom, it's the end of the entire world. You know that, right?\n"
    if trait_broken:
        voice "audio/_pristine/voice/cage/broken/28.flac"
        broken "It's the end of {i}a{/i} world. Your world. But not ours. Sometimes you need to break things to build something better.\n"
    elif trait_cheated:
        voice "audio/_pristine/voice/cage/cheated/28.flac"
        cheated "Fine by me! This world is bullshit anyways. The rest of us will find one that's better.\n"
    voice "audio/_pristine/voice/cage/hero/37.flac"
    hero "Besides, we already made our choice, all the way back in the woods. Nothing you can do about it now.\n"
    voice "audio/_pristine/voice/cage/narrator/77.flac"
    n "I suppose not. You know, I think a part of me always knew this was doomed from the start. I'm narrating on borrowed time, aren't I?\n"
    voice "audio/_pristine/voice/cage/narrator/78.flac"
    n "But even if I'm doomed to go, I might as well make sure you have a proper ending. Go on, then.\n"
    menu:
        extend ""

        "{i}• [[Take your Princess from her cage.]{/i}":
            play audio "audio/one_shot/footsteps_hike_short.flac"
            voice "audio/_pristine/voice/cage/narrator/79.flac"
            show cg cage free offer onlayer back at spectre_small_zoom_instant
            show player cage free reach onlayer front at Position(ypos=1125)
            with dissolve
            #show
            n "You cautiously approach the kneeling body, and extend your hand, bruised and bleeding from the trials that brought you to this point.\n"
            voice "audio/_pristine/voice/cage/narrator/80.flac"
            #play audio "audio/final/Prisoner_HairHeadStress_1.flac"
            hide cg onlayer back
            hide player onlayer front
            show bg cage free take onlayer back at Position(ypos=1125)
            show mid cage free take onlayer front at Position(ypos=1125)
            show head cage free take onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.5)
            show head cage free take smile onlayer inyourface
            with dissolve
            voice sustain
            n "And then you take her from her prison. She looks up at you, and for the first time since you laid eyes on her, she smiles, warmly.\n"
            voice "audio/_pristine/voice/cage/princess/61.flac"
            show head cage free take talk onlayer inyourface
            with dissolve
            p "I have no idea how we're supposed to leave.\n"
            play audio "audio/one_shot/chain_1.flac"
            voice "audio/_pristine/voice/cage/narrator/81.flac"
            hide head onlayer inyourface
            hide bg onlayer back
            hide mid onlayer front
            show farback cage free point onlayer farback at Position(ypos=1125)
            show bg cage free point onlayer back at Position(ypos=1125)
            show cage free point onlayer front at Position(ypos=1125)
            show head cage free point onlayer inyourface at Position(ypos=1100)
            with Dissolve(0.5)
            n "But the body points, and you follow its finger to a lone chain dangling from the doorway that sits far, far above you.\n"
            if trait_cheated:
                voice "audio/_pristine/voice/cage/cheated/29.flac"
                cheated "Are we supposed to climb up? While holding her?\n"
            voice "audio/_pristine/voice/cage/princess/62.flac"
            show head cage free point talk onlayer inyourface
            with dissolve
            p "I'll pull us out of here, if you just hold on.\n"
            #if trait_broken:
            #    voice "audio/_pristine/voice/cage/broken/29.flac"
            #    broken "It's safe. We can trust her now. Same as she can trust us not to drop her as soon as we get upstairs.\n"
            if trait_broken:
                voice "audio/_pristine/voice/cage/broken/29a.flac"
                show head cage free point onlayer inyourface
                with dissolve
                broken "Then let's leave. There's nothing left for us here.\n"
            voice "audio/_pristine/voice/cage/skeptic/71.flac"
            skeptic "I'm game.\n"
            voice "audio/_pristine/voice/cage/hero/38.flac"
            hero "So am I.\n"
            voice "audio/_pristine/voice/cage/narrator/82a.flac"
            n "Then get on with it.\n"
            menu:
                extend ""

                "{i}• [[Take hold of the chain.]{/i}":
                    play tertiary "audio/_pristine/sfx/cage_hoise_loop.flac" loop
                    voice "audio/_pristine/voice/cage/narrator/83c.flac"
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide cage onlayer front
                    hide head onlayer inyourface
                    show bg cage free rise onlayer farback at cage_big_sway, Position(ypos=1125)
                    show chains cage free rise onlayer back at sway, Position(ypos=1125)
                    show cage free rise onlayer front at cage_sway, Position(ypos=1125)
                    with Dissolve(0.5)
                    n "You wrap your hand in the chain, holding tight as it starts to move, and holding the Princess close to you. Together, you rise out of the pit.\n"
                    voice "audio/_pristine/voice/cage/princess/63.flac"
                    show cage free rise talk onlayer front at cage_sway, Position(ypos=1125)
                    with dissolve
                    p "I'm sorry if I made this harder than it had to be.\n"
                    $ gallery_cage.unlock_item(12)
                    $ renpy.save_persistent()
                    voice "audio/_pristine/voice/cage/narrator/84.flac"
                    $ quick_menu = False
                    hide bg onlayer farback
                    hide chains onlayer back
                    hide cage onlayer front
                    scene bg black
                    with fade
                    show bg cage free glance onlayer farback at sway, Position(ypos=1125)
                    show cg cage free glance panel 1 onlayer farback at sway, Position(ypos=1125)
                    show cage free glance down onlayer inyourface at cage_sway, Position(ypos=1125)
                    with fade
                    if persistent.quick_menu:
                        $ quick_menu = True
                    n "You glance back towards the Princess' body, doing its part as it hoists you up. It grows smaller, and smaller, slowly disappearing back into the shadows of the basement.\n"
                    voice "audio/_pristine/voice/cage/princess/64.flac"
                    show bg cage free glance onlayer farback at sway
                    show cg cage free glance panel 2 onlayer farback at sway
                    show cage free glance talk onlayer inyourface at cage_sway
                    with Dissolve(1.0)
                    p "No, that's not right. There shouldn't be an if. I'm sorry. I made this harder than it had to be.\n"
                    #voice "audio/_pristine/voice/cage/narrator/85.flac"
                    #n "The Princess' body is gone, and there's nowhere left for you to look but up.\n"
                    voice "audio/_pristine/voice/cage/skeptic/72.flac"
                    show bg cage free glance onlayer farback at sway
                    show cg cage free glance panel 3 onlayer farback at sway
                    show cage free glance down onlayer inyourface at cage_sway
                    with Dissolve(1.0)
                    skeptic "Maybe she has a point, in a way. Our bodies don't matter.\n"
                    voice "audio/_pristine/voice/cage/princess/65.flac"
                    hide bg onlayer farback
                    hide cg onlayer farback
                    hide cage onlayer inyourface
                    show farback cage free near onlayer farback at Position(ypos=1125)
                    show bg cage free near onlayer back at sway, Position(ypos=1125)
                    show cage free near talk onlayer inyourface at cage_sway, Position(ypos=1125)
                    with Dissolve(0.5)
                    p "We're almost there. I can smell the night air.\n"
                    if trait_cheated:
                        voice "audio/_pristine/voice/cage/cheated/30.flac"
                        show bg cage free near onlayer back at sway
                        show cage free near onlayer inyourface at cage_sway
                        with Dissolve(0.5)
                        cheated "That bit of light feels like it's mocking us. At any moment, she could just drop the whole thing and send us crashing down.\n"
                        voice "audio/_pristine/voice/cage/hero/39.flac"
                        hero "I don't think that's gonna happen, mate.\n"
                        voice "audio/_pristine/voice/cage/cheated/31.flac"
                        cheated "It'd be par for the course.\n"
                    elif trait_broken:
                        voice "audio/_pristine/voice/cage/broken/30.flac"
                        show bg cage free near onlayer back at sway
                        show cage free near onlayer inyourface at cage_sway
                        with Dissolve(0.5)
                        broken "She's sacrificed a lot to get here. More than we did, I think.\n"
                        #voice "audio/_pristine/voice/cage/hero/40.flac"
                        #hero "I'm sure we can figure out some way to reunite them. We'll have all the time in the world, right?\n"
                    $ gallery_cage.unlock_item(13)
                    $ renpy.save_persistent()
                    $ quick_menu = False

                    stop tertiary
                    play tertiary "audio/_pristine/sfx/cage_chains_fall_pop.flac"
                    queue tertiary "audio/_pristine/sfx/Cage_body dangling hooks_2.flac"
                    hide bg onlayer back
                    hide cage onlayer inyourface
                    hide farback onlayer farback
                    scene bg black
                    with fade
                    voice "audio/_pristine/voice/cage/narrator/86.flac"
                    show farback cage free end onlayer farback at Position(ypos=1125)
                    show bg cage free end onlayer back at Position(ypos=1125)
                    show mid cage free end onlayer back at Position(ypos=1125)
                    show cage free end onlayer front at Position(ypos=1125)
                    with fade
                    if persistent.quick_menu:
                        $ quick_menu = True
                    n "And then the chain stops its ascent, depositing you safely in the cabin doorway. I guess you never closed it behind you. Well, there's only one thing left for you to do.\n"
                    voice "audio/_pristine/voice/cage/princess/66.flac"
                    show cage free end talk onlayer front
                    with dissolve
                    p "Shall we?\n"
                    show cage free end onlayer front
                    label chain_free_menu_finale:
                        default chain_free_menu_finale = False
                        menu:
                            extend ""

                            "{i}• (Explore) ''You know, it's funny. All of this talk about free will, and I feel like I'm locked into this outcome.''{/i}" if chain_free_menu_finale == False:
                                $ chain_free_menu_finale = True
                                voice "audio/_pristine/voice/cage/princess/67.flac"
                                show cage free end joke talk onlayer front
                                with dissolve
                                p "I mean, what's the alternative? Dropping me to prove a point?\n"
                                voice "audio/_pristine/voice/cage/narrator/87.flac"
                                n "Huh. I hadn't even considered that. Should it be an option? Can it be an option?\n"
                                if trait_broken:
                                    voice "audio/_pristine/voice/cage/broken/31.flac"
                                    broken "No. It's not an option. We're not cruel for the sake of being cruel.\n"
                                voice "audio/_pristine/voice/cage/princess/68.flac"
                                show cage free end talk onlayer front
                                with dissolve
                                p "I'm joking, by the way. Please don't drop me.\n"
                                if trait_cheated:
                                    voice "audio/_pristine/voice/cage/cheated/32.flac"
                                    show cage free end onlayer front
                                    with dissolve
                                    cheated "I mean... we could...\n"
                                    voice "audio/_pristine/voice/cage/hero/41.flac"
                                    hero "Hell no, don't you even joke.\n"
                                    voice "audio/_pristine/voice/cage/cheated/33.flac"
                                    cheated "Who's joking? But fine, I see I'm outnumbered, as usual. Have it your way.\n"
                                voice "audio/_pristine/voice/cage/skeptic/73.flac"
                                show cage free end onlayer front
                                with dissolve
                                skeptic "It'd certainly be a new data point.\n"
                                if trait_paranoid:
                                    voice "audio/_pristine/voice/cage/paranoid/32.flac"
                                    paranoid "It'd probably come back to bite us is what it'd do.\n"
                                    voice "audio/_pristine/voice/cage/hero/42.flac"
                                    hero "Thankfully, I don't think we can. It really is like we're committed at this point.\n"
                                voice "audio/_pristine/voice/cage/narrator/88.flac"
                                n "It probably wouldn't work anyways. It'd make that perfectly good blade you threw out completely meaningless.\n"
                                jump chain_free_menu_finale

                            "{i}• [[Step into your freedom.]{/i}":
                                $ gallery_cage.unlock_item(14)
                                $ renpy.save_persistent()
                                play audio "audio/one_shot/footsteps_hike_short.flac"
                                voice "audio/_pristine/voice/cage/narrator/89.flac"
                                hide farback onlayer farback
                                hide bg onlayer back
                                hide mid onlayer back
                                hide cage onlayer front
                                show farback cage free outside onlayer farback at Position(ypos=1125)
                                show bg cage free outside onlayer back at Position(ypos=1125)
                                show mid cage free outside onlayer front at Position(ypos=1125)
                                show cage free outside onlayer inyourface at Position(ypos=1125)
                                with Dissolve(0.5)
                                n "And so you step into a world ended by your hand. What a travesty. Goodbye. It's been—\n"
                                stop music fadeout 20.0
                                stop sound fadeout 20.0
                                stop tertiary fadeout 20.0
                                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                                voice "audio/_pristine/voice/cage/hero/43.flac"
                                show quiet creep1 onlayer front at Position(ypos=1125)
                                with Dissolve(1.0)
                                hero "... Awful? Is He still there?\n"
                                voice "audio/_pristine/voice/cage/skeptic/74.flac"
                                skeptic "I think He's gone.\n"
                                if trait_broken:
                                    voice "audio/_pristine/voice/cage/broken/32.flac"
                                    broken "Yes He is. Which means we're finally free, I think.\n"
                                if trait_cheated:
                                    voice "audio/_pristine/voice/cage/cheated/34a.flac"
                                    cheated "Ha. Haha. Hahahahahaha. We did it! That wasn't so bad! ... Now I guess we'll need to find a new game to play.\n"
                                voice "audio/_pristine/voice/cage/princess/69.flac"
                                show quiet creep2 onlayer front at Position(ypos=1125)
                                show cage free outside talk onlayer inyourface at Position(ypos=1125)
                                with Dissolve(0.5)
                                p "Thank you, so much. I didn't think this was possible. But here we are.\n"
                                voice "audio/_pristine/voice/cage/princess/70.flac"
                                show quiet creep3 onlayer front at Position(ypos=1125)
                                show cage free outside cold onlayer inyourface at Position(ypos=1125)
                                with Dissolve(0.5)
                                p "It's a little cold out here, isn't it?\n"
                                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                hide cage onlayer inyourface
                                show hands cage free 1 onlayer front at Position(ypos=1125)
                                with Dissolve(1.5)
                                $ renpy.pause(1.0)
                                show hands cage free 2 onlayer front at Position(ypos=1125)
                                with Dissolve(1.0)
                                $ renpy.pause(0.5)
                                show hands cage free 3 onlayer front at Position(ypos=1125)
                                with Dissolve(0.5)
                                $ renpy.pause(0.25)
                                show hands cage free 4 onlayer front at Position(ypos=1125)
                                with Dissolve(0.25)
                                $ renpy.pause(0.125)
                                show hands cage free 5 onlayer front at Position(ypos=1125)
                                with Dissolve(0.25)
                                $ renpy.pause(0.125)
                                show hands cage free 6 onlayer front at Position(ypos=1125)
                                with Dissolve(0.25)
                                $ renpy.pause(0.125)
                                hide hands onlayer front
                                with Dissolve(0.25)
                                hide farback onlayer farback
                                hide bg onlayer back
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
                                    truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                                else:
                                    truth "You do not get the chance to respond. Something has ripped her from you, and it's left something else in her place.\n"
                                $ princess_satisfy += 1
                                $ princess_free += 1
                                $ cage_end = "free"
                                $ achievement.grant("ACH_CAGE_FREE")
                                jump mirror_start
                                # END


                            "{i}• [[Drop her.]{/i}" if chain_free_menu_finale:
                                stop music
                                if trait_broken:
                                    voice "audio/_pristine/voice/cage/broken/33.flac"
                                    broken "No... no, you can't!\n"
                                voice "audio/_pristine/voice/cage/narrator/90.flac"
                                n "Hah. Well I'll be damned. Did I just will that option into existence?\n"
                                voice "audio/_pristine/voice/cage/hero/44.flac"
                                hero "After everything?!\n"
                                if trait_cheated:
                                    voice "audio/_pristine/voice/cage/cheated/35.flac"
                                    cheated "Ha. So this is what it's like to dish it out. It... feels bad. That's not how I thought it would feel.\n"
                                voice "audio/_pristine/voice/cage/skeptic/75b.flac"
                                skeptic "You sure kept your cards close to your chest. Smartly played. We haven't seen what happens if we're the ones that beat her. But we'll see what happens now.\n"
                                if trait_broken:
                                    voice "audio/_pristine/voice/cage/broken/34.flac"
                                    broken "We're a monster, aren't we? Maybe we always have been.\n"
                                voice "audio/_pristine/voice/cage/narrator/91.flac"
                                stop sound fadeout 20.0
                                stop tertiary fadeout 20.0
                                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 5
                                show cage drop head onlayer front
                                show player cage drop onlayer inyourface at Position(ypos=1125)
                                with Dissolve(0.5)
                                n "Well, no time for taking it back! It's done. You let go of the Princess' head, and watch as she plunges into the abyss. I can't believe I was all doom-and-gloom just a moment ago. Congratulations! You might just have saved the entire world—\n"
                                $ gallery_cage.unlock_item(15)
                                $ renpy.save_persistent()
                                voice "audio/_pristine/voice/cage/princess/71.flac"
                                hide farback onlayer farback
                                hide bg onlayer back
                                hide mid onlayer back
                                hide cage onlayer front
                                hide player onlayer inyourface
                                show quiet creep1 onlayer back at Position(ypos=1125)
                                show bg cage drop panel 1 onlayer farback at Position(ypos=1125)
                                show hands cage drop 1 onlayer front at Position(ypos=1125)
                                with Dissolve(1.0)
                                p "All of that, just to take it all away. You're cold.\n"
                                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                show quiet creep2 onlayer back
                                show bg hands cage drop panel 2 onlayer farback at Position(ypos=1125)
                                show hands cage drop panel 2 onlayer front at Position(ypos=1125)
                                with Dissolve(1.0)
                                $ renpy.pause(0.5)
                                show quiet creep3 onlayer back
                                show bg hands cage drop panel 3 onlayer farback at Position(ypos=1125)
                                show hands cage drop panel 3 onlayer front at Position(ypos=1125)
                                with Dissolve(1.0)
                                $ renpy.pause(0.5)
                                show hands cage drop panel 4 onlayer front at Position(ypos=1125)
                                with Dissolve(0.5)
                                $ renpy.pause(0.25)
                                hide hands onlayer front
                                with Dissolve(0.5)
                                $ renpy.pause(0.25)
                                hide quiet onlayer back
                                hide bg onlayer farback
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
                                    truth "As she plummets, the Princess is taken from you. It's time to leave. Memory returns.\n"
                                else:
                                    truth "As she plummets, the Princess is taken. And something else is left in her place.\n"
                                $ princess_deny += 1
                                $ princess_kept += 1
                                $ cage_end = "drop"
                                $ achievement.grant("ACH_CAGE_DROP")
                                jump mirror_start
                                #END

label cage_slay_join:
    play tertiary "audio/final/chain_break_low.flac"
    queue tertiary "audio/_pristine/sfx/cage_chains_fall_pop.flac"
    hide bg cage encounter onlayer farback
    hide cage approach 4 talk onlayer farback
    hide mid cage encounter onlayer back
    hide player cage approach 4 knife onlayer front
    scene bg black
    voice "audio/_pristine/voice/cage/narrator/92.flac"
    n "As the words leave her mouth, your blade slices through the final chains. You come crashing down.\n"
    voice "audio/_pristine/voice/cage/hero/45.flac"
    scene bg cage slay start onlayer back at cage_blur, Position(ypos=1125)
    show mid cage slay start onlayer front at swayblur, Position(ypos=1125)
    show fore cage slay start onlayer inyourface at cage_blur, Position(ypos=1125)
    with fade
    hero "Well, at least we're not being strangled anymore.\n"
    voice "audio/_pristine/voice/cage/skeptic/76.flac"
    hide bg onlayer back
    hide mid onlayer front
    hide fore onlayer inyourface
    show bg cage slay start onlayer back at Position(ypos=1125)
    show mid cage slay start onlayer front at Position(ypos=1125)
    show fore cage slay start onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    skeptic "Hold on... did you hear what she said? We 'give her our implement.'\n"
    voice "audio/_pristine/voice/cage/hero/46.flac"
    hero "Yeah? What of it?\n"
    voice "audio/_pristine/voice/cage/skeptic/77.flac"
    skeptic "This whole thing's been a riddle! Blade! Heart! Now!\n"

    $ config.menu_include_disabled = True

    menu:
        extend ""

        "{i}• The pieces fall into place.{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False


        "{i}• For every permutation there is a pattern.{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• And when the pattern is learned, the illusion dissolves.{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• But was the pattern always there, or were you the ones who wrote it in the sand?{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• The writers must follow their own script.{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• [[Give her your implement.]{/i}":
            $ config.menu_include_disabled = False
            play secondary "audio/one_shot/footstep_run_dirt_short.flac"
            #queue secondary "audio/one_shot/knife_slash.flac"
            voice "audio/_pristine/voice/cage/narrator/93.flac"
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            show bg cage slay charge onlayer farback at Position(ypos=1125)
            show cage slay charge onlayer back at Position(ypos=1125)
            show speedlines onlayer front at Position(ypos=1125)
            show player cage slay charge onlayer inyourface at Position(ypos=1125)
            with Dissolve(0.5)
            n "Blade flashing, you rush towards the Princess.\n"
            voice "audio/_pristine/voice/cage/narrator/94.flac"
            play audio "audio/one_shot/knife_stab.flac"
            $ default_mouse = "blood"
            hide player onlayer inyourface
            hide speedlines onlayer front
            hide cage onlayer back
            hide bg onlayer farback
            show bg cage slay stab onlayer back at Position(ypos=1125)
            show mid cage slay stab onlayer front at Position(ypos=1125)
            show cage slay stab onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            n "Her body continues its slow march towards you, never changing course even as you sink your weapon into its heart.\n"
            voice "audio/_pristine/voice/cage/narrator/95.flac"
            play audio "audio/_pristine/sfx/Fury Body Horror_4.flac"
            show cage slay wrench onlayer front
            with Dissolve(0.5)
            n "Its hand wraps around yours, its flesh cold and its grip firm. But it does not try to wrench itself free. It instead drives the blade deeper into its own chest.\n"
            $ gallery_cage.unlock_item(16)
            $ renpy.save_persistent()
            voice "audio/_pristine/voice/cage/princess/72.flac"
            play audio "audio/one_shot/footsteps_hike_short.flac"
            hide bg onlayer back
            hide mid onlayer front
            hide cage onlayer front
            show cg cage slay wrench distant talk onlayer back at Position(ypos=1125)
            show fore cage slay wrench distant onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            sp "I cut myself free.\n"
            $ gallery_cage.unlock_item(17)
            $ renpy.save_persistent()
            $ blade_held = False
            $ default_mouse = "default"
            stop music
            play audio "audio/one_shot/collapse.flac"
            voice "audio/_pristine/voice/cage/narrator/96.flac"
            show cg cage slay collapse onlayer back
            with Dissolve(0.5)
            $ renpy.pause(0.5)
            play tertiary "audio/_pristine/sfx/cage_open.flac"
            queue tertiary "audio/one_shot/thump.flac"
            show cg cage slay collapse tumble onlayer back
            with Dissolve(0.5)
            voice sustain
            n "The body collapses to its knees. And as it crumples, life seeming to leave it at last, the door of the cage creaks open. The head of the Princess tumbles out.\n"
            voice "audio/_pristine/voice/cage/narrator/97.flac"
            n "Congratulations, it would seem that you actually managed to see this through. All that's left is to watch her perish—\n"
            voice "audio/_pristine/voice/cage/princess/73.flac"
            stop sound fadeout 20.0
            stop tertiary fadeout 20.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 5
            show quiet creep1 onlayer front at Position(ypos=1125)
            show cg cage slay collapse tumble talk onlayer back
            with dissolve
            sp "This is different. Maybe I got the pattern wrong. Or maybe I finally got it right.\n"
            voice "audio/_pristine/voice/cage/skeptic/78.flac"
            show cg cage slay collapse tumble onlayer back
            with dissolve
            skeptic "We... we did it. We figured it out. We won.\n"
            voice "audio/_pristine/voice/cage/skeptic/79.flac"
            skeptic "Why don't I feel like it means anything?\n"
            voice "audio/_pristine/voice/cage/hero/47.flac"
            hero "I just feel... bad. It's not much of a victory, is it?\n"
            #voice "audio/_pristine/voice/cage/paranoid/33.flac"
            #paranoid "I don't think there is such a thing for us. At least not here.\n"
            voice "audio/_pristine/voice/cage/paranoid/33b.flac"
            paranoid "I don't think there is such a thing for us. At least not here. This was just another trap. Haha. No matter what we do we just keep losing ground.\n"
            voice "audio/_pristine/voice/cage/princess/74.flac"
            show cg cage slay collapse tumble talk onlayer back
            with dissolve
            sp "I'm cold. But I think that's good. I think I can finally rest.\n"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            hide cg onlayer back
            show quiet creep3 onlayer front
            show hands cage slay 1 onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.5)
            show hands cage slay 2 onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.5)
            show hands cage slay 3 onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.25)
            show hands cage slay 4 onlayer front at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            show hands cage slay 5 onlayer front at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            show hands cage slay 6 onlayer front at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            hide hands onlayer front
            with Dissolve(0.25)
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
                truth "You do not get the chance to respond. Nor will you ever. It's time to leave. Memory returns.\n"
            else:
                truth "You do not get the chance to respond. Something has taken her away, and it's left something else in her place.\n" id cage_slay_join_121b5cb2
            $ achievement.grant("ACH_CAGE_RIDDLE")
            $ princess_kept += 1
            $ cage_end = "slay"
            jump mirror_start



            # END
