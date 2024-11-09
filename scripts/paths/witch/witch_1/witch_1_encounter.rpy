label witch_1_encounter_start:
    if witch_1_forest_share_loop_insist:
        voice "audio/voices/ch2/witch/_encounter/narrator/1.flac"
        n "She's acting like she already knows you. I guess what you said back in the woods really was true.\n"
    elif witch_1_forest_share_loop:
        voice "audio/voices/ch2/witch/_encounter/narrator/2.flac"
        n "You made a comment back in the woods about having been here before, and now she's acting like the two of you already know each other.\n"
        voice "audio/voices/ch2/witch/_encounter/narrator/3.flac"
        n "Oh no. You've already been here, haven't you?\n"
    else:
        voice "audio/voices/ch2/witch/_encounter/narrator/4.flac"
        n "She's acting like the two of you already know each other.\n"
        voice "audio/voices/ch2/witch/_encounter/narrator/3.flac"
        n "Oh no. You've already been here, haven't you?\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/1.flac"
    opportunist "That's pretty sharp! How'd you figure that one out?\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/5.flac"
    n "Call it deductive reasoning.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/2.flac"
    opportunist "Well, you seem to be great at it!\n"
    if witch_1_forest_share_loop:
        voice "audio/voices/ch2/witch/_encounter/hero/1.flac"
        hero "So... you really don't remember us, do you?\n"
    else:
        voice "audio/voices/ch2/witch/_encounter/hero/2.flac"
        hero "Do you remember us, then? Do you remember last time?\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/6.flac"
    n "No, I don't. But you and the Princess clearly have a shared reality, even if I'm not a part of it. I won't waste time fighting you on something that's clearly true.\n"
    if witch_1_forest_share_loop_insist:
        voice "audio/voices/ch2/witch/_encounter/hero/3.flac"
        hero "You fought us on it back in the woods.\n"
        voice "audio/voices/ch2/witch/_encounter/narrator/7.flac"
        n "That was when the only perspectives we had were yours and mine.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/3.flac"
    opportunist "I'm just glad we could put all this behind us!\n"
    voice "audio/voices/ch2/witch/_encounter/hero/4.flac"
    hero "Is it all behind us?\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/8.flac"
    n "Just focus on the task at hand. I don't care if you've been here before, and I don't care if you think you'll go somewhere else after this. My world is on the line right now. So I'd appreciate it if you would take this seriously, and slay her.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/4.flac"
    opportunist "Let's chat her up a bit first. Maybe we can find a middle ground where everyone's happy.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/9.flac"
    n "Don't talk to her. You're just going to make things more difficult than they have to be.\n"
    voice "audio/voices/ch2/witch/_encounter/princess/1.flac"
    show witch d sass talk onlayer back
    with dissolve
    sp "Well? I seem to remember you having a tongue.\n"
    show witch d sass onlayer back

label witch_1_menu:
    default witch_free = False
    default witch_menu_count = 0
    default witch_apologize = False
    default witch_leave_together_knowledge = False
    default witch_not_happy = False
    default witch_stall = False
    default witch_cut_ask = False
    default witch_betrayal_explore = False
    default witch_blade_offer = False
    default witch_cant_apology = False
    default witch_heart_comment = False
    default witch_can_wild = True
    menu:
        extend ""

        "{i}• (Explore) ''I'm sorry about last time.''{/i}" if witch_apologize == False and witch_cant_apology == False:
            $ witch_apologize = True
            voice "audio/voices/ch2/witch/_encounter/opportunist/5.flac"
            opportunist "Oooh, smart. Let's apologize. Get us back on the right foot.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/5.flac"
            show witch d eyeroll talk onlayer back
            with dissolve
            sp "Oh, you're sorry! Isn't that nice! You're such a gracious little monster.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/6.flac"
            show witch d annoyed talk onlayer back
            with dissolve
            sp "If you're sorry, then let me out of here. Prove it.\n"
            show witch d annoyed onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''Look, I made a mistake. We all make mistakes, right? I'm sure you've made mistakes.''{/i}" if witch_apologize == False and witch_leave_together_knowledge == False:
            $ witch_leave_together_knowledge = True
            $ witch_apologize = True
            voice "audio/voices/ch2/witch/_encounter/opportunist/5.flac"
            opportunist "Oooh, smart. Let's apologize. Get us back on the right foot.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/7.flac"
            show witch d angy talk onlayer back
            with dissolve
            sp "The only mistake I ever made was thinking you would help me. And I'm not going to make the same mistake twice.\n"
            voice "audio/voices/ch2/witch/_encounter/hero/5.flac"
            show witch d angy onlayer back
            with dissolve
            hero "Well, that leaves us at a stalemate.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/8.flac"
            show witch d eyeroll talk onlayer back
            with dissolve
            sp "But unfortunately, I need you if I'm ever going to leave this place.\n"
            show witch d eyeroll onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''Don't worry, the blade isn't for you. Or, not for killing you. We've got to get you out somehow, right?''{/i}" if blade_held and witch_free == False:
            voice "audio/voices/ch2/witch/_encounter/princess/9.flac"
            show witch d confident talk onlayer back
            with dissolve
            sp "Oh, I don't need you to cut me out.\n"
            jump witch_chains_fall_join

        "{i}• (Explore) ''I get the sense that you're not happy with me.''{/i}" if witch_not_happy == False:
            $ witch_not_happy = True
            voice "audio/voices/ch2/witch/_encounter/princess/10a.flac"
            show witch d annoyed talk onlayer back
            with dissolve
            sp "Is that a joke? Do you think a joke will charm my trust back? You'll have to try harder than that.\n"
            show witch d annoyed onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''You scared me, okay? When you started gnawing your arm off, it scared me, so I stabbed you. Things got out of hand.''{/i}" if witch_betrayal_mutual and witch_stall == False and witch_apologize == False:
            $ witch_stall = True
            voice "audio/voices/ch2/witch/_encounter/princess/11.flac"
            show witch d sass talk onlayer back
            with dissolve
            sp "Things did get out of hand, didn't they? But it's hard to let bygones be bygones when they led to murder.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/11a.flac"
            show witch d angy talk onlayer back
            with dissolve
            sp "And you started it.\n"
            show witch d angy onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''I'm unarmed. That's a gesture of good-will! So why don't we talk it out?''{/i}" if blade_held == False and witch_apologize == False and witch_stall == False:
            $ witch_stall = True
            voice "audio/voices/ch2/witch/_encounter/princess/12.flac"
            show witch d neutral talk onlayer back
            with dissolve
            sp "You came to me with empty hands last time, too, but that didn't mean you hadn't been plotting something nasty all along. What you did showed me as much.\n"
            voice "audio/voices/ch2/witch/_encounter/hero/6.flac"
            show witch d neutral onlayer back
            with dissolve
            hero "But we didn't plot anything! We just made an informed decision based on the information we had at the time.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/6.flac"
            opportunist "I think you're both making perfectly valid points. Sure, we didn't plot anything, but it's easy to see how she might think we did.\n"
            jump witch_1_menu

        "{i}• (Explore) ''We both died last time. Can't bygones be bygones?''{/i}" if witch_betrayal_mutual and witch_stall == False:
            $ witch_stall = True
            voice "audio/voices/ch2/witch/_encounter/princess/13.flac"
            show witch d annoyed talk onlayer back
            with dissolve
            sp "You were the one who stabbed me in the back when I was still in chains. A dirty little thing like you doesn't get to decide when all is fair.\n"
            show witch d annoyed talk onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''I didn't do shit to you last time. You're the one who locked me away until I died.''{/i}" if loop_1_locked and witch_stall == False and witch_leave_together_knowledge == False:
            $ witch_leave_together_knowledge = True
            $ witch_stall = True
            $ witch_cant_apology = True
            show witch d annoyed onlayer back
            with dissolve
            voice "audio/voices/ch2/witch/_encounter/opportunist/7.flac"
            opportunist "That is an exceptionally good point.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/14.flac"
            show witch d hiss onlayer back
            with dissolve
            sp "And you were the conniving beast that left in search of steel to slay me. Just because I won and you lost doesn't mean I'm to blame for bad blood.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/8.flac"
            show witch d angy onlayer back
            with dissolve
            opportunist "Also a good point.\n"
            voice "audio/voices/ch2/witch/_encounter/hero/7.flac"
            hero "She can't even hear you. Why are you trying to brown-nose her?\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/9.flac"
            opportunist "I'm not brown-nosing anyone! I'm just taking a fair and balanced approach and hearing out everything that everyone has to say. If she's in the wrong, then you don't have anything to worry about!\n"
            voice "audio/voices/ch2/witch/_encounter/princess/15a.flac"
            show witch d begrudging talk onlayer back
            with dissolve
            sp "But I must confess, this place never let me out into the world. While you were gasping your last down below, I was trying to claw and bash and break my way out, but I never did manage to be free. Until finally... I found myself here again. And you were gone.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/16.flac"
            show witch d wry talk onlayer back
            with dissolve
            sp "It seems that you get to come and go as you please. So you may be a bigger part of the answer to this riddle than I'd like you to be. Maybe bygones can be bygones.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/17.flac"
            show witch d sass talk onlayer back
            with dissolve
            sp "But you'll have to let me out first.\n"
            show witch d sass onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''I died last time. You didn't. If anyone here shouldn't be trusted, it's you!''{/i}" if current_mutual_death == 0 and witch_stall == False:
            $ witch_stall = True
            if witch_rescue_path:
                voice "audio/voices/ch2/witch/_encounter/princess/18.flac"
                show witch d annoyed talk onlayer back
                with dissolve
                sp "You were the one who tried to kill me when my back was turned. You were the one who started all of this! Only a poor loser twists their own failures around on the winner.\n"
            else:
                voice "audio/voices/ch2/witch/_encounter/princess/19.flac"
                show witch d annoyed talk onlayer back
                with dissolve
                sp "You were the one who went to get that knife. You were the one who started all of this! Only a poor loser twists their own failures around on the winner.\n"
            show witch d annoyed onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''Look, I know, I know. Things got messy last time. But I think there's something bigger than both of us at work. We should team up.''{/i}" if witch_leave_together_knowledge == False:
            $ witch_leave_together_knowledge = True
            voice "audio/voices/ch2/witch/_encounter/princess/20.flac"
            show witch d wry talk onlayer back
            with dissolve
            sp "I suppose you didn't come into my hovel of your own accord, did you...? All right. I suppose I could... 'team up.' I need a way out, after all, and unfortunately you're the only one I have.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/10.flac"
            show witch d wry onlayer back
            with dissolve
            opportunist "Seems to me like she's offering a mutually beneficial arrangement. We should take it!\n"
            voice "audio/voices/ch2/witch/_encounter/narrator/10.flac"
            n "Do you know what the word 'mutually' means? Because it sounds to me like she's offering an arrangement that benefits her, and her alone.\n"
            jump witch_1_menu

        "{i}• (Explore) ''So we're at an impasse. Neither of us are gonna get anywhere if we can't trust each other. Unless you want to fight. But I don't want to fight.''{/i}" if witch_apologize and witch_leave_together_knowledge == False:
            $ witch_leave_together_knowledge = True
            voice "audio/voices/ch2/witch/_encounter/princess/2.flac"
            show witch d sass talk onlayer back
            with dissolve
            sp "Just because I'll never trust you doesn't mean I won't use you to get what I want.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/3.flac"
            show witch d squint talk onlayer back
            with dissolve
            sp "The cabin lets prying little beasts like you come as you please, but it insists I stay where I am.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/4.flac"
            show witch d begrudging talk onlayer back
            with dissolve
            sp "If I'm to leave, I'm to leave with you, and you alone.\n"
            show witch d begrudging onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''I didn't bring my blade down, remember? How am I supposed to get you out of those chains?''{/i}" if witch_leave_together_knowledge and witch_cut_ask == False and blade_held == False and witch_free == False:
            label witch_chains_no_cut:
                $ witch_cut_ask = True
                voice "audio/voices/ch2/witch/_encounter/princess/21.flac"
                show witch d sass talk onlayer back
                with dissolve
                sp "Oh, I don't need you to cut me out.\n"
                jump witch_chains_fall_join

        "{i}• (Explore) ''I guess I'll cut you out of here.''{/i}" if blade_held and witch_free == False and witch_leave_together_knowledge and witch_cut_ask == False:
            jump witch_chains_no_cut

        "{i}• (Explore) ''Can't you get out of those on your own? Those chains didn't stop you last time.''{/i}" if witch_betrayal_mutual == False and witch_free == False:
            voice "audio/voices/ch2/witch/_encounter/princess/22.flac"
            show witch d wry talk onlayer back
            with dissolve
            sp "Oh, of course. They're nothing to me.\n"
            label witch_chains_fall_join:
                $ witch_free = True
                voice "audio/voices/ch2/witch/_encounter/narrator/11.flac"
                play audio "audio/one_shot/chain_1.flac"
                show witch d free anim onlayer back
                with Dissolve(0.5)
                $ renpy.pause(0.5)
                voice sustain
                show bg witch basement chain onlayer back
                show witch d free onlayer back
                with dissolve
                n "The Princess grins as the chains fall from her wrist.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/8.flac"
                hero "She could have gotten out of those the whole time! That sneaky little...\n"
                if witch_heart_comment == False:
                    $ witch_heart_comment = True
                    voice "audio/voices/ch2/witch/_encounter/opportunist/11a.flac"
                    opportunist "A woman after my own heart, really. She knows how to hold her cards close to her chest.\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/12.flac"
                n "This is why she can't just be abandoned here. If left to her own devices, she'll find a way out. Now stop her!\n"
            jump witch_1_menu

        "{i}• (Explore) ''If you could have gotten out this whole time, what do you even need me for? The cabin isn't locked.''{/i}" if witch_free and witch_leave_together_knowledge == False:
            $ witch_leave_together_knowledge = True
            voice "audio/voices/ch2/witch/_encounter/princess/23.flac"
            show witch d squint talk onlayer back
            with dissolve
            sp "The cabin lets prying little beasts like you come as you please, but it insists I stay where I am. That binding I shed is just a symbol of the crueler magic at work in this place.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/4.flac"
            show witch d eyeroll talk onlayer back
            with dissolve
            sp "If I'm to leave, I'm to leave with you, and you alone.\n"
            show witch d eyeroll onlayer back
            jump witch_1_menu

        "{i}• (Explore) ''Why do I have a nagging feeling you're going to stab me in the back if I help you out of here?''{/i}" if witch_betrayal_explore == False:
            $ witch_betrayal_explore = True
            voice "audio/voices/ch2/witch/_encounter/princess/24.flac"
            show witch d wry talk onlayer back
            with dissolve
            sp "And why would I do such a thing? Is someone's guilty conscience getting to them?\n"
            voice "audio/voices/ch2/witch/_encounter/princess/25.flac"
            show witch d confident talk onlayer back
            with dissolve
            sp "But I wouldn't worry. As much as I may hate you, letting you live is in my best interests. If you get me out of here, the only thing that will be dead and buried is the bad blood between us.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/12.flac"
            show witch d confident onlayer back
            with dissolve
            opportunist "Oh, that nagging feeling you mentioned is me, by the way. I'm actually a little anxious about a potential back-stabbing event.\n"
            voice "audio/voices/ch2/witch/_encounter/hero/9.flac"
            hero "She needs us to get out of here. We'll be fine if that's what we decide to do.\n"
            voice "audio/voices/ch2/witch/_encounter/narrator/13.flac"
            n "You won't be fine, because destruction is in her nature. If she gets out of here, that's it for the world, remember?\n"
            voice "audio/voices/ch2/witch/_encounter/hero/10.flac"
            hero "Even if that's true, that doesn't automatically mean she's gonna stab us in the back.\n"
            voice "audio/voices/ch2/witch/_encounter/narrator/14.flac"
            n "I think that depends on your definition of words like 'stab' and 'in the back.' She might not literally do that, but she could very well symbolically do the same thing.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/13.flac"
            opportunist "See? He gets it. There's nothing wrong with looking out for number one.\n"
            jump witch_1_menu

        "{i}• ''Okay. Let's leave.'' [[Leave with the Princess.]{/i}" if witch_free:
            voice "audio/voices/ch2/witch/_encounter/princess/26.flac"
            show witch d closed talk onlayer back
            with dissolve
            sp "Yes. Let's.\n"
            jump witch_1_stairs

        "{i}• ''I don't want to hurt you, but clearly there's some broken trust. Take this as a gesture of my goodwill.'' [[Give her the blade.]{/i}" if blade_held and witch_blade_offer == False:
            label witch_blade_given_join:
                default witch_2_voice = ""
                $ witch_blade_offer = True
                voice "audio/voices/ch2/witch/_encounter/narrator/15.flac"
                if witch_at_stairs:
                    show witch c incredulous onlayer front
                    with dissolve
                else:
                    show witch d sass onlayer back
                    with dissolve
                n "You — you can't be serious.\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/14.flac"
                opportunist "Now hold on, we should put this to a vote. That blade is one of our most valuable assets. We can't just give it to her! What if she uses it to kill us? I vote no.\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/16.flac"
                n "As do I.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/11.flac"
                hero "I... uh... abstain?\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/15.flac"
                opportunist "You abstain?! She's going to kill us if we give it to her!\n"
                menu:
                    extend ""

                    "{i}• This isn't a democracy. We're giving her the blade. [[Give her the blade.]{/i}":
                        #truth "NOTE, this leads to the LAST unfinished chapter in the game — it will be up in a few hours, but we wanted to make the witch testable as soon as possible.\n"
                        #truth "You can play through to this end of the witch chapter for testing purposes, but instead of starting the next chapter, it will return you to the main menu.\n"
                        #truth "If you want to preserve this run, load your previous autosave and make a manual save from it; the game autosaves at every menu so you won't lose any progress!\n"
                        #truth "Also I hope you've been enjoying our lil game!\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/17.flac"
                        n "You're going to get everyone killed. You know that, right? {i}Sigh.{/i} But of course you do.\n"
                        if witch_at_stairs:
                            stop music
                            voice "audio/voices/ch2/witch/_encounter/narrator/18.flac"
                            $ blade_held = False
                            $ default_mouse = "default"
                            play audio "audio/one_shot/knife_pickup.flac"
                            show witch ck squint onlayer front
                            with Dissolve(0.25)
                            n "You hand the blade to the Princess, who quickly snatches it from you, her eyes darting between you and the weapon with a nervous curiosity.\n"
                            voice "audio/voices/ch2/witch/_encounter/princess/27.flac"
                            play music "audio/_music/ch2/witch/The Witch II.flac" loop
                            show witch ck squint talk onlayer front
                            with dissolve
                            sp "I wouldn't have done that. Why did you?\n"
                        else:
                            stop music
                            voice "audio/voices/ch2/witch/_encounter/narrator/19.flac"
                            $ blade_held = False
                            $ default_mouse = "default"
                            play audio "audio/one_shot/knife_bounce_several.flac"
                            show witch d knife glance onlayer back
                            with dissolve
                            n "You toss the blade at the Princess' feet.\n"
                            voice "audio/voices/ch2/witch/_encounter/narrator/19a.flac"
                            play audio "audio/one_shot/knife_pickup.flac"
                            show witch d knife stare onlayer back
                            with dissolve
                            n "She eyes it with suspicion before kneeling down to pick it up.\n"
                            voice "audio/voices/ch2/witch/_encounter/princess/27.flac"
                            play music "audio/_music/ch2/witch/The Witch II.flac" loop
                            show witch d knife talk onlayer back
                            with dissolve
                            sp "I wouldn't have done that. Why did you?\n"
                            if witch_free == False:
                                $ witch_free = True
                                voice "audio/voices/ch2/witch/_encounter/narrator/20.flac"
                                play audio "audio/one_shot/chain_1.flac"
                                show witch d free knife anim onlayer back
                                with Dissolve(0.5)
                                $ renpy.pause(0.5)
                                voice sustain
                                show bg witch basement chain onlayer back
                                show witch d knife free onlayer back
                                n "You hear a clanging of metal against the dirt floor, and the chains fall from the Princess' wrist.\n"
                                voice "audio/voices/ch2/witch/_encounter/hero/8.flac"
                                hero "She could have gotten out of those the whole time! That sneaky little...\n"
                                if witch_heart_comment == False:
                                    $ witch_heart_comment = True
                                    voice "audio/voices/ch2/witch/_encounter/opportunist/16.flac"
                                    opportunist "A woman after my own heart. It's a shame we just gave her a weapon, because if I were her, I'd use it on us right now.\n"
                                else:
                                    voice "audio/voices/ch2/witch/_encounter/opportunist/17.flac"
                                    opportunist "It's a shame we just gave her a weapon, because if I were her, I'd use it on us right now.\n"
                                voice "audio/voices/ch2/witch/_encounter/hero/12.flac"
                                hero "Luckily for us, you're not her.\n"
                                voice "audio/voices/ch2/witch/_encounter/opportunist/18.flac"
                                opportunist "Oh, we sure think alike, though. I can promise you that. Whatever you say next, you'd better make it count.\n"
                            voice "audio/voices/ch2/witch/_encounter/narrator/21.flac"
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            show witch knife approach onlayer back
                            with dissolve
                            n "She creeps forward, taking one cautious step at a time, until you and she are face to face.\n"
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide witch onlayer back
                            show witch ck neutral onlayer front at Position(ypos=1125)
                            with Dissolve(0.5)
                        $ gallery_witch.unlock_item(3)
                        $ renpy.save_persistent()
                        voice "audio/voices/ch2/witch/_encounter/princess/28.flac"
                        show witch ck neutral talk onlayer front
                        with dissolve
                        sp "What do you think happens now?\n"
                        show witch ck neutral onlayer front
                        with dissolve
                        menu:
                            extend ""

                            "{i}• ''That's up to you. It's why I gave you the blade. I chose last time, and I regret it. So now it's your time to choose.''{/i}":
                                $ witch_2_voice = "cheated"
                                jump witch_knife_trick

                            "{i}• ''We're both scared and we're both hurting. If one of us doesn't make a change, we'll probably kill each other forever. Do you want that? I don't. We can be better than this.''{/i}":
                                $ witch_2_voice = "smitten"
                                label witch_knife_trick:
                                    voice "audio/voices/ch2/witch/_encounter/narrator/22.flac"
                                    show witch ck eyedart onlayer front
                                    with dissolve
                                    n "Her shoulders tense and her eyes dart away.\n"
                                    voice "audio/voices/ch2/witch/_encounter/princess/29.flac"
                                    show witch ck squint talk onlayer front
                                    with dissolve
                                    sp "This is another trick. You're trying to sow doubt. But it's not going to work on me!\n"
                                    #voice "audio/voices/ch2/witch/_encounter/narrator/23.flac"
                                    #n "The Princess grits her teeth, and her cunning gaze once again meets yours.\n"

                            "{i}• ''You're beautiful. I want to {b}actually{/b} save you, and this feels like the only way to do it.''{/i}":
                                $ witch_2_voice = "smitten"
                                voice "audio/voices/ch2/witch/_encounter/narrator/24.flac"
                                show witch ck eyedart blush onlayer front
                                with dissolve
                                n "She pulls back, clearly caught off-guard by whatever nonsense you just said to her.\n"
                                voice "audio/voices/ch2/witch/_encounter/hero/13.flac"
                                hero "I thought it was nice.\n"
                                voice "audio/voices/ch2/witch/_encounter/opportunist/19.flac"
                                opportunist "Whether it's nice depends on if we meant it. We didn't mean it... did we?\n"
                                voice "audio/voices/ch2/witch/_encounter/narrator/25.flac"
                                n "If you were lying, we'd all know. And unfortunately, you weren't lying.\n"
                                voice "audio/voices/ch2/witch/_encounter/princess/30.flac"
                                show witch ck tsundere talk onlayer front
                                with dissolve
                                sp "What?! What do you mean by that? What kind of game are you playing?!\n"
                                voice "audio/voices/ch2/witch/_encounter/narrator/26.flac"
                                show witch ck tense onlayer front
                                with dissolve
                                n "The look of surprise that momentarily softened her features vanishes as she steels her nerves.\n"

                            "{i}• ''If you're like someone I know, you're probably going to kill me.''{/i}":
                                $ witch_2_voice = "cheated"
                                voice "audio/voices/ch2/witch/_encounter/opportunist/20.flac"
                                opportunist "Oh hey, that someone is me! And yes, you're right, that is exactly what I would do.\n"
                                voice "audio/voices/ch2/witch/_encounter/narrator/22.flac"
                                show witch ck eyedart onlayer front
                                with dissolve
                                n "Her shoulders tense and her eyes dart away.\n"
                                voice "audio/voices/ch2/witch/_encounter/princess/31.flac"
                                show witch ck eyedart talk onlayer front
                                with dissolve
                                sp "You know me too well.\n"
                                voice "audio/voices/ch2/witch/_encounter/narrator/23.flac"
                                show witch ck squint onlayer front
                                with dissolve
                                n "The Princess grits her teeth, and her cunning gaze once again meets yours.\n"

                            "{i}• [[Remain silent.]{/i}":
                                $ witch_2_voice = "cheated"
                                voice "audio/voices/ch2/witch/_encounter/narrator/29.flac"
                                show witch ck embarrassed onlayer front
                                with dissolve
                                n "You and the Princess share a knowing look.\n"

                        voice "audio/voices/ch2/witch/_encounter/narrator/30.flac"
                        play audio "audio/final/Tower_KnifeBlow_1.flac"
                        show witch ck stab onlayer front
                        with dissolve
                        n "And then she buries the blade in your heart.\n"
                        voice "audio/voices/ch2/witch/_encounter/hero/14.flac"
                        hero "What?! No. No, come on that's not right!\n"
                        voice "audio/voices/ch2/witch/_encounter/opportunist/21.flac"
                        opportunist "I told you. I {i}told{/i} you this is what she was going to do.\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/31.flac"
                        play audio "audio/one_shot/collapse.flac"
                        hide bg onlayer back
                        hide witch onlayer front
                        scene bg black
                        $ renpy.pause(0.5)
                        voice sustain
                        show bg witch stabbed onlayer back at swayblur, Position(ypos=1125)
                        show witch loom glee onlayer front at swayblur, Position(ypos=1125)
                        with Dissolve(1.0)
                        n "Glee dances across her face as you fall to the ground.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/32.flac"
                        hide bg onlayer back
                        hide witch onlayer front
                        show bg witch stabbed onlayer back at Position(ypos=1125)
                        show witch loom glee talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        sp "Hahaha! I did it! I got you! You... you...\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/32.flac"
                        show witch loom tremble onlayer front
                        with dissolve
                        n "The Princess seems to tremble, her smile fading quickly, replaced with concern. Her nervous eyes brim with tears.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/33.flac"
                        show witch loom tremble talk onlayer front
                        with dissolve
                        sp "Why? Why did you let me do this?!\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/33.flac"
                        stop music fadeout 3.0
                        stop sound fadeout 3.0
                        stop secondary fadeout 3.0
                        show witch loom tremble onlayer front
                        with dissolve
                        n "But you don't have the strength to respond. Nor do you have the time.\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/34.flac"
                        hide bg onlayer back
                        hide witch onlayer front
                        with fade
                        $ blade_held = False
                        $ default_mouse = "default"
                        n "Everything goes dark, and you die.\n"
                        $ achievement.grant("ACH_WITCH_SACRIFICE")
                        #truth "NOTE. THE NEXT CHAPTER IS CURRENTLY UNAVAILABLE. WE'RE WORKING ON FINISHING IT AS SOON AS POSSIBLE, THANKS FOR BEARING WITH US! It's a good one :)\n"
                        #truth "Until we implement it, your next click'll shunt you back to the main menu.\n"
                        #return
                        jump witch_2_start
                        # end

                    "{i}• Haha. Yeah nevermind that was such a silly idea. I'm not going to give her the blade. She clearly hates us. [[Don't do it!]{/i}":
                        voice "audio/voices/ch2/witch/_encounter/narrator/35.flac"
                        n "Good.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/34.flac"
                        if witch_at_stairs:
                            show witch c wry talk onlayer front
                        else:
                            show witch d wry talk onlayer back
                        with dissolve
                        sp "Oh? Have you decided to rescind your 'gesture'? I wouldn't trust me with it, either.\n"
                        if witch_at_stairs:
                            show witch c wry onlayer front
                        else:
                            show witch d wry onlayer back
                        with dissolve
                        if witch_at_stairs:
                            jump witch_1_stairs_menu
                        else:
                            jump witch_1_menu

        "{i}• ''I don't trust you. Not enough to free you, and definitely not enough to get close to you. I'm leaving. Bye.'' [[Leave her in the basement.]{/i}" if witch_can_wild:
            if wild_encountered:
                $ witch_can_wild = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                #voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                #hero "Wait... what?!\n"
                jump witch_1_menu
            voice "audio/voices/ch2/witch/_encounter/opportunist/22.flac"
            opportunist "Very pragmatic. That is why you're in charge.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/35.flac"
            show witch d hiss onlayer back
            with dissolve
            sp "Abandoning me, are you? Fine then, run! Tuck your tail between your legs and scamper away!\n"
            voice "audio/voices/ch2/witch/_encounter/princess/36.flac"
            sp "You might be able to escape me, but you can't escape from what you are and what you've done. If I don't take you, the wilds will!\n"
            voice "audio/voices/ch2/witch/_encounter/narrator/36.flac"
            play audio "audio/final/Witch_RootsMoving_1.flac"
            play tertiary "audio/one_shot/footsteps_creaky.flac"
            hide bg onlayer back
            hide witch onlayer back
            show farback witch stairs up onlayer farback at Position(ypos=1125)
            show bg witch stairs up flee onlayer back at Position(ypos=1125)
            with dissolve
            n "You turn to leave. But as you do, there's a deep, guttural groan, seemingly uttered by the walls themselves, followed by the creak of wood being stretched beyond its limits.\n"
            voice "audio/voices/ch2/witch/_encounter/narrator/37.flac"
            n "The cabin starts to get smaller.\n"
            voice "audio/voices/ch2/witch/_encounter/hero/15.flac"
            hero "What the hell is going on?\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/23.flac"
            opportunist "We're getting out of here and saving our skins. That's what's going on.\n"
            jump witch_1_flee

        "{i}• ''I'd like to be straightforward with my intentions. I didn't care for how you treated me last time, and I think you might be a danger to the world. I'm going to attack you now.'' [[Slay the Princess.]{/i}" if blade_held and witch_can_wild:
            if wild_encountered:
                $ witch_can_wild = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                #voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                #hero "Wait... what?!\n"
                jump witch_1_menu
            stop music
            voice "audio/voices/ch2/witch/_encounter/princess/37.flac"
            show witch d hiss onlayer back
            with dissolve
            sp "Do you think that being direct with your ill-will frees you from its wickedness?\n"
            voice "audio/voices/ch2/witch/_encounter/princess/38.flac"
            show witch d squint talk onlayer back
            with dissolve
            sp "Murder and betrayal are still murder and betrayal, whether you state your intentions or keep them hidden behind your back.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/24.flac"
            show witch d squint onlayer back
            with dissolve
            opportunist "See? This is why we never tell people what we're actually thinking! She's just as mad, only now she's ready for us.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/39.flac"
            show witch d wry talk onlayer back
            with dissolve
            sp "Still, better a violent fool than a plotting coward. Better for me, I mean.\n"
            jump witch_attack_join

        "{i}• [[Slay the Princess.]{/i}" if blade_held and witch_can_wild:
            if wild_encountered:
                $ witch_can_wild = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                #voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                #hero "Wait... what?!\n"
                jump witch_1_menu
            stop music
            play audio "audio/one_shot/footstep_run_medium.flac"
            if witch_menu_count == 0:
                voice "audio/voices/ch2/witch/_encounter/narrator/38.flac"
                show bg witch basement onlayer back at spectre_small_zoom, Position(ypos=1125)
                show witch d wry onlayer back at spectre_small_zoom, Position(ypos=1125)
                with dissolve
                n "Without uttering a word, you charge the Princess.\n"
            else:
                voice "audio/voices/ch2/witch/_encounter/narrator/39.flac"
                show bg witch basement onlayer back at spectre_small_zoom, Position(ypos=1125)
                show witch d wry onlayer back at spectre_small_zoom, Position(ypos=1125)
                with dissolve
                n "There's nothing more for you to say. Blade at the ready, you charge the Princess.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/25.flac"
            opportunist "So much for finding an easy way out! I can't believe you're making us work for it.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/40.flac"
            show witch d hiss onlayer back at spectre_small_zoom_instant
            with dissolve
            sp "Better a violent fool than a plotting coward. Better for me, at least.\n"
            label witch_attack_join:
                $ achievement.grant("ACH_WITCH_ATTACK")
                $ renpy.music.set_volume(1.0, channel='music2')
                play audio "audio/one_shot/footstep_run_medium.flac"
                play music "audio/_music/ch2/witch/The Witch III.flac" loop
                play music2 "audio/_music/ch2/witch/The Witch III Drum.flac" loop
                if witch_free:
                    voice "audio/voices/ch2/witch/_encounter/narrator/40.flac"
                    hide bg onlayer back
                    hide witch onlayer back
                    show bg witch attack onlayer back at Position(ypos=1125)
                    show witch attack onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                    $ renpy.pause(0.5)
                    voice sustain
                    play audio "audio/final/thewild_Movement_alt_5.flac"
                    hide bg onlayer back
                    show bg witch pocket sand onlayer farback at Position(ypos=1125)
                    show witch pocket sand onlayer back at Position(ypos=1125)
                    show player witch pocket sand onlayer front at Position(ypos=1125)
                    show overlay sand onlayer inyourface at Position(ypos=1125)
                    with Dissolve(0.5)
                    n "As you close the distance, readying your strike, she throws a fistful of dirt into your eyes.\n"
                else:
                    $ witch_free = True
                    voice "audio/voices/ch2/witch/_encounter/narrator/41.flac"
                    play tertiary "audio/one_shot/chain_1.flac"
                    hide bg onlayer back
                    hide witch onlayer back
                    show bg witch attack onlayer back at Position(ypos=1125)
                    show witch attack free onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                    n "As you close the distance, readying your strike, the Princess' chain falls from her wrist.\n"
                    voice "audio/voices/ch2/witch/_encounter/narrator/41a.flac"
                    play audio "audio/final/thewild_Movement_alt_5.flac"
                    hide bg onlayer back
                    show bg witch pocket sand onlayer farback at Position(ypos=1125)
                    show witch pocket sand onlayer back at Position(ypos=1125)
                    show player witch pocket sand onlayer front at Position(ypos=1125)
                    show overlay sand onlayer inyourface at Position(ypos=1125)
                    with Dissolve(0.5)
                    n "She takes advantage of your split second of surprise, and throws a fistful of dirt into your eyes.\n"
                    voice "audio/voices/ch2/witch/_encounter/hero/8.flac"
                    hero "She could have gotten out of those the whole time! That sneaky little...\n"
                    if witch_heart_comment == False:
                        $ witch_heart_comment = True
                        voice "audio/voices/ch2/witch/_encounter/opportunist/26.flac"
                        opportunist "A woman after my own heart, really. It's a shame we're playing opposite teams.\n"
                    voice "audio/voices/ch2/witch/_encounter/narrator/42.flac"
                    n "This is why you couldn't just abandon her here. Left to her own devices, she would always find her way out. Now stop her!\n"
                voice "audio/voices/ch2/witch/_encounter/princess/41.flac"
                show witch pocket sand talk onlayer back at Position(ypos=1125)
                with dissolve
                sp "You must have known I would be ready for you. Deep in your heart, you know the same things about me I know about you. We're both so very awful.\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/43.flac"
                play audio "audio/one_shot/collapse.flac"
                hide bg onlayer farback
                hide witch onlayer back
                hide player onlayer front
                hide overlay onlayer inyourface
                scene bg black
                $ renpy.pause(0.25)
                voice sustain
                show bg witch attack 2 onlayer back at Position(ypos=1125)
                show witch attack 2 onlayer front at Position(ypos=1125)
                with fade
                n "As you brush the silt from your eyes, the Princess tackles you, flattening you against the dirt floor.\n"
                voice "audio/voices/ch2/witch/_encounter/princess/42.flac"
                show witch attack 2 talk onlayer front
                with dissolve
                sp "We were always going to kill each other here, weren't we? I can't trust you and you can't trust me and those doubts spin and spin and spin into HATE.\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/44.flac"
                play audio "audio/final/Witch_ClawsEyesRip_1.flac"
                show witch attack bite onlayer front
                with dissolve
                n "She buries her teeth deep into your chest, tearing at—\n{w=3.34}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch2/witch/_encounter/opportunist/27a.flac"
                opportunist "Great! She's distracted. Stab her in the back.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/16.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                show witch attack backstab onlayer front
                with dissolve
                hero "... In for a penny, right? Why not.\n"
                $ default_mouse = "blood"
                voice "audio/voices/ch2/witch/_encounter/narrator/45.flac"
                play audio "audio/final/Tower_KnifeBlow_1.flac"
                show witch attack backstab stab onlayer front
                with dissolve
                n "As the Princess rips meat from bone, you plunge your weapon into her unprotected back.\n"
                #voice "audio/voices/ch2/witch/_encounter/narrator/46.flac"
                #n "She recoils from you, howling in pain.\n"
                voice "audio/voices/ch2/witch/_encounter/princess/43.flac"
                show witch attack backstab howl onlayer front
                with dissolve
                sp "HA! YOU BASTARD! Even face-to-face you find a way to stab me in the back. I know you and you're hideous! Absolutely wretched! Just like me!\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/28.flac"
                opportunist "Maybe we are the same. So what! Throw her off us! Kick her in the shins!\n"
                voice "audio/voices/ch2/witch/_encounter/hero/17.flac"
                hero "We don't have to fight so dirty.\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/29.flac"
                opportunist "Of course we do. Fighting clean won't help us win. It takes a wretch to know a wretch, and we're all at the bottom of the barrel here. There's no point in pretending otherwise!\n"
                voice "audio/voices/ch2/witch/_encounter/hero/18a.flac"
                hero "Are we? At the bottom of the barrel?\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/30.flac"
                opportunist "We've got dirt in our eyes and a chunk of us chewed out. If that's not the bottom of the barrel, what is?\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/47.flac"
                n "No arguments here. You're doing great, keep playing dirty if that's what it takes.\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/31.flac"
                opportunist "But if we win, we won't be at the bottom anymore. We'll have climbed a little higher. And once we start climbing, well, who knows where we'll stop!\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/48.flac"
                n "You'll stop right here if you keep daydreaming, don't let yourself get distracted thinking about what comes after.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/19.flac"
                hero "None of us ever said we stopped fighting!\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/49.flac"
                play audio "audio/final/Witch_ClawsRipWet_3.flac"
                hide bg onlayer back
                hide witch onlayer front
                show bg witch attack 2 onlayer farback at Position(ypos=1125)
                show panel2 witch brawl onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "And what a low and vicious fight it is. Eyes gouged, skin scratched bloody, hair ripped and nails broken. Every rule there ever was in the book of honorable combat, both you and the Princess have broken a dozen times over.\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/32.flac"
                opportunist "That's nice and all, but are we winning?\n"
                play audio "audio/final/Witch_ClawsEyesRip_3.flac"
                voice "audio/voices/ch2/witch/_encounter/narrator/50a.flac"
                show panel1 witch brawl onlayer front at Position(ypos=1125)
                with Dissolve(1.0)
                n "Nobody's winning. I thought playing dirty was supposed to give you the upper hand, but I suppose that doesn't work if you both sink to the same lows... still, at least you're not losing.\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/51.flac"
                play audio "audio/final/Witch_ClawsRipWet_1.flac"
                play tertiary "audio/final/Witch_RootsMoving_1.flac"
                show panel3 witch brawl onlayer inyourface at Position(ypos=1125)
                with Dissolve(1.0)
                n "The Princess cackles maniacally as the fracas continues. But behind her cackle, you hear the low groan of warping wood.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/20.flac"
                hero "Wait... what's going on?\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/33.flac"
                opportunist "We're establishing a newer, better pecking order.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/21.flac"
                hero "No, the groaning thing. Why is the wood making noise?\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/34.flac"
                opportunist "Who cares about the groan? It's just a sound. Things make sounds all the time.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/22.flac"
                hero "I care about the groan! Doesn't that mean something bad is happening?\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/52.flac"
                n "Oh yes, well, I'm afraid that's the sound of the basement getting smaller.\n"
                $ gallery_witch.unlock_item(4)
                $ gallery_witch.unlock_item(5)
                $ gallery_witch.unlock_item(6)
                $ gallery_witch.unlock_item(7)
                $ renpy.save_persistent()
                voice "audio/voices/ch2/witch/_encounter/princess/44.flac"
                hide bg onlayer farback
                hide panel3 onlayer inyourface
                hide panel1 onlayer front
                hide panel2 onlayer back
                show bg witch attack 2 onlayer back at Position(ypos=1125)
                show witch brawl roots start onlayer front at Position(ypos=1125)
                with Dissolve(1.0)
                sp "Do you hear that, you pathetic wretch? Those are the roots of the wild, and they're coming to choke the breath from your lungs and squeeze the life out of you!\n"
                voice "audio/voices/ch2/witch/_encounter/hero/23.flac"
                hero "Excuse me, what?!\n"
                $ renpy.music.set_volume(0.0, 1.0, channel='music2')
                voice "audio/voices/ch2/witch/_encounter/narrator/53.flac"
                play audio "audio/final/Nightmare_MaleBreath_1.flac"
                play tertiary "audio/one_shot/collapse.flac"
                queue tertiary "audio/final/Witch_RootsMoving_2.flac"
                hide bg onlayer back
                show roots brawl 1 onlayer back at Position(ypos=1125)
                show witch b breathless onlayer front at Position(ypos=1125)
                with Dissolve(1.0)
                n "You and the Princess disengage for a brief moment, just long enough to get your bearings. Behind you, the basement door has been sealed over, thick roots barring your only exit from the dirt pit. And slowly, but very perceptibly, the roots are closing in on you both.\n"
                voice "audio/voices/ch2/witch/_encounter/princess/45.flac"
                show witch b breathless talk onlayer front
                with dissolve
                sp "That's right. They're coming for you, and they won't stop until there's nothing left down here but them.\n"
                label witch_fight_menu:
                    if witch_fight_menu_count == 1:
                        voice "audio/voices/ch2/witch/_encounter/narrator/54.flac"
                        play audio "audio/final/Witch_RootsMoving_1.flac"
                        show roots brawl 2 onlayer back
                        with Dissolve(1.5)
                        n "The roots grow ever closer.\n"
                        voice "audio/voices/ch2/witch/_encounter/hero/24.flac"
                        hero "We know. We can see them.\n"
                    elif witch_fight_menu_count == 2:
                        voice "audio/voices/ch2/witch/_encounter/narrator/55.flac"
                        play audio "audio/final/Witch_TreeWrap_1.flac"
                        show roots brawl 3 onlayer back
                        with Dissolve(1.5)
                        n "You feel something against your back. A thick root pushing its way into the cavern, an unstoppable, unyielding wall of bark. You're running out of time.\n"
                        voice "audio/voices/ch2/witch/_encounter/hero/25.flac"
                        hero "Shit, what do we do what do we do?\n"
                        voice "audio/voices/ch2/witch/_encounter/opportunist/35.flac"
                        opportunist "We should probably get back to stabbing. The only way out of this is through her, right?\n"
                    elif witch_fight_menu_count >= 3:
                        $ wild_bonus_voice = "cheated"
                        jump witch_basement_constriction_join
                    $ witch_fight_menu_count += 1
                    default witch_fight_menu_count = 0
                    default witch_fight_mutual_crush_comment = False
                    default witch_fight_mutual_crush_comment_follow = False
                    default witch_fight_menu_sucks_comment = False
                    default witch_fight_menu_animals_comment = False
                    default witch_fight_menu_sorry = False
                    menu:
                        extend ""

                        "{i}• (Explore) ''What about you? They'll crush you just as easily as they'll crush me.''{/i}" if witch_fight_mutual_crush_comment == False:
                            $ witch_fight_mutual_crush_comment = True
                            voice "audio/voices/ch2/witch/_encounter/princess/46.flac"
                            show witch b insane talk onlayer front
                            with dissolve
                            sp "As long as you suffer while you die, I'll gladly suffer with you. Especially if I get to see it happen.\n"
                            voice "audio/voices/ch2/witch/_encounter/opportunist/36.flac"
                            show witch b insane onlayer front
                            with dissolve
                            opportunist "This doesn't help anyone! I can't believe she'd kill us both just to spite me.\n"
                            voice "audio/voices/ch2/witch/_encounter/narrator/56.flac"
                            n "See? This is exactly why you've been tasked to slay her. She's an antisocial monster who'll gladly burn the whole world for her satisfaction.\n"
                            jump witch_fight_menu

                        "{i}• (Explore) ''Make them stop! You can make them stop, right?''{/i}" if witch_fight_mutual_crush_comment_follow == False:
                            $ witch_fight_mutual_crush_comment_follow = True
                            if witch_fight_mutual_crush_comment == False:
                                $ witch_fight_mutual_crush_comment = True
                                voice "audio/voices/ch2/witch/_encounter/princess/47.flac"
                                show witch b smug talk onlayer front
                                with dissolve
                                sp "I could. But who says I want to? As long as you suffer while you die, I'll gladly suffer with you. Especially if I get to see it happen.\n"
                                voice "audio/voices/ch2/witch/_encounter/opportunist/36.flac"
                                show witch b smug onlayer front
                                with dissolve
                                opportunist "This doesn't help anyone! I can't believe she'd kill us both just to spite me.\n"
                                voice "audio/voices/ch2/witch/_encounter/narrator/56.flac"
                                n "See? This is exactly why you've been tasked to slay her. She's an antisocial monster who'll gladly burn the whole world for her satisfaction.\n"
                            else:
                                voice "audio/voices/ch2/witch/_encounter/princess/48.flac"
                                show witch b smug talk onlayer front
                                with dissolve
                                sp "I could, but as I've already made so so clear, I. Don't. Want to.\n"
                                show witch b smug onlayer front
                                with dissolve
                            jump witch_fight_menu

                        "{i}• (Explore) ''Why, though? Why are you doing this?''{/i}" if witch_fight_mutual_crush_comment and witch_fight_mutual_crush_comment_follow == False:
                            $ witch_fight_mutual_crush_comment_follow = True
                            voice "audio/voices/ch2/witch/_encounter/princess/49.flac"
                            show witch b breathless talk onlayer front
                            with dissolve
                            sp "Because it's in my nature. Just like you coming down here to kill me is in yours. It's who I am.\n"
                            voice "audio/voices/ch2/witch/_encounter/opportunist/37.flac"
                            show witch b breathless onlayer front
                            with dissolve
                            opportunist "That is extremely not us. We're just doing what we're told, and making the best out of a difficult situation.\n"
                            voice "audio/voices/ch2/witch/_encounter/narrator/58.flac"
                            n "Exactly. You're in the right here. Now focus up, and win.\n"
                            jump witch_fight_menu

                        "{i}• (Explore) ''Come on! They're pressing in on me. They're pressing in on you! This sucks!''{/i}" if witch_fight_menu_count > 1 and witch_fight_menu_sucks_comment == False:
                            $ witch_fight_menu_sucks_comment = True
                            voice "audio/voices/ch2/witch/_encounter/princess/50.flac"
                            show witch b explain talk onlayer front
                            with dissolve
                            sp "Awww what's the matter? You're scared of a few thorny roots digging into your neck? Scared of suffocating in this dark, dark place as I watch you die? Good!\n"
                            voice "audio/voices/ch2/witch/_encounter/opportunist/38.flac"
                            show witch b smug onlayer front
                            with dissolve
                            opportunist "That one made me feel bad inside. I don't want people to think we're scared. Nobody likes someone who's scared of things.\n"
                            voice "audio/voices/ch2/witch/_encounter/hero/26.flac"
                            hero "I for one think this is a perfectly reasonable situation to be scared in. This is starting to hurt! I don't want to die like this!\n"
                            jump witch_fight_menu

                        "{i}• (Explore) ''We're not animals! We're people. We can work this out. We can make things better.''{/i}" if witch_fight_menu_animals_comment == False:
                            $ witch_fight_menu_animals_comment = True
                            voice "audio/voices/ch2/witch/_encounter/princess/51.flac"
                            show witch b insane talk onlayer front
                            with dissolve
                            sp "But we are animals! We are! You're nothing but fear and instinct and that's all I am too! We don't have to make things better! We can't make things better!\n"
                            voice "audio/voices/ch2/witch/_encounter/princess/52.flac"
                            show witch b breathless talk onlayer front
                            with dissolve
                            sp "We're just meant to chase each other in the dark until one of us catches the other. And then we'll do it again, and again, and again!\n"
                            voice "audio/voices/ch2/witch/_encounter/opportunist/39.flac"
                            show witch b breathless onlayer front
                            with dissolve
                            opportunist "You know, I don't think she's actually a go-getter at all. I think we may have misread the situation.\n"
                            voice "audio/voices/ch2/witch/_encounter/hero/27.flac"
                            hero "I think you misread the situation.\n"
                            voice "audio/voices/ch2/witch/_encounter/opportunist/40.flac"
                            opportunist "Everyone makes mistakes. The important thing is that we can move on from them together, with no hard feelings.\n"
                            voice "audio/voices/ch2/witch/_encounter/narrator/59.flac"
                            n "{i}Sigh.{/i} Just focus up. You aren't dead yet. You can figure this out.\n"
                            jump witch_fight_menu

                        "{i}• (Explore) ''I take it all back! I can help you get out of here! You and I can work together! We can be friends. I'm sorry!''{/i}" if witch_fight_menu_sorry == False:
                            $ witch_fight_menu_sorry = True
                            voice "audio/voices/ch2/witch/_encounter/princess/53.flac"
                            show witch b smug talk onlayer front
                            with dissolve
                            sp "Too little, too late! We're both going to die a splintery and miserable death! And you're going to hate it just as much as you hate me and I hate you!\n"
                            show witch b smug onlayer front
                            with dissolve
                            jump witch_fight_menu

                        "{i}• [[Give up, and await your death.]{/i}":
                            $ gallery_witch.unlock_item(16)
                            $ wild_bonus_voice = "cheated"
                            voice "audio/voices/ch2/witch/_encounter/narrator/60.flac"
                            $ blade_held = False
                            $ default_mouse = "default"
                            play audio "audio/one_shot/knife_bounce_several.flac"
                            play audio "audio/final/Witch_TreeWrap_1.flac"
                            show roots brawl 3 onlayer back
                            with Dissolve(1.5)
                            n "The blade tumbles uselessly from your palm as the roots continue to expand into the cramped basement.\n"
                            voice "audio/voices/ch2/witch/_encounter/opportunist/41.flac"
                            opportunist "{i}Sigh{/i}. We're never going to make something of ourselves with that attitude.\n"
                            voice "audio/voices/ch2/witch/_encounter/narrator/61.flac"
                            show witch b relax onlayer front
                            with dissolve
                            n "The princess finally puts down her guard, arms falling to her sides, a look of smug satisfaction screwed on her face despite her torn and bloodied skin and the insistent roots pressing in from all directions.\n"
                            voice "audio/voices/ch2/witch/_encounter/hero/28.flac"
                            hero "At least she isn't going to 'make something of herself' either.\n"
                            label witch_basement_constriction_join:
                                stop music2
                                voice "audio/voices/ch2/witch/_encounter/narrator/70.flac"
                                play audio "audio/final/Witch_TreeWrap_1.flac"
                                hide roots onlayer back
                                hide bg onlayer back
                                hide witch onlayer front
                                hide player onlayer inyourface
                                show witch brawl roots join onlayer back at Position(ypos=1125)
                                show fore witch brawl roots join onlayer front at Position(ypos=1125)
                                with Dissolve(2.0)
                                n "The roots twist around you both, binding your limbs and rendering you helpless. As your fates close in, all you can do is watch her, and all she can do is watch you.\n"
                                voice "audio/voices/ch2/witch/_encounter/narrator/64.flac"
                                play audio "audio/final/Witch_TreeWrap_2.flac"
                                n "At first it's almost gentle, the two of you lifted delicately off the ground. But the cradle of the growing roots soon gives way to tightness, and that tightness gives way to bulging pressure as they begin to constrict.\n"
                                voice "audio/voices/ch2/witch/_encounter/narrator/65.flac"
                                play audio "audio/final/_witch_squish_1.flac"
                                show witch brawl roots squish onlayer back
                                show fore witch brawl roots squish onlayer front
                                with Dissolve(2.0)
                                n "The sound of creaking wood is drowned out by the snaps and pops of your bones, pain flooding your senses as you feel your skin deform, being shaped unnaturally by the living basement.\n"
                                voice "audio/voices/ch2/witch/_encounter/narrator/66a.flac"
                                n "Tears well up in the Princess' eyes, her own bones splintering and flesh swelling with trapped blood, but still she smiles through all of it.\n"
                                voice "audio/voices/ch2/witch/_encounter/princess/54.flac"
                                show witch brawl roots squish talk onlayer back
                                with dissolve
                                sp "I can't wait to do this again, you wretched little thing. I hate you... but I wouldn't have it any other way.\n"
                                play audio "audio/final/_witch_squish_2.flac"
                                voice "audio/voices/ch2/witch/_encounter/narrator/67a.flac"
                                show witch brawl roots last onlayer back
                                show fore witch brawl roots last onlayer front
                                with Dissolve(1.5)
                                n "The pressure is unbearable. You can't breathe, your vision swimming with red, your head pounding as everything tightens.\n"
                                $ gallery_witch.unlock_item(8)
                                $ gallery_witch.unlock_item(9)
                                $ renpy.save_persistent()
                                play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
                                stop music
                                stop music2
                                stop sound
                                stop secondary
                                stop tertiary
                                voice "audio/voices/ch2/witch/_encounter/narrator/68.flac"
                                hide fore onlayer front
                                show witch brawl roots dead onlayer back
                                $ renpy.pause(1.0)
                                voice sustain
                                hide witch onlayer back
                                scene bg black
                                n "And then you pop. Everything goes dark, and you die.\n"
                                $ wild_source = "witch"
                                jump wild_start
                                    # END

                        "{i}• [[Go out fighting.]{/i}":
                            $ wild_bonus_voice = "stubborn"
                            voice "audio/voices/ch2/witch/_encounter/narrator/69.flac"
                            $ renpy.music.set_volume(1.0, 1.0, channel='music2')
                            play audio "audio/final/_witch_brawl_final.flac"
                            hide bg onlayer back
                            hide witch onlayer front
                            show bg witch final fight roots onlayer back at Position(ypos=1125)
                            show witch final fight roots her onlayer front at Position(ypos=1125)
                            show player witch final fight roots onlayer inyourface at Position(ypos=1125)
                            with Dissolve(0.5)
                            n "You attack the Princess once more, and once more the two of you fall into a vicious brawl. The basement continues to shrink as you fight, but neither of you pay it any more mind. Not until it's too late.\n"
                            jump witch_basement_constriction_join


label witch_1_stairs:
    stop music
    default witch_at_stairs = False
    $ witch_at_stairs = True
    voice "audio/voices/ch2/witch/_encounter/narrator/21.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    show witch approach onlayer back
    with Dissolve(1.0)
    n "She creeps forward, taking one cautious step at a time, until you and she are face to face.\n"
    play music "audio/_music/ch2/witch/The Witch II.flac" loop
    voice "audio/voices/ch2/witch/_encounter/narrator/72.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    hide witch onlayer back
    show witch c neutral onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    n "She never breaks eye-contact, even as the two of you find yourselves face to face.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/73.flac"
    show witch c squint onlayer front
    with dissolve
    n "She's silent for a long moment, as if testing to see what you'll do now that she's within arm's reach.\n"
    voice "audio/voices/ch2/witch/_encounter/princess/55.flac"
    show witch c offer talk onlayer front
    with dissolve
    sp "After you, darling. You're the one it lets come and go. It's best if I follow.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/42.flac"
    show witch c offer onlayer front
    with dissolve
    opportunist "Oh no, we can't have that. If anyone is going to turn their back on anyone else, she's going to turn her back on us.\n"
    voice "audio/voices/ch2/witch/_encounter/hero/29.flac"
    hero "It shouldn't matter who leads and who follows. We're working together here.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/43.flac"
    opportunist "Well, if it doesn't matter, then she can go first. We may be in this together, but that doesn't mean we have to trust her.\n"
    if blade_held:
        voice "audio/voices/ch2/witch/_encounter/hero/30.flac"
        hero "We're armed and she's not. What's she going to do, bite us when we're not looking?\n"
    else:
        voice "audio/voices/ch2/witch/_encounter/hero/31.flac"
        hero "Somebody has to go first, and it might as well be us. We're the ones who broke her trust last time.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/74.flac"
    n "You're talking a lot about trusting someone who, by her very definition, cannot be trusted. I don't know how many more warnings I have to dole out, but if you help her out of here, you're going to regret it.\n"
    label witch_1_stairs_menu:
        default witch_stairs_explore = False
        default witch_stairs_implore = False
        menu:
            extend ""

            "{i}• (Explore) ''You first.''{/i}" if witch_stairs_explore == False and witch_stairs_implore == False:
                $ witch_stairs_explore = True
                voice "audio/voices/ch2/witch/_encounter/princess/56.flac"
                show witch c wry talk onlayer front
                with dissolve
                sp "And turn my back on you? Do you think me a fool? Your tricks are one of the only things I've known. And I've learned better by now.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/32.flac"
                show witch c squint onlayer front
                with dissolve
                hero "Just go first.\n"
                jump witch_1_stairs_menu

            "{i}• (Explore) ''Clearly, there's some broken trust here. What if I gave you this?'' [[Give her the blade.]{/i}" if blade_held and witch_blade_offer == False and witch_stairs_implore == False:
                $ witch_blade_offer = True
                jump witch_blade_given_join

            "{i}• (Explore) ''You're the one who said you can't leave here without me, which means I hold all the cards. Either you go first, or we stay here. Up to you!''{/i}" if witch_stairs_implore == False and witch_stairs_explore:
                $ witch_stairs_implore = True
                voice "audio/voices/ch2/witch/_encounter/narrator/75.flac"
                play audio "audio/final/witch_sniff.flac"
                show witch c sniff onlayer front
                with dissolve
                n "The Princess leans close, her nose twitching as she sniffs your neck inquisitorially.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/33.flac"
                hero "What is she doing?\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/44a.flac"
                opportunist "I think she's trying to figure out if we're lying, so it's a good thing we didn't lie!\n"
                #voice "audio/voices/ch2/witch/_encounter/narrator/76.flac"
                #n "She pulls back, gently smiling.\n"
                voice "audio/voices/ch2/witch/_encounter/princess/57.flac"
                show witch c tsundere talk onlayer front
                with dissolve
                sp "Your stink is the stink of a wretch, but not of a liar. If I have to go first, I'll go first, but I'll have you know my ears are sharp, and I've got eyes on the back of my head. They'll be watching.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/34.flac"
                show witch c neutral onlayer front
                with dissolve
                hero "Eyes on the back of her head?! Does she really?\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/45.flac"
                opportunist "Nooooo. We're fine.\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/77.flac"
                n "The Princess pointedly turns her back on you and starts up the stairs.\n"
                jump witch_1_stairs_menu


            "{i}• [[Step onto the stairs.]{/i}":
                if witch_stairs_implore:
                    jump witch_stairs_princess_first
                else:
                    $ gallery_witch.unlock_item(10)
                    $ renpy.save_persistent()
                    jump witch_stairs_player_first



label witch_stairs_princess_first:


    voice "audio/voices/ch2/witch/_encounter/narrator/78.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    hide bg onlayer back
    hide witch onlayer front
    show farback witch stairs up onlayer farback at Position(ypos=1125)
    show bg witch stairs up onlayer back at Position(ypos=1125)
    show witch stairs first onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "You follow close behind her, the two of you walking on tiptoes through the knotted roots of the basement stairs.\n"
    if blade_held:
        voice "audio/voices/ch2/witch/_encounter/opportunist/46.flac"
        opportunist "It's time boys! Stab her in the back! Do it! Do it now!\n"
        voice "audio/voices/ch2/witch/_encounter/hero/35.flac"
        hero "Wait, I thought we were helping her escape.\n"
        voice "audio/voices/ch2/witch/_encounter/opportunist/47.flac"
        opportunist "Of course we're not! You didn't buy all of that noise I was putting down, did you? I was just waiting for a moment for us to strike. She has it in for us, you know.\n"
        label witch_back_stab_menu:
            default witch_back_stab_refuse_explore = False
            menu:
                extend ""

                "{i}• (Explore) I'm not stabbing her in the back.{/i}" if witch_back_stab_refuse_explore == False:
                    $ witch_back_stab_refuse_explore = True
                    voice "audio/voices/ch2/witch/_encounter/opportunist/48.flac"
                    opportunist "You do realize that she hates us, right? If we don't make the first move now, she's going to find a way to make the first move herself.\n"
                    voice "audio/voices/ch2/witch/_encounter/hero/36.flac"
                    hero "Why would she do that? She wants to leave, which means we need to work together. She knows that! She wouldn't just act against her best interests.\n"
                    voice "audio/voices/ch2/witch/_encounter/opportunist/49.flac"
                    opportunist "I dunno. If I were her, I'd betray us. Look at me right now, suggesting betrayal! You really need to learn to put yourself in someone else's shoes.\n"
                    voice "audio/voices/ch2/witch/_encounter/narrator/79.flac"
                    n "I'm with that little weasel. You have an opportunity to save the world. You should take it.\n"
                    jump witch_back_stab_menu

                "{i}• I said I'm not stabbing her in the back. And I make the choices here.{/i}":
                    default witch_great_idea = False
                    $ witch_great_idea = True
                    voice "audio/voices/ch2/witch/_encounter/opportunist/50a.flac"
                    opportunist "And that's a great idea! See, this is why you're in charge and I'm not. You think things through. You stick to your guns. It shows real leadership, and more people should be like you.\n"
                    jump witch_leave_join

                "{i}• Wow, that's an amazing idea that I totally never saw coming, thanks for looking out for us! [[Stab her in the back.]{/i}":
                    voice "audio/voices/ch2/witch/_encounter/opportunist/51.flac"
                    opportunist "Wow! You said exactly the thing I imagined you would say as soon as you heard my brilliant plan. This whole day is a dream come true, really.\n"
                    jump witch_back_stab

                "{i}• I am not going to praise you, but I am going to [[Stab her in the back.]{/i}":
                    voice "audio/voices/ch2/witch/_encounter/opportunist/52.flac"
                    opportunist "Oh, you're no fun. But at least you get how important it is that we leave this basement at the top of the pecking order.\n"
                    jump witch_back_stab

                "{i}• Ugh. Fine. [[Stab her in the back.]{/i}":
                    voice "audio/voices/ch2/witch/_encounter/opportunist/52.flac"
                    opportunist "Oh, you're no fun. But at least you get how important it is that we leave this basement at the top of the pecking order.\n"
                    label witch_back_stab:
                        $ gallery_witch.unlock_item(11)
                        $ renpy.save_persistent()
                        $ achievement.grant("ACH_WITCH_BETRAY")
                        voice "audio/voices/ch2/witch/_encounter/narrator/80.flac"
                        play audio "audio/final/Tower_KnifeBlow_1.flac"
                        hide bg onlayer back
                        hide witch onlayer back
                        hide farback onlayer back
                        hide farback onlayer farback
                        show cg player betrays witch onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        n "You plunge the blade deep into the Princess' back, driving her to her knees amid the roots.\n"
                        voice "audio/voices/ch2/witch/_encounter/opportunist/53.flac"
                        opportunist "Would you look at that! No need to thank me, but... y'know... please, do thank me.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/58.flac"
                        show cg player betrays witch talk onlayer back
                        with Dissolve(1.0)
                        sp "Of course you'd betray me the moment I turned my back on you.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/59.flac"
                        sp "Don't think you're leaving here alive, wretch!\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/81.flac"
                        play secondary "audio/one_shot/tower_stairs_fall.flac"
                        queue secondary "audio/one_shot/tackle.flac"
                        hide cg onlayer back
                        hide farback onlayer farback
                        scene bg black
                        n "She shoves you in return, sharp teeth clamping around your ankle as the two of you tumble down the uneven stairs in a hastening flurry of violence and loathing.\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/82.flac"
                        play audio "audio/final/Nightmare_NeckCrack_1.flac"
                        scene bg witch betray basement onlayer back at swayblur, Position(ypos=1125)
                        show witch betray basement wounded onlayer back at swayblur, Position(ypos=1125)
                        show player witch betray onlayer front at swayblur, Position(ypos=1125)
                        with fade
                        n "You separate with a bone-shaking thud as you hit the basement floor. You feel something pop. The Princess lands against the far wall, gasping as she struggles to recover from the impact.\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/83.flac"
                        hide bg onlayer back
                        hide witch onlayer back
                        hide player onlayer front
                        scene bg witch betray basement onlayer back at Position(ypos=1125)
                        show witch betray basement laugh onlayer back at Position(ypos=1125)
                        show player witch betray onlayer front at Position(ypos=1125)
                        with Dissolve(1.5)
                        n "You're still in shock, trying to get ahold of yourself. She grins as you continue to remain exactly where you are, cackling derisively as she watches you realize that you won't be getting up.\n"
                        voice "audio/voices/ch2/witch/_encounter/hero/37.flac"
                        show witch betray basement smug onlayer back
                        with dissolve
                        hero "Wait. Why won't we be getting up?\n"
                        voice "audio/voices/ch2/witch/_encounter/narrator/84.flac"
                        n "I'm afraid your back is broken. One unlucky fall is all it takes, really, and you had several.\n"
                        voice "audio/voices/ch2/witch/_encounter/opportunist/54a.flac"
                        opportunist "You know what. I'll say it! That sucks! I don't like having a broken back.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/60.flac"
                        show witch betray basement smug talk onlayer back
                        with dissolve
                        spmid "Did you really think you could stab me in the back without suffering the consequences? Fool! fool! fool! You're such a ridiculous fool!\n"
                        show witch betray basement smug onlayer back
                        with dissolve
                        jump witch_betrayal_menu


    else:
        label witch_leave_join:
            voice "audio/voices/ch2/witch/_encounter/princess/61.flac"
            sp "We're almost there. You'd better not try anything. I know you're thinking it.\n"
            if blade_held == False:
                voice "audio/voices/ch2/witch/_encounter/opportunist/55.flac"
                opportunist "Us? No. Never! Just keep your eyes peeled when you get out of the basement, if you catch my drift.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/38.flac"
                hero "I don't follow.\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/56.flac"
                opportunist "Oh, you'll know when you see it.\n"
            else:
                voice "audio/voices/ch2/witch/_encounter/opportunist/57.flac"
                opportunist "Us? No. Never! I can't believe she'd even suggest that. The gall!\n"
            voice "audio/voices/ch2/witch/_encounter/narrator/85.flac"
            $ quick_menu = False
            play audio "audio/one_shot/footsteps_creaky.flac"
            hide witch onlayer back
            hide bg onlayer back
            hide farback onlayer farback
            hide farback onlayer back
            scene bg black
            with fade
            show farback witch stairs up onlayer farback at Position(ypos=1125)
            show bg witch stairs up onlayer back at Position(ypos=1125)
            scene farback witch cabin onlayer farback at flip, Position(ypos=1125)
            show bg witch cabin onlayer back at flip, Position(ypos=1125)
            show door witch1 onlayer back at flip, Position(ypos=1125)
            if blade_held == False:
                show knife witch upstairs onlayer back at Position(ypos=1125)
            show witch up smile onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "The Princess reaches the top of the stairs and crosses over the threshold, turning back to smile at you.\n"
            if blade_held == False:
                voice "audio/voices/ch2/witch/_encounter/narrator/86.flac"
                show witch up glance onlayer back at Position(ypos=1125)
                with dissolve
                n "But something catches her eye. Oh no.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/39.flac"
                hero "Oh no?\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/58a.flac"
                opportunist "It's the blade, isn't it? I was going to tell you to grab it once we got upstairs. That was the whole 'keep your eyes peeled' thing. And then you would have stabbed her in the back, and we would've been winners!\n"
                #voice "audio/voices/ch2/witch/_encounter/narrator/87.flac"
                show witch up eyes dart onlayer back at Position(ypos=1125)
                with dissolve
                $ renpy.pause(2.5)
                #n "Yes. It's the blade. The Princess takes the weapon from the table, her eyes nervously darting between you and its gleaming edge.\n"
                voice "audio/voices/ch2/witch/_encounter/princess/62.flac"
                show witch up sus talk onlayer back at Position(ypos=1125)
                with dissolve
                sp "I wonder if perhaps you were planning to bury this in my back. What an awful little scheme that would be. Too bad I got here first. And I don't even need it.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/63.flac"
            show witch up glee talk onlayer back at Position(ypos=1125)
            with dissolve
            sp "Bye-bye, you loathsome little nuisance!\n"
            $ achievement.grant("ACH_WITCH_FOOL")
            voice "audio/voices/ch2/witch/_encounter/narrator/88.flac"
            play secondary "audio/one_shot/door_close.flac"
            queue secondary "audio/one_shot/lock_click.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide knife onlayer back
            hide witch onlayer back
            hide door onlayer back
            scene bg black
            n "And then she slams the door on you. Its lock swiftly clicks into place.\n"
            scene bg witch slam onlayer back
            with fade
            if loop_1_locked:
                voice "audio/voices/ch2/witch/_encounter/hero/40.flac"
                hero "No! Not again!\n"
            if blade_held == False:
                voice "audio/voices/ch2/witch/_encounter/opportunist/59.flac"
                opportunist "Locked in the basement? I thought for sure she was just going to stab us.\n"
            else:
                voice "audio/voices/ch2/witch/_encounter/opportunist/60a.flac"
                opportunist "Maybe not stabbing her in the back wasn't such a great idea.\n"
            voice "audio/voices/ch2/witch/_encounter/narrator/89.flac"
            n "The Princess cackles from the other side of the door.\n"
            if loop_1_locked:
                voice "audio/voices/ch2/witch/_encounter/princess/64.flac"
                sp "I can't believe you let me do that to you again!\n"
            else:
                voice "audio/voices/ch2/witch/_encounter/princess/65.flac"
                sp "How does it feel to be locked away and forgotten by the world? Isn't it just awful?\n"
            label witch_leave_locked_menu:
                default witch_leave_locked_try = False
                default witch_leave_locked_force = False
                default witch_leave_locked_plead = False
                default witch_leave_locked_funny = False
                default witch_leave_locked_need = False
                menu:
                    extend ""

                    "{i}• (Explore) Try the door.{/i}" if witch_leave_locked_try == False and witch_leave_locked_force == False:
                        $ witch_leave_locked_try = True
                        play audio "audio/one_shot/door_try.flac"
                        voice "audio/voices/ch2/witch/_encounter/narrator/90.flac"
                        n "You try the door. It's locked.\n"
                        jump witch_leave_locked_menu

                    "{i}• (Explore) Force the door.{/i}" if witch_leave_locked_force == False:
                        $ witch_leave_locked_force = True
                        play audio "audio/one_shot/door_try.flac"
                        voice "audio/voices/ch2/witch/_encounter/narrator/91.flac"
                        n "You throw yourself against the door. It won't budge.\n"
                        jump witch_leave_locked_menu

                    "{i}• (Explore) ''Okay. Fine. You got me. Very funny. Can you let me out now?''{/i}" if witch_leave_locked_funny == False:
                        $ witch_leave_locked_funny = True
                        voice "audio/voices/ch2/witch/_encounter/princess/66.flac"
                        sp "No! You're going to sit down there forever. Languishing!\n"
                        jump witch_leave_locked_menu

                    "{i}• (Explore) ''Please just let me out, I promise I won't be mad.''{/i}" if witch_leave_locked_plead == False:
                        $ witch_leave_locked_plead = True
                        voice "audio/voices/ch2/witch/_encounter/princess/67.flac"
                        sp "As if I could ever trust you after everything you've done to me. And after what I've done to you, you can't trust me, either. Neither of us is ever getting out of here.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/68.flac"
                        sp "It's in our nature to be trapped.\n"
                        jump witch_leave_locked_menu

                    "{i}• (Explore) ''I thought you needed me to get out.''{/i}" if witch_leave_locked_need == False:
                        $ witch_leave_locked_need = True
                        voice "audio/voices/ch2/witch/_encounter/princess/69.flac"
                        sp "I do. But I just couldn't help myself. And we both know that you're already scheming about how to get back at me if I ever open this door.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/70.flac"
                        sp "So we're going to stay exactly as we are right now. For as long as either of us lives.\n"
                        jump witch_leave_locked_menu

                    "{i}• Okay. What happens now? I'm stuck here.{/i}":
                        $ gallery_witch.unlock_item(12)
                        $ gallery_witch.unlock_item(13)
                        $ gallery_witch.unlock_item(14)
                        $ gallery_witch.unlock_item(15)
                        $ renpy.save_persistent()
                        stop music fadeout 15.0
                        stop sound fadeout 20.0
                        stop tertiary fadeout 20.0
                        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                        show quiet creep1 onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        hero "...\n"
                        opportunist "...\n"
                        voice "audio/voices/ch2/witch/_encounter/hero/41.flac"
                        show quiet creep2 onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        hero "Why isn't He saying anything?\n"
                        voice "audio/voices/ch2/witch/_encounter/opportunist/61a.flac"
                        hide bg onlayer back
                        show quiet creep3 onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        opportunist "I think He's gone.\n"
                        show witch slam quiet first onlayer back at Position(ypos=1125)
                        $ renpy.pause(0.5)
                        show witch slam quiet aback onlayer back
                        $ renpy.pause(0.1)
                        voice "audio/voices/ch2/witch/_encounter/princess/71.flac"
                        hide bg onlayer back
                        hide quiet onlayer back
                        show farback quiet onlayer farback at Position(ypos=1125)
                        with Dissolve(1.0)
                        show witch slam quiet aback talk onlayer back
                        with dissolve
                        sp "O-oh! I didn't think I'd have to see you face-to-face again, otherwise I might have given you a little more courtesy at the top of the stairs. No hard feelings, I'm sure.\n"
                        voice "audio/voices/ch2/witch/_encounter/princess/72.flac"
                        sp "Why is everything going away? I feel... cold.\n"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show arms witch s1 onlayer farback at Position(ypos=1125)
                        with Dissolve(1.0)
                        $ renpy.pause(0.125)
                        show witch slam quiet taken onlayer back
                        show arms witch s2 onlayer farback
                        with Dissolve(1.0)
                        $ renpy.pause(0.125)
                        hide witch onlayer back
                        show arms witch s3 onlayer farback
                        with Dissolve(0.5)
                        $ renpy.pause(0.125)
                        show arms witch s4 onlayer farback
                        with Dissolve(0.5)
                        $ renpy.pause(0.125)
                        hide arms onlayer farback
                        with Dissolve(0.5)
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
                            truth "But you don't get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                        else:
                            truth "But you don't get the chance to respond. Something has taken her away, and it's left something else in her place.\n"
                        $ witch_end = "witch_betray_lock"
                        $ princess_deny += 1
                        $ princess_kept += 1
                        jump mirror_start
                        # end





label witch_stairs_player_first:

    voice "audio/voices/ch2/witch/_encounter/princess/73.flac"
    show witch c squint talk onlayer front
    with dissolve
    sp "That's right! You're the one who's going first. Don't worry. I'll be right behind you, watching every single thing you do.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/62.flac"
    opportunist "That's exactly what I'm worried about.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/92.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    hide bg onlayer back
    hide witch onlayer front
    show farback witch stairs up onlayer farback at Position(ypos=1125)
    show bg witch stairs up onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "You step onto the stairs and begin your ascent from the basement. The Princess follows close on your heels, perhaps even a little closer than you'd like.\n"
    if blade_held == False:
        voice "audio/voices/ch2/witch/_encounter/hero/42.flac"
        hero "You're only saying that because you want us to feel nervous!\n"
    else:
        voice "audio/voices/ch2/witch/_encounter/hero/43.flac"
        hero "You're only saying that because you want us to feel nervous! You want us to turn around and kill her.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/93.flac"
    n "I do want those things, but I want them for a good reason. I don't need you to trust me for my sake, because I already know that I'm right. This is for you.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/63.flac"
    opportunist "Can we walk backwards up the stairs? I think that's the smarter idea. She can't sneak in an attack if we're facing her.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/94.flac"
    n "No. The stairs are a bunch of overgrown roots. You'll trip and hurt yourself.\n"
    # FAST
    voice "audio/voices/ch2/witch/_encounter/opportunist/64.flac"
    opportunist "But—\n{w=0.17}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch2/witch/_encounter/narrator/95.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    show farback witch stairs up onlayer farback at spectre_small_zoom, Position(ypos=1125)
    show bg witch stairs up onlayer back at spectre_small_zoom, Position(ypos=1125)
    with Dissolve(1.0)
    n "The Princess is silent as you both continue the climb, and in no time at all, the upstairs of the cabin is within reach.\n"
    voice "audio/voices/ch2/witch/_encounter/hero/44.flac"
    hero "Isn't that a relief? We're fine! Nothing happened.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/96.flac"
    n "You're not even going to wait until you're through that door to proudly claim your victory, are you?\n"
    voice "audio/voices/ch2/witch/_encounter/hero/45.flac"
    hero "... Why did you just say that?\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/65.flac"
    opportunist "I think we know why.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/97.flac"
    play audio "audio/final/Witch_ClawsRipWet_1.flac"
    hide farback onlayer farback
    hide bg onlayer back
    scene bg black
    n "You feel something dig into your shoulder, sharp and piercing, the Princess clawing at you and pulling you down with her full weight.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/98.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    play secondary "audio/one_shot/tower_stairs_fall.flac"
    queue secondary "audio/one_shot/tackle.flac"
    n "Together, you tumble back down the uneven stairs, your body and hers crashing against the unyielding wooden roots until finally, you both separate with a bone-shaking thud against the basement floor. You feel something pop.\n"
    $ achievement.grant("ACH_WITCH_FOOL")
    voice "audio/voices/ch2/witch/_encounter/narrator/99.flac"
    scene bg witch betray basement onlayer back at swayblur, Position(ypos=1125)
    show witch betray basement wounded onlayer back at swayblur, Position(ypos=1125)
    show player witch betray onlayer front at swayblur, Position(ypos=1125)
    with fade
    n "The Princess lands against the far wall, gasping as she struggles to recover from the impact..\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/83.flac"
    hide bg onlayer back
    hide witch onlayer back
    hide player onlayer front
    scene bg witch betray basement onlayer back at Position(ypos=1125)
    show witch betray basement laugh onlayer back at Position(ypos=1125)
    show player witch betray onlayer front at Position(ypos=1125)
    with Dissolve(1.5)
    n "You're still in shock, trying to get ahold of yourself. She grins as you continue to remain exactly where you are, cackling derisively as she watches you realize that you won't be getting up.\n"
    voice "audio/voices/ch2/witch/_encounter/hero/47.flac"
    show witch betray basement smug onlayer back
    with dissolve
    hero "Wait. Why won't we be getting up?\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/84.flac"
    n "I'm afraid your back is broken. One unlucky fall is all it takes, really, and you had several.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/66.flac"
    opportunist "You know what. I'll say it! That sucks! I don't like having a broken back.\n"
    voice "audio/voices/ch2/witch/_encounter/hero/48.flac"
    hero "We were going to help her! Why?! Why did she do that?\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/67.flac"
    opportunist "It's what I would have done.\n"
    voice "audio/voices/ch2/witch/_encounter/hero/49.flac"
    hero "Have you considered not being like that?\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/68.flac"
    opportunist "Of course not! It's what keeps us alive.\n"
    voice "audio/voices/ch2/witch/_encounter/hero/50.flac"
    hero "And yet here we are, paralyzed and stuck with someone who hates us in the basement of a remote cabin.\n"
    voice "audio/voices/ch2/witch/_encounter/princess/74.flac"
    show witch betray basement smug talk onlayer back
    with dissolve
    spmid "You must have known this was coming. The arrogance of turning your back to me after everything you'd done!\n"
    show witch betray basement smug onlayer back
    with dissolve
    jump witch_betrayal_menu

label witch_betrayal_menu:
    default witch_back_broken_share = False
    menu:
        extend ""

        "{i}• ''I can't get up. You broke my back.''{/i}" if witch_back_broken_share == False:
            $ witch_back_broken_share = True
            voice "audio/voices/ch2/witch/_encounter/princess/75a.flac"
            show witch betray basement cruel talk onlayer back
            with dissolve
            spmid "Oh, I broke your back, did I? You were the one who started this little game. You were the one who chose spite and violence and conflict! If not for your betrayal, I could have had my freedom a lifetime ago.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/76.flac"
            show witch betray basement celebrate talk onlayer back
            with dissolve
            spmid "But I'm the victor now! And that means I get to select my prize. If only I could decide which is better... do I kill you with my own hands? Or do I let you suffer the way you decided to let me suffer?\n"
            voice "audio/voices/ch2/witch/_encounter/princess/77.flac"
            show witch betray basement smug talk onlayer back
            with dissolve
            spmid "Maybe I'll do a bit of both.\n"

        "{i}• ''What the hell was that for? I was trying to help you out of here!''{/i}" if witch_stairs_implore == False:
            voice "audio/voices/ch2/witch/_encounter/princess/78.flac"
            show witch betray basement cruel talk onlayer back
            with dissolve
            spmid "Maybe you were and maybe you weren't. But even more than I wanted my freedom... I really, really wanted to hurt you.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/79.flac"
            show witch betray basement wounded talk onlayer back
            with dissolve
            spmid "And you know as well as I that by our very natures, only one of us could make it up those stairs unscathed. Someone had to make the first move. Better me than you.\n"

        "{i}• ''Damn. I thought I had you there''{/i}" if witch_stairs_implore:
            voice "audio/voices/ch2/witch/_encounter/narrator/102.flac"
            show witch betray basement laugh onlayer back
            with dissolve
            n "The Princess lets out a mocking laugh.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/80.flac"
            show witch betray basement smug talk onlayer back
            with dissolve
            spmid "I could see your scheme twitching in every muscle. I understand you too well for there to be secrets between us. We're the same creatures at our core, spite runs through our very marrow.\n"
            voice "audio/voices/ch2/witch/_encounter/princess/81.flac"
            show witch betray basement cruel talk onlayer back
            with dissolve
            spmid "By our very natures, only one of us could make it up those stairs unscathed. Better me than you.\n"

        "{i}• ''We were never going to get up those stairs, were we?''{/i}":
            voice "audio/voices/ch2/witch/_encounter/narrator/102.flac"
            show witch betray basement laugh onlayer back
            with dissolve
            n "The Princess lets out a mocking laugh.\n"
            if witch_stairs_implore == False:
                voice "audio/voices/ch2/witch/_encounter/princess/82.flac"
                show witch betray basement cruel talk onlayer back
                with dissolve
                spmid "By our very natures, only one of us could make it upstairs unscathed. Someone had to make the first move. Better me than you.\n"
            else:
                if loop_1_locked:
                    voice "audio/voices/ch2/witch/_encounter/princess/83a.flac"
                    show witch betray basement cruel talk onlayer back
                    with dissolve
                    spmid "Of course not. By our very natures, only one of us could make it upstairs unscathed. Someone had to make the first move. If I had the chance, I would have locked you down in this basement again.\n"
                else:
                    voice "audio/voices/ch2/witch/_encounter/princess/84.flac"
                    show witch betray basement cruel talk onlayer back
                    with dissolve
                    spmid "Of course not. By our very natures, only one of us could make it upstairs unscathed. Someone had to make the first move. If I had the chance, I would have locked you down in this basement.\n"
                voice "audio/voices/ch2/witch/_encounter/princess/85.flac"
                show witch betray basement smug talk onlayer back
                with dissolve
                spmid "It would have been funny. Even if it meant I couldn't leave. I really, truly detest you.\n"

        "{i}• ''We could have gotten out of here if we'd just trusted each other.''{/i}":
            if loop_1_locked:
                voice "audio/voices/ch2/witch/_encounter/princess/86a.flac"
                show witch betray basement smug talk onlayer back
                with dissolve
                spmid "You should have known I would never walk hand-in-hand with a loathsome thing like you.\n"
            else:
                voice "audio/voices/ch2/witch/_encounter/princess/86.flac"
                show witch betray basement smug talk onlayer back
                with dissolve
                spmid "Why would I ever trust you? Your hands have spilled my blood. And knowing that, you should never have trusted me, either. You should have known I would never walk hand-in-hand with a loathsome thing like you.\n"
            if witch_stairs_implore == False:
                voice "audio/voices/ch2/witch/_encounter/princess/87.flac"
                show witch betray basement cruel talk onlayer back
                with dissolve
                spmid "By our very natures, only one of us could make it upstairs unscathed. Someone had to make the first move. Better me than you.\n"
            else:
                label witch_locked_joke:
                    if loop_1_locked:
                        voice "audio/voices/ch2/witch/_encounter/princess/88.flac"
                        show witch betray basement cruel talk onlayer back
                        with dissolve
                        spmid "Somebody had to make the first move. And if I had the chance, I would have locked you in this basement again.\n"
                    else:
                        voice "audio/voices/ch2/witch/_encounter/princess/89.flac"
                        show witch betray basement cruel talk onlayer back
                        with dissolve
                        spmid "Somebody had to make the first move. And if I had the chance, I would have locked you in this basement.\n"
                    voice "audio/voices/ch2/witch/_encounter/princess/85.flac"
                    show witch betray basement smug talk onlayer back
                    with dissolve
                    spmid "It would have been funny, even if it meant I couldn't leave. I really, truly detest you.\n"

        "{i}• [[Say nothing.]{/i}":
            if witch_stairs_implore == False:
                voice "audio/voices/ch2/witch/_encounter/princess/87.flac"
                show witch betray basement cruel talk onlayer back
                with dissolve
                spmid "By our very natures, only one of us could make it upstairs unscathed. Someone had to make the first move. Better me than you.\n"
            else:
                voice "audio/voices/ch2/witch/_encounter/princess/90.flac"
                show witch betray basement cruel talk onlayer back
                with dissolve
                spmid "By our very natures, only one of us could make it upstairs unscathed.\n"
                jump witch_locked_joke

    show witch betray basement cruel onlayer back
    with dissolve
    if witch_stairs_implore:
        voice "audio/voices/ch2/witch/_encounter/opportunist/69.flac"
        opportunist "At least we can all agree that it was a good idea to make her go first.\n"
        voice "audio/voices/ch2/witch/_encounter/hero/51.flac"
        hero "How?\n"
        voice "audio/voices/ch2/witch/_encounter/opportunist/70.flac"
        opportunist "Well, she was going to betray us, wasn't she? And we struck first!\n"
        voice "audio/voices/ch2/witch/_encounter/hero/52.flac"
        hero "Our back is broken.\n"
        voice "audio/voices/ch2/witch/_encounter/opportunist/71.flac"
        opportunist "But we gave it our all! No regrets! Besides, she's got to have it as bad as us, right?\n"


    else:
        if blade_held:
            voice "audio/voices/ch2/witch/_encounter/opportunist/72.flac"
            opportunist "See, this is why I wanted her to go first. I had this whole little scheme planned where she'd turn her back on us, and I'd say 'Now stab her in the back! Do it now!'\n"
        else:
            voice "audio/voices/ch2/witch/_encounter/opportunist/73.flac"
            opportunist "See, this is why I wanted her to go first. I had this whole little scheme planned where once she'd passed by the table upstairs, I'd have said 'now pick up the blade and stab her in the back.'\n"
        voice "audio/voices/ch2/witch/_encounter/opportunist/74.flac"
        opportunist "And then you'd say something like 'wow, that's an amazing idea that I never saw coming, thanks for looking out for us!'\n"
        voice "audio/voices/ch2/witch/_encounter/opportunist/75.flac"
        opportunist "And then you would've done it! And we wouldn't be stuck down here with a broken back!\n"
        if blade_held:
            voice "audio/voices/ch2/witch/_encounter/hero/53.flac"
            hero "Why didn't you tell us your plan {i}before{/i} we agreed to go first?\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/76a.flac"
            opportunist "Because then you'd have had to lie to her. And you're a terrible liar.\n"
            voice "audio/voices/ch2/witch/_encounter/hero/54.flac"
            hero "That's not— okay that's actually a good point.\n"
            voice "audio/voices/ch2/witch/_encounter/narrator/103.flac"
            n "It would have been a good point if it had actually worked. But it didn't work, did it?\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/77a.flac"
            opportunist "Well, it's not my fault that nobody listened to me.\n"
        else:
            voice "audio/voices/ch2/witch/_encounter/hero/55.flac"
            hero "There's just one problem with that.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/78.flac"
            opportunist "And what's that?\n"
            voice "audio/voices/ch2/witch/_encounter/hero/56.flac"
            hero "She was clearly planning to betray us. And if she was in front of us, she would've gotten to the blade first.\n"
            voice "audio/voices/ch2/witch/_encounter/opportunist/79.flac"
            opportunist "Ugh. You're right, aren't you? I thought this whole thing was ironclad, but really it was doomed from the start, wasn't it?\n"

    voice "audio/voices/ch2/witch/_encounter/narrator/104.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    show witch betray basement twitch onlayer back at shakeshort
    with dissolve
    n "The Princess' body twitches as she tries to get up.\n"
    if witch_stairs_implore == False:
        voice "audio/voices/ch2/witch/_encounter/opportunist/80.flac"
        opportunist "Oh! So she's got it as bad as us.\n"
    else:
        voice "audio/voices/ch2/witch/_encounter/opportunist/81.flac"
        opportunist "Oh! So she does have it as bad as us.\n"
    if witch_back_broken_share:
        voice "audio/voices/ch2/witch/_encounter/princess/91.flac"
        show witch betray basement irony talk onlayer back
        with dissolve
        spmid "It seems you're not the only one who's broken.\n"
    else:
        voice "audio/voices/ch2/witch/_encounter/princess/92.flac"
        show witch betray basement irony talk onlayer back
        with dissolve
        spmid "Something inside me is... broken. Isn't that a cruel twist of the knife? Isn't that so, so funny?\n"
        voice "audio/voices/ch2/witch/_encounter/narrator/105.flac"
        show witch betray basement cold onlayer back
        with dissolve
        n "She eyes you with intensity, silence falling between you for a long moment as her gaze travels up and down your battered form.\n"
        voice "audio/voices/ch2/witch/_encounter/princess/93.flac"
        show witch betray basement smug talk onlayer back
        with dissolve
        spmid "Seems I'm not the only one, though.\n"

    voice "audio/voices/ch2/witch/_encounter/hero/57.flac"
    show witch betray basement wounded onlayer back
    with dissolve
    hero "Wait... are we both just stuck here?\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/106.flac"
    n "It certainly seems that way. What a way to go. But look on the bright side! In all this chaos, you may have actually managed to deliver a lethal wound. The world could be saved after all.\n"
    voice "audio/voices/ch2/witch/_encounter/princess/94.flac"
    stop music fadeout 15.0
    stop sound fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
    show witch betray basement irony talk onlayer back
    with dissolve
    spmid "We're going to die together. Isn't that a lovely treat! I wonder how long it'll take. Maybe I'll get to watch the worms lick your bones clean.\n"
    voice "audio/voices/ch2/witch/_encounter/hero/58.flac"
    hide witch onlayer back
    show quiet creep1 onlayer back at Position(ypos=1125)
    show witch betray basement wounded onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    hero "Is that really what's going to happen now?\n"
    voice "audio/voices/ch2/witch/_encounter/hero/59.flac"
    show quiet creep2 onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    hero "... Hello? Are you still there? What happens next?\n"
    truth "He doesn't respond.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/82.flac"
    show quiet creep3 onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    opportunist "I think He's gone...\n"
    voice "audio/voices/ch2/witch/_encounter/princess/95.flac"
    show witch betray basement wounded talk onlayer back
    with dissolve
    spmid "Something strange is twisting this place out of shape.\n"
    voice "audio/voices/ch2/witch/_encounter/princess/96.flac"
    show witch betray basement cold onlayer back
    with dissolve
    spmid "I wasn't feeling much of anything. But now I feel... cold.\n"
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    hide witch onlayer back
    show arms witch b1 onlayer back at Position(ypos=1125)
    show witch betray basement cold onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.125)
    show arms witch b2 onlayer back at Position(ypos=1125)
    show witch betray basement quiet onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    show arms witch b3 onlayer back
    hide witch onlayer back
    with Dissolve(1.0)
    $ renpy.pause(0.125)
    show arms witch b4 onlayer back
    with Dissolve(0.4)
    $ renpy.pause(0.125)
    hide arms onlayer back
    with Dissolve(0.4)
    $ blade_held = False
    $ default_mouse = "default"
    hide player onlayer front
    hide player onlayer inyourface
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
    $ renpy.pause(0.125)
    if loops_finished != 0:
        truth "But you don't get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
    else:
        truth "But you don't get the chance to respond. Something has taken her away, and it's left something else in her place.\n"
    if witch_stairs_implore:
        $ witch_end = "player_betray"
    else:
        $ witch_end = "witch_betray"
    $ princess_deny += 1
    $ princess_kept += 1
    jump mirror_start
    # END



label witch_1_flee:
    $ achievement.grant("ACH_WITCH_ABANDON")
    voice "audio/voices/ch2/witch/_encounter/narrator/107.flac"
    play tertiary "audio/final/Witch_RootsMoving_1.flac"
    play audio "audio/one_shot/footstep_run_medium.flac"
    show farback witch stairs up onlayer farback at small_zoom, Position(ypos=1125)
    show bg witch stairs up flee onlayer back at small_zoom, Position(ypos=1125)
    with dissolve
    n "As the roots that make up the walls of the cramped basement attempt to close in around you, instinct kicks in, and you bolt upstairs.\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/108.flac"
    play tertiary "audio/final/Witch_TreeWrap_1.flac"
    play audio "audio/one_shot/footstep_run_medium.flac"
    show farback witch stairs up onlayer farback at big_zoom_instant, Position(ypos=1125)
    show bg witch stairs up flee onlayer back at big_zoom_instant, Position(ypos=1125)
    with dissolve
    n "The steps are uneven and lively, creaking as they expand out of the dirt floor, the stairway growing smaller and smaller as you dart up towards the light. You manage to squeeze through the door just as the entrance seals itself shut behind you.\n"
    $ quick_menu = False
    voice "audio/voices/ch2/witch/_encounter/narrator/109.flac"
    play audio "audio/final/Witch_RootsMoving_2.flac"
    hide farback onlayer farback
    hide bg onlayer back
    show farback damsel outside onlayer farback at Position(ypos=1125)
    show bg witch cabin flee 1 onlayer back at Position(ypos=1185)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The cabin is smaller than it was before. And it's getting even smaller, and smaller.\n"
    voice "audio/voices/ch2/witch/_encounter/opportunist/83.flac"
    opportunist "That's fine. We'll just leave!\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/110.flac"
    n "I'm sure you'd like to do that. But unfortunately, there is no longer a front door. The roots have already closed over the only possible exit. What little light peaks through the holes that were once windows is growing weaker as the cabin continues to close in on itself.\n"
    voice "audio/voices/ch2/witch/_encounter/hero/60.flac"
    hero "Shit. What do we do?!\n"
    voice "audio/voices/ch2/witch/_encounter/narrator/111.flac"
    n "As your mind races for an answer, you hear the Princess' voice crackle up the stairs.\n"
    voice "audio/voices/ch2/witch/_encounter/princess/97.flac"
    sp "Do you hear that, you loathsome thing? Those are the roots of the wild, and they're coming to choke the breath from your lungs and squeeze the life out of you!\n"
    label witch_upstairs_menu:
        default witch_upstairs_count = 0
        if witch_upstairs_count == 1:
            voice "audio/voices/ch2/witch/_encounter/narrator/54.flac"
            play audio "audio/final/Witch_RootsMoving_1.flac"
            hide farback onalyer farback
            show bg witch cabin flee 2 onlayer back
            with Dissolve(1.0)
            n "The roots grow ever closer.\n"
            voice "audio/voices/ch2/witch/_encounter/hero/24.flac"
            hero "We know. We can see them.\n"
        elif witch_upstairs_count == 2:
            voice "audio/voices/ch2/witch/_encounter/narrator/113.flac"
            play audio "audio/final/Witch_RootsMoving_2.flac"
            hide farback onalyer farback
            show bg witch cabin flee 3 onlayer back
            with Dissolve(1.0)
            n "You feel something against your back. A thick root pushing its way into the cabin, an unstoppable, unyielding wall of bark. You're running out of time.\n"
            voice "audio/voices/ch2/witch/_encounter/hero/25.flac"
            hero "Shit, what do we do what do we do?\n"
        elif witch_upstairs_count == 3:
            jump witch_upstairs_end
        $ witch_upstairs_count += 1
        menu:
            extend ""

            "{i}• (Explore) ''What about you? They'll crush you just as easily as they'll crush me.''{/i}" if witch_fight_mutual_crush_comment == False:
                $ witch_fight_mutual_crush_comment = True
                voice "audio/voices/ch2/witch/_encounter/princess/98.flac"
                spmid "As long as you suffer while you die, I'll gladly suffer with you. Especially if I get to hear it happen.\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/84.flac"
                opportunist "This doesn't help anyone! I can't believe she'd kill us both just to spite me.\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/114.flac"
                n "See? This is exactly why you were tasked to slay her and why you shouldn't have left her in the basement. She's an antisocial monster who'll gladly burn the whole world for her satisfaction.\n"
                jump witch_upstairs_menu

            "{i}• (Explore) ''Make them stop! You can make them stop, right?''{/i}" if witch_fight_mutual_crush_comment_follow == False:
                $ witch_fight_mutual_crush_comment_follow = True
                if witch_fight_mutual_crush_comment == False:
                    $ witch_fight_mutual_crush_comment = True
                    voice "audio/voices/ch2/witch/_encounter/princess/99.flac"
                    sp "I could. But who says I want to? They're coming for me, too, but as long as you suffer while you die, I'll gladly suffer with you. Especially if I get to hear it happen.\n"
                    voice "audio/voices/ch2/witch/_encounter/opportunist/85.flac"
                    opportunist "This doesn't help anyone! I can't believe she'd kill herself just to spite me.\n"
                    voice "audio/voices/ch2/witch/_encounter/narrator/56.flac"
                    n "See? This is exactly why you've been tasked to slay her. She's an antisocial monster who'll gladly burn the whole world for her satisfaction.\n"
                else:
                    voice "audio/voices/ch2/witch/_encounter/princess/100.flac"
                    sp "I could, but as I already made so so clear, I. Don't. Want to.\n"
                jump witch_upstairs_menu

            "{i}• (Explore) ''Why, though? Why are you doing this?''{/i}" if witch_fight_mutual_crush_comment and witch_fight_mutual_crush_comment_follow == False:
                $ witch_fight_mutual_crush_comment_follow = True
                voice "audio/voices/ch2/witch/_encounter/princess/101.flac"
                spmid "Because it's in my nature. Just like you coming here to hurt me is in yours. It's who I am.\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/86.flac"
                opportunist "That is extremely not us. We're just doing what we're told, and making the best out of a difficult situation. We didn't even try to kill her! We just left her here.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/61.flac"
                hero "It's the same thing.\n"
                voice "audio/voices/ch2/witch/_encounter/narrator/116.flac"
                n "It isn't.\n"
                jump witch_upstairs_menu

            "{i}• (Explore) ''Come on! They're pressing in on me. They're probably pressing in on you too! I'm only assuming that because I can't see you but it sure sounds like they are!''{/i}" if witch_upstairs_count > 1 and witch_fight_menu_sucks_comment == False:
                $ witch_fight_menu_sucks_comment = True
                voice "audio/voices/ch2/witch/_encounter/princess/102.flac"
                spmid "Awww what's the matter? You're scared of thorny roots digging into your neck? Are you scared of suffocating in this dark, dark place alone? Good!\n"
                voice "audio/voices/ch2/witch/_encounter/opportunist/38.flac"
                opportunist "That one made me feel bad inside. I don't want people to think we're scared. Nobody likes someone who's scared of things.\n"
                voice "audio/voices/ch2/witch/_encounter/hero/62.flac"
                hero "I for one think this is a perfectly reasonable situation to feel scared in. This place is getting awful tight...\n"
                jump witch_upstairs_menu

            "{i}• (Explore) ''We're not animals! We're people. We can work this out. We can make things better.''{/i}" if witch_fight_menu_animals_comment == False:
                $ witch_fight_menu_animals_comment = True
                voice "audio/voices/ch2/witch/_encounter/princess/103.flac"
                sp "But we are animals! We are! You're nothing but fear and instinct and that's all I am, too! We don't have to make things better! We can't make things better!\n"
                voice "audio/voices/ch2/witch/_encounter/princess/104.flac"
                spmid "We're just meant to chase each other in the dark until one of us catches the other.\n"
                jump witch_upstairs_menu

            "{i}• (Explore) ''I take it all back! I can help you get out of here! You and I can work together! We can be friends.''{/i}" if witch_fight_menu_sorry == False:
                $ witch_fight_menu_sorry = True
                voice "audio/voices/ch2/witch/_encounter/princess/105.flac"
                spmid "Too late! We're both going to die! We're both going to die a splintery and miserable death! And you're going to hate it just as much as you hate me and I hate you!\n"
                jump witch_upstairs_menu

            "{i}• [[Give up, and await your death.]{/i}":
                label witch_upstairs_end:
                    voice "audio/voices/ch2/witch/_encounter/narrator/117.flac"
                    play audio "audio/final/Witch_RootsMoving_2.flac"
                    play tertiary "audio/one_shot/collapse.flac"
                    show fore witch brawl roots join onlayer front at Position(ypos=1125)
                    show bg witch cabin flee 3 onlayer back at collapse
                    with Dissolve(1.0)
                    n "You slump to the floor as the roots continue to expand into the cabin.\n"
                    voice "audio/voices/ch2/witch/_encounter/opportunist/41.flac"
                    opportunist "{i}Sigh{/i}. We're never going to make something of ourselves with that attitude.\n"
                    voice "audio/voices/ch2/witch/_encounter/hero/28.flac"
                    hero "At least she isn't going to 'make something of herself' either.\n"
                    voice "audio/voices/ch2/witch/_encounter/narrator/118.flac"
                    play audio "audio/final/Witch_RootsMoving_1.flac"
                    show fore witch brawl roots squish onlayer front
                    with Dissolve(1.0)
                    n "At first it's almost gentle, your body being lifted delicately off the ground as the floor shifts beneath you. But the cradle of the growing roots starts to feel suffocating, then unbearably tight, then that tightness gives way to bulging pressure as they begin to constrict.\n"
                    voice "audio/voices/ch2/witch/_encounter/narrator/119.flac"
                    play audio "audio/final/_witch_squish_1.flac"
                    show fore witch brawl roots last onlayer front
                    with Dissolve(1.0)
                    n "The sound of creaking wood is drowned out by the snaps and pops of your bones, pain flooding your senses as you feel your skin deform, being shaped unnaturally by the living cabin.\n"
                    voice "audio/voices/ch2/witch/_encounter/princess/106.flac"
                    sp "This suffering is what you deserve, you hideous creature! Know as you die that you are hated! I hate you! And I'm glad to die horribly if it means you die with me! I wouldn't have it any other way!\n"
                    voice "audio/voices/ch2/witch/_encounter/narrator/120.flac"
                    play audio "audio/final/_witch_squish_2.flac"
                    n "The pressure is unfathomable. You can't breathe, your vision swimming with red, your head pounding with trapped blood.\n"
                    play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
                    stop music
                    stop music2
                    stop sound
                    stop secondary
                    stop tertiary
                    voice "audio/voices/ch2/witch/_encounter/narrator/68.flac"
                    hide fore onlayer front
                    hide bg onlayer back
                    hide farback onlayer farback
                    show witch brawl roots dead onlayer back
                    $ renpy.pause(1.0)
                    voice sustain
                    hide witch onlayer back
                    scene bg black
                    n "And then you pop. Everything goes dark, and you die.\n"
                    $ wild_source = "witch"
                    $ wild_bonus_voice = "paranoid"
                    jump wild_start
                    # END

return
