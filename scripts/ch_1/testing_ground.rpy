label testing_ground:

    menu:

        ""

        "{i}• TEST BUTTON{/i}":
            hide bg onlayer farback
            hide midground onlayer back
            hide front onlayer front
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 1.0
            stop sound
            stop music

            #$ mound_fight_triggered = True
            #$ final_ending = "leave"
            $ loops_finished = 5
            $ stubborn_met = True
            $ hunted_met = True
            $ smitten_met = True
            $ paranoid_met = True
            $ skeptic_met = True
            $ cheated_met = True
            $ opportunist_met = True
            $ cold_met = True
            $ broken_met = True
            $ contrarian_met = True
            $ adversary_2_end = "fight_succeed"
            $ first_mound = "apotheosis"
            $ tower_2_end = "submit"
            $ first_princess = "harsh"
            $ spectre_end = "slay"
            $ second_mound = "prisoner"
            $ third_mound = "den"
            $ beast_2_slay_attempt = True
            $ damsel_end = "dereal"
            $ beast_2_end = "free_succeed"
            $ den_end = "slay"
            $ razor_end = "peace"
            $ fourth_mound = "razor"
            $ prisoner_end = "free"
            $ fifth_mound = "prizoner"
            $ wraith_end = "free"
            show farback quiet onlayer farback at Position(ypos=1125)
            show content m empty onlayer front at Position(ypos=1125)
            show mirror frame onlayer front at Position(ypos=1125)
            show player mirror onlayer front at Position(ypos=1125)
            jump mirror_finale
            #$ loops_destroyed = 2
            #$ loops_finished = 4
            #$ oblivion_when_met = 2

            jump felina_cabin_staging


return
