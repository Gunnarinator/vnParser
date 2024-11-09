label adversary_1_fight_immediate:
    default adversary_understanding_comment = False
    default adversary_understanding = ""
    play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
    voice "audio/voices/ch2/adversary/_fight/narrator/1.flac"
    n "Good. With a singular focus, you launch off the wet stone floor of the basement and catapult yourself headlong towards the Princess.\n"
    voice "audio/voices/ch2/adversary/_fight/hero/1.flac"
    hero "Here we go. Let's make this count.\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/1.flac"
    stubborn "Oh, we'll make it count, alright.\n"
    jump adversary_1_fight_immediate_late_join

label adversary_1_fight_immediate_late_join:
    $ default_mouse = "blood"
    voice "audio/voices/ch2/adversary/_fight/narrator/2.flac"
    play audio "audio/final/Tower_KnifeBlow_1.flac"
    hide farback onlayer farback
    hide adversary onlayer back
    hide adversary onlayer front
    hide farback onlayer back
    hide farback onlayer farback
    hide bg onlayer back
    hide chain onlayer front
    hide chain onlayer back
    hide player onlayer inyourface
    scene bg adversary throat grab onlayer back at Position(ypos=1125)
    show adversary bs grin onlayer front at Position(ypos=1125)
    show arm adversary bs shake onlayer front at Position(ypos=1125)
    with dissolve
    n "You can feel flesh give way before a sudden impact blunts your momentum, your weapon tightly lodged in the bone of her arm. She grins at you from behind her guard.\n"
    voice "audio/voices/ch2/adversary/_fight/hero/2a.flac"
    hero "Pull it out. We'll try a different angle.\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/2.flac"
    stubborn "No. We can do this. Just. Keep. Pushing.\n"
    voice "audio/voices/ch2/adversary/_fight/hero/3.flac"
    hero "We're not going to win if our weapon's stuck in her arm.\n"
    menu:
        extend ""

        "{i}• [[Keep pushing.]{/i}":
            $ gallery_adversary.unlock_item(3)
            $ renpy.save_persistent()
            play audio "audio/one_shot/stab_goop.flac"
            voice "audio/voices/ch2/adversary/_fight/narrator/3.flac"
            show blood adversary bs onlayer front at Position(ypos=1125) with hpunch
            n "The Princess' grin widens as the two of you push against each other, her fiery eyes and masochistic glee practically lighting up the dreary cave.\n"
            $ adversary_understanding_comment = True
            if adversary_attack_immediate:
                voice "audio/voices/ch2/adversary/_fight/princess/adv_1.flac"
                show adversary bs grin talk onlayer front
                show arm adversary bs1 onlayer front
                with dissolve
                sp "{i}Yes.{/i} You get it, don't you?\n"
            else:
                voice "audio/voices/ch2/adversary/_fight/princess/adv_2.flac"
                show adversary bs grin talk onlayer front
                show arm adversary bs1 onlayer front
                with dissolve
                sp "{i}Yes.{/i} You finally get it, don't you?\n"
            show adversary bs grin onlayer front
            label adversary_1_blade_fight_push_menu:
                menu:
                    extend ""

                    "{i}• ''I do.''{/i}":
                        $ adversary_understanding = "agree"
                        jump adversary_1_blade_task_explain_join

                    "{i}• (Lie) ''I do.''{/i}":
                        $ adversary_understanding = "lie"
                        jump adversary_1_blade_task_explain_join

                    "{i}• ''What are you talking about?''{/i}":
                        $ adversary_understanding = "question"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_3.flac"
                        show adversary bs grin talk onlayer front with dissolve
                        sp "Are you really going to make me explain it? Look at how evenly matched we are!\n"
                        label adversary_1_blade_task_explain_join:
                            if basement_1_shared_task:
                                voice "audio/voices/ch2/adversary/_fight/princess/adv_4.flac"
                                sp "Dying and coming back. Clashing against each other over the fate of everything. Forever.\n"
                                voice "audio/voices/ch2/adversary/_fight/hero/4.flac"
                                show adversary bs grin onlayer front
                                hero "Did... did she just admit out loud that she's going to end the world if she gets out of here?\n"
                                voice "audio/voices/ch2/adversary/_fight/narrator/4.flac"
                                n "She most certainly did. I hope you've made a mental note of that, Hero. There's no more room for doubt.\n"

                            else:
                                voice "audio/voices/ch2/adversary/_fight/princess/adv_5.flac"
                                show adversary bs grin talk onlayer front with dissolve
                                sp "Nothing exists outside of us. It's just you and me. Dying and coming back. Clashing against each other. Forever.\n"
                                voice "audio/voices/ch2/adversary/_fight/narrator/5.flac"
                                show adversary bs grin onlayer front
                                n "That's not what's going on. There's an entire world at stake here!\n"

                            if adversary_understanding != "agree":
                                voice "audio/voices/ch2/adversary/_fight/stubborn/3.flac"
                                stubborn "Don't you all get it? The fate of the world doesn't matter. The only thing that matters is this fight.\n"
                                voice "audio/voices/ch2/adversary/_fight/princess/adv_6.flac"
                                show adversary bs grin talk onlayer front with dissolve
                                sp "And look at us. We're both so much stronger than we were last time. Think about how much more we can become. Nothing is better than this.\n"
                                voice "audio/voices/ch2/adversary/_fight/stubborn/4.flac"
                                show adversary bs grin onlayer front
                                stubborn "She's right. Imagine how much further we can push each other. Imagine how strong we can be.\n"
                                voice "audio/voices/ch2/adversary/_fight/narrator/6.flac"
                                n "I warned you on the stairs and I'll warn you again. Don't get caught up in emotion. Remember why you're here.\n"
                                voice "audio/voices/ch2/adversary/_fight/princess/adv_7.flac"
                                show adversary bs grin talk onlayer front with dissolve
                                sp "Ugh. I hate using words. They're so clumsy.\n"
                            else:
                                voice "audio/voices/ch2/adversary/_fight/stubborn/5.flac"
                                stubborn "Yes! The fate of the world doesn't matter. The only thing that matters is this fight. The only thing that matters is getting {i}stronger{/i}. And the only way to get stronger is to {i}win{/i}. Even if it takes us forever to get there.\n"

                    "{i}• [[Silently continue pushing.]{/i}":
                        $ adversary_understanding_agree = True
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_8a.flac"
                        show adversary bs grin talk onlayer front with dissolve
                        sp "Yes! You're right! We don't even need to talk about it!\n"

                    "{i}• [[Unlodge the blade.]{/i}":
                        jump adversary_1_blade_fight_unlodge_join

            voice "audio/voices/ch2/adversary/_fight/narrator/7.flac"
            play audio "audio/final/Adversary2_PowerfulGrab_1.flac"
            hide adversary onlayer front
            hide blood onlayer front
            hide arm onlayer front
            show adversary bs knee onlayer front at Position(ypos=1125) with hpunch
            with dissolve
            n "Your balance is suddenly thrown off as the Princess pulls you into her knee.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/8.flac"
            play audio "audio/final/Adversary_SkullBreaksBrain_2.flac"
            hide bg onlayer back
            hide adversary onlayer front
            scene bg black
            n "It collides with your ribs and you feel them splinter, cracking like wet wood from the impact.\n"
            if adversary_1_chains_broken == False:
                $ adversary_1_chains_broken = True
                voice "audio/voices/ch2/adversary/_fight/narrator/8a.flac"
                n "As she strikes you again you hear the whine of straining metal, and then a snap — it would appear that she's loose.\n"
            voice "audio/voices/ch2/adversary/_fight/stubborn/6.flac"
            stubborn "We're fine.\n"
            play audio "audio/final/Adversary_BodySMashedAgainstWall_1.flac"
            hide bg onlayer back
            hide adversary onlayer front
            voice "audio/voices/ch2/adversary/_fight/narrator/9.flac"
            n "But you barely have enough time to notice before the Princess follows up and smashes her forehead against yours.\n"
            $ blade_held = False
            $ default_mouse = "default"
            voice "audio/voices/ch2/adversary/_fight/narrator/10.flac"
            play audio "audio/one_shot/collapse.flac"
            scene farback adversary f onlayer farback at Position(ypos=1125)
            show bg adversary f onlayer back at Position(ypos=1125)
            show adversary ff blade stuck onlayer back at Position(ypos=1125)
            with fade
            n "Your grip loosens from the impact, the blade still wedged in her arm as you tumble to the cold stone floor.\n"
            voice "audio/voices/ch2/adversary/_fight/stubborn/7.flac"
            stubborn "I said we're {i}fine{/i}.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/11.flac"
            n "I didn't say you weren't fine. I was just describing what happened.\n"
            voice "audio/voices/ch2/adversary/_fight/hero/5.flac"
            hero "You might not have said as much, but you certainly implied it.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/12.flac"
            play audio "audio/final/Adversary_StabCut_10.flac"
            show adversary ff blade pull onlayer back
            with dissolve
            n "It really doesn't matter. The Princess glances down at the blade embedded in her arm, and with near total ignorance to pain, slides it out of its sinewy prison.\n"
            voice "audio/voices/ch2/adversary/_fight/princess/adv_9.flac"
            play audio "audio/one_shot/knife_bounce_several.flac"
            show adversary ff blade toss onlayer back
            show knife f close onlayer back at Position(ypos=1125)
            with dissolve
            sp "You forgot this.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/13.flac"
            show adversary ff grin onlayer back
            with dissolve
            n "She tosses it at your feet.\n"
            label adversary_1_blade_fight_first_join:
                default adversary_blade_first_gun_jump = False
                default adversary_blade_first_metaphor = False
                default adversary_blade_first_understanding = False
                default adversary_blade_can_understanding = False
                menu:

                    extend ""

                    "{i}• (Explore) I hope you heard all of that, Mr. Narrator. This is a lot different than last time, but last time definitely {b}happened{/b}.{/i}" if adversary_1_forest_share_loop and adversary_1_narrator_proof == False:
                        $ adversary_1_narrator_proof = True
                        if adversary_blade_can_understanding:
                            $ adversary_blade_can_understanding = False
                        if adversary_1_forest_share_loop_insist:
                            voice "audio/voices/ch2/adversary/_shared/narrator/1.flac"
                            n "Okay, fine. Let's say for a moment that I believe you.\n"
                        else:
                            voice "audio/voices/ch2/adversary/_shared/narrator/2.flac"
                            n "What's that? Oh, that whole 'déjà vu' situation. Yes it does seem like you and the Princess remember each other, so let's say for a moment that I {b}do{/b} believe you.\n"
                        voice "audio/voices/ch2/adversary/_shared/narrator/3.flac"
                        n "For all you know, whatever happened to you last time was a fluke, and beyond that, do you know who doesn't remember anything that happened last time? Me. I. Don't. Remember.\n"
                        voice "audio/voices/ch2/adversary/_fight/hero/6.flac"
                        hero "Are... are you okay?\n"
                        voice "audio/voices/ch2/adversary/_shared/narrator/4.flac"
                        n "Of course I'm not okay! As far as we're all concerned, the fate of my world is still very much on the line. Not all of us have the luxury of jumping over to a parallel universe the second we die.\n"
                        jump adversary_1_blade_fight_first_join

                    "{i}• (Explore) ''Aren't you jumping the gun a little here? We each died {b}once{/b}. That doesn't mean we're {b}immortal{/b}.''{/i}" if adversary_blade_first_gun_jump == False:
                        $ adversary_blade_first_gun_jump = True
                        if adversary_blade_can_understanding:
                            $ adversary_blade_can_understanding = False
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_10.flac"
                        show adversary ff grin talk onlayer back
                        with dissolve
                        sp "How much more proof do you need? Would it help to watch me rise from the dead with your own two eyes?\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_11.flac"
                        show adversary ff love talk onlayer back
                        with dissolve
                        sp "Fine. Go ahead. Stab me in the heart. See what happens.\n"
                        voice "audio/voices/ch2/adversary/_fight/narrator/14.flac"
                        show adversary ff exposed onlayer back
                        with dissolve
                        n "The Princess throws open her arms, exposing her chest. Is... she really just going to let you slay her? {b}Do it{/b}. Do it {b}right now{/b} before she changes her mind.\n"
                        voice "audio/voices/ch2/adversary/_fight/hero/7.flac"
                        hero "Hold on. What if this is a trick? If she's leaving herself open like this, there's only one way we can strike at her. For all we know she's three steps ahead of us.\n"
                        voice "audio/voices/ch2/adversary/_fight/stubborn/8.flac"
                        stubborn "Three steps ahead of us? Have you met her? This isn't a trick.\n"
                        voice "audio/voices/ch2/adversary/_fight/hero/8.flac"
                        hero "And how would you know that?\n"
                        voice "audio/voices/ch2/adversary/_fight/stubborn/9.flac"
                        stubborn "Because {b}I{/b} wouldn't think to trick us. So why would she?\n"
                        voice "audio/voices/ch2/adversary/_fight/narrator/15.flac"
                        n "That's a great point. So please, stop hesitating and end this now.\n"
                        label adversary_blade_kill_me_menu:
                            default adversary_blade_kill_me_dropped = False
                            default adversary_blade_kill_me_trick_explore = False
                            menu:
                                extend ""

                                "{i}• (Explore) ''How do I know you're not tricking me?''{/i}" if adversary_blade_kill_me_trick_explore == False and adversary_blade_kill_me_dropped == False:
                                    $ adversary_blade_kill_me_trick_explore = True
                                    voice "audio/voices/ch2/adversary/_fight/princess/adv_12.flac"
                                    show adversary ff love talk onlayer back
                                    with dissolve
                                    sp "I'm not tricking you! I just don't want you to be afraid. It's {b}boring{/b} if you're afraid. Neither of us can die in any way that matters. If you need proof, then {b}take it{/b}.\n"
                                    show adversary ff exposed onlayer back
                                    with dissolve
                                    jump adversary_blade_kill_me_menu

                                "{i}• (Explore) ''Cut it out, will you? I'm not going to take a cheap win like that.''{/i}" if adversary_blade_kill_me_dropped == False:
                                    $ adversary_blade_kill_me_dropped = True
                                    voice "audio/voices/ch2/adversary/_fight/narrator/16.flac"
                                    show adversary ff grin onlayer back
                                    with dissolve
                                    n "The Princess grins as her arms fall back to her sides.\n"
                                    voice "audio/voices/ch2/adversary/_fight/princess/adv_13.flac"
                                    show adversary ff grin talk onlayer back
                                    with dissolve
                                    sp "Good. Enough talk. Let's fight.\n"
                                    jump adversary_blade_kill_me_menu

                                "{i}• [[Slay the Princess.]{/i}":
                                    $ blade_held = True
                                    $ default_mouse = "blood"
                                    play audio "audio/one_shot/knife_pickup.flac"
                                    if adversary_blade_kill_me_dropped == False:
                                        jump adversary_stabbed_heart
                                    else:
                                        jump adversary_penultimate

                    "{i}• (Explore) ''Were you being metaphorical when you said that nothing exists outside of us? There's more to the world than just this cabin. I saw trees and everything on my way here.''{/i}" if adversary_blade_first_metaphor == False:
                        $ adversary_blade_first_metaphor = True
                        $ adversary_blade_can_understanding = True
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_14.flac"
                        show adversary ff confused talk onlayer back
                        with dissolve
                        sp "I meant that nothing else matters. It's hard to describe, it's just a feeling. That it's just {b}us{/b}. That when we hurt each other we're alive and when that happens everything else is gone.\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_15.flac"
                        sp "You feel it too, right?\n"
                        show adversary ff confused onlayer back
                        with dissolve
                        jump adversary_1_blade_fight_first_join

                    "{i}• (Explore) ''Don't you want to be free, though? Isn't there more to life than waking up chained in a basement and fighting to the death in an endless loop?''{/i}" if adversary_free_offer == False:
                        $ adversary_free_offer = True
                        if adversary_blade_can_understanding:
                            $ adversary_blade_can_understanding = False
                        voice "audio/voices/ch2/adversary/_fight/narrator/17.flac"
                        n "You're walking a thin line, 'Hero.'\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_16.flac"
                        show adversary ff confused talk onlayer back
                        with dissolve
                        sp "Is there more to life? When you're not here I feel empty and alone. When we're not fighting I feel... stuck. Like there's something important I'm supposed to be doing. Like I'm being shoved into a space where I don't fit.\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_17.flac"
                        show adversary ff grin talk onlayer back
                        with dissolve
                        sp "But when we fight each other... when we fight each other it's like this {b}wave{/b} of feeling.\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_17a.flac"
                        show adversary ff love talk onlayer back
                        with dissolve
                        sp "Like everything I break in you and everything you break in me is important, like we're really, truly communicating.\n"
                        voice "audio/voices/ch2/adversary/_fight/stubborn/10.flac"
                        show adversary ff love onlayer back
                        with dissolve
                        stubborn "Life is suffering, and we will feel every inch of it, and we will persevere.\n"
                        voice "audio/voices/ch2/adversary/_fight/hero/9.flac"
                        hero "Can't say I'm a fan of whatever weird bond those two have.\n"
                        voice "audio/voices/ch2/adversary/_fight/narrator/18.flac"
                        n "Nor am I. It's dangerous. But maybe you can use it to your advantage.\n"
                        # CONTINUE HERE
                        menu:
                            extend ""

                            "{i}• ''Oh I get it, so you're like some sort of psychosexual sadomasochist. That makes sense.''{/i}":
                                voice "audio/voices/ch2/adversary/_fight/princess/adv_18.flac"
                                show adversary ff confused talk onlayer back
                                with dissolve
                                sp "I don't know what that is, but I hated the sound of it coming out of your mouth. I don't like being crammed into smart-sounding boxes.\n"
                                show adversary ff confused onlayer back

                            "{i}• ''There will always be another chance to for us to kill each other.''{/i}":
                                voice "audio/voices/ch2/adversary/_fight/princess/adv_19.flac"
                                show adversary ff frustrated talk onlayer back
                                with dissolve
                                sp "I. Don't. CARE!\n"
                                show adversary ff frustrated onlayer back

                            "{i}• ''There's no getting through to you, is there? Fine.''{/i}":
                                voice "audio/voices/ch2/adversary/_fight/princess/adv_20.flac"
                                show adversary ff frustrated talk onlayer back
                                with dissolve
                                sp "I don't need you to get through to me! I just need you to keep fighting.\n"
                                show adversary ff frustrated onlayer back

                            "{i}• [[Say nothing.]{/i}":
                                voice "audio/voices/ch2/adversary/_fight/princess/adv_21.flac"
                                show adversary ff love talk onlayer back
                                with dissolve
                                sp "I hope you finally get it now...\n"
                                show adversary ff love onlayer back

                            "{i}• ''Okay, sure, I get it now. Let's do this. [[Pick up the blade and attack her again.]{/i}":
                                $ blade_held = True
                                $ default_mouse = "blood"
                                play audio "audio/one_shot/knife_pickup.flac"
                                jump adversary_penultimate


                        jump adversary_1_blade_fight_first_join


                    "{i}• (Explore) ''Is that what you meant when you said I 'understood?' Because if that's the case then I absolutely don't get it. I'm not even sure there's an 'it' to get!''{/i}" if adversary_blade_first_understanding == False and adversary_blade_first_metaphor and adversary_blade_can_understanding:
                        $ adversary_blade_first_understanding = True
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_22.flac"
                        show adversary ff confused talk onlayer back
                        with dissolve
                        sp "Oh...\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_23.flac"
                        show adversary ff frustrated talk onlayer back
                        with dissolve
                        sp "That makes me... angry. No, frustrated. Wait... sad.\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_24.flac"
                        show adversary ff grin talk onlayer back
                        with dissolve
                        sp "Maybe you can still get it, though. If I show you.\n"
                        show adversary ff grin onlayer back
                        jump adversary_1_blade_fight_first_join

                    "{i}• (Explore) ''Yes! The two of us are a chorus of notes building on top of each other forever. The song we write in our blood will be the most beautiful music ever written!''{/i}" if adversary_blade_first_understanding == False and adversary_blade_first_metaphor and adversary_blade_can_understanding:
                        $ adversary_blade_first_understanding = True
                        voice "audio/voices/ch2/adversary/_fight/narrator/19.flac"
                        show adversary ff love onlayer back
                        with dissolve
                        n "Great. It seems like both you and the Princess have bought into some sort of shared delusion. Just make sure that whatever you're using for that 'song written in blood' is mostly hers.\n"
                        voice "audio/voices/ch2/adversary/_fight/stubborn/11.flac"
                        stubborn "{i}Sniff.{/i}\n"
                        voice "audio/voices/ch2/adversary/_fight/narrator/20.flac"
                        n "I'm sorry, are you crying?\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_25.flac"
                        show adversary ff confused onlayer back
                        with dissolve
                        sp "{i}Sniff.{/i}\n"
                        voice "audio/voices/ch2/adversary/_fight/hero/10.flac"
                        hero "Is {b}she{/b} crying?\n"
                        voice "audio/voices/ch2/adversary/_fight/stubborn/12.flac"
                        stubborn "{i}Sniffling.{/i} Are you two not? That was some goddamned poetry.\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_26.flac"
                        show adversary ff confused talk onlayer back
                        with dissolve
                        sp "I'm ready whenever you are.\n"
                        show adversary ff confused onlayer back
                        with dissolve
                        jump adversary_1_blade_fight_first_join

                    "{i}• ''Actually, I think I'm done fighting you. I don't think this is healthy for either of us.''{/i}" if adversary_can_fury:
                        if fury_encountered:
                            $ adversary_can_fury = False
                            voice "audio/voices/mound/bonus/path.flac"
                            mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                            jump adversary_1_blade_fight_first_join
                        $ adversary_combat_to_pacifism = True
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_27.flac"
                        show adversary ff confused talk onlayer back
                        with dissolve
                        sp "You're kidding, right?\n"
                        #if adversary_1_chains_broken == False:
                        #    $ adversary_1_chains_broken = True
                        #    voice "audio/voices/ch2/adversary/_fight/narrator/21.flac"
                        #    n "In a fit of rage, she pulls at her chains, the movement snapping them with terrifying ease.\n"
                        voice "audio/voices/ch2/adversary/_fight/princess/adv_28.flac"
                        show adversary ff frustrated talk onlayer back
                        with dissolve
                        sp "You can't just give up! What do you think you're doing?! This... this isn't fair! This is even worse than deciding not to fight me from the beginning!\n"
                        show adversary ff frustrated onlayer back
                        with dissolve
                        #voice "audio/voices/ch2/adversary/_fight/princess/adv_29.flac"
                        #sp "Gah! Let's see if you still feel that way once I start beating you.\n"
                        jump adversary_pacifism_explore

                    #"{i}• [[Attempt to free the Princess.]{/i}" if adversary_free_offer:
                    #    jump adversary_free_attempt

                    "{i}• [[Pick up the blade and attack her again.]{/i}":
                        $ blade_held = True
                        $ default_mouse = "blood"
                        play audio "audio/one_shot/knife_pickup.flac"
                        jump adversary_penultimate

        "{i}• [[Unlodge the blade and attack her from a different angle.]{/i}":
            label adversary_1_blade_fight_unlodge_join:
                voice "audio/voices/ch2/adversary/_fight/narrator/22.flac"
                play audio "audio/final/Adversary2_PowerfulGrab_1.flac"
                hide adversary onlayer front
                hide blood onlayer front
                hide player onlayer front
                hide arm onlayer front
                show adversary bs knee onlayer front at Position(ypos=1125)
                with dissolve
                n "You pull back on the blade's hilt, doing your best to free it from its sinewed prison. But as you tug the blade free the Princess slams you down onto her knee.\n"
                voice "audio/voices/ch2/adversary/_fight/narrator/23.flac"
                play audio "audio/final/Adversary_SkullBreaksBrain_2.flac"
                hide bg onlayer back
                hide adversary onlayer front
                scene bg black
                n "It collides with your ribs and you feel them splinter, crackling like wet wood from the impact, and you find yourself in midair, effortlessly tossed across the room.\n"
                voice "audio/voices/ch2/adversary/_fight/narrator/24.flac"
                play audio "audio/one_shot/collapse.flac"
                scene farback adversary f onlayer farback at Position(ypos=1125)
                show bg adversary f onlayer back at Position(ypos=1125)
                show adversary ff confused onlayer back at Position(ypos=1125)
                with fade
                n "You hit the floor, your ribs complaining painfully. But you can feel the hilt in your grip. You still have your weapon.\n"
                if adversary_understanding_comment:
                    show adversary ff confused talk onlayer back
                    with dissolve
                    voice "audio/voices/ch2/adversary/_fight/princess/adv_30.flac"
                    sp "Maybe you don't get it.\n"
                jump adversary_1_fight_agile



label adversary_stabbed_heart:
    default adversary_stabbed_heart_accept = False

    define nstub = Character(_("The Narrator and the Voice of the Stubborn"), color = "#ffffff", what_color = "#ffffff", what_text_align=0.5, what_outlines=[ (3, "#000000") ], who_outlines= [ (3, "#000000") ], what_style = "voice_style", ctc="ctc_blink", ctc_position="nestled")

    $ gallery_adversary.unlock_item(8)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/adversary/_fight/narrator/25.flac"
    $ blade_held = True
    $ default_mouse = "blood"
    play audio "audio/one_shot/footstep_run_dirt_short.flac"
    play secondary "audio/one_shot/knife_stab.flac"
    hide adversary onlayer back
    hide adversary onlayer front
    hide farback onlayer back
    hide farback onlayer farback
    hide bg onlayer back
    hide knife onlayer back
    scene bg adversary throat grab onlayer back at Position(ypos=1125)
    show adversary stabbed smile onlayer front at Position(ypos=1125)
    with dissolve
    n "The Princess remains unflinching as you run her down, her stoic expression once again curving into a knowing smile as the pristine blade buries deep into her heart.\n"
    voice "audio/voices/ch2/adversary/_fight/hero/11a.flac"
    hero "Did she really just... let us do that?\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/26.flac"
    n "Apparently, yes.\n"
    voice "audio/voices/ch2/adversary/_fight/princess/adv_31.flac"
    stop music fadeout 3.0
    show adversary stabbed smile talk onlayer front at Position(ypos=1125)
    with dissolve
    sp "See you soon.\n"
    #voice "audio/voices/ch2/adversary/_fight/narrator/27.flac"
    #n "Her smile quivers as blood pools at its edges.\n"
    # stop music
    $ blade_held = False
    $ default_mouse = "default"

    $ achievement.grant("ACH_ADV_BAIT")
    voice "audio/voices/ch2/adversary/_fight/narrator/28.flac"
    hide adversary onlayer front
    hide bg onlayer back
    play audio "audio/one_shot/collapse.flac"
    scene farback adversary basement onlayer farback at Position(ypos=1125)
    show bg adversary basement onlayer back at Position(ypos=1125)
    show adversary d dead onlayer back at Position(ypos=1125)
    with Dissolve(2.0)
    n "And then she stumbles back into the wall, the blade still lodged firmly in her chest. She collapses to the ground.\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/29.flac"
    n "She's dead. It's over. It's finally over.\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/13.flac"
    stubborn "But... but it can't be over! She said she'd be back!\n"
    voice "audio/voices/ch2/adversary/_fight/hero/12.flac"
    hero "I know the two of you had some sort of weird... bond. But look on the bright side. Now we don't have to die! Isn't that nice?\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/14a.flac"
    stubborn "No! It's not nice! I wanted to fight her forever! This... this is shit! It's not fair!\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/30.flac"
    n "Life isn't fair, but what's done is done, and whether you like it or not, the entire world is in your debt for saving it from ruin. I'm sure in due time you'll learn to live with yourself.\n"
    voice "audio/voices/ch2/adversary/_fight/hero/13.flac"
    hero "Let's just get out of here.\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/31.flac"
    n "Yes, that sounds like a splendid idea.\n"
    menu:
        extend ""

        "{i}• [[Watch her body for a little while longer.]{/i}":
            voice "audio/voices/ch2/adversary/_fight/narrator/32.flac"
            n "{i}Sigh{/i}. Fine. You remain where you are and watch over the Princess' corpse.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/33.flac"
            n "She remains dead.\n"

        "{i}• [[Turn and leave.]{/i}":
            $ adversary_stabbed_heart_accept = True
            voice "audio/voices/ch2/adversary/_fight/narrator/34.flac"
            n "Thank you for listening to reason. For a second there I was concerned you'd bought into that stubborn one's madness.\n"
            voice "audio/voices/ch2/adversary/_fight/stubborn/15.flac"
            stubborn "Madness? I'm the only sane one here! I understand what we're supposed to be! The rest of you are in denial!\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/35.flac"
            play audio "audio/one_shot/footsteps_stone.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide adversary onlayer back
            scene bg adversary stairs onlayer back at Position(ypos=1125)
            with fade
            n "You turn your back to the Princess and make your way to the base of the stairs. It's time for you to move on to a new, safer chapter of your life.\n"

    voice "audio/voices/ch2/adversary/_fight/stubborn/16.flac"
    stubborn "I'm telling you, she's coming back. She said she's coming back.\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/36.flac"
    n "She's not.\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/17a.flac"
    stubborn "She is!\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/37.flac"
    n "She's not. Coming. Back. She's DEAD. Your blade is embedded in her heart. You slew her. It's over. I don't know how many more times or how many different ways I need to express this objective reality before it finally makes its way through your dense skull.\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/18.flac"
    stubborn "How many different ways have you got left to express it? Because it'll take a hell of a lot more to convince me that she's not coming back.\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/38.flac"
    n "Oh I've got plenty.\n"
    voice "audio/voices/ch2/adversary/_fight/hero/14.flac"
    hero "Can the two of you stop arguing?\n"
    voice "audio/voices/ch2/adversary/_fight/nstub.flac"
    nstub "NO!\n"
    if adversary_stabbed_heart_accept:
        play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
        voice "audio/voices/ch2/adversary/_fight/princess/adv_32.flac"
        sp "Hahahaha! Yes! I told you I'd be back!\n"
        voice "audio/voices/ch2/adversary/_fight/hero/15.flac"
        hero "What was that?\n"
        voice "audio/voices/ch2/adversary/_fight/stubborn/19.flac"
        stubborn "You know what that was.\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/39.flac"
        n "Yes. That's the sound of the entire world being shit out of luck.\n"
        voice "audio/voices/ch2/adversary/_fight/princess/adv_33.flac"
        sp "Are you walking away from me? You didn't think this would work, did you? I can't believe you were just going to leave me here.\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/40.flac"
        play audio "audio/final/footsteps_stone_short.flac"
        hide bg onlayer back
        scene farback adversary basement onlayer farback at Position(ypos=1125)
        show bg adversary basement onlayer back at Position(ypos=1125)
        show adversary d revive stand up onlayer back at Position(ypos=1125)
        with Dissolve(2.0)
        n "You turn around to see the Princess stumbling to her feet, one hand wrapped around the hilt of the blade you buried in her heart.\n"
        voice "audio/voices/ch2/adversary/_fight/princess/adv_34.flac"
        show adversary d revive standing talk onlayer back
        sp "You're not getting out of this that easy.\n"
        jump adversary_no_die_join
    else:
        play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
        show adversary d revive onlayer back
        voice "audio/voices/ch2/adversary/_fight/hero/16.flac"
        hero "I'm not the only one who just saw her eyes open, right?\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/41.flac"
        n "What are you talking about, for the millionth time she's—\n{w=2.70}{nw}"
        show screen disableclick(0.5)
        voice "audio/voices/ch2/adversary/_fight/princess/adv_32.flac"
        show adversary d revive talk onlayer back
        with dissolve
        sp "Hahahaha! Yes! I told you I'd be back!\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/42.flac"
        show adversary d revive onlayer back
        with dissolve
        n "Alive. We're shit out of luck, aren't we?\n"
        voice "audio/voices/ch2/adversary/_fight/stubborn/20.flac"
        stubborn "I knew it! I told you all we should believe in her! This is perfect!\n"
        voice "audio/voices/ch2/adversary/_fight/princess/adv_35.flac"
        show adversary d revive talk onlayer back
        with dissolve
        sp "And you waited for me. I knew I could count on you, I knew we were {i}connected{/i}.\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/43.flac"
    play audio "audio/final/footsteps_stone_short.flac"
    show adversary d revive stand up onlayer back
    with dissolve
    n "The Princess staggers to her feet, one hand wrapped around the hilt of the blade you buried in her heart.\n"
    voice "audio/voices/ch2/adversary/_fight/princess/adv_36.flac"
    sp "We don't even need to start over anymore, do we? Let's go again!\n"
    jump adversary_no_die_join

label adversary_no_die_join:

    $ gallery_adversary.unlock_item(7)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/adversary/_fight/narrator/44.flac"
    play audio "audio/final/Adversary_StabCut_10.flac"
    show adversary d revive standing pull onlayer back
    with dissolve
    n "She pulls the weapon from her chest, barely wincing, and hurls it at your feet.\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/21.flac"
    play audio "audio/one_shot/knife_bounce_several.flac"
    show adversary d revive standing onlayer back
    show knife floor onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    stubborn "You know what to do. Again!\n"
    voice "audio/voices/ch2/adversary/_fight/hero/17.flac"
    hero "But she came back! What's the point of fighting her if she can just do that?\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/45.flac"
    n "All of you need to settle down! This whole situation is coming dangerously close to untethering. She clearly never actually died. You just missed her heart, that's all.\n"
    voice "audio/voices/ch2/adversary/_fight/hero/18a.flac"
    hero "Oh. We just missed her heart. Of course! That's all. You were the one who said we hit her heart! You were the one who said it was 'finally over!'\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/46.flac"
    n "Well I guess I had it wrong!\n"
    voice "audio/voices/ch2/adversary/_fight/hero/19.flac"
    hero "You guess you had it wrong? Aren't you supposed to know everything?\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/47.flac"
    n "I never said I knew {i}everything{/i}.\n"
    label adversary_stabbed_heart_menu:
        default adversary_cant_die_thought = False
        default adversary_cant_die_lie = False
        menu:
            extend ""

            "{i}• (Explore) 'Close to untethering?' What's that supposed to mean?{/i}":
                voice "audio/voices/ch2/adversary/_fight/narrator/48.flac"
                n "Nothing. It means nothing. I shouldn't have said that.\n"
                voice "audio/voices/ch2/adversary/_fight/hero/20.flac"
                hero "But you did say it, so it means something.\n"
                voice "audio/voices/ch2/adversary/_fight/stubborn/22.flac"
                stubborn "Oh stop bickering over nothing. Our destiny is right in front of us. Pick up the blade, and go to her!\n"
                voice "audio/voices/ch2/adversary/_fight/narrator/49.flac"
                n "Okay fine. That is what I meant by 'untethering.' Do you hear him rambling on about destiny? He's lost the thread, and if you lose the thread, you won't be able to save the world.\n"
                voice "audio/voices/ch2/adversary/_fight/hero/21.flac"
                hero "And what is {i}that{/i} supposed to mean?\n"
                voice "audio/voices/ch2/adversary/_fight/narrator/50.flac"
                n "I don't have to answer that, and I'm not going to answer that.\n"
                voice "audio/voices/ch2/adversary/_fight/hero/22.flac"
                hero "Why the bloody hell not?\n"
                voice "audio/voices/ch2/adversary/_fight/narrator/51.flac"
                n "Because right now, there's still a razor-thin chance that you're able to get your act together. There are patterns of thought out there that beg to be finished but once you finish them... that's it. They change everything, there's no going back, and if I say anything else, you're going to finish one of those thoughts.\n"
                voice "audio/voices/ch2/adversary/_fight/hero/23.flac"
                hero "{i}What?!{/i}\n"
                menu:
                    extend ""

                    "{i}• The Princess Can't Die.{/i}":
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• You mean like 'The Princess Can't Die' don't you? Well, it's too late for that. I think we've all thought that one.{/i}":
                        label adversary_stabbed_heart_cant_die:
                            $ gallery_adversary.unlock_item(10)
                            $ renpy.save_persistent()
                            $ achievement.grant("ACH_ADV_NO_DIE")
                            if adversary_cant_die_thought == False:
                                voice "audio/voices/ch2/adversary/_fight/narrator/52.flac"
                                n "{i}Sigh.{/i} Yes. Exactly. Like The Princess Can't Die. I tried, you know. I tried very hard to make this work.\n"
                            else:
                                voice "audio/voices/ch2/adversary/_fight/narrator/53.flac"
                                n "But you did think it, didn't you? {i}Sigh{/i}. I tried, you know. I tried very hard to make this work.\n"
                            $ adversary_cant_die_thought = True
                            voice "audio/voices/ch2/adversary/_fight/hero/24.flac"
                            hero "I. I don't like that resignation. Are you sure we can't just unthink it?\n"
                            voice "audio/voices/ch2/adversary/_fight/narrator/54.flac"
                            n "Yes. Like I said, I'm afraid some thoughts can't be unthought. I'll be back in a moment. I'm going to pour myself a stiff drink. If I'm going to see the end of everything, I'd rather not be sober.\n"
                            voice "audio/voices/ch2/adversary/_fight/stubborn/23.flac"
                            stubborn "So I was right! Why are all of you so glum? This is perfect, isn't it? We get to experience greatness and battle and triumph forever.\n"
                            voice "audio/voices/ch2/adversary/_fight/narrator/55.flac"
                            n "Well, I think it was the stubborn one who said your destiny awaits, right?\n"
                            voice "audio/voices/ch2/adversary/_fight/hero/25.flac"
                            hero "No no no. No. Hold on, there has to be another way. What if we just leave her down here? What if we run away? What if we convince her to {i}not{/i} end the world?\n"
                            voice "audio/voices/ch2/adversary/_fight/narrator/56.flac"
                            n "You can't reason with her. Ending the world is her fundamental nature. It's not a decision she can flip on and off. It is her.\n"
                            voice "audio/voices/ch2/adversary/_fight/hero/26.flac"
                            hero "And why exactly can't we leave her down here?\n"
                            voice "audio/voices/ch2/adversary/_fight/narrator/57.flac"
                            n "Because all it would do is stall the inevitable.\n"
                            voice "audio/voices/ch2/adversary/_fight/hero/27.flac"
                            hero "And what's wrong with stalling?\n"
                            voice "audio/voices/ch2/adversary/_fight/narrator/58.flac"
                            n "Oh there's plenty wrong with stalling. The end is still the end, and I'd rather face mine head-on.\n"
                            voice "audio/voices/ch2/adversary/_fight/hero/28a.flac"
                            hero "Oh you mopey ass. Why did you even ask us to slay her if it was going to end like this?\n"
                            voice "audio/voices/ch2/adversary/_fight/narrator/59.flac"
                            n "Because it didn't have to end like this. If you don't mind, I'd rather not spend everyone's last moments arguing with you.\n"
                            voice "audio/voices/ch2/adversary/_fight/stubborn/24.flac"
                            stubborn "It's time.\n"
                            voice "audio/voices/ch2/adversary/_fight/narrator/60.flac"
                            n "Yes. I suppose it is.\n"
                            voice "audio/voices/ch2/adversary/_fight/hero/29.flac"
                            hero "If... if we fight her forever, then maybe she can't end the world. Maybe everything can still work out.\n"
                            voice "audio/voices/ch2/adversary/_fight/narrator/61.flac"
                            n "I guess we'll just have to see how things play out.\n"
                            voice "audio/voices/ch2/adversary/_fight/princess/adv_37.flac"
                            show adversary d revive standing talk noknife onlayer back
                            with dissolve
                            sp "Don't you get it? You don't have to shuffle your feet. What comes next is going to last {i}forever{/i}.\n"
                            show adversary d revive standing onlayer back
                            menu:
                                extend ""

                                "{i}• [[Join your Adversary.]{/i}":
                                    $ blade_held = True
                                    $ default_mouse = "blood"
                                    play audio "audio/one_shot/knife_pickup.flac"
                                    jump adversary_end


                    "{i}• The Princess Can't Die.{/i}":
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• I'm not going to say The Princess Can't Die. I'm not even going to think it.{/i}":
                        $ adversary_cant_die_thought = True
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}":
                        jump adversary_stabbed_heart_cant_die

                    "{i}• (Lie) 'The Princess Can Die.'{/i}":
                        $ adversary_cant_die_thought = True
                        $ adversary_cant_die_lie = True
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}":
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

                    "{i}• The Princess Can't Die.{/i}" if preferences.self_voicing == False:
                        jump adversary_stabbed_heart_cant_die

            "{i}• [[Attack her again.]{/i}":
                $ blade_held = True
                $ default_mouse = "blood"
                play audio "audio/one_shot/knife_pickup.flac"
                jump adversary_end

label adversary_penultimate:
    default adversary_penultimate_seen = False
    $ adversary_penultimate_seen = True
    voice "audio/voices/ch2/adversary/_fight/narrator/62.flac"
    play secondary "audio/one_shot/knife_stab.flac"
    queue secondary "audio/final/Adversary_HandThroughChest_1.flac"
    hide bg onlayer back
    hide knife onlayer back
    hide adversary onlayer back
    hide farback onlayer farback
    hide adversary onlayer front
    scene bg black
    with fade
    show bg adversary throat grab onlayer back at Position(ypos=1125)
    show adversary mutual onlayer front at Position(ypos=1125) with hpunch
    with dissolve
    n "You and the Princess attack each other once again, each of you dealing a single terrible, lethal blow.\n" id adversary_penultimate_6d726989
    voice "audio/voices/ch2/adversary/_fight/hero/30.flac"
    hero "Wait, does that mean we're...?\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/63.flac"
    $ blade_held = False
    $ default_mouse = "default"
    stop music
    hide bg onlayer back
    hide adversary onlayer front
    scene bg black
    n "Dead. Or, rather, about to be dead. As your blade pierces her sternum, the Princess buries her fist into the soft meat of your organs. You feel a few horrifically painful pops, a gush of fluid, and... it's over. It's finally over.\n"
    $ blade_held = False
    $ default_mouse = "default"
    voice "audio/voices/ch2/adversary/_fight/stubborn/25.flac"
    stubborn "No it's not. We're just getting started.\n"
    voice "audio/voices/ch2/adversary/_fight/narrator/64.flac"
    n "But it is over. Dead is dead. I know this isn't the happiest ending for you, but you saved the entire world from ruin. There are few better endings than that.\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/26.flac"
    stubborn "Well? Are you going to listen to him, or are you going to listen to me? Get. Up.\n"
    menu:
        extend ""

        "{i}• [[Get up.]{/i}":
            $ adversary_respawn_count += 1
            voice "audio/voices/ch2/adversary/_fight/narrator/65.flac"
            n "Wait. No, that can't be right.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/66.flac"
            scene farback adversary basement onlayer farback at Position(ypos=1125)
            show bg adversary basement onlayer back at Position(ypos=1125)
            show adversary d dead onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "Your eyes bolt open, and you push yourself back to your feet... alive.\n"
            voice "audio/voices/ch2/adversary/_fight/stubborn/27.flac"
            stubborn "Ha! I told you. I told you this wasn't over.\n"
            voice "audio/voices/ch2/adversary/_fight/hero/31.flac"
            hero "What about her? That blade went right through her heart...\n"
            voice "audio/voices/ch2/adversary/_fight/stubborn/28.flac"
            stubborn "What about her? If we're fine, then she's fine.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/67.flac"
            play music "audio/_music/ch2/adversary/The Adversary Heightened.flac" loop
            show adversary revive delayed onlayer back
            n "No, she's dead. She has to be— NO.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/68a.flac"
            n "Great. We're all shit out of luck, aren't we?\n"
            voice "audio/voices/ch2/adversary/_fight/stubborn/29.flac"
            stubborn "I knew it! I told you we should all believe in her! This is perfect!\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/69.flac"
            show adversary d revive stand up onlayer back
            with dissolve
            n "The Princess rises from the ground, staggering slightly, one hand wrapped around the hilt of the blade still buried in her heart.\n"
            voice "audio/voices/ch2/adversary/_fight/princess/adv_36.flac"
            sp "We don't even need to start over anymore, do we? Let's go again!\n"
            jump adversary_no_die_join


label adversary_end:
    voice "audio/voices/ch2/adversary/_fight/narrator/70.flac"
    $ blade_held = True
    $ default_mouse = "blood"
    play audio "audio/one_shot/knife_pickup.flac"
    hide bg onlayer back
    hide knife onlayer back
    hide adversary onlayer back
    hide farback onlayer farback
    scene bg adversary throat grab onlayer back at Position(ypos=1125)
    show adversary finale eyes onlayer front at Position(ypos=1125)
    with dissolve
    #n "With an unbreakable determination, you snatch the blade from the floor and stumble back to your feet. Both you and the Princess quake with adrenaline as your eyes lock across the basement floor and share a knowing look. This is it. The moment before your final clash\n."
    n "With an unbreakable determination, you snatch the blade from the floor and stumble back to your feet. Both you and the Princess quake with adrenaline as your eyes lock across the basement floor and share a knowing look.\n" id adversary_end_6e47fcfe
    if adversary_respawn_count == 0:
        if adversary_cant_die_thought:
            voice "audio/voices/ch2/adversary/_fight/hero/32.flac"
            hero "That's a lot of flowery description coming from someone who thinks he already knows how this is going to play out.\n"
            voice "audio/voices/ch2/adversary/_fight/narrator/71.flac"
            n "Oh indulge me, will you? Me knowing how this is going to play out is exactly why I'm being flowery. Let me have just this one thing, alright?\n"
            voice "audio/voices/ch2/adversary/_fight/hero/33.flac"
            hero "Alright.\n"
        voice "audio/voices/ch2/adversary/_fight/stubborn/30.flac"
        stubborn "Here it comes. The big finish.\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/72.flac"
        n "Free from hesitation, you close the distance, both you and the Princess ready to end each other.\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/73.flac"
        play secondary "audio/final/Adversary_TensionBoneBreak_2.flac"
        queue secondary "audio/final/Adversary_HandThroughChest_1.flac"
        hide bg onlayer back
        hide knife onlayer back
        hide adversary onlayer back
        hide farback onlayer farback
        hide adversary onlayer front
        show bg adversary throat grab onlayer back at Position(ypos=1125)
        show adversary neck slash onlayer back at Position(ypos=1125)
        with dissolve
        n "Your blade digs into her neck, grinding against her vertebrae as her fist connects with your body and—\n{w=5.70}{nw}"
        show screen disableclick(0.5)
        voice "audio/voices/ch2/adversary/_fight/narrator/74.flac"
        hide bg onlayer back
        hide adversary onlayer back
        scene bg black
        n "Wait, no, really?\n"
        voice "audio/voices/ch2/adversary/_fight/hero/34a.flac"
        hero "What happened? Why did everything go dark?\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/75.flac"
        n "You died. That blow was apparently lethal. How anticlimactic.\n"
        voice "audio/voices/ch2/adversary/_fight/stubborn/31.flac"
        stubborn "You don't get it, do you? We're not dead. We're stronger than this. So stop whining and get up.\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/76.flac"
        n "Saying 'get up' is not going to change the fact that you're dead. How dense are you?\n"
        voice "audio/voices/ch2/adversary/_fight/stubborn/32.flac"
        stubborn "Funny that you're calling me dense when you still haven't figured it out. We can't be dead. We're just like her. All of you need to wake up, and enter the new world.\n"
        voice "audio/voices/ch2/adversary/_fight/hero/35a.flac"
        hero "You know... maybe he has a point. If we're {i}dead{/i} dead, how are we still talking?\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/77.flac"
        n "Because you being dead is reality! Because it says {i}right here{/i} that you're—\n{w=5.10}{nw}"
        show screen disableclick(0.5)
        menu:
            extend ""

            "{i}• [[Wake up.]{/i}":
                voice "audio/voices/ch2/adversary/_fight/stubborn/33.flac"
                stubborn "Well?\n"
                voice "audio/voices/ch2/adversary/_fight/narrator/78.flac"
                n "Alive.\n"
                voice "audio/voices/ch2/adversary/_fight/stubborn/34.flac"
                stubborn "That's right.\n"
                voice "audio/voices/ch2/adversary/_fight/princess/adv_38.flac"
                scene farback adversary basement onlayer farback at Position(ypos=1125)
                show bg adversary basement onlayer back at Position(ypos=1125)
                show adversary d revive standing talk noknife onlayer back
                with dissolve
                sp "I thought I lost you there, but you've figured things out, haven't you? Good. The two of us can finally be together.\n"
                show adversary d revive standing talk noknife onlayer back
                menu:
                    extend ""

                    "{i}• [[Join your Adversary.]{/i}":
                        $ adversary_respawn_count += 1

    else:
        voice "audio/voices/ch2/adversary/_fight/narrator/79.flac"
        n "Free from hesitation, you close the distance, both you and the Princess aiming to end each other.\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/80.flac"
        hide bg onlayer back
        hide knife onlayer back
        hide adversary onlayer back
        hide farback onlayer farback
        hide adversary onlayer front
        show bg adversary throat grab onlayer back at Position(ypos=1125)
        show adversary neck slash onlayer back at Position(ypos=1125)
        play secondary "audio/final/Adversary_TensionBoneBreak_2.flac"
        queue secondary "audio/final/Adversary_HandThroughChest_1.flac"
        n "Your blade digs into her neck, grinding against her vertebrae as her fist connects with your body. The impact forces the air from your lungs, stars dancing in front of your eyes as you fail to keep your bearing.\n"
        voice "audio/voices/ch2/adversary/_fight/narrator/81.flac"
        hide bg onlayer back
        hide adversary onlayer back
        scene bg black
        n "You both collapse to the ground before either of you has a chance to survey the damage.\n"
        voice "audio/voices/ch2/adversary/_fight/stubborn/35.flac"
        stubborn "And then we get up.\n"
        menu:
            extend ""

            "{i}• [[Get up.]{/i}":
                voice "audio/voices/ch2/adversary/_fight/narrator/82.flac"
                scene farback adversary basement onlayer farback at Position(ypos=1125)
                show bg adversary basement onlayer back at Position(ypos=1125)
                show adversary d revive standing onlayer back
                with dissolve
                n "Yes. And then you get up.\n"
                voice "audio/voices/ch2/adversary/_fight/princess/adv_39.flac"
                show adversary d revive standing talk noknife onlayer back
                with dissolve
                sp "That was a good one. More!\n"
                show adversary d revive standing onlayer back
                menu:
                    extend ""

                    "{i}• [[Slay the Princess.]{/i}":
                        $ adversary_respawn_count += 1

    voice "audio/voices/ch2/adversary/_fight/narrator/83.flac"
    play audio "audio/final/Adversary_ABackAndForth_1.flac"
    stop music fadeout 30.0
    stop sound fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
    hide farback onlayer farback
    hide bg onlayer back
    hide adversary onlayer back
    show bg adversary throat grab onlayer back
    show battle adversary finale onlayer front
    with dissolve
    n "You and the Princess exchange dozens of devastating blows. Sometimes you manage to strike first, and sometimes she tears through you before you have a chance to act, but more often than not, each of you fells the other in the same moment.\n"
    # narrator's voice fades out
    voice "audio/voices/ch2/adversary/_fight/narrator/84.flac"
    hide quiet onlayer back
    show quiet creep1 onlayer front at Position(ypos=1125)
    with dissolve
    n "And then you get up and do it again, and again, and again, and again, and again, and again, and again...\n"
    voice "audio/voices/ch2/adversary/_fight/hero/36a.flac"
    hide quiet onlayer back
    show quiet creep2 onlayer front at Position(ypos=1125)
    with dissolve
    hero "We're all still here. This is all going to be okay, isn't it?\n"
    voice "audio/voices/ch2/adversary/_fight/hero/37.flac"
    hero "Isn't it...?\n"
    if loops_finished != 0:
        truth "But He doesn't answer the voice. He'll never answer. He's gone.\n"
    else:
        truth "But He doesn't answer the voice. He's gone.\n"
    voice "audio/voices/ch2/adversary/_fight/princess/adv_40.flac"
    hide bg onlayer back
    hide battle onlayer front
    show quiet creep3 onlayer front at Position(ypos=1125)
    show adversary quiet engaged talk onlayer front at Position(ypos=1125)
    with Dissolve(2.0)
    sp "What are you waiting for, I'm right here! Do you think this is...\n"
    voice "audio/voices/ch2/adversary/_fight/princess/adv_41.flac"
    show adversary quiet confused talk onlayer front
    with dissolve
    sp "W... what is this place?\n"
    voice "audio/voices/ch2/adversary/_fight/hero/38a.flac"
    hero "Did... we do this?\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/36.flac"
    stubborn "Huh. I didn't think we had it in us. But I guess that stuck-up control freak was right.\n" id adversary_end_fcc40020
    voice "audio/voices/ch2/adversary/_fight/hero/39a.flac"
    hero "It's the end of the world, isn't it? It's the end of everything.\n"
    voice "audio/voices/ch2/adversary/_fight/stubborn/37.flac"
    stubborn "Far from it. We're still here, and she's still here too.\n"
    show adversary quiet tired talk onlayer front
    with dissolve
    truth "The Princess stumbles, and her body slumps.\n"
    voice "audio/voices/ch2/adversary/_fight/princess/adv_42.flac"
    sp "I feel so... tired.\n"
    default adversary_whisk_silent = False
    if loops_finished == 0:
        menu:
            extend ""

            "{i}• ''Chin up! Isn't this what we wanted? Just you and me forever?''{/i}":
                jump adversary_whisk_join

            "{i}• ''Are you okay?''{/i}":
                jump adversary_whisk_join

            "{i}• ''We ended the world, didn't we? Everything is gone.''{/i}":
                jump adversary_whisk_join

            "{i}• ''We've been fighting for a long time. You should rest''{/i}":
                jump adversary_whisk_join

            "{i}• [[Remain silent.]{/i}":
                $ adversary_whisk_silent = True
                jump adversary_whisk_join

label adversary_whisk_join:
    # animation of the adversary being whisked away
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    hide quiet onlayer front
    show quiet creep3 onlayer back at Position(ypos=1125)
    show hands grab close1 onlayer back at Position(ypos=1125)
    show adversary quiet trance onlayer front
    with dissolve
    with Dissolve(2.0)
    $ renpy.pause(0.125)
    hide hands onlayer back
    show hands grab close2 onlayer back
    show adversary quiet trance grab onlayer front
    with Dissolve(1.5)
    $ renpy.pause(0.125)
    hide adversary onlayer front
    hide hands onlayer back
    show hands grab close3 onlayer back
    with dissolve
    $ renpy.pause(0.125)
    hide hands onlayer back
    show hands grab close4 onlayer back
    with dissolve
    $ renpy.pause(0.125)
    $ blade_held = False
    $ default_mouse = "default"
    hide hands onlayer back
    with dissolve
    hide bg onlayer back
    hide quiet onlayer back
    hide farback onlayer back
    hide farback onlayer farback
    hide bg onlayer back
    show farback quiet onlayer farback at Position(ypos=1125)
    with Dissolve(4.0)
    show mirror quiet distant onlayer back at Position(ypos=1125)
    if loops_finished != 0:
        truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
    elif adversary_whisk_silent:
        truth "You do not respond. Something has taken her away, and it's left something else in her stead.\n"
    else:
        truth "You do not have an opportunity to respond. Something has taken her away, and it's left something else in her stead.\n"
    $ princess_kept += 1
    $ princess_satisfy += 1
    jump mirror_start

    #if adversary_1_cabin_mirror_ask or adversary_1_cabin_mirror_approached:
    # voice "audio/voices/ch2/adversary/_fight/hero/40.flac"
    #    hero "It's that mirror again. Why is it here? Why now?!\n"
    #else:
    # voice "audio/voices/ch2/adversary/_fight/hero/41.flac"
    #    hero "Is that a... mirror? Why is it here? Why now?!\n"
    # voice "audio/voices/ch2/adversary/_fight/stubborn/38.flac"
    #stubborn "I don't care about the mirror, I care about her! Where did she go?\n"

    # jump to mirror
return
