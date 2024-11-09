label nightmare_encounter_start:
    stop music
    default nightmare_falling = False
    default nightmare_run_attempt = False
    default nightmare_can_wraith = True
    voice "audio/voices/ch2/nightmare/_encounter/narrator/1.flac"
    play audio "audio/final/Assorted_Static_2.flac"
    hide fog onlayer front
    hide nightmare onlayer front
    scene bg black big onlayer inyourface at Position(ypos=1125)
    n "Your vision cuts out as your blood begins to coagulate. It's as if every part of your being is coming to a lurching halt.\n"
    play audio "audio/final/Nightmare_BloodFlow_1.flac"
    play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop
    paranoid "Heart. Lungs. Liver. Nerves. Heart. Lungs. Liver. Nerves.\n"
    play music "audio/_music/ch2/nightmare/The Nightmare II.flac" loop
    voice "audio/voices/ch2/nightmare/_encounter/narrator/2.flac"
    play audio "audio/final/Nightmare_MaleBreath_1.flac"
    hide bg onlayer inyourface
    show nightmare head tilt2 onlayer front at Position(ypos=1125)
    n "Your lungs pull in a desperate gulp of air as your eyes shoot back open.\n"
    voice "audio/voices/ch2/nightmare/_encounter/hero/1a.flac"
    stop voice2
    hero "What are you doing?\n"
    voice "audio/voices/ch2/nightmare/_encounter/paranoid/1.flac"
    paranoid "I'm working. Do you want this body to function, or do you want—\n{w=4.0}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch2/nightmare/_encounter/narrator/3.flac"
    play audio "audio/final/Assorted_Static_5.flac"
    scene bg black big onlayer inyourface at Position(ypos=1125)
    n "And then experience stops once more as your body reapproaches death.\n"
    voice "audio/voices/ch2/nightmare/_encounter/hero/2.flac"
    hero "Okay, whatever you were doing, please just start doing it again.\n"
    voice "audio/voices/ch2/nightmare/_encounter/paranoid/2.flac"
    paranoid "Are you sure about that? Are you sure that's what you want, or do you want to interrupt me some more?\n"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/4.flac"
    n "You have seconds left.\n"
    voice "audio/voices/ch2/nightmare/_encounter/hero/3.flac"
    hero "Yes, I'm sure!\n"
    play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop
    play audio "audio/final/Nightmare_BloodFlow_1.flac"
    paranoid "Heart. Lungs. Liver. Nerves. Heart...\n"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/5.flac"
    play audio "audio/final/Nightmare_MaleBreath_1.flac"
    hide bg onlayer inyourface
    show nightmare head tilt onlayer front
    n "Again, your eyes shoot open as you gasp for breath.\n"
    voice "audio/voices/ch2/nightmare/_encounter/princess/1.flac"
    play audio "audio/one_shot/static_short.flac"
    show nightmare coy onlayer front
    sp "Can't decide what you want to do, can you?\n"
    voice "audio/voices/ch2/nightmare/_encounter/princess/2.flac"
    play audio "audio/final/Assorted_Static_14.flac"
    show nightmare hands hips onlayer front
    sp "Oh, well. Standing there gasping like a fish is more fun than dead, even if you look ridiculous.\n"
    #sp "Well, breathing is more fun than dead, even if you're not very good at it.\n"
    voice "audio/voices/ch2/nightmare/_encounter/hero/4.flac"
    hero "She isn't attacking us. Why?\n"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/6.flac"
    n "The 'why' doesn't matter. She's already proven her ill intent. Don't lose sight of your mission.\n"
    if blade_held:
        voice "audio/voices/ch2/nightmare/_encounter/narrator/7.flac"
        n "Your weapon is still in your hands. Strike at her and end this before it's too late.\n"
    else:
        voice "audio/voices/ch2/nightmare/_encounter/hero/5.flac"
        hero "And how are we supposed to do that? We don't have a weapon, and the way out of here is nowhere to be seen.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/8.flac"
        n "That isn't my fault.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/6.flac"
        hero "It doesn't matter whose fault it is, because fighting her isn't an option right now.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/9.flac"
        n "Then you should get looking, shouldn't you?\n"

label nightmare_encounter_menu:
    default nightmare_stairs_reveal = False
    default nightmare_turn_off_comment = False
    default nightmare_can_die_ask = False
    default nightmare_why_no_kill = False
    default nightmare_why_need = False
    default nightmare_why_threaten = False
    default nightmare_share_task = False
    default nightmare_people_die = False
    default nightmare_separate_ways = False
    default nightmare_agony_explore = False
    default nightmare_die_explore = False
    default nightmare_infinite_explore = False
    default nightmare_lunatic_explore = False
    default nightmare_turn_off_explore = False
    default nightmare_kill_threaten = False
    default nightmare_refuse_explore = False
    default nightmare_friendship_offer = False
    menu:
        extend ""

        "{i}• (Explore) ''Why won't you finish me off?''{/i}" if nightmare_why_no_kill == False:
            $ nightmare_why_no_kill = True
            voice "audio/voices/ch2/nightmare/_encounter/princess/3.flac"
            play audio "audio/final/Assorted_Static_14.flac"
            show nightmare head tilt onlayer front
            sp "Because I don't want to. And even I did, I don't have to.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/4.flac"
            sp "Look at the way you're struggling to stay alive. It's taking everything you have to keep your heart pumping right now. And I'm enjoying the show.\n"
            voice "audio/voices/ch2/nightmare/_encounter/narrator/10.flac"
            play audio "audio/final/Assorted_Static_10.flac"
            show nightmare touch1 onlayer front
            n "The Princess leans forward, bringing her masked-lips close to your ear.\n"
            stop voice2
            voice "audio/voices/ch2/nightmare/_encounter/princess/5.flac"
            sp "If I want to see you gone, all I need to do is break your concentration.\n"
            voice "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_mucho.flac"
            paranoid "HEART. LUNGS. LIVER. NERVES.\n"
            voice "audio/voices/ch2/nightmare/_encounter/narrator/11.flac"
            play audio "audio/final/Assorted_Static_4.flac"
            show nightmare touch2 onlayer front
            n "She slowly runs her velvet glove across the base of your neck. It feels like static and then—\n{w=8.0}{nw}"
            show screen disableclick(0.5)
            play audio "audio/final/Assorted_Static_5.flac"
            voice "audio/voices/ch2/nightmare/_encounter/paranoid/3.flac"
            scene bg black big onlayer inyourface at Position(ypos=1125)
            paranoid "Shit shit shit, make her stop!\n"
            voice "audio/voices/ch2/nightmare/_encounter/hero/7.flac"
            hero "Hey! Snap out of it!\n"
            voice "audio/voices/ch2/nightmare/_encounter/paranoid/4.flac"
            play audio "audio/final/Nightmare_BloodFlow_1.flac"
            paranoid "Okay. Deep breath. Deep breath. We're fine. Heart. Lungs. Liver. Nerves. Heart...\n"
            voice "audio/voices/ch2/nightmare/_encounter/narrator/12.flac"
            play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_fast.ogg" loop fadein 1.0
            hide bg onlayer inyourface
            n "—you're back.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/6.flac"
            sp "One moment, and then you're gone. Just. Like. That.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/7.flac"
            show nightmare touch1 onlayer front
            sp "Ah, and there's the fear.\n"
            voice "audio/voices/ch2/nightmare/_encounter/narrator/13.flac"
            play audio "audio/one_shot/static_short.flac"
            show nightmare upstairs neutral onlayer front
            n "She pulls away.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/8a.flac"
            show nightmare upstairs impatient onlayer front
            spmid "But that wouldn't be very fun, now would it? I've already done that.\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''What good am I to you alive? What do you want from me?''{/i}" if nightmare_why_need == False and nightmare_why_no_kill == False:
            jump nightmare_want_leave_join

        "{i}• (Explore) ''What happened after you killed me last time?''{/i}" if nightmare_why_need == False:
            label nightmare_want_leave_join:
                $ nightmare_why_need = True
                voice "audio/voices/ch2/nightmare/_encounter/princess/9.flac"
                play audio "audio/one_shot/static_short.flac"
                show nightmare head tilt2 onlayer front
                sp "I tried to leave while you suffocated, but that stupid cabin wouldn't let me. So I started to drag your body out with me and then...\n"
                voice "audio/voices/ch2/nightmare/_encounter/princess/10.flac"
                play audio "audio/final/Assorted_Static_4.flac"
                show nightmare coy onlayer front
                sp "Well, you died before I could get to the door. And then I was here, and now you're here too.\n"
                voice "audio/voices/ch2/nightmare/_encounter/princess/11.flac"
                play audio "audio/final/Assorted_Static_13.flac"
                show nightmare hands hips onlayer front
                sp "I don't think I can leave without you, and dead doesn't count. And as much as I love what we have going on, I have bigger plans than tormenting one poor little creature forever. I want to leave.\n"
                jump nightmare_encounter_menu

        "{i}• (Explore) ''If you need me alive, then why did you threaten me on the stairs? Why didn't you try being nice to me?''{/i}" if nightmare_why_need and nightmare_why_threaten == False:
            $ nightmare_why_threaten = True
            voice "audio/voices/ch2/nightmare/_encounter/princess/12.flac"
            play audio "audio/final/Assorted_Static_14.flac"
            show nightmare stairs door onlayer front
            sp "I am being nice. You're alive, aren't you?\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/13.flac"
            play audio "audio/one_shot/static_short.flac"
            show nightmare head tilt2 onlayer front
            sp "And you died of fright as soon as you saw me last time. I didn't think keeping you alive was an option. But it looks like that's not a problem anymore. At least not for me!\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/14.flac"
            show nightmare head tilt onlayer front
            sp "You seem miserable.\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''I was sent here to stop you from destroying the world. I can't just let you leave.''{/i}" if nightmare_share_task == False:
            $ nightmare_share_task = True
            if basement_1_shared_task:
                voice "audio/voices/ch2/nightmare/_encounter/princess/15.flac"
                play audio "audio/one_shot/static_short.flac"
                show nightmare twirl 1 onlayer front
                sp "I know! You told me last time.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/16.flac"
            play audio "audio/final/Assorted_Static_3.flac"
            show nightmare head tilt2 onlayer front
            sp "'Destroy' is such an unenlightened way of putting it. So sudden. So violent. So little nuance.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/17.flac"
            play audio "audio/one_shot/static_short.flac"
            show nightmare upstairs neutral onlayer front
            spmid "I'm not going to destroy the world, but I am going to hold it in my hands and squeeze it.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/18.flac"
            play audio "audio/final/Assorted_Static_4.flac"
            show nightmare upstairs angry onlayer front
            sp "I'm going to make it afraid, just like I've made you afraid.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/19a.flac"
            play audio "audio/final/Assorted_Static_13.flac"
            show nightmare twirl full onlayer front
            sp "The world needs fear, doesn't it? Every terror I'd bring would make the good times so much better. I'm practically doing a public good! So what harm is there really in letting me out?\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''People will die if you do to them what you've done to me.''{/i}" if nightmare_share_task and nightmare_people_die == False:
            $ nightmare_people_die = True
            voice "audio/voices/ch2/nightmare/_encounter/princess/20.flac"
            play audio "audio/final/Assorted_Static_5.flac"
            show nightmare touch1 onlayer front
            sp "But everybody dies eventually! They're all full of wet, writhing things and in the end, each and every one of them gets unwound! And then those things get to become a new everybody, just to come apart all over again.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/21.flac"
            play audio "audio/one_shot/static_short.flac"
            show nightmare coy onlayer front
            sp "All I want is to be there for it! I want to watch it happen. And maybe do a little unwinding myself. Is that really so much to ask?\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''And if I let you out? What then? Do we go our separate ways?''{/i}" if nightmare_separate_ways == False and (nightmare_share_task or nightmare_why_need):
            $ nightmare_separate_ways = True
            voice "audio/voices/ch2/nightmare/_encounter/princess/22.flac"
            play audio "audio/final/Assorted_Static_11.flac"
            show nightmare hands hips onlayer front
            sp "Oh, no, definitely not. If you're what I need to leave this place, chances are you're pretty useful. I think I'll keep you right by my side. A little good luck charm, to make sure I stay free.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/23.flac"
            play audio "audio/one_shot/static_short.flac"
            show nightmare head tilt onlayer front
            sp "Don't worry, I'll make sure to take good care of you. I promise.\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''Being around you is agony. I'm not going to stick around.''{/i}" if nightmare_separate_ways and nightmare_agony_explore == False:
            $ nightmare_agony_explore = True
            voice "audio/voices/ch2/nightmare/_encounter/princess/24.flac"
            play audio "audio/final/Assorted_Static_4.flac"
            show nightmare hands hips onlayer front
            sp "We both know that you don't have a say here. So you should just look on the bright side.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/25.flac"
            play audio "audio/final/Assorted_Static_11.flac"
            show nightmare head tilt2 onlayer front
            sp "I don't know what the bright side is for you, but I'm positive you can find it if you look hard enough.\n"
            jump nightmare_encounter_menu


        "{i}• (Explore) ''I'll just die then.''{/i}" if nightmare_agony_explore and nightmare_die_explore == False:
            $ nightmare_die_explore = True
            voice "audio/voices/ch2/nightmare/_encounter/princess/26.flac"
            play audio "audio/final/Assorted_Static_13.flac"
            show nightmare twirl full onlayer front
            sp "And then we'll wind up right back where we started. Round and round we'll go! I wonder what will be different next time. Maybe you'll actually be able to move a limb. Who knows!\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/27.flac"
            play audio "audio/final/Assorted_Static_11.flac"
            show nightmare touch1 onlayer front
            sp "But I'm always going to win.\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''Are you sure about that? Give it enough tries and I'm bound to win eventually. And maybe you don't get to come back like I do.''{/i}" if nightmare_die_explore and nightmare_infinite_explore == False:
            $ nightmare_infinite_explore = True
            voice "audio/voices/ch2/nightmare/_encounter/princess/28.flac"
            play audio "audio/final/static_short.flac"
            show nightmare upstairs impatient onlayer front
            spmid "Is that a bet you're willing to take? Imagine climbing a mountain of lifetimes, and when you finally reach the summit, when you finally win, the only view you find is me.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/29.flac"
            play audio "audio/final/Assorted_Static_13.flac"
            show nightmare twirl full onlayer front
            sp "And then I push you, and you go tumbling all the way down those millions upon millions of battered and broken pieces of you that couldn't make the cut.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/30.flac"
            play audio "audio/final/Assorted_Static_4.flac"
            show nightmare head tilt onlayer front
            sp "What then? Would you have it in you to climb again? It sounds like a lot of effort for nothing. When instead, we can just leave this place together. Hand-in-hand.\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''You're a lunatic. You know that, right?''{/i}" if nightmare_lunatic_explore == False:
            $ nightmare_lunatic_explore = True
            play audio "audio/final/Assorted_Static_5.flac"
            show nightmare stairs wait onlayer front
            if nightmare_turn_off_comment == False:
                $ nightmare_turn_off_comment = True
                voice "audio/voices/ch2/nightmare/_encounter/princess/31.flac"
                sp "I am what I am. And right now, I'm in control.\n"
            else:
                voice "audio/voices/ch2/nightmare/_encounter/princess/32.flac"
                sp "Like I said, I am what I am. And right now, I'm in control.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/33.flac"
            play audio "audio/final/Assorted_Static_10.flac"
            show nightmare stairs door onlayer front
            sp "So... you might want to be a little nicer to me.\n"
            voice "audio/voices/ch2/nightmare/_encounter/narrator/14.flac"
            play audio "audio/final/static_short.flac"
            show nightmare touch1 onlayer front
            n "She raises one long gloved finger, its tip hovering just over your skin, seeming to enjoy the lingering threat. But she withdraws, sparing you another momentary glimpse of death.\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''If you want to work together, can you at least turn off this whole organs-shutting-down situation?''{/i}" if nightmare_turn_off_explore == False:
            $ nightmare_turn_off_explore = True
            play audio "audio/final/Assorted_Static_14.flac"
            show nightmare coy onlayer front
            if nightmare_turn_off_comment == False:
                $ nightmare_turn_off_comment = True
                voice "audio/voices/ch2/nightmare/_encounter/princess/34a.flac"
                sp "I am what I am. It's not my fault that you can't handle being around me.\n"
            else:
                voice "audio/voices/ch2/nightmare/_encounter/princess/35.flac"
                sp "Like I said, I am what I am. It's not my fault that you can't handle being around me.\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''How about I just kill you instead?''{/i}" if nightmare_can_die_ask == False and nightmare_kill_threaten == False:
            $ nightmare_kill_threaten = True
            if blade_held:
                jump nightmare_can_die_join
            else:
                voice "audio/voices/ch2/nightmare/_encounter/princess/36a.flac"
                play audio "audio/final/Assorted_Static_5.flac"
                show nightmare stairs door onlayer front
                sp "That's adorable!\n"
                voice "audio/voices/ch2/nightmare/_encounter/princess/37.flac"
                play audio "audio/final/Assorted_Static_4.flac"
                show nightmare head tilt2 onlayer front
                sp "You don't have anything that can hurt me, so do your worst.\n"
                jump nightmare_encounter_menu

        "{i}• (Explore) ''Does that mean you can die?''{/i}" if nightmare_can_die_ask == False and nightmare_kill_threaten:
            label nightmare_can_die_join:
                $ nightmare_can_die_ask = True
                voice "audio/voices/ch2/nightmare/_encounter/narrator/15.flac"
                play audio "audio/final/Assorted_Static_4.flac"
                play tertiary "audio/final/Nightmare_NeckCrack_1.flac"
                show nightmare head tilt onlayer front
                n "The Princess cocks her head, neck cracking uncomfortably, and you can't help but imagine a smile carve its way from ear to ear on the other side of her mask.\n"
                if blade_held:
                    voice "audio/voices/ch2/nightmare/_encounter/princess/38.flac"
                    play audio "audio/final/Assorted_Static_4.flac"
                    show nightmare hands hips onlayer front
                    sp "Thinking about that knife, are we?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/39.flac"
                    play audio "audio/final/Assorted_Static_2.flac"
                    show nightmare upstairs angry onlayer front
                    sp "Go ahead. Put that little theory to the test. See how it plays out. But I don't think you're going to like what happens.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/40.flac"
                    play audio "audio/final/Assorted_Static_12.flac"
                    show nightmare upstairs impatient onlayer front
                    spmid "Because even if you make me dead, you're not getting out of here.\n"
                    play audio "audio/final/Assorted_Static_4.flac"
                    show nightmare stairs wait onlayer front
                    if nightmare_stairs_reveal == False:
                        voice "audio/voices/ch2/nightmare/_encounter/princess/41.flac"
                        sp "This place is {i}mine{/i}.\n"
                    else:
                        voice "audio/voices/ch2/nightmare/_encounter/princess/42.flac"
                        sp "Don't forget that this place is {i}mine{/i}.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/43.flac"
                    sp "And I'm not giving you the stairs unless I'm leaving with you.\n"
                else:
                    voice "audio/voices/ch2/nightmare/_encounter/princess/44.flac"
                    play audio "audio/final/Assorted_Static_5.flac"
                    show nightmare stairs wait onlayer front
                    sp "Of course I can die! I'm dying all the time and so are you. But we're both still here, and you can't make me go away.\n"
                jump nightmare_encounter_menu

        "{i}• (Explore) ''And what if I refuse to let you out? What happens then?''{/i}" if nightmare_refuse_explore == False and (nightmare_share_task or nightmare_why_need):
            $ nightmare_refuse_explore = True
            voice "audio/voices/ch2/nightmare/_encounter/princess/45.flac"
            play audio "audio/final/Assorted_Static_4.flac"
            show nightmare hands hips onlayer front
            sp "Then we're stuck down here together until you change your mind.\n"
            stop voice2 fadeout 1.0
            voice "audio/voices/ch2/nightmare/_encounter/narrator/16.flac"
            play audio "audio/final/Assorted_Static_12.flac"
            show bg black big onlayer inyourface at Position(ypos=1125)
            n "Static and a skipped beat as she touches your shoulder and whispers in your ear.\n"
            voice "audio/voices/ch2/nightmare/_encounter/paranoid/5.flac"
            play audio "audio/final/Nightmare_BloodFlow_1.flac"
            paranoid "NO! Heart! Lungs! Liver! Nerves!\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/46.flac"
            play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_fast.ogg" loop fadein 1.0
            play audio "audio/final/Nightmare_MaleBreath_1.flac"
            hide bg onlayer inyourface
            play audio "audio/final/Assorted_Static_4.flac"
            show nightmare touch1 onlayer front
            sp "Or until your heart finally gives out.\n"
            play audio "audio/final/Assorted_Static_5.flac"
            show nightmare twirl full onlayer front
            voice "audio/voices/ch2/nightmare/_encounter/princess/47.flac"
            sp "And then, when you die, I'll find myself somewhere new, and before too long, you'll be there too. That's how this all works right? This doesn't end until you let me out.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/48.flac"
            play audio "audio/final/static_short.flac"
            show nightmare stairs wait onlayer front
            sp "And a lot can happen before then. I'm sure I can get creative.\n"
            jump nightmare_encounter_menu

        "{i}• (Explore) ''We don't have to be enemies. We can work together. We can be friends, even.''{/i}" if nightmare_friendship_offer == False:
            $ nightmare_friendship_offer = True
            play audio "audio/final/Assorted_Static_5.flac"
            show nightmare coy onlayer front
            if nightmare_why_need == False:
                voice "audio/voices/ch2/nightmare/_encounter/princess/49.flac"
                sp "Would you look at that! You're suggesting exactly what I want. Somebody's ahead of the curve.\n"
                jump nightmare_want_leave_join
            else:
                voice "audio/voices/ch2/nightmare/_encounter/princess/50.flac"
                sp "I'm glad you're seeing things my way.\n"
            jump nightmare_encounter_menu


        "{i}• ''I'm not doing any of this. I'm not helping you leave, and I'm not going to try and kill you, so do your worst.'' [[Toss the blade and remain with your Nightmare.]{/i}" if blade_held:
            $ blade_held = False
            $ default_mouse = "default"
            play audio "audio/final/Razor_SwordSwish_3.flac"
            voice "audio/voices/ch2/nightmare/_encounter/narrator/17.flac"
            n "Are you serious?! You fling the blade into the void, denying yourself the opportunity to ever slay her and finish your mission.\n"
            voice "audio/voices/ch2/nightmare/_encounter/hero/8.flac"
            hero "Nobody's happy here. But... maybe it's for the best.\n"
            jump nightmare_delusion_join

        "{i}• ''I'm not doing any of this. I'm not helping you leave, and I'm not going to try and kill you, so do your worst.'' [[Remain with your Nightmare.]{/i}" if blade_held == False:
            label nightmare_delusion_join:
                voice "audio/voices/ch2/nightmare/_encounter/princess/51.flac"
                play audio "audio/final/Assorted_Static_12.flac"
                hide nightmare onlayer front
                hide farback onlayer farback
                hide eyes onlayer back
                hide eyes2 onlayer back
                hide wood onlayer front
                hide rocks onlayer front
                show nightmare closeup maskoff1 onlayer front at Position(ypos=1125)
                stop music
                sp "You poor, deluded thing. Do you think a single moment of bravery changes you into something you're not? I am what I am, and you're always going to be a coward.\n"
                label nightmare_delusion_late_join:
                    stop voice2
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/18.flac"
                    play music "audio/_music/mound/Oblivion.flac" loop
                    hide bg onlayer back
                    show nightmare maskremove onlayer front
                    with dissolve
                    stop voice2 fadeout 3.0
                    n "She raises a hand to her mask and pulls it down. You don't get the chance to see what lies beneath before it envelops you.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/19.flac"
                    hide nightmare onlayer front
                    hide farback onlayer farback
                    hide eyes onlayer back
                    hide eyes2 onlayer back
                    hide wood onlayer front
                    hide rocks onlayer front
                    show nm seq 1
                    n "Like a creeping mold, the complete reality of your existence threads it way through your mind. Birth, death, birth again. Decay and bloom. A million stitches from a million microscopic wounds you've inflicted on everyone you've ever met with every muscle you've moved and every word you've ever spoken.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/hero/9.flac"
                    hero "No no no!\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/52.flac"
                    spmid "Let me out.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/20.flac"
                    scene bg black
                    n "Your existence hurts them.\n"
                    #voice "audio/voices/ch2/nightmare/_encounter/princess/53.flac"
                    #sp "Let me out.\n"
                    #voice "audio/voices/ch2/nightmare/_encounter/narrator/21.flac"
                    #show nm seq 2
                    #n "The saccharine scent of the long-dead corpses you've left unburied. The marriages you've broken. The children you've orphaned.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/54.flac"
                    spmid "Let me out!\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/22.flac"
                    show nm seq 2
                    n "A lonely soul in a room by itself weeping. It lives for eighty years and then it's gone. And then it's there again.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/55.flac"
                    scene bg black
                    spmid "Let. Me. Out!\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/23.flac"
                    show nm seq 3
                    n "A reprieve. A good life. Love, children, a steady career. Recognition from your peers. Here one moment, gone the next. The worms have found their orifices.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/56.flac"
                    scene bg black
                    spmid "LET. ME. OUT!\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/24.flac"
                    show nm seq 4
                    n "Diagnosis. It forgets everything it is. Anger. Rage. Distance. Poverty. The lonely soul is lonely again. Love turns to mockery. It dies. It is reborn. Worse. Lonelier.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/57.flac"
                    spmid "LET ME OUT!\n"
                    voice "audio/voices/ch2/nightmare/_encounter/hero/10.flac"
                    hero "No no no no no! What's happening to us!\n"
                    #voice "audio/voices/ch2/nightmare/_encounter/paranoid/6.flac"
                    #paranoid "Just. Heart. Endure. Lungs. It. Liver. This. Nerves. Has. Heart. To. Lungs. End. Nerves. Eventually. Heart...\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/58.flac"
                    spmid "LET ME OUT!\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/25.flac"
                    n "This is all too much. I... can't keep going.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/paranoid/7.flac"
                    paranoid "You can't keep going? What are you talking about?\n"
                    truth "But he doesn't respond.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/59.flac"
                    scene sequence23
                    sp "Oops... I think I broke you.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/60.flac"
                    scene bg black
                    sp "I'll see you soon! You'll know what to do.\n"
                    $ gallery_nightmare.unlock_item(11)
                    $ gallery_nightmare.unlock_item(12)
                    $ gallery_nightmare.unlock_item(13)
                    $ gallery_nightmare.unlock_item(14)
                    $ gallery_nightmare.unlock_item(15)
                    $ gallery_nightmare.unlock_item(16)
                    $ renpy.save_persistent()
                    stop music
                    stop sound
                    stop secondary
                    scene bg black
                    truth "Your body is dead, but you live on.\n"
                    $ achievement.grant("ACH_NIGHT_MONOLITH")
                    jump nightmare_2_start

        "{i}• ''Okay, let's get out of here.'' [[Leave together.]{/i}":
            jump nightmare_leave_together_start

        "{i}• ''Fine, you win. I'll let you leave.'' [[Leave together.]{/i}":
            jump nightmare_leave_together_start

        "{i}• [[Run.]{/i}":
            $ nightmare_run_attempt = True
            scene bg black big onlayer inyourface at Position(ypos=1125)
            play audio "audio/one_shot/footstep_run_dirt_short.flac"
            voice "audio/voices/ch2/nightmare/_encounter/narrator/26.flac"
            n "You turn and run, doing your best to put one useless leg in front of the other.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/61.flac"
            stop music
            sp "You poor, poor thing. Wrong choice.\n"
            voice "audio/voices/ch2/nightmare/_encounter/narrator/27.flac"
            play audio "audio/final/Assorted_Static_12.flac"
            hide bg onlayer inyourface
            show nightmare closeup maskoff1 onlayer front at Position(ypos=1125)
            n "You get nowhere before the Princess is in front of you once again.\n"
            voice "audio/voices/ch2/nightmare/_encounter/princess/62.flac"
            sp "You're always going to be a coward.\n"
            jump nightmare_delusion_late_join

        "{i}• [[Slay the Princess.]{/i}" if nightmare_can_wraith and blade_held:
            if wraith_encountered:
                $ nightmare_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump nightmare_encounter_menu
            jump nightmare_kill_join

label nightmare_leave_together_start:
    voice "audio/voices/ch2/nightmare/_encounter/narrator/28.flac"
    n "What?! NO!\n"
    voice "audio/voices/ch2/nightmare/_encounter/princess/63.flac"
    play audio "audio/final/Assorted_Static_5.flac"
    show nightmare stairs wait onlayer front
    sp "I knew you'd come around! Oh, this is going to be so wonderful!\n"
    # FAST
    voice "audio/voices/ch2/nightmare/_encounter/narrator/29.flac"
    n "No I'm not going to let this happen, I— before you can utter another word, your body stops moving, and—\n{w=6.3}{nw}"
    show screen disableclick(0.5)
    play audio "audio/final/Assorted_Static_12.flac"
    scene bg black big onlayer inyourface at Position(ypos=1125)
    stop voice2
    voice "audio/voices/ch2/nightmare/_encounter/paranoid/8.flac"
    paranoid "Do you think you can just wrest control away from us? This body is barely functioning as is. Doesn't the world end if we fail to stop her? Won't letting us die here just make it end faster?\n"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/30.flac"
    n "Sh-shit...\n"
    play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_fast.ogg" loop fadein 1.0
    play audio "audio/final/Nightmare_BloodFlow_1.flac"
    paranoid "Heart. Lungs. Liver. Nerves. Heart...\n"
    hide bg onlayer inyourface
    play audio "audio/final/Nightmare_MaleBreath_1.flac"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/31.flac"
    hide nightmare onlayer front
    show stairs basement nightmare onlayer front at Position(ypos=1125)
    show nightmare stairs basement create onlayer front at Position(ypos=1125)
    hide wood onlayer front
    with dissolve
    n "With a flick of the Princess' wrist, the stairs slide back into place. I can't believe you're making me watch you damn everyone to torment and oblivion.\n"
    if blade_held:
        voice "audio/voices/ch2/nightmare/_encounter/princess/64.flac"
        play audio "audio/final/Assorted_Static_4.flac"
        show nightmare stairs wait onlayer front
        sp "Go ahead. I'll be right behind you.\n"
        stop voice2 fadeout 1.0
        $ renpy.pause(1.0)
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/9.flac"
        play audio "audio/final/Assorted_Static_5.flac"
        scene bg black big onlayer inyourface at Position(ypos=1125)
        paranoid "I wouldn't trust having our back to her.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/11.flac"
        hero "You're not wrong, but maybe you should let me handle the feedback. Just focus on keeping us alive.\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/10.flac"
        paranoid "Haha. Right.\n"
        play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_1.ogg" loop fadein 1.0
        play audio "audio/final/Nightmare_BloodFlow_1.flac"
        paranoid "Heart. Lungs. Liver. Nerves. Heart...\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/12.flac"
        hide bg onlayer inyourface
        play audio "audio/final/Nightmare_MaleBreath_1.flac"
        hero "Besides, I get the feeling she's telling the truth. She needs us alive.\n"
        label nightmare_leave_menu:
            default nightmare_leave_stairs_comment = False
            menu:
                extend ""

                "{i}• (Explore) ''How about you go first?''{/i}" if nightmare_leave_stairs_comment == False:
                    $ nightmare_leave_stairs_comment = True
                    voice "audio/voices/ch2/nightmare/_encounter/princess/65.flac"
                    play audio "audio/final/Assorted_Static_4.flac"
                    show nightmare stairs wait onlayer front
                    sp "What, are you scared of turning your back to me? You don't have to be worried that I'm going to do something bad. You're too important to me now.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/princess/66.flac"
                    play audio "audio/final/Assorted_Static_5.flac"
                    show nightmare stairs door onlayer front
                    sp "And besides, what if I lost track of you and dropped the stairs on accident? I wouldn't want that to happen. And I don't think you'd want that to happen either. So go on, go ahead.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/32.flac"
                    n "She urges you forward like one might a reluctant pet.\n"
                    jump nightmare_leave_menu

                "{i}• ''Okay. Fine'' [[Step onto the stairs.]{/i}" if nightmare_leave_stairs_comment:
                    jump nightmare_stairs_leave_join

                "{i}• [[Step onto the stairs.]{/i}" if nightmare_leave_stairs_comment == False:
                    label nightmare_stairs_leave_join:
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/33.flac"
                        play audio "audio/one_shot/footsteps_creaky.flac"
                        hide nightmare onlayer front
                        hide farback onlayer farback
                        hide eyes onlayer back
                        hide eyes2 onlayer back
                        hide wood onlayer front
                        hide rocks onlayer front
                        show farback nightmare basement onlayer farback at Position(ypos=1125)
                        show eyes nightmare stairs onlayer back at Position(ypos=1125)
                        show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
                        show stairs nightmare following onlayer front at Position(ypos=1125)
                        scene bg black
                        n "You place a shaky foot on the first step and begin your ascent from the basement.\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/34.flac"
                        play audio "audio/final/Assorted_Static_12.flac"
                        n "You can feel the static prickling of the Princess on your neck, your limbs buzzing with pins and needles, an uncomfortable and constant reminder that you exist, and that your existence is so very precarious.\n"
                        #n "For a brief moment, you glance back behind you. Nothing remains but the abyss.\n"
                        voice "audio/voices/ch2/nightmare/_encounter/princess/67.flac"
                        sp "You're almost there...\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/35.flac"
                        play audio "audio/one_shot/footsteps_creaky.flac"
                        hide nightmare onlayer front
                        hide farback onlayer farback
                        hide eyes onlayer back
                        hide eyes2 onlayer back
                        hide wood onlayer front
                        hide rocks onlayer front
                        hide stairs onlayer front
                        show farback nightmare basement onlayer farback at Position(ypos=1125)
                        show eyes nightmare stairs onlayer back at Position(ypos=1125)
                        show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
                        show door stairs nightmare onlayer front at Position(ypos=1125)
                        with fade
                        n "The only thing left between you and the cabin is the now shut door to the basement. It would be a real shame if it had locked behind you.\n"
                        stop voice2 fadeout 1.0
                        $ renpy.pause(1.0)
                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/11.flac"
                        paranoid "Oh, you snake. There wasn't even a door when we first got here. The door was from last time! I told you we shouldn't trust him!\n"
                        voice "audio/voices/ch2/nightmare/_encounter/hero/13.flac"
                        hero "I know he's messing with us, but you can't lose your cool. We need you right now, remember?\n"
                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/12.flac"
                        paranoid "Yes. I remember. Of course I remember. Heart. Lungs. Liver. Nerves. This is so frustrating! Heart...\n"
                        play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop
                        voice "audio/voices/ch2/nightmare/_encounter/hero/14.flac"
                        hero "Thank you. And you! You'd really rather us die down here than let her out?\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/36.flac"
                        n "Of course I would! As much as I want you to have a happy ending, the fate of the world is a little more important. And you still have a weapon. You can still make this right.\n"
                        label nightmare_stairs_blade_menu:
                            default nightmare_stairs_lock_comment = False
                            default nightmare_stairs_lock_try = False
                            default nightmare_made_it_upstairs = False
                            menu:
                                extend ""

                                "{i}• (Explore) ''I think the door's locked.''{/i}" if nightmare_stairs_lock_comment == False:
                                    $ nightmare_stairs_lock_comment = True
                                    if nightmare_stairs_lock_try == False:
                                        voice "audio/voices/ch2/nightmare/_encounter/princess/68.flac"
                                        sp "You haven't even tried it! It'll open. You just have to give it a tug.\n"
                                    else:
                                        voice "audio/voices/ch2/nightmare/_encounter/princess/69.flac"
                                        sp "It'll open. You just have to give it a tug.\n"
                                    jump nightmare_stairs_blade_menu

                                "{i}• (Explore) [[Try the door.]{/i}" if nightmare_stairs_lock_try == False or nightmare_stairs_lock_comment:
                                    $ nightmare_stairs_lock_try = True
                                    if nightmare_stairs_lock_comment:
                                        $ nightmare_made_it_upstairs = True
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/37.flac"
                                        play audio "audio/one_shot/door_bedroom.flac"
                                        hide door onlayer front
                                        if blade_held:
                                            show bg stairs nightmare door upstairs onlayer front at Position(ypos=1125)
                                        else:
                                            show bg stairs nightmare door upstairs knife onlayer front at Position(ypos=1125)
                                        show door stairs nightmare playeropen onlayer front at Position(ypos=1125)
                                        with dissolve
                                        n "You pull against the door. The lock gently clicks open in response to your effort, and the door creaks on its hinges. This isn't right! That's not even the way it's supposed to swing! It's supposed to swing {i}out{/i}.\n"
                                        stop voice2 fadeout 1.0
                                        $ renpy.pause(1.0)
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/13.flac"
                                        scene bg black big onlayer inyourface at Position(ypos=1125)
                                        play audio "audio/final/Assorted_Static_12.flac"
                                        paranoid "You're not nearly as powerful as you'd have us think, are you?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/15.flac"
                                        hero "Ahem.\n"
                                        play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop
                                        play audio "audio/final/Nightmare_BloodFlow_1.flac"
                                        paranoid "Heart. Lungs. Liver. Nerves. Heart...\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/16.flac"
                                        hide bg onlayer inyourface
                                        play audio "audio/final/Nightmare_MaleBreath_1.flac"
                                        hero "Anyways, like he said, you're not really in control here, are you?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/38.flac"
                                        n "I never said I was! If I was in control here, why would I need {i}you{/i} to slay her?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/17.flac"
                                        hero "I don't know! Secret reasons?!\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/princess/70.flac"
                                        sp "The door is open. What are you dawdling for? It's time for us to go. The world is waiting.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/39.flac"
                                        play audio "audio/final/Assorted_Static_13.flac"
                                        hide nightmare onlayer front
                                        hide farback onlayer farback
                                        hide eyes onlayer back
                                        hide eyes2 onlayer back
                                        hide wood onlayer front
                                        hide rocks onlayer front
                                        hide door onlayer front
                                        hide bg onlayer front
                                        show farback nightmare upstairs onlayer farback at Position(ypos=1125)
                                        show bg nightmare upstairs onlayer back at Position(ypos=1125)
                                        show nightmare upstairs impatient onlayer front at Position(ypos=1125)
                                        with Dissolve(2.0)
                                        n "Shit. The Princess moves past you and into the cabin. This is it. This is your final moment to make things right. KILL HER.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/18.flac"
                                        hero "I thought you wanted us to 'slay' her.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/40.flac"
                                        n "It's the same thing! Do it! Do it now! Do it now or everything is OVER.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/19.flac"
                                        hero "Okay, what do we do?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/20a.flac"
                                        hero "I said, 'what do we do?'\n"
                                        stop voice2 fadeout 1.0
                                        $ renpy.pause(1.0)
                                        scene bg black big onlayer inyourface at Position(ypos=1125)
                                        play audio "audio/final/Assorted_Static_4.flac"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/14.flac"
                                        paranoid "Oh, do you want to hear from me now?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/21.flac"
                                        hero "Yes!\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/15.flac"
                                        paranoid "Well I thought you needed me to run the autonomic nervous system.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/22.flac"
                                        hero "We do, but this is {i}important{/i}! Look, I'll even do it myself, just tell us who to trust!\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/23.flac"
                                        hero "Uhhh... brain?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/16.flac"
                                        paranoid "Heart...\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/24.flac"
                                        hero "Right. Heart.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/17.flac"
                                        paranoid "Lungs...\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/25.flac"
                                        hero "Lungs...\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/18.flac"
                                        paranoid "Liver. Nerves.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/26.flac"
                                        hero "Okay, thanks. I've got it.\n"
                                        play voice2 "audio/voices/ch2/nightmare/_encounter/hero/nm_hero_loop.ogg" loop
                                        play audio "audio/final/Nightmare_BloodFlow_1.flac"
                                        play audio "audio/final/Nightmare_MaleBreath_1.flac"
                                        hide bg onlayer inyourface
                                        hero "Heart. Lungs. Liver. Nerves. Heart...\n"
                                        stop voice2 fadeout 1.0
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/19.flac"
                                        paranoid "You're terrible at this.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/27.flac"
                                        hero "I know, but I'm doing my best—\n{w=2.2}{nw}"
                                        show screen disableclick(0.5)
                                        scene bg black big onlayer inyourface at Position(ypos=1125)
                                        play audio "audio/final/Assorted_Static_12.flac"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/20.flac"
                                        paranoid "Yes, it's very hard to stay focused on running things when other people are talking to you, isn't it?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/princess/71.flac"
                                        show nightmare upstairs angry onlayer front
                                        sp "WHAT ARE YOU DOING?!\n"
                                        play audio "audio/final/Nightmare_BloodFlow_1.flac"
                                        play voice2 "audio/voices/ch2/nightmare/_encounter/hero/nm_hero_loop_2.ogg" loop
                                        hero "Heart. Lungs. Liver. Nerves. Heart...\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/21.flac"
                                        hide bg onlayer inyourface
                                        play audio "audio/final/Nightmare_MaleBreath_1.flac"
                                        paranoid "Finally, I can talk. Now what were you asking me? Running everything kind of feels like popping in and out of consciousness. It's easy to lose track of things.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/41.flac"
                                        n "They were asking you for your blessing to trust me.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/22.flac"
                                        paranoid "Oh that's right! Yeah, fuck this guy. Don't trust him.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/42.flac"
                                        n "Really? So you'd have them trust {i}her{/i}?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/23.flac"
                                        paranoid "Oh of course not. Can't trust anybody here but ourselves. But I guess that leaves us back where we started, doesn't it?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/24.flac"
                                        paranoid "I suppose if I had to make a choice, I'd pick the one that doesn't make our organs shut down.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/43.flac"
                                        n "Thank you for your gracious show of support.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/25.flac"
                                        paranoid "But that's a marginal preference. We'll have to deal with Him later. I'd just rather deal with Him while our organs are intact.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/44.flac"
                                        n "{i}Sigh.{/i} Whatever. You heard what he had to say. So whether you trust me or not, killing her is still the best, nay, the only option you have worth taking.\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/26.flac"
                                        paranoid "All right. I'm done. You can let me take over again.\n"
                                        stop voice2 fadeout 1.0
                                        $ renpy.pause(1.0)
                                        voice "audio/voices/ch2/nightmare/_encounter/hero/28.flac"
                                        hero "Finally! That was awful. I really don't know how you do it.\n"
                                        play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop
                                        play audio "audio/final/Nightmare_BloodFlow_1.flac"
                                        paranoid "Heart. Lungs. Liver. Nerves. Heart...\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/princess/72.flac"
                                        show nightmare upstairs impatient onlayer front
                                        sp "You've been standing there staring blankly for a while now and I have to say my patience is running a little thin. So don't make a lady wait any longer, okay?\n"
                                        voice "audio/voices/ch2/nightmare/_encounter/princess/73.flac"
                                        play audio "audio/final/Assorted_Static_5.flac"
                                        show nightmare upstairs angry onlayer front
                                        sp "Open. The. Door.\n"
                                        label nightmare_upstairs_slay_menu:
                                            menu:
                                                extend ""

                                                "{i}• [[Slay the Princess.]{/i}" if nightmare_can_wraith:
                                                    if wraith_encountered:
                                                        $ nightmare_can_wraith = False
                                                        voice "audio/voices/mound/bonus/path.flac"
                                                        mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                                                        jump nightmare_upstairs_slay_menu
                                                    jump nightmare_kill_upstairs

                                                "{i}• [[Leave the Cabin.]{/i}":
                                                    jump nightmare_free_outside

                                    else:
                                        play audio "audio/one_shot/door_try.flac"
                                        voice "audio/voices/ch2/nightmare/_encounter/narrator/45.flac"
                                        n "Look at that! It's locked. What a relief for the world.\n"
                                        jump nightmare_stairs_blade_menu

                                "{i}• [[Slay the Princess.]{/i}" if nightmare_can_wraith:
                                    if wraith_encountered:
                                        $ nightmare_can_wraith = False
                                        voice "audio/voices/mound/bonus/path.flac"
                                        mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                                        jump nightmare_stairs_blade_menu
                                    jump nightmare_kill_upstairs
    else:
        voice "audio/voices/ch2/nightmare/_encounter/princess/74.flac"
        play audio "audio/final/Assorted_Static_5.flac"
        hide nightmare onlayer front
        hide farback onlayer farback
        hide eyes onlayer back
        hide eyes2 onlayer back
        hide wood onlayer front
        hide rocks onlayer front
        show farback nightmare basement onlayer farback at Position(ypos=1125)
        show eyes nightmare stairs onlayer back at Position(ypos=1125)
        show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
        show stairs nightmare following onlayer front at Position(ypos=1125)
        show nightmare stairs ahead onlayer front at Position(ypos=1125)
        with dissolve
        sp "Come along, now. You don't want to be stuck down here.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/46.flac"
        n "The Princess glides onto the stairs and beckons you to follow. If only you had a weapon. This would be the perfect opportunity to use it.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/29.flac"
        hero "But we don't. And we've already made our choice.\n"
        stop voice2 fadeout 1.0
        $ renpy.pause(1.0)
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/27.flac"
        paranoid "We can still grab it on the way out.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/30.flac"
        hero "You're not wrong, but maybe you should let me handle the suggestions for the time being. Just focus on keeping us alive.\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/28.flac"
        paranoid "Haha. Right.\n"
        play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop
        paranoid "Heart. Lungs. Liver. Nerves. Heart...\n"
        menu:
            extend ""

            "{i}• [[Step onto the stairs and follow the Princess.]{/i}":
                voice "audio/voices/ch2/nightmare/_encounter/narrator/47.flac"
                play audio "audio/one_shot/footsteps_creaky.flac"
                show nightmare stairs following onlayer front at Position(ypos=1125)
                with fade
                n "You step onto the basement stairs, following the Princess as she ascends. Pins and needles punctuate your every step, an uncomfortable and constant reminder of your mortality.\n"
                voice "audio/voices/ch2/nightmare/_encounter/narrator/48.flac"
                n "Is this really worth it?\n"
                voice "audio/voices/ch2/nightmare/_encounter/hero/31.flac"
                hero "At least it's a choice.\n"
                voice "audio/voices/ch2/nightmare/_encounter/narrator/49.flac"
                n "That doesn't justify anything. A terrible choice is still terrible.\n"
                voice "audio/voices/ch2/nightmare/_encounter/princess/75.flac"
                sp "Make sure you keep up. We wouldn't want you to fall.\n"
                voice "audio/voices/ch2/nightmare/_encounter/narrator/50.flac"
                show farback nightmare basement onlayer inyourface at Position(ypos=1125)
                show eyes nightmare stairs onlayer inyourface at Position(ypos=1125)
                show eyes2 nightmare stairs onlayer inyourface at Position(ypos=1125)
                with dissolve
                n "As if acting on instinct, you crane your neck and look behind you. There is nothing there.\n"

        voice "audio/voices/ch2/nightmare/_encounter/narrator/51.flac"
        hide farback onlayer inyourface
        hide eyes onlayer inyourface
        hide eyes2 onlayer inyourface
        hide nightmare onlayer front
        hide farback onlayer farback
        hide eyes onlayer back
        hide eyes2 onlayer back
        hide wood onlayer front
        hide rocks onlayer front
        hide stairs onlayer front
        show farback nightmare basement onlayer farback at Position(ypos=1125)
        show eyes nightmare stairs onlayer back at Position(ypos=1125)
        show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
        show bg stairs nightmare door upstairs knife onlayer front at Position(ypos=1125)
        show door stairs nightmare onlayer front at Position(ypos=1125)
        show nightmare stairs door open1 onlayer front at Position(ypos=1125)
        with fade
        n "The Princess reaches the top of the stairs and taps the door.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/51a.flac"
        play audio "audio/one_shot/door_bedroom.flac"
        play tertiary "audio/final/Nightmare_NeckCrack_1.flac"
        show nightmare stairs door open2 onlayer front at Position(ypos=1125)
        show door stairs nightmare open onlayer front at Position(ypos=1125)
        with dissolve
        n "Her head twists back in your direction, watching you with dead eyes as the way out creaks open.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/52.flac"
        n "Don't forget that your pristine blade is still on the other side. You can still make this right. You can still save everyone, and you can still save yourself from becoming her tormented pet.\n"
        stop voice2 fadeout 1.0
        $ renpy.pause(1.0)
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/29.flac"
        play audio "audio/final/Assorted_Static_12.flac"
        scene bg black big onlayer inyourface at Position(ypos=1125)
        paranoid "There's no harm in us having a weapon. All it does is give us more options. And we are dangerously low on those right now.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/32.flac"
        hero "Uh...\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/30.flac"
        paranoid "Have you considered that maybe you could operate the autonomic nervous system for a bit? Everyone is trying to manipulate us and I can only do so many things at once to keep us alive.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/33.flac"
        hero "Er... heart? Erm. Liver?\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/53.flac"
        n "Your body seizes violently as you regain consciousness on the floor of the cabin.\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/31.flac"
        paranoid "No, no no! You're doing it all wrong. You're supposed to do it like this: Heart. Lungs. Liver. Nerves. Heart...\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/32.flac"
        paranoid "I guess I have to do everything around here, don't I?\n"
        play audio "audio/final/Nightmare_BloodFlow_1.flac"
        play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop
        paranoid "Heart. Lungs. Liver. Nerves. Heart...\n"
        voice "audio/voices/ch2/nightmare/_encounter/princess/76.flac"
        play audio "audio/final/Nightmare_MaleBreath_1.flac"
        hide bg onlayer front
        hide bg onlayer inyourface
        hide nightmare onlayer front
        hide farback onlayer farback
        hide eyes onlayer back
        hide eyes2 onlayer back
        hide wood onlayer front
        hide rocks onlayer front
        hide door onlayer front
        show farback nightmare upstairs onlayer farback at Position(ypos=1125)
        show bg nightmare upstairs onlayer back at Position(ypos=1125)
        show knife nm leave onlayer back at Position(ypos=1125)
        show nightmare upstairs impatient onlayer front at Position(ypos=1125)
        sp "There we go, back with me where you belong! I thought you might have decided to break yourself just to spite me. It's better for you that you didn't.\n"
        voice "audio/voices/ch2/nightmare/_encounter/princess/77.flac"
        show nightmare upstairs blade look onlayer front
        sp "Now we can get back to business. For starters, we won't need this where we're going!\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/54.flac"
        play tertiary "audio/one_shot/knife_pickup.flac"
        queue tertiary "audio/final/Razor_SwordSwish_3.flac"
        hide knife onlayer back
        show nightmare upstairs blade toss anim onlayer front
        n "The Princess plucks the blade from the floor and tosses it through the door behind you. It vanishes into the inky black of the basement, never to be seen again.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/34a.flac"
        hero "I guess we're not stabbing her in the back.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/55.flac"
        n "{i}Sigh.{/i} I guess not.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/56.flac"
        n "I'm going to fix myself a stiff drink. If I'm about to watch you hand the world to her on a silver platter, I'd rather not be sober.\n"
        voice "audio/voices/ch2/nightmare/_encounter/princess/78.flac"
        sp "And now you open the door.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/35.flac"
        hero "There's nothing else for us to do.\n"
        menu:

            extend ""

            "{i}• [[Step into the world.]{/i}":
                jump nightmare_free_outside


    label nightmare_free_outside:
        $ achievement.grant("ACH_NIGHT_FREE")
        play audio "audio/one_shot/door_bedroom.flac"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/57.flac"
        hide farback onlayer farback
        hide bg onlayer back
        hide nightmare onlayer front
        show farback nightmare freedom door open onlayer farback at Position(ypos=1125)
        show bg nightmare freedom door open onlayer back at Position(ypos=1125)
        with fade
        n "The doorknob twists in your hand, revealing the forested path beyond the cabin. You bastard. You've actually done it. You've actually doomed everyone.\n"
        $ gallery_nightmare.unlock_item(4)
        $ gallery_nightmare.unlock_item(5)
        $ gallery_nightmare.unlock_item(6)
        $ gallery_nightmare.unlock_item(7)
        $ renpy.save_persistent()
        voice "audio/voices/ch2/nightmare/_encounter/princess/79.flac"
        stop music fadeout 15.0
        stop sound fadeout 20.0
        stop tertiary fadeout 20.0
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
        hide bg onlayer back
        hide farback onlayer back
        hide bg onlayer front
        show farback damsel outside onlayer farback at Position(ypos=1125)
        show bg damsel outside onlayer back at Position(ypos=1125)
        show mid damsel outside onlayer back at Position(ypos=1125)
        show fore damsel outside onlayer front at Position(ypos=1125)
        show quiet creep1 onlayer front at Position(ypos=1125)
        show nightmare freedom1 onlayer inyourface at Position(ypos=1125)
        with dissolve
        sp "It's so beautiful. I can't wait to ruin it.\n"
        voice "audio/voices/ch2/nightmare/_encounter/princess/80.flac"
        show quiet creep2 onlayer front at Position(ypos=1125)
        show nightmare freedom2 onlayer inyourface at Position(ypos=1125)
        with dissolve
        sp "But it's so cold, too. It's... itching against my skin.\n"
        show quiet creep3 onlayer front at Position(ypos=1125)
        show nightmare freedom3 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        truth "The Princess, exhausted, slumps to the ground.\n"
        voice "audio/voices/ch2/nightmare/_encounter/princess/81.flac"

        sp "Why is it so cold?\n"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        stop voice2 fadeout 3.0
        show arms nightmare1 onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.125)
        show arms nightmare2 onlayer front at Position(ypos=1125)
        show nightmare freedom4 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.125)
        hide nightmare onlayer inyourface
        show arms nightmare3 onlayer front at Position(ypos=1125)
        with dissolve
        $ renpy.pause(0.125)
        hide arms onlayer front
        show arms nightmare4 onlayer front at Position(ypos=1125)
        with dissolve
        $ renpy.pause(0.1025)
        hide arms onlayer front
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
            truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
        else:
            truth "You do not have an opportunity to respond. Something has taken her away, and it's left something else in her stead.\n"
        $ princess_free += 1
        $ princess_satisfy += 1
        $ current_princess = "nightmare"
        jump mirror_start
        # end

label nightmare_kill_join:
    voice "audio/voices/ch2/nightmare/_encounter/narrator/58.flac"
    play audio "audio/final/Assorted_Static_5.flac"
    play tertiary "audio/one_shot/footstep_run_medium.flac"
    show bg black big onlayer inyourface at Position(ypos=1125)
    show knife slice onlayer inyourface at yflip, Position(ypos=1125)
    with fade
    n "Your will concentrates into a single fine point, and you strike out against the Princess, ignoring the constant reminders of your breaking body.\n"
    $ default_mouse = "blood"
    play audio "audio/one_shot/knife_stab.flac"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/59.flac"
    hide bg onlayer inyourface
    hide knife onlayer inyourface
    show nightmare slay upstairs onlayer front at Position(ypos=1125)
    with dissolve
    n "She doesn't even move as the blade sinks into her heart.\n"
    voice "audio/voices/ch2/nightmare/_encounter/hero/36a.flac"
    hero "We did it. We actually did it!\n"
    voice "audio/voices/ch2/nightmare/_encounter/princess/82.flac"
    $ default_mouse = "default"
    show nightmare slay upstairs2 onlayer front at Position(ypos=1125)
    with dissolve
    sp "Hahahaha! You actually went for it! Oh you're going to regret this! I can be so much more terrible for you than I am now!\n"
    voice "audio/voices/ch2/nightmare/_encounter/hero/37.flac"
    hero "C-can she?\n"
    stop voice2 fadeout 1.0
    $ renpy.pause(1.0)
    voice "audio/voices/ch2/nightmare/_encounter/paranoid/33.flac"
    paranoid "We've already seen how she can change... heart. Lungs. Liver. Nerves...\n"
    play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop fadein 2.0
    voice "audio/voices/ch2/nightmare/_encounter/princess/83.flac"
    sp "You're not getting those stairs back. I'll see you when you finally decide to die.\n"
    $ achievement.grant("ACH_NIGHT_STUCK")
    $ blade_held = False
    $ default_mouse = "default"
    $ gallery_nightmare.unlock_item(10)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/nightmare/_encounter/narrator/60.flac"
    stop music fadeout 3.0
    play audio "audio/one_shot/collapse.flac"
    hide eyes onlayer back
    hide eyes2 onlayer back
    show nightmare slay downstairs dead onlayer front
    with dissolve
    n "She falls to the ground, unmoving.\n"
    jump nightmare_kill_join_late


label nightmare_kill_upstairs:
    $ nightmare_falling = True
    voice "audio/voices/ch2/nightmare/_encounter/narrator/58.flac"
    play audio "audio/final/Assorted_Static_5.flac"
    play tertiary "audio/one_shot/footstep_run_medium.flac"
    show bg black big onlayer inyourface at Position(ypos=1125)
    show knife slice onlayer inyourface at yflip, Position(ypos=1125)
    with fade
    n "Your will concentrates into a single fine point, and you strike out against the Princess, ignoring the constant reminders of your breaking body.\n"
    $ default_mouse = "blood"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/59.flac"
    play audio "audio/one_shot/knife_stab.flac"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/59.flac"
    if nightmare_made_it_upstairs:
        hide bg onlayer inyourface
        hide knife onlayer inyourface
        hide farback onlayer farback
        hide bg onlayer back
        hide nightmare onlayer front
        show bg nightmare freedom door onlayer back at Position(ypos=1125)
        show nightmare slay upstairs onlayer front at Position(ypos=1125)
        with dissolve
    else:
        hide bg onlayer inyourface
        hide knife onlayer inyourface
        hide farback onlayer farback
        hide bg onlayer back
        hide nightmare onlayer front
        hide nightmare onlayer front
        hide farback onlayer farback
        hide eyes onlayer back
        hide eyes2 onlayer back
        hide wood onlayer front
        hide rocks onlayer front
        hide door onlayer front
        show farback nightmare basement onlayer farback at Position(ypos=1125)
        show eyes nightmare stairs onlayer back at Position(ypos=1125)
        show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
        show steps nightmare stairs onlayer back at Position(ypos=1125)
        show nightmare slay upstairs onlayer front at Position(ypos=1125)
        with dissolve
    n "She doesn't even move as the blade sinks into her heart.\n"
    voice "audio/voices/ch2/nightmare/_encounter/hero/36a.flac"
    hero "We did it. We actually did it!\n"
    voice "audio/voices/ch2/nightmare/_encounter/princess/84.flac"
    if nightmare_made_it_upstairs:
        hide bg onlayer back
        hide nightmare onlayer front
        show farback nightmare upstairs onlayer farback at Position(ypos=1125)
        show bg nightmare upstairs onlayer back at Position(ypos=1125)
        show nightmare slay upstairs2 onlayer front at Position(ypos=1125)
        with dissolve
    else:
        show nightmare slay upstairs2 onlayer front at Position(ypos=1125)
    sp "Hahahaha! You actually went for it! Oh you're going to regret this! I can be so much more terrible for you than I am now!\n"
    voice "audio/voices/ch2/nightmare/_encounter/hero/37.flac"
    hero "Can she?\n"
    stop voice2 fadeout 1.0
    $ renpy.pause(1.0)
    voice "audio/voices/ch2/nightmare/_encounter/paranoid/33.flac"
    paranoid "We've already seen how she can change... heart. Lungs. Liver. Nerves...\n"
    play voice2 "audio/voices/ch2/nightmare/_encounter/paranoid/nm_loop_slow.ogg" loop fadein 2.0
    voice "audio/voices/ch2/nightmare/_encounter/narrator/61.flac"
    play audio "audio/final/Assorted_Static_5.flac"
    play tertiary "audio/one_shot/tackle.flac"
    show nightmare slay upstairs push onlayer front at Position(ypos=1125)
    n "In her final moments, the Princess lunges forward, tackling you, and you both plunge into the endless abyss of her basement labyrinth.\n"
    play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
    play sound "audio/final/Nightmare_Falling_1_Loop.flac" loop
    hide farback onlayer farback
    hide steps onlayer back
    hide bg onlayer inyourface
    hide knife onlayer inyourface
    hide farback onlayer farback
    hide bg onlayer back
    hide nightmare onlayer front
    scene bg black big onlayer inyourface at Position(ypos=1125)
    voice "audio/voices/ch2/nightmare/_encounter/narrator/fall_bonus.flac"
    n "As the two of you fall, you rip your blade from her chest, tightly clutching it in your hands.\n"
    voice "audio/voices/ch2/nightmare/_encounter/princess/85.flac"
    hide bg onlayer inyourface
    show farback falling forever onlayer farback at Position(ypos=1125)
    show nightmare slay falling onlayer front at Position(ypos=1125)
    with dissolve
    sp "Have fun falling forever! I'll see you when you finally decide to die.\n"
    voice "audio/voices/ch2/nightmare/_encounter/narrator/62.flac"
    hide eyes onlayer back
    hide eyes2 onlayer back
    show nightmare slay dead onlayer front
    with dissolve
    #n "She tears herself away from your blade, her body twisting from yours, tumbling away into the darkness.\n"
    n "She tears herself away from you and tumbles away into the darkness.\n"
    $ gallery_nightmare.unlock_item(8)
    $ gallery_nightmare.unlock_item(9)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/nightmare/_encounter/narrator/63.flac"
    $ achievement.grant("ACH_NIGHT_FALL")
    stop music fadeout 3.0
    hide nightmare onlayer front
    with dissolve
    n "You are alone. And you are falling. Forever. But you saved the world. You should be proud of yourself for seeing this through.\n"
    label nightmare_kill_join_late:
        stop voice2 fadeout 1.0
        $ renpy.pause(1.0)
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/34.flac"
        paranoid "Oh, I can stop now, can't I?\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/35.flac"
        paranoid "I can! Finally.\n"
        if nightmare_falling:
            voice "audio/voices/ch2/nightmare/_encounter/hero/38.flac"
            hero "Are, are we really gonna fall forever? Can't you narrate us some stairs out of here?\n"
        else:
            voice "audio/voices/ch2/nightmare/_encounter/hero/39.flac"
            hero "And now that she's gone, you can let us out of here, right?\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/36.flac"
        paranoid "But she was the one who controlled this place, wasn't she? And now she's dead. I don't like to think what that means for us.\n"
        if nightmare_falling:
            voice "audio/voices/ch2/nightmare/_encounter/narrator/64.flac"
            n "It means you're falling. Forever.\n"
        else:
            voice "audio/voices/ch2/nightmare/_encounter/narrator/65.flac"
            n "It means that you're stuck here. Forever.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/40.flac"
        hero "Oh no. Oh no no no no no. Oh no I hate this!\n"
        if nightmare_falling:
            voice "audio/voices/ch2/nightmare/_encounter/narrator/66.flac"
            n "You continue to fall.\n"
        else:
            voice "audio/voices/ch2/nightmare/_encounter/narrator/67.flac"
            n "Time passes.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/41.flac"
        hero "... forever's going to end eventually, right?\n"
        if nightmare_falling:
            voice "audio/voices/ch2/nightmare/_encounter/narrator/68.flac"
            n "No. It won't. That's the whole point of 'forever.' It doesn't end. You continue to fall, and you will only continue to fall.\n"
        else:
            voice "audio/voices/ch2/nightmare/_encounter/narrator/69.flac"
            n "No. It won't. That's the whole point of 'forever.' It doesn't end.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/42.flac"
        hero "I feel sick.\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/37.flac"
        paranoid "It doesn't have to be forever, though, does it?\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/43.flac"
        hero "... what do you mean?\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/38.flac"
        paranoid "We still have a way out clutched in our hands.\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/44.flac"
        hero "Are you suggesting we kill ourselves? Won't we be dead? ... I guess that hasn't stopped us before.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/70.flac"
        n "That's a terrible idea. You've already saved the entire world from ruin, why would you want to die?\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/39.flac"
        paranoid "Because right now, you don't want us to do that.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/71.flac"
        n "You're right! I don't!\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/40.flac"
        paranoid "But if we've already 'saved the world' then why does it matter if we die? Why do you care?\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/72.flac"
        n "I just do! I value life. Every life. Even yours. Especially yours.\n"
        voice "audio/voices/ch2/nightmare/_encounter/paranoid/41.flac"
        paranoid "Why?\n"
        voice "audio/voices/ch2/nightmare/_encounter/hero/45.flac"
        hero "What do you mean why? I think it's perfectly reasonable to value life.\n"
        voice "audio/voices/ch2/nightmare/_encounter/narrator/73.flac"
        n "Exactly. I don't have to answer that.\n"
        label nightmare_falling_forever:
            default nightmare_falling_come_back = False
            default nightmare_falling_company = False
            default nightmare_falling_drop = False
            default nightmare_falling_biology = False
            default nightmare_falling_fine = False
            default nightmare_falling_lonely = False
            default nightmare_falling_stuck = False
            default nightmare_falling_secret_count = 0
            menu:
                extend ""

                "{i}• (Explore) ''It's not like it matters if I die. I'll just come back again.''{/i}" if nightmare_falling_come_back == False:
                    $ nightmare_falling_come_back = True
                    if nightmare_1_forest_share_loop_insist:
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/74a.flac"
                        n "Ah yes, the whole 'looping' thing. How unfortunate. You were only supposed to be here once.\n"
                    else:
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/75.flac"
                        n "'Again?' That's unfortunate. You were only supposed to be here once.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/paranoid/42.flac"
                    paranoid "I don't like the way you said that. You knew this was a possibility, didn't you?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/76.flac"
                    n "Of course I did, though I'd rather hoped I was the first one. That explains a lot though.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/hero/46a.flac"
                    hero "Oh you bastard, how much are you not telling us?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/77.flac"
                    n "Plenty. But it's all in your best interest. And the world's. And mine.\n"
                    if nightmare_falling:
                        voice "audio/voices/ch2/nightmare/_encounter/hero/47a.flac"
                        hero "She's dead and we're falling forever. How could telling us your secrets possibly hurt anyone?\n"
                        #voice "audio/voices/ch2/nightmare/_encounter/hero/47.flac"
                        #hero "How could keeping secrets be in anyone's best interest? She's dead and we're falling forever. How could telling us your secrets possibly hurt anyone?\n"
                    else:
                        voice "audio/voices/ch2/nightmare/_encounter/hero/48a.flac"
                        hero "She's dead and we're stuck in her hellvoid forever. How could telling us your secrets possibly hurt anyone?\n"
                        #voice "audio/voices/ch2/nightmare/_encounter/hero/48.flac"
                        #hero "How could keeping secrets be in anyone's best interest? She's dead and we're stuck in her hellvoid forever. How could telling us your secrets possibly hurt anyone?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/78.flac"
                    n "It just can. Look, this world is saved, but if you 'start over', for all you know you're just putting another world in danger. You barely managed to land the killing blow here. What if you don't manage it next time?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/79.flac"
                    n "{i}Sigh.{/i} I've already said too much, really. You won't get another word out of me on the subject.\n"
                    jump nightmare_falling_forever


                "{i}• (Explore) ''Can you tell me your secrets now?''{/i}" if nightmare_falling_secret_count == 0 and nightmare_falling_come_back:
                    $ nightmare_falling_secret_count += 1
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/80.flac"
                    n "No.\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) ''How about now? Is it secret-time?''{/i}" if nightmare_falling_secret_count == 1:
                    $ nightmare_falling_secret_count += 1
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/81.flac"
                    n "Still no.\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) ''I'm going to wear you down eventually. You might as well spill those sweet-sweet secrets now. Then we'll have something else to talk about!''{/i}" if nightmare_falling_secret_count == 2:
                    $ nightmare_falling_secret_count += 1
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/82.flac"
                    n "You're not going to wear me down.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/hero/49.flac"
                    hero "Ooh, we should ask him one more time. He's on the cusp of sharing his secrets. I can feel it.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/83.flac"
                    n "I'm not.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/paranoid/43.flac"
                    paranoid "Either way, at least needling Him is something to do.\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) ''Secret?''{/i}" if nightmare_falling_secret_count == 3 or nightmare_falling_secret_count == 4:
                    if nightmare_falling_secret_count == 3:
                        $ nightmare_falling_secret_count += 1
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/84.flac"
                        n "The Narrator ignores you.\n"
                        voice "audio/voices/ch2/nightmare/_encounter/hero/50.flac"
                        hero "You can't just describe yourself ignoring us.\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/85.flac"
                        n "I can.\n"
                    else:
                        $ nightmare_falling_secret_count += 1
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/86.flac"
                        n "The Narrator continues to ignore you.\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) ''But I've got the best company I could ask for! You guys! What more do I need?''{/i}" if nightmare_falling_best_company == False:
                    default nightmare_falling_best_company = False
                    $ nightmare_falling_best_company = True
                    voice "audio/voices/ch2/nightmare/_encounter/paranoid/44.flac"
                    paranoid "Oh, you could do a lot better than us.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/87.flac"
                    n "Exactly. You'll be fine here. Just come up with a game or something to pass the time.\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) ''I don't know... falling forever doesn't seem too bad to me.''{/i}" if nightmare_falling_fine == False and nightmare_falling_biology == False and nightmare_falling:
                    $ nightmare_falling_fine = True
                    voice "audio/voices/ch2/nightmare/_encounter/hero/51.flac"
                    hero "You say that now, but let's see how we all feel after a week or a month or a year...\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) ''Am I not a creature of biology? Won't I starve or die of dehydration before forever happens?''{/i}" if nightmare_falling_biology == False:
                    $ nightmare_falling_biology = True
                    voice "audio/voices/ch2/nightmare/_encounter/hero/52.flac"
                    hero "That's a grim thought, isn't it?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/88.flac"
                    n "But I suppose you're right. You are a creature of biology. Something will happen to you before forever comes along.\n"
                    if nightmare_falling_drop == False and nightmare_falling:
                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/45.flac"
                        paranoid "We don't have to starve to death falling through an infinite void. You have our way out. Use it.\n"
                    elif nightmare_falling_drop == False:
                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/46.flac"
                        paranoid "We don't have to starve to death. You have our way out. Use it.\n"
                    else:
                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/47.flac"
                        paranoid "You really shouldn't have gotten rid of the blade. It was our way out! What were you thinking?\n"
                        voice "audio/voices/ch2/nightmare/_encounter/hero/53.flac"
                        hero "Now now, if we're going to be stuck here until we starve, we really shouldn't be at each other's throats.\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) ''Are you stuck here with us or are you capable of going... other places?''{/i}" if nightmare_falling_stuck == False:
                    $ nightmare_falling_stuck = True
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/89.flac"
                    n "I'm stuck here with you. I wish I weren't.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/paranoid/48.flac"
                    paranoid "Feeling's mutual.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/hero/54a.flac"
                    hero "At least we're all being honest!\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) ''I get it. You don't want us to die because you'd be lonely! How sweet.''{/i}" if nightmare_falling_stuck and nightmare_falling_lonely == False:
                    $ nightmare_falling_lonely = True
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/90a.flac"
                    n "Unlike you, I'm not capable of being lonely.\n"
                    voice "audio/voices/ch2/nightmare/_encounter/hero/55a.flac"
                    hero "Aw, sure you are! Give it some time without us and I'm sure you'll start feeling lonely.\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) [[Drop the blade.]{/i}" if nightmare_falling_drop == False and nightmare_falling:
                    $ nightmare_falling_drop = True
                    $ blade_held = False
                    $ default_mouse = "default"
                    voice "audio/voices/ch2/nightmare/_encounter/hero/56.flac"
                    hero "Oh no, what are you doing?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/91.flac"
                    n "You loosen your grip, and the blade tumbles through your open fingers. Now you're really falling forever. There's no way out now.\n"
                    if nightmare_falling_biology:
                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/49.flac"
                        paranoid "You mean other than starving...\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/92.flac"
                        n "Right. I mean other than that.\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) [[Take the blade from her body.]{/i}" if nightmare_falling_drop == False and nightmare_falling == False and blade_held == False:
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/bonus_2.flac"
                    $ blade_held = True
                    $ default_mouse = "blood"
                    play audio "audio/one_shot/knife_pickup.flac"
                    show nightmare slay downstairs dead empty onlayer front at Position(ypos=1125)
                    with dissolve
                    n "You remove the blade from the Princess' body. What, exactly, are you planning on doing with it?\n"
                    jump nightmare_falling_forever

                "{i}• (Explore) [[Throw the blade into the void.]{/i}" if nightmare_falling_drop == False and nightmare_falling == False and blade_held:
                    $ blade_held = False
                    $ default_mouse = "default"
                    $ nightmare_falling_drop = True
                    voice "audio/voices/ch2/nightmare/_encounter/hero/56.flac"
                    hero "Oh no, what are you doing?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/93.flac"
                    n "You tighten your grip and fling the blade as hard as you can into the void. It's gone. Now you're really stuck here forever. There's no way out now.\n"
                    if nightmare_falling_biology:
                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/49.flac"
                        paranoid "You mean other than starving...\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/92.flac"
                        n "Right. I mean other than that.\n"
                    jump nightmare_falling_forever

                "{i}• [[Slay yourself.]{/i}" if nightmare_falling_drop == False and blade_held:
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/94.flac"
                    n "{i}Sigh.{/i} I don't like this, but I suppose there's not much I can do to stop you, is there?\n"
                    voice "audio/voices/ch2/nightmare/_encounter/narrator/95.flac"
                    play audio "audio/one_shot/stab_goop.flac"
                    show player throat slit anim onlayer inyourface at Position(ypos=1125)
                    with dissolve
                    n "You raise the blade to your neck and slit your carotid artery.\n"
                    stop sound fadeout 5.0
                    stop secondary fadeout 5.0
                    stop tertiary fadeout 5.0
                    play audio "audio/final/Prisoner_SawingThrough_1.flac"
                    voice "audio/voices/ch2/nightmare/_encounter/paranoid/50.flac"
                    hide farback onlayer farback
                    hide nightmare onlayer front
                    hide farback onlayer farback
                    hide eyes onlayer back
                    hide eyes2 onlayer back
                    hide wood onlayer front
                    hide rocks onlayer front
                    hide bg onlayer back
                    hide player onlayer inyourface
                    scene bg black
                    paranoid "Here we go.\n"
                    if nightmare_falling_come_back:
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/96.flac"
                        n "You'd better get this right next time. Do you hear me? Don't blow it.\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/97.flac"
                    n "Everything goes dark, and you die.\n"
                    $ blade_held = False
                    $ default_mouse = "default"
                    $ wraith_source = "nightmare"
                    if nightmare_falling:
                        $ wraith_bonus_voice = "opportunist"
                    else:
                        $ wraith_bonus_voice = "cold"
                    jump wraith_start
                    # END

                "{i}• [[Wait.]{/i}":
                    if nightmare_falling_biology == False or nightmare_falling_drop == False:
                        if nightmare_falling:
                            voice "audio/voices/ch2/nightmare/_encounter/narrator/98.flac"
                            n "More time passes. You continue to fall.\n"
                        else:
                            voice "audio/voices/ch2/nightmare/_encounter/narrator/99.flac"
                            n "More time passes. You're still here.\n"
                        jump nightmare_falling_forever
                    else:
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/100.flac"
                        n "You wait, and then you wait for a little while longer. But eventually the thirst sets in. And the hunger. The darkness of this place prevents you from wholly grasping the context of passing time, but that doesn't stop it from passing, nor does it stop your biology from unraveling.\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/101.flac"
                        n "The only things you know for certain are that it's long, and that it hurts. The vastness of your suffering can't be adequately put into words.\n"
                        voice "audio/voices/ch2/nightmare/_encounter/paranoid/51.flac"
                        paranoid "We really shouldn't have tossed the blade...\n"
                        voice "audio/voices/ch2/nightmare/_encounter/narrator/102.flac"
                        stop sound fadeout 5.0
                        stop secondary fadeout 5.0
                        stop tertiary fadeout 5.0
                        hide farback onlayer farback
                        hide nightmare onlayer front
                        hide farback onlayer farback
                        hide eyes onlayer back
                        hide eyes2 onlayer back
                        hide wood onlayer front
                        hide rocks onlayer front
                        hide bg onlayer back
                        scene bg black
                        with Dissolve(5.0)
                        n "No, you really shouldn't have. But biology and time are immutable forces, and eventually, long before forever gets the chance to come, everything goes dark, and you die.\n"
                        if nightmare_falling_come_back:
                            voice "audio/voices/ch2/nightmare/_encounter/narrator/103.flac"
                            n "Don't muck it up next time. The Princess may be slain here, but she isn't slain There.\n"
                        $ blade_held = False
                        $ default_mouse = "default"
                        $ wraith_source = "nightmare"
                        if nightmare_falling:
                            $ wraith_bonus_voice = "opportunist"
                        else:
                            $ wraith_bonus_voice = "cold"
                        jump wraith_start
                        # END

return
