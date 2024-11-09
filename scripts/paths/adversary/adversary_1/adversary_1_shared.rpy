label adversary_1_assorted_variables:

    default adversary_1_style = "direct"
    default adversary_1_wounded = False
    default adversary_attack_immediate = False
    default adversary_can_attack_immediate = True
    default adversary_combat_to_pacifism = False
    default adversary_can_fury = True

label adversary_1_distant_chat:
    default adversary_different_comment = False
    default adversary_memory_comment = False
    default adversary_chat_comment = False
    default adversary_scared_comment = False
    default adversary_closer_comment = False
    default adversary_free_offer = False
    default adversary_unpack = False
    default adversary_unarmed_banter = False
    $ adversary_1_narrator_accepts_origin = "distant"
    default adversary_proof_toggle = False

    if adversary_1_narrator_proof == False and adversary_proof_toggle:
        $ adversary_1_narrator_accepts_origin = "distant"
        $ adversary_1_narrator_proof = True
        jump adversary_1_narrator_accepts

    menu:
        extend ""

        "{i}• (Explore) I hope you heard all of that, Mr. Narrator. This is a lot different than last time, but last time definitely {b}happened{/b}.{/i}" if adversary_1_forest_share_loop and adversary_1_narrator_proof == False:
            $ adversary_can_attack_immediate = False
            $ adversary_1_narrator_proof = True
            if adversary_1_forest_share_loop_insist:
                voice "audio/voices/ch2/adversary/_shared/narrator/1.flac"
                n "Okay, fine. Let's say for a moment that I believe you.\n"
            else:
                voice "audio/voices/ch2/adversary/_shared/narrator/2.flac"
                n "What's that? Oh, that whole 'déjà vu' situation. Yes it does seem like you and the Princess remember each other, so let's say for a moment that I {b}do{/b} believe you.\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/3.flac"
            n "For all we know whatever happened to you last time was just a fluke, and beyond that, do you know who doesn't remember anything that happened last time? Me. I don't remember what happened last time.\n"
            voice "audio/voices/ch2/adversary/_shared/hero/1.flac"
            hero "Are... are you okay?\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/4.flac"
            n "Of course I'm not okay! As far as we're all concerned, the fate of my world is still very much on the line. Not all of us have the luxury of jumping over to a parallel universe the second we die.\n"
            jump adversary_1_distant_chat

        "{i}• (Explore) ''You look... different.''{/i}" if adversary_different_comment == False:
            $ adversary_can_attack_immediate = False
            $ adversary_different_comment = True
            $ adversary_proof_toggle = True
            if blade_held:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_1.flac"
                show adversary d excited talk onlayer back
                with dissolve
                sp "You look exactly the same.\n"
                show adversary d excited onlayer back
            else:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_2a.flac"
                show adversary d crossed talk onlayer back
                with dissolve
                sp "Aside from your empty hands, you look exactly the same.\n"
                show adversary d crossed onlayer back
            jump adversary_1_distant_chat

        "{i}• (Explore) ''So you {b}do{/b} remember me!''{/i}" if adversary_memory_comment == False:
            $ adversary_can_attack_immediate = False
            $ adversary_memory_comment = True
            $ adversary_proof_toggle = True
            if blade_held:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_3.flac"
                show adversary d neutral onlayer back
                with dissolve
                sp "Oh, I remember you, alright. Best three minutes of my life. So why don't we do it again?\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/1.flac"
                stubborn "See? She wants to fight us again. There's no reason for us to stand around talking.\n"
                if adversary_1_narrator_proof == False:
                    $ adversary_1_narrator_accepts_origin = "distant"
                    jump adversary_1_narrator_accepts
            else:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_4a.flac"
                show adversary d neutral onlayer back
                with dissolve
                sp "Oh, I remember you, alright. Best three minutes of my life. So why don't we do it again? Or are you scared I'm going to put you down for good this time?\n"
                if adversary_1_narrator_proof == False:
                    $ adversary_1_narrator_accepts_origin = "distant"
                    jump adversary_1_narrator_accepts
                voice "audio/voices/ch2/adversary/_shared/stubborn/2.flac"
                stubborn "Are you just going to let her talk to us like that? We're not scared.\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/5.flac"
                n "I think my position on violence in this situation is already more than clear, but you really shouldn't let yourself be goaded so easily. There's more at risk in this encounter than your fragile ego.\n"
                voice "audio/voices/ch2/adversary/_shared/hero/2.flac"
                hero "I agree. If we're going to fight her, we need a weapon.\n"
            jump adversary_1_distant_chat

        "{i}• (Explore) ''I actually am just here to chat.''{/i}" if adversary_chat_comment == False and blade_held == False:
            $ adversary_can_attack_immediate = False
            $ adversary_chat_comment = True
            $ adversary_proof_toggle = True
            if basement_1_talked:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_5.flac"
                show adversary d talk2 onlayer back
                with dissolve
                sp "Haven't we talked enough? Do you really have anything else to say, or are you just stalling because you're scared I'm going kill you again?\n"
                show adversary d excited onlayer back
            else:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_6.flac"
                show adversary d talk2 onlayer back
                with dissolve
                sp "Why? You didn't want to talk last time. Are you scared I'm going to kill you again?\n"
                show adversary d bored onlayer back
            if adversary_1_narrator_proof == False:
                $ adversary_1_narrator_accepts_origin = "distant"
                jump adversary_1_narrator_accepts
            jump adversary_1_distant_chat

        "{i}• (Explore) ''I'm not scared of you.''{/i}" if adversary_scared_comment and adversary_closer_comment == False:
            $ adversary_closer_comment = True
            $ adversary_can_attack_immediate = False
            voice "audio/voices/ch2/adversary/_shared/princess/adv_7.flac"
            show adversary d excited talk onlayer back
            with dissolve
            sp "Then prove it. Come a little closer.\n"
            show adversary d neutral onlayer back
            jump adversary_1_distant_chat

        "{i}• (Explore) ''I'm actually here to free you.''{/i}" if adversary_free_offer == False:
            $ adversary_free_offer = True
            $ adversary_can_attack_immediate = False
            voice "audio/voices/ch2/adversary/_shared/narrator/6.flac"
            show adversary d crossed onlayer back
            with dissolve
            n "Free her?! You aren't — {i}sigh{/i}. I don't know why I'm even bothering, to be honest. You know the stakes of the situation.\n"
            voice "audio/voices/ch2/adversary/_shared/princess/adv_8.flac"
            show adversary d crossed talk onlayer back
            with dissolve
            sp "Who says I want to be free?\n"
            show adversary d crossed onlayer back
            menu:
                extend ""

                "{i}• ''You don't want to be free? Are you serious?''{/i}":
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_9.flac"
                    show adversary d talk2 onlayer back
                    with dissolve
                    sp "Yeah. I'm fine right where I am.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/3.flac"
                    show adversary d glare onlayer back
                    hero "Okay, hold on, did you hear that? Maybe we don't have to do anything. If she's fine where she is, maybe—\n{w=7.4}{nw}"
                    show screen disableclick(0.5)
                    if blade_held:
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_10.flac"
                        show adversary d excited talk onlayer back
                        with dissolve
                        sp "But you're going to have to {i}fight me to the death{/i}.\n"
                    else:
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_11.flac"
                        show adversary d excited talk onlayer back
                        with dissolve
                        sp "As long as you go back upstairs, pick up that knife, and {i}fight me to the death{/i}.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/4.flac"
                    show adversary d excited onlayer back
                    hero "Nevermind.\n"
                    voice "audio/voices/ch2/adversary/_shared/narrator/7a.flac"
                    n "There is no happy ending here where everyone makes it out of this place alive. You either deal with her here, right now, or she'll eventually find her way out. Whether she even wants to leave is hardly relevant. This cabin won't last forever.\n"
                    if blade_held:
                        voice "audio/voices/ch2/adversary/_shared/stubborn/3.flac"
                        stubborn "Hear that? Between Him and Her, that should be all the motivation you need. Now stop standing there and fight her!\n"
                        voice "audio/voices/ch2/adversary/_shared/narrator/8.flac"
                        n "No. Stop standing there and {i}slay{/i} her.\n"
                    else:
                        voice "audio/voices/ch2/adversary/_shared/stubborn/4.flac"
                        stubborn "Hear that? Between Him and Her, that should be all the motivation you need. Now pick up the blade and fight her!\n"
                        voice "audio/voices/ch2/adversary/_shared/narrator/9.flac"
                        n "No. Pick up the blade and {i}slay{/i} her.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/5.flac"
                    hero "You're being a bit semantic, aren't you?\n"
                    voice "audio/voices/ch2/adversary/_shared/narrator/10.flac"
                    n "I am, but it's an important distinction. If you're going to see this through, you need to hold the right intent. This isn't a sparring match, it is a lethal confrontation that will decide the future of {i}everything{/i}.\n"
                    voice "audio/voices/ch2/adversary/_shared/stubborn/5.flac"
                    stubborn "Fine. As long as it leads to a fight, do whatever He just said.\n"

                "{i}• ''If you don't want to be free, then what do you want?''{/i}":
                    $ adversary_proof_toggle = True
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_12.flac"
                    show adversary d excited talk onlayer back
                    with dissolve
                    sp "I want the two of us to fight to the death. I want to feel your knife split my flesh, and I want to hear your bones snap beneath my fists.\n"
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_13.flac"
                    show adversary d neutral onlayer back
                    with dissolve
                    sp "Is that really too much to ask?\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/6.flac"
                    hero "Yeah. Especially that last part.\n"
                    voice "audio/voices/ch2/adversary/_shared/stubborn/6.flac"
                    stubborn "Don't be such a coward.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/7.flac"
                    hero "I'm just being cautious. If it comes to violence we can find a way to deal with her that doesn't involve throwing our life away. I'd rather not die again, and I find it deeply disturbing that you seem to relish the thought of it.\n"
                    voice "audio/voices/ch2/adversary/_shared/stubborn/7.flac"
                    stubborn "Because it doesn't matter if we die again! It'll just be another opportunity to have the fight of our life.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/8.flac"
                    hero "We don't know that for sure, and I'd rather not bet on it...\n"
                    if adversary_1_narrator_proof == False:
                        $ adversary_1_narrator_accepts_origin = "distant"
                        jump adversary_1_narrator_accepts

                "{i}• ''Me? Anyone? Why wouldn't you want to be free?''{/i}":
                    voice "audio/voices/ch2/adversary/_shared/hero/9.flac"
                    hero "Are you sure we want to look a gift horse in the mouth right now? If she doesn't want to leave, doesn't this whole situation just work out for everyone?\n"
                    label adversary_free_explore_join:
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_14.flac"
                        show adversary d talk onlayer back
                        with dissolve
                        sp "There's nothing out there for me. The only thing I care about is right here.\n"
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_14a.flac"
                        show adversary d neutral onlayer back
                        with dissolve
                        sp "All I want is to keep knowing what it feels like to kill you and be {i}killed{/i} by you.\n"
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_15.flac"
                        show adversary d excited talk onlayer back
                        with dissolve
                        sp "I want to feel that knife split me open. I want to feel your bones snap beneath my fists.\n"
                        voice "audio/voices/ch2/adversary/_shared/narrator/11.flac"
                        show adversary d neutral onlayer back
                        n "I think I'll just let the Princess speak for herself here. Leaving her in the basement isn't an answer. You have to make a choice.\n"
                        voice "audio/voices/ch2/adversary/_shared/stubborn/8.flac"
                        stubborn "And there's only one choice worth making. Fight her! Win!\n"

                "{i}• [[Remain silent.]{/i}":
                    voice "audio/voices/ch2/adversary/_shared/hero/10.flac"
                    hero "Are you really just gonna... not say anything to that? If she doesn't want to leave, doesn't this whole situation just work out for everyone?\n"
                    jump adversary_free_explore_join

            jump adversary_1_distant_chat

        "{i}• (Explore) ''I'm not saying I'm {b}not{/b} here to fight, but I think the two of us have a few things to unpack first. Like how we're both still alive.''{/i}" if adversary_unpack == False:
            $ adversary_can_attack_immediate = False
            $ adversary_unpack = True
            $ adversary_proof_toggle = True
            voice "audio/voices/ch2/adversary/_shared/princess/adv_16.flac"
            show adversary d excited talk onlayer back
            with dissolve
            sp "What is there to unpack? I was dead and now I'm not and the same goes for you. There. Unpacking done.\n"
            voice "audio/voices/ch2/adversary/_shared/princess/adv_17.flac"
            show adversary d neutral onlayer back
            with dissolve
            sp "Don't you get it? We've been given free reign to wail on each other {i}forever{/i}.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/9.flac"
            stubborn "Couldn't have said it better myself.\n"
            if adversary_1_narrator_proof == False:
                $ adversary_1_narrator_accepts_origin = "distant"
                jump adversary_1_narrator_accepts
            jump adversary_1_distant_chat

        "{i}• (Explore) ''I haven't decided what I'm doing yet.''{/i}" if adversary_closer_comment == False:
            $ adversary_can_attack_immediate = False
            $ adversary_closer_comment = True
            $ adversary_proof_toggle = True
            if basement_1_talked:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_18a.flac"
                show adversary d talk onlayer back
                with dissolve
                sp "You haven't decided? We talked more than enough last time. Do you really have anything else to say, or are you just stalling because you're scared I'm going to kill you?\n"
            else:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_19.flac"
                show adversary d excited talk onlayer back
                with dissolve
                sp "And why not? You decided what to do with me quickly enough last time. Are you scared I'm going to kill you again? Maybe you're worried I'll put you down for good this time...\n"
            voice "audio/voices/ch2/adversary/_shared/princess/adv_20.flac"
            show adversary d neutral onlayer back
            with dissolve
            sp "If you want to talk, I guess I can talk, but you should come a little closer first.\n"
            if adversary_1_narrator_proof == False:
                $ adversary_1_narrator_accepts_origin = "distant"
                jump adversary_1_narrator_accepts
            jump adversary_1_distant_chat

        "{i}• (Explore) ''Don't worry, I'm always up for a good fight. In fact, the only reason I came down here without a weapon is because having a knife felt {b}unfair.{/b}''{/i}" if adversary_unarmed_banter == False and blade_held == False:
            $ adversary_can_attack_immediate = False
            $ adversary_unarmed_banter = True
            voice "audio/voices/ch2/adversary/_shared/princess/adv_21.flac"
            show adversary d talk2 onlayer back
            with dissolve
            sp "Then why are you just standing there?\n"
            voice "audio/voices/ch2/adversary/_shared/princess/adv_21a.flac"
            show adversary d excited talk onlayer back
            with dissolve
            sp "{i}Fight me{/i}.\n"
            show adversary d neutral onlayer back
            jump adversary_1_distant_chat

        "{i}• [[Slay the Princess.]{/i}" if blade_held and adversary_can_attack_immediate:
            stop music
            $ adversary_attack_immediate = True
            play audio "audio/one_shot/footstep_run_dirt_short.flac"
            hide adversary onlayer back
            hide adversary onlayer front
            hide farback onlayer back
            hide farback onlayer farback
            hide bg onlayer back
            scene bg adversary readying onlayer back at Position(ypos=1125)
            if adversary_1_chains_broken == False:
                show chain adversary readying onlayer front at Position(ypos=1125)
            show adversary readying onlayer front at Position(ypos=1125)
            with dissolve
            jump adversary_1_fight_immediate

        "{i}• [[Attack the Princess.]{/i}" if blade_held and adversary_can_attack_immediate == False:
            play audio "audio/one_shot/footstep_run_dirt_short.flac"
            hide adversary onlayer back
            hide adversary onlayer front
            hide farback onlayer back
            hide farback onlayer farback
            hide bg onlayer back
            scene bg adversary readying onlayer back at Position(ypos=1125)
            if adversary_1_chains_broken == False:
                show chain adversary readying onlayer front at Position(ypos=1125)
            show adversary readying onlayer front at Position(ypos=1125)
            with dissolve
            jump adversary_1_fight

        "{i}• ''Fine. Let's do this.'' [[Attack her unarmed.]{/i}" if blade_held == False and adversary_unarmed_banter and adversary_can_fury:
            if fury_encountered:
                $ adversary_can_fury = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                #voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                #hero "Wait... what?!\n"
                jump adversary_1_distant_chat
            jump adversary_1_fight_unarmed

        "{i}• [[Attack her unarmed.]{/i}" if blade_held == False and adversary_can_fury:
            if fury_encountered:
                $ adversary_can_fury = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                #voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                #hero "Wait... what?!\n"
                jump adversary_1_distant_chat
            jump adversary_1_fight_unarmed

        "{i}• ''The blade's upstairs. I'll be right back.'' [[Go upstairs and retrieve the blade.]{/i}" if adversary_1_cabin_blade_taken == False:
            voice "audio/voices/ch2/adversary/_shared/princess/adv_22.flac"
            show adversary d neutral onlayer back
            with dissolve
            sp "I'll be waiting.\n"
            jump adversary_1_retrieve_knife

        "{i}• [[Step closer.]{/i}" if adversary_closer_comment:
            jump adversary_1_close_join

        "{i}• ''I don't know what happened to you since the last time we met, but I am {b}not{/b} fighting a giant demon-lady. Bye!'' [[Turn around and leave.]{/i}" if adversary_can_fury:
            if fury_encountered:
                $ adversary_can_fury = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                #voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                #hero "Wait... what?!\n"
                jump adversary_1_distant_chat
            jump adversary_1_empty_leave

        "{i}• [[Attempt to free the Princess.]{/i}" if adversary_free_offer and blade_held:
            jump adversary_free_attempt

        "{i}• [[Turn around and leave without saying anything.]{/i}" if adversary_can_fury:
            if fury_encountered:
                $ adversary_can_fury = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                #voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                #hero "Wait... what?!\n"
                jump adversary_1_distant_chat
            jump adversary_1_empty_leave

label adversary_1_narrator_accepts:

    default adversary_1_narrator_accepts_origin = ""

    $ adversary_1_narrator_proof = True
    if adversary_1_forest_share_loop:
        voice "audio/voices/ch2/adversary/_shared/narrator/12.flac"
        n "All right. Fine. I believe you.\n"
    else:
        voice "audio/voices/ch2/adversary/_shared/narrator/13.flac"
        n "All right. Fine. If you're not going to address it, I will.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/11.flac"
    hero "What?\n"
    if adversary_1_forest_share_loop:
        voice "audio/voices/ch2/adversary/_shared/narrator/14.flac"
        n "What you said earlier in the woods. I believe you. You've already met the Princess, and the Princess has already met you. But that's all the more reason to take this seriously.\n"
    else:
        voice "audio/voices/ch2/adversary/_shared/narrator/15a.flac"
        n "You've already met the Princess, the Princess has already met you, and the two of you killed each other. Did you think that you'd be able to just... openly talk about all of that without me noticing?\n"
        voice "audio/voices/ch2/adversary/_shared/hero/12.flac"
        hero "... maybe? You did seem to just gloss over the whole thing for a while.\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/16a.flac"
        n "Of course I glossed over it! When a colleague says something insane, 'glossing over it' is one of the best ways to stay focused and keep moving forward. But enough is enough. I believe you. And that's all the more reason to take this seriously.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/17a.flac"
    n "You don't know that whatever brought the two of you back to life isn't a fluke. And beyond that, do you know who doesn't remember anything that happened last time? Me. I. Don't. Remember.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/13.flac"
    hero "Are... are you okay?\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/18.flac"
    n "Of course I'm not okay! As far as we're all concerned, the fate of {i}my{/i} world is still very much on the line. Not all of us have the luxury of jumping over to a parallel universe the second we die.\n"
    menu:
        extend ""

        "{i}• Just because it bothers you, I'm going to take this even less seriously. You don't know the depths of my apathy!{/i}":
            voice "audio/voices/ch2/adversary/_shared/narrator/19.flac"
            n "You're joking, right? I'm just going to pretend that you're joking.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/10.flac"
            stubborn "Yeah. You'd better be joking. We can't win unless you take this seriously.\n"

        "{i}• (Lie) No. I don't know what you're talking about, I've never died. Do you see how alive I am right now? Would someone as alive as me already have died? I didn't think so.{/i}":
            voice "audio/voices/ch2/adversary/_shared/narrator/20.flac"
            n "Don't try to lie to me. Just please, take this seriously.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/11.flac"
            stubborn "Agreed. We can't win unless you treat this fight with the gravity it deserves.\n"

        "{i}• Don't worry. I'm going to do a good job!{/i}":
            voice "audio/voices/ch2/adversary/_shared/narrator/21.flac"
            n "Great. Now focus up and do it, then.\n"

        "{i}• You got me. Pretty much everything you just said is true.{/i}":
            voice "audio/voices/ch2/adversary/_shared/narrator/22.flac"
            n "I know. You and the Princess have been talking about it.\n"
            voice "audio/voices/ch2/adversary/_shared/hero/14.flac"
            hero "You don't have to be so snarky...\n"

        "{i}• [[Remain silent.]{/i}":
            voice "audio/voices/ch2/adversary/_shared/narrator/23.flac"
            n "I'm going to take that silence as a sign that from this moment on, you're going to treat the task before you with utmost importance and seriousness. I'm so glad that we're finally all on the same page.\n"

    if adversary_1_narrator_accepts_origin == "distant":
        jump adversary_1_distant_chat
    elif adversary_1_narrator_accepts_origin == "close":
        jump adversary_1_close_menu
    # if then block takes you back

label adversary_1_close_join:
    play audio "audio/one_shot/footsteps_stone.flac"
    $ quick_menu = False
    $ adversary_1_narrator_accepts_origin = "close"
    hide adversary onlayer back
    hide bg onlayer back
    hide farback onlayer farback
    show bg adversary throat grab onlayer back at Position(ypos=1125)
    show adversary c neutral onlayer front at Position(ypos=1125)
    if adversary_1_chains_broken == False:
        show chain adversary c neutral onlayer front
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    if blade_held == False:
        voice "audio/voices/ch2/adversary/_shared/narrator/24.flac"
        n "You take a cautious step towards the Princess. Unarmed. I wish I could believe you know what you're doing, but you clearly don't.\n"
    else:
        voice "audio/voices/ch2/adversary/_shared/narrator/25.flac"
        n "Blade held tight in your hand, you take a cautious step towards the Princess.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/26.flac"
    n "You stop a few feet short of her reach, her chains taut as she stares down at you.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/15.flac"
    hero "She's a lot bigger than I thought she was.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/12.flac"
    stubborn "Why do you sound so scared? We can take her.\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_23.flac"
    show adversary c neutral talk onlayer front at Position(ypos=1125)
    if adversary_1_chains_broken == False:
        show chain adversary c neutral onlayer front
    with dissolve
    sp "Well? What do you want? Because every second we waste talking is a second we could spend killing each other instead.\n"
    show adversary c neutral onlayer front at Position(ypos=1125)
    if adversary_1_chains_broken == False:
        show chain adversary c neutral onlayer front
    label adversary_1_close_menu:
        default adversary_why_violence = False
        default adversary_spar_offer = False
        default adversary_no_end = False
        default adversary_ask_free = False
        default adversary_ask_rebirth = False
        default adversary_close_why = False
        default adversary_close_purpose = False
        menu:
            extend ""

            "{i}• (Explore) ''Why do you want us to kill each other?''{/i}" if adversary_why_violence == False and adversary_spar_offer == False:
                $ adversary_why_violence = True
                voice "audio/voices/ch2/adversary/_shared/princess/adv_24.flac"
                show adversary c confused talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c bored onlayer front
                with dissolve
                sp "Why wouldn't I want that? Why don't {i}you{/i} want that? It felt good last time. It felt right!\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_25.flac"
                show adversary c neutral talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                with dissolve
                sp "And it makes sense.\n"
                show adversary c neutral onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                if adversary_1_narrator_proof == False:
                    $ adversary_1_narrator_accepts_origin = "close"
                    jump adversary_1_narrator_accepts
                jump adversary_1_close_menu

            "{i}• (Explore) ''Can't we just... I don't know, spar a little? Maybe there's a compromise where we can all get what we want, nobody has to die, and the world doesn't have to end.''{/i}" if adversary_spar_offer == False:
                $ adversary_spar_offer = True
                voice "audio/voices/ch2/adversary/_shared/princess/adv_26.flac"
                show adversary c bored talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c bored onlayer front
                with dissolve
                sp "Sparring? That's just play-fighting. It isn't real.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_27aa.flac"
                show adversary c cocky talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c cocky onlayer front
                with dissolve
                sp "What's real is when my flesh splits open. What's real is when you keep getting up until your legs can't hold you.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_27ab.flac"
                show adversary c excited talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                with dissolve
                sp "What's real are the things we do to each other when the only options left are winning and dying.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_28.flac"
                show adversary c neutral talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                with dissolve
                sp "That is the only thing I'm interested in.\n"
                show adversary c neutral onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                jump adversary_1_close_menu

            "{i}• (Explore) ''If all you want to do is fight me, does that mean you won't end the world?''{/i}" if adversary_no_end == False:
                $ adversary_no_end = True
                voice "audio/voices/ch2/adversary/_shared/princess/adv_29.flac"
                show adversary c excited talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                with dissolve
                sp "The world. Ha! If there's a world, I haven't seen it. There's you, and there's me, and there's the ground beneath our feet.\n"
                if basement_1_shared_task:
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_30.flac"
                    show adversary c bored talk onlayer front at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary c bored onlayer front
                    with dissolve
                    sp "Besides, I thought we went over this last time. I never wanted to end the world.\n"
                    show adversary c bored onlayer front at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary c bored onlayer front
                    if adversary_1_narrator_proof == False:
                        $ adversary_1_narrator_accepts_origin = "close"
                        jump adversary_1_narrator_accepts
                else:
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_31.flac"
                    show adversary c confused talk onlayer front at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary c bored onlayer front
                    with dissolve
                    sp "Why would I care about ending something I've never seen?\n"
                    show adversary c confused onlayer front at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary c bored onlayer front
                jump adversary_1_close_menu

            "{i}• (Explore) ''So you're just... fine locked away in here? You really don't want to be free?''{/i}" if adversary_ask_free == False and adversary_1_chains_broken == False and adversary_free_offer:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_32.flac"
                show adversary c bored talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c bored onlayer front
                with dissolve
                sp "Here you go again talking about my 'freedom.'\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/27.flac"
                show adversary c glance chains onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    hide chain onlayer front
                with dissolve
                n "The Princess glances down at her chains.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_33.flac"
                sp "If you're talking about these, they're nothing.\n"
                jump adversary_1_close_free_join

            "{i}• (Explore) ''Don't you want to be free?''{/i}" if adversary_ask_free == False and adversary_1_chains_broken == False and adversary_free_offer == False:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_34.flac"
                show adversary c confused talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c bored onlayer front
                with dissolve
                sp "Free?\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/27.flac"
                show adversary c glance chains onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    hide chain onlayer front
                with dissolve
                n "The Princess glances down at her chains.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_35.flac"
                show adversary c cocky talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c cocky onlayer front at Position(ypos=1125)
                with dissolve
                sp "Oh, you mean these? They're just metal. They're nothing.\n"
                label adversary_1_close_free_join:
                    $ adversary_1_chains_broken = True
                    $ adversary_free_offer = True
                    $ adversary_ask_free = True
                    voice "audio/voices/ch2/adversary/_shared/narrator/28.flac"
                    play audio "audio/final/Beast_ChainsFastDrag_1.flac"
                    play secondary "audio/one_shot/footsteps_stone.flac"
                    hide chain onlayer front
                    show adversary c chains pull onlayer front
                    with dissolve
                    n "She steps forward, her bindings creaking under the pressure of her strength.\n"
                    play audio "audio/final/Adversary_ChainSTressBreaking_2.flac"
                    voice "audio/voices/ch2/adversary/_shared/narrator/28a.flac"
                    show adversary c chains snap onlayer front
                    with dissolve
                    n "And then they snap. It was only a matter of time, but she's loose.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/16.flac"
                    show adversary c cocky onlayer front
                    with dissolve
                    hero "Dear lord, what do we do?\n"
                    if blade_held:
                        voice "audio/voices/ch2/adversary/_shared/narrator/29.flac"
                        n "You took the blade. How about you use it?\n"
                        voice "audio/voices/ch2/adversary/_shared/stubborn/13.flac"
                        stubborn "Exactly. We do exactly what I've been telling you to do since the second we got here. We fight her, we kill her, we win.\n"
                    else:
                        voice "audio/voices/ch2/adversary/_shared/narrator/71.flac"
                        n "Oh, if only there were some sort of weapon you could use to fight a world-ending monstrosity... I wonder where you might find one of those.\n"
                        voice "audio/voices/ch2/adversary/_shared/stubborn/14.flac"
                        stubborn "Just do exactly what I've been telling you to do since the second we got here. Take the blade, fight her, kill her, and {i}win{/i}.\n"
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_36.flac"
                    show adversary c cocky talk onlayer front
                    with dissolve
                    sp "What, did you think you were safe standing right outside my grasp? The only reason I haven't drawn blood is because I want to make sure that your heart is in it. I don't like fighting someone with a weak spirit.\n"
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_37.flac"
                    show adversary c excited onlayer front
                    with dissolve
                    sp "But go ahead. Keep trying my patience.\n"
                    jump adversary_1_close_menu

            "{i}• (Explore) ''What happened after you died?''{/i}" if adversary_ask_rebirth == False:
                $ adversary_ask_rebirth = True
                voice "audio/voices/ch2/adversary/_shared/princess/adv_38.flac"
                show adversary c confused talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c bored onlayer front at Position(ypos=1125)
                with dissolve
                sp "I woke up. Didn't you?\n"
                show adversary c neutral onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front at Position(ypos=1125)
                with dissolve
                label adversary_1_close_post_death_menu:
                    default adversary_1_count = 0
                    default adversary_1_close_no_wounds = False
                    default adversary_1_close_different = False
                    default adversary_1_basement_different = False
                    default adversary_1_close_single_file = False
                    default adversary_1_close_bother = False
                    if adversary_1_count >= 5:
                        jump adversary_1_close_menu
                    menu:
                        extend ""

                        "{i}• (Explore) ''Or... we could just walk single-file out of here.''{/i}" if adversary_1_close_single_file == False and adversary_1_basement_different:
                            $ adversary_1_count += 1
                            $ adversary_1_close_single_file = True
                            voice "audio/voices/ch2/adversary/_shared/hero/17.flac"
                            show adversary c confused onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c bored onlayer front
                            with dissolve
                            hero "That's right. Not everything has to be so violent.\n"
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_43.flac"
                            show adversary c frustrated talk onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c neutral onlayer front
                            with dissolve
                            sp "That's pathetic. I would never do that, and I hate that you even suggested it.\n"
                            show adversary c frustrated onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c neutral onlayer front
                            with dissolve
                            jump adversary_1_close_post_death_menu

                        "{i}• (Explore) ''You don't have any wounds...''{/i}" if adversary_1_close_no_wounds == False:
                            $ adversary_1_count += 1
                            $ adversary_1_close_no_wounds = True
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_39a.flac"
                            show adversary c neutral talk onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c neutral onlayer front
                            with dissolve
                            sp "You don't either.\n"
                            show adversary c neutral onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c neutral onlayer front
                            jump adversary_1_close_post_death_menu

                        "{i}• (Explore) ''You're different...''{/i}" if adversary_1_close_different == False:
                            $ adversary_1_count += 1
                            $ adversary_1_close_different = True
                            if adversary_different_comment:
                                voice "audio/voices/ch2/adversary/_shared/princess/adv_40.flac"
                                show adversary c bored talk onlayer front at Position(ypos=1125)
                                if adversary_1_chains_broken == False:
                                    show chain adversary c bored onlayer front
                                with dissolve
                                sp "I know. You already told me.\n"
                                show adversary c bored onlayer front at Position(ypos=1125)
                                if adversary_1_chains_broken == False:
                                    show chain adversary c bored onlayer front
                            else:
                                $ adversary_different_comment = True
                                voice "audio/voices/ch2/adversary/_shared/princess/adv_41.flac"
                                show adversary c excited talk onlayer front at Position(ypos=1125)
                                if adversary_1_chains_broken == False:
                                    show chain adversary c neutral onlayer front
                                with dissolve
                                sp "You aren't.\n"
                                show adversary c excited onlayer front at Position(ypos=1125)
                                if adversary_1_chains_broken == False:
                                    show chain adversary c neutral onlayer front
                            jump adversary_1_close_post_death_menu

                        "{i}• (Explore) ''The basement is different.''{/i}" if adversary_1_basement_different == False:
                            $ adversary_1_count += 1
                            $ adversary_1_basement_different = True
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_42.flac"
                            show adversary c cocky talk onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c cocky onlayer front
                            with dissolve
                            sp "I like it. It's so cramped. Like the only way out of here is through each other.\n"
                            show adversary c cocky onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c cocky onlayer front
                            jump adversary_1_close_post_death_menu

                        "{i}• (Explore) ''Doesn't any of this bother you? Don't you care about what you are?''{/i}" if adversary_1_close_bother == False:
                            $ adversary_1_close_bother = True
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_44.flac"
                            show adversary c frustrated talk onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c neutral onlayer front
                            with dissolve
                            sp "Gah! I care, okay? I guess I just care differently than you. When I saw you come back down here, I thought you would understand! I thought that we would want the same thing.\n"
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_45.flac"
                            show adversary c confused talk onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c bored onlayer front
                            with dissolve
                            sp "But all you've done is ask me annoying little questions. It's like you don't even want to enjoy being alive.\n"
                            voice "audio/voices/ch2/adversary/_shared/stubborn/15.flac"
                            show adversary c confused onlayer front at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary c bored onlayer front
                            stubborn "I wish she could hear ME right now. I want to enjoy being alive! I want to fight!\n"
                            jump adversary_1_close_post_death_menu

                        "{i}• [[Leave it at that.]{/i}":
                            if adversary_1_narrator_proof == False:
                                $ adversary_1_narrator_accepts_origin = "close"
                                jump adversary_1_narrator_accepts
                            jump adversary_1_close_menu

            "{i}• (Explore) ''We have to figure out why we're here.''{/i}" if adversary_close_why == False and adversary_close_purpose == False:
                $ adversary_close_why = True
                voice "audio/voices/ch2/adversary/_shared/princess/adv_46.flac"
                show adversary c confused talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c bored onlayer front
                with dissolve
                sp "We don't, because I know why we're here. We're here to kill each other.\n"
                voice "audio/voices/ch2/adversary/_shared/hero/18a.flac"
                show adversary c confused onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c bored onlayer front
                hero "'We're here to kill {b}each other{/b}?' It sounds like she doesn't care if she dies here. Maybe we can use that to our advantage.\n"
                #voice "audio/voices/ch2/adversary/_shared/narrator/31.flac"
                #n "How astute, and at least a little unexpected. You shouldn't trust her to keep her word, but the little voice has a point.\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/16.flac"
                stubborn "How boring. I'm not interested in watching you try and outwit her, I'm interested in overpowering her. We shouldn't need to use any dirty little tricks to win.\n"
                menu:
                    extend ""

                    "{i}• ''I don't mean 'why are we here existentially', I mean, quite literally, why are you in this basement? Who sent me here to kill you? Why me? Why you? There are answers out there and we need to find them.''{/i}":
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_47a.flac"
                        show adversary c cocky talk onlayer front at Position(ypos=1125)
                        if adversary_1_chains_broken == False:
                            show chain adversary c cocky onlayer front
                        with dissolve
                        sp "And then what? I'm still going to want to coat these walls in our blood. I know what I am. I don't need answers.\n"
                        show adversary c cocky onlayer front at Position(ypos=1125)
                        if adversary_1_chains_broken == False:
                            show chain adversary c cocky onlayer front
                        with dissolve
                        jump adversary_1_close_menu

                    "{i}• ''You were put down here for a reason. I was sent to kill you for a reason. Don't you care what that reason is?''{/i}":
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_48.flac"
                        show adversary c cocky talk onlayer front at Position(ypos=1125)
                        if adversary_1_chains_broken == False:
                            show chain adversary c cocky onlayer front
                        with dissolve
                        sp "I don't need to care, because I already know what I am. I've already found my purpose.\n"
                        show adversary c cocky onlayer front at Position(ypos=1125)
                        if adversary_1_chains_broken == False:
                            show chain adversary c cocky onlayer front
                        jump adversary_1_princess_grin

                    "{i}• ''We're here because some people want me to kill you.''{/i}":
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_49.flac"
                        show adversary c cocky talk onlayer front at Position(ypos=1125)
                        if adversary_1_chains_broken == False:
                            show chain adversary c cocky onlayer front
                        with dissolve
                        sp "Who cares what 'people' want? I know what I am. I've found my purpose.\n"
                        show adversary c cocky onlayer front at Position(ypos=1125)
                        jump adversary_1_princess_grin

                    "{i}• ''We're here because you're supposed to be a threat to the world. I need to find out if that's true, and if it is true, I have to find out why.''{/i}" if adversary_no_end == False:
                        $ adversary_no_end = True
                        voice "audio/voices/ch2/adversary/_shared/princess/adv_50.flac"
                        show adversary c excited talk onlayer front at Position(ypos=1125)
                        if adversary_1_chains_broken == False:
                            show chain adversary c neutral onlayer front
                        with dissolve
                        sp "The world. Ha! If there's a world I haven't seen it. There's you, and there's me, and there's the ground beneath our feet.\n"
                        voice "audio/voices/ch2/adversary/_shared/hero/19a.flac"
                        show adversary c excited onlayer front at Position(ypos=1125)
                        hero "Okay, that's not right. There's definitely a world. We've seen it with our own eyes!\n"
                        voice "audio/voices/ch2/adversary/_shared/narrator/32.flac"
                        n "That's right. Don't let her drop the stakes of this situation.\n"
                        voice "audio/voices/ch2/adversary/_shared/stubborn/17a.flac"
                        stubborn "That's right, it's good to have a goal. It's good to have something to fight for.\n"
                        jump adversary_1_close_menu

                    "{i}• [[Leave it at that.]{/i}":
                        jump adversary_1_close_menu

            "{i}• (Explore) ''You were put down here for a reason. I was sent to kill you for a reason. Don't you care what that reason is?''{/i}" if adversary_close_purpose == False:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_51.flac"
                show adversary c cocky talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c cocky onlayer front
                with dissolve
                sp "I don't need to care, because I already know what I am. I've already found my purpose.\n"
                jump adversary_1_princess_grin

            "{i}• (Explore) ''The last time we talked, you seemed to care about why you were here. What made you stop caring?''{/i}" if basement_1_shared_task and adversary_close_purpose == False:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_52.flac"
                show adversary c cocky talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c cocky onlayer front
                with dissolve
                sp "I stopped caring because I found my purpose.\n"
                label adversary_1_princess_grin:
                    $ adversary_close_purpose = True
                    voice "audio/voices/ch2/adversary/_shared/narrator/33.flac"
                    show adversary c excited onlayer front at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary c neutral onlayer front
                    with dissolve
                    n "The Princess flashes a sinister grin.\n"
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_53.flac"
                    show adversary c excited talk onlayer front at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary c neutral onlayer front
                    with dissolve
                    sp "You.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/20b.flac"
                    show adversary c excited onlayer front at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary c neutral onlayer front
                    with dissolve
                    hero "Does she mean... her purpose is killing us?\n"
                    voice "audio/voices/ch2/adversary/_shared/stubborn/18.flac"
                    stubborn "No, she means {i}fighting{/i} us. She means both of us getting stronger through sheer pain and will, with the fear of death no longer able to hold us back.\n"
                    if blade_held:
                        voice "audio/voices/ch2/adversary/_shared/stubborn/19.flac"
                        stubborn "Just start stabbing her already! I'm sick of all this anticipation. We're {i}ready{/i}.\n"
                    else:
                        voice "audio/voices/ch2/adversary/_shared/stubborn/20.flac"
                        stubborn "Just go and pick up the blade already. I'm sick of all this anticipation. We're {i}ready{/i}.\n"
                    jump adversary_1_close_menu

            "{i}• [[Attack the Princess.]{/i}" if blade_held:
                jump adversary_1_fight

            "{i}• ''Fine. If you want a fight, I'll give you a fight.'' [[Attack the Princess.]{/i}" if blade_held:
                jump adversary_1_fight

            "{i}• ''Fine. If you want a fight, I'll give you a fight. I'll be right back.'' [[Retrieve the knife to Slay the Princess.]{/i}" if adversary_1_cabin_blade_taken == False:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_54.flac"
                sp "I'll be waiting, but you'd better not be wasting my time.\n"
                jump adversary_1_retrieve_knife

            "{i}• ''I'm not going to fight you.''{/i}" if adversary_can_fury:
                if fury_encountered:
                    $ adversary_can_fury = False
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump adversary_1_close_menu
                $ adversary_1_narrator_accepts_origin = "close"
                jump adversary_1_refuse

            "{i}• [[Attempt to free the Princess.]{/i}" if (adversary_free_offer or adversary_close_why or adversary_close_purpose) and blade_held and adversary_1_chains_broken == False:
                jump adversary_free_attempt

            "{i}• [[Turn around and leave.]{/i}" if adversary_can_fury:
                if fury_encountered:
                    $ adversary_can_fury = False
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump adversary_1_close_menu
                jump adversary_1_empty_leave

            "{i}• [[Remain silent.]{/i}" if adversary_can_fury:
                if fury_encountered:
                    $ adversary_can_fury = False
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump adversary_1_close_menu
                $ adversary_1_narrator_accepts_origin = "close"
                jump adversary_1_refuse

label adversary_1_flee:
    stop music fadeout 1.0
    default adversary_1_flee_die_choice = False
    label adversary_1_empty_leave:
        voice "audio/voices/ch2/adversary/_shared/princess/adv_55.flac"
        if adversary_1_narrator_accepts_origin == "close":
            show adversary c frustrated talk onlayer front at Position(ypos=1125)
            if adversary_1_chains_broken == False:
                show chain adversary c neutral onlayer front
            with dissolve
        elif adversary_1_narrator_accepts_origin == "chains":
            show adversary d loose onlayer back
        else:
            show adversary d crossed talk onlayer back at Position(ypos=1125)
            with dissolve
        sp "Oh, you've got another thing coming if you think you can just turn around and leave.\n"
        play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
        if adversary_1_chains_broken == False:
            $ adversary_1_chains_broken = True
            play audio "audio/final/Beast_ChainsFastDrag_1.flac"
            voice "audio/voices/ch2/adversary/_shared/narrator/34.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide adversary onlayer front
            hide adversary onlayer back
            hide chain onlayer front
            show farback adversary basement onlayer farback at Position(ypos=1125)
            show bg adversary chains onlayer back at Position(ypos=1125)
            show adversary d chains pull onlayer back at Position(ypos=1125)
            with dissolve
            n "As you step towards the stairs, you hear the heavy creak of straining metal.\n{w=4.0}{nw}"
            show screen disableclick(0.5)
            play audio "audio/final/Adversary_ChainSTressBreaking_2.flac"
            voice "audio/voices/ch2/adversary/_shared/narrator/34a.flac"
            show adversary d chains snap onlayer back at Position(ypos=1125)
            with dissolve
            n "And then a snap. She's loose. You have to make a decision, and you have to make it fast.\n"
            show bg adversary chains onlayer back at Position(ypos=1125)
            show adversary d loose onlayer back at Position(ypos=1125)
            with dissolve
            menu:
                extend ""

                "{i}• (Explore) Okay, team. What are we thinking?{/i}":
                    voice "audio/voices/ch2/adversary/_shared/hero/21a.flac"
                    play audio "audio/final/adversary_charge.flac"
                    hide adversary onlayer back
                    show adversary charge onlayer front at Position(ypos=1125)
                    with dissolve
                    hero "Er, how about we get the hell out of—\n{w=2.31}{nw}"
                    show screen disableclick(0.5)
                    voice "audio/voices/ch2/adversary/_shared/narrator/35b.flac"
                    $ blade_held = False
                    $ default_mouse = "default"
                    play audio "audio/one_shot/knife_bounce_several.flac"
                    play secondary "audio/final/Adversary_BodySMashedAgainstWall_3.flac"
                    scene bg black
                    hide adversary onlayer front
                    hide farback onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    n "But the little voice doesn't have the chance to finish that thought before the Princess barrels into you and smashes your body into the rough stone wall.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/22a.flac"
                    hero "Can I finish my thought now?\n"
                    voice "audio/voices/ch2/adversary/_shared/narrator/36.flac"
                    n "Sure. Why not?\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/23.flac"
                    hero "... here.\n"
                    voice "audio/voices/ch2/adversary/_shared/narrator/37.flac"
                    stop sound fadeout 20.0
                    stop music fadeout 20.0
                    stop secondary fadeout 20.0
                    n "So glad we could stick around to hear the end of that. But I'm afraid that's all the time you had left. Why, for the love of everything, did you stop to think? What did you expect you'd come up with?\n"
                    label adversary_1_flee_die_join:
                        voice "audio/voices/ch2/adversary/_shared/narrator/38.flac"
                        n "{i}Sigh{/i}. It doesn't matter, because everything goes dark, and you die. Great job.\n"
                        voice "audio/voices/ch2/adversary/_shared/stubborn/21.flac"
                        stubborn "No, come on. We can't be dead! We didn't even get a chance to fight her...\n"
                        stop music fadeout 5.0
                        stop sound fadeout 5.0
                        stop secondary fadeout 5.0
                        stop tertiary fadeout 5.0
                        if adversary_1_flee_die_choice:
                            voice "audio/voices/ch2/adversary/_shared/narrator/39.flac"
                            n "I'm not the one who decided you should die here. If you have a problem, take it up with the one making the choices.\n"
                        if adversary_1_narrator_proof:
                            voice "audio/voices/ch2/adversary/_shared/narrator/40.flac"
                            n "Dead is dead, but maybe you'll have better luck next time.\n"
                        else:
                            voice "audio/voices/ch2/adversary/_shared/narrator/41.flac"
                            n "Dead is dead.\n"

                        $ fury_source = "death_downstairs"
                        jump fury_start
                        # END - leads to broken dury ch 3

                "{i}• [[Turn and fight her head-on.]{/i}" if blade_held:
                    $ adversary_1_style = "direct"
                    #voice "audio/voices/ch2/adversary/_shared/narrator/42.flac"
                    play audio "audio/one_shot/footstep_run_dirt_short.flac"
                    hide adversary onlayer back
                    hide adversary onlayer front
                    hide farback onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    scene bg adversary readying onlayer back at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary readying onlayer front at Position(ypos=1125)
                    show adversary readying onlayer front at Position(ypos=1125)
                    with dissolve
                    #n "As the Princess breaks free, you launch off the wet stone floor and catapult headlong towards her.\n"
                    jump adversary_1_fight

                "{i}• [[Dodge to the side and counter-attack.]{/i}" if blade_held:
                    $ adversary_1_style = "agile"
                    jump adversary_1_fight_agile

                "{i}• [[Run like hell.]{/i}":
                    $ quick_menu = False
                    play audio "audio/final/adversary_charge.flac"
                    voice "audio/voices/ch2/adversary/_shared/narrator/43.flac"
                    hide adversary onlayer back
                    hide adversary onlayer front
                    hide farback onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    scene bg black
                    with fade
                    if persistent.quick_menu:
                        $ quick_menu = True
                    n "You do your best to scramble up the stairs before the Princess can reach you.\n"
                    if blade_held:
                        voice "audio/voices/ch2/adversary/_shared/stubborn/22.flac"
                        stubborn "You coward!\n"
                    voice "audio/voices/ch2/adversary/_shared/narrator/44.flac"
                    play audio "audio/one_shot/door_stone.flac"
                    n "You can practically feel her steamy breath on the back of your neck, but you manage, just barely, to throw yourself over the threshold and slam the heavy stone doors behind you.\n"
                    jump adversary_1_upstairs

                "{i}• [[Die.]{/i}":
                    $ adversary_1_flee_die_choice = True
                    play audio "audio/final/adversary_charge.flac"
                    hide adversary onlayer back
                    show adversary charge onlayer front at Position(ypos=1125)
                    with dissolve
                    $ renpy.pause(0.75)
                    label adversary_1_flee_die_action:
                        voice "audio/voices/ch2/adversary/_shared/narrator/45.flac"
                        $ blade_held = False
                        $ default_mouse = "default"
                        play audio "audio/one_shot/knife_bounce_several.flac"
                        play secondary "audio/final/Adversary_BodySMashedAgainstWall_3.flac"
                        scene bg black
                        hide adversary onlayer front
                        hide adversary onlayer back
                        hide farback onlayer back
                        hide farback onlayer farback
                        hide bg onlayer back
                        n "Are you... {i}sigh{/i}. Okay. The Princess barrels into you and smashes your body into the rough stone wall.\n"
                        voice "audio/voices/ch2/adversary/_shared/narrator/46.flac"
                        n "Why, for the love of everything, did you decide to do {b}that{/b}?\n"
                        jump adversary_1_flee_die_join

        else:
            voice "audio/voices/ch2/adversary/_shared/narrator/47.flac"
            play audio "audio/final/adversary_charge.flac"
            hide adversary onlayer back
            show adversary charge onlayer front at Position(ypos=1125)
            with dissolve
            play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
            n "As you step towards the stairs, you hear thundering footfalls as the Princess barrels towards you.\n"
            voice "audio/voices/ch2/adversary/_shared/hero/24.flac"
            hero "Let's get out of here, quick!\n"
            if blade_held:
                voice "audio/voices/ch2/adversary/_shared/stubborn/23a.flac"
                stubborn "Turn around and fight her. It's the only way out of this!\n"
            else:
                voice "audio/voices/ch2/adversary/_shared/stubborn/24.flac"
                stubborn "The blade's still upstairs. Getting it is the only thing that matters right now.\n"

            menu:
                extend ""

                "{i}• [[Turn and fight.]{/i}" if blade_held:
                    voice "audio/voices/ch2/adversary/_shared/narrator/48.flac"
                    $ blade_held = False
                    $ default_mouse = "default"
                    play audio "audio/one_shot/knife_bounce_several.flac"
                    play secondary "audio/final/Adversary_BodySMashedAgainstWall_3.flac"
                    scene bg black
                    hide adversary onlayer front
                    hide adversary onlayer back
                    hide farback onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    n "But you don't get a chance to turn around and fight before the Princess barrels into you and smashes your body into the rough stone wall.\n"
                    label adversary_1_flee_free_stopped_join:
                        voice "audio/voices/ch2/adversary/_shared/narrator/49.flac"
                        n "You shouldn't have let her break out of her bindings. Why didn't you listen to me?\n"
                        jump adversary_1_flee_die_join

                "{i}• [[Run like hell.]{/i}":
                    label adversary_flee_late_join:
                        voice "audio/voices/ch2/adversary/_shared/narrator/50.flac"
                        $ blade_held = False
                        $ default_mouse = "default"
                        play audio "audio/one_shot/knife_bounce_several.flac"
                        play secondary "audio/final/Adversary_BodySMashedAgainstWall_3.flac"
                        scene bg black
                        hide adversary onlayer front
                        hide adversary onlayer back
                        hide farback onlayer back
                        hide farback onlayer farback
                        hide bg onlayer back
                        n "But you don't get a chance to run for the stairs before the Princess, loose from her chains, barrels into you and smashes your body to pieces against the wall.\n"
                    jump adversary_1_flee_free_stopped_join

                "{i}• [[Die.]{/i}":
                    jump adversary_1_flee_die_action

label adversary_1_upstairs:
    $ quick_menu = False
    voice "audio/voices/ch2/adversary/_shared/narrator/51.flac"
    scene farback adversary cabin onlayer farback at Position(ypos=1125)
    show bg adversary cabin onlayer back at Position(ypos=1125)
    show door adversary1 onlayer back at Position(ypos=1125)
    show table adversary onlayer back at Position(ypos=1125)
    if blade_held == False:
        show knife adversary onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You're safe. If only for a moment.\n"
    if blade_held == False:
        voice "audio/voices/ch2/adversary/_shared/stubborn/25.flac"
        stubborn "The blade. Take the blade from the altar.\n"
        menu:
            extend ""

            "{i}• [[Take the blade.]{/i}" if blade_held == False:
                $ blade_held = True
                $ default_mouse = "blade"
                play audio "audio/one_shot/knife_pickup.flac"
                voice "audio/voices/ch2/adversary/_shared/narrator/52.flac"
                hide knife onlayer back with dissolve
                n "You take the blade from the altar.\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/26.flac"
                stubborn "Finally!\n"

            "{i}• [[You're fine just the way you are, thank you.]{/i}":
                voice "audio/voices/ch2/adversary/_shared/hero/25.flac"
                hero "Are you sure about that?\n"

    voice "audio/voices/ch2/adversary/_shared/princess/adv_56.flac"
    sp "Do you think this door is enough to hold me? You're not getting out of this. I don't care how many things I have to break. I'm getting the fight I want.\n"
    label adversary_1_upstairs_late_join:
        default adversary_1_upstairs_flag = False
        $ adversary_1_upstairs_flag = True
        voice "audio/voices/ch2/adversary/_shared/narrator/53.flac"
        play audio "audio/final/Adversary_HoleBeingPunchesRock_1.flac"
        show bg black with hpunch
        n "The entire cabin shakes as the Princess throws herself against the basement door.\n"
        if adversary_1_retrieve_knife_explore == False:
            voice "audio/voices/ch2/adversary/_shared/hero/26a.flac"
            hero "It's huge and made of stone. We're fine... right?\n"
        else:
            voice "audio/voices/ch2/adversary/_shared/hero/27.flac"
            hero "We're fine... right?\n"
        if blade_held:
            voice "audio/voices/ch2/adversary/_shared/stubborn/27.flac"
            stubborn "Of course we are. Any second now she's going to break through that entryway, and we're finally going to get to do what we came here to do.\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/54.flac"
            play audio "audio/final/Adversary_HoleBeingPunchesRock_2.flac"
            show door adversary crack1 onlayer back with hpunch
            n "Another impact shakes the cabin, a massive gash splitting its way up the stone doors.\n"
        else:
            voice "audio/voices/ch2/adversary/_shared/stubborn/28.flac"
            stubborn "If we had a weapon we'd be fine.\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/55.flac"
            n "Yes, you should probably pick up the blade, shouldn't you?\n"
            voice "audio/voices/ch2/adversary/_shared/hero/28.flac"
            hero "I know I'd feel a lot safer with it.\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/56.flac"
            play audio "audio/final/Adversary_HoleBeingPunchesRock_2.flac"
            show door adversary crack1 onlayer back with hpunch
            n "But before you can act, another impact shakes the cabin, a massive gash splitting its way up the stone doors.\n"
        voice "audio/voices/ch2/adversary/_shared/stubborn/29.flac"
        play audio "audio/final/Adversary_HoleBeingPunchesRock_3.flac"
        show door adversary crack2 onlayer back with hpunch
        stubborn "Here she comes.\n"
        $ gallery_adversary.unlock_item(4)
        $ renpy.save_persistent()
        voice "audio/voices/ch2/adversary/_shared/narrator/57.flac"
        play audio "audio/final/_adversary_door_explode.flac"
        show door adversary shatter1 onlayer back with hpunch
        with dissolve
        $ renpy.pause(0.5)
        voice sustain
        hide door onlayer back
        show adversary doorway onlayer back at Position(ypos=1125)
        show door adversary shatter2 onlayer back at Position(ypos=1125)
        with Dissolve(1.0)
        n "The doors explode outwards, shards of stone clattering against the walls as the Princess emerges from the basement.\n"
        if blade_held and adversary_1_cabin_blade_taken == False:
            voice "audio/voices/ch2/adversary/_shared/princess/adv_57.flac"
            show adversary cabin excited onlayer back with dissolve
            sp "At least you finally have a weapon. Good.\n"
        elif blade_held:
            voice "audio/voices/ch2/adversary/_shared/princess/adv_58.flac"
            show adversary cabin disappointed talk onlayer back with dissolve
            sp "Stop. Running.\n"
        else:
            voice "audio/voices/ch2/adversary/_shared/princess/adv_59.flac"
            show adversary cabin disappointed talk onlayer back with dissolve
            sp "After everything we've been through, I can't believe this is going to end with you cowering in a corner. You're pathetic.\n"


        voice "audio/voices/ch2/adversary/_shared/hero/29.flac"
        hero "We're doomed.\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/58.flac"
        play audio "audio/final/adversary_charge.flac"
        hide adversary onlayer back
        show adversary charge cabin onlayer front at Position(ypos=1125)
        n "In a fit of violence, the Princess explodes across the room and closes the gap between you.\n"
        if blade_held:
            if adversary_1_wounded:
                default adversary_upstairs_fury = False
                $ adversary_upstairs_fury = True
                voice "audio/voices/ch2/adversary/_shared/narrator/59.flac"
                $ default_mouse = "blood"
                play audio "audio/final/Adversary_ABackAndForth_1.flac"
                hide adversary onlayer front
                hide door onlayer back
                hide bg onlayer back
                hide knife onlayer back
                hide table onlayer back
                hide farback onlayer back
                hide farback onlayer farback
                scene bg adversary throat grab onlayer farback at Position(ypos=1125)
                show onslaught1 knife onlayer back at Position(ypos=1125)
                show onslaught2 knife onlayer front at Position(ypos=1125)
                show onslaught3 knife onlayer inyourface at Position(ypos=1125)
                with dissolve
                n "You do your best to defend yourself from her onslaught, but it's too late, and the wounds you accumulated earlier are far too numerous for you to keep pace with her.\n"
                play audio "audio/final/Assorted_BeatingToPulp_7_sequenced.flac"
                voice "audio/voices/ch2/adversary/_shared/narrator/64.flac"
                $ blade_held = False
                $ default_mouse = "default"
                play secondary "audio/one_shot/knife_bounce_several.flac"
                hide bg onlayer farback
                hide onslaught1 onlayer back
                hide onslaught2 onlayer front
                hide onslaught3 onlayer inyourface
                scene bg black
                with fade
                n "She is merciless. With every blow comes a bloom of fresh pain, igniting nerves you didn't know you even had, your skin bruising and splitting and bleeding as her fists rain down relentlessly. But thankfully, you won't have to bear this agony for much longer. Your body has its limits, and she has found them.\n"
                jump adversary_1_pulverized_upstairs
            else:
                voice "audio/voices/ch2/adversary/_shared/narrator/60.flac"
                play audio "audio/final/Adversary_ABackAndForth_1.flac"
                hide adversary onlayer front
                hide door onlayer back
                hide bg onlayer back
                hide knife onlayer back
                hide table onlayer back
                hide farback onlayer back
                hide farback onlayer farback
                scene bg adversary throat grab onlayer farback at Position(ypos=1125)
                show onslaught1 knife onlayer back at Position(ypos=1125)
                show onslaught2 knife onlayer front at Position(ypos=1125)
                show onslaught3 knife onlayer inyourface at Position(ypos=1125)
                with dissolve
                n "You do your best to defend yourself from her onslaught, but you're sorely outmatched. For every wound you inflict on her, she inflicts two on you, until finally, you're no longer able to so much as stand. Your body is giving out.\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/30.flac"
                $ blade_held = False
                $ default_mouse = "default"
                play audio "audio/one_shot/knife_bounce_several.flac"
                hide bg onlayer farback
                hide onslaught1 onlayer back
                hide onslaught2 onlayer front
                hide onslaught3 onlayer inyourface
                scene bg black
                with fade
                stubborn "'Giving out?' No, nobody's giving out, we're just getting started!\n"
                voice "audio/voices/ch2/adversary/_shared/hero/30.flac"
                hero "Don't be delusional. It's over.\n"
                play audio "audio/final/Adversary_CharacterCollapsesSToneFloor_1.flac"
                voice "audio/voices/ch2/adversary/_shared/narrator/61.flac"
                n "You fall to your knees.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_60.flac"
                scene bg adversary throat grab onlayer back at Position(ypos=1125)
                show adversary loom disappointed onlayer front at Position(ypos=1125)
                sp "Is... is that it? You're supposed to be tougher than this. Come on! Get up! Keep fighting me!\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/31.flac"
                stubborn "No, this isn't right! Listen to me! Listen to her! We can do this.\n"
                voice "audio/voices/ch2/adversary/_shared/hero/31.flac"
                hero "We can't.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_61.flac"
                play audio "audio/final/Adversary_BodySMashedAgainstWall_3.flac"
                show adversary loom kick talk onlayer front with hpunch
                with dissolve
                sp "Why. Won't. You. Get. UP?!\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/62.flac"
                play audio "audio/final/Adversary_BodySMashedAgainstWall_2.flac"
                show bg black with hpunch
                n "She kicks you in the chest, splinters from your shattered ribs stabbing into your heart and lungs. Your vision starts to swim. Finally, her face, twisted into an expression of disappointment and fury, fades.\n"
                $ quick_menu = False
                $ gallery_adversary.unlock_item(5)
                $ renpy.save_persistent()
                voice "audio/voices/ch2/adversary/_shared/narrator/63.flac"
                stop music fadeout 5.0
                stop sound fadeout 5.0
                stop secondary fadeout 5.0
                stop tertiary fadeout 5.0
                hide adversary onlayer front
                hide bg onlayer back
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "Everything goes dark, and you die.\n"
                $ trait_hunted = True
                jump adversary_2_start
                # end - leads to hunted ch 3

        else:
            play audio "audio/final/Assorted_BeatingToPulp_7_sequenced.flac"
            voice "audio/voices/ch2/adversary/_shared/narrator/64.flac"
            hide adversary onlayer front
            hide door onlayer back
            hide bg onlayer back
            hide knife onlayer back
            hide table onlayer back
            hide farback onlayer back
            hide farback onlayer farback
            scene bg adversary throat grab onlayer farback at Position(ypos=1125)
            show onslaught1 empty onlayer back at Position(ypos=1125)
            show onslaught2 empty onlayer front at Position(ypos=1125)
            show onslaught3 empty onlayer inyourface at Position(ypos=1125)
            with dissolve
            n "She is merciless. With every blow comes a bloom of fresh pain, igniting nerves you didn't know you even had, your skin bruising and splitting and bleeding as her fists rain down relentlessly. But thankfully, you won't have to bear this agony for much longer. Your body has its limits, and she has found them.\n"
            play audio "audio/final/Adversary_CharacterCollapsesSToneFloor_1.flac"
            hide bg onlayer farback
            hide onslaught1 onlayer back
            hide onslaught2 onlayer front
            hide onslaught3 onlayer inyourface
            scene bg black
            with fade
            label adversary_1_pulverized_upstairs:
                voice "audio/voices/ch2/adversary/_shared/stubborn/32.flac"
                stubborn "I hate this.\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/65.flac"
                play audio "audio/final/Adversary_HeavyBlowSuperStrong_1.flac"
                show bg adversary throat grab onlayer back at Position(ypos=1125)
                show adversary throat grab onlayer front at Position(ypos=1125)
                with dissolve
                n "With your body a shapeless pulp, her fingers wrap around what's left of your neck.\n"
                if blade_held:
                    $ gallery_adversary.unlock_item(5)
                else:
                    $ gallery_adversary.unlock_item(6)
                $ renpy.save_persistent()
                if blade_held:
                    $ blade_held = False
                    $ default_mouse = "default"
                    play audio "audio/one_shot/knife_bounce_several.flac"
                    voice "audio/voices/ch2/adversary/_shared/narrator/65a.flac"
                    n "The blade falls from your limp grip as she lifts you off the ground.\n"
                show adversary throat grab talk onlayer front at Position(ypos=1125)
                with dissolve
                voice "audio/voices/ch2/adversary/_shared/princess/adv_62a.flac"
                sp "You disgust me.\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/66.flac"
                play audio "audio/final/Adversary_PowerfulFingersDiggingSkull_2.flac"
                stop music fadeout 5.0
                stop sound fadeout 5.0
                stop secondary fadeout 5.0
                stop tertiary fadeout 5.0
                hide adversary onlayer front
                hide bg onlayer back
                scene bg black
                n "You hear a snap, then everything goes dark and you die.\n"
                $ fury_source = "death_upstairs"
                jump fury_start
                # end - leads to BROKEN ch 3?

label adversary_1_refuse:
    stop music fadeout 5.0
    voice "audio/voices/ch2/adversary/_shared/narrator/67.flac"
    n "What are you trying to do? Do you think pacifism is going to win her over? Because it won't.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/33.flac"
    stubborn "Right! This isn't fun. This isn't interesting. It's pathetic and cowardly and boring.\n"
    play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
    if blade_held:
        if adversary_1_narrator_accepts_origin == "close":
            show adversary c confused talk onlayer front at Position(ypos=1125)
            if adversary_1_chains_broken == False:
                show chain adversary c neutral onlayer front at Position(ypos=1125)
        else:
            show adversary d bored onlayer back
        with dissolve
        voice "audio/voices/ch2/adversary/_shared/princess/adv_63.flac"
        sp "Oh, you tease. I can't believe you'd go to all the trouble to bring a knife down here and then refuse to use it.\n"
        voice "audio/voices/ch2/adversary/_shared/princess/adv_64.flac"
        if adversary_1_narrator_accepts_origin == "close":
            show adversary c cocky talk onlayer front at Position(ypos=1125)
            if adversary_1_chains_broken == False:
                show chain adversary c cocky onlayer front at Position(ypos=1125)
        else:
            show adversary d neutral onlayer back
        with dissolve
        sp "Let's see if you still feel that way once I start beating you.\n"
    else:
        voice "audio/voices/ch2/adversary/_shared/princess/adv_65.flac"
        if adversary_1_narrator_accepts_origin == "close":
            show adversary c cocky talk onlayer front at Position(ypos=1125)
            if adversary_1_chains_broken == False:
                show chain adversary c cocky onlayer front at Position(ypos=1125)
        else:
            show adversary d neutral onlayer back
        with dissolve
        sp "Is that so? Let's see if you still feel that way once I start beating you.\n"
    if adversary_1_chains_broken == False:
        if adversary_1_narrator_accepts_origin == "close":
            show adversary c cocky onlayer front at Position(ypos=1125)
            if adversary_1_chains_broken == False:
                show chain adversary c cocky onlayer front at Position(ypos=1125)
        else:
            show adversary d neutral onlayer back
        with dissolve
        voice "audio/voices/ch2/adversary/_shared/hero/32.flac"
        hero "She's still bound by those chains. All we have to do is take a step back and she won't be able to do anything to us.\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/68.flac"
        n "All that does is put the two of you at another impasse. You can't stall forever.\n"
        voice "audio/voices/ch2/adversary/_shared/stubborn/34.flac"
        stubborn "Ha! Do you really think those chains will stop her? She's not the type to hand out empty threats. She's honest. It's what makes her so interesting.\n"
        voice "audio/voices/ch2/adversary/_shared/hero/33.flac"
        hero "But she has to be bluffing, right? If she isn't bluffing then why is she still—\n{w=5.0}{nw}"
        show screen disableclick(0.5)
        $ adversary_1_chains_broken = True
        voice "audio/voices/ch2/adversary/_shared/narrator/69.flac"
        play audio "audio/final/Beast_ChainsFastDrag_1.flac"
        hide adversary onlayer front
        hide chain onlayer front
        hide adversary onlayer back
        hide farback onlayer farback
        hide bg onlayer back
        scene farback adversary basement onlayer farback at Position(ypos=1125)
        show bg adversary basement onlayer back at Position(ypos=1125)
        show adversary d chains pull onlayer back at Position(ypos=1125)
        with fade
        n "You step back as she steps forward, her bindings creaking ominously.\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/69a.flac"
        play audio "audio/final/Adversary_ChainSTressBreaking_2.flac"
        show adversary d chains snap onlayer back at Position(ypos=1125)
        with dissolve
        n "And then they snap. It was only a matter of time. But she's loose.\n"
        voice "audio/voices/ch2/adversary/_shared/hero/34.flac"
        show bg adversary chains onlayer back
        show adversary d loose onlayer back
        with dissolve
        hero "Dear lord, what do we do?\n"
        if blade_held:
            voice "audio/voices/ch2/adversary/_shared/narrator/70.flac"
            n "You took the blade. How about you use it?\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/35.flac"
            stubborn "Exactly. We do what I've been telling you to do since the second we got here. We fight her, we kill her, we win.\n"
        else:
            voice "audio/voices/ch2/adversary/_shared/narrator/71.flac"
            n "Oh, if only there were some sort of weapon you could use to fight a world-ending monstrosity... I wonder where you might find one of those.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/36.flac"
            stubborn "Exactly. Just do what I've been telling you to do since the second we got here. Take the blade, fight her, kill her, and win.\n"
        # pacifism break menu
        menu:

            extend ""

            "{i}• [[Attack the Princess.]{/i}" if blade_held:
                play audio "audio/one_shot/footstep_run_dirt_short.flac"
                hide adversary onlayer back
                hide adversary onlayer front
                hide farback onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                scene bg adversary readying onlayer back at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary readying onlayer front at Position(ypos=1125)
                show adversary readying onlayer front at Position(ypos=1125)
                jump adversary_1_fight

            "{i}• ''Okay, fine. If you want to fight then we can fight. You're not giving me many options. Just let me get a weapon.'' [[Go upstairs and retrieve the blade.]{/i}" if adversary_1_cabin_blade_taken == False:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_66.flac"
                sp "Ha. Finally! I'll be waiting, but you'd better not be wasting my time.\n"
                jump adversary_1_retrieve_knife

            "{i}• [[Flee up the stairs and retrieve the blade.]{/i}" if adversary_1_cabin_blade_taken == False:
                $ adversary_1_narrator_accepts_origin = "chains"
                jump adversary_1_empty_leave

            "{i}• ''This doesn't change anything.'' [[Refuse to fight.]{/i}":
                voice "audio/voices/ch2/adversary/_shared/narrator/72.flac"
                n "{i}Sigh{/i}. I suppose there isn't much I can do to stop you, is there?\n"
                jump adversary_pacifism

            "{i}• [[Silently stand your ground and refuse to fight.]{/i}":
                voice "audio/voices/ch2/adversary/_shared/narrator/72.flac"
                n "{i}Sigh{/i}. I suppose there isn't much I can do to stop you, is there?\n"
                jump adversary_pacifism

    else:
        label adversary_pacifism:
            voice "audio/voices/ch2/adversary/_shared/narrator/73.flac"
            play audio "audio/final/adversary_charge.flac"
            if adversary_1_narrator_accepts_origin != "close":
                hide adversary onlayer back
                show adversary charge onlayer front at Position(ypos=1125)
                with dissolve
                n "You stand your ground as the Princess thunders across the basement floor, her shoulders tucked low as her fierce, unblinking gaze locks onto yours.\n"
            if blade_held:
                $ blade_held = False
                $ default_mouse = "default"
                play secondary "audio/one_shot/knife_bounce_several.flac"
            voice "audio/voices/ch2/adversary/_shared/narrator/74.flac"
            play audio "audio/final/Adversary_HandThroughChest_1.flac"
            hide adversary onlayer back
            hide farback onlayer farback
            hide adversary onlayer front
            hide bg onlayer back
            scene bg black
            n "You don't see the impact, and you can't say for sure if you even feel it. But you hear your bones splinter, and you can feel your feet leave the floor as you're hurled bodily into the unflinching stone wall.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/37.flac"
            stubborn "We're fine.\n"
            voice "audio/voices/ch2/adversary/_shared/hero/35.flac"
            hero "Are we fine? Are we really?\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/75.flac"
            n "No. You're obviously not fine. Your body is broken.\n"
            if adversary_1_cabin_blade_taken:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_67.flac"
                sp "Enough games. Pick up that knife and fight me.\n"
                if adversary_combat_to_pacifism:
                    voice "audio/voices/ch2/adversary/_shared/narrator/76.flac"
                    scene farback adversary f onlayer farback at Position(ypos=1125)
                    show bg adversary f onlayer back at Position(ypos=1125)
                    show adversary ff confused onlayer back at Position(ypos=1125)
                    show knife f floor onlayer back at Position(ypos=1125)
                    with fade
                    n "Your eyes, swimming with a concussed delirium, search for the blade.\n"
                else:
                    voice "audio/voices/ch2/adversary/_shared/narrator/77.flac"
                    scene farback adversary f onlayer farback at Position(ypos=1125)
                    show bg adversary f onlayer back at Position(ypos=1125)
                    show adversary f bored onlayer back at Position(ypos=1125)
                    show knife f floor onlayer back at Position(ypos=1125)
                    with fade
                    n "Your eyes, swimming with a concussed delirium, look down in confusion at your now empty hands.\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/78.flac"
                n "It takes you a moment to drag your vision across the floor before you manage to pick it out among the stalagmites littering the basement. It's sitting at the Princess' feet.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_68.flac"
                show adversary f annoyed talk onlayer back
                with dissolve
                sp "Here. Let me lend you a hand.\n"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                show adversary f kneel onlayer back
                with dissolve
                $ renpy.pause(0.33)
                show adversary f contemplate onlayer back
                with dissolve
                $ renpy.pause(0.33)
                play audio "audio/one_shot/knife_bounce_several.flac"
                show adversary f throw onlayer back
                show knife f close onlayer back
                with dissolve
                voice "audio/voices/ch2/adversary/_shared/narrator/79a.flac"
                n "She bends to the floor and pinches the tip of the weapon between her fingers. She stares down at it in mocking disgust before hurling it towards you.\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/80.flac"
                show adversary f watch onlayer back
                with dissolve
                n "It lands at your feet with a pathetic, tinny clatter.\n"
            else:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_69.flac"
                scene farback adversary f onlayer farback at Position(ypos=1125)
                show bg adversary f onlayer back at Position(ypos=1125)
                show adversary f talk onlayer back at Position(ypos=1125)
                with fade
                sp "Enough games. Go upstairs, pick up that knife, and fight me.\n"

    label adversary_pacifism_explore:
        $ adversary_1_wounded = True
        default adversary_pacifism_stuck = False
        default adversary_pacifism_standing = False
        menu:
            extend ""

            "{i}• (Explore) ''I can't get up.''{/i}" if adversary_pacifism_stuck == False:
                $ adversary_pacifism_stuck = True
                voice "audio/voices/ch2/adversary/_shared/stubborn/38.flac"
                if adversary_combat_to_pacifism:
                    show adversary ff confused onlayer back
                else:
                    show adversary f watch onlayer back
                with dissolve
                stubborn "Stop moping. You're fine. Now get up.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_70a.flac"
                if adversary_combat_to_pacifism:
                    show adversary ff confused talk onlayer back
                else:
                    show adversary f bored talk onlayer back
                with dissolve
                sp "What are you made of, tissue paper? I didn't hit you that hard.\n"
                if adversary_combat_to_pacifism:
                    show adversary ff confused onlayer back
                else:
                    show adversary f bored onlayer back
                jump adversary_pacifism_explore

            "{i}• ''You might as well just kill me, because you're not going to change my mind.''{/i}" if adversary_pacifism_stuck:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_71a.flac"
                if adversary_combat_to_pacifism:
                    show adversary ff confused talk onlayer back
                else:
                    show adversary f bored talk onlayer back
                with dissolve
                sp "Is this a trick? Are you tricking me?\n"
                jump adversary_pacifism_death_join

            "{i}• [[Get up.]{/i}" if adversary_pacifism_stuck:
                $ adversary_pacifism_standing = True
                play audio "audio/one_shot/collapse.flac"
                voice "audio/voices/ch2/adversary/_shared/narrator/81.flac"
                show farback adversary f onlayer farback at up
                show bg adversary f onlayer back at up
                if adversary_combat_to_pacifism:
                    show adversary ff grin onlayer back at up
                else:
                    show adversary f bored onlayer back at up
                n "You shakily push yourself to your feet. After the blow you took, it's a miracle you can move, let alone stand, but here you are. Maybe you can actually pull this off.\n"
                label adversary_pacifism_divert_menu:
                    default adversary_pacifism_divert_explore = False
                    menu:
                        extend ""

                        "{i}• (Explore) ''If I turn my back on you to get the blade... how do I know you won't just kill me?''{/i}" if adversary_1_cabin_blade_taken == False and adversary_pacifism_divert_explore == False and adversary_1_retrieve_knife_already == False:
                            $ adversary_pacifism_divert_explore = True
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_72.flac"
                            if adversary_combat_to_pacifism:
                                show adversary ff confused talk onlayer back
                            else:
                                show adversary f talk onlayer back
                            with dissolve
                            sp "Why are you even asking me that? If I wanted you dead, you'd be dead.\n"
                            voice "audio/voices/ch2/adversary/_shared/hero/36.flac"
                            if adversary_combat_to_pacifism:
                                show adversary ff confused onlayer back
                            else:
                                show adversary f watch onlayer back
                            with dissolve
                            hero "All right, what do we think?\n"
                            voice "audio/voices/ch2/adversary/_shared/stubborn/39.flac"
                            stubborn "She's telling the truth.\n"
                            voice "audio/voices/ch2/adversary/_shared/narrator/82.flac"
                            n "You shouldn't trust her, but it doesn't really matter if she's telling the truth, does it? You need a weapon to do this right. But keep your eyes on her, and don't take her at her word.\n"
                            jump adversary_pacifism_divert_menu

                        "{i}• ''Okay. I'll be right back.'' [[Retrieve the blade.]{/i}" if adversary_1_cabin_blade_taken == False and adversary_1_retrieve_knife_already == False:
                            #GOHERE
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_73.flac"
                            if adversary_combat_to_pacifism:
                                show adversary ff confused talk onlayer back
                            else:
                                show adversary f talk onlayer back
                            with dissolve
                            sp "You'd better not take too long. I'll be waiting.\n"
                            jump adversary_1_retrieve_knife

                        "{i}• ''I'm still not going to fight you.''{/i}":
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_71a.flac"
                            if adversary_combat_to_pacifism:
                                show adversary ff confused talk onlayer back
                            else:
                                show adversary f bored talk onlayer back
                            sp "Is this a trick? Are you tricking me?\n"
                            jump adversary_pacifism_death_join

                        "{i}• [[Remain silent.]{/i}":
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_74.flac"
                            if adversary_combat_to_pacifism:
                                show adversary ff frustrated talk onlayer back
                            else:
                                show adversary f bored talk onlayer back
                            with dissolve
                            sp "Is that all you have to say? What is this, some sort of trick? Are you tricking me? Why are you just standing there?\n"
                            jump adversary_pacifism_death_join

                        "{i}• [[Run like hell.]{/i}" if adversary_1_cabin_blade_taken == False and adversary_1_retrieve_knife_already == False:
                            voice "audio/voices/ch2/adversary/_shared/narrator/83.flac"
                            play audio "audio/one_shot/footstep_run_medium.flac"
                            hide adversary onlayer back
                            hide farback onlayer farback
                            hide bg onlayer back
                            scene bg black
                            with fade
                            n "You do your best to scramble up the stairs. The Princess calls after you as you hobble away.\n"
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_75.flac"
                            sp "See you soon.\n"
                            jump adversary_1_retrieve_knife

                        "{i}• [[Grab the blade and run like hell.]{/i}" if adversary_1_cabin_blade_taken or adversary_1_retrieve_knife_already:
                            $ blade_held = True
                            voice "audio/voices/ch2/adversary/_shared/narrator/84.flac"
                            $ blade_held = True
                            if adversary_combat_to_pacifism:
                                $ default_mouse = "blood"
                            else:
                                $ default_mouse = "blade"
                            play audio "audio/one_shot/knife_pickup.flac"
                            play secondary "audio/one_shot/footstep_run_medium.flac"
                            hide adversary onlayer back
                            hide farback onlayer farback
                            hide knife onlayer back
                            hide bg onlayer back
                            scene bg black
                            with fade
                            n "You grab the blade from the floor and do your best to scramble up the stairs before the Princess can reach you.\n"
                            voice "audio/voices/ch2/adversary/_shared/stubborn/40.flac"
                            stubborn "You coward!\n"
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_76.flac"
                            sp "Oh no you don't!\n"
                            voice "audio/voices/ch2/adversary/_shared/narrator/85.flac"
                            play audio "audio/final/adversary_charge.flac"
                            n "Your broken bones scream in protest, muscles nearly seizing with the shock, and she's so close on your heels you can almost feel her heavy breath steaming the back of your neck.\n"
                            voice "audio/voices/ch2/adversary/_shared/narrator/86.flac"
                            play audio "audio/one_shot/door_stone.flac"
                            n "But you manage, just barely, to throw yourself over the threshold and slam the heavy stone doors behind you.\n"
                            jump adversary_1_upstairs

                        "{i}• [[Attack the Princess.]{/i}" if adversary_1_cabin_blade_taken and adversary_combat_to_pacifism == False:
                            play audio "audio/one_shot/footstep_run_dirt_short.flac"
                            $ blade_held = True
                            $ default_mouse = "blade"
                            play audio "audio/one_shot/knife_pickup.flac"
                            hide adversary onlayer back
                            hide adversary onlayer front
                            hide farback onlayer back
                            hide farback onlayer farback
                            hide bg onlayer back
                            scene bg adversary readying onlayer back at Position(ypos=1125)
                            if adversary_1_chains_broken == False:
                                show chain adversary readying onlayer front at Position(ypos=1125)
                            show adversary readying onlayer front at Position(ypos=1125)
                            with dissolve
                            jump adversary_1_fight

            "{i}• [[Remain silent.]{/i}":
                if adversary_pacifism_stuck:
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_77.flac"
                    if adversary_combat_to_pacifism:
                        show adversary ff confused talk onlayer back
                    else:
                        show adversary f bored talk onlayer back
                    with dissolve
                    sp "Is that all you have to say? What is this? Some sort of trick? Are you tricking me? Are you really that pathetic?\n"
                else:
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_78.flac"
                    if adversary_combat_to_pacifism:
                        show adversary ff confused talk onlayer back
                    else:
                        show adversary f bored talk onlayer back
                    with dissolve
                    sp "Why aren't you saying anything?! Is this some sort of trick? Are you tricking me? Or are you really that fragile?\n"
                label adversary_pacifism_death_join:
                    default adversary_pacifism_last_words = ""
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_79.flac"
                    if adversary_combat_to_pacifism:
                        show adversary ff frustrated talk onlayer back
                    else:
                        show adversary f annoyed talk onlayer back
                    with dissolve
                    sp "Because why would you... why wouldn't you...\n"
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_80.flac"
                    sp "Gah!\n"
                    voice "audio/voices/ch2/adversary/_shared/narrator/87.flac"
                    play audio "audio/final/adversary_charge.flac"
                    hide adversary onlayer back
                    hide adversary onlayer front
                    hide farback onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide knife onlayer back
                    scene bg black
                    n "The Princess' shoulders tense with fury as she storms towards you.\n"
                    voice "audio/voices/ch2/adversary/_shared/narrator/88.flac"
                    scene bg adversary throat grab onlayer back at Position(ypos=1125)
                    show adversary finale eyes onlayer front at Position(ypos=1125)
                    with dissolve
                    n "You can see her face flush, her knuckles going white as she clenches her fists, her entire body trembling with a burning rage.\n"
                    voice "audio/voices/ch2/adversary/_shared/stubborn/41.flac"
                    stubborn "I can't believe you're making me watch this.\n"
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_81.flac"
                    sp "Fine. If you want to die like a pathetic little worm, you can die like a pathetic little worm.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/37.flac"
                    hero "I guess I'll see you all next time.\n"
                    if adversary_pacifism_standing:
                        voice "audio/voices/ch2/adversary/_shared/narrator/89.flac"
                        play audio "audio/final/Adversary_HoleBeingPunchesRock_3.flac"
                        hide bg onlayer back
                        hide adversary onlayer front
                        show bg adversary throat grab onlayer back at Position(ypos=1125)
                        show adversary throat grab onlayer front at Position(ypos=1125) with hpunch
                        with dissolve
                        n "She grabs you by the throat and slams your body against the wall. Her eye twitches as her grip tightens around your neck.\n"
                    else:
                        voice "audio/voices/ch2/adversary/_shared/narrator/90.flac"
                        play audio "audio/final/Adversary_HoleBeingPunchesRock_3.flac"
                        hide bg onlayer back
                        hide adversary onlayer front
                        show bg adversary throat grab onlayer back at Position(ypos=1125)
                        show adversary throat grab onlayer front at Position(ypos=1125) with hpunch
                        with dissolve
                        n "She reaches down and grabs you by the throat, lifting your limp form and slamming it forcefully against the wall. Her eyes twitch as her grip tightens around your neck.\n"
                    voice "audio/voices/ch2/adversary/_shared/hero/38.flac"
                    hero "She sure is taking her time, isn't she?\n"
                    voice "audio/voices/ch2/adversary/_shared/princess/adv_82.flac"
                    play audio "audio/final/Adversary_HoleBeingPunchesRock_3.flac"
                    show adversary throat grab talk onlayer front with hpunch
                    sp "WHY?! Why are you letting me do this? Why are you making me do this? Why won't you fight back?!\n"
                    show adversary throat grab onlayer front
                    menu:
                        extend ""

                        "{i}• ''Because death doesn't matter anymore, does it? Fighting, not fighting — what does any of it matter if it all ends the same way?''{/i}":
                            $ adversary_pacifism_last_words = "deathless"
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_83.flac"
                            play audio "audio/final/Adversary_HoleBeingPunchesRock_2.flac"
                            show adversary throat grab talk onlayer front with hpunch
                            sp "It— it matters! I like fighting you! I... grrrrrrrr.\n"
                            jump adversary_pacifism_end

                        "{i}• ''Because there's more to this than just fighting each other. If letting you kill me is how I can show you that, then it's worth it.''{/i}":
                            $ adversary_pacifism_last_words = "more"
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_84.flac"
                            play audio "audio/final/Adversary_HoleBeingPunchesRock_2.flac"
                            show adversary throat grab talk onlayer front with hpunch
                            sp "What? What more can there possibly be? What are you trying to do? I don't want to think, why are you trying to make me think?\n"
                            jump adversary_pacifism_end

                        "{i}• ''I care about you, and I don't want to hurt you anymore.''{/i}":
                            $ adversary_pacifism_last_words = "care"
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_85.flac"
                            play audio "audio/final/Adversary_HoleBeingPunchesRock_2.flac"
                            show adversary throat grab talk onlayer front with hpunch
                            sp "You care about me? What is that supposed to mean? If you cared about me you'd fight me. You'd understand! But... gah, why are you trying to make me think?\n"
                            jump adversary_pacifism_end

                        "{i}• ''I just think it's kind of funny...''{/i}":
                            $ adversary_pacifism_last_words = "funny"
                            jump adversary_pacifism_end

                        "{i}• [[Remain silent.]{/i}":
                            $ adversary_pacifism_last_words = "silent"
                            voice "audio/voices/ch2/adversary/_shared/princess/adv_86.flac"
                            play audio "audio/final/Adversary_HoleBeingPunchesRock_2.flac"
                            show adversary throat grab talk onlayer front with hpunch
                            sp "You won't even answer me, huh? I hate you.\n"
                            label adversary_pacifism_end:
                                voice "audio/voices/ch2/adversary/_shared/narrator/91.flac"
                                play audio "audio/final/Adversary_HandThroughChest_1.flac"
                                hide bg onlayer back
                                hide adversary onlayer front
                                scene bg black
                                n "Her grip hardens, and you feel a horrific pop in your neck.\n"
                                voice "audio/voices/ch2/adversary/_shared/narrator/92.flac"
                                play audio "audio/one_shot/collapse.flac"
                                scene farback adversary f onlayer farback at swayblur, Position(ypos=1125)
                                show bg adversary f onlayer back at swayblur, Position(ypos=1125)
                                show adversary f frustrated onlayer back at swayblur, Position(ypos=1125)
                                with fade
                                n "She releases you, your numb body crumpling to the stone floor as your vision starts to fade.\n"
                                voice "audio/voices/ch2/adversary/_shared/princess/adv_87.flac"
                                scene bg black
                                hide farback adversary f onlayer farback at swayblur, Position(ypos=1125)
                                hide bg adversary f onlayer back at swayblur, Position(ypos=1125)
                                hide adversary f frustrated talk onlayer back at swayblur, Position(ypos=1125)
                                with fade
                                sp "... what am I supposed to do without you?\n"
                                voice "audio/voices/ch2/adversary/_shared/hero/39.flac"
                                hide farback onalyer farback
                                hide bg onlayer back
                                hide adversary onlayer back
                                with fade
                                hero "I guess I'll see you all next time... I can say that now, right? We're dead?\n"
                                voice "audio/voices/ch2/adversary/_shared/stubborn/42.flac"
                                stubborn "Great. I can't wait to be stuck in this useless body all over again.\n"
                                hide farback onlayer farback
                                hide bg onlayer back
                                hide adversary onlayer back
                                $ gallery_adversary.unlock_item(16)
                                $ gallery_adversary.unlock_item(17)
                                $ renpy.save_persistent()
                                stop sound fadeout 5.0
                                stop music fadeout 5.0
                                stop secondary fadeout 5.0
                                stop tertiary fadeout 5.0
                                if adversary_1_narrator_proof:
                                    voice "audio/voices/ch2/adversary/_shared/narrator/93.flac"
                                    n "I won't be seeing you, but I suppose something like me will. Everything goes dark, and you die.\n"
                                else:
                                    voice "audio/voices/ch1/knife/narrator/knife_n_30.flac"
                                    n "Everything goes dark and you die.\n"
                                $ fury_source = "pacifism"
                                $ achievement.grant("ACH_ADV_PACIFISM")
                                jump fury_start
                                # end - FURY + contrarian



label adversary_1_retrieve_knife:

    voice "audio/voices/ch2/adversary/_shared/narrator/94.flac"
    play audio "audio/one_shot/footsteps_stone.flac"
    hide adversary onlayer back
    hide adversary onlayer front
    hide chain onlayer front
    hide bg onlayer back
    hide bg onlayer farback
    hide farback onlayer farback
    scene bg black
    with fade
    n "You make your way back up the stairs to the cabin above. The Princess, surprisingly true to her word, lets you leave.\n"
    scene farback adversary cabin onlayer farback at Position(ypos=1125)
    show bg adversary cabin onlayer back at Position(ypos=1125)
    show door adversary1 onlayer back at Position(ypos=1125)
    show table adversary onlayer back at Position(ypos=1125)
    show knife adversary onlayer back at Position(ypos=1125)
    with fade
    voice "audio/voices/ch2/adversary/_shared/narrator/95.flac"
    play audio "audio/one_shot/door_stone.flac"
    n "The blade remains where you left it on the wrought-iron altar.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/43.flac"
    stubborn "Great. Now pick it up and march back down there. I'm tired of us constantly moving in circles instead of fighting her like we're supposed to.\n"
    label adversary_1_retrieve_knife_menu:
        default adversary_1_retrieve_knife_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''You know, we could just stay here. Who says we have to fight to the death?''{/i}" if adversary_1_retrieve_knife_explore == False:
                $ adversary_1_retrieve_knife_explore = True
                voice "audio/voices/ch2/adversary/_shared/stubborn/44.flac"
                stubborn "Me. I say that.\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/96.flac"
                n "Staying up here doesn't solve anything. All it does is kick the can down the road. If you don't deal with her now, she will find a way a out.\n"
                if adversary_1_chains_broken == False:
                    voice "audio/voices/ch2/adversary/_shared/hero/40.flac"
                    hero "Those doors are made of stone and she's still in chains. She's strong, yeah, but is she break-her-chains-and-smash-through-stone strong?\n"
                else:
                    voice "audio/voices/ch2/adversary/_shared/hero/41.flac"
                    hero "Those doors are made of stone. She's strong, yeah, but is she smash-through-stone strong?\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/45.flac"
                stubborn "Wouldn't it be exciting if she was?\n"
                voice "audio/voices/ch2/adversary/_shared/hero/42.flac"
                hero "Here's another idea. What if we just leave?\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/97.flac"
                n "Absolutely not. If you leave, she'll leave, and that'll be the end of everything as we know it.\n"
                jump adversary_1_retrieve_knife_menu

            "{i}• [[Take the blade from the altar.]{/i}" if blade_held == False:
                default adversary_1_retrieve_knife_already = False
                $ adversary_1_retrieve_knife_already = True
                $ blade_held = True
                hide knife onlayer back
                with dissolve
                voice "audio/voices/ch2/adversary/_shared/narrator/98.flac"
                $ blade_held = True
                $ default_mouse = "blade"
                play audio "audio/one_shot/knife_pickup.flac"
                n "You take the blade from the altar. It would be difficult to slay the Princess and save the world without a weapon, as I'm sure you're all too aware by now.\n"
                jump adversary_1_retrieve_knife_menu

            "{i}• ''We're doing it. We're staying up here.''{/i}" if adversary_1_retrieve_knife_explore and adversary_can_fury:
                if fury_encountered:
                    $ adversary_can_fury = False
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    jump adversary_1_retrieve_knife_menu
                if blade_held:
                    voice "audio/voices/ch2/adversary/_shared/narrator/99.flac"
                    n "Did you pick up the blade just to mess with me? Is your brain that numb to the consequences of all this?\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/100.flac"
                n "... Fine. You stay up here. Nothing happens. Are you done? Are you ready to finally start taking this seriously?\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/46.flac"
                stubborn "I'm ready to start taking this seriously. Put me in charge.\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/101.flac"
                n "Oh how I wish I could, because literally anyone else making decisions would be better than this, but unfortunately that's beyond the scope of my abilities.\n"
                voice "audio/voices/ch2/adversary/_shared/hero/43.flac"
                hero "Is she really just going to wait down there forever? She's got to start getting impatient eventually—\n{w=6.6}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch2/adversary/_shared/narrator/102.flac"
                n "Your thoughts are interrupted by the sound of the Princess furiously stomping her way up the stairs.\n" id adversary_1_retrieve_knife_menu_0e9bd107
                if adversary_1_chains_broken == False:
                    voice "audio/voices/ch2/adversary/_shared/hero/44.flac"
                    hero "But what about her chains?!\n"
                    voice "audio/voices/ch2/adversary/_shared/narrator/103.flac"
                    n "What about them? They're clearly not holding her back any longer.\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/47a.flac"
                stubborn "Hahaha. Yes! Yes! We're finally going to get our rematch and there's nothing you can do to stop it.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_88.flac"
                sp "I'm tired of waiting. You thought you could just leave me down there, didn't you? But I can feel you trembling on the other side of this door. There's nowhere left for you to run.\n"
                jump adversary_1_upstairs_late_join

            "{i}• ''We're leaving.''{/i}" if adversary_1_retrieve_knife_explore and adversary_can_fury:
                if fury_encountered:
                    $ adversary_can_fury = False
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    jump adversary_1_retrieve_knife_menu
                if blade_held:
                    voice "audio/voices/ch2/adversary/_shared/narrator/99.flac"
                    n "Did you pick up the blade just to mess with me? Is your brain that numb to the consequences of all this?\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_88.flac"
                sp "I'm tired of waiting. You thought you could just leave me down there, didn't you? But I can feel you trembling on the other side of this door. There's nowhere left for you to run.\n"
                jump adversary_1_upstairs_late_join

            "{i}• [[Return to the basement.]{/i}" if blade_held:
                voice "audio/voices/ch2/adversary/_shared/narrator/104.flac"
                play audio "audio/one_shot/footsteps_stone.flac"
                hide table onlayer back
                hide door onlayer back
                hide bg onlayer back
                hide farback onlayer farback
                hide knife onlayer back
                scene bg black
                with fade
                n "Blade in hand, you make your way back down the basement stairs.\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/105.flac"
                show bg adversary throat grab onlayer back at Position(ypos=1125)
                show adversary c neutral onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                with fade
                n "You find the Princess waiting for you, just where you left her.\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/48.flac"
                stubborn "See? I knew we could trust her. I told you we could trust her.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_89.flac"
                show bg adversary throat grab onlayer back at Position(ypos=1125)
                show adversary c cocky talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c cocky onlayer front
                with dissolve
                sp "Glad to see you finally stopped having cold feet. I could barely wait, my skin is practically crawling with anticipation.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_89a.flac"
                show bg adversary throat grab onlayer back at Position(ypos=1125)
                show adversary c frustrated talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                with dissolve
                sp "Fight me. NOW.\n"
                show bg adversary throat grab onlayer back at Position(ypos=1125)
                show adversary c cocky onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c cocky onlayer front
                with dissolve
                menu:
                    extend ""

                    "{i}• [[Attack the Princess.]{/i}":
                        play audio "audio/one_shot/footstep_run_dirt_short.flac"
                        hide adversary onlayer back
                        hide adversary onlayer front
                        hide farback onlayer back
                        hide farback onlayer farback
                        hide bg onlayer back
                        scene bg adversary readying onlayer back at Position(ypos=1125)
                        if adversary_1_chains_broken == False:
                            show chain adversary readying onlayer front at Position(ypos=1125)
                        show adversary readying onlayer front at Position(ypos=1125)
                        with dissolve
                        jump adversary_1_fight

label adversary_1_fight_unarmed:

    play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
    voice "audio/voices/ch2/adversary/_shared/narrator/106.flac"
    n "{i}Sigh{/i}. I guess we'll have to see how this goes...\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/107a.flac"
    play audio "audio/one_shot/footstep_run_dirt_short.flac"
    hide adversary onlayer back
    hide adversary onlayer front
    hide farback onlayer farback
    hide bg onlayer back
    scene bg adversary readying onlayer back at Position(ypos=1125)
    if adversary_1_chains_broken == False:
        show chain adversary readying onlayer front at Position(ypos=1125)
    show adversary readying onlayer front at Position(ypos=1125)
    with dissolve
    n "Your hands empty, you charge the Princess.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/49.flac"
    stubborn "Quit the pessimism, will you?\n"
    voice "audio/voices/ch2/adversary/_shared/hero/45.flac"
    hero "Right? It's almost like you don't want us to beat her.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/108.flac"
    n "No. Look. I'm rooting for you. I really am. I'm just doing my best to keep my expectations grounded. You don't have a weapon. You're supposed to have a weapon.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/50.flac"
    stubborn "We'll be fine. Just watch.\n"
    $ gallery_adversary.unlock_item(11)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/adversary/_shared/narrator/109.flac"
    play audio "audio/final/Adversary_HeavyBlowSuperStrong_1.flac"
    hide bg onlayer back
    hide chain onlayer front
    hide adversary onlayer front
    show bg adversary throat grab onlayer farback at Position(ypos=1125)
    show battle1 adversary unarmed1 onlayer back at Position(ypos=1125)
    with dissolve
    n "You attack, fists raised, and the two of you fall into combat. Your clawed fingers tear into her flesh, and her fists and elbows return the blows in kind, bruises blossoming in her wake and blood vessels rupturing in vivid sprays of gore.\n"
    $ gallery_adversary.unlock_item(12)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/adversary/_shared/princess/adv_90.flac"
    play audio "audio/final/Adversary_HeavyBlowSuperStrong_2.flac"
    show battle2 adversary unarmed1 onlayer front at Position(ypos=1125)
    with dissolve
    sp "Not bad. You're tougher than I thought you'd be.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/51.flac"
    stubborn "Hear that? She respects us. We can pull this off!\n"
    voice "audio/voices/ch2/adversary/_shared/hero/46.flac"
    hero "Yeah... yeah! You're right!\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_91.flac"
    play audio "audio/final/Adversary_HeavyBlowSuperStrong_3.flac"
    show battle3 adversary unarmed1 onlayer inyourface at Position(ypos=1125)
    with dissolve
    sp "But without that knife you'll never be enough.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/110.flac"
    play audio "audio/final/Adversary_BodySMashedAgainstWall_1.flac"
    hide battle1 onlayer back
    hide battle2 onlayer front
    hide battle3 onlayer inyourface
    hide bg onlayer farback
    hide bg onlayer back
    scene bg black
    n "Her knee connects with your sternum with a loud, violent crack. The wind leaves your lungs, and as you struggle for breath, you can feel something flooding in to fill the space. Hot blood, suffocating you from the inside.\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_92.flac"
    sp "You have to want to kill me. Like this.\n"
    stop music fadeout 1.0
    voice "audio/voices/ch2/adversary/_shared/narrator/111.flac"
    play audio "audio/final/Adversary_HandThroughChest_1.flac"
    hide battle1 onlayer back
    hide battle2 onlayer front
    hide battle3 onlayer inyourface
    hide bg onlayer farback
    hide bg onlayer back
    scene bg black
    n "You don't so much as see her movement before she deals the killing blow. Everything goes dark, and you die.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/47.flac"
    hero "Are... are you serious? That's it?\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/112.flac"
    n "That's it.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/52.flac"
    stubborn "Like hell it is! We're not giving up that easy, now GET UP!\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/113.flac"
    n "Didn't you hear me? You're dead. There's no getting up from that.\n"
    menu:
        extend ""

        "{i}• [[Get up.]{/i}":
            voice "audio/voices/ch2/adversary/_shared/narrator/114.flac"
            n "Wait... no, that's not right you're—\n{w=2.2}{nw}"
            show screen disableclick(0.5)
            voice "audio/voices/ch2/adversary/_shared/stubborn/53.flac"
            stubborn "Not dead anymore?\n"
            play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
            voice "audio/voices/ch2/adversary/_shared/narrator/115.flac"
            play audio "audio/one_shot/collapse.flac"
            scene farback adversary basement onlayer farback at Position(ypos=1125)
            show bg adversary basement onlayer back at Position(ypos=1125)
            show gore unarmed onlayer back at Position(ypos=1125)
            show adversary d unarmed onlayer back at Position(ypos=1125)
            with fade
            n "Yes. Your eyes bolt open and you push yourself back to your feet. You're... alive.\n"

        "{i}• [[Die.]{/i}":
            stop sound fadeout 5.0
            stop music fadeout 5.0
            stop secondary fadeout 5.0
            stop tertiary fadeout 5.0
            if adversary_1_narrator_proof:
                voice "audio/voices/ch2/adversary/_shared/narrator/116.flac"
                n "It's over, but maybe you'll have better luck next time.\n"
            else:
                voice "audio/voices/ch2/adversary/_shared/narrator/117.flac"
                n "It's over.\n"
            $ fury_source = "death_downstairs"
            $ fury_unarmed_sub = "broken"
            jump fury_start
            # END - leads to broken fury

    $ gallery_adversary.unlock_item(13)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/adversary/_shared/narrator/118.flac"
    play audio "audio/final/footsteps_stone_short.flac"
    show adversary d unarmed aback onlayer back
    with dissolve
    n "The Princess takes a step back and looks down at her pulp-covered fists.\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_93.flac"
    show adversary d unarmed aback talk onlayer back
    with dissolve
    sp "I could have sworn I killed you. That's your face splattered on the walls and dripping from my hands.\n"
    label adversary_1_face_missing_menu:
        default adversary_1_face_missing_explore = False
        default adversary_1_face_princess_attack = False
        menu:
            extend ""

            "{i}• (Explore) ''Wait no... my face? You're joking right? You're exaggerating? I still have my face right?'' [[Touch your face.]{/i}" if adversary_1_face_missing_explore == False:
                $ adversary_1_face_missing_explore = True
                voice "audio/voices/ch2/adversary/_shared/princess/adv_94.flac"
                show adversary d unarmed talk onlayer back
                with dissolve
                sp "You don't. I don't even know how you're talking to me!\n"
                voice "audio/voices/ch2/adversary/_shared/narrator/119a.flac"
                show adversary d unarmed disgusted onlayer back
                with dissolve
                n "You raise your hands and touch the front of your head. She's... not wrong.\n"
                voice "audio/voices/ch2/adversary/_shared/hero/48.flac"
                hero "What?!?!? What did she do? What are we missing?\n"
                voice "audio/voices/ch2/adversary/_shared/stubborn/54.flac"
                stubborn "Who cares if we're missing our face? We can fight just fine without one.\n"
                jump adversary_1_face_missing_menu

            "{i}• ''Can... can I go get my pristine blade now?''{/i}":
                voice "audio/voices/ch2/adversary/_shared/narrator/120.flac"
                show adversary d unarmed grin onlayer back
                with dissolve
                n "The Princess breaks into a wide grin.\n"
                voice "audio/voices/ch2/adversary/_shared/princess/adv_95.flac"
                show adversary d unarmed grin talk onlayer back
                with dissolve
                sp "No.\n"
                label adversary_1_face_missing_princess_attack_join:
                    $ adversary_1_face_princess_attack = True
                    if adversary_1_chains_broken == False:
                        $ adversary_1_chains_broken = True
                        voice "audio/voices/ch2/adversary/_shared/narrator/28.flac"
                        play audio "audio/final/Beast_ChainsFastDrag_1.flac"
                        hide farback onlayer farback
                        hide adversary onlayer back
                        hide gore onlayer back
                        hide bg onlayer back
                        scene bg black
                        with fade
                        n "She steps forward, her bindings creaking under the pressure of her strength.\n"
                        play audio "audio/final/Adversary_ChainSTressBreaking_2.flac"
                        voice "audio/voices/ch2/adversary/_shared/narrator/28a.flac"
                        n "And then they snap. It was only a matter of time, but she's loose.\n"
                        voice "audio/voices/ch2/adversary/_shared/narrator/121a.flac"
                        play audio "audio/final/Adversary_HeavyBlowSuperStrong_1.flac"
                        show bg adversary throat grab onlayer farback at Position(ypos=1125)
                        show battle1 adversary unarmed2 onlayer back at Position(ypos=1125)
                        with dissolve
                        n "And then she slams into you, and you're once again forced to engage her in unarmed combat.\n"
                    else:
                        voice "audio/voices/ch2/adversary/_shared/narrator/121.flac"
                        play audio "audio/final/Adversary_HeavyBlowSuperStrong_1.flac"
                        hide farback onlayer farback
                        hide adversary onlayer back
                        hide gore onlayer back
                        hide bg onlayer back
                        show bg adversary throat grab onlayer farback at Position(ypos=1125)
                        show battle1 adversary unarmed2 onlayer back at Position(ypos=1125)
                        with dissolve
                        n "She slams into you, and you're once again forced to engage her in unarmed combat.\n"
                    jump adversary_1_face_missing_post

            "{i}• ''No, you definitely killed me. I just got better.''{/i}" if adversary_1_face_missing_explore == False:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_96.flac"
                show adversary d unarmed grin talk onlayer back
                sp "Maybe this will be a good fight after all.\n"
                jump adversary_1_face_missing_post

            "{i}• ''You're not putting me down that easy.''{/i}" if adversary_1_face_missing_explore == False:
                voice "audio/voices/ch2/adversary/_shared/princess/adv_96.flac"
                show adversary d unarmed grin talk onlayer back
                sp "Maybe this will be a good fight after all.\n"
                jump adversary_1_face_missing_post

            "{i}• [[Run.]{/i}":
                voice "audio/voices/ch2/adversary/_shared/princess/adv_97.flac"
                show adversary d unarmed grin talk onlayer back
                sp "Oh no you don't!\n"
                jump adversary_1_face_missing_princess_attack_join

            "{i}• [[Attack the Princess.]{/i}":
                jump adversary_1_face_missing_post

label adversary_1_face_missing_post:

    if adversary_1_face_princess_attack == False:
        voice "audio/voices/ch2/adversary/_shared/narrator/122.flac"
        play audio "audio/final/Adversary_HeavyBlowSuperStrong_1.flac"
        hide farback onlayer farback
        hide adversary onlayer back
        hide gore onlayer back
        hide bg onlayer back
        show bg adversary throat grab onlayer farback at Position(ypos=1125)
        show battle1 adversary unarmed2 onlayer back at Position(ypos=1125)
        with dissolve
        n "The two of you clash once more.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/123.flac"
    play audio "audio/final/Adversary_HeavyBlowSuperStrong_2.flac"
    show battle2 adversary unarmed2 onlayer front at Position(ypos=1125)
    with dissolve
    n "It's... not as one-sided as I feared, but it's still a far cry from what I'd hoped. Her injuries, though numerous, pale in comparison to yours, and the wounds you've inflicted upon her barely seem to have slowed her down. As much as you're trying to ignore it, adrenaline pushing you far past your limits, every movement burns.\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_98.flac"
    play audio "audio/final/Adversary_HeavyBlowSuperStrong_3.flac"
    show battle3 adversary unarmed2 onlayer inyourface at Position(ypos=1125)
    with dissolve
    sp "This is getting boring. Are you even trying to keep up with me?\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/124.flac"
    play audio "audio/final/Adversary_HandThroughChest_1.flac"
    hide battle1 onlayer back
    hide battle2 onlayer front
    hide battle3 onlayer inyourface
    hide bg onlayer farback
    hide bg onlayer back
    scene bg black
    n "She lands another devastating—no, lethal—blow. Everything goes dark. Again. And you die. Again.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/55.flac"
    stubborn "You know what I'm going to say.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/49.flac"
    hero "That we're not dead?\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/56.flac"
    stubborn "Yeah. That we're not dead. Come on. Get up. If we can just keep going, we're bound to wear her down eventually.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/50.flac"
    hero "Are you sure she can't do what we're doing right now?\n"
    if adversary_1_forest_princess_why_me:
        voice "audio/voices/ch2/adversary/_shared/stubborn/57.flac"
        stubborn "Of course I'm sure. We're special, remember?\n"
    else:
        voice "audio/voices/ch2/adversary/_shared/stubborn/58.flac"
        stubborn "There's only one way to find out.\n"
    menu:
        extend ""

        "{i}• [[Get up.]{/i}":
            voice "audio/voices/ch2/adversary/_shared/narrator/125.flac"
            n "Once more, you push yourself back to your mangled feet.\n"

        "{i}• [[Die.]{/i}":
            stop sound fadeout 5.0
            stop music fadeout 5.0
            stop secondary fadeout 5.0
            stop tertiary fadeout 5.0
            voice "audio/voices/ch2/adversary/_shared/stubborn/59.flac"
            stubborn "You can't just... decide to die like that! Not when we're so close.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/60.flac"
            stubborn "You! Annoying Man Who Tells Us To Do Things! You're not just going to let this happen, are you? We can't slay the Princess if we're dead!\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/126.flac"
            n "What do you want me to do? I have a duty to report facts as facts, and the fact is that you decided to die. If you have a problem with it, take it up with the one making the decisions.\n"
            if adversary_1_narrator_proof:
                voice "audio/voices/ch2/adversary/_shared/narrator/116.flac"
                n "It's over, but maybe you'll have better luck next time.\n"
            else:
                voice "audio/voices/ch2/adversary/_shared/narrator/117.flac"
                n "It's over.\n"
            $ fury_source = "death_downstairs"
            $ fury_unarmed_sub = "broken"
            jump fury_start
            # END - FURY

    voice "audio/voices/ch2/adversary/_shared/princess/adv_99.flac"
    show bg adversary throat grab onlayer back at Position(ypos=1125)
    show adversary c unarmed aback talk onlayer front at Position(ypos=1125)
    with Dissolve(2.0)
    sp "How... how are you still moving? How are you still doing ANYTHING?\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_100.flac"
    show adversary c unarmed disgusted talk onlayer front
    with dissolve
    sp "B-Bodies aren't supposed to look like that!\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/127.flac"
    show adversary c unarmed disgusted onlayer front
    with dissolve
    n "An uncharacteristic terror seems to grip her voice.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/51.flac"
    hero "Have we ever seen her afraid before?\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/128.flac"
    n "No, we haven't.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/61a.flac"
    stubborn "This is how we win. We can do this forever.\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_101.flac"
    show adversary c unarmed pity talk onlayer front
    with dissolve
    sp "I'm going to put you out of your misery. I don't like looking at you like this. You're all twitching. And wrong.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/62.flac"
    stubborn "I'd like to see her try. We're invincible!\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/129.flac"
    stop music fadeout 10.0
    stop sound fadeout 10.0
    stop secondary fadeout 10.0
    stop tertiary fadeout 10.0
    play audio "audio/final/Adversary_HandThroughChest_1.flac"
    hide adversary onlayer front
    hide bg onlayer back
    scene bg black
    n "Her fist flies towards where your face used to be, your twisted body incapable of moving out of the way. And then you see nothing.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/52.flac"
    hero "Everything goes dark and we die?\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/64.flac"
    stubborn "{i}Grumbling noises{/i}.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/130.flac"
    n "Yes. Something like that.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/63.flac"
    stubborn "{i}More grumbling noises{/i}.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/131.flac"
    n "Well? Don't you have something to say?\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/65.flac"
    stubborn "Yeah. I quit.\n"
    $ fury_source = "unarmed"
    $ fury_unarmed_sub = "contrarian"
    $ achievement.grant("ACH_ADV_UNARMED")
    jump fury_start
    # end - unarmed contrarian

label adversary_1_fight:
    default adversary_delayed_fight = False
    play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
    if adversary_1_wounded:
        voice "audio/voices/ch2/adversary/_shared/narrator/132.flac"
        play audio "audio/one_shot/footstep_run_dirt_short.flac"
        hide farback onlayer farback
        hide adversary onlayer back
        hide gore onlayer back
        hide bg onlayer back
        hide chain onlayer front
        hide adversary onlayer front
        scene bg adversary throat grab onlayer back at Position(ypos=1125)
        show adversary finale eyes onlayer front at Position(ypos=1125)
        with dissolve
        n "As you attempt to charge towards the Princess, you stumble, your thoughts consumed with the realization of just how much damage she managed to inflict earlier.\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/133.flac"
        n "Your legs refuse to stand strong beneath you, your head swims and your ears ring as the room spins. Your heart pumps erratically. She's ruptured something inside you, something that was clearly very important.\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/134.flac"
        stop music fadeout 5.0
        stop sound fadeout 5.0
        stop secondary fadeout 5.0
        stop tertiary fadeout 5.0
        play audio "audio/final/Adversary_HandThroughChest_1.flac"
        hide bg onlayer back
        hide adversary onlayer front
        scene bg black
        n "Your mind and body both hesitating, the Princess smashes into you. You failed to draw first blood, and you'll never have the chance to draw second. Everything goes dark, and you die. I'm sorry.\n"
        voice "audio/voices/ch2/adversary/_shared/hero/53.flac"
        hero "That's it?\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/135.flac"
        n "That's it.\n"
        voice "audio/voices/ch2/adversary/_shared/stubborn/66.flac"
        stubborn "Bullshit! Whatever. We'll do better next time.\n"
        $ fury_source = "death_downstairs"
        jump fury_start
        # END - contrarian ch. 3?
    else:
        $ adversary_delayed_fight = True
        voice "audio/voices/ch2/adversary/_shared/narrator/136.flac"
        play audio "audio/one_shot/footstep_run_dirt_short.flac"
        hide adversary onlayer back
        hide adversary onlayer front
        hide farback onlayer back
        hide farback onlayer farback
        hide bg onlayer back
        scene bg adversary readying onlayer back at Position(ypos=1125)
        if adversary_1_chains_broken == False:
            show chain adversary readying onlayer front at Position(ypos=1125)
        show adversary readying onlayer front at Position(ypos=1125)
        with dissolve
        n "Finally ready to complete your destined task, you launch off the wet stone floor of the basement and catapult yourself headlong towards the Princess.\n"
        voice "audio/voices/ch2/adversary/_shared/hero/54.flac"
        hero "Here we go. Let's make this count.\n"
        voice "audio/voices/ch2/adversary/_shared/stubborn/67.flac"
        stubborn "Oh, we'll make it count, alright.\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/137.flac"
        $ default_mouse = "blood"
        play audio "audio/one_shot/knife_slash.flac"
        hide chain onlayer front
        hide bg onlayer back
        hide adversary onlayer front
        show bg adversary throat grab onlayer back at Position(ypos=1125)
        show adversary chest slashed onlayer front at Position(ypos=1125)
        show player slash onlayer inyourface at Position(ypos=1125)
        with dissolve
        n "As you bridge the gap, your blade slashes across the Princess' chest, splitting skin and drawing a jagged line of bright red blood.\n"
        voice "audio/voices/ch2/adversary/_shared/narrator/138.flac"
        play audio "audio/final/Adversary_HandThroughChest_1.flac"
        hide player onlayer inyourface
        show adversary chest slashed counter onlayer front with hpunch
        with dissolve
        n "But she's unfazed by your onslaught. Her expression barely changes as her fist collides with your ribs, cracking them like twigs and driving you right back down to the basement floor.\n"
        play audio "audio/one_shot/collapse.flac"
        hide adversary onlayer front
        hide bg onlayer back
        scene bg black onlayer back
        if adversary_1_chains_broken == False:
            $ adversary_1_chains_broken = True
            play audio "audio/final/Adversary_ChainSTressBreaking_2.flac"
            voice "audio/voices/ch2/adversary/_shared/narrator/138a.flac"
            n "You can hear her chains snap as you struggle to recover from the impact.\n"
        voice "audio/voices/ch2/adversary/_shared/stubborn/68.flac"
        scene farback adversary f onlayer farback at Position(ypos=1125)
        show bg adversary f onlayer back at Position(ypos=1125)
        show adversary fs disappointed onlayer back at Position(ypos=1125)
        with dissolve
        stubborn "She almost looks disappointed in us. Why is she disappointed in us?!\n"
        voice "audio/voices/ch2/adversary/_shared/princess/adv_102a.flac"
        show adversary fs disappointed talk onlayer back
        with dissolve
        sp "Oh. You don't actually get it, do you?\n"
        voice "audio/voices/ch2/adversary/_shared/princess/adv_103.flac"
        show adversary fs serious talk onlayer back
        with dissolve
        sp "That knife may be sharp, but you clearly don't want to kill me.\n"
        voice "audio/voices/ch2/adversary/_shared/princess/adv_104.flac"
        show adversary fs grin talk onlayer back
        with dissolve
        sp "It's not fun if you hesitate. It's not fun if you try and trick me and make me bleed out. It's only fun if you go straight for the heart.\n"
        voice "audio/voices/ch2/adversary/_shared/princess/adv_104a.flac"
        show adversary fs disappointed talk onlayer back
        with dissolve
        sp "You need to put everything you have into seeing me dead... or what's the point?\n"
        voice "audio/voices/ch2/adversary/_shared/princess/adv_105.flac"
        show adversary fs kill me onlayer back
        with dissolve
        sp "So don't be afraid. Don't hesitate. Kill me!\n"
        if adversary_1_narrator_proof:
            voice "audio/voices/ch2/adversary/_shared/narrator/139.flac"
            n "Don't let her get into your head. Reincarnation or not, this world needs you to win.\n"
        else:
            voice "audio/voices/ch2/adversary/_shared/narrator/140.flac"
            n "Don't let her get into your head. You've only got one shot at this.\n"
        voice "audio/voices/ch2/adversary/_shared/hero/55.flac"
        hero "She's huge, but that probably means she's slower than us. Take it slow, think it through, and don't panic. Bleeding her out is our best course of action.\n"
        voice "audio/voices/ch2/adversary/_shared/stubborn/69.flac"
        stubborn "Don't listen to them. She understands something that they don't. The only way to win, the only way out of this, is through her.\n"
        label adversary_delayed_fight_menu:
            menu:
                extend ""

                "{i}• [[Bait an opening and outmaneuver her.]{/i}":
                    jump adversary_1_fight_agile

                "{i}• [[Strike at her heart head-on.]{/i}":
                    default adversary_slashed = False
                    $ adversary_slashed = True
                    voice "audio/voices/ch2/adversary/_shared/narrator/141.flac"
                    n "Okay. If that's your plan, then that's your plan. You push yourself off the ground, ignoring the pain in your ribs as you charge at the Princess once more.\n"
                    play audio "audio/one_shot/footstep_run_dirt_short.flac"
                    hide farback onlayer farback
                    hide adversary onlayer back
                    hide adversary onlayer front
                    hide farback onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide player onlayer inyourface
                    scene bg black with fade
                    jump adversary_1_fight_immediate_late_join

                "{i}• [[Run.]{/i}" if adversary_can_fury:
                    if fury_encountered:
                        $ adversary_can_fury = False
                        voice "audio/voices/mound/bonus/path.flac"
                        mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                        voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                        hero "Wait... what?!\n"
                        jump adversary_delayed_fight_menu
                    jump adversary_flee_late_join


label adversary_1_fight_agile:
    play audio "audio/final/adversary_charge.flac"
    hide adversary onlayer back
    hide adversary onlayer front
    hide farback onlayer back
    hide farback onlayer farback
    hide bg onlayer back
    scene bg black
    if adversary_1_style == "agile":
        voice "audio/voices/ch2/adversary/_shared/narrator/142.flac"
        n "As the Princess barrels towards you, you do your best to maneuver between the tight walls of the basement.\n"
    else:
        voice "audio/voices/ch2/adversary/_shared/narrator/143.flac"
        n "You push yourself off the ground and attack the Princess, trying to bait an opening.\n"
    $ gallery_adversary.unlock_item(15)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/adversary/_shared/narrator/144.flac"
    play audio "audio/final/Adversary_ABackAndForth_1.flac"
    scene bg adversary throat grab onlayer back at Position(ypos=1125)
    show battle1 adversary agility onlayer front at Position(ypos=1125)
    with dissolve
    n "You do your best to outplay her, slashing out and leaving red cuts in the tattered remains of her white dress, but you have little room to maneuver. For every glancing blow you manage to land, she slams you against the wall in retaliation, each impact threatening to be the last.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/70.flac"
    show battle2 adversary agility onlayer inyourface at Position(ypos=1125)
    stubborn "This weak little dance isn't working. Just toughen up and overpower her!\n"
    voice "audio/voices/ch2/adversary/_shared/hero/56.flac"
    play audio "audio/final/Adversary_PlayerRagdolledSlammed_1.flac"
    $ blade_held = False
    $ default_mouse = "default"
    play secondary "audio/one_shot/knife_bounce_several.flac"
    hide battle1 onlayer front
    hide battle2 onlayer inyourface
    hide bg onlayer back
    scene bg black
    with fade
    hero "She's throwing us around like a ragdoll. I think 'overpowering her' is a little out of the question.\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_106.flac"
    scene bg adversary throat grab onlayer back at Position(ypos=1125)
    show adversary finale eyes onlayer front at Position(ypos=1125)
    with dissolve
    sp "Did you think you could stop me with a few cuts? All this dancing around is doing nothing but annoying me. I own this place. And I own you.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/145.flac"
    play audio "audio/final/Adversary_HoleBeingPunchesRock_1.flac"
    hide adversary onlayer front
    show adversary agility grab onlayer front at Position(ypos=1125)
    with dissolve
    n "The Princess' arm shoots forward, her palm wrapping around your head, fingers gripping your skull.\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_107.flac"
    play audio "audio/final/Adversary_PowerfulFingersDiggingSkull_2.flac"
    show adversary agility grab talk onlayer front
    with dissolve
    sp "How disappointing.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/146.flac"
    play audio "audio/final/Adversary_SkullBreaksBrain_2.flac"
    hide adversary onlayer front
    hide bg onlayer back
    show adversary agility head squish onlayer front at Position(ypos=1125)
    stop music fadeout 5.0
    stop sound fadeout 5.0
    stop secondary fadeout 5.0
    stop tertiary fadeout 5.0
    n "She squeezes, the pressure unbearable as her fingers dig into your scalp. The last thing you hear is the unsettling crack of your skull and the sickening churn of what was your grey matter.\n"
    hide adversary onlayer front
    scene bg black
    voice "audio/voices/ch2/adversary/_shared/narrator/147.flac"
    n "Everything goes dark, and you die.\n"
    $ trait_hunted = True
    jump adversary_2_start

label adversary_free_attempt:

    voice "audio/voices/ch2/adversary/_shared/narrator/148.flac"
    n "I'm sorry, did I hear that right? Did you just say you're going to try and free her?\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/71.flac"
    stubborn "She doesn't even want to be free!\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/149.flac"
    n "Exactly. So beyond the apocalyptic moral implications of letting her out, how do you even think that's going to work?\n"
    voice "audio/voices/ch2/adversary/_shared/hero/57.flac"
    hero "I mean, we have a weapon, right? We could always just cut her out, yeah?\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/150.flac"
    n "While she's trying to kill you?\n"
    voice "audio/voices/ch2/adversary/_shared/hero/58.flac"
    hero "Yeah, why not?\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/151.flac"
    n "{i}Sigh{/i}. And then what? Do you think she'll just follow you out of here?\n"
    voice "audio/voices/ch2/adversary/_shared/hero/59.flac"
    hero "Maybe? I don't know. It's worth a shot, isn't it?\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/152.flac"
    n "No. It's not.\n"
    menu:
        extend ""

        "{i}• We're doing it. [[Free the Princess.]{/i}":
            voice "audio/voices/ch2/adversary/_shared/narrator/153.flac"
            n "Actually, no. You're not. I have a responsibility to the world here, and I'm not just going to let you throw yourself into a scenario where the literal best outcome is the end of everything.\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/154.flac"
            n "Until you come up with any other idea, your body remains standing rigidly in place.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/72.flac"
            stubborn "What do you think you're doing? You can't just order our body around like it's some sort of... doll!\n"
            $ gallery_adversary.unlock_item(9)
            $ renpy.save_persistent()
            voice "audio/voices/ch2/adversary/_shared/narrator/155.flac"
            show player adversary flipoff onlayer inyourface at Position(ypos=1125)
            with dissolve
            n "Watch me. Your left arm lifts towards the ceiling, and your hand twists into an obscene gesture. See? I can make you do whatever I want.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/73.flac"
            stubborn "So what, you barely managed to lift our arm.\n"
            voice "audio/voices/ch2/adversary/_shared/princess/adv_108.flac"
            if adversary_1_narrator_accepts_origin == "distant":
                show adversary d crossed talk onlayer back
            else:
                show adversary c neutral talk onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                with dissolve
            sp "What are you doing? What is that? Why are you moving so... weird?\n"
            voice "audio/voices/ch2/adversary/_shared/narrator/156.flac"
            if adversary_1_narrator_accepts_origin == "distant":
                show adversary d flipoff onlayer back
            else:
                show adversary c flipoff onlayer front at Position(ypos=1125)
                if adversary_1_chains_broken == False:
                    show chain adversary c neutral onlayer front
                with dissolve
            n "The Princess, taken aback, flashes her own rude gesture in return.\n"
            voice "audio/voices/ch2/adversary/_shared/stubborn/74.flac"
            stubborn "Hey, you. Decision-maker. I want us to fight her as much as he wants us to kill her, but this is boorish. Just ignore him. If you want to try and free her, I don't think there's much he can do to actually stop you.\n"
            menu:

                extend ""

                "{i}• [[Attack the Princess.]{/i}":
                    label adversary_skeptic_fight_join:
                        play audio "audio/one_shot/footstep_run_dirt_short.flac"
                        hide adversary onlayer back
                        hide adversary onlayer front
                        hide farback onlayer back
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide player onlayer inyourface
                        scene bg adversary readying onlayer back at Position(ypos=1125)
                        if adversary_1_chains_broken == False:
                            show chain adversary readying onlayer front at Position(ypos=1125)
                        show adversary readying onlayer front at Position(ypos=1125)
                        with dissolve
                        jump adversary_1_fight

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

                "{i}• [[Free the Princess.]{/i}":
                    voice "audio/voices/ch2/adversary/_shared/narrator/157.flac"
                    play audio "audio/one_shot/footstep_run_dirt_short.flac"
                    hide farback onlayer farback
                    hide adversary onlayer back
                    hide adversary onlayer front
                    hide farback onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide player onlayer inyourface
                    scene bg adversary readying onlayer back at Position(ypos=1125)
                    if adversary_1_chains_broken == False:
                        show chain adversary readying onlayer front at Position(ypos=1125)
                    show adversary readying onlayer front at Position(ypos=1125)
                    with dissolve
                    n "You know what? Fine. Blade in hand, you charge forward to try and free the Princess from her bindings.\n"

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

                "{i}• [[Attack the Princess.]{/i}":
                    jump adversary_skeptic_fight_join

        "{i}• The Narrator is right. This was a very silly idea. Let's just fight her. [[Attack the Princess.]{/i}":
            jump adversary_skeptic_fight_join

    if adversary_attack_immediate:
        voice "audio/voices/ch2/adversary/_shared/princess/adv_109.flac"
        sp "Finally! I thought I'd knocked a screw loose.\n"
    else:
        voice "audio/voices/ch2/adversary/_shared/princess/adv_110.flac"
        sp "Finally! I have no idea what you were just doing, but I'm glad it's over.\n"
    $ gallery_adversary.unlock_item(14)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/adversary/_shared/narrator/158.flac"
    $ default_mouse = "blood"
    play secondary "audio/one_shot/knife_slash.flac"
    queue secondary "audio/final/Adversary_HandThroughChest_1.flac"
    hide chain onlayer front
    hide adversary onlayer front
    hide bg onlayer back
    show bg adversary throat grab onlayer back at Position(ypos=1125)
    show battle1 adversary free onlayer front at Position(ypos=1125)
    show battle2 adversary free onlayer inyourface at Position(ypos=1125)
    with dissolve
    n "As you slash across her wrist, her elbow comes crashing down on your skull. An unsettling crack echoes in your ears.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/159.flac"
    hide battle1 onlayer front
    hide battle2 onlayer inyourface
    hide bg onlayer back
    hide player onlayer inyourface
    hide player onlayer front
    scene bg black
    stop music fadeout 5.0
    stop sound fadeout 5.0
    stop secondary fadeout 5.0
    stop tertiary fadeout 5.0
    n "It's a devastating blow. Your body crumples to the floor, limbs suddenly refusing to respond. This... might be it.\n"
    voice "audio/voices/ch2/adversary/_shared/princess/adv_111.flac"
    sp "That's it, huh? You've gotten really soft.\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/160.flac"
    n "Everything goes dark, and you die.\n"
    voice "audio/voices/ch2/adversary/_shared/hero/60.flac"
    hero "Really? In just one blow?\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/161.flac"
    n "Yes.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/75.flac"
    stubborn "Oh, come on, that's hardly fair! We're not dead, you're just— you're just flipping the table over!\n"
    voice "audio/voices/ch2/adversary/_shared/narrator/162.flac"
    n "It is what it is. You're dead. Finished. Over.\n"
    voice "audio/voices/ch2/adversary/_shared/stubborn/76a.flac"
    stubborn "{i}Grumbling noises.{/i} All right. Fine. This whole thing's a frustrating mess anyways. We're better off with a fresh start. I'll see you two next time.\n"
    # end - skeptic ch 3
    $ trait_skeptic = True
    jump adversary_2_start

return
