label stranger_1_start:
    default stranger_1_woods_share_loop = False

    $ trait_contrarian = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter stranger with fade
    show text _("{color=#FFFFFF00}Chapter 2. The Stranger.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)

    play sound "audio/looping/uncomfortable ambiance.ogg" loop
    play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
    play music "audio/_music/ch1/Fragmentation.flac" loop
    scene bg path walls onlayer farback at Position(ypos=1125)
    show mid path walls onlayer back at Position(ypos=1125)
    show front path walls onlayer front at Position(ypos=1125)
    show bg black
    #show loading_icon
    hide chapter
    hide text
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    $ gallery_stranger.unlock_gallery()
    $ gallery_zch1.unlock_item(14)
    $ renpy.save_persistent()
    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"

label stranger_1_woods:
    default stranger_1_forest_count = 0
    default stranger_1_forest_share_died = False
    default stranger_1_forest_share_loop = False
    default stranger_1_forest_princess_press = False
    default stranger_1_forest_share_loop_insist = False
    default stranger_1_forest_deja_vu = False
    default stranger_1_forest_deja_vu_follow_up = False
    default stranger_1_woods_walls = False
    default stranger_1_world_end_share = False
    menu:
        extend ""

        "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if stranger_1_woods_share_loop == False:
            $ stranger_1_woods_share_loop = True
            voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
            n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
            label stranger_1_no_memory:
                $ stranger_1_woods_share_loop = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_1.flac"
                contrarian "I don't know. I think it's more fun if He knows what we're thinking. He's like a captive audience.\n"
                if stranger_1_woods_walls:
                    voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_2.flac"
                    contrarian "He might have walled off everything but the path to the cabin, but I'm sure there's plenty of other ways we can ruin his day.\n"
                else:
                    voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_2a.flac"
                    contrarian "The entire world ending wasn't enough to get rid of us. I don't think there's much He can do other than object. I wonder what else we can do to ruin his day.\n"
                $ stranger_1_world_end_share = True
                voice "audio/voices/ch2/stranger/narrator/ch2_sn_1.flac"
                n "If by ruining my day you mean ruining everyone's day forever, then yes, I suppose there are plenty of ways you can pull that off.\n"
                voice "audio/voices/ch2/stranger/hero/ch2_sh_1.flac"
                hero "The world really did end last time, didn't it? We should be careful. For all we know we just got lucky.\n"
                voice "audio/voices/ch2/stranger/narrator/ch2_sn_2.flac"
                n "The world hasn't ended yet, and you are {i}never{/i} going to slay her with that attitude. Stuff those pathetic little voices to the back of your mind and stay focused on the task ahead.\n"
                jump stranger_1_woods

        "{i}• (Explore) Wait... hasn't this already happened?{/i}" if stranger_1_woods_share_loop == False:
            $ stranger_1_woods_share_loop = True
            voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
            n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
            jump stranger_1_no_memory

        "{i}• (Explore) Okay, no.{/i}" if stranger_1_woods_share_loop == False:
            $ stranger_1_woods_share_loop = True
            voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
            n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
            jump stranger_1_no_memory

        "{i}• (Explore) You aren't kidding. She actually ended the world last time, didn't she? What the hell is she?{/i}" if stranger_1_woods_share_loop == False:
            $ stranger_1_woods_share_loop = True
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_bonus.flac"
            n "Last time? Last I checked there wasn't any 'last time'. We've just met, you and I.\n"
            jump stranger_1_no_memory

        "{i}• (Explore) Oh, you bastard! You're in for it now. I'm wise to your tricks!{/i}" if stranger_1_woods_share_loop == False:
            $ stranger_1_woods_share_loop = True
            voice "audio/voices/ch2/prisoner/narrator/ch2_pn_7.flac"
            n "My tricks? What on earth are you talking about? We've just met for the first time.\n"
            jump stranger_1_no_memory

        "{i}• (Explore) But I died! The whole world ended! What am I doing here?{/i}" if stranger_1_woods_share_loop == False:
            $ stranger_1_woods_share_loop = True
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_3.flac"
            n "I can assure you that you're not dead, and that the Princess has yet to end the world, otherwise you wouldn't be here. And to answer your question, you're here to slay the Princess. I literally told you that a second ago.\n"
            jump stranger_1_no_memory

        "{i}• (Explore) Those walls weren't here last time! You can't just force me to go to the cabin.{/i}" if stranger_1_woods_walls == False:
            $ stranger_1_woods_walls = True
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_4b.flac"
            n "What are you talking about? I'm sure those walls have always been there. It makes sense if you think about it. If there weren't any walls in the woods, someone might have gotten lost. Or, heaven forbid, someone other than you might have stumbled onto the Princess.\n"
            if stranger_1_woods_share_loop == False:
                jump stranger_1_no_memory
            jump stranger_1_woods

        "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if stranger_1_forest_share_loop and (stranger_1_forest_deja_vu == False or (stranger_1_forest_deja_vu_follow_up)) and stranger_1_forest_share_loop_insist == False:
            $ stranger_1_forest_share_loop_insist = True
            $ stranger_1_forest_count += 1
            voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
            n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
            voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
            n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_5.flac"
            n "You said the world ended, right? I'm assuming that only happened because you didn't listen to me, and you should take that as more than enough evidence that I'm telling the truth about the Princess.\n"
            voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_3.flac"
            contrarian "For all we know, the world just happened to end on its own.\n"
            voice "audio/voices/ch2/stranger/hero/ch2_sh_2.flac"
            hero "But He's right. It did end. And what are the odds that something {i}else{/i} ended it?\n"
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_6.flac"
            n "Of course she was the one who ended it. And I believe your other question was something along the lines of 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
            voice "audio/voices/ch2/stranger/hero/ch2_sh_3.flac"
            hero "What do you mean? Of course there weren't any consequences. Sure, the world ended, but now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
            voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
            n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
            voice "audio/voices/ch2/stranger/hero/ch2_sh_4.flac"
            hero "Are you saying that everyone from the first time around is still dead?\n"
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_7.flac"
            n "I'm saying it's possible.\n"
            voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_4.flac"
            contrarian "Who cares? If that's the case, there's got to be {i}millions{/i} of worlds out there. What does one of them ending even matter?\n"
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_8.flac"
            n "Of course it matters! There were people there, and now they're gone! ... at least in this purely hypothetical scenario.\n"
            voice "audio/voices/ch2/stranger/hero/ch2_sh_5.flac"
            hero "I have to agree with him. On the off chance this is how things work, we should take this scenario a little more seriously.\n" id stranger_1_no_memory_a3e6e490
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_9.flac"
            n "Thank you.\n"
            jump stranger_1_woods

        "(Lie) Yep. Okay. Heading to the cabin now where I'm definitely going to slay that Princess.":
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_10.flac"
            n "You know I can tell when you're lying, right? Please take this seriously. I'm begging you.\n"
            jump cabin_arrival_stranger_1_menu

        "{i}• Yeah, yeah. I get it. I'm going to the cabin.{/i}":
            jump cabin_arrival_stranger_1_menu

        "{i}• [[Silently proceed to the cabin.]{/i}" if stranger_1_forest_count == 0:
            jump cabin_arrival_stranger_1_menu

        "{i}• ''If I can't run away from the cabin, then I'm just staying here in the woods. Forever.'' [[Stay in the woods. Forever.]{/i}" if mound_can_attempt_flee and loops_finished >= 1:
            if loops_finished >= 2:
                $ mound_can_attempt_flee = False
                voice "audio/voices/mound/bonus/flee.flac"
                mound "You have already committed to my completion. You cannot go further astray.\n"
                jump stranger_1_woods
            voice "audio/voices/ch2/stranger/contrarian/bonus1.flac"
            contrarian "Oooh, that's clever! A little boring, though.\n"
            voice "audio/voices/ch2/stranger/narrator/bonus1.flac"
            n "It's extremely boring.\n"
            voice "audio/voices/ch2/stranger/hero/bonus1.flac"
            hero "Can we really do that? Can we really just do nothing?\n"
            voice "audio/voices/ch2/stranger/narrator/bonus2.flac"
            n "No, you can't just do nothing. You have to do {i}something{/i}.\n"
            voice "audio/voices/ch2/stranger/contrarian/bonus2.flac"
            contrarian "All right! So it's decided. Even if it's boring, we're going to do nothing. Forever!\n"
            stop sound fadeout 20.0
            stop music fadeout 20.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
            voice "audio/voices/ch3/clarity/narrator/15a.flac"
            show quiet creep1 onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            voice "audio/voices/ch3/clarity/narrator/15a.flac"
            n "Congratulations, you continue to waste everyone's time and do nothing... wait, can you still hear me? Everything is getting fuzzy...\n"
            show quiet creep2 onlayer inyourface
            with Dissolve(1.0)
            voice "audio/voices/ch2/stranger/hero/bonus2.flac"
            hero "What is that weird feeling? It's like I'm barely even here anymore.\n"
            show quiet creep3 onlayer inyourface
            with Dissolve(1.0)
            voice "audio/voices/ch2/stranger/contrarian/bonus3.flac"
            contrarian "Well, it's not nothing, that's for sure. Does that mean we messed up?\n"
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

label cabin_arrival_stranger_1_menu:
    play audio "audio/one_shot/footsteps_hike_short.flac"
    $ quick_menu = False
    hide bg onlayer farback
    hide mid onlayer back
    hide front onlayer front
    show bg black
    with fade
    scene skyline cabin onlayer farback at Position(ypos = 1080)
    show walls cabin onlayer back at Position(ypos=1100)
    show midground cabin onlayer front at Position(ypos = 1140)
    show foreground cabin onlayer inyourface at Position(ypos = 1120)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/woods/narrator/script_n_38.flac"
    n "A warning, before you go any further...\n"
    voice "audio/voices/ch1/woods/narrator/script_n_62.flac"
    n "She will lie, she will cheat, and she will do everything in her power to stop you from slaying her. Don't believe a word she says.\n"
    voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_5.flac"
    contrarian "If we're stuck going in there, maybe we {i}should{/i} believe her. Maybe she isn't a liar.\n"
    voice "audio/voices/ch2/stranger/narrator/ch2_sn_11.flac"
    n "Ignore him. He's just being difficult for the sake of it.\n"
    voice "audio/voices/ch2/stranger/hero/ch2_sh_6.flac"
    hero "Let's keep an open mind.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            $ quick_menu = False
            play audio "audio/one_shot/enter_cabin_audio.flac"
            hide skyline onlayer farback
            hide bg onlayer back
            hide midground onlayer front
            hide walls onlayer back
            hide foreground onlayer inyourface
            # make cutscene for walls
            stop sound fadeout 1.0
            stop music fadeout 1.0
            scene bg black
            #show loading_icon
            with fade

    if persistent.quick_menu:
        $ quick_menu = True
    jump stranger_1_cabin_start
