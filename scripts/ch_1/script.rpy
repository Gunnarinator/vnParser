# The script of the game goes in this file.

init -999 python:

    def newest_slot_tuple():
        """
        Returns a tuple with the newest slot page and name.
        """
        newest = renpy.newest_slot()

        if newest is not None:
            page, name = newest.split("-")
            return (page, name)


    class Continue(Action):
        """
        Loads the last save file.
        """

        def __call__(self):

            if not self.get_sensitive():
                return

            # Assign variables from the tuple.
            newest_page, newest_name = newest_slot_tuple()

            # Load the file using the newest slot information.
            FileLoad(newest_name, confirm=False, page=newest_page, newest=True)()

        def get_sensitive(self):

            # Insensitive in-game.
            if not main_menu:
                return False

            # Insensitive during replay mode.
            if _in_replay:
                return False

            # Get the tuple.
            newest = newest_slot_tuple()

            # Insensitive if no new slot files.
            if newest is None:
                return False

            # Assign variables from the tuple.
            newest_page, newest_name = newest

            # Insensitive if the newest save is '_reload-*'
            if newest_page == '_reload':
                return False

            # This action returns true if the file is loadable.
            return FileLoadable(newest_name, page=newest_page)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The script of the game goes in this file.
init python:

    if renpy.variant("pc"):
        config.pad_bindings["pad_back_press"] = [ "quick_load", ]
        config.pad_bindings["pad_lefttrigger_pos"] = [ "self_voicing", ]


# the shader goes here!
    preferences.afm_after_click = True
    shader_debug_mode = False
    import datetime
    config.keymap["quick_save"] = ["K_F5"]
    config.keymap["quick_load"] = ["K_F9"]
    config.keymap['toggle_afm'].append("K_t")

    custom_keymap = renpy.Keymap(
        quick_save = QuickSave(),
        quick_load = QuickLoad()
    )

    config.underlay.append(custom_keymap)

    #def menu(items, **add_input):
    #    """Overwrites the default menu handler, thus allowing us to log the
    #    choice made by the player.
    #    The default menu handler is set to renpy.display_menu(), as seen in
    #    renpy/defaultstore.py.
    #    Implementation of this is based on delta's readback module."""
    #    rv = renpy.display_menu(items, **add_input)
    #    for item_text, choice_obj in items:
    #        if rv == choice_obj.value:
    #            log_menu_choice(item_text)
    #    return rv

    #def log_menu_choice(item_text):
    #    """Log a choice-menu choice, which is passed in as item_text.
    #    Implementation based on add_history() in renpy/character.py."""
    #    h = renpy.character.HistoryEntry()
    #    h.who = ""
    #    h.what = item_text
    #    h.what_args = []

    #    if renpy.game.context().rollback:
    #        h.rollback_identifier = renpy.game.log.current.identifier
    #    else:
    #        h.rollback_identifier = None

    #    _history_list.append(h)

    #    while len(_history_list) > renpy.config.history_length:
    #        _history_list.pop(0)

# The game starts here.
label splashscreen:

    default persistent.one_time_gallery_unlock_sync = False
    if renpy.variant("pc"):
        if persistent.one_time_gallery_unlock_sync == False:
            $ persistent.one_time_gallery_unlock_sync = True
            if achievement.has("ACH_CREDITS"):
                $ persistent.gallery_unlocked = True

    default language_string = "english"

    default voice_font = "DejaVuSans.ttf"


    $ renpy.save_persistent()
    $ config.menu_include_disabled = False
    default hoveredy = 100
    default small_yadj = False
    default option_length = 93
    default persistent.gimmick_gimmick_loaded = False
    default persistent.gimmick_quick_loaded = False
    default persistent.language_set = False
    if persistent.quiet_gimmick and renpy.variant("pc"):
        if renpy.list_saved_games("gimmick"):
            $ persistent.gimmick_gimmick_loaded = True
            $ persistent.quiet_gimmick_stage_2 = True
            $ renpy.load('gimmick')
            $ persistent.quiet_gimmick = False
        elif renpy.list_saved_games("quick-1$"):
            $ persistent.gimmick_quick_loaded = True
            $ persistent.quiet_gimmick_stage_2 = True
            $ renpy.load('quick-1')
            $ persistent.quiet_gimmick = False
        else:
            $ persistent.quiet_gimmick = False
            $ persistent.gimmick_quick_loaded = False
            $ persistent.gimmick_gimmick_loaded = False

    $ renpy.unlink_save("gimmick")

    $ persistent.gimmick_quick_loaded = False
    $ persistent.gimmick_gimmick_loaded = False
    # defining transforms that apply the shader

    default persistent.quick_menu = True

    default flash = Fade(.25, 0, .75, color="#fff")

    transform screenshake:
        linear 0.15 xoffset -5 yoffset -5
        linear 0.1 xoffset 10 yoffset 7
        linear 0.13 xoffset 2 yoffset -2
        linear 0.05 xoffset -1 yoffset 1
        linear 0.13 xoffset -8 yoffset -1
        linear 0.09 xoffset 3 yoffset 1
        linear 0.07 xoffset -2 yoffset -10
        linear 0.1 xoffset 6 yoffset 3
        linear 0.11 xoffset -5 yoffset 2
        linear 0.08 xoffset 5 yoffset -4
        linear 0.05 xoffset -6 yoffset -5
        linear 0.14 xoffset 5 yoffset 3
        linear 0.06 xoffset 1 yoffset -9
        linear 0.1 xoffset 10 yoffset 7
        repeat

    transform shaketiny:
        linear 0.05 xoffset -1 yoffset 1
        linear 0.13 xoffset -8 yoffset -1
        linear 0.09 xoffset 3 yoffset 1
        linear 0.07 xoffset -2 yoffset -10
        linear 0.1 xoffset 6 yoffset 3


    transform shakeshort:
        linear 0.15 xoffset -5 yoffset -5
        linear 0.1 xoffset 10 yoffset 7
        linear 0.13 xoffset 2 yoffset -2
        linear 0.05 xoffset -1 yoffset 1
        linear 0.13 xoffset -8 yoffset -1
        linear 0.09 xoffset 3 yoffset 1
        linear 0.07 xoffset -2 yoffset -10
        linear 0.1 xoffset 6 yoffset 3
        linear 0.11 xoffset -5 yoffset 2
        linear 0.08 xoffset 5 yoffset -4
        linear 0.05 xoffset -6 yoffset -5
        linear 0.14 xoffset 5 yoffset 3
        linear 0.06 xoffset 1 yoffset -9
        linear 0.1 xoffset 10 yoffset 7
        linear 0.1 xoffset 0 yoffset 0

    transform sway:
        linear 2.0 xoffset -10
        linear 2.5 xoffset 15
        repeat

    transform cage_big_sway:
        linear 3.0 xoffset -25
        linear 3.5 xoffset 18
        repeat

    transform cage_sway:
        linear 1.6 xoffset -5
        linear 2.5 xoffset 3
        repeat

    transform swayblur:
        linear 1.0 blur 16 xoffset -10
        linear 2.5 blur 5 xoffset 15
        repeat

    transform blurred:
        linear 1.0 blur 16
        linear 2.5 blur 37
        repeat

    transform cage_blur:
        linear 1.0 blur 16 xoffset -5
        linear 2.5 blur 5 xoffset 3
        repeat

    transform bigswayblur:
        linear 1.0 blur 65 xoffset -10 yoffset -5
        linear 2.5 blur 50 xoffset 15 yoffset 8
        linear 1.6 blur 42 xoffset -3 yoffset 12
        linear 2.9 blur 76 xoffset 7 yoffset 4
        repeat

    transform collapse:
        easein .15 yoffset -110
        easein 0.05 yoffset -100

    transform rise:
        easein .15 yoffset 10
        easein 0.05 yoffset 0

    transform chin:
        easein .15 yoffset -5

    transform bigchin:
        easein .15 yoffset -20

    transform up:
        easein .15 yoffset 60
        easein 0.05 yoffset 50

    transform distortion:
        shader "distortion_perlin"
        u_frame(4.)
        u_speed(0.15)
        u_distortion(0.0002)
        u_distortion2(0.0005)
        u_scale(1.5)
        u_scale2(200.0)
        u_interlacing(0.00010)
        u_interlacing_y(512.0)
        u_vignette(0.5)
        u_static(0.075)
        u_debug(1.0 if shader_debug_mode else 0.0)

    transform distortion_princess:
        shader "distortion_perlin"
        u_frame(4.)
        u_speed(0.15)
        u_distortion(0.0002)
        u_distortion2(0.0005)
        u_scale(1.5)
        u_scale2(200.0)
        u_interlacing(0.00010)
        u_interlacing_y(128.0)
        u_vignette(0.5)
        u_static(0.075)
        u_debug(1.0 if shader_debug_mode else 0.0)

    transform distortion_back:
        shader "distortion_perlin"
        u_frame(4.)
        u_speed(0.15)
        u_distortion(0.0002)
        u_distortion2(0.0005)
        u_scale(1.5)
        u_scale2(200.0)
        u_interlacing(0.00010)
        u_interlacing_y(512.0)
        u_vignette(0.5)
        u_static(0.075)
        u_debug(1.0 if shader_debug_mode else 0.0)

    transform distortion_fore:
        shader "distortion_perlin"
        u_frame(4.)
        u_speed(1.15)
        u_distortion(0.0006)
        u_distortion2(0.0010)
        u_scale(5.0)
        u_scale2(100.0)
        u_interlacing(0.00065)
        u_interlacing_y(64.0)
        u_vignette(0.5)
        u_static(0.075)
        #u_debug(1.0 if shader_debug_mode else 0.0)
        u_debug(0.0)

    transform strongwarp:
        shader "distortion_perlin"
        u_frame(4.)
        u_speed(1.15)
        u_distortion(0.0006)
        u_distortion2(0.0010)
        u_scale(5.0)
        u_scale2(100.0)
        u_interlacing(0.00065)
        u_interlacing_y(64.0)
        u_vignette(0.5)
        u_static(0.075)
        #u_debug(1.0 if shader_debug_mode else 0.0)
        u_debug(0.0)

    transform midwarp:
        shader "distortion_perlin"
        u_frame(4.)
        u_speed(1.15)
        u_distortion(0.0005)
        u_distortion2(0.0008)
        u_scale(4.0)
        u_scale2(100.0)
        u_interlacing(0.00065)
        u_interlacing_y(64.0)
        u_vignette(0.5)
        u_static(0.075)
        #u_debug(1.0 if shader_debug_mode else 0.0)
        u_debug(0.0)

    transform spectre_small_zoom:
        ease 0.5 zoom 1.05 yoffset 50

    transform zoom_fall:
        ease 0.5 yoffset -20

    transform spectre_small_zoom_instant:
        ease 0.5 zoom 1.05 yoffset 50

    transform apoth_zoom_in:
        ease 0.5 zoom 1.1 yoffset 100 xoffset -50

    transform apoth_zoom_fall:
        ease 2.0 zoom 1.1 yoffset 75 xoffset 50

    transform apoth_zoom_out:
        ease 0.5 zoom 1.0 yoffset -100 xoffset -200

    transform xflip:
        yzoom -1

    transform alpha_dragon:
        linear .3 alpha 0.1
        pause 0.1
        linear .2 alpha 0.9
        pause .2
        linear .2 alpha 0.5
        pause 0.15
        linear .2 alpha 0.8
        pause 0.05
        linear .2 alpha 0.3
        pause 0.12
        linear .2 alpha 1.0
        pause 0.1
        linear .2 alpha 0.6
        pause 0.13
        repeat

    transform alpha_dragon_safe:
        alpha 0.5

    transform alpha_dragon_delay:
        linear .45 alpha 0.8
        pause 0.1
        linear .3 alpha 0.4
        pause .2
        linear .16 alpha 0.7
        pause 0.15
        linear .2 alpha 0.2
        pause 0.05
        linear .2 alpha 0.3
        pause 0.12
        linear .23 alpha 1.0
        pause 0.1
        linear .2 alpha 0.6
        pause 0.13
        repeat

    transform zoom_in:
        ease 0.5 zoom 1.1

    transform zoom_instant:
        zoom 1.1

    transform big_zoom:
        ease 1.0 zoom 1.2 yoffset 200

    transform big_zoom_instant:
        zoom 1.2 yoffset 200

    transform small_zoom:
        ease 1.0 zoom 1.1 yoffset 100

    transform cage_zoom:
        ease 0.5 zoom 1.12 yoffset 100
        ease 0.15 zoom 1.10 yoffset 80

    transform tower_zoom1:
        ease 0.5 zoom 1.06 yoffset 10
        ease 0.15 zoom 1.05

    transform tower_zoom2:
        ease 0.5 zoom 1.11 yoffset 20
        ease 0.15 zoom 1.1

    transform tower_zoom3:
        ease 0.5 zoom 1.16
        ease 0.15 zoom 1.15

    transform zoom_out:
          ease 0.5 zoom 1.0

    transform zoom_out_far:
        ease 0.5 zoom 0.95



    default persistent.gallery_unlocked = False
    default persistent.death_count = 0
    $ preferences.text_cps = 0
    $ config.default_text_cps = 0
    define config.nw_voice = True
    $ achievement.sync()
    scene bg black
    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop
    if persistent.language_set == False:
        call screen language_select with fade

    scene bg black with fade
    show splashscreen logo at distortion with Dissolve(1.5)
    $ renpy.pause(2.0)
    scene bg black with fade
    show splashscreen serenity at distortion with Dissolve(1.5)
    $ renpy.pause(2.0)
    #show text "{color=#FFFFFF00}Slay the Princess is a horror game, and is not intended for all audiences. Please visit our website www.blacktabbygames.com if you need a list of specific content warnings.{/color}"
    scene bg black
    show text _("{color=#D9D9D9}{size=72}CONTENT WARNING{/size}\n\n\n{size=48}This is a horror game, and is not intended for all audiences. Please visit our website www.blacktabbygames.com if you need a list of specific content warnings.{/size}\n\n\n{size=48}Slay the Princess contains flickering image effects as well as a parallax effect that on rare occasions has caused motion sickness in players.{/size}\n\n\n{size=48}If either of these effects cause health issues for you, you can disable them in the game's preferences.{/size}{/color}") at Position(ypos=500)

    #scene splashscreen content warning with fade
    with fade
    if _preferences.afm_enable:
        $ renpy.pause(12.0)
    else:
        $ renpy.pause()
    scene bg black
    show text _("{color=#D9D9D9}{size=56}Whatever horrors you may find in these dark spaces,\nhave heart and see them through.{/size}\n\n\n{size=46}There are no premature endings. There are no wrong decisions.\n\n\nThere are only fresh perspectives and new beginnings.{/size}\n\n\n\n{size=64}This is a love story.{/size}{/color}") at Position(ypos=500)
    with fade
    if _preferences.afm_enable:
        $ renpy.pause(8.0)
    else:
        $ renpy.pause()
    hide text
    stop sound fadeout(2.0)
    return

label start:

    hide screen keymap_screen
    show screen keymap_screen
    #jump credits
    $ quick_menu = False
    $ _window_during_transitions = True
    window show
    default persistent.performance_mode = False
    default persistent.parallax_on = True
    default persistent.flickering = True

    default persistent.tooltip_shown = False

    $ current_loop = 1

    stop music fadeout 1.0
    $ quick_menu = False
    $ current_princess = "base"
    $ trait_hero = True
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter princess with fade
    show text _("{color=#FFFFFF00}Chapter One. The Hero and the Princess.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    scene bg black
    stop sound fadeout 1.0

    #jump testing_ground
    #jump pristine_climax_images
    #play music "audio/_music/mound/Transformation Intro.flac"
    #queue music "audio/_music/mound/Transformation Loop.flac" loop
    #jump felina_godkiller_ending


    # revert next line later
    play music "audio/_music/ch1/The Princess.flac" loop

    scene bg path onlayer farback at flip, Position(ypos=1125)
    show midground path onlayer back at flip, Position(ypos=1125)
    show front path onlayer front at flip, Position(ypos=1125)

    show bg black
    ##show loading_icon
    hide chapter
    with fade

    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"

    if persistent.quick_menu:
        $ quick_menu = True

    if loops_finished > 0 or loops_destroyed > 0:
        $ achievement.grant("ACH_SOULS")

    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a princess.\n"

    # GALLERY UNLOCK TEST
    #$gallery_ztlq.unlock_gallery()
    #$gallery_zfinale.unlock_gallery()
    #$gallery_adversary.unlock_gallery()
    #$gallery_apotheosis.unlock_gallery()
    #$gallery_beast.unlock_gallery()
    #$gallery_cage.unlock_gallery()
    #$gallery_clarity.unlock_gallery()
    #$gallery_damsel.unlock_gallery()
    #$gallery_den.unlock_gallery()
    #$gallery_dragon.unlock_gallery()
    #$gallery_fury.unlock_gallery()
    #$gallery_grey.unlock_gallery()
    #$gallery_happy.unlock_gallery()
    #$gallery_needle.unlock_gallery()
    #$gallery_nightmare.unlock_gallery()
    #$gallery_prisoner.unlock_gallery()
    #$gallery_razor.unlock_gallery()
    #$gallery_spectre.unlock_gallery()
    #$gallery_stranger.unlock_gallery()
    #$gallery_thorn.unlock_gallery()
    #$gallery_tower.unlock_gallery()
    #$gallery_witch.unlock_gallery()
    #$gallery_wraith.unlock_gallery()
    #$gallery_wild.unlock_gallery()


    $gallery_zch1.unlock_gallery()
    $gallery_zch1.unlock_item(1)
    $renpy.save_persistent()

    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her. If you don't, it will be the end of the world.\n"

    if persistent.tooltip_shown == False and (loops_finished >= 1 or loops_destroyed >= 1):
        $ persistent.tooltip_shown = True
        if renpy.variant("console_nintendo_switch"):
            truth "Note: You can skip previously seen dialogue by hitting the R button on your controller.\n"
        elif renpy.variant("console_sony_ps5") or renpy.variant("console_sony_ps4"):
            truth "Note: You can skip previously seen dialogue by hitting R1 on your controller.\n"
        elif renpy.variant("console_xbox"):
            truth "Note: You can skip previously seen dialogue by hitting RB on your controller.\n"
        else:
            truth "Note: You can skip previously seen dialogue by hitting 'TAB' on your keyboard, or 'R1' on your controller.\n"
        n "You're here to slay her. If you don't, it will be the end of the world.{fast}\n"
    $ forest_1_questioning_start == False
    $ forest_1_questioning_followup == False
    $ forest_1_questioning_evidence == False
    $ forest_1_conscientious_objector_explore == False
    $ forest_1_someone_else_explore == False
    $ forest_1_refuse_explore == False
    $ forest_1_why_dangerous == False
    $ forest_1_what_happens == False
    $ forest_1_casuality_explore == False
    $ forest_1_let_it_burn == False
    $ forest_1_reluctant_visit == False

    default ch1_can_cabin = True
    if adversary_encountered and prisoner_encountered and tower_encountered and spectre_encountered and razor_encountered and nightmare_encountered and damsel_encountered and beast_encountered and witch_encountered:
        $ ch1_can_cabin = False
    $ config.menu_include_disabled = False
    label forest_dialogue:
        default forest_1_questioning_start = False
        default forest_1_questioning_followup = False
        default forest_1_questioning_evidence = False
        default forest_1_conscientious_objector_explore = False
        default forest_1_someone_else_explore = False
        default forest_1_refuse_explore = False
        default forest_1_why_dangerous = False
        default forest_1_what_happens = False
        default forest_1_casuality_explore = False
        default forest_1_let_it_burn = False
        default forest_1_reluctant_visit = False
        default forest_1_prize = False
        default forest_1_prize_follow_up = False
        menu:

            extend ""

            "{i}• (Explore) The end of the world? What are you talking about?{/i}" if forest_1_questioning_start == False:
                $ forest_1_questioning_start = True
                voice "audio/voices/ch1/woods/narrator/script_n_3.flac"
                n "I'm talking about the end of everything as we know it. No more birds, no more trees, and, perhaps most problematically of all, no more people. You have to put an end to her.\n"
                jump forest_dialogue

            "{i}• (Explore) But how can a princess locked away in a basement end the world?{/i}" if forest_1_questioning_start and forest_1_questioning_followup == False:
                $ forest_1_questioning_followup = True
                voice "audio/voices/ch1/woods/narrator/script_n_4.flac"
                n "Don't linger on the specifics. You have a job to do here. Just get in there and do what needs to be done. We're all counting on you.\n"
                jump forest_dialogue

            "{i}• (Explore) If you don't tell me why she's dangerous, I'm not going to kill her.{/i}" if forest_1_questioning_start and forest_1_questioning_followup == False:
                $ forest_1_why_dangerous = True
                $ forest_1_questioning_followup = True
                voice "audio/voices/ch1/woods/narrator/script_n_5.flac"
                n "{i}She's{/i} not dangerous. She's just a princess. The danger comes if she gets out. Which she will. Unless {i}you{/i} do something about it.\n"
                jump forest_dialogue

            "{i}• (Explore) Okay. What happens if she gets out then? I want specifics.{/i}" if forest_1_why_dangerous and forest_1_what_happens == False:
                $ forest_1_what_happens = True
                voice "audio/voices/ch1/woods/narrator/script_n_6.flac"
                n "The more specifics you have, the harder it will be for you to do this very important job. She's a princess. People will listen to her, because listening to her is in their nature. And when they do, everything will come crashing down.\n"
                jump forest_dialogue

            "{i}• (Explore) Do you have any evidence to back this up?{/i}" if forest_1_questioning_evidence == False and forest_1_questioning_start:
                $ forest_1_questioning_evidence = True
                voice "audio/voices/ch1/woods/narrator/script_n_7.flac"
                n "Look, you're already on the path that leads to the cabin. Why would you be here if it weren't to complete a very important task? You've made it this far, you might as well reach the end of your journey.\n"
                jump forest_dialogue

            "{i}• (Explore) Have you considered that maybe the only reason she's going to end the world is {b}because{/b} she's locked up?{/i}" if forest_1_casuality_explore == False:
                $ forest_1_casuality_explore = True
                voice "audio/voices/ch1/woods/narrator/script_n_8.flac"
                n "While I appreciate the mental exercise, we are running up against a bit of a ticking clock.\n"
                voice "audio/voices/ch1/woods/narrator/script_n_9.flac"
                n "Nevertheless, let me assure you: the Princess is locked up because she's dangerous, she is not dangerous because she's locked up.\n"
                voice "audio/voices/ch1/woods/narrator/script_n_10.flac"
                n "And before you decide to waste even more of our time by asking how I know that, let me suggest a more pragmatic lens through which to view this situation.\n"
                voice "audio/voices/ch1/woods/narrator/script_n_11.flac"
                n "Causality doesn't matter here, because the end result is the same no matter what led us up to this point. If the Princess leaves the cabin, the world will end, and there is no changing that.\n"
                voice "audio/voices/ch1/woods/narrator/script_n_12.flac"
                n "It's no use arguing semantics over a metaphorical chicken-or-egg, because the egg is hatched and it's about to ruin everything.\n"
                voice "audio/voices/ch1/woods/narrator/script_n_13.flac"
                n "Unless, of course, you do your job and {i}slay her{/i}.\n"
                jump forest_dialogue

            "{i}• (Explore) Killing a princess seems kind of bad, though, doesn't it?{/i}" if forest_1_conscientious_objector_explore == False:
                $ forest_1_conscientious_objector_explore = True
                voice "audio/voices/ch1/woods/narrator/script_n_14.flac"
                n "Does it? Are you a monarchist? Is slaying a princess that much worse than slaying a fisherman or a miller or a seamstress? \nIf anything, slaying a princess is much {i}better{/i} than slaying a seamstress. \nSeamstresses contribute something of value to society.\n"
                jump forest_dialogue

            "{i}• (Explore) Can't someone else do this?{/i}" if forest_1_someone_else_explore == False:
                $ forest_1_someone_else_explore = True
                if forest_1_questioning_followup:
                    voice "audio/voices/ch1/woods/narrator/script_n_15.flac"
                    n "Oh, if only that were the case, but I don't make the rules.\n"
                    voice "audio/voices/ch1/woods/narrator/script_n_16.flac"
                    n "I have to say I'm surprised at your reluctance thus far. But unfortunately for the both of us, you're the only one who can pull this off.\n"
                    voice "audio/voices/ch1/woods/narrator/script_n_17.flac"
                    n "Like I said, I don't make the rules. No matter how much I wish I did.\n"
                else:
                    voice "audio/voices/ch1/woods/narrator/script_n_18.flac"
                    n "Unfortunately, you're the only one who can pull this off. I don't make the rules. I wish I did, but I don't.\n"
                jump forest_dialogue

            "{i}• (Explore) Forget it, I'm not doing this.{/i}" if forest_1_refuse_explore == False:
                $ forest_1_refuse_explore = True
                voice "audio/voices/ch1/woods/narrator/script_n_19.flac"
                n "Are you serious? No, you {i}have{/i} to do it.\n"
                jump forest_dialogue

            "{i}• (Explore) Have you considered that maybe I'm okay with the world ending?{/i}" if forest_1_let_it_burn == False:
                $ forest_1_let_it_burn = True
                voice "audio/voices/ch1/woods/narrator/script_n_20.flac"
                n "Of course I haven't. Why would I even consider that? {i}Nobody{/i} wants the world to end.\n"
                voice "audio/voices/ch1/woods/narrator/script_n_21.flac"
                n "I mean, maybe {i}some{/i} people do, like nihilists or very very evil people, but surely you're not one of those... right?\n"
                jump forest_dialogue

            "{i}• (Explore) Do I get some sort of reward for doing this?{/i}" if forest_1_prize == False:
                $ forest_1_prize = True
                voice "audio/voices/ch1/woods/narrator/s1.flac"
                n "Yes, but you'll have to slay her before you get it.\n"
                jump forest_dialogue

            "{i}• (Explore) Can you tell me what my prize is going to be for doing a good job?{/i}" if forest_1_prize and forest_1_prize_follow_up == False:
                $ forest_1_prize_follow_up = True
                voice "audio/voices/ch1/woods/narrator/s2.flac"
                n "It's a secret, but I think you'll like it. It's a special reward, just for you. And whatever you think it might be, I can promise you it's going to be even better than your wildest imagination.\n"
                jump forest_dialogue

            "{i}• Look, I'll go to the cabin and I'll talk to her, and if she's as bad as you say she is then {b}maybe{/b} I'll slay her. But I'm not committing to anything until I've had the chance to meet her face to face.{/i}" if (forest_1_refuse_explore or forest_1_questioning_start) and ch1_can_cabin:
                default forest_1_web_of_lies = False
                $ forest_1_reluctant_visit = True
                $ forest_1_web_of_lies = True
                voice "audio/voices/ch1/woods/narrator/script_n_22.flac"
                n "Then I guess we'll just have to see what happens. But a word of warning— if you go in prepared to hear her out, she could easily trap you in her web of lies. And the more you listen to her honeyed words, the harder it'll be to pull yourself out.\n"
                voice "audio/voices/ch1/woods/narrator/script_n_23.flac"
                n "Then each and every one of us is doomed.\n"
                voice "audio/voices/ch1/woods/narrator/script_n_24.flac"
                n "So, sure, go talk to her. See how that turns out for all of us.\n"

            "{i}• Okay. Fine. I'll go to the cabin.{/i}" if forest_1_refuse_explore and ch1_can_cabin:
                jump start_get_this_over_with_join

            "{i}• Okay, I'm sold. Let's get this over with.{/i}" if forest_1_questioning_start and ch1_can_cabin:
                label start_get_this_over_with_join:
                    voice "audio/voices/ch1/woods/narrator/script_n_25.flac"
                    n "Good. As long as you remain focused on your goal, it should all be smooth sailing.\n"
                jump cabin_arrival_1

            "{i}• Oh, okay. Thanks for telling me what to do.{/i}" if ch1_can_cabin:
                voice "audio/voices/ch1/woods/narrator/script_n_26.flac"
                n "Don't mention it. It's all part of the job.\n"
                jump cabin_arrival_1

            "{i}• Sweet! I've always wanted to off a monarch. Viva la revolución!{/i}" if forest_1_conscientious_objector_explore == False and ch1_can_cabin:
                voice "audio/voices/ch1/woods/narrator/script_n_27.flac"
                n "That's the spirit!\n"
                jump cabin_arrival_1

            "{i}• [[Silently continue to the cabin.]{/i}" if ch1_can_cabin:
                jump cabin_arrival_1

            "{i}• [[Turn around and leave.]{/i}" if stranger_encountered == False:
                default forest_1_leave_attempt = False
                $ forest_1_leave_attempt = True
                label turn_and_leave_join:
                    voice "audio/voices/ch1/woods/narrator/script_n_28.flac"
                    n "Seriously? You're just going to turn around and leave? Do you even know where you're going?\n"
                    #if ch1_can_cabin == False:
                    #    $ config.menu_include_disabled = True
                    menu:

                        extend ""

                        "{i}• Okay, fine. You're persistent. I'll go to the cabin and I'll slay the Princess. Ugh!{/i}" if ch1_can_cabin:
                            voice "audio/voices/ch1/woods/narrator/script_n_29.flac"
                            n "{i}Thank you{/i}! The whole world owes you a debt of gratitude. Really.\n"
                            if current_loop == 2:
                                if trait_stubborn:
                                    voice "audio/voices/ch1/voices/ch1_stubborn_1.flac"
                                    stubborn "Oh, about {i}time{/i}. I can't believe you were about to run away.\n"
                                elif trait_hunted:
                                    voice "audio/voices/ch1/voices/ch1_hunted_1.flac"
                                    hunted "If this is what you think is best, I'll keep my ears pricked. Hopefully she won't catch us off-guard as easily as she did last time...\n"
                                elif trait_smitten:
                                    voice "audio/voices/ch1/voices/ch1_smitten_1.flac"
                                    smitten "Save. You'll go to the cabin and {i}save{/i} the Princess.\n"
                                elif trait_paranoid:
                                    voice "audio/voices/ch1/voices/ch1_paranoid_1.flac"
                                    paranoid "One little trick was all it took for you to go in there?\n"
                                    voice "audio/voices/ch1/voices/ch1_paranoid_2.flac"
                                    paranoid "{i}Sigh{/i}. I guess you're the one in control aren't you? So if you want us to die again, I guess we'll die again. Good luck. To all of us.\n"
                                elif trait_skeptic:
                                    voice "audio/voices/ch1/voices/ch1_skeptic_1.flac"
                                    skeptic "Good. Going back to the cabin is the only way we can get to the bottom of things.\n"
                                elif trait_flinching:
                                    voice "audio/voices/ch1/voices/ch1_flinching_1.flac"
                                    flinching "No, no, {i}no{/i} what are you doing, we were so close to getting out of here!\n"
                                elif trait_cold:
                                    voice "audio/voices/ch1/voices/ch1_cold_1.flac"
                                    cold "Oh well, cabin it is.\n"
                                elif trait_opportunist:
                                    voice "audio/voices/ch1/voices/ch1_opportunist_1.flac"
                                    opportunist "This is probably for the best.\n"
                                elif trait_broken:
                                    voice "audio/voices/ch1/voices/ch1_broken_1.flac"
                                    broken "So much for getting out of here...\n"
                                $ stranger_override = False
                                jump chapter_2_stranger_rejoin_1
                            jump cabin_arrival_1

                        "{i}• Okay, fine. I'll go to the cabin and I'll talk to the Princess. Maybe I'll slay her. Maybe I won't. I guess we'll see.{/i}" if ch1_can_cabin:
                            voice "audio/voices/ch1/woods/narrator/script_n_30.flac"
                            n "I guess we will.\n"
                            if current_loop == 2:
                                $ stranger_override = False
                                if trait_stubborn:
                                    voice "audio/voices/ch1/voices/ch1_stubborn_1.flac"
                                    stubborn "Oh, about {i}time{/i}. I can't believe you were about to run away.\n"
                                elif trait_hunted:
                                    voice "audio/voices/ch1/voices/ch1_hunted_1.flac"
                                    hunted "If this is what you think is best, I'll keep my ears pricked. Hopefully she won't catch us off-guard as easily as she did last time...\n"
                                elif trait_smitten:
                                    voice "audio/voices/ch1/voices/ch1_smitten_2.flac"
                                    smitten "You're joking, right? If we're going to the cabin, there's no world where we do anything other than {i}save{/i} her.\n"
                                elif trait_paranoid:
                                    voice "audio/voices/ch1/voices/ch1_paranoid_1.flac"
                                    paranoid "One little trick was all it took for you to go in there?\n"
                                    voice "audio/voices/ch1/voices/ch1_paranoid_2.flac"
                                    paranoid "{i}Sigh{/i}. I guess you're the one in control aren't you? So if you want us to die again, I guess we'll die again. Good luck. To all of us.\n"
                                elif trait_skeptic:
                                    voice "audio/voices/ch1/voices/ch1_skeptic_1.flac"
                                    skeptic "Good. Going back to the cabin is the only way we can get to the bottom of things.\n"
                                elif trait_flinching:
                                    voice "audio/voices/ch1/voices/ch1_flinching_1.flac"
                                    flinching "No, no, {i}no{/i} what are you doing, we were so close to getting out of here!\n"
                                elif trait_cold:
                                    voice "audio/voices/ch1/voices/ch1_cold_1.flac"
                                    cold "Oh well, cabin it is.\n"
                                elif trait_opportunist:
                                    voice "audio/voices/ch1/voices/ch1_opportunist_1.flac"
                                    opportunist "This is probably for the best.\n"
                                elif trait_broken:
                                    voice "audio/voices/ch1/voices/ch1_broken_1.flac"
                                    broken "So much for getting out of here...\n"
                                jump chapter_2_stranger_rejoin_1
                            jump cabin_arrival_1

                        "{i}• (Lie) Yes, I definitely know where I'm going.{/i}":
                            voice "audio/voices/ch1/woods/narrator/script_n_31.flac"
                            n "Somehow I doubt that, but fine.\n"
                            play audio "audio/one_shot/footsteps_hike_short.flac"
                            voice "audio/voices/ch1/woods/narrator/script_n_32.flac"
                            hide bg onlayer farback
                            hide midground onlayer back
                            hide front onlayer front
                            scene bg path onlayer farback at Position(ypos=1125)
                            show midground path onlayer back at Position(ypos=1125)
                            show front path onlayer front at Position(ypos=1125)
                            with fade
                            n "I suppose you just quietly continue down the path away from the cabin.\n"
                            jump turn_around_1_late_join

                        "{i}• Nope!{/i}":
                            jump turn_around_1

                        "{i}• The only thing that matters is where I'm not going. (The cabin. I am not going to the cabin.){/i}":
                            jump turn_around_1

                        "{i}• It's like I said, I'm pretty okay with the world ending. I relish the coming of a new dawn beyond our own.{/i}" if forest_1_let_it_burn:
                            jump forest_1_nihilism_walk

                        "{i}• I'm actually pretty okay with the world ending. I relish the coming of a new dawn beyond our own. Gonna go walk in the opposite direction now!{/i}" if forest_1_let_it_burn == False:
                            label forest_1_nihilism_walk:
                                play audio "audio/one_shot/footsteps_hike_short.flac"
                                voice "audio/voices/ch1/woods/narrator/script_n_33.flac"
                                n "There won't {i}be{/i} a 'new dawn' if the world ends. There'll just be {i}nothing{/i}. Forever!\n"
                            jump turn_around_1

                        "{i}• [[Quietly continue down the path away from the cabin.]{/i}":
                            label turn_around_1:
                                default forest_1_flee_hero_spoke = False
                                $ forest_1_flee_hero_spoke = True
                                $ quick_menu = False
                                play audio "audio/one_shot/footsteps_hike_short.flac"
                                voice "audio/voices/ch1/woods/narrator/script_n_34.flac"
                                hide bg onlayer farback
                                hide midground onlayer back
                                hide front onlayer front
                                scene bg path onlayer farback at Position(ypos=1125)
                                show midground path onlayer back at Position(ypos=1125)
                                show front path onlayer front at Position(ypos=1125)
                                with fade
                                if persistent.quick_menu:
                                    $ quick_menu = True
                                n "Fine, I suppose you just quietly continue down the path away from the cabin.\n"
                                label turn_around_1_late_join:
                                    if current_loop == 1:
                                        voice "audio/voices/ch1/woods/hero/script_h_1.flac"
                                        hero "Good. What we're being asked to do here is {i}wrong{/i}. Better to wash our hands of this whole situation than to take part in it.\n"
                                        voice "audio/voices/ch1/woods/narrator/script_n_35.flac"
                                        n "Ignore that annoying little voice. He doesn't know what he's talking about.\n"

                                    $gallery_zch1.unlock_item(2)
                                    $renpy.save_persistent()
                                    play audio "audio/one_shot/footsteps_hike_short.flac"
                                    voice "audio/voices/ch1/woods/narrator/script_n_36.flac"
                                    $ quick_menu = False
                                    hide bg onlayer farback
                                    hide midground onlayer back
                                    hide front onlayer front
                                    with fade
                                    scene skyline cabin onlayer farback at Position(ypos = 1080)
                                    show bg cabin onlayer back at Position(ypos = 1200)
                                    show midground cabin onlayer front at Position(ypos = 1140)
                                    show foreground cabin onlayer inyourface at Position(ypos = 1120)
                                    with fade
                                    if persistent.quick_menu:
                                        $ quick_menu = True
                                    n "That's strange. It looks like this path also leads to the cabin. How convenient! Everything's back on track again. Maybe the world can still be saved after all.\n"
                                    if trait_cold:
                                        voice "audio/voices/ch1/voices/ch1_cold_2.flac"
                                        cold "Oh? How quaint. He really wants us to go in there, doesn't he?\n"
                                    menu:
                                        extend ""

                                        "{i}• Okay, okay! I'm going into the cabin. Sheesh.{/i}" if ch1_can_cabin:
                                            voice "audio/voices/ch1/woods/narrator/script_n_37.flac"
                                            n "That's great to hear! And as long as you bring that fiery attitude to Princess slaying, I think this will all resolve splendidly.\n"
                                            if current_loop == 2:
                                                $ stranger_override = False
                                                if trait_stubborn:
                                                    voice "audio/voices/ch1/voices/ch1_stubborn_1.flac"
                                                    stubborn "Oh, about {i}time{/i}. I can't believe you were about to run away.\n"
                                                elif trait_hunted:
                                                    voice "audio/voices/ch1/voices/ch1_hunted_1.flac"
                                                    hunted "If this is what you think is best, I'll keep my ears pricked. Hopefully she won't catch us off-guard as easily as she did last time...\n"
                                                elif trait_smitten:
                                                    voice "audio/voices/ch1/voices/ch1_smitten_3.flac"
                                                    smitten "Oh, it's going to resolve splendidly, all right.\n"
                                                elif trait_paranoid:
                                                    voice "audio/voices/ch1/voices/ch1_paranoid_3.flac"
                                                    paranoid "A couple of laps around the woods were all it took for you to go in there?\n"
                                                    voice "audio/voices/ch1/voices/ch1_paranoid_2.flac"
                                                    paranoid "{i}Sigh{/i}. I guess you're the one in control aren't you? So if you want us to die again, I guess we'll die again. Good luck. To all of us.\n"
                                                elif trait_skeptic:
                                                    voice "audio/voices/ch1/voices/ch1_skeptic_1.flac"
                                                    skeptic "Good. Going back to the cabin is the only way we can get to the bottom of things.\n"
                                                elif trait_flinching:
                                                    voice "audio/voices/ch1/voices/ch1_flinching_1.flac"
                                                    flinching "No, no, {i}no{/i} what are you doing, we were so close to getting out of here!\n"
                                                    #flinching "No, no, {i}no{/i} what are you doing, I'm sure if we just looked harder we'd find a way out of here!\n"
                                                elif trait_cold:
                                                    voice "audio/voices/ch1/voices/ch1_cold_1.flac"
                                                    cold "Oh well, cabin it is.\n"
                                                elif trait_opportunist:
                                                    voice "audio/voices/ch1/voices/ch1_opportunist_1.flac"
                                                    opportunist "This is probably for the best.\n"
                                                elif trait_broken:
                                                    voice "audio/voices/ch1/voices/ch1_broken_1.flac"
                                                    broken "So much for getting out of here...\n"
                                                jump chapter_2_stranger_rejoin
                                            voice "audio/voices/ch1/woods/narrator/script_n_38.flac"
                                            n "A warning, before you go any further...\n"
                                            voice "audio/voices/ch1/woods/narrator/script_n_39.flac"
                                            n "She will lie, she will cheat, and she will do everything in her power to stop you from slaying her. Don't believe a word she says."
                                            voice "audio/voices/ch1/woods/narrator/script_n_40.flac"
                                            n "Fortunately, she's only a Princess, whereas you are a valiant and talented warrior. It'll be {i}easy{/i} so long as you stay focused.\n"
                                            voice "audio/voices/ch1/woods/hero/script_h_2.flac"
                                            hero "We can't just go through with this and listen to Him. She's a princess. We're supposed to save princesses, not slay them.\n"
                                            #voice "audio/voices/ch1/woods/narrator/script_n_41.flac"
                                            #n "Ignore that annoying little voice. He doesn't know what he's talking about.\n"
                                            jump cabin_arrival_1_menu

                                        "{i}• [[Turn around (again) and leave (again.)]{/i}":

                                            voice "audio/voices/ch1/woods/narrator/script_n_42.flac"
                                            n "You're really keen on wasting everyone's time, aren't you? It's remarkably selfish, if you ask me. I've already outlined the stakes of the situation. If you don't do your job, everyone dies.\nLike, {i}dies{/i} dies. Forever.\n"
                                            if current_loop != 2:
                                                menu:
                                                    extend ""

                                                    "{i}• I don't care! I'm not killing a princess!{/i}":
                                                        voice "audio/voices/ch1/woods/narrator/script_n_43.flac"
                                                        n "'Killing' is such gauche phrasing, and completely ignores the bigger picture. Your task is to {i}slay{/i} the Princess. Because she's terrible and she's really got it coming to her.\n"

                                                    "{i}• Good! Maybe everyone {b}should{/b} die! It's what they get for dumping me in the woods and asking me to {b}kill{/b} someone for them.{/i}":
                                                        voice "audio/voices/ch1/woods/narrator/script_n_44.flac"
                                                        n "When I said everyone, I meant {i}everyone{/i}. That's a pretty large group to just condemn to death over a single Princess.\n"
                                                        voice "audio/voices/ch1/woods/narrator/script_n_45.flac"
                                                        n "And last I checked you're a part of everyone, too, so if you think about it, walking up to that cabin and slaying her is really in {i}your{/i} best interests as well.\n"

                                                    "{i}• You're not emotionally blackmailing me into doing this!{/i}":
                                                        voice "audio/voices/ch1/woods/narrator/script_n_46.flac"
                                                        n "Stakes and consequences aren't emotional blackmail. They're facts of life, and if you had an ounce of maturity you'd understand that.\n"

                                                    "{i}• [[Quietly continue down the path.]{/i}":
                                                        voice "audio/voices/ch1/woods/narrator/script_n_47.flac"
                                                        n "Your silence is deafening."

                                            play audio "audio/one_shot/footsteps_hike_short.flac"
                                            voice "audio/voices/ch1/woods/narrator/script_n_48.flac"
                                            $ quick_menu = False
                                            hide skyline onlayer farback
                                            hide bg onlayer back
                                            hide midground onlayer front
                                            hide foreground onlayer inyourface
                                            with fade
                                            scene bg path onlayer farback at Position(ypos=1125)
                                            show midground path onlayer back at Position(ypos=1125)
                                            show front path onlayer front at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "But fine. You turn around and trek back down the path you came."
                                            # if you're on chapter 2 this takes you to CAUGHT
                                            if current_loop == 2:
                                                stop music fadeout 10.0
                                                stop sound fadeout 20.0
                                                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                                                jump caught_start

                                            play audio "audio/one_shot/footsteps_hike_short.flac"
                                            voice "audio/voices/ch1/woods/narrator/script_n_49.flac"
                                            hide bg onlayer farback
                                            hide midground onlayer back
                                            hide front onlayer front
                                            with fade
                                            scene skyline cabin onlayer farback at Position(ypos = 1080)
                                            show bg cabin onlayer back at Position(ypos = 1200)
                                            show midground cabin onlayer front at Position(ypos = 1140)
                                            show foreground cabin onlayer inyourface at Position(ypos = 1120)
                                            with fade
                                            n "Oh, would you look at that! You're at the cabin again! Now, I'm not normally one for superstition or astrology, but I have to say, it seems like the Universe itself is doing its best to bring you to your fated confrontation with the Princess.\n"
                                            if trait_stubborn:
                                                voice "audio/voices/ch1/voices/ch1_stubborn_2.flac"
                                                stubborn "I guarantee you that every second you spend running away is time She's going to use to get {i}stronger{/i}. Just get in there already!\n"
                                            elif trait_hunted:
                                                voice "audio/voices/ch1/voices/ch1_hunted_2.flac"
                                                hunted "It's like we're being herded back here time and time again... I don't know if our guide is the one doing this, or if He's as helpless to shape this place as we are.\n"
                                                #hero "Maybe this is the safest way forward for us.\n"
                                                #voice "audio/voices/ch1/voices/ch1_hunted_3.flac"
                                                #hunted "I don't think anything is safe in this place.\n"
                                            elif trait_smitten:
                                                voice "audio/voices/ch1/voices/ch1_smitten_4.flac"
                                                smitten "He's right, you know, at least about the universe bringing us back here. It's our destiny to save her from this place.\n"
                                                n "You don't even know her.\n"
                                            elif trait_paranoid:
                                                voice "audio/voices/ch1/voices/ch1_paranoid_4.flac"
                                                paranoid "He's being so infuriatingly obvious. Keep moving. Don't go in there. He's bound to break eventually.\n"
                                            elif trait_skeptic:
                                                voice "audio/voices/ch1/voices/ch1_skeptic_2.flac"
                                                skeptic "Is He the one pulling the strings here, or is this the work of something else entirely?\n"
                                            elif trait_flinching:
                                                voice "audio/voices/ch1/voices/ch1_flinching_2.flac"
                                                flinching "I don't care how many times we keep winding up here, we can't go into that place. We just can't!\n"
                                            elif trait_opportunist:
                                                voice "audio/voices/ch1/voices/ch1_opportunist_2.flac"
                                                opportunist "Well, if the {i}universe{/i} wants us to go in there...\n"
                                            elif trait_broken:
                                                voice "audio/voices/ch1/voices/ch1_broken_2.flac"
                                                broken "He's right. There's no use trying to get out of this place, is there? It's like reality itself wants us to die all over again...\n"
                                            menu:
                                                extend ""

                                                "{i}• There's no fighting this, is there? I have to go into the cabin, don't I? Fine.{/i}" if ch1_can_cabin:
                                                    voice "audio/voices/ch1/woods/narrator/script_n_50.flac"
                                                    n "There's always a choice, but let me tell you right now that you're making the correct decision for pretty much everyone.\n"
                                                    if current_loop == 2:
                                                        $ stranger_override = False
                                                        if trait_stubborn:
                                                            voice "audio/voices/ch1/voices/ch1_stubborn_1.flac"
                                                            stubborn "Oh, about {i}time{/i}. I can't believe you were about to run away.\n"
                                                        elif trait_hunted:
                                                            voice "audio/voices/ch1/voices/ch1_hunted_1.flac"
                                                            hunted "If this is what you think is best, I'll keep my ears pricked. Hopefully she won't catch us off-guard as easily as she did last time...\n"
                                                        elif trait_paranoid:
                                                            voice "audio/voices/ch1/voices/ch1_paranoid_2.flac"
                                                            paranoid "{i}Sigh{/i}. I guess you're the one in control aren't you? So if you want us to die again, I guess we'll die again. Good luck. To all of us.\n"
                                                        elif trait_skeptic:
                                                            voice "audio/voices/ch1/voices/ch1_skeptic_1.flac"
                                                            skeptic "Good. Going back to the cabin is the only way we can get to the bottom of things.\n"
                                                        elif trait_flinching:
                                                            voice "audio/voices/ch1/voices/ch1_flinching_1.flac"
                                                            flinching "No, no, {i}no{/i} what are you doing, we were so close to getting out of here!\n"
                                                            #flinching "No, no, {i}no{/i} what are you doing, I'm sure if we just looked harder we'd find a way out of here!\n"
                                                        elif trait_cold:
                                                            voice "audio/voices/ch1/voices/ch1_cold_1.flac"
                                                            cold "Oh well, cabin it is.\n"
                                                        elif trait_opportunist:
                                                            voice "audio/voices/ch1/voices/ch1_opportunist_3.flac"
                                                            opportunist "Eh, this is probably for the best.\n"
                                                        elif trait_broken:
                                                            voice "audio/voices/ch1/voices/ch1_broken_1.flac"
                                                            broken "So much for getting out of here...\n"
                                                        jump chapter_2_stranger_rejoin
                                                    voice "audio/voices/ch1/woods/hero/script_h_2.flac"
                                                    hero "We can't just go through with this and listen to Him. She's a Princess. We're supposed to save princesses, not slay them.\n"
                                                    #hero "We can't just go through with this and listen to Him. She's a Princess. We're supposed to save princesses, not slay them. Maybe we can figure out a better solution once we're inside.\n"
                                                    #voice "audio/voices/ch1/woods/narrator/script_n_51.flac"
                                                    #n "Ignore that little voice. He doesn't know what he's talking about.\n"
                                                    jump cabin_arrival_1_menu


                                                "{i}• Oh, yeah? Well I guess I start walking in a different direction. Again. In fact, I'm going to just keep trekking through the wilderness until I find a way out of this place.{/i}":
                                                    if current_princess == "base":
                                                        $ current_princess = "stranger"
                                                    $ config.menu_include_disabled = True
                                                    stop music fadeout 1.0
                                                    voice "audio/voices/ch1/woods/narrator/script_n_52.flac"
                                                    n "There's always a choice, but let me tell you right now that you're making the {i}wrong{/i} one for pretty much everyone who's ever lived, as well as for everyone who ever will.\n"
                                                    $ quick_menu = False
                                                    play music "audio/_music/ch1/Reality Unwound.flac" loop
                                                    play audio "audio/one_shot/footsteps_hike_short.flac"
                                                    voice "audio/voices/ch1/woods/narrator/script_n_53.flac"
                                                    hide skyline onlayer farback
                                                    hide bg onlayer farback
                                                    hide bg onlayer back
                                                    hide midground onlayer front
                                                    hide foreground onlayer inyourface
                                                    with fade
                                                    show midground cabin fractal1 onlayer front at flip, Position(ypos=1125)
                                                    show bg cabin fractal1 onlayer back at flip, Position(ypos=1125)
                                                    show foreground cabin fractal1 onlayer inyourface at flip, Position(ypos=1125)
                                                    with dissolve
                                                    if persistent.quick_menu:
                                                        $ quick_menu = True
                                                    n "And here we go. As you trudge into the woods, something strange starts to happen.\n"
                                                    voice "audio/voices/ch1/woods/narrator/script_n_54.flac"
                                                    n "At first, it's little flickers out of the corner of your eyes, glimpses of familiar wooden structures through the leaves.\n"
                                                    voice "audio/voices/ch1/woods/narrator/script_n_55.flac"
                                                    play audio "audio/one_shot/glass_1.flac"
                                                    hide midground onlayer front
                                                    hide bg onlayer back
                                                    hide foreground onlayer inyourface
                                                    show midground cabin fractal2 onlayer front at Position(ypos=1125)
                                                    show bg cabin fractal2 onlayer back at Position(ypos=1125)
                                                    show foreground cabin fractal2 onlayer inyourface at Position(ypos=1125)
                                                    with hpunch
                                                    n "But as you focus on your surroundings, you start to realize that those flickers weren't just a trick of light.\n"
                                                    voice "audio/voices/ch1/woods/narrator/script_n_56.flac"
                                                    play audio "audio/one_shot/glass_1.flac"
                                                    hide midground onlayer front
                                                    hide bg onlayer back
                                                    hide foreground onlayer inyourface
                                                    show midground cabin fractal3 onlayer front at Position(ypos=1125)
                                                    show bg cabin fractal2 onlayer back at Position(ypos=1125)
                                                    show foreground cabin fractal3 onlayer inyourface at Position(ypos=1125)
                                                    with hpunch
                                                    n "In every direction there is a path and a cabin. And not just {i}a{/i} cabin. {i}The{/i} cabin. An infinite fractal of paths and cabins desperately trying to draw you back to where you need to be.\n"
                                                    voice "audio/voices/ch1/woods/hero/script_h_3.flac"
                                                    hero "Wait... what's going on?\n"
                                                    voice "audio/voices/ch1/woods/narrator/script_n_57.flac"
                                                    n "But you're too stubborn for that, aren't you? It doesn't matter how many paths or cabins appear around you. You're just going to do whatever you can to shirk your responsibility, because you care more about irritating me than you do about the fate of the world.\n"
                                                    voice "audio/voices/ch1/woods/narrator/script_n_58.flac"
                                                    n "You've doomed us all. You know that, right? But of course you do, otherwise you wouldn't just wander off into the forest in search of certain death.\n"
                                                    play audio "audio/one_shot/glass_1.flac"
                                                    $ persistent.death_count += 1
                                                    voice "audio/voices/ch1/woods/narrator/script_n_59.flac"
                                                    $ quick_menu = False
                                                    stop music fadeout 1.0
                                                    stop sound fadeout 1.0
                                                    hide midground onlayer front
                                                    hide bg onlayer back
                                                    hide foreground onlayer inyourface
                                                    show bg black onlayer back at Position(ypos=1125)
                                                    with dissolve
                                                    n "You lose track of just how long you spend aimlessly tromping through the wilderness, but it's not like any of that time spent lost in the woods really matters, because it isn't long before the world ends and everyone dies.\n"
                                                    $ current_princess = "stranger"
                                                    hide bg black onlayer back with dissolve
                                                    if current_princess == "stranger":
                                                        jump start_2

label cabin_arrival_1:
    $gallery_zch1.unlock_item(2)
    $renpy.save_persistent()
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_hike_short.flac"
    hide bg path onlayer farback
    hide midground path onlayer back
    hide front path onlayer front
    show bg black
    with fade
    scene skyline cabin onlayer farback at Position(ypos = 1080)
    show bg cabin onlayer back at Position(ypos = 1200)
    show midground cabin onlayer front at Position(ypos = 1140)
    show foreground cabin onlayer inyourface at Position(ypos = 1120)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/woods/narrator/script_n_60.flac"
    n "You make your way up the short path to the cabin. You'll find the Princess within.\n"
    if forest_1_web_of_lies == False:
        voice "audio/voices/ch1/woods/narrator/script_n_61.flac"
        n "A warning, before you go any further...\n"
        voice "audio/voices/ch1/woods/narrator/script_n_62.flac"
        n "She will lie, she will cheat, and she will do everything in her power to stop you from slaying her. Don't believe a word she says.\n"
        #bvoice "audio/voices/ch1/woods/narrator/script_n_63.flac"
        #n "Fortunately, she's only a Princess, while you are a valiant and talented warrior. It'll be {i}easy{/i} so long as you stay focused.\n"
    if forest_1_flee_hero_spoke == False:
        voice "audio/voices/ch1/woods/hero/script_h_4.flac"
        hero "We're not going to go through with this, right? She's a princess. We're supposed to save princesses, not slay them.\n"
        voice "audio/voices/ch1/woods/narrator/script_n_64.flac"
        n "Ignore him. He doesn't know what he's talking about.\n"
    label cabin_arrival_1_menu:
        menu:
            extend ""

            "{i}• [[Proceed into the cabin.]{/i}":
                play audio "audio/one_shot/enter_cabin_audio.flac"
                image cutscene cabin = Movie(play="images/_animations/cutscenes/Enter Cabin_1.webm",loop=False)
                $ quick_menu = False
                hide loading_icon
                hide skyline onlayer farback
                hide bg onlayer back
                hide midground onlayer front
                hide foreground onlayer inyourface
                show cutscene cabin
                with dissolve
                $ renpy.pause(4.0)
                stop sound fadeout 1.0
                hide cutscene
                scene bg black
                #show loading_icon
                with fade
                jump cabin_interrior_1

label cabin_interrior_1:

    $gallery_zch1.unlock_item(3)
    $renpy.save_persistent()
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    scene farback interior cabin onlayer farback at Position(ypos=1125)
    show bg cabin int onlayer back at Position(ypos=1125)
    show knife interior cabin onlayer back at Position(ypos=1125)
    show door cabin1 onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/woods/narrator/script_n_65.flac"
    n "The interior of the cabin is almost entirely bare. The air is stale and musty and the floor and walls are painted in a fine layer of dust. The only furniture of note is a plain wooden table. Perched on that table is a pristine blade.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_66.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    if beast_encountered and damsel_encountered and witch_encountered:
        $ ch1_can_empty = False
        $ config.menu_include_disabled = True
    if adversary_encountered and prisoner_encountered and tower_encountered and spectre_encountered and razor_encountered and nightmare_encountered:
        $ ch1_can_knife = False
        $ config.menu_include_disabled = True
    label cabin_interrior_1_menu:
        if blade_held:
            $ config.menu_include_disabled = False
        default ch1_can_knife = True

        default blade_taken_1 = False
        default blade_held = False
        menu:
            extend ""

            "{i}• (Explore) [[Take the blade.]{/i}" if blade_held == False and ch1_can_knife:
                $ blade_taken_1 = True
                $ blade_held = True
                $ default_mouse = "blade"
                stop music fadeout 1.0
                play audio "audio/one_shot/knife_pickup.flac"
                voice "audio/voices/ch1/woods/narrator/script_n_67.flac"
                hide knife interior cabin onlayer back
                with dissolve
                n "You take the blade from the table. It'd be rather difficult to slay the Princess and save the world without it.\n"
                play music "audio/_music/ch1/The World-Ender.flac"
                queue music "audio/_music/ch1/The World-Ender Loop.flac" loop
                jump cabin_interrior_1_menu

            "{i}• [[Enter the basement.]{/i}" if (ch1_can_empty and blade_held == False) or blade_held:
                #if blade_held:
                $ config.menu_include_disabled = False
                $ quick_menu = False
                play audio "audio/one_shot/door_bedroom.flac"
                show door cabin2 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                show door cabin3 onlayer back at Position(ypos=1125) with Dissolve(0.5)
                hide farback onlayer farback
                hide bg onlayer back
                hide door onlayer back
                hide table onlayer back
                hide knife onlayer back
                hide mirror onlayer back
                with fade

$ renpy.free_memory()

default basement_1_name_ask = False
default basement_1_eating_ask = False
default basement_1_name_ask_follow_up = False
default basement_1_threatening_tension = False
default basement_1_why_imprisoned = False
default basement_1_shared_task = False

$ renpy.start_predict("princess *")
play sound "audio/looping/ambient_basement_interior.ogg" loop
if blade_held:
    jump basement_1_knife_start
else:
    jump basement_1_empty_start

return
