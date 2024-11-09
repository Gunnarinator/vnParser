label razor_1_basement_menu:

    if razor_last_time_mention and razor_narrator_loop_comment == False:
        $ razor_narrator_loop_comment = True
        if razor_1_forest_share_loop_insist:
            voice "audio/voices/ch2/razor/basement/narrator/1.flac"
            n "There you go again, talking up delusions about a past-life experience that clearly didn't happen.\n"
        else:
            voice "audio/voices/ch2/razor/basement/narrator/2.flac"
            n "'Last time?' What are you talking about?\n"
        voice "audio/voices/ch2/razor/basement/cheated/1.flac"
        cheated "Ugh. It's like the two of you are working together on this. Aren't you listening to her? She's obviously lying through her teeth.\n"
        voice "audio/voices/ch2/razor/basement/hero/1.flac"
        hero "I'm terrible at spotting liars and even I can tell something's up here. We can't be the only ones who looped back to the start. Someone else has to remember, right?\n"
        voice "audio/voices/ch2/razor/basement/narrator/3.flac"
        n "Yes. Something is obviously 'up' and we can all tell that she's lying. But the thing she's lying about is how dangerous she is, not 'dimension-hopping' or 'time-travel' or whatever it is you think you're doing.\n"

    elif razor_general_follow_flag and razor_general_follow_count == 0:
        $ razor_general_follow_count += 1
        $ razor_general_follow_flag = False
        voice "audio/voices/ch2/razor/basement/cheated/2.flac"
        cheated "I have absolutely zero doubts that she is going to stab us if we get close to her.\n"
        voice "audio/voices/ch2/razor/basement/hero/2.flac"
        hero "She certainly feels threatening.\n"
        voice "audio/voices/ch2/razor/basement/narrator/4.flac"
        n "Just because she's acting like she's going to stab you doesn't mean she has the means to actually do it.\n"
        if blade_held:
            voice "audio/voices/ch2/razor/basement/narrator/5.flac"
            n "But you know who is armed? You. So stop second guessing yourself and do your job.\n"
        else:
            voice "audio/voices/ch2/razor/basement/narrator/6.flac"
            n "But you know who has the capacity to quickly arm himself? You do. So stop second guessing yourself, go upstairs, take the blade, and do your job.\n"
        voice "audio/voices/ch2/razor/basement/hero/3.flac"
        hero "But I'm nervous.\n"
        voice "audio/voices/ch2/razor/basement/narrator/6a.flac"
        n "All the more reason to jump into the deep end and deal with her right now, before you waste any more time getting stuck in your head.\n"

    elif razor_general_follow_flag and razor_general_follow_count == 1:
        $ razor_general_follow_count += 1
        $ razor_general_follow_flag = False
        voice "audio/voices/ch2/razor/basement/narrator/7.flac"
        n "How many more times does she have to vaguely threaten you before you to finally decide you're ready to deal with her?\n"
        voice "audio/voices/ch2/razor/basement/cheated/3.flac"
        cheated "We're clearly still figuring out our angle. We don't have the luxury of watching this from a distance.\n"
        voice "audio/voices/ch2/razor/basement/narrator/8.flac"
        n "Oh, I'm sorry, do you think I'm in a position of luxury right now?\n"
        voice "audio/voices/ch2/razor/basement/hero/4.flac"
        hero "You're acting like you are.\n"
        voice "audio/voices/ch2/razor/basement/narrator/9.flac"
        n "My entire world is at risk.\n"
        voice "audio/voices/ch2/razor/basement/cheated/4.flac"
        cheated "Then maybe you should behave with a little more humility. A bit of self-deprecation would go a long way.\n"
        voice "audio/voices/ch2/razor/basement/narrator/10.flac"
        n "No. I have my dignity.\n"
        voice "audio/voices/ch2/razor/basement/cheated/5.flac"
        cheated "Fine. Then we'll continue to treat you exactly how you deserve to be treated.\n"


    elif razor_general_follow_flag and razor_general_follow_count == 2:
        $ razor_general_follow_count += 1
        $ razor_general_follow_flag = False
        voice "audio/voices/ch2/razor/basement/narrator/11.flac"
        n "I think I've said my piece at this point.\n"
        voice "audio/voices/ch2/razor/basement/cheated/6.flac"
        cheated "I think we all have. But if you want to keep exhausting your questions, it beats getting stabbed to death.\n"

    elif razor_general_follow_flag and razor_general_follow_count == 3:
        $ razor_general_follow_count += 1
        $ razor_general_follow_flag = False
        voice "audio/voices/ch2/razor/basement/princess/1.flac"
        show razor d bored talk onlayer back
        with dissolve
        sp "Okay, I'm bored now.\n"
        voice "audio/voices/ch2/razor/basement/hero/5.flac"
        show razor d bored onlayer back
        with dissolve
        hero "She's bored...?\n"
        voice "audio/voices/ch2/razor/basement/narrator/12.flac"
        n "That's absurd. She doesn't get to be bored. Not in a way that matters. She's a {i}prisoner{/i}. She's—\n{w=5.0}{nw}"
        show screen disableclick(0.5)
        $ gallery_razor.unlock_item(4)
        $ renpy.save_persistent()
        jump razor_1_initiative

    # note: menu options that toggle razor_general_follow_flag to true, instead of getting specific follow-ups, increment the "razor_general_follow_flag" tree above, which culminates in her cutting herself free and attacking you.

    # some notes: loop_1_princess_killed; razor_revival
    default razor_count = 0
    default razor_stab_ask = False
    default razor_last_time_ask = False
    default razor_last_time_mention = False
    default razor_last_time_ask_follow = False
    default razor_narrator_loop_comment = False
    default razor_suspicious_comment = False
    default razor_let_out = False
    default razor_activities = False
    default razor_talk = False
    default razor_last_time_kill = False
    default razor_no_key = False
    default razor_good_will = False
    default razor_mad = False
    default razor_drop_knife_ask = False
    default razor_drop_knife_2 = False
    default razor_drop_knife_3 = False
    default razor_honest_mention = False
    default razor_nobody_die = False

    default razor_general_follow_flag = False
    default razor_general_follow_count = 0

    menu:

        extend ""

        "{i}• (Explore) ''Prove it then. Prove that you don't have a knife.''{/i}" if razor_drop_knife_2 == False and razor_drop_knife_ask:
            $ razor_drop_knife_2 = True
            $ razor_count += 1
            voice "audio/voices/ch2/razor/basement/princess/2.flac"
            show razor d surprise talk onlayer back
            with dissolve
            sp "It would be so much easier to prove that I do have a sharp object. I could just show it to you! But I don't have one, so I can't.\n"
            voice "audio/voices/ch2/razor/basement/narrator/13.flac"
            show razor d hands onlayer back
            with dissolve
            n "The Princess smiles as she pulls her hands from behind her back.\n"
            voice "audio/voices/ch2/razor/basement/princess/3.flac"
            show razor d hands talk onlayer back
            with dissolve
            sp "But look at this! Hands! Hands that don't have anything in them to stab you with.\n"
            voice "audio/voices/ch2/razor/basement/narrator/14.flac"
            show razor d sleeves onlayer back
            with dissolve
            n "Her smile stretches into an even wider grin as she shakes her sleeves.\n"
            voice "audio/voices/ch2/razor/basement/princess/4.flac"
            show razor d sleeves talk onlayer back
            with dissolve
            sp "And empty sleeves too! Look at how few stabbing implements I have. It's practically zero!\n"
            show razor d neutral onlayer back
            with dissolve
            jump razor_1_basement_menu

        "{i}• (Explore) ''But what if you're just hiding it somewhere secret?''{/i}" if razor_drop_knife_2 and razor_drop_knife_3 == False:
            $ razor_drop_knife_3 = True
            $ razor_count += 1
            voice "audio/voices/ch2/razor/basement/princess/5.flac"
            show razor d surprise talk onlayer back
            with dissolve
            sp "I've shown you all of my hiding spots! What kind of Princess do you think I am? I would never hide something sharp somewhere secret.\n"
            voice "audio/voices/ch2/razor/basement/princess/6.flac"
            show razor d cheeky talk onlayer back
            with dissolve
            sp "Wait, that sounds like I'm lying, but I'm actually not. My secret zones are for me only they have nothing to do with you or my intention to not-stab you to death the second you get close to me.\n"
            voice "audio/voices/ch2/razor/basement/narrator/15.flac"
            show razor d serious onlayer back
            with dissolve
            n "Her smile drops for a moment, her expression sharp and flat.\n"
            voice "audio/voices/ch2/razor/basement/princess/7.flac"
            show razor d serious talk onlayer back
            with dissolve
            sp "I assure you, there's nothing hidden there.\n"
            voice "audio/voices/ch2/razor/basement/hero/6.flac"
            show razor d serious onlayer back
            with dissolve
            hero "I'm inclined to believe her on that one. She seems serious.\n"
            voice "audio/voices/ch2/razor/basement/cheated/7.flac"
            cheated "Of course, but that doesn't mean that she doesn't have something hidden {i}somewhere{/i}. We know for a fact she's armed.\n"
            jump razor_1_basement_menu

        "{i}• (Explore) ''If I come close to you, you're just going to stab me, aren't you?''{/i}" if razor_stab_ask == False:
            $ razor_count += 1
            $ razor_stab_ask = True
            $ razor_general_follow_flag = True
            voice "audio/voices/ch2/razor/basement/princess/8.flac"
            show razor d cheeky talk onlayer back
            with dissolve
            sp "What? Noooo. No I wouldn't stab you. I am just a sweet innocent Princess, trapped here for no reason.\n"
            voice "audio/voices/ch2/razor/basement/princess/9.flac"
            show razor d surprise talk onlayer back
            with dissolve
            sp "And you are a brave knight who is supposed to walk up to... not-stabbing-distance to help me.\n"
            show razor d surprise onlayer back
            with dissolve
            jump razor_1_basement_menu

        "{i}• (Explore) ''Do you remember what happened last time?''{/i}" if razor_last_time_ask == False:
            $ razor_last_time_ask = True
            $ razor_last_time_mention = True
            $ razor_count += 1
            if razor_revival:
                voice "audio/voices/ch2/razor/basement/princess/10.flac"
                show razor d shrug talk onlayer back
                with dissolve
                sp "Last time? If somebody came into my house and stabbed me to death and then I killed him, surely I would remember that!\n"
            elif loop_1_princess_killed:
                voice "audio/voices/ch2/razor/basement/princess/11.flac"
                show razor d shrug talk onlayer back
                with dissolve
                sp "Last time? If somebody came into my house and tried to kill me and I cut his neck open and then he stabbed me in the heart and we both died looking in each other's eyes, well, surely I would remember that!\n"
            else:
                voice "audio/voices/ch2/razor/basement/princess/12.flac"
                show razor d shrug talk onlayer back
                with dissolve
                sp "Last time? If somebody came into my house and tried to kill me and I cut his neck open, surely I would remember that!\n"
            voice "audio/voices/ch2/razor/basement/princess/13.flac"
            show razor d surprise talk onlayer back
            with dissolve
            sp "But I don't remember it! So it must not have happened.\n"
            show razor d shrug onlayer back
            with dissolve
            jump razor_1_basement_menu

        "{i}• (Explore) ''But that's exactly what happened! So you do remember it.''{/i}" if razor_last_time_ask and razor_last_time_ask_follow == False:
            $ razor_count += 1
            $ razor_last_time_ask_follow = True
            voice "audio/voices/ch2/razor/basement/princess/14.flac"
            show razor d cheeky talk onlayer back
            with dissolve
            sp "Would I just lie? Would I just lie to your face and tell you that a thing I remembered happening didn't happen just so I could stab you again?\n"
            voice "audio/voices/ch2/razor/basement/princess/15.flac"
            show razor d idea talk onlayer back
            with dissolve
            sp "I mean just so I could stab you for the first time.\n"
            show razor d faux confused onlayer back
            with dissolve
            if razor_narrator_loop_comment:
                voice "audio/voices/ch2/razor/basement/cheated/8.flac"
                cheated "Aha! She slipped up there! She said again. And her taking it back doesn't count.\n"
                voice "audio/voices/ch2/razor/basement/narrator/16.flac"
                n "Do you hear how deranged you sound right now? Please just stop dawdling. This is only going to end with violence. Postponing the inevitable is only going to make it worse for you when it actually happens.\n"
            jump razor_1_basement_menu

        "{i}• (Explore) ''I know you have a knife. I'll let you out of here if you drop it.''{/i}" if razor_drop_knife_ask == False:
            $ razor_drop_knife_ask = True
            $ razor_count += 1
            voice "audio/voices/ch2/razor/basement/princess/26.flac"
            show razor d cheeky talk onlayer back
            with dissolve
            sp "A knife? What are you talking about? I don't have a knife. Where would I keep a knife?\n"
            voice "audio/voices/ch2/razor/basement/princess/27.flac"
            show razor d surprise talk onlayer back
            with dissolve
            sp "And why would I stab you to death? I don't know you. You haven't given me a reason to stab you to death. It would be so silly of me to cut you open and look at your insides.\n"
            voice "audio/voices/ch2/razor/basement/cheated/10.flac"
            show razor d surprise onlayer back
            with dissolve
            cheated "Okay, I could have sworn we didn't mention stabbing anyone to death.\n"
            voice "audio/voices/ch2/razor/basement/narrator/19.flac"
            n "It sounds like she's really out for blood. Fortunately for you, she isn't armed.\n"
            jump razor_1_basement_menu

        "{i}• (Explore) ''I'd like to trust you, but you're being so suspicious right now!''{/i}" if razor_suspicious_comment == False:
            $ razor_general_follow_flag = True
            $ razor_suspicious_comment = True
            $ razor_count += 1
            voice "audio/voices/ch2/razor/basement/princess/16.flac"
            show razor d plead onlayer back
            with dissolve
            sp "That's so rude of you, passing judgments on strangers you've never met just because they're different from you! How would you like it if I did that, huh?\n"
            if blade_held:
                voice "audio/voices/ch2/razor/basement/princess/17a.flac"
                show razor d bored talk onlayer back
                with dissolve
                sp "Silly little birdface thinks he's so serious coming down here but doesn't know anything! Thinks he can tell me to get rid of all the knives I don't even have while he gets to wave one around right in front of me!\n"
            else:
                voice "audio/voices/ch2/razor/basement/princess/18.flac"
                show razor d bored talk onlayer back
                with dissolve
                sp "Silly little birdface thinks he's so serious coming down here but doesn't know anything! He doesn't even have a knife for stabbing!\n"
            voice "audio/voices/ch2/razor/basement/princess/19.flac"
            show razor d cheeky talk onlayer back
            with dissolve
            sp "I bet you didn't like that did you? I bet you didn't like being judged for no reason.\n"
            show razor d neutral onlayer back
            with dissolve
            jump razor_1_basement_menu

        "{i}• (Explore) ''Can we just talk things through?''{/i}" if razor_talk == False:
            $ razor_talk = True
            $ razor_count += 1
            $ razor_general_follow_flag = True
            voice "audio/voices/ch2/razor/basement/princess/20a.flac"
            show razor d faux confused talk onlayer back
            with dissolve
            sp "But we don't have anything to talk through! We're strangers and this place is cramped and annoying and you should just come over here and let me out.\n"
            show razor d faux confused onlayer back
            with dissolve
            jump razor_1_basement_menu

        "{i}• (Explore) ''I don't have the key.''{/i}" if razor_no_key == False:
            $ razor_no_key = True
            $ razor_count += 1
            $ razor_general_follow_flag = True
            voice "audio/voices/ch2/razor/basement/princess/21.flac"
            show razor d bored talk onlayer back
            with dissolve
            sp "Oh you don't okay I see.\n"
            voice "audio/voices/ch2/razor/basement/princess/22a.flac"
            show razor d idea talk onlayer back
            with dissolve
            sp "I have an idea! You should come over here and stare directly at the chains. You won't be able to find the key if you don't know what it's supposed to look like. So you'd better come right within close staring distance just to be sure.\n"
            show razor d cheeky onlayer back
            with dissolve
            jump razor_1_basement_menu

        "{i}• (Explore) ''I don't have a weapon. Isn't that a sign of good will?''{/i}" if blade_held == False and razor_good_will == False:
            $ razor_good_will = True
            $ razor_count += 1
            voice "audio/voices/ch2/razor/basement/princess/23.flac"
            show razor d idea talk onlayer back
            with dissolve
            sp "Yes! Yes of course! Haven't you seen that I've only been nice to you since you got here?\n"
            voice "audio/voices/ch2/razor/basement/hero/7.flac"
            show razor d idea onlayer back
            with dissolve
            hero "Has she?\n"
            voice "audio/voices/ch2/razor/basement/cheated/9.flac"
            cheated "Her words have been fine but her general attitude's been weird and extremely suspicious, and I think that's what really counts.\n"
            voice "audio/voices/ch2/razor/basement/narrator/17.flac"
            n "This shouldn't even be a question. She absolutely has not been nice to you.\n"
            jump razor_1_basement_menu

        "{i}• (Explore) ''We killed each other last time. I'd rather not do that again.''{/i}" if razor_last_time_kill == False and loop_1_princess_killed:
            $ razor_last_time_kill = True
            $ razor_count += 1
            $ razor_last_time_mention = True
            voice "audio/voices/ch2/razor/basement/princess/24.flac"
            show razor d surprise talk onlayer back
            with dissolve
            sp "But if we killed each other, then why are we here, right now, both of us normal and un-stabbed?\n"
            show razor d surprise onlayer back
            with dissolve
            if razor_narrator_loop_comment == False:
                voice "audio/voices/ch2/razor/basement/narrator/18.flac"
                n "I do have to hand it to her, that's a very good question, and it's one with a simple answer: you haven't slain her yet. So how about you get moving?\n"
            jump razor_1_basement_menu

        "{i}• (Explore) ''Look, I know that you're mad at me but I think we both just need to let bygones be bygones.''{/i}" if razor_mad == False:
            $ razor_mad = True
            $ razor_count += 1
            $ razor_general_follow_flag = True
            voice "audio/voices/ch2/razor/basement/princess/25a.flac"
            show razor d plead onlayer back
            with dissolve
            sp "But I'm not mad at you! So please stop standing so far out of reach.\n"
            show razor d surprise onlayer back
            with dissolve
            jump razor_1_basement_menu



        "{i}• (Explore) ''What happened after you died last time?''{/i}" if razor_last_time_ask == False and loop_1_princess_killed:
            $ razor_last_time_ask = True
            $ razor_last_time_mention = True
            $ razor_count += 1
            voice "audio/voices/ch2/razor/basement/princess/28.flac"
            show razor d faux confused talk onlayer back
            with dissolve
            sp "That's funny! You're funny! I'm not dead, so I can't have died!\n"
            show razor d faux confused onlayer back
            with dissolve
            jump razor_1_basement_menu

        "{i}• (Explore) ''What if we're both honest with each other? I was sent here to stop you from ending the world, and you slashed my throat last time.''{/i}" if razor_honest_mention == False and razor_revival == False:
            label razor_world_end_join:
                $ razor_honest_mention = True
                $ razor_last_time_mention = True
                $ razor_count += 1
                $ razor_general_follow_flag = True
                voice "audio/voices/ch2/razor/basement/princess/29.flac"
                show razor d cheeky talk onlayer back
                with dissolve
                sp "That doesn't sound like me!\n"
                show razor d cheeky onlayer back
                with dissolve
                jump razor_1_basement_menu

        "{i}• (Explore) ''What if we're both honest with each other? I was sent here to stop you from ending the world, and you killed me last time after coming back from being stabbed in the heart.''{/i}" if razor_honest_mention == False and razor_revival:
            jump razor_world_end_join

        "{i}• (Explore) ''Nobody has to die.''{/i}" if razor_nobody_die == False:
            $ razor_nobody_die = True
            $ razor_count += 1
            $ razor_general_follow_flag = True
            voice "audio/voices/ch2/razor/basement/princess/30.flac"
            show razor d surprise talk onlayer back
            with dissolve
            sp "Of course not! At least not now. Because you're here to save me. But you'll have to come close.\n"
            show razor d surprise talk onlayer back
            with dissolve
            jump razor_1_basement_menu

        "{i}• (Explore) ''Okay. What are you going to do if I let you out?''{/i}" if razor_let_out == False:
            $ razor_let_out = True
            $ razor_count += 1
            voice "audio/voices/ch2/razor/basement/princess/31.flac"
            show razor d shrug talk onlayer back
            with dissolve
            sp "All sorts of things, which is why I think that's a great idea! I would love to not be chained up down here. Being chained up is so boring and I crave fresh and new activities to broaden my horizons.\n"
            voice "audio/voices/ch2/razor/basement/narrator/20.flac"
            show razor d surprise onlayer back
            with dissolve
            n "Please don't let her out of here.\n"
            voice "audio/voices/ch2/razor/basement/cheated/11.flac"
            cheated "Believe it or not, I think I'm actually with Him on this.\n"
            voice "audio/voices/ch2/razor/basement/hero/8.flac"
            hero "Okay, but what if all of this is just a misunderstanding? There has to be room for this to be a misunderstanding.\n"
            jump razor_1_basement_menu

        "{i}• (Explore) ''Activities like stabbing or cutting or murdering?''{/i}" if razor_let_out and razor_activities == False:
            $ razor_activities = True
            $ razor_count += 1
            voice "audio/voices/ch2/razor/basement/princess/32.flac"
            show razor d idea talk onlayer back
            with dissolve
            sp "Yes! I mean maybe! I've never done any of those things but there is something alluring about the sound of it.\n"
            voice "audio/voices/ch2/razor/basement/princess/33.flac"
            show razor d surprise talk onlayer back
            with dissolve
            sp "I think it would also be fun to do other activities like look at a bird or touch a tree.\n"
            voice "audio/voices/ch2/razor/basement/hero/9.flac"
            show razor d surprise onlayer back
            with dissolve
            hero "Okay, now listen.\n"
            voice "audio/voices/ch2/razor/basement/cheated/12.flac"
            cheated "You're not actually buying this, are you?\n"
            voice "audio/voices/ch2/razor/basement/hero/10.flac"
            hero "Listen.\n"
            voice "audio/voices/ch2/razor/basement/narrator/21a.flac"
            n "... Yes?\n"
            #n "... Yes? We're listening.\n"
            voice "audio/voices/ch2/razor/basement/hero/11a.flac"
            hero "I would like to look at a bird.\n"
            voice "audio/voices/ch2/razor/basement/narrator/22.flac"
            n "You can look at a bird later.\n"
            voice "audio/voices/ch2/razor/basement/hero/12.flac"
            hero "But if we look at a bird {i}now{/i} we wouldn't have to be {i}here{/i}.\n"
            voice "audio/voices/ch2/razor/basement/cheated/13.flac"
            cheated "He has a point.\n"
            voice "audio/voices/ch2/razor/basement/narrator/23.flac"
            n "Just make a decision already.\n"
            jump razor_1_basement_menu

        "{i}• ''Okay, fine. I'm coming closer to free you. You'd better not try anything.'' [[Approach the Princess.]{/i}":
            voice "audio/voices/ch2/razor/basement/princess/34.flac"
            show razor d idea talk onlayer back
            with dissolve
            sp "Of course I won't!\n"
            show razor d idea onlayer back
            with dissolve
            jump razor_1_approach

        "{i}• ''Yeah. I'm not trusting this. Bye!'' [[Turn and leave.]{/i}":
            jump razor_1_leave

        "{i}• ''I'll be right back. I left something upstairs.'' [[Go retrieve the knife upstairs.]{/i}" if blade_held == False:
            jump razor_1_leave

        "{i}• ''Screw it.'' [[Slay the Princess.]{/i}" if blade_held:
            jump razor_1_slay_attempt

label razor_1_initiative:

    voice "audio/voices/ch2/razor/basement/narrator/24.flac"
    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
    show bg razor nochain onlayer back
    show razor initiative erupt onlayer back
    with dissolve
    n "Shit. In a sudden burst of movement, the Princess leaps towards you, a blade erupting from her free arm, her wrist limp and empty from the violent expulsion. Huh. So I guess she did have a knife of her own after all.\n"
    voice "audio/voices/ch2/razor/basement/cheated/14a.flac"
    cheated "How conciliatory of you. We appreciate it, really. Now what are we going to do?!\n"
    voice "audio/voices/ch2/razor/basement/hero/13.flac"
    hero "At least we're safe here. She's still in chains.\n"
    voice "audio/voices/ch2/razor/basement/narrator/25.flac"
    play audio "audio/final/Prisoner_HeavyChains_1.flac"
    show razor initiative stopped onlayer back
    with dissolve
    n "And those chains stop her from continuing her advance, at least for a moment.\n"
    voice "audio/voices/ch2/razor/basement/narrator/25a.flac"
    show razor initiative examine onlayer back
    with dissolve
    n "She looks down at them with something between annoyance and confusion.\n"
    voice "audio/voices/ch2/razor/basement/narrator/26.flac"
    play audio "audio/final/Razor_SwordCutArm_2.flac"
    show razor initiative chop arm onlayer back
    with dissolve
    n "And then she slices through her arm.\n"
    voice "audio/voices/ch2/razor/basement/hero/14.flac"
    hero "Okay. Maybe we aren't safe here.\n"
    voice "audio/voices/ch2/razor/basement/narrator/27.flac"
    play audio "audio/one_shot/footstep_run_medium.flac"
    hide razor onlayer back
    show bg razor posthandchop onlayer back at Position(ypos=1125)
    show cg razor charge onlayer front at Position(ypos=1125)
    with dissolve
    n "She doesn't even hesitate before darting towards you with a terrifying speed you can't hope to outpace.\n"
    if blade_held:
        voice "audio/voices/ch2/razor/basement/cheated/15.flac"
        cheated "Ah, shit. Okay. She's down an arm and we still have a weapon. I guess we'll have to use it.\n"
        voice "audio/voices/ch2/razor/basement/narrator/28.flac"
        play audio "audio/final/Razor_SwordHitDrag_1.flac"
        hide bg onlayer back
        hide farback onlayer back
        hide cg onlayer front
        show bg razor generic onlayer farback at Position(ypos=1125)
        show panel1 razor charge fight onlayer back at Position(ypos=1125)
        with Dissolve(1.0)
        n "And use it you do. But unfortunately for you, and for the entire world, you are horribly outmatched.\n"
        voice "audio/voices/ch2/razor/basement/narrator/29a.flac"
        $ blade_held = False
        $ default_mouse = "flip"
        play secondary "audio/final/Razor_SwordCutArm_3.flac"
        queue secondary "audio/one_shot/thump.flac"
        queue secondary "audio/one_shot/knife_bounce_several.flac"
        show panel2 razor charge fight onlayer front at Position(ypos=1125)
        with dissolve
        n "You keep pace with her for a single brief and wordless exchange before she severs your hand, and with it, your only line of defense.\n" id razor_1_initiative_922a0831
        #voice "audio/voices/ch2/razor/basement/narrator/29.flac"
        #n "You keep pace with her for a single brief and worldless exchange before she severs your hand, and with it, removes your only line of defense.\n"
        if razor_revival:
            voice "audio/voices/ch2/razor/basement/hero/15.flac"
            hero "She's much better at this than she was last time.\n"
            voice "audio/voices/ch2/razor/basement/cheated/16.flac"
            cheated "Yeah. It's unreal. Bloody cheater.\n"
        else:
            voice "audio/voices/ch2/razor/basement/hero/16.flac"
            hero "She's even better at this than she was last time.\n"
            voice "audio/voices/ch2/razor/basement/cheated/17.flac"
            cheated "Bloody cheater.\n"
        jump razor_1_end
    else:
        voice "audio/voices/ch2/razor/basement/cheated/18.flac"
        play audio "audio/one_shot/footstep_run_medium.flac"
        hide bg onlayer back
        hide farback onlayer back
        hide farback onlayer farback
        hide cg onlayer front
        scene cg razor flee onlayer back at Position(ypos=1125)
        with dissolve
        cheated "That won't stop us from trying. Run run run run run!\n"
        voice "audio/voices/ch2/razor/basement/narrator/30.flac"
        n "You sprint for the stairs, but I wasn't exaggerating when I said she was running at you with a terrifying speed you couldn't hope to outpace.\n"
        voice "audio/voices/ch2/razor/basement/hero/17.flac"
        hero "We don't make it, do we?\n"
        voice "audio/voices/ch2/razor/basement/narrator/31.flac"
        play audio "audio/final/Razor_ImpaleSwordBody_1.flac"
        hide farback onlayer farback
        hide cg onlayer back
        scene bg black
        n "No. You feel her blade in your back before you make it to the first stair.\n"
        label razor_1_end:
            stop music
            voice "audio/voices/ch2/razor/basement/princess/35.flac"
            hide panel1 onlayer back
            hide farback onlayer farback
            hide bg onlayer farback
            hide panel2 onlayer front
            hide bg onlayer back
            show bg razor approach killed onlayer back at Position(ypos=1125)
            show cg razor kill flee onlayer front at Position(ypos=1125)
            with dissolve
            sp "I'm going to kill you now.\n"
            voice "audio/voices/ch2/razor/basement/narrator/32.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
            show cg razor kill face squelch onlayer front at Position(ypos=1125)
            with dissolve
            n "And with a squelch, she does just that.\n"
            voice "audio/voices/ch2/razor/basement/narrator/32a.flac"
            play audio "audio/one_shot/collapse.flac"
            hide bg onlayer back
            hide cg onlayer front
            with fade
            n "Everything goes dark, and you die.\n"
            $ quick_menu = False
            $ blade_held = False
            $ default_mouse = "default"
            if razor_paranoid_override:
                $ trait_paranoid = True
            else:
                $ trait_broken = True
            jump razor_2_start
            # END


label razor_1_approach:

    voice "audio/voices/ch2/razor/basement/narrator/33.flac"
    play audio "audio/one_shot/footsteps_stone.flac"
    hide razor onlayer back
    hide bg onlayer back
    hide farback onlayer farback
    scene farback razor approach onlayer farback at Position(ypos=1125)
    show bg razor approach onlayer back at Position(ypos=1125)
    show cg razor approach onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    n "Against your better judgment, you walk across the room to within arm's reach of the Princess.\n"
    voice "audio/voices/ch2/razor/basement/cheated/19.flac"
    play audio "audio/one_shot/footsteps_stone.flac"
    show cg razor approach killed onlayer front
    with Dissolve(1.0)
    cheated "I don't like the way you said 'within arm's reach.'\n"
    voice "audio/voices/ch2/razor/basement/narrator/34.flac"
    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
    show cg razor approach killed thenyours onlayer front
    n "You hear the horrible sound of metal slicing through meat.\n"
    voice "audio/voices/ch2/razor/basement/hero/18.flac"
    hero "... Whose meat? Not ours, right?\n"
    voice "audio/voices/ch2/razor/basement/narrator/35.flac"
    n "Hers at first.\n"
    voice "audio/voices/ch2/razor/basement/narrator/36.flac"
    n "Then yours. Your neck, specifically.\n"
    if razor_revival == False:
        voice "audio/voices/ch2/razor/basement/cheated/20.flac"
        cheated "Again? Really?!\n"
    voice "audio/voices/ch2/razor/basement/princess/36.flac"
    show farback razor approach onlayer farback
    show bg razor approach onlayer back
    show cg razor kill flee onlayer front
    with dissolve
    sp "Hehe!\n"
    $ gallery_razor.unlock_item(5)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/razor/basement/narrator/37.flac"
    play audio "audio/one_shot/collapse.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide cg onlayer front
    scene bg black
    $ renpy.pause(0.25)
    voice sustain
    scene farback razor approach killed final onlayer farback at swayblur, Position(ypos=1125)
    show bg razor approach killed final onlayer back at swayblur, Position(ypos=1125)
    show cg razor approach killed final onlayer back at swayblur, Position(ypos=1125)
    with Dissolve(0.5)
    n "You collapse to the ground, your vision swimming as you attempt to focus on her bloody blade and the limp sack of flesh that was once her arm.\n"
    stop music
    voice "audio/voices/ch2/razor/basement/princess/37a.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide cg onlayer back
    scene farback razor approach killed final onlayer farback at Position(ypos=1125)
    show bg razor approach killed final onlayer back at Position(ypos=1125)
    show cg razor approach killed final talk onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    sp "You're going to die now.\n"
    voice "audio/voices/ch2/razor/basement/narrator/38.flac"
    play audio "audio/final/Adversary_SkullBreaksBrain_1.flac"
    $ quick_menu = False
    $ blade_held = False
    $ default_mouse = "default"
    hide farback onlayer farback
    hide bg onlayer back
    hide cg onlayer back
    scene bg black
    n "And with a quick jerk of her elbow, she does just that. Everything goes dark, and you die.\n"
    $ trait_broken = True
    jump razor_2_start
    # END

label razor_1_leave:

    default razor_paranoid_override = False
    $ razor_paranoid_override = True
    voice "audio/voices/ch2/razor/basement/princess/38.flac"
    show razor d bored talk onlayer back
    with dissolve
    sp "It's boring if you leave.\n"
    voice "audio/voices/ch2/razor/basement/hero/5.flac"
    show razor d bored onlayer back
    with dissolve
    hero "She's bored...?\n"
    voice "audio/voices/ch2/razor/basement/narrator/39.flac"
    n "That's absurd. She doesn't get to be bored. Not in a way that matters. She's a {i}prisoner{/i}. She's—\n{w=5.0}{nw}"
    show screen disableclick(0.5)
    jump razor_1_initiative


label razor_1_slay_attempt:

    voice "audio/voices/ch2/razor/basement/narrator/40.flac"
    play audio "audio/one_shot/footstep_run_medium.flac"
    hide bg onlayer back
    hide farback onlayer back
    hide razor onlayer back
    show bg razor approach killed onlayer back at Position(ypos=1125)
    show cg razor approach killed onlayer front at Position(ypos=1125)
    show speedlines onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    n "The Princess falls silent, her smile unwavering as you charge across the room.\n"
    voice "audio/voices/ch2/razor/basement/cheated/21.flac"
    cheated "Okay. She hasn't pulled out a knife yet. And her hands are still behind her back. I think we can do this. I think we can win. We just have to strike now, but make sure you keep your eyes on those hands, I don't trust her for a second.\n"
    voice "audio/voices/ch2/razor/basement/narrator/41.flac"
    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
    hide speedlines onlayer inyourface
    show cg razor impaled face onlayer front
    with dissolve
    n "But your focus is broken by the horrible sound of metal slicing through meat.\n"
    voice "audio/voices/ch2/razor/basement/hero/18.flac"
    hero "... Whose meat? Not ours, right?\n"
    voice "audio/voices/ch2/razor/basement/narrator/42.flac"
    n "Hers at first.\n"
    voice "audio/voices/ch2/razor/basement/narrator/43.flac"
    n "Then yours.\n"
    voice "audio/voices/ch2/razor/basement/princess/36.flac"
    show cg razor impaled face talk onlayer front
    with dissolve
    sp "Hehe!\n"
    voice "audio/voices/ch2/razor/basement/cheated/22a.flac"
    show cg razor impaled face onlayer front
    cheated "How?! What did she even hit us with?\n"
    $ gallery_razor.unlock_item(3)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/razor/basement/narrator/44.flac"
    hide bg onlayer back
    hide cg onlayer front
    show bg razor approach killed onlayer back at Position(ypos=1125)
    show cg razor charge ouch onlayer front at Position(ypos=1125)
    with dissolve
    n "You stare down at your chest, and at the long, thin blade she impaled you with.\n"
    voice "audio/voices/ch2/razor/basement/narrator/44a.flac"
    hide bg onlayer back
    hide cg onlayer front
    show cg razor charge impaled onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "And then at the red, angry slit along the flesh of her thigh, where the blade had been nestled just a moment ago. It's still lodged in her leg, emerging from her knee, hinging up and out of her body like some extra metallic limb.\n"
    voice "audio/voices/ch2/razor/basement/cheated/23.flac"
    cheated "Bullshit. Absolute bullshit.\n"
    voice "audio/voices/ch2/razor/basement/princess/37a.flac"
    stop music
    hide cg onlayer back
    show bg razor approach killed onlayer back at Position(ypos=1125)
    show cg razor impaled face talk onlayer front at Position(ypos=1125)
    with dissolve
    sp "You're going to die now.\n"
    voice "audio/voices/ch2/razor/basement/narrator/45.flac"
    play audio "audio/final/Adversary_SkullBreaksBrain_1.flac"
    hide cg onlayer front
    hide farback onlayer farback
    hide bg onlayer back
    hide cg onlayer back
    scene bg black
    n "With a twist of her knee and a painful squelch, she does just that. Everything goes dark, and you die.\n"
    $ trait_stubborn = True
    $ quick_menu = False
    $ blade_held = False
    $ default_mouse = "default"
    jump razor_2_start
    # end


return
