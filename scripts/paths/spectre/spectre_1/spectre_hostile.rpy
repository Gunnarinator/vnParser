label spectre_menu_hostile:
    default spectre_thoughts_hostile_explore = False
    default spectre_bones_ask = False
    default spectre_bone_smash = False
    menu:
        extend ""

        "{i}• (Explore) ''If I knew I'd have to talk to you again, I wouldn't have slain you.''{/i}" if spectre_if_only == False:
            jump spectre_had_talk_again

        "{i}• (Explore) ''I died too and I'm not floating around like you are. What happened? Why am I different? Why are you different?''{/i}" if spectre_also_dead == False:
            jump spectre_floating

        "{i}• (Explore) ''Stop playing the victim. You threatened me last time.''{/i}" if spectre_victim == False:
            jump spectre_victim_stop

        "{i}• (Explore) ''What if I buried your bones outside?''{/i}" if spectre_thoughts_hostile_explore and spectre_bones_ask == False:
            $ spectre_bones_ask = True
            voice "audio/voices/ch2/spectre/_hostile/princess/1.flac"
            show spectre c flat talk onlayer front
            with dissolve
            p "Those are just bones. They aren't me. Bury them, destroy them, whatever. That dusty pile of death is just a reminder of what you've done. It's not a fix for anything.\n"
            show spectre c flat onlayer front
            with dissolve
            jump spectre_menu_hostile

        "{i}• (Explore) ''Of course I attacked you. You're supposed to end the world. That's why I killed you last time, too.''{/i}" if spectre_world_end_explore == False:
            label spectre_hostile_world_join:
                $ spectre_world_end_explore = True
                voice "audio/voices/ch2/spectre/_hostile/princess/2.flac"
                show spectre c angry onlayer front
                with Dissolve(0.5)
                p "So that's where the hostility comes from. I don't know where you got that idea.\n"
                label spectre_hostile_world_menu:
                    default spectre_hostile_world_end_explore = False
                    default spectre_hostile_world_end_explore_follow = False
                    default spectre_hostile_world_yes_no = False
                    menu:
                        extend ""

                        "{i}• (Explore) ''Well? Were you going to end the world? Would you end it, if you could?''{/i}" if spectre_hostile_world_end_explore == False:
                            $ spectre_hostile_world_end_explore = True
                            voice "audio/voices/ch2/spectre/_hostile/princess/3.flac"
                            show spectre c shrug talk onlayer front
                            with dissolve
                            p "Well, killer, what does it mean for something to end anyway? You 'ended' me, but I'm still right here in front of you, aren't I?\n"
                            if spectre_death_shared:
                                voice "audio/voices/ch2/spectre/_hostile/princess/4.flac"
                                show spectre c scary onlayer front
                                with dissolve
                                p "You apparently 'ended' too, yet here you are. And you don't even look any different.\n"
                            voice "audio/voices/ch2/spectre/_hostile/princess/5.flac"
                            play audio "audio/final/Spectre_PossessingPlayer_1.flac"
                            show spectre c scary talk onlayer front
                            sp "After seeing what you've seen, how can you be sure anything ends?\n"
                            voice "audio/voices/ch2/spectre/_hostile/cold/2.flac"
                            show spectre c scary onlayer front
                            with dissolve
                            cold "I see her point. Everything here is so... impermanent, always shifting. The end of one thing just leads to the start of another.\n"
                            jump spectre_hostile_world_menu

                        "{i}• (Explore) ''Things end. Things have to end. This sentence just ended.''{/i}" if spectre_hostile_world_end_explore_follow == False and spectre_hostile_world_end_explore:
                            $ spectre_hostile_world_end_explore_follow = True
                            voice "audio/voices/ch2/spectre/_hostile/princess/6.flac"
                            show spectre c flat talk onlayer front
                            with dissolve
                            p "Oh, come on. I'm floating right in front of you, still here despite your best efforts. You can't pretend that doesn't mess with the whole concept of 'ending'.\n"
                            show spectre c flat onlayer front
                            with dissolve
                            jump spectre_hostile_world_menu

                        "{i}• (Explore) ''It's a yes or no question. Do you want to end the world?''{/i}" if spectre_hostile_world_yes_no == False:
                            $ spectre_hostile_world_yes_no = True
                            voice "audio/voices/ch2/spectre/_hostile/princess/7.flac"
                            show spectre c flat talk onlayer front
                            with dissolve
                            p "I already gave you my answer. All I want to do is leave. All I want to do is stop feeling trapped. I couldn't give a damn about the world. I can't even remember what it's like.\n"
                            voice "audio/voices/ch2/spectre/_hostile/hero/3.flac"
                            show spectre c flat onlayer front
                            with dissolve
                            hero "I think that's all the answer we're going to get out of her...\n"
                            jump spectre_hostile_world_menu

                        "{i}• (Return) [[Leave it at that.]{/i}":
                            jump spectre_menu_hostile

        "{i}• (Explore) ''You're dead. Or at least mostly dead. What can you even do to hurt me?''{/i}" if spectre_how_hurt_explore == False:
            jump spectre_how_hurt

        "{i}• (Explore) ''What do you want from me?''{/i}" if spectre_possession_ask == False:
            voice "audio/voices/ch2/spectre/_hostile/princess/8.flac"
            play audio "audio/final/Spectre_WindPassingThrough_11.flac"
            show spectre c scary talk onlayer front
            sp "I want you to make things right. I want you to set. Me. Free.\n"
            voice "audio/voices/ch2/spectre/_hostile/princess/9.flac"
            show spectre c angry onlayer front
            with dissolve
            p "This place won't let me leave, but you seem to come and go as you please. So help me out. Let me in, and maybe all of this can be water under the bridge.\n"
            voice "audio/voices/ch2/spectre/_hostile/princess/10.flac"
            play audio "audio/final/Spectre_PossessingPlayer_1.flac"
            show spectre c angry talk onlayer front
            sp "Remember. You owe me.\n"
            voice "audio/voices/ch2/spectre/_hostile/hero/4.flac"
            show spectre c angry onlayer front
            with dissolve
            hero "Maybe we should have just left her here. Maybe we should still just leave her here. If she can't get out on her own, then why do we have to do anything?\n"
            voice "audio/voices/ch2/spectre/_hostile/narrator/2.flac"
            n "'Hasn't gotten out' and 'can't get out' are two very different things.\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/23.flac"
            cold "That would be dull, anyway. It's always more interesting if we make a choice.\n"
            label spectre_hostile_possession_join:
                $ spectre_possession_ask = True
                voice "audio/voices/ch2/spectre/_hostile/narrator/3.flac"
                n "Absolutely not.\n"
                voice "audio/voices/ch2/spectre/_hostile/hero/5.flac"
                hero "Is she asking us if she can... possess us?\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/37.flac"
                n "She is, and I hope I don't need to explain why you can't let that happen. It would be catastrophic if she managed to escape this place, and if you let her in, there is very little anyone could do to stop her.\n"
                voice "audio/voices/ch2/spectre/_encounter/hero/18.flac"
                hero "Would she be able to see... {i}us{/i} if we went along with it?\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/24.flac"
                cold "Now isn't that an interesting thought. We could finally bring her face-to-face with Him.\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/38a.flac"
                n "{i}Sigh{/i}. You won't like how things play out if you go down this path.\n"
                label spectre_hostile_possession_menu:
                    menu:
                        extend ""

                        "{i}• (Explore) ''What if I say no?''{/i}" if spectre_possession_no_explore == False:
                            $ spectre_possession_no_explore = True
                            voice "audio/voices/ch2/spectre/_hostile/princess/11.flac"
                            play audio "audio/final/Spectre_WindPassingThrough_9.flac"
                            show spectre c angry talk onlayer front
                            sp "Try it. See what happens.\n"
                            voice "audio/voices/ch2/spectre/_hostile/hero/6.flac"
                            show spectre c angry onlayer front
                            with dissolve
                            hero "I don't like how she said that. It sounds dangerous.\n"
                            #voice "audio/voices/ch2/spectre/_hostile/narrator/4.flac"
                            #n "Obviously it's dangerous. But one of these options is dangerous for everyone else in the world, and the other is only dangerous for you. And, of course, you could always figure out how to slay her, the least dangerous choice for everyone, including you.\n"
                            voice "audio/voices/ch2/spectre/_hostile/cold/4.flac"
                            cold "Is anything 'dangerous' if we can never really die?\n"
                            if spectre_narrator_loop == False:
                                $ spectre_narrator_loop = True
                                voice "audio/voices/ch2/spectre/_hostile/narrator/5.flac"
                                n "Look. You and the Princess clearly have a history, and that history clearly involves death. But aside from some horrifying implications, I don't care what's already happened between the two of you.\n"
                            else:
                                voice "audio/voices/ch2/spectre/_hostile/narrator/6.flac"
                                n "Aside from some horrifying implications, I don't really care what's already happened between you and the Princess.\n"
                            voice "audio/voices/ch2/spectre/_hostile/narrator/7.flac"
                            n "And you don't know that you can never really die. Maybe you could only come back once! And even then, there are fates that come close to death in their terror.\n"
                            voice "audio/voices/ch2/spectre/_hostile/cold/5.flac"
                            cold "What a strange thing to say. Isn't the turn of phrase, 'fates worse than death?'\n"
                            voice "audio/voices/ch2/spectre/_hostile/narrator/8.flac"
                            n "There are no fates worse than the finality of death. Anyone who says otherwise is a fool.\n"
                            jump spectre_hostile_possession_menu

                        "{i}• (Explore) ''This would just be temporary, right? You'll leave once we're out of the cabin?''{/i}" if spectre_possession_no_wont == False:
                            $ spectre_possession_no_wont = True
                            voice "audio/voices/ch2/spectre/_hostile/princess/12.flac"
                            show spectre c homesick talk onlayer front
                            with dissolve
                            p "Look, I don't want to be stuck with you any more than you want to be stuck with me. You're my murderer. All I see when I look into your eyes is the thing that ran at me with the point of a blade aimed for my heart.\n"
                            voice "audio/voices/ch2/spectre/_hostile/princess/13.flac"
                            show spectre c flat talk onlayer front
                            with dissolve
                            p "So... you're not exactly my first choice. But you're also my only choice.\n"
                            voice "audio/voices/ch2/spectre/_hostile/cold/6.flac"
                            show spectre c flat onlayer front
                            with dissolve
                            cold "It sounds to me like she'd be a lovely roommate.\n"
                            jump spectre_hostile_possession_menu

                        "{i}• (Explore) ''If... if I let you in, do I still get to be in control?''{/i}" if spectre_possession_control == False:
                            $ spectre_possession_control = True
                            voice "audio/voices/ch2/spectre/_hostile/princess/14.flac"
                            play audio "audio/final/Spectre_PossessingPlayer_5.flac"
                            show spectre c scary onlayer front
                            with dissolve
                            sp "There's only one way to find out.\n"
                            voice "audio/voices/ch2/spectre/_hostile/hero/7.flac"
                            hero "That's not very reassuring.\n"
                            voice "audio/voices/ch2/spectre/_hostile/cold/7a.flac"
                            cold "What's another voice rattling around in here? We'll be fine.\n"
                            voice "audio/voices/ch2/spectre/_hostile/hero/8.flac"
                            hero "It's pretty crowded already, wouldn't you say? And she's not exactly friendly.\n"
                            voice "audio/voices/ch2/spectre/_hostile/cold/8.flac"
                            cold "Neither is He.\n"
                            voice "audio/voices/ch2/spectre/_hostile/narrator/9.flac"
                            n "I'm being perfectly respectful considering the stakes of the situation! Don't push my good will.\n"
                            jump spectre_hostile_possession_menu

                        "{i}• ''Before I agree to anything, we need to talk about what happens after you leave. I was told you'd end the world.''{/i}" if spectre_world_end_explore == False and spectre_possession_ask:
                            jump spectre_hostile_world_join

                        "{i}• ''No complaints here. Do it.'' [[Let the Princess possess you.]{/i}":
                            jump spectre_possession_join

                        "{i}• ''The answer is no.''{/i}" if spectre_can_wraith:
                            if wraith_encountered:
                                $ spectre_can_wraith = False
                                voice "audio/voices/mound/bonus/path.flac"
                                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                                hero "Wait... what?!\n"
                                jump spectre_hostile_possession_menu
                            voice "audio/voices/ch2/spectre/_hostile/princess/15.flac"
                            play audio "audio/final/Spectre_PossessingPlayer_1.flac"
                            show spectre c angry talk onlayer front
                            with dissolve
                            sp "Of all the people you could have been, why did you have to be you?\n"
                            jump spectre_death

                        "{i}• (Return) ''I need to think on this.''{/i}":
                            voice "audio/voices/ch2/spectre/_hostile/princess/16.flac"
                            show spectre c homesick talk onlayer front
                            with dissolve
                            p "Take your time. I'll be waiting. I'm very good at waiting.\n"
                            show spectre c homesick onlayer front
                            with dissolve
                            jump spectre_menu_hostile

        "{i}• (Explore) Okay team, I'm out of ideas. Thoughts?{/i}" if spectre_thoughts_explore == False:
            $ spectre_thoughts_explore = True
            $ spectre_thoughts_hostile_explore = True
            voice "audio/voices/ch2/spectre/_hostile/cold/1.flac"
            cold "She might be making it hard for us to kill her body, but those bones look very, very real. Maybe breaking them breaks her.\n"
            voice "audio/voices/ch2/spectre/_hostile/hero/1.flac"
            hero "Or maybe burying them would put her to rest.\n"
            voice "audio/voices/ch2/spectre/_hostile/narrator/1.flac"
            n "Don't take any piece of her outside of this cabin. {i}Sigh.{/i} Maybe you should stop looking for loopholes and try harder to actually slay her.\n"
            voice "audio/voices/ch2/spectre/_hostile/hero/2.flac"
            hero "But we are trying!\n"
            jump spectre_menu_hostile

        "{i}• ''Okay. I've given it enough thought. Let's get you out of here.'' [[Let the Princess possess you.]{/i}" if spectre_possession_ask:
            jump spectre_possession_join

        "{i}• ''Okay. I've given it enough thought. The answer is no. I can't let you out, and I won't let you possess me.''{/i}" if spectre_can_wraith and spectre_possession_ask:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_hostile
            voice "audio/voices/ch2/spectre/_hostile/princess/17.flac"
            show spectre c angry onlayer front
            with Dissolve(0.5)
            p "Figures. I guess we'll have to fight then.\n"
            jump spectre_death

        "{i}• [[Smash her bones.]{/i}" if spectre_thoughts_hostile_explore and spectre_can_wraith:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_hostile
            voice "audio/voices/ch2/spectre/_hostile/narrator/10.flac"
            play audio "audio/final/spectre_smash.flac"
            hide spectre onlayer front
            hide bg onlayer back
            hide farback onlayer farback
            scene cg spectre bones smash onlayer back at Position(ypos=1125)
            with Dissolve(0.5)
            n "You push through the Princess and rush the pile of bones on the floor, swinging your fist down and smashing through what remains of her ribcage. The ancient bones splinter, then crumble, reduced to dust almost instantly.\n"
            stop music
            $ spectre_bone_smash = True
            if spectre_bones_ask:
                voice "audio/voices/ch2/spectre/_hostile/princess/18.flac"
                p "Even after what I've said, you still gave it your all. Such a disappointing choice. I don't think I like the person behind those eyes.\n"
                jump spectre_hostile_second_join
            else:
                jump spectre_hostile_second_join

        "{i}• [[Slay the Princess, harder.]{/i}" if spectre_can_wraith and blade_held:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_hostile
            stop music
            voice "audio/voices/ch2/spectre/_hostile/narrator/11.flac"
            play audio "audio/final/Spectre_WindPassingThrough_13.flac"
            show spectre c cut onlayer front
            show player spectre c cut onlayer inyourface at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.5)
            voice sustain
            hide spectre with dissolve
            n "You swing at the Princess once more, and once more, your blade cuts through nothing as she disappears.\n"
            voice "audio/voices/ch2/spectre/_hostile/princess/19.flac"
            sp "Really?\n"
            voice "audio/voices/ch2/spectre/_hostile/narrator/12.flac"
            hide bg onlayer back
            hide farback onlayer farback
            hide player onlayer inyourface
            scene bg spectre heart stairs onlayer back at Position(ypos=1125)
            show spectre heart stairs onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            n "Her voice chides from elsewhere in the room. You whirl around, finding her hovering between you and the basement stairs, looking you over with grim disappointment.\n"
            voice "audio/voices/ch2/spectre/_hostile/narrator/13.flac"
            show spectre heart stairs onlayer front at spectre_small_zoom, Position(ypos=1125)
            n "She draws in close.\n"
            label spectre_hostile_second_join:
                if spectre_bone_smash and spectre_bones_ask == False:
                    voice "audio/voices/ch2/spectre/_hostile/princess/20.flac"
                    hide cg onlayer back
                    show bg spectre heart stairs onlayer back at Position(ypos=1125)
                    show spectre heart stairs talk onlayer front at spectre_small_zoom_instant
                    with Dissolve(0.5)
                    p "Those bones aren't me. I'm me.\n"
                    voice "audio/voices/ch2/spectre/_hostile/princess/21a.flac"
                    p "But you've made it obvious that you don't want to help.\n"
                else:
                    voice "audio/voices/ch2/spectre/_hostile/princess/22.flac"
                    hide cg onlayer back
                    show bg spectre heart stairs onlayer back at Position(ypos=1125)
                    show spectre heart stairs talk onlayer front at spectre_small_zoom_instant
                    with Dissolve(0.5)
                    p "I was willing to let bygones be bygones, killer. I was willing to ignore everything you did to me so we could get out of here. Together.\n"
                voice "audio/voices/ch2/spectre/_hostile/princess/23.flac"
                show spectre heart cry touch onlayer front
                with dissolve
                p "All I ever wanted was to leave this place. All I ever wanted was to find a way back home.\n" id spectre_hostile_second_join_95d8ffb1
                voice "audio/voices/ch2/spectre/_hostile/princess/24.flac"
                show spectre heart eyes fall talk onlayer front
                with dissolve
                p "Wherever home is.\n"
                voice "audio/voices/ch2/spectre/_hostile/narrator/14.flac"
                show spectre heart evil look onlayer front
                with dissolve
                n "Her eyes turn from wells of sorrow to pits of wrath as she stares into you.\n"
                voice "audio/voices/ch2/spectre/_hostile/princess/25.flac"
                play audio "audio/final/Spectre_PossessingPlayer_2.flac"
                show spectre heart evil look talk onlayer front
                sp "But I guess violence is the only language you speak.\n"
                jump spectre_kill_player

        "{i}• [[Grab the Princess, but try harder.]{/i}" if spectre_can_wraith and blade_held == False:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_hostile
            stop music
            voice "audio/voices/ch2/spectre/_hostile/narrator/15.flac"
            play audio "audio/final/Spectre_WindPassingThrough_13.flac"
            show spectre c grab onlayer front
            show player spectre c grab onlayer inyourface at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.5)
            voice sustain
            hide spectre with dissolve
            n "You attempt once more to seize the Princess, and once more, you grip only cold, empty air as she disappears.\n"
            voice "audio/voices/ch2/spectre/_hostile/princess/19.flac"
            sp "Really?\n"
            voice "audio/voices/ch2/spectre/_hostile/narrator/12.flac"
            hide bg onlayer back
            hide farback onlayer farback
            hide player onlayer inyourface
            scene bg spectre heart stairs onlayer back at Position(ypos=1125)
            show spectre heart stairs onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            n "Her voice chides from elsewhere in the room. You whirl around, finding her hovering between you and the basement stairs, looking you over with grim disappointment.\n"
            jump spectre_hostile_second_join

        "{i}• ''Fine. If I can't hurt you, then there really isn't anything for me to do here. I guess I'll get going.'' [[Leave her in the basement.]{/i}" if spectre_can_wraith:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_hostile
            stop music
            voice "audio/voices/ch2/spectre/_encounter/narrator/55.flac"
            n "This isn't a solution. Nobody wins here.\n"
            jump spectre_retrieve_abandon_join

        "{i}• ''Right. I don't think there's much more for us to talk about. I'm going to get my blade now, and then the two of us can fight.'' [[Retrieve the blade.]{/i}" if blade_held == False and spectre_can_wraith:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_hostile
            stop music
            $ spectre_blade_retrieve = True
            voice "audio/voices/ch2/spectre/_encounter/narrator/57.flac"
            n "Excellent idea. It's good to hear that you're finally seeing reason.\n"
            jump spectre_retrieve_abandon_join
return
