label credits:



    default song_ypos = 200
    $ quick_menu = False

    scene bg black
    $ renpy.show_screen("credits_1", _layer="master")
    with fade
    $ renpy.pause(4.0)
    $ renpy.hide_screen("credits_1")
    scene credits btg
    $ renpy.show_screen("credits_2", _layer="master")
    with fade
    $ renpy.pause(10.0)
    $ renpy.hide_screen("credits_2")
    scene credits serenity
    $ renpy.show_screen("credits_3", _layer="master")
    with fade
    $ renpy.pause(5.0)
    $ renpy.hide_screen("credits_3")
    scene credits serenity
    $ renpy.show_screen("credits_3a", _layer="master")
    with Dissolve(1.0)
    $ renpy.pause(5.0)
    scene credits serenity
    $ renpy.show_screen("credits_3b", _layer="master")
    with Dissolve(1.0)
    $ renpy.pause(5.0)
    scene credits altagram
    $ renpy.show_screen("credits_4", _layer="master")
    with fade
    $ renpy.pause(5.0)
    scene credits altagram
    $ renpy.show_screen("credits_4a", _layer="master")
    with Dissolve(1.0)
    $ renpy.pause(5.0)
    scene credits altagram
    $ renpy.show_screen("credits_4b", _layer="master")
    with Dissolve(1.0)
    $ renpy.pause(5.0)
    scene credits viridian
    $ renpy.show_screen("credits_4c", _layer="master")
    with fade
    $ renpy.pause(5.0)
    scene bg black
    $ renpy.show_screen("credits_5", _layer="master")
    with fade
    $ renpy.pause(5.0)
    scene bg black
    $ renpy.show_screen("credits_6", _layer="master")
    with fade
    $ renpy.pause(5.0)
    scene credits laundrybear
    $ renpy.show_screen("credits_7", _layer="master")
    with fade
    $ renpy.pause(5.0)
    scene bg black
    $ renpy.show_screen("credits_8", _layer="master")
    with fade
    $ renpy.pause(5.0)
    scene credits patreon2
    $ renpy.show_screen("credits_9", _layer="master")
    with fade
    $ renpy.pause(7.5)
    scene credits special2
    $ renpy.show_screen("credits_10", _layer="master")
    with fade
    $ renpy.pause(7.5)
    if final_ending != "good":
        $ achievement.grant("ACH_CREDITS")
        scene bg black
        show text _("{=amatic}{color=#FFFFFF}{size=70}Our Song{/size}{/color}{/=amatic}") at Position(ypos=75)
        #scene credits our song
        $ renpy.show_screen("song", _layer="master")
        with fade
    else:
        #scene credits your song
        scene bg black
        show text _("{=amatic}{color=#FFFFFF}{size=70}Your Song{/size}{/color}{/=amatic}") at Position(ypos=75)
        $ renpy.show_screen("song", _layer="master")
        with fade

    if renpy.variant("pc"):
        truthsmall "Thank you so much for playing. As an expression of our gratitude, here's the track order for a special playlist just for you. If you'd like to take a screenshot, you can hide the UI by hitting 'h.'\n"
    else:
        truthsmall "Thank you so much for playing. As an expression of our gratitude, here's the track order for a special playlist just for you.\n"
    if persistent.gallery_unlocked == False and final_ending != "good" and final_ending != "oblivion":
        $ persistent.gallery_unlocked = True
        truthsmall "And now that you've finished the full story for the first time, you've also unlocked the gallery! You can access it from the main and in-game menus under the 'memories' tab, and it's full of clues that will help you find undiscovered vessels and interactions. Happy hunting!\n"
    if renpy.variant("pc"):
        label credits_loop:
            menu:
                extend ""

                "{i}• (Explore) Join the Discord.{/i}" if renpy.variant("pc"):
                    $ renpy.run(OpenURL('https://discord.gg/blacktabbygames'))
                    jump credits_loop

                "{i}• (Explore) Join our Mailing List.{/i}" if renpy.variant("pc"):
                    $ renpy.run(OpenURL('https://mailchi.mp/70710220f538/blacktabbynewletter'))
                    jump credits_loop

                #"{i}• (Explore) Support us on Patreon.{/i}":
                #    $ renpy.run(OpenURL('https://www.patreon.com/abbyhoward'))
                #    jump credits_loop

                "{i}• (Explore) Join the Subreddit.{/i}" if renpy.variant("pc"):
                    $ renpy.run(OpenURL('https://www.reddit.com/r/slaytheprincess'))
                    jump credits_loop

                "{i}• (Explore) Follow us Somewhere Else.{/i}" if renpy.variant("pc"):
                    $ renpy.run(OpenURL('https://www.blacktabbygames.com/where-to-find-us'))
                    jump credits_loop

                "{i}• (Explore) Make your Playlist.{/i}" if renpy.variant("pc"):
                    $ renpy.run(OpenURL('https://spotify.link/PdG0uXZecEb'))
                    jump credits_loop

                "{i}• (Explore) Play our Other Game.{/i}" if renpy.variant("pc"):
                    # STEAM
                    $ renpy.run(OpenURL('steam://openurl/https://store.steampowered.com/app/1609230/Scarlet_Hollow/?utm_campaign=princess_credits'))

                    # GOG
                    #$ renpy.run(OpenURL('https://www.gog.com/en/game/scarlet_hollow'))
                    jump credits_loop

                "{i}• Return to Main Menu.{/i}":
                    return

    else:
        return


return
