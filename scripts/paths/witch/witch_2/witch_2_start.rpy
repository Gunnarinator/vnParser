label witch_2_start:

    # starting things up

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False

    # combinations
    # opportunist + smitten
    # opportunist + cheated

    $ current_princess = "thorn"

    if witch_2_voice == "cheated":
        $ trait_cheated = True
    else:
        $ trait_smitten = True

    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter thorn with fade
    show text _("{color=#FFFFFF00}Chapter 3. The Thorn.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    scene bg black with fade

    play sound "audio/looping/STP_jungle_loop.ogg" loop fadein 1.0
    play music "audio/_music/ch3/thorn/The Thorn.flac"
    queue music "audio/_music/ch3/thorn/The Thorn Loop.flac" loop

    scene farback thorn path onlayer farback at Position(ypos=1125)
    show bg thorn path onlayer back at Position(ypos=1125)
    show mid thorn path onlayer front at Position(ypos=1125)
    show fore thorn path onlayer inyourface at Position(ypos=1125)
    with fade

    $ gallery_thorn.unlock_gallery()
    $ gallery_thorn.unlock_item(1)
    $ renpy.save_persistent()

    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/thorn/narrator/1.flac"
    n "You're on a path in the woods—\n{w=1.9}{nw}"
    show screen disableclick(0.5)
    if trait_cheated:
        voice "audio/voices/ch3/thorn/cheated/1.flac"
        cheated "She stabbed us! She actually stabbed us!\n"
        voice "audio/voices/ch3/thorn/opportunist/1.flac"
        opportunist "Of course she stabbed us. We gave her the blade. Which, might I add, I voted against.\n"
        voice "audio/voices/ch3/thorn/cheated/2.flac"
        cheated "But the whole point was that she wasn't supposed to do that. The whole point of giving her the blade was to break the cycle of violence. And she just... she just killed us anyway!\n"
        voice "audio/voices/ch3/thorn/hero/1.flac"
        hero "I guess it really doesn't matter that she killed us though, right? We're back here, which means that everything's fine. Or fine-adjacent.\n"
        voice "audio/voices/ch3/thorn/hero/2.flac"
        hero "Maybe she won't be as keen to betray us {i}this{/i} time. We've already proven to her that we can change. Maybe that's all it'll take to show her there's another way to do things.\n"

    else:
        voice "audio/voices/ch3/thorn/hero/3.flac"
        hero "I can't believe she actually stabbed us!\n"
        voice "audio/voices/ch3/thorn/opportunist/2.flac"
        opportunist "I told you not to give her the blade. I told you it would come around to bite us. I voted against it.\n"
        voice "audio/voices/ch3/thorn/hero/4.flac"
        hero "Yeah, we know. You already got your 'I-told-you-sos' in while we were bleeding out.\n"
        voice "audio/voices/ch3/thorn/opportunist/3.flac"
        opportunist "I just wanted to make sure that everyone here knows that I was and am on the right side of that argument.\n"
        voice "audio/voices/ch3/thorn/smitten/1.flac"
        smitten "Oh, you're far from being on the right side of anything. You're fixated on the past, whereas what you should be is fixated on {i}the future{/i}.\n"
        voice "audio/voices/ch3/thorn/opportunist/4.flac"
        opportunist "Oho! A visionary. I like it, tell me more.\n"
        voice "audio/voices/ch3/thorn/smitten/2.flac"
        smitten "Gladly, my dear fellow. By cruelly turning on the Princess in her moment of vulnerability, we made ourselves an enemy. But by mastering our fear and insecurity and handing over our power, we've begun a journey to something so much deeper.\n"
        voice "audio/voices/ch3/thorn/opportunist/5.flac"
        opportunist "I like journeys. Traveling is a bit of a passion of mine. It makes me so {i}relatable{/i}. Now where are we off to?\n"
        voice "audio/voices/ch3/thorn/smitten/3.flac"
        smitten "Well, if we're lucky, it's a journey... to love!\n"
        voice "audio/voices/ch3/thorn/hero/5a.flac"
        hero "She hates us.\n"
        voice "audio/voices/ch3/thorn/smitten/4.flac"
        smitten "Does she? She hesitated before stabbing us to death.\n"
        #voice "audio/voices/ch3/thorn/hero/6.flac"
        #hero "As ridiculous as this guy is, maybe he has a point. I don't know if I necessarily buy into his whole 'love journey' thing, but...\n"
        voice "audio/voices/ch3/thorn/hero/7.flac"
        hero "Maybe she won't be as keen to betray us {i}this{/i} time. We've already proven to her that we can change. So maybe she'll realize that things don't have to end in violence.\n"
    voice "audio/voices/ch3/thorn/opportunist/6.flac"
    opportunist "You know, maybe you're right! In which case, I suppose the only thing to do is to get back to the cabin and give it another try.\n"
    voice "audio/voices/ch3/thorn/narrator/2a.flac"
    n "Give what another try, exactly? You are aware that I've been listening to you, right?\n"
    if trait_smitten:
        voice "audio/voices/ch3/thorn/smitten/5.flac"
        smitten "It makes no difference if we conspire in the shadows or bare our intentions with open hearts. We are breaking your cruel cycle and whisking her away to freedom!\n"
        voice "audio/voices/ch3/thorn/narrator/3.flac"
        n "Oh, are you now?\n"
    else:
        voice "audio/voices/ch3/thorn/cheated/3.flac"
        cheated "Like that changes anything. We all know the game is rigged. It doesn't even matter if she's nice this time, I'm sure He'll find a way to turn us against each other.\n"

    voice "audio/voices/ch3/thorn/narrator/4.flac"
    n "Great. So you've obviously been here before. Since you've apparently died at least once—\n{w=4.6}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/thorn/hero/8.flac"
    hero "Twice, actually.\n"
    voice "audio/voices/ch3/thorn/narrator/5.flac"
    n "Sure. Twice. {i}Sigh{/i}. Then I'll spare you the little introduction I had planned. You already know about the Princess, and clearly, you already know that she's dangerous. So don't muck this up. It's bad enough that this isn't your first time through.\n"

label witch_2_path_menu:
    default witch_2_looping = False
    default witch_2_different = False
    default witch_2_intentions = False
    default witch_2_intent_free = False
    default witch_2_intent_harsh = False
    default witch_2_leave_explore = False
    menu:

        extend ""

        "{i}• (Explore) This place is different. It keeps changing.{/i}" if witch_2_different == False:
            $ witch_2_different = True
            voice "audio/voices/ch3/thorn/narrator/6.flac"
            n "Wonderful. If the woods themselves are changing, then that's all the more reason for you to take this seriously. It would mean your grip on things is slipping, which in turn, likely means her influence is spreading.\n"
            voice "audio/voices/ch3/thorn/opportunist/7.flac"
            opportunist "Someone's in the know.\n"
            if trait_cheated:
                voice "audio/voices/ch3/thorn/cheated/4.flac"
                cheated "I've had enough of these annoying little secrets. If you want us to do this, you have to let us in on your game already! All of your game.\n" id witch_2_path_menu_24a6b07f
            voice "audio/voices/ch3/thorn/narrator/7.flac"
            n "{i}Sigh.{/i} I've already said too much. The more information you have, the more difficult your task will be. Don't listen to her, definitely don't free her, and if you can, don't even think about her.\n"
            if trait_smitten:
                voice "audio/voices/ch3/thorn/smitten/6a.flac"
                smitten "You don't have to worry about me, my head's always empty. {i}Romantic sigh.{/i} Except for thoughts of her.\n"
                #voice "audio/voices/ch3/thorn/smitten/6.flac"
                #smitten "You don't have to worry about me, my head's always empty. {i}Romantic sigh.{/i} Except for thoughts of her. Maybe you do need to worry about me. after all.\n"
            jump witch_2_path_menu

        "{i}• (Explore) We're going to free her.{/i}" if witch_2_intentions == False:
            $ witch_2_intentions = True
            $ witch_2_intent_free = True
            voice "audio/voices/ch3/thorn/narrator/8.flac"
            n "{i}Sigh.{/i} Please don't.\n"
            if trait_smitten:
                voice "audio/voices/ch3/thorn/smitten/7.flac"
                smitten "You can't stop all of us, you villain!\n"
            else:
                voice "audio/voices/ch3/thorn/cheated/5a.flac"
                cheated "I'm with him. If our previous encounters have taught us anything, it's that freeing her is a bad idea.\n"
            voice "audio/voices/ch3/thorn/opportunist/8.flac"
            opportunist "Let's just see how the wind blows. I'm not opposed to saving her, but let's not rule anything out just yet. Let's see what she has to say.\n"
            label witch_2_opportunist_waffle_join:
                voice "audio/voices/ch3/thorn/hero/9.flac"
                hero "Stop sitting on the fence and pick a side already, we don't need you waffling when things get hairy.\n"
                voice "audio/voices/ch3/thorn/opportunist/9.flac"
                opportunist "I've already picked a side! Our side. I'm here to make sure that whatever happens, we wind up on top.\n"
                voice "audio/voices/ch3/thorn/hero/10.flac"
                hero "Because that's worked out great so far.\n"
                voice "audio/voices/ch3/thorn/opportunist/10.flac"
                opportunist "Well, we're not out of the game yet, are we? And again, I'll have you know I wouldn't have gotten us killed last time. I wanted to stab her in the back, not hand over our precious back-stabbing implement!\n"
            jump witch_2_path_menu

        "{i}• (Explore) We're even now. I'm sure she understands that. But we can see what she has to say for herself when we get to the cabin.{/i}" if witch_2_intentions == False:
            $ witch_2_intentions = True
            voice "audio/voices/ch3/thorn/opportunist/11.flac"
            opportunist "Yes, good. Playing both sides. That's what smart people do, and you're the smartest in the room.\n"
            voice "audio/voices/ch3/thorn/hero/11.flac"
            hero "I'm not sure it counts as 'playing both sides' if people can hear you doing it.\n"
            voice "audio/voices/ch3/thorn/opportunist/12a.flac"
            opportunist "Buddy, you're thinking in far too few dimensions. There's layers to doing this right, and I'm pretty sure the one making the choices gets that. Trust in the plan!\n"
            voice "audio/voices/ch3/thorn/hero/12.flac"
            hero "Trust in what plan?\n"
            voice "audio/voices/ch3/thorn/opportunist/13.flac"
            opportunist "The decider's plan! Sure, we don't know what the plan is yet, but that's part of the whole 'trusting' thing, isn't it? A good leader knows how and when to keep things secret. And sometimes a good leader even knows to keeps things secret from himself.\n"
            if trait_smitten:
                voice "audio/voices/ch3/thorn/smitten/8.flac"
                smitten "There isn't a plan and that's the whole point! We're supposed to be guided by emotion. We're supposed to passionately live in the moment. And I'm sure that when the time comes, those passions will tell us to set our darling Princess free.\n"
            else:
                voice "audio/voices/ch3/thorn/cheated/6.flac"
                cheated "Sure. We'll see what she has to say for herself. But don't forget that whatever she says is likely just as much lies as what He's been telling us. We should keep our cards close to our chest.\n"
            voice "audio/voices/ch3/thorn/narrator/9a.flac"
            n "If I were you, I'd remember what she's done. You know how dangerous she is, and you should know that someone like her shouldn't be let loose upon the world.\n"
            jump witch_2_path_menu

        "{i}• (Explore) I hope you don't think I'm planning on freeing her after she stabbed me in the heart.{/i}" if witch_2_intentions == False:
            $ witch_2_intent_harsh = True
            $ witch_2_intentions = True
            voice "audio/voices/ch3/thorn/narrator/10.flac"
            n "That's the spirit. Don't forget what she's done to you. She's practically asking for you to slay her.\n"
            if trait_smitten:
                voice "audio/voices/ch3/thorn/smitten/9.flac"
                smitten "Even though we were stabbed in the heart, it doesn't mean that we don't still have one. She'll come around, just like we did.\n"
            else:
                voice "audio/voices/ch3/thorn/cheated/7.flac"
                cheated "You're damned right! You need two to break a cycle of violence, and if she's not playing the same game as us, we've got to go back to treating her like an enemy.\n"
            voice "audio/voices/ch3/thorn/opportunist/14.flac"
            opportunist "Let's just see how the wind blows. I'm not opposed to violence here, but let's not rule anything out just yet. Maybe we won her over last time, who knows!\n"
            jump witch_2_opportunist_waffle_join

        "{i}• (Explore) Screw the cabin, what happens if we just leave?{/i}" if witch_2_leave_explore == False:
            $ witch_2_leave_explore = True
            voice "audio/voices/ch3/thorn/narrator/11.flac"
            n "She gets out, is what happens. Maybe not right away, but eventually. And a world that's doomed tomorrow is just as bad as a world that's doomed today.\n"
            if trait_smitten:
                voice "audio/voices/ch3/thorn/smitten/10.flac"
                smitten "He's a bummer, isn't he? All doom this and doom that. There's more to the world than how and when it will end. Love is what makes everything worth doing.\n"
                voice "audio/voices/ch3/thorn/narrator/12.flac"
                n "Whatever you do, don't listen to this one. He's ridiculous. Whatever he wants you to do, do the opposite.\n"
            else:
                voice "audio/voices/ch3/thorn/cheated/8.flac"
                cheated "I'm not sure I buy that. Everything has to end eventually. If it takes years to get out of there and supposedly end the world, then we've bought everyone that time and all without having to murder anybody in the process.\n"
                voice "audio/voices/ch3/thorn/cheated/9.flac"
                cheated "Not that she's innocent, but... murder is unpleasant. And risky. It could be a better solution for everyone.\n"
                voice "audio/voices/ch3/thorn/narrator/13.flac"
                n "You're here to permanently end the threat she poses. You're not here to temporarily postpone it.\n"
            jump witch_2_path_menu

        "{i}• (Explore) You sure seem to be taking the whole 'looping' thing in stride.{/i}" if witch_2_looping == False:
            $ witch_2_looping = True
            voice "audio/voices/ch3/thorn/narrator/14.flac"
            n "{i}Sigh{/i}. What do you want me to say? It's bad that you've been here before. It's bad for you, it's bad for me, and it's especially bad for the world. The more times you run through this, the more likely it is that you'll fail. And you've already failed twice.\n"
            voice "audio/voices/ch3/thorn/hero/13.flac"
            hero "So you knew this could happen?\n"
            voice "audio/voices/ch3/thorn/narrator/15.flac"
            n "Theoretically, sure. I knew this {i}could{/i} happen. But I was supposed to be the first. I'd really rather not get into it.\n"
            if trait_smitten:
                voice "audio/voices/ch3/thorn/smitten/11.flac"
                smitten "I don't care about where we came from and I don't care to discuss the theory of anything. I yearn only to bring her freedom. I'm here to feel, not to think!\n"
            else:
                voice "audio/voices/ch3/thorn/cheated/10.flac"
                cheated "Great. Not even He really seems to get what's going on. If the guy who goes around acting like he knows all the rules doesn't even know how this works, what's the point in listening?\n"
            voice "audio/voices/ch3/thorn/narrator/16.flac"
            n "Then we can all move on! And forget what I said about failure.\n"
            voice "audio/voices/ch3/thorn/narrator/17.flac"
            n "It's important that you believe in yourself, and the fact that you're here probably means that you still have a chance to pull this off and save the world. My world, at least. It sounds like you've probably doomed a couple of others already.\n"
            voice "audio/voices/ch3/thorn/narrator/18.flac"
            n "I need to stop talking. Think... happy thoughts.\n"
            jump witch_2_path_menu


        "{i}• No matter what happens next, it seems like all our answers are in the cabin. Let's see this through. [[Proceed to the cabin.]{/i}":
            jump witch_2_exterior

        "{i}• [[Silently proceed to the cabin.]{/i}":
            jump witch_2_exterior

        "{i}• I'm done with this. Bye! [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
            if loops_finished >= 2:
                $ mound_can_attempt_flee = False
                voice "audio/voices/mound/bonus/flee.flac"
                mound "You have already committed to my completion. You cannot go further astray.\n"
                jump witch_2_path_menu
            $ caught_origin_ch3 = True
            $ caught_origin_current = "witch2"
            voice "audio/voices/ch3/thorn/opportunist/15.flac"
            opportunist "If that's what you think is best!\n"
            if trait_cheated:
                voice "audio/voices/ch3/thorn/cheated/11.flac"
                cheated "Good choice! Flip the table. Let's get out of here.\n"
            voice "audio/voices/ch3/thorn/narrator/19.flac"
            play audio "audio/one_shot/footsteps_hike_short.flac"
            scene farback thorn path onlayer farback at flip, Position(ypos=1125)
            show bg thorn path onlayer back at flip, Position(ypos=1125)
            show mid thorn path onlayer front at flip, Position(ypos=1125)
            show fore thorn path onlayer inyourface at flip, Position(ypos=1125)
            with fade
            n "Are you serious?! Fine. You walk away from the the cabin. We'll see how that goes for you.\n"
            if trait_smitten:
                voice "audio/voices/ch3/thorn/smitten/12.flac"
                smitten "B-but she's the other way! Don't abandon our destiny!\n"
            jump caught_start

label witch_2_exterior:
    $ gallery_thorn.unlock_item(2)
    $ renpy.save_persistent()
    play audio "audio/one_shot/footsteps_hike_short.flac"
    $ quick_menu = False
    hide farback onlayer farback
    hide bg onlayer back
    hide mid onlayer front
    hide fore onlayer inyourface
    with fade
    scene skyline cabin onlayer farback at Position(ypos=1125)
    show bg thorn ext onlayer back at Position(ypos=1125)
    show mid thorn ext onlayer front at Position(ypos=1125)
    show fore thorn ext onlayer inyourface at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/thorn/narrator/20.flac"
    n "It isn't long before you find yourself at the base of the cabin. I think it's clear where everyone stands at this point.\n"
    voice "audio/voices/ch3/thorn/hero/14.flac"
    hero "I don't know if I'd say 'everyone.'\n"
    voice "audio/voices/ch3/thorn/opportunist/16.flac"
    opportunist "Are you talking about me? I have a position. It's a good one, too.\n"
    if witch_2_looping == False:
        voice "audio/voices/ch3/thorn/narrator/21.flac"
        n "Ignore him, he's just talking for talking's sake. My position is the only one that matters. The Princess is a threat to you. She's a threat to me. And most importantly, she's a threat to the world. You know what you have to do.\n"
    else:
        voice "audio/voices/ch3/thorn/narrator/22.flac"
        n "Ignore him, he's just talking for talking's sake. My position is the only one that matters. You know what you have to do.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            $ quick_menu = False
            play audio "audio/one_shot/door_bedroom.flac"
            hide skyline onlayer farback
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            with fade
            jump witch_2_cabin


label witch_2_cabin:
    $ gallery_thorn.unlock_item(3)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/thorn/narrator/23.flac"
    scene skyline cabin onlayer farback at Position(ypos=1125)
    show bg thorn cabin onlayer back at Position(ypos=1125)
    show fore thorn cabin onlayer front at Position(ypos=1125)
    show mirror thorn cabin onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The interior of the cabin is hardly an interior at all anymore. The burned-out ruins merely suggest the shape of the structure that once stood here, charred wood still reeking of ash, but beneath it lies the fresh smell of spring growth after rain, the promise of new life in the wreckage of the old.\n"
    voice "audio/voices/ch3/thorn/narrator/24.flac"
    n "The only furniture of note is the crisped shell of what was once a table, a pristine— wait, this isn't right. There's supposed to be a pristine blade. Why isn't there a pristine blade?\n"
    voice "audio/voices/ch3/thorn/hero/15.flac"
    hero "We... we gave it to her last time. She can't still have it, can she?\n"
    voice "audio/voices/ch3/thorn/opportunist/17.flac"
    opportunist "Well, it's not here. And if she has it...\n"
    voice "audio/voices/ch3/thorn/hero/16.flac"
    hero "Let me guess, you want to get all chummy with her.\n"
    voice "audio/voices/ch3/thorn/opportunist/18.flac"
    opportunist "Look, as far as I see it, if it's between Him and her, I say we side with the one who has the weapon. It's just the smart thing to do!\n"
    voice "audio/voices/ch3/thorn/narrator/25.flac"
    n "I wouldn't be so hasty. I'm sure the blade will turn up somewhere. She can't have it, that's not how this is supposed to work.\n"
    if trait_cheated:
        voice "audio/voices/ch3/thorn/cheated/12.flac"
        cheated "Of course we don't get to make a choice about the blade. Every single time we come back here, something has to be different.\n"
    else:
        voice "audio/voices/ch3/thorn/smitten/13.flac"
        smitten "If she does have it, that's all the more reason to put our faith in her. We've already shown her our heart. Now she has to show us hers.\n"
        voice "audio/voices/ch3/thorn/opportunist/19.flac"
        opportunist "Unless her heart tells her to stab us. Which doesn't seem {i}un{/i}likely. So yes, I agree. Let's make sure we get on her good side!\n"
    label witch_2_cabin_menu:
        default witch_2_mirror_comment = False
        menu:
            extend ""

            "{i}• (Explore) How do we even get down there? The only thing I see is that mirror.{/i}" if witch_2_mirror_comment == False:
                $ witch_2_mirror_comment = True
                $ current_run_mirror_comment = True
                if witch_1_cabin_mirror_ask or witch_1_cabin_mirror_approached:
                    voice "audio/voices/ch3/thorn/hero/17.flac"
                    hero "You're right, the mirror is back. There isn't anywhere for us to go.\n"
                    voice "audio/voices/ch3/thorn/narrator/26.flac"
                    n "But there isn't a mirror.\n"
                else:
                    voice "audio/voices/ch3/thorn/hero/18.flac"
                    hero "Yeah. Why didn't you mention the mirror?\n"
                    voice "audio/voices/ch3/thorn/narrator/27.flac"
                    n "I didn't mention a mirror because there isn't a mirror.\n"
                if witch_1_cabin_mirror_ask or witch_1_cabin_mirror_approached:
                    voice "audio/voices/ch3/thorn/opportunist/20.flac"
                    opportunist "I still don't get His angle here.\n"
                    if trait_cheated:
                        voice "audio/voices/ch3/thorn/cheated/13.flac"
                        cheated "Seems like whatever we do, he's always going to say it isn't there.\n"
                else:
                    voice "audio/voices/ch3/thorn/opportunist/21.flac"
                    opportunist "But He says there isn't one. That's got to count for something, right?\n"
                    if trait_cheated:
                        voice "audio/voices/ch3/thorn/cheated/14.flac"
                        cheated "Yeah, it counts for something.\n"
                if trait_cheated:
                    voice "audio/voices/ch3/thorn/cheated/15.flac"
                    cheated "He's either a liar or he doesn't hold all the cards. But I think we already knew it had to be one of those.\n"
                if trait_smitten:
                    voice "audio/voices/ch3/thorn/smitten/14.flac"
                    smitten "Either way, I say we take a look. It feels like it's been forever since we've actually seen ourselves. For all we know, our feathers are all out of place, and that's why we haven't yet won her heart. We must put our best face forward!\n"
                    voice "audio/voices/ch3/thorn/opportunist/22.flac"
                    opportunist "Yeah, we can't go around looking disheveled! A real go-getter takes care of his appearance.\n"
                voice "audio/voices/ch3/thorn/hero/19.flac"
                hero "So is the door to the basement behind the mirror?\n"
                voice "audio/voices/ch3/thorn/narrator/28.flac"
                n "{i}Sigh{/i}. I promise you there isn't a mirror. And there isn't a door to the basement. The entrance is more of a burned out frame than anything else, and it's right there, on the far side of the room. Do you really not see it?\n"
                jump witch_2_cabin_menu

            "{i}• [[Approach the mirror.]{/i}":
                $ quick_menu = False
                voice "audio/voices/ch3/thorn/narrator/29.flac"
                play audio "audio/one_shot/footsteps_hike_short.flac"
                hide skyline onlayer farback
                hide bg onlayer back
                hide fore onlayer front
                hide mirror onlayer front
                show skyline cabin onlayer farback at Position(ypos=1125)
                show bg onlayer back at Position(ypos=1125)
                show mid thorn cabin close onlayer front at Position(ypos=1125)
                show mirror thorn cabin close onlayer front at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You step forward and approach the scorched entryway leading to the basement, hesitating before you begin the descent.\n"
                if trait_smitten:
                    voice "audio/voices/ch3/thorn/smitten/15.flac"
                    smitten "You know what you have to do. Wipe away the grit from the mirror, and behold our handsome features.\n"
                if witch_1_cabin_mirror_approached:
                    if trait_cheated:
                        voice "audio/voices/ch3/thorn/cheated/16.flac"
                        cheated "It went away when we touched it last time. Not that this place always follows the same rules.\n"
                    else:
                        voice "audio/voices/ch3/thorn/hero/20.flac"
                        hero "It went away when we touched it last time...\n"
                else:
                    if trait_cheated:
                        voice "audio/voices/ch3/thorn/cheated/17.flac"
                        cheated "Might as well take a look while we can. There's nothing else to do here now that the knife has been taken from us.\n"
                    #else:
                    #    voice "audio/voices/ch3/thorn/hero/21.flac"
                    #    hero "All right. Let's just wipe off that grime.\n"

                $ current_run_mirror_touched = True
                menu:
                    extend ""

                    "{i}• [[Wipe the mirror clean.]{/i}":
                        hide mirror onlayer front
                        #$ renpy.pause(0.1)
                        #show player mound finale reach onlayer inyourface at Position(ypos=1125)
                        #with Dissolve(0.5)
                        if witch_2_mirror_comment:
                            voice "audio/voices/ch3/thorn/narrator/30.flac"
                            n "You reach forward and wave your hand through the hollow entrance leading to the basement. You really thought there was a mirror there, didn't you? That... can't be good. As if things weren't unpredictable enough.\n"
                        else:
                            voice "audio/voices/ch3/thorn/narrator/31.flac"
                            n "You reach forward and wave your hand through the hollow entrance leading to the basement. What are you doing?\n"
                        if trait_smitten:
                            voice "audio/voices/ch3/thorn/smitten/16.flac"
                            smitten "Alas, our fine features remain unseen. We'll just have to trust that she'll find us beautiful as we are.\n"
                        else:
                            voice "audio/voices/ch3/thorn/cheated/18.flac"
                            cheated "Figures.\n"
                        voice "audio/voices/ch3/thorn/hero/22.flac"
                        #hide player onlayer inyourface
                        hero "Well, it seems like the only way to go is forward, isn't it?\n"
                        voice "audio/voices/ch3/thorn/opportunist/23.flac"
                        opportunist "Yes, that's where everything tends to be. Let's just put on a good face and have our wits about us.\n"
                        menu:
                            extend ""

                            "{i}• [[Enter the basement.]{/i}":
                                $ quick_menu = False
                                voice "audio/voices/ch3/thorn/narrator/32.flac"
                                play audio "audio/one_shot/footsteps_hike_short.flac"
                                hide skyline onlayer farback
                                hide bg onlayer back
                                hide mid onlayer front
                                scene bg black
                                with fade
                                n "You step through the frame of scorched wood and make your way into the darkness below.\n"
                                jump witch_2_stairs

label witch_2_stairs:

    show bg thorn stairs onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/thorn/narrator/33.flac"
    n "The stairs to the basement are covered in a fine layer of gritty ash. The air still feels warm, as if the fires that ruined this place had only recently been extinguished, yet fresh shoots of thorny branches are already weaving themselves through the soot-covered earth of the walls around you.\n"
    voice "audio/voices/ch3/thorn/narrator/34.flac"
    n "Their spines point courteously down towards the basement, so you're able to brush past their jagged points with ease. At least on the way down. But you don't need to think about the way back up just yet. That's a matter for after the world's been saved.\n"
    if trait_smitten:
        voice "audio/voices/ch3/thorn/smitten/17.flac"
        smitten "These thorns are an expression of her pain, I know it. She's calling out for help!\n"
    else:
        voice "audio/voices/ch3/thorn/cheated/19.flac"
        cheated "I'd say this feels like a trap, but you practically said as much. Yet you still want us to keep going.\n"
        voice "audio/voices/ch3/thorn/narrator/35.flac"
        n "They're only thorns, I'd say getting a few scratches in exchange for the lives of everyone in existence is a fair trade. I'm sure you'll manage.\n"
    voice "audio/voices/ch3/thorn/narrator/36.flac"
    n "Her voice, worn down by pain and suspicion, hobbles up the stairs.\n"
    if loop_1_locked:
        voice "audio/voices/ch3/thorn/princess/1.flac"
        p "I can't get away from you, can I? I lock you away, and you come back. You let me kill you, and you come back.\n"
    elif current_mutual_death == 1:
        voice "audio/voices/ch3/thorn/princess/2.flac"
        p "I can't get away from you, can I? We kill each other, and you come back. You let me kill you, and you come back.\n"
    else:
        voice "audio/voices/ch3/thorn/princess/3.flac"
        p "I can't get away from you, can I? You betray me, I kill you, and you come back. You let me kill you, and you come back.\n"
    voice "audio/voices/ch3/thorn/princess/4.flac"
    p "I don't know why you let me do that. I don't know what you want from me.\n"
    label witch_2_stairs_menu:
        default witch_2_stairs_menu_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''I want to figure out a way out of here. For good.''{/i}" if witch_2_stairs_menu_explore == False:
                jump witch_2_stairs_join

            "{i}• (Explore) ''I don't know what I want. I never really chose to come here.''{/i}" if witch_2_stairs_menu_explore == False:
                jump witch_2_stairs_join

            "{i}• (Explore) ''I want to free you. I mean it.''{/i}" if witch_2_stairs_menu_explore == False:
                jump witch_2_stairs_join

            "{i}• (Explore) ''I just want to talk. Really talk.''{/i}" if witch_2_stairs_menu_explore == False:
                label witch_2_stairs_join:
                    $ witch_2_stairs_menu_explore = True
                    voice "audio/voices/ch3/thorn/princess/5.flac"
                    p "I think you know how this goes. I'm down here, and I can't leave. So come down and talk. It's not like I can stop you.\n"
                    jump witch_2_stairs_menu

            "{i}• [[Proceed down the stairs.]{/i}":
                jump witch_2_basement

label witch_2_basement:
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_hike_short.flac"
    hide bg onlayer back
    with fade
    voice "audio/voices/ch3/thorn/narrator/37.flac"
    n "You continue down the basement stairs, brushing past the smooth edges of thorns that grow more and more plentiful as you make your way forward.\n"
    $ gallery_thorn.unlock_item(4)
    $ renpy.save_persistent()
    show farback thorn basement onlayer farback at Position(ypos=1125)
    show bg thorn basement onlayer back at Position(ypos=1125)
    show thorn dk neutral onlayer back at Position(ypos=1125)
    show fore thorn basement onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/thorn/narrator/38.flac"
    n "You step out into what was once a vast, open cavern, now overrun by briars and prickles and thistles, the space thick with hostile vegetation.\n"
    voice "audio/voices/ch3/thorn/narrator/39.flac"
    n "At the heart of it all, encased in a tight weave of vines, is the Princess, her bloody, trembling hands clutching a pristine blade.\n"
    voice "audio/voices/ch3/thorn/princess/6.flac"
    show thorn dk neutral talk onlayer back
    p "Did you know this was going to happen to me? Are you here to watch me suffer? Are you here to laugh?\n"
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_hike_short.flac"
    hide farback onlayer farback
    hide farback onlayer back
    hide bg onlayer back
    hide thorn onlayer back
    hide fore onlayer front
    with fade
    show bg thorn close onlayer back at Position(ypos=1125)
    show thorn c neutral onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True

label witch_2_basement_menu:
    default witch_2_menu_count = 0
    default witch_2_doubt_count = 3
    default witch_2_player_hostile = False
    default witch_2_intro = False
    default witch_2_follow = False
    default witch_2_what_say = False
    default witch_2_blade_ask = False
    default witch_2_blade_attempt = False
    if blade_held:
        if trait_smitten:
            voice "audio/voices/ch3/thorn/smitten/18.flac"
            smitten "She trusts us. She trusts us! Doesn't that set your heart aflutter?\n"
            voice "audio/voices/ch3/thorn/hero/23.flac"
            hero "... Yeah, a little. It could just be nerves, being this close to her does bring back unpleasant memories. But I don't know. It doesn't feel bad. It feels good. Like we're special to her.\n"
            voice "audio/voices/ch3/thorn/smitten/19.flac"
            smitten "We are special, to have gained an ounce of trust from a maiden so guarded. Now all that remains is to free her from her bindings.\n"
            voice "audio/voices/ch3/thorn/hero/24.flac"
            hero "Yeah, let's do it! Let's show her how much both of us have changed.\n"
        else:
            voice "audio/voices/ch3/thorn/cheated/20.flac"
            cheated "I'll be damned. She really gave it to us.\n"
            voice "audio/voices/ch3/thorn/opportunist/24.flac"
            opportunist "It feels like it's been so long since we've held real power in our hands. I wonder what we should do with it.\n"
            voice "audio/voices/ch3/thorn/hero/25.flac"
            hero "We free her, obviously. It's the right thing to do.\n"
            voice "audio/voices/ch3/thorn/cheated/21.flac"
            cheated "I think you're right. She's as much a victim in all of this as we've been. And besides, it would really stick it to Him to free her.\n"

        voice "audio/voices/ch3/thorn/opportunist/25.flac"
        opportunist "Or... hear me out. We slay her, right here, right now. She's never been so helpless, and if we don't take advantage of that, we may never get another chance!\n"
        voice "audio/voices/ch3/thorn/narrator/40.flac"
        n "That sounds like a splendid idea. You should listen to {i}him{/i}.\n"
        if trait_smitten:
            voice "audio/voices/ch3/thorn/smitten/20.flac"
            smitten "I see that the lines have been drawn.\n"
        else:
            voice "audio/voices/ch3/thorn/cheated/22.flac"
            cheated "We've all said our piece. Now it's time to make our move.\n"
        voice "audio/voices/ch3/thorn/hero/26.flac"
        hero "It's two against one.\n"
        voice "audio/voices/ch3/thorn/narrator/41.flac"
        n "It's two against two.\n"
        voice "audio/voices/ch3/thorn/hero/27.flac"
        hero "You don't count.\n"
        voice "audio/voices/ch3/thorn/opportunist/26.flac"
        opportunist "And why shouldn't He count?\n"
        voice "audio/voices/ch3/thorn/hero/28.flac"
        hero "Because He's clearly not one of us?\n"
        voice "audio/voices/ch3/thorn/opportunist/27.flac"
        opportunist "That doesn't matter. He's been with us the whole time, he should get a say.\n"
        voice "audio/voices/ch3/thorn/princess/7.flac"
        show thorn superclose noknife talk onlayer back
        with dissolve
        p "So. Did you mean it? Or was I a fool to hand my life to you?\n"
        show thorn superclose noknife onlayer back
        with dissolve
    menu:
        extend ""

        "{i}• (Explore) ''Yeah. I'm here to laugh. What did you think would happen after you killed me? Did you think I wouldn't hold it against you?''{/i}" if witch_2_player_hostile == False and witch_2_menu_count == 0 and blade_held == False and witch_2_intro == False:
            $ witch_2_menu_count += 1
            $ witch_2_player_hostile = True
            voice "audio/voices/ch3/thorn/princess/8.flac"
            show thorn c threaten talk onlayer back
            with dissolve
            p "Careful now, I'm the one with the knife.\n"
            voice "audio/voices/ch3/thorn/princess/9.flac"
            show thorn c clutch talk onlayer back
            with dissolve
            p "Of course I thought there might be bad blood. I didn't think I could trust you then, and it looks like I was right, because I definitely can't trust you now.\n"
            voice "audio/voices/ch3/thorn/princess/10.flac"
            show thorn c sullen talk onlayer back
            with dissolve
            p "I guess this is what I deserve. What we both deserve.\n"
            show thorn c sullen onlayer back
            with dissolve
            if trait_smitten:
                voice "audio/voices/ch3/thorn/smitten/21.flac"
                smitten "Look at the regret in those beautiful eyes. She is our shining star, and you have brought her to tears! How could you say such cruelties?\n"
                voice "audio/voices/ch3/thorn/opportunist/28.flac"
                opportunist "Tears are easy to fake, don't let her get to you. She's resorting to desperate tactics, which means we're winning!\n"
            if trait_cheated:
                voice "audio/voices/ch3/thorn/cheated/23.flac"
                cheated "I'm out. Whatever you do, don't let her out of there. It's not going to end well for anyone.\n"
                voice "audio/voices/ch3/thorn/opportunist/29.flac"
                opportunist "Hey! Welcome to the winning team.\n"
                voice "audio/voices/ch3/thorn/cheated/24.flac"
                cheated "Oh, can it, will you? I'm not happy to be here, this is just the only move that was still worth making.\n"
            jump witch_2_basement_menu

        "{i}• (Explore) ''I'm not here to laugh. I'm here to free you. If you'll let me.''{/i}" if witch_2_player_hostile == False and blade_held == False and witch_2_intro == False:
            $ witch_2_intro = True
            $ witch_2_menu_count += True
            voice "audio/voices/ch3/thorn/princess/11.flac"
            show thorn c sad talk onlayer back
            with dissolve
            p "I... I want to trust you.\n"
            voice "audio/voices/ch3/thorn/narrator/43.flac"
            show thorn c clutch onlayer back
            with dissolve
            n "Her grip tightens on the blade.\n"
            voice "audio/voices/ch3/thorn/princess/12.flac"
            show thorn c nervous talk onlayer back
            with dissolve
            p "But you're hiding something, aren't you? Why would you help me if you weren't helping yourself?\n"
            show thorn c nervous onlayer back
            with dissolve
            jump witch_2_basement_menu

        "{i}• (Explore) ''You're not the only one who yearns for freedom. I'm as trapped as you are. I think we need to leave together.''{/i}" if witch_2_intro and witch_2_follow == False and witch_2_player_hostile == False and blade_held == False:
            $ witch_2_follow = True
            $ witch_2_menu_count += 1
            voice "audio/voices/ch3/thorn/narrator/44.flac"
            show thorn c clutch onlayer back
            with dissolve
            n "The Princess clutches the blade closer to her chest.\n"
            voice "audio/voices/ch3/thorn/princess/13b.flac"
            show thorn c ache talk onlayer back
            with dissolve
            p "That sounds... nice. I'm so tired of the bad blood between us. But it's hard to let it go. You've hurt me.\n"
            voice "audio/voices/ch3/thorn/narrator/45.flac"
            show thorn c resigned2 onlayer back
            with dissolve
            n "Her eyes dart away from yours for a brief moment.\n"
            voice "audio/voices/ch3/thorn/princess/14.flac"
            show thorn c resigned1 onlayer back
            with dissolve
            p "And I've also hurt you.\n"
            show thorn c resigned2 onlayer back
            with dissolve
            #edited
            jump witch_2_basement_menu

        "{i}• (Explore) ''I can cut you free. But you'll have to give me the blade.''{/i}" if witch_2_intro == False and blade_held == False:
            $ witch_2_intro = True
            $ witch_2_menu_count += 1
            if witch_2_player_hostile:
                voice "audio/voices/ch3/thorn/princess/15.flac"
                show thorn c angry talk onlayer back
                with dissolve
                p "I'm not falling for it!\n"
                show thorn c clutch onlayer back
                with dissolve
            else:
                voice "audio/voices/ch3/thorn/princess/16.flac"
                show thorn c clutch talk onlayer back
                with dissolve
                p "And I'm supposed to believe it's safe in your hands? That you aren't just saying what you need to say in order to fool me and save yourself?\n"
                show thorn c sad onlayer back
                with dissolve
            jump witch_2_basement_menu

        "{i}• (Explore) ''Is there nothing I can say to change your mind?''{/i}" if blade_held == False and witch_2_what_say == False and witch_2_menu_count >= 1 and witch_2_ask_approve == False:
            $ witch_2_what_say = True
            $ witch_2_menu_count += 1
            if witch_2_player_hostile:
                voice "audio/voices/ch3/thorn/princess/17.flac"
                show thorn c sullen talk onlayer back
                with dissolve
                p "No. We're past that. You and I both know words are hollow.\n"
                voice "audio/voices/ch3/thorn/opportunist/30.flac"
                show thorn c sullen onlayer back
                with dissolve
                opportunist "Figures. I wouldn't trust her, so why would she trust us?\n"
                voice "audio/voices/ch3/thorn/hero/29.flac"
                hero "You're the one who got us here, if you weren't doing so much scheming maybe we could have formed a genuine connection. Maybe we could have fixed things!\n"
                voice "audio/voices/ch3/thorn/opportunist/31.flac"
                opportunist "I think there are a lot of other people worth pointing fingers at before you go blaming me, I'm just looking out for our best interests. Did you forget that she stabbed us last time?!\n"
                if trait_cheated:
                    voice "audio/voices/ch3/thorn/cheated/25.flac"
                    cheated "The game's over. We shouldn't have pushed her so hard. Give it up and leave her here. It's not like she can go anywhere on her own.\n"
                else:
                    voice "audio/voices/ch3/thorn/smitten/22.flac"
                    smitten "I remember, and I'd do it all again. I'd gladly take a thousand knives to save her just once.\n"
            else:
                voice "audio/voices/ch3/thorn/princess/18.flac"
                show thorn c nervous talk onlayer back
                with dissolve
                p "I... I don't know! What can either of us really say at this point? How can we trust something as hollow as words?\n"
                voice "audio/voices/ch3/thorn/opportunist/32.flac"
                show thorn c neutral onlayer back
                with dissolve
                opportunist "She's right, there's nothing left to say. So let's get a move on and do something, before she comes up with a scheme to get out of there on her own.\n"
                if trait_smitten:
                    voice "audio/voices/ch3/thorn/smitten/23.flac"
                    smitten "We don't need words to send a message. It is through action that we can show her our adoration, our devotion, our kindness.\n"
                else:
                    voice "audio/voices/ch3/thorn/cheated/26.flac"
                    cheated "Careful with that one, he's not the smooth negotiator he thinks he is. But it does feel like we're stuck until we do something. If there's even anything to do besides make things worse.\n"
                    voice "audio/voices/ch3/thorn/hero/30.flac"
                    hero "We're not making things worse. I think she wants to trust us.\n"
            jump witch_2_basement_menu

        "{i}• (Explore) ''Then maybe it's past time for either of us to say anything. All that counts is action'' [[Reach for the blade.]{/i}" if blade_held == False and witch_2_what_say and witch_2_player_hostile == False and witch_2_ask_approve == False:
            $ witch_2_menu_count += 1
            jump witch_2_take_blade_join

        "{i}• (Explore) ''Can I take the blade now?''{/i}" if witch_2_follow and blade_held == False and witch_2_blade_ask == False and witch_2_player_hostile == False:
            default witch_2_ask_approve = False
            $ witch_2_ask_approve = True
            $ witch_2_blade_ask = True
            $ witch_2_menu_count += 1
            voice "audio/voices/ch3/thorn/narrator/46.flac"
            show thorn c neutral onlayer back
            with dissolve
            $ renpy.pause(0.2)
            voice sustain
            show thorn c resigned2 onlayer back
            with dissolve
            n "Her eyes briefly meet yours, then dart back to the floor. She hangs her head in resignation.\n"
            voice "audio/voices/ch3/thorn/princess/19.flac"
            show thorn c resigned2 talk onlayer back
            with dissolve
            p "Okay.\n"
            show thorn c resigned2 onlayer back
            with dissolve
            jump witch_2_basement_menu

        "{i}• (Explore) [[Reach for the blade.]{/i}" if blade_held == False and witch_2_blade_hostile_attempt == False:
            $ witch_2_menu_count += 1
            if witch_2_follow or witch_2_blade_ask:
                label witch_2_take_blade_join:

                    if witch_2_blade_attempt:
                        $ witch_2_blade_attempt = True
                        voice "audio/voices/ch3/thorn/narrator/47.flac"
                        hide bg onlayer back
                        hide thorn onlayer back
                        show bg thorn super close onlayer back at Position(ypos=1125)
                        show thorn give knife onlayer back at Position(ypos=1125)
                        show player thorn give knife onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        n "You reach into the thorns once more and lay your hand on the Princess' bloody fingers, wrapped tightly around the blade. Her hand trembles in yours.\n"
                    else:
                        $ witch_2_blade_attempt = True
                        voice "audio/voices/ch3/thorn/narrator/48.flac"
                        hide bg onlayer back
                        hide thorn onlayer back
                        show bg thorn super close onlayer back at Position(ypos=1125)
                        show thorn give knife onlayer back at Position(ypos=1125)
                        show player thorn give knife onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        n "You reach towards her bloodied hands, laying your palm on her trembling fingers.\n"
                    play audio "audio/one_shot/knife_tighten.flac"
                    $ blade_held = True
                    $ default_mouse = "blood"
                    voice "audio/voices/ch3/thorn/narrator/49.flac"
                    hide player onlayer back
                    show thorn snatch onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "For a moment, she clutches it even tighter, her knuckles going white with the effort.\n"
                    voice "audio/voices/ch3/thorn/narrator/49a.flac"
                    $ blade_held = True
                    $ default_mouse = "blood"
                    play audio "audio/one_shot/knife_pickup.flac"
                    hide player onlayer back
                    show thorn superclose noknife onlayer back
                    with Dissolve(1.0)
                    n "But then the tension fades. Her grip finally loosens, and she allows you to take the weapon.\n"
                    voice "audio/voices/ch3/thorn/narrator/50.flac"
                    n "You carefully pull it free from the thorns, though they scrape at your skin, leaving red trickles of fresh blood all along your arms.\n"
                    jump witch_2_basement_menu
            else:
                if witch_2_blade_attempt == False:
                    $ witch_2_blade_attempt = True
                    voice "audio/voices/ch3/thorn/narrator/51.flac"
                    hide bg onlayer back
                    hide thorn onlayer back
                    show bg thorn super close onlayer back at Position(ypos=1125)
                    show thorn give knife onlayer back at Position(ypos=1125)
                    show player thorn snatch onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "You reach into the thorns, towards her bloodied hands and the blade clutched tight in her grasp.\n"
                    voice "audio/voices/ch3/thorn/narrator/52.flac"
                    show thorn snatch onlayer back
                    with dissolve
                    n "But she snatches it away, ignoring the thorns that carve fresh wounds as she moves within her prison of vines.\n"
                    voice "audio/voices/ch3/thorn/princess/20.flac"
                    show thorn snatch talk onlayer back
                    with dissolve
                    p "I knew this is the only reason you'd come back down here! I'm not falling for it! It's mine now, and I'll let these thorns tear me to shreds before I hand it over.\n"
                else:
                    default witch_2_blade_hostile_attempt = False
                    $ witch_2_blade_hostile_attempt = True
                    $ witch_2_player_hostile = True
                    voice "audio/voices/ch3/thorn/narrator/53.flac"
                    hide bg onlayer back
                    hide thorn onlayer back
                    show bg thorn super close onlayer back at Position(ypos=1125)
                    show thorn snatch onlayer back at Position(ypos=1125)
                    show player thorn snatch onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "You reach into the nest of thorns once again, and again she yanks the blade away, despite the obvious pain it causes.\n"
                    voice "audio/voices/ch3/thorn/princess/21.flac"
                    show thorn snatch talk onlayer back
                    with dissolve
                    p "Play your games all you want, but I've decided how I feel! I can do this forever if that's what it takes to keep it out of your hands.\n"
                    hide bg onlayer back
                    hide thorn onlayer back
                    hide player onlayer back
                    show bg thorn close onlayer back at Position(ypos=1125)
                    show thorn c neutral onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                jump witch_2_basement_menu


        "{i}• ''You're in a prison of your own making. I broke our cycle of violence. If you still want to wallow in it, be my guest.'' [[Turn and leave.]{/i}" if blade_held == False:
            jump witch_2_leave

        "{i}• ''I guess I don't have anything left to say to you.'' [[Turn and leave.]{/i}" if blade_held == False:
            jump witch_2_leave

        "{i}• ''Fine. If you're going to be like that, I'm going to leave. Have a nice life.'' [[Turn and leave.]{/i}" if blade_held == False:
            jump witch_2_leave

        "{i}• [[Cut her free.]{/i}" if blade_held:
            jump witch_2_free

        "{i}• [[Slay the Princess.]{/i}" if blade_held:
            jump witch_2_slain

        "{i}• ''I just wanted my blade back. You're on your own.'' [[Turn and leave.]{/i}" if blade_held:
            jump witch_2_leave

label witch_2_slain:

    stop music
    if trait_smitten:
        voice "audio/voices/ch3/thorn/smitten/24.flac"
        smitten "Oh, you scoundrel!\n"
    voice "audio/voices/ch3/thorn/hero/31.flac"
    hero "Why?! We finally gained her trust. That took a lot of work!\n"
    voice "audio/voices/ch3/thorn/opportunist/33a.flac"
    opportunist "Sorry, boys. It looks like we've got our tie-breaker.\n"
    $ gallery_thorn.unlock_item(5)
    $ gallery_thorn.unlock_item(6)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/thorn/narrator/54.flac"
    play audio "audio/one_shot/knife_tighten.flac"
    hide bg onlayer back
    hide thorn onlayer back
    hide player onlayer back
    show bg thorn super close onlayer back at Position(ypos=1125)
    show quiet creep1 onlayer back at Position(ypos=1125)
    show cg thorn slay1 onlayer back at Position(ypos=1125)
    show player thorn slay1 onlayer front at Position(ypos=1125)
    with Dissolve(0.5)
    #show
    n "Blade safely in hand, you turn it on the Princess, and drive it towards her heart.\n"
    play music "audio/_music/ch3/thorn/The Thorn II.flac"
    queue music "audio/_music/ch3/thorn/The Thorn II Loop.flac" loop
    hide quiet onlayer back
    hide bg onlayer back
    hide cg onlayer back
    hide player onlayer front
    scene bg black
    play audio "audio/final/Witch_VinesTwist_2.flac"
    voice "audio/voices/ch3/thorn/narrator/55.flac"
    n "But her thistled prison proves to be an impossible obstacle, its thorns digging deeper and deeper into your flesh the closer you come to striking the fatal blow.\n"
    if trait_smitten:
        voice "audio/voices/ch3/thorn/smitten/25.flac"
        smitten "Ha! We're not going to make it. This is what we deserve. Better we trap ourselves in this eternal moment than have her blood on our hands. We still managed to get our romantic end, in a way.\n"
    if trait_cheated:
        voice "audio/voices/ch3/thorn/cheated/27.flac"
        cheated "Those damned vines are going to stop us, just like they stopped her. Of course! Like we should have expected it to turn out any other way. It's funny, really. I'm laughing.\n"
    $ achievement.grant("ACH_THORN_TRAP")
    $ default_mouse = "blood"
    stop music fadeout 15.0
    stop sound fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
    voice "audio/voices/ch3/thorn/narrator/56.flac"
    play audio "audio/one_shot/blood_drip.flac"
    show bg thorn super close onlayer back at Position(ypos=1125)
    show quiet creep2 onlayer back at Position(ypos=1125)
    show cg thorn slay2 onlayer back at Position(ypos=1125)
    with fade
    n "The tip of your blade only manages to touch her sternum before it stops moving entirely. A single drop of blood trickles down her chest as the two of you stare into each others' eyes.\n"
    voice "audio/voices/ch3/thorn/narrator/57.flac"
    n "Come on. Just push it a little further. {i}Sigh{/i}. But you can't, can you?\n"
    voice "audio/voices/ch3/thorn/princess/22.flac"
    show quiet creep3 onlayer back
    show cg thorn slay2 talk onlayer back
    with dissolve
    p "I knew this was coming. I can't believe I ever let myself hope for better. This was always going to be us, wasn't it?\n"
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    show cg thorn slay2 cold onlayer back
    with Dissolve(0.75)
    $ renpy.pause(0.125)
    show cg thorn slay2 quiet onlayer back
    with Dissolve(0.75)
    $ renpy.pause(0.125)
    show cg thorn slay2 quiet 2 onlayer back
    with Dissolve(0.75)
    $ renpy.pause(0.125)
    show cg thorn slay2 quiet 3 onlayer back
    with Dissolve(0.75)
    $ renpy.pause(0.125)
    hide cg onlayer back
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
    if persistent.quick_menu:
        $ quick_menu = True
    if loops_finished != 0:
        truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
    else:
        truth "You do not have an opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
    $ thorn_end = "slay_attempt"
    $ princess_deny += 1
    $ princess_kept += 1
    jump mirror_start

label witch_2_free:

    voice "audio/voices/ch3/thorn/opportunist/34.flac"
    opportunist "Yes! What a good idea. Let's cut her free.\n"
    voice "audio/voices/ch3/thorn/hero/32a.flac"
    hero "Oh, so you're suddenly team 'free her?' You can't just switch sides as soon as we make a decision.\n"
    voice "audio/voices/ch3/thorn/opportunist/35.flac"
    opportunist "I can do whatever I want. And I believe with my whole heart that this is the right course of action. Let's free this Princess!\n"
    if trait_smitten:
        voice "audio/voices/ch3/thorn/smitten/28.flac"
        smitten "Everyone deserves a chance at redemption. Let him join us, and be merry! We are all united by our passion!\n"
        voice "audio/voices/ch3/thorn/opportunist/36.flac"
        opportunist "That's right, what he said.\n"
        voice "audio/voices/ch3/thorn/hero/33.flac"
        hero "We've already given him a chance at redemption!\n"
        voice "audio/voices/ch3/thorn/opportunist/37.flac"
        opportunist "And who says I don't deserve another? I really mean it this time, I'm big enough to admit when I'm wrong. So I want to help you all free her!\n"
        voice "audio/voices/ch3/thorn/smitten/29.flac"
        smitten "And I have no problem with that! Welcome to the team. You're one of us now. One of the good guys.\n"
    else:
        voice "audio/voices/ch3/thorn/cheated/28.flac"
        cheated "Even if he'll stick a knife in our back as soon as he has the opportunity, it's still better to have him nominally on our side. At least that gets him to shut up for a while.\n"
        voice "audio/voices/ch3/thorn/opportunist/38.flac"
        opportunist "See, we're all friends here! United in our actions and intentions.\n"
        voice "audio/voices/ch3/thorn/hero/34.flac"
        hero "Yeah, united. But the other one has a point, if it keeps you quiet, sure, we're all friends.\n"
    voice "audio/voices/ch3/thorn/narrator/58.flac"
    play audio "audio/final/Adversary_StabCut_8.flac"
    hide bg onlayer back
    hide farback onlayer farback
    hide farback onlayer back
    hide thorn onlayer back
    hide player onlayer back
    hide fore onlayer front
    hide cg onlayer back
    show bg thorn free onlayer back at Position(ypos=1125)
    show thorn free onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    n "You take the blade to the thorny vines imprisoning the Princess, and she flinches, relaxing only slightly as the blade slices into the thick vegetation rather than her arm.\n"
    voice "audio/voices/ch3/thorn/narrator/59.flac"
    play audio "audio/final/Adversary_StabCut_7.flac"
    show bg thorn free2 onlayer back at Position(ypos=1125)
    show thorn free2 onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    n "And she flinches again as the last of the vines is cut away, as if, after all of that, she's still expecting you to turn on her and stab her in the heart. But you're not going to do that, are you? Still, all it would take is a single slip of the blade.\n"
    if trait_smitten:
        voice "audio/voices/ch3/thorn/smitten/30.flac"
        smitten "Such a pathetic attempt at distraction and subterfuge! Our blade is a dashing sword, and every dashing sword is an extension of its hero. It won't slip.\n"
        voice "audio/voices/ch3/thorn/opportunist/39.flac"
        opportunist "You're right. He can't even make it slip, can he? He's a bit of a nobody. Good thing I've been on your side of all this since the beginning.\n"
    else:
        voice "audio/voices/ch3/thorn/cheated/29.flac"
        cheated "Is that really all you've got? Threatening us with an accidental misstep? I expected more from you.\n"
        voice "audio/voices/ch3/thorn/opportunist/40.flac"
        opportunist "Our blade didn't even waver when he said that. Yeah, you're right! He's a bit of a nobody, isn't he? Good thing I've been on your side of all this since the beginning.\n"
        #edited

    voice "audio/voices/ch3/thorn/narrator/60.flac"
    play tertiary "audio/final/Adversary_StabCut_8.flac"
    queue tertiary "audio/one_shot/collapse.flac"
    show bg thorn free arms onlayer back
    show thorn free arms onlayer back
    with Dissolve(1.5)
    n "The Princess falls into your arms, tears streaking down her cheeks. I can't believe you're making me describe this. I hate you.\n"
    voice "audio/voices/ch3/thorn/princess/23.flac"
    show thorn free arms talk onlayer back
    with dissolve
    p "You actually meant it. You... rescued me.\n"
    show thorn free arms glance onlayer back
    with dissolve
    if trait_smitten:
        default witch_2_kiss = False
        voice "audio/voices/ch3/thorn/smitten/31.flac"
        smitten "Do you see the way she's looking at us? Kiss her! Kiss her now before the moment ends!\n"
    menu:
        extend ""

        "{i}• ''Of course I did.''{/i}":
            label witch_2_free_join:
                voice "audio/voices/ch3/thorn/narrator/61.flac"
                show thorn hand hold onlayer back
                with Dissolve(0.5)
                n "She smiles, her hand slipping into yours, and the two of you rush to the basement stairs.\n"
                if trait_smitten and witch_2_kiss == False:
                    voice "audio/voices/ch3/thorn/smitten/32.flac"
                    smitten "You should have kissed her, you fool! It was the perfect moment!\n"

        "{i}• ''I just really hate the people who put us here.''{/i}":
            voice "audio/voices/ch3/thorn/princess/24.flac"
            show thorn free arms talk onlayer back
            with dissolve
            p "Me, too.\n"
            jump witch_2_free_join

        "{i}• [[Kiss her.]{/i}" if trait_smitten:
            stop music
            $ witch_2_kiss = True
            voice "audio/voices/ch3/thorn/hero/35.flac"
            hero "Can we actually do that?\n"
            voice "audio/voices/ch3/thorn/narrator/62.flac"
            n "No! You can't! Absolutely not!\n"
            voice "audio/voices/ch3/thorn/smitten/33.flac"
            show thorn kiss1 onlayer back
            with dissolve
            smitten "You know as well as I do that we can.\n"
            voice "audio/voices/ch3/thorn/opportunist/41a.flac"
            opportunist "And we wouldn't want to throw away a chance for a special moment, now would we?\n"
            voice "audio/voices/ch3/thorn/narrator/63.flac"
            n "If I were only capable of throwing myself off a bridge.\n"
            voice "audio/voices/ch3/thorn/smitten/34.flac"
            smitten "Well, are you going to describe our steamy, romantic kiss?\n"
            play music "audio/_music/ch3/thorn/The Thorn Kiss.flac"
            queue music "audio/_music/ch3/thorn/The Thorn Kiss Loop.flac" loop
            voice "audio/voices/ch3/thorn/narrator/64.flac"
            show thorn kiss2 onlayer back
            with dissolve
            n "{i}Sigh{/i}. You lean in and you kiss her.\n"
            voice "audio/voices/ch3/thorn/hero/36.flac"
            hero "... And?\n"
            voice "audio/voices/ch3/thorn/narrator/65.flac"
            n "And she reciprocates. Enthusiastically. You kiss. It's done. Are you happy now?\n"
            voice "audio/voices/ch3/thorn/smitten/35.flac"
            smitten "Come on now, this is a big moment! You can do better than that!\n"
            voice "audio/voices/ch3/thorn/narrator/66.flac"
            n "Ugh! FINE. You and the Princess lock eyes and stare deep into each other's souls with all of the roaring emotion that comes from letting what once was hatred turn into pure, unbridled passion.\n"
            voice "audio/voices/ch3/thorn/hero/37.flac"
            hero "Are you making fun of us?\n"
            voice "audio/voices/ch3/thorn/narrator/67.flac"
            n "And then each of you close your eyes and kiss. Words can describe neither the nuclear fire nor the oceanic depth of your connection.\n"
            voice "audio/voices/ch3/thorn/opportunist/42.flac"
            opportunist "Please, I think he actually likes romance.\n"
            voice "audio/voices/ch3/thorn/narrator/68.flac"
            n "If history itself were not about to end, historians would document this moment for the rest of time. Musicians would write era defining ballads, and great artists would expend entire lifetimes trying to merely capture the spark you hold right now.\n"
            #n "Yes.\n"
            voice "audio/voices/ch3/thorn/hero/38.flac"
            hero "He's making fun of us.\n"
            voice "audio/voices/ch3/thorn/smitten/36.flac"
            smitten "It doesn't matter either way. Because this is good stuff.\n"
            voice "audio/voices/ch3/thorn/narrator/69.flac"
            n "I'm aware of my skills.\n"
            $ gallery_thorn.unlock_item(15)
            $ gallery_thorn.unlock_item(16)
            $ renpy.save_persistent()
            $ achievement.grant("ACH_THORN_KISS")
            voice "audio/voices/ch3/thorn/narrator/70.flac"
            show thorn kiss smile onlayer back
            with Dissolve(0.5)
            n "But unfortunately for you, the moment doesn't last forever. You open your eyes. The Princess smiles gently up at you. Time for you to damn the whole world to oblivion, I suppose.\n"
            voice "audio/voices/ch3/thorn/princess/25.flac"
            show thorn kiss talk onlayer back
            with dissolve
            p "That was nice.\n"
            jump witch_2_no_smile_join

        "{i}• [[Remain silent.]{/i}":
            label witch_2_no_smile_join:
                voice "audio/voices/ch3/thorn/narrator/71.flac"
                show thorn hand hold onlayer back
                with Dissolve(0.5)
                n "Her hand slips into yours, and the two of you rush to the basement stairs.\n"
                #edited to match first iteration

    voice "audio/voices/ch3/thorn/narrator/72.flac"
    play audio "audio/one_shot/footsteps_hike_short.flac"
    hide bg onlayer back
    hide farback onlayer farback
    hide farback onlayer back
    hide thorn onlayer back
    hide player onlayer back
    hide fore onlayer front
    hide cg onlayer back
    show farback thorn stairs onlayer farback at Position(ypos=1125)
    show bg thorn stairs blocked onlayer back at Position(ypos=1125)
    show fore thorn stairs blocked onlayer front at Position(ypos=1125)
    show thorn stairs blocked onlayer inyourface at Position(ypos=1125)
    with Dissolve(0.5)
    n "Shameful, really, that the same thorns that so graciously allowed you downstairs are now blocking your only way out.\n"
    if trait_smitten:
        voice "audio/voices/ch3/thorn/smitten/37.flac"
        smitten "Please. After all the trials we've been through, do you really think a few measly thorns can stop us? Love is an even more powerful weapon than our blade.\n"
    else:
        voice "audio/voices/ch3/thorn/cheated/30.flac"
        cheated "You're getting desperate, aren't you? Even more proof that you can't actually do anything to stop us.\n"
    voice "audio/voices/ch3/thorn/hero/39.flac"
    hero "We cut through those other vines just fine. They're only thorns, I'm not afraid of getting a few scrapes.\n"
    voice "audio/voices/ch3/thorn/opportunist/43.flac"
    opportunist "I'm not even sure we need to do any cutting. We can just move them out of the way. What a pathetic showing, really.\n"
    voice "audio/voices/ch3/thorn/princess/26.flac"
    p "A few pointy sticks can't keep us down here. We're both meant for so much more than this.\n"

    menu:
        extend ""

        "{i}• [[Cut into the thorns.]{/i}":
            voice "audio/voices/ch3/thorn/narrator/73.flac"
            play audio "audio/final/Razor_SwordSwish_1.flac"
            play tertiary "audio/final/Witch_RootsMoving_1.flac"
            show bg thorn stairs give onlayer back
            show fore thorn stairs give onlayer front
            show thorn stairs give onlayer inyourface
            with Dissolve(1.5)
            n "As you swing your blade into the thorns covering the basement stairs they... yield.\n"

        "{i}• [[Step into the thorns.]{/i}":
            voice "audio/voices/ch3/thorn/narrator/74.flac"
            play audio "audio/final/Witch_RootsMoving_1.flac"
            show bg thorn stairs give onlayer back
            show fore thorn stairs give onlayer front
            show thorn stairs give onlayer inyourface
            with Dissolve(1.5)
            n "As you step into the thorns covering the basement stairs, they... yield.\n"

    voice "audio/voices/ch3/thorn/narrator/75.flac"
    play audio "audio/one_shot/footsteps_hike_short.flac"
    hide thorn onlayer inyourface
    hide farback onlayer farback
    hide fore onlayer front
    hide bg onlayer back
    scene bg black
    scene farback thorn stairs ascend onlayer farback at Position(ypos=1125)
    show bg thorn stairs ascend onlayer back at Position(ypos=1125)
    show fore thorn stairs ascend onlayer front at Position(ypos=1125)
    show thorn ascend onlayer front at Position(ypos=1125)
    with Dissolve(0.5)
    n "Both you and the Princess ascend the stairs without obstacle. This is unacceptable! The second you step out of this cabin with her, the world {i}ends{/i} do you hear me? What did the world ever do to you to deserve this?\n"
    if trait_cheated:
        voice "audio/voices/ch3/thorn/cheated/31.flac"
        cheated "It feels so good to hear you say that. That you're admitting you've lost, and we've bested you at your own game at last. I don't care what happens now. That's all I've wanted.\n"
    if trait_smitten:
        if witch_2_kiss:
            voice "audio/voices/ch3/thorn/smitten/38.flac"
            smitten "Your nightmare is our dream. Whatever world would condemn star-crossed lovers like us to a cycle of violence and despair isn't a world worth saving.\n"
        else:
            voice "audio/voices/ch3/thorn/smitten/39.flac"
            smitten "Your nightmare is our dream. Whatever world would condemn an innocent like her to a cycle of violence and despair isn't a world worth saving.\n"
        voice "audio/voices/ch3/thorn/smitten/40.flac"
        smitten "We'll weave something new together. Something better.\n"

    play audio "audio/one_shot/footsteps_hike_short.flac"
    voice "audio/voices/ch3/thorn/narrator/76.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide fore onlayer front
    hide thorn onlayer front
    show bg door thorn onlayer back at Position(ypos=1125)
    show thorn door onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    n "You and the Princess hesitate at the cabin door. This is your last chance.\n" id witch_2_no_smile_join_70d05ec8
    voice "audio/voices/ch3/thorn/hero/40.flac"
    hero "We've already made our decision.\n"
    voice "audio/voices/ch3/thorn/princess/27a.flac"
    show thorn door talk onlayer back
    with dissolve
    p "We're finally leaving here together, aren't we? And all we had to do was trust each other. It wasn't easy, but... I'm glad we finally could.\n"
    show thorn door onlayer back
    with dissolve
    menu:
        extend ""

        "{i}• [[Step into your freedom.]{/i}":
            $ achievement.grant("ACH_THORN_LEAF")
            $ quick_menu = False
            stop music fadeout 25.0
            stop sound fadeout 25.0
            stop tertiary fadeout 25.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
            play audio "audio/one_shot/door_bedroom.flac"
            show thorn door open onlayer back
            with Dissolve(0.25)
            $ renpy.pause(0.25)
            voice "audio/voices/ch3/thorn/narrator/77.flac"
            $ gallery_thorn.unlock_item(8)
            $ gallery_thorn.unlock_item(9)
            $ gallery_thorn.unlock_item(10)
            $ gallery_thorn.unlock_item(11)
            $ gallery_thorn.unlock_item(12)
            $ gallery_thorn.unlock_item(13)
            $ gallery_thorn.unlock_item(14)
            $ renpy.save_persistent()
            hide bg onlayer back
            hide thorn onlayer back
            show farback thorn outside onlayer farback at Position(ypos=1125)
            show bg thorn outside onlayer back at Position(ypos=1125)
            show thorn outside neutral onlayer front at Position(ypos=1125)
            show fore thorn outside onlayer inyourface at Position(ypos=1125)
            with fade
            n "Hands clasped, the two of you open the door, and step out into a new day. You irredeemable murderers.\n"
            voice "audio/voices/ch3/thorn/princess/28.flac"
            show quiet creep1 onlayer back at Position(ypos=1125)
            show thorn outside talk player onlayer front
            with dissolve
            p "What do we do now?\n"
            voice "audio/voices/ch3/thorn/princess/29.flac"
            show quiet creep2 onlayer back
            show thorn outside talk afraid onlayer front
            with Dissolve(0.3)
            p "Wh—where's everything going?\n"
            voice "audio/voices/ch3/thorn/princess/30.flac"
            hide fore onlayer front
            show quiet creep3 onlayer back
            show thorn outside cold talk onlayer front
            with Dissolve(1.5)
            p "Why is it so cold?\n"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            show arms thorn outside1 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            show arms thorn outside2 onlayer back at Position(ypos=1125)
            show thorn outside quiet onlayer front
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            hide thorn onlayer front
            show arms thorn outside3 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            show arms thorn outside4 onlayer back at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.125)
            hide arms thorn onlayer back
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
            if persistent.quick_menu:
                $ quick_menu = True
            if loops_finished != 0:
                truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
            else:
                truth "You do not have an opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
            if witch_2_kiss:
                $ thorn_end = "free_kiss"
                $ princess_satisfy += 1
            else:
                $ thorn_end = "free"
            $ princess_free += 1
            $ princess_satisfy += 1
            jump mirror_start
            # END

label witch_2_leave:
    if blade_held:
        stop music fadeout 25.0
        stop sound fadeout 25.0
        stop tertiary fadeout 25.0
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
    else:
        stop music
    $ achievement.grant("ACH_THORN_ABANDON")
    voice "audio/voices/ch3/thorn/princess/31.flac"
    hide bg onlayer back
    hide farback onlayer farback
    hide farback onlayer back
    hide thorn onlayer back
    hide player onlayer back
    hide fore onlayer front
    hide cg onlayer back
    show farback thorn basement onlayer farback at Position(ypos=1125)
    show bg thorn basement onlayer back at Position(ypos=1125)
    if blade_held:
        show quiet creep1 onlayer back at Position(ypos=1125)
        show thorn d mad talk onlayer back at Position(ypos=1125)
    else:
        show thorn dk laugh onlayer back at Position(ypos=1125)
    show fore thorn basement onlayer front at Position(ypos=1125)
    with Dissolve(0.75)
    p "Do you really think you can just wash your hands of all this? Do you really think you can just leave me here?!\n"
    voice "audio/voices/ch3/thorn/opportunist/44.flac"
    if blade_held == False:
        play music "audio/_music/ch3/thorn/The Thorn II.flac"
        queue music "audio/_music/ch3/thorn/The Thorn II Loop.flac" loop
        show thorn d mad onlayer back
        with dissolve
    else:
        show quiet creep2 onlayer back
        with Dissolve(0.5)
    opportunist "This is even better than stabbing her. The same reward without any of that nasty effort.\n"
    voice "audio/voices/ch3/thorn/narrator/78.flac"
    n "It's not 'even better.' Putting off a choice is always worse than making a committed decision, especially when you already know the right answer.\n"
    if trait_smitten:
        voice "audio/voices/ch3/thorn/smitten/41.flac"
        smitten "It's even more cruel if you ask me. Leaving an incredible soul like hers to languish forever, in pain and alone. How can we bear to live with the guilt?\n"
        voice "audio/voices/ch3/thorn/opportunist/45.flac"
        if blade_held:
            show quiet creep3 onlayer back
            with Dissolve(0.5)
        opportunist "We'll live with it just fine. Besides, she'll get over it.\n"
        voice "audio/voices/ch3/thorn/narrator/79.flac"
        n "That's what I'm afraid of.\n"
    else:
        voice "audio/voices/ch3/thorn/cheated/32.flac"
        cheated "Almost feels like we're as bad as the powers that be. Is that all it really took to twist us into yet another tyrant? A single ounce of control?\n"
        voice "audio/voices/ch3/thorn/hero/41.flac"
        hero "It sure feels like it. She looks so... sad, bleeding and alone. And we're just turning our back on her.\n"
        voice "audio/voices/ch3/thorn/opportunist/46.flac"
        if blade_held:
            show quiet creep3 onlayer back
            with Dissolve(0.5)
        opportunist "Oh, stop trying to bring morality into this. There are winners in life, and there are losers, and what matters is that right now, we've decided to be a winner.\n"
    if blade_held:
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        hide thorn onlayer back
        show arms thorn d1 onlayer back at Position(ypos=1125)
        show thorn d mad onlayer back at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.125)
        show arms thorn d2 onlayer back at Position(ypos=1125)
        show thorn d quiet onlayer back at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.125)
        show arms thorn d3 onlayer back at Position(ypos=1125)
        hide thorn onlayer back at Position(ypos=1125)
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        show arms thorn d4 onlayer back at Position(ypos=1125)
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        hide arms onlayer back at Position(ypos=1125)
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
        if persistent.quick_menu:
            $ quick_menu = True
        if loops_finished != 0:
            truth "But in your commitment to leaving things unresolved, you have no chance at resolution, nor will you ever. It's time to leave. Memory returns.\n"
        else:
            truth "But in your commitment to leaving things unresolved, you have no chance at resolution. Something has taken her away, and it's left something else in her place.\n"
        $ thorn_end = "abandoned"
        $ princess_kept += 1
        $ princess_deny += 1
        jump mirror_start
        # END


    else:
        voice "audio/voices/ch3/thorn/narrator/80.flac"
        play audio "audio/one_shot/footsteps_hike_short.flac"
        hide bg onlayer back
        hide farback onlayer farback
        hide farback onlayer back
        hide thorn onlayer back
        hide player onlayer back
        hide fore onlayer front
        hide cg onlayer back
        show farback thorn stairs onlayer farback at Position(ypos=1125)
        show bg thorn stairs blocked onlayer back at Position(ypos=1125)
        show fore thorn stairs blocked onlayer front at Position(ypos=1125)
        with Dissolve(0.5)
        n "But as you approach the basement stairs, you make a grim realization. The thorns won't let you leave.\n"
        voice "audio/voices/ch3/thorn/hero/42.flac"
        hero "And we don't have any way to cut through them.\n"
        voice "audio/voices/ch3/thorn/opportunist/47.flac"
        opportunist "Okay! New plan. We re-befriend the Princess, get the blade, and all of us leave here together as friends.\n"
        voice "audio/voices/ch3/thorn/princess/32.flac"
        p "You can't leave without me, can you? Isn't that funny. Isn't that so funny! This is perfect, actually. Just you and me, rotting down here forever. Together.\n"
        hide farback onlayer farback
        hide bg onalyer back
        hide fore onlayer front
        show farback thorn basement onlayer farback at Position(ypos=1125)
        show bg thorn basement onlayer back at Position(ypos=1125)
        show thorn dk laugh onlayer back at Position(ypos=1125)
        show fore thorn basement onlayer front at Position(ypos=1125)
        with Dissolve(0.75)
        if trait_smitten:
            voice "audio/voices/ch3/thorn/smitten/42.flac"
            smitten "It's what we deserve after everything we've done. It's... romantic, even. We got our beautiful ending after all, tragic as it may be.\n"
        voice "audio/voices/ch3/thorn/princess/33.flac"
        show thorn d wily talk onlayer back
        with dissolve
        p "You know, just to make sure things are little more permanent, I think I'm going to take this particular needle out of the picture.\n"
        voice "audio/voices/ch3/thorn/opportunist/48.flac"
        opportunist "She wouldn't.\n"
        if trait_cheated:
            voice "audio/voices/ch3/thorn/cheated/33.flac"
            cheated "It's only fair. We were going to leave her with no way out. She's returning the kindness.\n"
        voice "audio/voices/ch3/thorn/narrator/81.flac"
        play audio "audio/one_shot/knife_pickup.flac"
        show thorn d blade lift onlayer back
        with dissolve
        n "Thorns slice into the Princess' hands, lacerating what little skin remains, as she raises the blade to her mouth.\n"
        voice "audio/voices/ch3/thorn/opportunist/49.flac"
        opportunist "Take it! Take it now before she swallows it out of spite!\n"
        menu:
            extend ""

            "{i}• [[Rush for the blade.]{/i}":
                stop music fadeout 20.0
                stop sound fadeout 20.0
                stop tertiary fadeout 20.0
                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                $ quick_menu = False
                play audio "audio/one_shot/footstep_run_medium.flac"
                voice "audio/voices/ch3/thorn/narrator/82.flac"
                play tertiary "audio/final/Witch_VinesTwist_2.flac"
                hide bg onlayer back
                hide farback onlayer farback
                hide farback onlayer back
                hide thorn onlayer back
                hide player onlayer back
                hide fore onlayer front
                hide cg onlayer back
                show bg thorn super close onlayer back at Position(ypos=1125)
                show quiet creep1 onlayer back at Position(ypos=1125)
                show cg thorn swallow rush onlayer back at Position(ypos=1125)
                show player thorn swallow rush onlayer front at Position(ypos=1125)
                with Dissolve(0.5)
                n "You rush towards the Princess, arm outsretched and grasping for the blade.\n"
                voice "audio/voices/ch3/thorn/narrator/83.flac"
                n "But as you tear through her thistled prison, the thorny vines dig deep into your arms, seemingly growing thicker and sturdier the closer you get to your goal. It feels like it should be within reach, yet you cannot reach it quickly enough.\n"
                voice "audio/voices/ch3/thorn/hero/43.flac"
                hero "It's no use. Even if we grab it, we won't be able to pull it back out of there.\n"
                voice "audio/voices/ch3/thorn/opportunist/50.flac"
                opportunist "It's better than letting her eat it and losing it forever!\n"
                play audio "audio/final/Witch_VinesTwist_1.flac"
                $ achievement.grant("ACH_THORN_TRAP")
                $ default_mouse = "blood"
                voice "audio/voices/ch3/thorn/narrator/84.flac"
                hide player onlayer front
                show quiet creep2 onlayer back
                show cg thorn swallow grab onlayer back
                show vines thorn swallow grab onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                n "You just manage to reach her hand, grasping it firmly in yours, before the thorns finally trap you in place. Blood trickles down your arm, mingling with hers. The two of you lock eyes.\n"
                $ gallery_thorn.unlock_item(6)
                $ renpy.save_persistent()
                voice "audio/voices/ch3/thorn/princess/34.flac"
                show quiet creep3 onlayer back
                show cg thorn swallow grab talk onlayer back
                with dissolve
                p "We're stuck like this, aren't we? I knew this was always going to be how it ended.\n"
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                hide cg onlayer back
                show arms thorn swallow1 onlayer back at Position(ypos=1125)
                show cg thorn swallow grab onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                $ renpy.pause(0.125)
                hide vines onlayer back
                show arms thorn swallow2 onlayer back at Position(ypos=1125)
                show cg thorn swallow quiet onlayer back at Position(ypos=1125)
                with Dissolve(0.75)
                $ renpy.pause(0.125)
                hide cg onlayer back
                show arms thorn swallow3 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                $ renpy.pause(0.125)
                show arms thorn swallow4 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                $ renpy.pause(0.125)
                hide arms onlayer back
                with Dissolve(0.5)
                $ renpy.pause(0.125)
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
                if persistent.quick_menu:
                    $ quick_menu = True
                if loops_finished != 0:
                    truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                else:
                    truth "You do not have an opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
                $ thorn_end = "stuck_together"
                $ princess_kept += 1
                $ princess_deny += 1
                jump mirror_start
                # END

            "{i}• [[Do nothing.]{/i}":
                stop music fadeout 20.0
                stop sound fadeout 20.0
                stop tertiary fadeout 20.0
                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                voice "audio/voices/ch3/thorn/narrator/85.flac"
                hide thorn onlayer back
                show quiet creep1 onlayer back at Position(ypos=1125)
                show thorn d swallow onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                n "You stand in place among the thorns, inert, merely watching as the Princess swallows your only way out of this place.\n"
                voice "audio/voices/ch3/thorn/opportunist/51.flac"
                show quiet creep2 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                opportunist "She actually did it.\n"
                if trait_smitten:
                    voice "audio/voices/ch3/thorn/smitten/43.flac"
                    smitten "Good for her. Such a decisive woman.\n"
                    voice "audio/voices/ch3/thorn/opportunist/52.flac"
                    opportunist "But extremely not good for us!\n"
                else:
                    voice "audio/voices/ch3/thorn/cheated/34.flac"
                    cheated "She's better at this game than we are.\n"
                    voice "audio/voices/ch3/thorn/opportunist/53.flac"
                    opportunist "But we're all losers now. Nobody wins! Nobody.\n"
                    voice "audio/voices/ch3/thorn/cheated/35.flac"
                    cheated "She wins if she gets what she wants. And it looks like what she wanted... was this.\n"
                voice "audio/voices/ch3/thorn/narrator/86.flac"
                show quiet creep3 onlayer back at Position(ypos=1125)
                show thorn d bloody onlayer back
                with Dissolve(0.5)
                n "Blood trickles down the corner of her mouth. Then flows from between her lips.\n"
                voice "audio/voices/ch3/thorn/narrator/87.flac"
                show thorn d bloody smile onlayer back
                with dissolve
                n "She smiles.\n"
                $ gallery_thorn.unlock_item(6)
                $ gallery_thorn.unlock_item(7)
                $ renpy.save_persistent()
                voice "audio/voices/ch3/thorn/princess/35.flac"
                show thorn d bloody smile talk onlayer back
                with dissolve
                p "There. Isn't this just perfect?\n"
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                hide thorn onlayer back
                show arms thorn d1 onlayer back at Position(ypos=1125)
                show thorn d bloody smile onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                $ renpy.pause(0.125)
                show arms thorn d2 onlayer back at Position(ypos=1125)
                show thorn d quiet onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                $ renpy.pause(0.125)
                show arms thorn d3 onlayer back at Position(ypos=1125)
                hide thorn onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                $ renpy.pause(0.125)
                show arms thorn d4 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                $ renpy.pause(0.125)
                hide arms onlayer back at Position(ypos=1125)
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
                if persistent.quick_menu:
                    $ quick_menu = True
                if loops_finished != 0:
                    truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                else:
                    truth "You do not have an opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
                $ thorn_end = "stuck"
                $ princess_kept += 1
                $ princess_deny += 1
                jump mirror_start
                # END



return
