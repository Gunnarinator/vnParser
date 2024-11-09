label beast_2_start:

    # starting things up

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False

    # combination — hunted + stubborn (reflection of adversary - if you try fighting)
    # combination — hunted + skeptic (if you try talking)
    $ current_princess = "den"
    $ den_encountered = True

    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    scene chapter den with fade
    show text _("{color=#FFFFFF00}Chapter Three. The Den.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    scene bg black

    if persistent.quick_menu:
        $ quick_menu = True

    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    play secondary "audio/looping/STP_jungle_loop.ogg" loop fadein 1.0
    play music "audio/_music/ch3/den/The Den Intro.flac"
    queue music "audio/_music/ch3/den/The Den Loop.flac" loop
    scene farback den woods onlayer farback at Position(ypos=1125)
    show bg den woods onlayer back at Position(ypos=1125)
    show fore den woods onlayer front at Position(ypos=1125)
    with fade
    $ gallery_den.unlock_gallery()
    $ renpy.save_persistent()
    # FAST
    voice "audio/voices/ch3/den/narrator/1.flac"
    n "You're on a path in the woods—\n{w=1.32}{nw}"
    show screen disableclick(0.5)
    if trait_stubborn:
        voice "audio/voices/ch3/den/stubborn/1.flac"
        stubborn "Yeah. We are. And this time we're not going to run until we die. We're taking her head-on, and we're winning.\n"
        voice "audio/voices/ch3/den/hunted/1.flac"
        hunted "You {i}felt{/i} her. She didn't have a soft underbelly. She didn't have blindspots. What could we have done that would have saved us from her hunger.\n"
        voice "audio/voices/ch3/den/stubborn/2.flac"
        stubborn "When someone tries to make you dead, you have to hit them back. You have to show them your authority. There's nothing worse than a bully that thinks they own you.\n"
    if trait_skeptic:
        voice "audio/voices/ch3/den/skeptic/1.flac"
        skeptic "That didn't work. We're going in with a plan this time. We're not getting stuck in another loop, just acting on instinct. We're stuck in a big enough loop as it is.\n"
        voice "audio/voices/ch3/den/hunted/2.flac"
        hunted "Instinct was keeping us alive.\n"
        voice "audio/voices/ch3/den/skeptic/2.flac"
        skeptic "Until it wasn't.\n"
        voice "audio/voices/ch3/den/hero/1.flac"
        hero "So what are we supposed to do?\n"

    voice "audio/voices/ch3/den/narrator/2.flac"
    n "Great. So you've been here before. That doesn't bode well. You're not supposed to have been here before, this is supposed to be one-and-done.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/den/stubborn/3.flac"
        stubborn "Oh, shut up! It bodes fine. You're the reason we're stuck in this shit situation, and now I have to do the hard work of dragging us out.\n"
        voice "audio/voices/ch3/den/narrator/3.flac"
        n "And how do you intend to do that?\n"
        voice "audio/voices/ch3/den/stubborn/4.flac"
        stubborn "We're going to fight her, and we're going to win. There's a reason she slinks around in the shadows.\n"
        voice "audio/voices/ch3/den/narrator/4.flac"
        n "Well, no complaints here.\n"
        voice "audio/voices/ch3/den/hero/2.flac"
        hero "Now hold on, we're not just going to let the fact that He knows things about this whole looping situation go, are we?\n"
        voice "audio/voices/ch3/den/stubborn/5.flac"
        stubborn "He's not important. He can have his secrets for all I care. She's killed us twice now, that's enough of a reason for us to want her dead.\n"
    else:
        voice "audio/voices/ch3/den/skeptic/3.flac"
        skeptic "So you know more than you're letting on.\n"
        voice "audio/voices/ch3/den/hero/3.flac"
        hero "Yeah, what he said!\n"
        voice "audio/voices/ch3/den/narrator/5.flac"
        n "Of course I do, but believe me, it's in your best interests. The more you know about the Princess, the more difficult your task will be.\n"
        voice "audio/voices/ch3/den/skeptic/4.flac"
        skeptic "And why is that?\n"
        voice "audio/voices/ch3/den/narrator/6.flac"
        n "Having me explain why would defeat the whole purpose. There are simply some things I'm not allowed to tell you, it's a hard rule.\n"
        voice "audio/voices/ch3/den/skeptic/5.flac"
        skeptic "And whose rule is it? Who's telling you to boss us around? We've died twice already. And if you want us to stay alive this time, it's in your best interests to give us an edge.\n"
        voice "audio/voices/ch3/den/narrator/7.flac"
        n "It's my rule, and this conversation is over.\n"

label beast_2_path_menu:
    default beast_2_plan = False
    default beast_2_path_different = False
    default beast_2_answers = False
    default beast_2_leave = False
    menu:

        extend ""

        "{i}• (Explore) Okay. What's the plan?{/i}" if beast_2_plan == False:
            $ beast_2_plan = True
            if trait_stubborn:
                voice "audio/voices/ch3/den/stubborn/6.flac"
                stubborn "Like I said, we're going to fight her.\n"
                voice "audio/voices/ch3/den/hunted/3.flac"
                hunted "But we're so small.\n"
                voice "audio/voices/ch3/den/stubborn/7.flac"
                stubborn "We don't actually know how big she is. We just know she wants us to think she's big. And if she is going to treat us like prey again, then she is sorely underestimating us. One good wallop. That's all we need to put her on the defensive.\n"
            else:
                label beast_2_skeptic_plan_join:
                    voice "audio/voices/ch3/den/skeptic/6.flac"
                    skeptic "She spent as much time as she could in the shadows. So we're going to draw her out.\n"
                    voice "audio/voices/ch3/den/hunted/4.flac"
                    hunted "But she's fast. And she's clever.\n"
                    voice "audio/voices/ch3/den/skeptic/7.flac"
                    skeptic "We're clever, too. So this time we're not going to let her cut off our escape. We're gonna lead her to the stairs ourselves.\n"
                    voice "audio/voices/ch3/den/skeptic/8.flac"
                    skeptic "It'll be a lot easier to deal with her once we can actually see what she is.\n"
                    voice "audio/voices/ch3/den/narrator/8.flac"
                    n "But you already know what she is. She's a Princess.\n"
                    voice "audio/voices/ch3/den/hero/4.flac"
                    hero "Yeah. Right.\n"
                    voice "audio/voices/ch3/den/skeptic/9.flac"
                    skeptic "A Princess we couldn't see, and one that had big sharp teeth, too. How about you stick to describing things and we'll stick to doing our job.\n"
                    voice "audio/voices/ch3/den/narrator/9.flac"
                    n "Sharp teeth...?\n"
                    if beast_2_plan == False:
                        jump beast_2_exterior_menu
            jump beast_2_path_menu

        "{i}• (Explore) The path is different than it was before.{/i}" if beast_2_path_different == False:
            $ beast_2_path_different = True
            if trait_skeptic:
                voice "audio/voices/ch3/den/skeptic/10.flac"
                skeptic "You're right. This is different, isn't it?\n"
                voice "audio/voices/ch3/den/hero/5.flac"
                hero "I'm starting to lose track of things myself.\n"
            voice "audio/voices/ch3/den/hunted/5.flac"
            hunted "Ground is ground. It doesn't matter what shape it takes. We'll adapt.\n"
            voice "audio/voices/ch3/den/narrator/10.flac"
            n "If it looks different that's because the situation has started to spiral out of everyone's control. So please, disavow yourself of the notion that you can just come back here and fix this place if you manage to make a mess, before that line of thinking leaves you yet another world in ruin.\n"
            voice "audio/voices/ch3/den/narrator/11.flac"
            n "Though as evidenced by you dying—twice—it's safe to assume the fates of the worlds you've left behind don't concern you very much.\n"
            voice "audio/voices/ch3/den/narrator/12.flac"
            n "Consider this your last opportunity to make things right. For you, and for the rest of existence. But especially for you.\n"
            if trait_stubborn:
                voice "audio/voices/ch3/den/stubborn/8.flac"
                stubborn "We don't need your pep-talk. I'll make sure we pull this off.\n"
            else:
                voice "audio/voices/ch3/den/skeptic/11.flac"
                skeptic "Clearly, we're not getting anything out of him.\n"
            jump beast_2_path_menu

        "{i}• (Explore) I want answers. What is going on here? What do you know that you're not telling me?{/i}" if beast_2_answers == False:
            $ beast_2_answers = True
            if trait_skeptic:
                voice "audio/voices/ch3/den/narrator/13.flac"
                n "Like I said, I've told you as much as I can without putting you at a disadvantage.\n"
            else:
                voice "audio/voices/ch3/den/narrator/14.flac"
                n "I've told you as much as I can without putting you at a disadvantage.\n"
            if trait_stubborn:
                voice "audio/voices/ch3/den/narrator/15.flac"
                n "If anything, I've told you too much. Like that grumbling voice said just a moment ago: you've already died by her hands twice. You shouldn't need much else in the way of motivation.\n"
            else:
                voice "audio/voices/ch3/den/narrator/16.flac"
                n "If anything, I've told you too much. You've already died by her hands twice. You shouldn't need much in the way of motivation.\n"
            jump beast_2_path_menu

        "{i}• (Explore) What if we just leave? What happens then?{/i}" if beast_2_leave == False:
            $ beast_2_leave = True
            if trait_skeptic:
                voice "audio/voices/ch3/den/skeptic/12.flac"
                skeptic "It doesn't seem like she can escape on her own.\n"
            else:
                voice "audio/voices/ch3/den/hero/6.flac"
                hero "Yeah, she was still there last time. I'm not so sure she can free herself without our help.\n"
            voice "audio/voices/ch3/den/narrator/17a.flac"
            n "Maybe not quickly, but it's inevitable. That cabin won't last forever.\n"
            if trait_skeptic:
                voice "audio/voices/ch3/den/skeptic/13.flac"
                skeptic "And she will?\n"
                voice "audio/voices/ch3/den/narrator/18.flac"
                n "Forget I said anything. Just treat this with the urgency it deserves.\n"
            jump beast_2_path_menu

        "{i}• No matter what happens next, it seems like all our answers are in the cabin. Let's see this through. [[Proceed to the cabin.]{/i}":
            jump beast_2_exterior

        "{i}• [[Silently proceed to the cabin.]{/i}":
            jump beast_2_exterior

        "{i}• I'm done with this. Bye! [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
            if loops_finished >= 2:
                $ mound_can_attempt_flee = False
                voice "audio/voices/mound/bonus/flee.flac"
                mound "You have already committed to my completion. You cannot go further astray.\n"
                jump beast_2_path_menu
            $ caught_origin_ch3 = True
            $ caught_origin_current = "beast2"
            if trait_stubborn:
                voice "audio/voices/ch3/den/stubborn/9.flac"
                stubborn "Coward! Deserter!\n"
            if trait_skeptic:
                voice "audio/voices/ch3/den/skeptic/14.flac"
                skeptic "That's another strategy. No complaints here.\n"
            voice "audio/voices/ch3/den/hunted/6.flac"
            hunted "Turning our back to her? Always a mistake.\n"
            voice "audio/voices/ch3/den/narrator/19.flac"
            play audio "audio/one_shot/footsteps_hike_short.flac"
            show farback den woods onlayer farback at flip, zoom_in
            show bg den woods onlayer back at flip, zoom_in
            show fore den woods onlayer front at flip, zoom_in
            with fade
            n "Are you serious?! Fine. You walk away from the the cabin. We'll see how that goes for you.\n"
            jump caught_start

label beast_2_exterior:
    $ gallery_den.unlock_item(1)
    $ renpy.save_persistent()
    play audio "audio/one_shot/footsteps_hike_short.flac"
    $ quick_menu = False
    hide farback onlayer farback
    hide bg onlayer back
    hide fore onlayer front
    scene bg black
    with fade
    scene farback den ext onlayer farback at Position(ypos=1125)
    show bg den ext onlayer back at Position(ypos=1125)
    show fore den ext onlayer front at Position(ypos=1125)
    with fade

    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/den/narrator/20.flac"
    n "You make your way down to the cabin. Your fated confrontation awaits. You know what to do.\n"
    if beast_2_plan:
        if trait_stubborn:
            label beast_2_stubborn_plan_join:
                voice "audio/voices/ch3/den/stubborn/10.flac"
                stubborn "We've already been over the plan.\n"
                voice "audio/voices/ch3/den/hero/7.flac"
                hero "I'm not sure that 'use violence' counts as a plan.\n"
                voice "audio/voices/ch3/den/stubborn/11.flac"
                stubborn "It's a better plan than you had last time.\n"
                voice "audio/voices/ch3/den/hunted/7.flac"
                hunted "I don't like this. But I'll try to keep us breathing.\n"
        else:
            voice "audio/voices/ch3/den/skeptic/15.flac"
            skeptic "All right. We've been over the plan. Goad her out of the shadows. Make her show herself.\n"
            voice "audio/voices/ch3/den/hunted/8.flac"
            hunted "And what if she doesn't want to be seen?\n"
            voice "audio/voices/ch3/den/skeptic/16.flac"
            skeptic "We'll figure out a way to make it happen.\n"
            voice "audio/voices/ch3/den/hero/8.flac"
            hero "And if that doesn't make her any easier to fight?\n"
            voice "audio/voices/ch3/den/skeptic/17.flac"
            skeptic "It will. It's always easier to fight what you can see. No matter how big or toothy she might be.\n"

    else:
        voice "audio/voices/ch3/den/hero/9.flac"
        hero "So... we need a plan.\n"
        if trait_stubborn:
            jump beast_2_stubborn_plan_join
        else:
            voice "audio/voices/ch3/den/skeptic/18.flac"
            skeptic "We've been over the plan. Goad her out of the shadows. Make her show herself.\n"
            voice "audio/voices/ch3/den/hunted/8.flac"
            hunted "And what if she doesn't want to be seen?\n"
            voice "audio/voices/ch3/den/skeptic/19.flac"
            skeptic "We'll figure out a way to make it happen.\n"
            voice "audio/voices/ch3/den/hero/10.flac"
            hero "And if that doesn't make her any easier to fight?\n"
            voice "audio/voices/ch3/den/skeptic/17.flac"
            skeptic "It will. It's always easier to fight what you can see. No matter how big or toothy she might be.\n"
            jump beast_2_skeptic_plan_join

    label beast_2_exterior_menu:
        menu:
            extend ""

            "{i}• [[Proceed into the cabin.]{/i}":
                play audio "audio/one_shot/door_bedroom.flac"
                $ quick_menu = False
                hide farback onlayer farback
                hide bg onlayer back
                hide fore onlayer front
                jump beast_2_interior

label beast_2_interior:
    $ gallery_den.unlock_item(2)
    $ renpy.save_persistent()
    scene farback den cabin onlayer farback at Position(ypos=1125)
    show bg den cabin onlayer back at Position(ypos=1125)
    show knife den cabin onlayer back at Position(ypos=1125)
    show mirror den cabin onlayer back at Position(ypos=1125)
    with fade

    if persistent.quick_menu:
        $ quick_menu = True

    voice "audio/voices/ch3/den/narrator/21.flac"
    n "The interior is dark and overgrown. Vines and brush obscure so much of the place that, had you not seen the exterior, you might not have noticed this was a cabin at all.\n"
    voice "audio/voices/ch3/den/narrator/22.flac"
    n "The only 'furniture' of note, if you could call it that, is a knotted stump, a pristine blade embedded in its exposed rings.\n"
    voice "audio/voices/ch3/den/narrator/23.flac"
    n "The blade is your implement. You'll need it if you're going to do this right.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/den/stubborn/12.flac"
        stubborn "Take it. We're not fighting a monster without a blade. Even if it's not a very big one.\n"
    elif beast_1_cabin_mirror_ask == False and beast_1_cabin_mirror_approached == False and trait_skeptic == False:
        voice "audio/voices/ch3/den/hero/11.flac"
        hero "Take it. We already know she's violent, there are only upsides to having something sharp with us.\n"
    if beast_1_cabin_mirror_ask or beast_1_cabin_mirror_approached:
        if trait_skeptic:
            voice "audio/voices/ch3/den/skeptic/20.flac"
            skeptic "Of course that damn mirror's back, and of course He's not saying anything about it. Why is it following us?\n"
        else:
            voice "audio/voices/ch3/den/hero/12.flac"
            hero "Great, that mirror's back. And it's where the door is supposed to be.\n"

    else:
        if trait_skeptic:
            voice "audio/voices/ch3/den/skeptic/21.flac"
            skeptic "If there's a way forward, that mirror is blocking it off.\n"
        else:
            voice "audio/voices/ch3/den/hero/13.flac"
            hero "Is no one going to mention the mirror?\n"
    voice "audio/voices/ch3/den/narrator/24.flac"
    n "What are you talking about? There is no mirror. There's just the stump and a narrow tunnel that leads to the basement.\n"
    voice "audio/voices/ch3/den/hunted/9.flac"
    hunted "He isn't tricking us. Can't you feel the wind? It's telling us there's a hole in that wall. Our eyes deceive us.\n"
    if trait_skeptic:
        voice "audio/voices/ch3/den/skeptic/22.flac"
        skeptic "Then either way, we need to investigate. Might as well get started.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/den/stubborn/13.flac"
        stubborn "If that mirror's blocking our way, just smash it and be done with it.\n"


    label beast_2_cabin_menu:
        default beast_2_blade_taken = False
        menu:
            extend ""

            "{i}• (Explore) [[Take the blade.]{/i}" if beast_2_blade_taken == False:
                $ beast_2_blade_taken = True
                voice "audio/voices/ch3/den/hunted/10.flac"
                hunted "Yes. Take the steel claw.\n"
                $ blade_held = True
                $ default_mouse = "blade"
                play audio "audio/one_shot/knife_pickup.flac"
                voice "audio/voices/ch3/den/narrator/25.flac"
                hide knife onlayer back with dissolve
                n "You pull the blade from the stump, gripping it tight. It would be difficult to slay the Princess and save the world without a weapon.\n"
                if trait_skeptic:
                    voice "audio/voices/ch3/den/skeptic/23.flac"
                    skeptic "Odds are we'll need it. Thanks for not putting us in a bad spot.\n"
                else:
                    voice "audio/voices/ch3/den/stubborn/14.flac"
                    stubborn "Good. One step closer to ending this.\n"
                jump beast_2_cabin_menu

            "{i}• [[Approach the mirror.]{/i}":
                if beast_2_blade_taken == False:
                    if trait_skeptic:
                        voice "audio/voices/ch3/den/skeptic/24.flac"
                        skeptic "You really think being unarmed is best? I hope you know what you're doing. But let's not forget that it's up here if things go south.\n"
                    else:
                        voice "audio/voices/ch3/den/stubborn/15.flac"
                        stubborn "I don't know what you're planning, but you're making my job a hell of a lot harder right now.\n"
                    voice "audio/voices/ch3/den/hunted/11a.flac"
                    hunted "The steel claw makes us sloppy. Too confident. We'll be faster without it.\n"
                play audio "audio/one_shot/footsteps_hike_short.flac"
                voice "audio/voices/ch3/den/narrator/26.flac"
                hide farback onlayer farback
                hide bg onlayer back
                hide knife onlayer back
                hide mirror onlayer back
                scene bg den close onlayer back at Position(ypos=1125)
                if blade_held == False:
                    show knife den close onlayer back at Position(ypos=1125)
                show mirror den close onlayer back at Position(ypos=1125)
                with dissolve
                n "You step forward, approaching the small hole that leads to the basement, hesitating before you enter the Princess' lair.\n"
                if trait_skeptic:
                    voice "audio/voices/ch3/den/skeptic/25.flac"
                    skeptic "Haven't you been paying attention? We're not hesitating, this supposed hole is blocked by that old mirror.\n"
                else:
                    voice "audio/voices/ch3/den/stubborn/16.flac"
                    stubborn "You heard Him. Stop hesitating and smash that antique.\n"
                voice "audio/voices/ch3/den/hunted/12.flac"
                hunted "That mirror isn't part of this place. It's seeped through from... somewhere else.\n"
                voice "audio/voices/ch3/den/narrator/27.flac"
                n "'It,' if there even is an 'it,' is a hallucination. Like you said, you've been here twice before. Your mind was bound to start playing tricks on you eventually.\n"
                if beast_1_cabin_mirror_approached:
                    voice "audio/voices/ch3/den/hero/14.flac"
                    hero "It went away after we reached out to it last time. Might as well try wiping it clean again, what's the harm?\n"
                else:
                    voice "audio/voices/ch3/den/hero/15.flac"
                    hero "It's so grimy. Maybe we can wipe it clean and finally get a look at ourselves.\n"

                menu:
                    extend ""

                    "{i}• [[Wipe the mirror clean.]{/i}":
                        voice "audio/voices/ch3/den/narrator/28.flac"
                        #show player wall onlayer front at Position(ypos=1125) with dissolve
                        hide mirror onlayer back
                        n "You reach forward and wave your hand over the open hole leading to the basement.\n"

                    "{i}• [[Smash it.]{/i}" if trait_stubborn:
                        default beast_2_smash_attempt = False
                        $ beast_2_smash_attempt = True
                        voice "audio/voices/ch3/den/narrator/29.flac"
                        show player den close onlayer front at Position(ypos=1125)
                        with dissolve
                        $ renpy.pause(0.1)
                        voice sustain
                        play audio "audio/one_shot/collapse.flac"
                        hide player onlayer front
                        hide knife onlayer back
                        hide bg onlayer back
                        hide mirror onlayer back
                        scene bg black with dissolve
                        with dissolve
                        n "You bring your fist crashing down into the open hole leading to the basement, throwing yourself off-balance and tumbling headlong into the pitch black.\n"
                        jump beast_2_stairs

                voice "audio/voices/ch3/den/hunted/13.flac"
                hunted "See? Nothing! Tricks of the eye. No one sense can be trusted on its own.\n"
                $ quick_menu = False
                if beast_2_smash_attempt:
                    hide player onlayer front
                    hide knife onlayer back
                    hide bg onlayer back
                    scene bg black with dissolve
                    jump beast_2_stairs
                play audio "audio/one_shot/footsteps_hike_short.flac"
                hide player onlayer front
                hide knife onlayer back
                hide bg onlayer back
                scene bg black with dissolve
                voice "audio/voices/ch3/den/narrator/30.flac"
                n "You step forward into the darkness.\n"
                $ current_run_mirror_comment = True
                jump beast_2_stairs

label beast_2_stairs:
    $ quick_menu = False
    scene bg den stairs onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/den/narrator/31.flac"
    n "If there were once stairs leading into the basement, there is nothing left to attest to their existence now. There is only a long tunnel of packed earth, growing more narrow as you descend.\n"
    voice "audio/voices/ch3/den/narrator/32.flac"
    n "It smells of mold and decay. The damp walls leave streaks of dirt along your body as you're forced to hunch, then finally squat down on all fours in order to continue. If the Princess lives here, slaying her is probably doing her a favor.\n"
    play audio "audio/one_shot/footstep_mines.flac"
    voice "audio/voices/ch3/den/narrator/33.flac"
    show bg den stairs onlayer back at spectre_small_zoom
    n "As you crawl forward on hands and knees, you're met only with the sounds of ambient earth. No voice slinks confidently up the stairs. No entity threatens violence or pleads for safety.\n"
    voice "audio/voices/ch3/den/hunted/14.flac"
    hunted "Stay quiet. Don't give her a sound.\n"
    menu:
        extend ""

        "{i}• ''We have unfinished business.''{/i}":
            label beast_2_stairs_comment:
                voice "audio/voices/ch3/den/narrator/34.flac"
                n "The Princess leaves your remark unanswered.\n"
                voice "audio/voices/ch3/den/hunted/15.flac"
                hunted "See? She knows. We have to be like her. Focused. Present. Patient.\n"
                if trait_skeptic:
                    voice "audio/voices/ch3/den/skeptic/26.flac"
                    skeptic "I suppose it'll take a little more than words to coax her out. Let's keep going.\n"
                else:
                    voice "audio/voices/ch3/den/stubborn/17.flac"
                    stubborn "We're past the point of words, anyway. This is a conversation that can only be had with hard steel and sharp teeth.\n"
                voice "audio/voices/ch3/den/narrator/35.flac"
                $ quick_menu = False
                play audio "audio/one_shot/footstep_mines.flac"
                hide bg onlayer back
                with fade
                n "You put the voices to the back of your mind and proceed down the 'stairs.'\n"
                jump beast_2_basement

        "{i}• ''We should talk.''{/i}":
            jump beast_2_stairs_comment

        "{i}• ''We don't have to fight. I'm ready to let you out of here.''{/i}":
            jump beast_2_stairs_comment

        "{i}• (Lie) ''We don't have to fight. I'm ready to let you out of here.''{/i}":
            jump beast_2_stairs_comment

        "{i}• [[Say nothing, and silently proceed down the 'stairs.']{/i}":
            voice "audio/voices/ch3/den/narrator/36.flac"
            $ quick_menu = False
            play audio "audio/one_shot/footstep_mines.flac"
            hide bg onlayer back
            with fade
            n "You say nothing, maintaining the silence as you carefully make your way down into the basement.\n" id beast_2_stairs_comment_f63c5df5
            jump beast_2_basement

label beast_2_basement:
    voice "audio/voices/ch3/den/narrator/37.flac"
    if persistent.quick_menu:
        $ quick_menu = True
    scene bg den basement onlayer farback at Position(ypos=1125)
    with fade
    n "The basement is dark and cavernous. A gaping maw, threatening to swallow you whole. There is no light here, save for what little starlight has managed to filter down the tunnel, and though you can't see the vastness of the space, you can feel it. You're exposed.\n"
    if trait_stubborn:
        if blade_held:
            voice "audio/voices/ch3/den/stubborn/18.flac"
            stubborn "It doesn't matter if we can't see down here. We know where she is.\n"
        else:
            voice "audio/voices/ch3/den/stubborn/19.flac"
            stubborn "It doesn't matter if we can't see down here. We know where she is. It would be better with a blade, but we'll make do.\n"
    else:
        voice "audio/voices/ch3/den/skeptic/27.flac"
        skeptic "Stay on your toes. We take a step into the shadows, and as soon as she moves, we jump back, make her follow. From there we trap her in the tunnel, draw her out of the cabin, whatever it takes to get her out of her element. Then we're safe.\n"

    label beast_2_basement_menu:
        default beast_2_basement_chat = False
        menu:
            extend ""

            "{i}• (Explore) ''Staying quiet, are we?''{/i}" if beast_2_basement_chat == False:
                $ beast_2_basement_chat = True
                voice "audio/voices/ch3/den/narrator/38.flac"
                n "She doesn't respond. I assume that means her answer is 'yes.'\n"
                jump beast_2_basement_menu

            "{i}• (Explore) ''We don't have to do this.''{/i}" if beast_2_basement_chat == False:
                $ beast_2_basement_chat = True
                voice "audio/voices/ch3/den/narrator/39.flac"
                n "She doesn't respond. It seems that she thinks you do, in fact, 'have to do this.'\n"
                jump beast_2_basement_menu

            "{i}• [[Step into the shadows, ready to fight.]{/i}":
                jump beast_2_fight

            "{i}• [[Step into the shadows and try to lure her out.]{/i}":
                jump beast_2_free

label beast_2_fight:

    voice "audio/voices/ch3/den/narrator/40.flac"
    play audio "audio/one_shot/footstep_mines.flac"
    hide bg den basement onlayer back
    show bg den erupt onlayer farback at Position(ypos=1125)
    with dissolve
    n "You step into the shadows and are enveloped in total darkness. Your heart pounds in your chest, ears pricked, eyes wide despite the inky blackness, waiting for any sign of movement.\n"
    play audio "audio/final/den_charge.flac"
    stop music
    voice "audio/voices/ch3/den/hunted/16.flac"
    hunted "There! She's about to strike.\n"
    if trait_stubborn and blade_held:
        play music "audio/_pristine/music/den/Rhythm of the Flesh Intro.flac"
        queue music "audio/_pristine/music/den/Rhythm of the Flesh Loop.flac" loop
        play audio "audio/final/den_emerge.flac"
        voice "audio/voices/ch3/den/narrator/41.flac"
        show den erupt onlayer back at Position(ypos=1125)
        with Dissolve(1.0)
        n "With the near-silence of a determined predator, the Princess erupts from the shadows.\n"
        $ default_mouse = "blood"
        play audio "audio/final/Tower_KnifeBlow_4.flac"
        play secondary "audio/final/den_recoil.flac"
        voice "audio/voices/ch3/den/narrator/42.flac"
        hide bg onlayer farback
        hide den onlayer back
        show bg den fight1 onlayer farback at Position(ypos=1125)
        show den fight 1 onlayer front at Position(ypos=1125)
        with dissolve
        n "You're quick to react, swinging your blade, its tip intercepting her before she can draw first blood. She recoils, stunned for a brief moment.\n"
        play audio "audio/one_shot/tackle.flac"
        play secondary "audio/final/BEAST_LionSniff_2.flac"
        voice "audio/voices/ch3/den/stubborn/20.flac"
        hide den onlayer front
        hide bg onlayer farback
        show bg den fight2 onlayer farback at Position(ypos=1125)
        show den fight 2 onlayer back at Position(ypos=1125)
        with dissolve
        stubborn "See? I told you. We needed to assert our might. We needed to prove to her that she can bleed, too. She'll doubt her every move now.\n"
        # PRISTINE JOIN
        jump den_pristine_fight

    else:
        voice "audio/voices/ch3/den/hero/17.flac"
        hero "We're screwed.\n"
        if trait_stubborn:
            voice "audio/voices/ch3/den/stubborn/21.flac"
            stubborn "We can do this. Even without a weapon. I'm no stranger to bloody fists.\n"
        else:
            if blade_held == False:
                voice "audio/voices/ch3/den/skeptic/28.flac"
                skeptic "I know. This wasn't part of the plan. We were supposed to come down here prepared, with a weapon and... oh, what's the use.\n"
            else:
                voice "audio/voices/ch3/den/skeptic/28a.flac"
                skeptic "I know. This wasn't part of the plan. We were supposed to come down here prepared and... oh, what's the use.\n"
        voice "audio/voices/ch3/den/narrator/46a.flac"
        stop music fadeout 10.0
        stop sound fadeout 20.0
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
        play audio "audio/final/den_roar_final.flac"
        voice "audio/voices/ch3/den/narrator/46.flac"
        hide bg onlayer farback
        hide bg onlayer back
        hide den onlayer front
        show bg den fight end onlayer back at Position(ypos=1125)
        show quiet creep1 onlayer front at Position(ypos=1125)
        show den fight end onlayer inyourface at Position(ypos=1125)
        with Dissolve(2.0)
        n "You just barely make out the shape of teeth and eyes as the Princess emerges, enormous maw gaping, ready to swallow you whole—\n"
        voice "audio/voices/ch3/den/hero/16.flac"
        show quiet creep2 onlayer front at Position(ypos=1125)
        with Dissolve(2.0)
        hero "And...?\n"
        $ gallery_den.unlock_item(3)
        $ renpy.save_persistent()
        show quiet creep3 onlayer front at Position(ypos=1125)
        show den erupt recognize onlayer inyourface
        with Dissolve(2.0)
        truth "But He doesn't respond. Eyes glance at you from the untextured threads of a world unraveled. 'Am I free?' They ask.\n" id beast_2_fight_902dabe6
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show arms den erupt onlayer front at Position(ypos=1125)
        show den erupt quiet onlayer inyourface at Position(ypos=1125)
        with Dissolve(2.0)
        $ renpy.pause(0.125)
        hide arms onlayer front
        show arms den erupt quiet2 onlayer front at Position(ypos=1125)
        with dissolve
        $ renpy.pause(0.125)
        hide den onlayer inyourface
        hide arms onlayer front
        show arms den erupt quiet3 onlayer front at Position(ypos=1125)
        with dissolve
        $ renpy.pause(0.125)
        hide arms onlayer front
        show arms den erupt quiet4 onlayer front at Position(ypos=1125)
        with dissolve
        $ renpy.pause(0.125)
        hide arms onlayer front
        with dissolve
        $ renpy.pause(0.125)
        hide stars onlayer farback
        hide bg onlayer back
        hide quiet onlayer front
        show farback quiet onlayer farback at Position(ypos=1125)
        with Dissolve(4.0)
        show mirror quiet distant onlayer back at Position(ypos=1125)
        if loops_finished != 0:
            truth "But you do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
        else:
            truth "But you do not have an opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
        $ beast_2_end == "fight_fail"
        $ blade_held = False
        $ default_mouse = "default"
        $ princess_kept += 1
        $ princess_satisfy += 1
        jump mirror_start
        # END

label beast_2_free:
    voice "audio/voices/ch3/den/narrator/47.flac"
    play audio "audio/one_shot/footstep_mines.flac"
    hide bg den basement onlayer back
    show bg den erupt onlayer farback at Position(ypos=1125)
    with dissolve
    n "You step into the shadows and are enveloped in total darkness. Your heart pounds in your chest, ears pricked, eyes wide despite the inky blackness, waiting for any sign of movement.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/den/stubborn/22.flac"
        stubborn "And what? You're going to turn around the second she runs for us. You'll get us killed, you pathetic fool.\n"
    else:
        voice "audio/voices/ch3/den/skeptic/29.flac"
        skeptic "That's right. Keep steady. Don't let your nerves get the better of you.\n"
    play audio "audio/final/den_charge.flac"
    voice "audio/voices/ch3/den/hunted/16.flac"
    hunted "There! She's about to strike.\n"
    play audio "audio/final/den_emerge.flac"
    play secondary "audio/one_shot/footstep_run_dirt_short.flac"
    voice "audio/voices/ch3/den/narrator/48.flac"
    hide bg onlayer farback
    show bg den free onlayer back at Position(ypos=1125)
    show fore den free onlayer front at Position(ypos=1125)
    with dissolve
    n "With the near-silence of a determined predator, the Princess erupts from the shadows. But you've already started your swift escape.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/den/stubborn/23.flac"
        hide fore onlayer front
        show quiet creep1 onlayer front at Position(ypos=1125)
        with Dissolve(2.0)
        stubborn "Stop it! Fight her!\n"
        stop music fadeout 10.0
        stop sound fadeout 20.0
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
        play audio "audio/final/BEAST_LionSniffNEW_1.flac"
        voice "audio/voices/ch3/den/narrator/49a.flac"
        show quiet creep2 onlayer front at Position(ypos=1125)
        with Dissolve(1.5)
        n "The conflict in your heart, though usually of little consequence, slows you down just enough. You don't make it into the tunnel before you feel her hot breath at your back, rushing up your spine and closing in on your neck as her teeth press into your skin and—\n"
        $ gallery_den.unlock_item(3)
        $ renpy.save_persistent()
        voice "audio/voices/ch3/den/hunted/18.flac"
        show quiet creep3 onlayer front at Position(ypos=1125)
        with Dissolve(1.5)
        hunted "Death. Again.\n"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        hide stars onlayer farback
        hide bg onlayer back
        hide quiet onlayer front
        show farback quiet onlayer farback at Position(ypos=1125)
        with Dissolve(4.0)
        show mirror quiet distant onlayer back at Position(ypos=1125)
        if loops_finished != 0:
            truth "But death doesn't come. It's time to leave. Memory returns.\n"
        else:
            truth "But death doesn't come. You turn to see that something has taken her away, and it's left something else in her place.\n"
        $ blade_held = False
        $ default_mouse = "default"
        $ beast_2_end == "free_fail"
        $ princess_kept += 1
        $ princess_satisfy += 1
        jump mirror_start
        # END
    else:
        voice "audio/voices/ch3/den/skeptic/30.flac"
        skeptic "That's stage one. Now stay focused.\n"
        play audio "audio/one_shot/footstep_mines.flac"
        play secondary "audio/_pristine/sfx/den_tunnel_chase.flac"
        #voice "audio/voices/ch3/den/narrator/50a.flac"
        voice "audio/_pristine/voice/den/narrator/23a.flac"
        hide bg onlayer back
        hide fore onlayer front
        show farback den free 2 onlayer farback at Position(ypos=1125)
        if blade_held:
            show bg den free 2 knife onlayer back at Position(ypos=1125)
        else:
            show bg den free 2 onlayer back at Position(ypos=1125)
        with dissolve
        # This needs more sound effects

        #n "You dive into the tunnel and begin scrambling up towards the cabin. You hear her behind you, claws raking at the dirt, chains rattling, breaths hot and heavy with the effort of the ascent.\n"
        n "You dive into the tunnel and begin scrambling up towards the cabin. You hear her behind you, claws raking at the dirt, chains rattling, then snapping, breaths hot and heavy with the effort of the ascent.\n"
        $ achievement.grant("ACH_BEAST_FLIGHT")
        play audio "audio/final/BEAST_LionSniff_2.flac"
        voice "audio/voices/ch3/den/narrator/51.flac"
        n "But the sounds are coming slower now, the breaths pained and stuttering. You no longer sense frantic motion behind you in the tunnel. You risk a glance.\n"
        voice "audio/voices/ch3/den/narrator/52.flac"
        $ quick_menu = False
        hide bg onlayer back
        hide farback onlayer farback
        scene bg black with fade
        with dissolve
        scene bg den stairs onlayer back at Position(ypos=1125)
        show den free 1 onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "She is a broad and sickly creature, her withered and emaciated flesh clinging to bones too large to fit into the narrow space. She managed to squirm her way into the tunnel in pursuit, but now she's stuck, incapable of either moving towards you, or returning to the open darkness of the basement below.\n"
        voice "audio/voices/ch3/den/hero/18.flac"
        hero "So that's what she's become. She wasn't like this when we started... was she?\n"
        voice "audio/voices/ch3/den/skeptic/31.flac"
        skeptic "No. She wasn't.\n"
        voice "audio/voices/ch3/den/hunted/19.flac"
        hunted "Looking at her makes me feel sad.\n"
        voice "audio/voices/ch3/den/skeptic/32.flac"
        skeptic "Yeah. Now that we can see her, she doesn't feel like much of a threat at all.\n"
        play audio "audio/_pristine/sfx/den_swing.flac"
        voice "audio/_pristine/voice/den/narrator/21.flac"
        show den free swing onlayer back
        with Dissolve(0.5)
        n "She paws futilely at the air between you, but her shoulders are pinned in the narrow confines of the opening. She has no hope of reaching you.\n"
        play audio "audio/one_shot/collapse.flac"
        voice "audio/_pristine/voice/den/narrator/22.flac"
        # sound for arm falling

        show den free resigned onlayer back
        with Dissolve(0.5)
        n "And she realizes this. Her arm goes limp, flopping to the dirt floor of the tunnel, and her eyes fall from yours. Defeated.\n"
        voice "audio/voices/ch3/den/narrator/53.flac"
        show den free 2 onlayer back
        with dissolve
        n "Her eyes look up at yours. Wide. Pleading. 'Come back,' you can imagine them saying. 'Don't leave me here!' But you shouldn't listen to the sad eyes of a vanquished enemy. She wants nothing more than to change places with you.\n"
        voice "audio/voices/ch3/den/hero/19.flac"
        hero "If you want us to ignore her then why would you tell us any of that 'wide, pleading eyes begging for mercy' business to begin with? All it does is make us feel conflicted.\n"
        voice "audio/voices/ch3/den/narrator/54.flac"
        n "I'm merely describing things as they are. It's not my fault that her eyes had something to say, even if that something was a ploy. Which, if I might stress, I pointed out to you.\n"
        voice "audio/voices/ch3/den/hero/20.flac"
        hero "What should we do about her, anyway? Can she still end the world like this?\n"
        voice "audio/voices/ch3/den/hunted/20.flac"
        hunted "She hurts. We should help.\n"
        # PRISTINE JOIN
        jump den_pristine_free

return
