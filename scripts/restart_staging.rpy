label restart_start:

    if first_princess_set == False and oblivion_flag == False:
        $ first_princess_set = True
        if current_princess == "stranger":
            $ first_princess = "stranger"
        elif blade_taken_1:
            $ first_princess = "harsh"
        else:
            $ first_princess = "gentle"

    $ mound_can_attempt_flee = True
    $ config.menu_include_disabled = False
    $ can_spectre = True
    stop sound fadeout 1.0
    stop secondary fadeout 1.0
    stop music fadeout 1.0
    # checks to see if the playing is restarting from the "caught" sideplot; if false, grants achievements

    if oblivion_flag == False:
        if current_princess == "adversary":
            $ achievement.grant("ACH_ADVERSARY")
            $ gallery_adversary.unlock_item(18)
            $ gallery_adversary.unlock_item(19)
            $ renpy.save_persistent()
        elif current_princess == "needle":
            $ achievement.grant("ACH_NEEDLE")
            $ gallery_needle.unlock_item(18)
            $ gallery_needle.unlock_item(19)
            $ renpy.save_persistent()
        elif current_princess == "beast":
            $ achievement.grant("ACH_BEAST")
            $ gallery_beast.unlock_item(15)
            $ gallery_beast.unlock_item(16)
            $ renpy.save_persistent()
        elif current_princess == "den":
            $ achievement.grant("ACH_DEN")
            $ gallery_den.unlock_item(18)
            $ gallery_den.unlock_item(19)
            $ renpy.save_persistent()
        elif current_princess == "damsel":
            $ achievement.grant("ACH_DAMSEL")
            $ gallery_damsel.unlock_item(17)
            $ gallery_damsel.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "dereal":
            $ achievement.grant("ACH_DAMSEL_DEREAL")
            $ gallery_damsel.unlock_item(17)
            $ gallery_damsel.unlock_item(19)
            $ renpy.save_persistent()
        elif current_princess == "nightmare":
            $ achievement.grant("ACH_NIGHTMARE")
            $ gallery_nightmare.unlock_item(17)
            $ gallery_nightmare.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "clarity":
            $ achievement.grant("ACH_CLARITY")
            $ gallery_clarity.unlock_item(12)
            $ gallery_clarity.unlock_item(13)
            $ renpy.save_persistent()
        elif current_princess == "prisonerhead":
            $ gallery_prisoner.unlock_item(15)
            $ gallery_prisoner.unlock_item(16)
            $ renpy.save_persistent()
            $ achievement.grant("ACH_PRISONER_HEAD")
        elif current_princess == "prisonerchain":
            $ gallery_prisoner.unlock_item(13)
            $ gallery_prisoner.unlock_item(14)
            $ renpy.save_persistent()
            $ achievement.grant("ACH_PRISONER_FULL")
        elif current_princess == "razorheart":
            $ achievement.grant("ACH_RAZORHEART")
            $ gallery_razor.unlock_item(18)
            $ gallery_razor.unlock_item(19)
            $ renpy.save_persistent()
        elif current_princess == "razor":
            $ gallery_razor.unlock_item(16)
            $ gallery_razor.unlock_item(17)
            $ renpy.save_persistent()
            $ achievement.grant("ACH_RAZOR")
        elif current_princess == "spectre":
            $ achievement.grant("ACH_SPECTRE")
            $ gallery_spectre.unlock_item(16)
            $ gallery_spectre.unlock_item(17)
            $ renpy.save_persistent()
        elif current_princess == "stranger":
            $ achievement.grant("ACH_STRANGER")
            $ gallery_stranger.unlock_item(10)
            $ gallery_stranger.unlock_item(11)
            $ renpy.save_persistent()
        elif current_princess == "tower":
            $ achievement.grant("ACH_TOWER")
            $ gallery_tower.unlock_item(11)
            $ gallery_tower.unlock_item(12)
            $ renpy.save_persistent()
        elif current_princess == "apotheosis":
            $ achievement.grant("ACH_APOTHEOSIS")
            $ gallery_apotheosis.unlock_item(18)
            $ gallery_apotheosis.unlock_item(19)
            $ renpy.save_persistent()
        elif current_princess == "witch":
            $ achievement.grant("ACH_WITCH")
            $ gallery_witch.unlock_item(17)
            $ gallery_witch.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "thorn":
            $ achievement.grant("ACH_THORN")
            $ gallery_thorn.unlock_item(17)
            $ gallery_thorn.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "fury":
            $ achievement.grant("ACH_FURY")
            $ gallery_fury.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "greydamsel":
            $ achievement.grant("ACH_GREY_DAMSEL")
            $ gallery_grey.unlock_item(15)
            $ gallery_grey.unlock_item(16)
            $ renpy.save_persistent()
        elif current_princess == "greyprisoner":
            $ achievement.grant("ACH_GREY_PRISONER")
            $ gallery_grey.unlock_item(17)
            $ gallery_grey.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "wildnerves":
            $ achievement.grant("ACH_WILD_NERVES")
            $ gallery_wild.unlock_item(7)
            $ gallery_wild.unlock_item(8)
            $ renpy.save_persistent()
        elif current_princess == "wildwound":
            $ achievement.grant("ACH_WILD_WOUND")
            $ gallery_wild.unlock_item(9)
            $ gallery_wild.unlock_item(10)
            $ renpy.save_persistent()
        elif current_princess == "wraith":
            $ achievement.grant("ACH_WRAITH")
            $ gallery_wraith.unlock_item(9)
            $ gallery_wraith.unlock_item(10)
            $ renpy.save_persistent()
        elif current_princess == "happy":
            $ achievement.grant("ACH_HAPPY")
            $ gallery_happy.unlock_item(17)
            $ gallery_happy.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "happydry":
            $ achievement.grant("ACH_HAPPY")
            $ gallery_happy.unlock_item(17)
            $ gallery_happy.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "dragon" or current_princess == "dragonhand":
            $ achievement.grant("ACH_DRAGON")
            $ gallery_dragon.unlock_item(17)
            $ gallery_dragon.unlock_item(18)
            $ renpy.save_persistent()
        elif current_princess == "dragonfused":
            $ achievement.grant("ACH_DRAGON_FUSE_HEART")
            $ gallery_dragon.unlock_item(17)
            $ gallery_dragon.unlock_item(19)
            $ renpy.save_persistent()
        elif current_princess == "cage":
            $ achievement.grant("ACH_CAGE")
            $ gallery_cage.unlock_item(18)
            $ gallery_cage.unlock_item(19)
            $ renpy.save_persistent()
        elif current_princess == "furyheart":
            $ achievement.grant("ACH_FURY_HEART")
            $ gallery_fury.unlock_item(19)
            $ renpy.save_persistent()

    # increment meta loop; keep track of "first chapter 1" princess met; avoids doing some if coming to restart via oblivon loop
    if oblivion_flag == False:
        # resetting "voices" and adding voices met to the pool of voices met

        if trait_stubborn:
            $ stubborn_met = True
            $ trait_stubborn = False

        if trait_hunted:
            $ hunted_met = True
            $ trait_hunted = False

        if trait_smitten:
            $ smitten_met = True
            $ trait_smitten = False

        if trait_paranoid:
            $ paranoid_met = True
            $ trait_paranoid = False

        if trait_skeptic:
            $ skeptic_met = True
            $ trait_skeptic = False

        if trait_cheated:
            $ cheated_met = True
            $ trait_cheated = False

        if trait_cold:
            $ cold_met = True
            $ trait_cold = False

        if trait_contrarian:
            $ contrarian_met = True
            $ trait_contrarian = False

        if trait_broken:
            $ broken_met = True
            $ trait_broken = False

        if trait_opportunist:
            $ opportunist_met = True
            $ trait_opportunist = False
        $ loops_finished += 1
        # feeding into mound - tests to see if player has "destroyed" the most recent loop
        if loops_finished == 1:
            if current_princess == "adversary":
                $ first_mound = "adversary"
            elif current_princess == "needle":
                $ first_mound = "needle"
            elif current_princess == "beast":
                $ first_mound = "beast"
            elif current_princess == "den":
                $ first_mound = "den"
            elif current_princess == "damsel":
                $ first_mound = "damsel"
            elif current_princess == "dereal":
                $ first_mound = "dereal"
            elif current_princess == "nightmare":
                $ first_mound = "nightmare"
            elif current_princess == "clarity":
                $ first_mound = "clarity"
            elif current_princess == "prisonerhead":
                $ first_mound = "prisonerhead"
            elif current_princess == "prisonerchain":
                $ first_mound = "prisonerchain"
            elif current_princess == "razorheart":
                $ first_mound = "razorheart"
            elif current_princess == "razor":
                $ first_mound = "razor"
            elif current_princess == "spectre":
                $ first_mound = "spectre"
            elif current_princess == "stranger":
                $ first_mound = "stranger"
            elif current_princess == "tower":
                $ first_mound = "tower"
            elif current_princess == "apotheosis":
                $ first_mound = "apotheosis"
            elif current_princess == "witch":
                $ first_mound = "witch"
            elif current_princess == "thorn":
                $ first_mound = "thorn"
            elif current_princess == "fury":
                $ first_mound = "fury"
            elif current_princess == "greydamsel":
                $ first_mound = "greydamsel"
            elif current_princess == "greyprisoner":
                $ first_mound = "greyprisoner"
            elif current_princess == "wildnerves":
                $ first_mound = "wildnerves"
            elif current_princess == "wildwound":
                $ first_mound = "wildwound"
            elif current_princess == "wraith":
                $ first_mound = "wraith"
            elif current_princess == "happy":
                $ first_mound = "happy"
            elif current_princess == "happydry":
                $ first_mound = "happydry"
            elif current_princess == "furyheart":
                $ first_mound = "furyheart"
            elif current_princess == "dragon":
                $ first_mound = "dragon"
            elif current_princess == "dragonfused":
                $ first_mound = "dragonfused"
            elif current_princess == "dragonhand":
                $ first_mound = "dragonhand"
            elif current_princess == "cage":
                $ first_mound = "cage"
        elif loops_finished == 2:
            if current_princess == "adversary":
                $ second_mound = "adversary"
            elif current_princess == "needle":
                $ second_mound = "needle"
            elif current_princess == "beast":
                $ second_mound = "beast"
            elif current_princess == "den":
                $ second_mound = "den"
            elif current_princess == "damsel":
                $ second_mound = "damsel"
            elif current_princess == "dereal":
                $ second_mound = "dereal"
            elif current_princess == "nightmare":
                $ second_mound = "nightmare"
            elif current_princess == "clarity":
                $ second_mound = "clarity"
            elif current_princess == "prisonerhead":
                $ second_mound = "prisonerhead"
            elif current_princess == "prisonerchain":
                $ second_mound = "prisonerchain"
            elif current_princess == "razorheart":
                $ second_mound = "razorheart"
            elif current_princess == "razor":
                $ second_mound = "razor"
            elif current_princess == "spectre":
                $ second_mound = "spectre"
            elif current_princess == "stranger":
                $ second_mound = "stranger"
            elif current_princess == "tower":
                $ second_mound = "tower"
            elif current_princess == "apotheosis":
                $ second_mound = "apotheosis"
            elif current_princess == "witch":
                $ second_mound = "witch"
            elif current_princess == "thorn":
                $ second_mound = "thorn"
            elif current_princess == "fury":
                $ second_mound = "fury"
            elif current_princess == "greydamsel":
                $ second_mound = "greydamsel"
            elif current_princess == "greyprisoner":
                $ second_mound = "greyprisoner"
            elif current_princess == "wildnerves":
                $ second_mound = "wildnerves"
            elif current_princess == "wildwound":
                $ second_mound = "wildwound"
            elif current_princess == "wraith":
                $ second_mound = "wraith"
            elif current_princess == "happy":
                $ second_mound = "happy"
            elif current_princess == "happydry":
                $ second_mound = "happydry"
            elif current_princess == "furyheart":
                $ second_mound = "furyheart"
            elif current_princess == "dragon":
                $ second_mound = "dragon"
            elif current_princess == "dragonfused":
                $ second_mound = "dragonfused"
            elif current_princess == "dragonhand":
                $ second_mound = "dragonhand"
            elif current_princess == "cage":
                $ second_mound = "cage"
        elif loops_finished == 3:
            if current_princess == "adversary":
                $ third_mound = "adversary"
            elif current_princess == "needle":
                $ third_mound = "needle"
            elif current_princess == "beast":
                $ third_mound = "beast"
            elif current_princess == "den":
                $ third_mound = "den"
            elif current_princess == "damsel":
                $ third_mound = "damsel"
            elif current_princess == "dereal":
                $ third_mound = "dereal"
            elif current_princess == "nightmare":
                $ third_mound = "nightmare"
            elif current_princess == "clarity":
                $ third_mound = "clarity"
            elif current_princess == "prisonerhead":
                $ third_mound = "prisonerhead"
            elif current_princess == "prisonerchain":
                $ third_mound = "prisonerchain"
            elif current_princess == "razorheart":
                $ third_mound = "razorheart"
            elif current_princess == "razor":
                $ third_mound = "razor"
            elif current_princess == "spectre":
                $ third_mound = "spectre"
            elif current_princess == "stranger":
                $ third_mound = "stranger"
            elif current_princess == "tower":
                $ third_mound = "tower"
            elif current_princess == "apotheosis":
                $ third_mound = "apotheosis"
            elif current_princess == "witch":
                $ third_mound = "witch"
            elif current_princess == "thorn":
                $ third_mound = "thorn"
            elif current_princess == "fury":
                $ third_mound = "fury"
            elif current_princess == "greydamsel":
                $ third_mound = "greydamsel"
            elif current_princess == "greyprisoner":
                $ third_mound = "greyprisoner"
            elif current_princess == "wildnerves":
                $ third_mound = "wildnerves"
            elif current_princess == "wildwound":
                $ third_mound = "wildwound"
            elif current_princess == "wraith":
                $ third_mound = "wraith"
            elif current_princess == "happy":
                $ third_mound = "happy"
            elif current_princess == "happydry":
                $ third_mound = "happydry"
            elif current_princess == "furyheart":
                $ third_mound = "furyheart"
            elif current_princess == "dragon":
                $ third_mound = "dragon"
            elif current_princess == "dragonfused":
                $ third_mound = "dragonfused"
            elif current_princess == "dragonhand":
                $ third_mound = "dragonhand"
            elif current_princess == "cage":
                $ third_mound = "cage"
        elif loops_finished == 4:
            if current_princess == "adversary":
                $ fourth_mound = "adversary"
            elif current_princess == "needle":
                $ fourth_mound = "needle"
            elif current_princess == "beast":
                $ fourth_mound = "beast"
            elif current_princess == "den":
                $ fourth_mound = "den"
            elif current_princess == "damsel":
                $ fourth_mound = "damsel"
            elif current_princess == "dereal":
                $ fourth_mound = "dereal"
            elif current_princess == "nightmare":
                $ fourth_mound = "nightmare"
            elif current_princess == "clarity":
                $ fourth_mound = "clarity"
            elif current_princess == "prisonerhead":
                $ fourth_mound = "prisonerhead"
            elif current_princess == "prisonerchain":
                $ fourth_mound = "prisonerchain"
            elif current_princess == "razorheart":
                $ fourth_mound = "razorheart"
            elif current_princess == "razor":
                $ fourth_mound = "razor"
            elif current_princess == "spectre":
                $ fourth_mound = "spectre"
            elif current_princess == "stranger":
                $ fourth_mound = "stranger"
            elif current_princess == "tower":
                $ fourth_mound = "tower"
            elif current_princess == "apotheosis":
                $ fourth_mound = "apotheosis"
            elif current_princess == "witch":
                $ fourth_mound = "witch"
            elif current_princess == "thorn":
                $ fourth_mound = "thorn"
            elif current_princess == "fury":
                $ fourth_mound = "fury"
            elif current_princess == "greydamsel":
                $ fourth_mound = "greydamsel"
            elif current_princess == "greyprisoner":
                $ fourth_mound = "greyprisoner"
            elif current_princess == "wildnerves":
                $ fourth_mound = "wildnerves"
            elif current_princess == "wildwound":
                $ fourth_mound = "wildwound"
            elif current_princess == "wraith":
                $ fourth_mound = "wraith"
            elif current_princess == "happy":
                $ fourth_mound = "happy"
            elif current_princess == "happydry":
                $ fourth_mound = "happydry"
            elif current_princess == "furyheart":
                $ fourth_mound = "furyheart"
            elif current_princess == "dragon":
                $ fourth_mound = "dragon"
            elif current_princess == "dragonfused":
                $ fourth_mound = "dragonfused"
            elif current_princess == "dragonhand":
                $ fourth_mound = "dragonhand"
            elif current_princess == "cage":
                $ fourth_mound = "cage"
        elif loops_finished == 5:
            if current_princess == "adversary":
                $ fifth_mound = "adversary"
            elif current_princess == "needle":
                $ fifth_mound = "needle"
            elif current_princess == "beast":
                $ fifth_mound = "beast"
            elif current_princess == "den":
                $ fifth_mound = "den"
            elif current_princess == "damsel":
                $ fifth_mound = "damsel"
            elif current_princess == "dereal":
                $ fifth_mound = "dereal"
            elif current_princess == "nightmare":
                $ fifth_mound = "nightmare"
            elif current_princess == "clarity":
                $ fifth_mound = "clarity"
            elif current_princess == "prisonerhead":
                $ fifth_mound = "prisonerhead"
            elif current_princess == "prisonerchain":
                $ fifth_mound = "prisonerchain"
            elif current_princess == "razorheart":
                $ fifth_mound = "razorheart"
            elif current_princess == "razor":
                $ fifth_mound = "razor"
            elif current_princess == "spectre":
                $ fifth_mound = "spectre"
            elif current_princess == "stranger":
                $ fifth_mound = "stranger"
            elif current_princess == "tower":
                $ fifth_mound = "tower"
            elif current_princess == "apotheosis":
                $ fifth_mound = "apotheosis"
            elif current_princess == "witch":
                $ fifth_mound = "witch"
            elif current_princess == "thorn":
                $ fifth_mound = "thorn"
            elif current_princess == "fury":
                $ fifth_mound = "fury"
            elif current_princess == "greydamsel":
                $ fifth_mound = "greydamsel"
            elif current_princess == "greyprisoner":
                $ fifth_mound = "greyprisoner"
            elif current_princess == "wildnerves":
                $ fifth_mound = "wildnerves"
            elif current_princess == "wildwound":
                $ fifth_mound = "wildwound"
            elif current_princess == "wraith":
                $ fifth_mound = "wraith"
            elif current_princess == "happy":
                $ fifth_mound = "happy"
            elif current_princess == "happydry":
                $ fifth_mound = "happydry"
            elif current_princess == "furyheart":
                $ fifth_mound = "furyheart"
            elif current_princess == "dragon":
                $ fifth_mound = "dragon"
            elif current_princess == "dragonfused":
                $ fifth_mound = "dragonfused"
            elif current_princess == "dragonhand":
                $ fifth_mound = "dragonhand"
            elif current_princess == "cage":
                $ fifth_mound = "cage"
    else:
        $ caught_origin_current = ""
        $ oblivion_flag = False
        $ loops_destroyed += 1


    # resetting traits in event player progressed oblivion ending

    $ trait_stubborn = False

    $ trait_hunted = False

    $ trait_smitten = False

    $ trait_paranoid = False

    $ trait_skeptic = False

    $ trait_cheated = False

    $ trait_cold = False

    $ trait_contrarian = False

    $ trait_broken = False

    $ trait_opportunist = False

    default first_princess = "stranger"
    default first_princess_set = False

    # resetting broad ch2 + 3 variables

    $ current_run_mirror_comment = False
    $ current_run_mirror_touched = False

    # resetting UI variables

    $ config.menu_include_disabled = False
    $ quick_menu = False
    $ blade_held = False
    $ default_mouse = "default"
    $ blade_taken_1 = False

    # resetting ch1 variables that need to be reset

    $ current_mutual_death = 0

    # ch1 forest explore resets:

    $ forest_1_questioning_start = False
    $ forest_1_questioning_followup = False
    $ forest_1_questioning_evidence = False
    $ forest_1_conscientious_objector_explore = False
    $ forest_1_someone_else_explore = False
    $ forest_1_refuse_explore = False
    $ forest_1_why_dangerous = False
    $ forest_1_what_happens = False
    $ forest_1_casuality_explore = False
    $ forest_1_let_it_burn = False
    $ forest_1_reluctant_visit = False
    $ forest_1_prize = False
    $ forest_1_prize_follow_up = False

    # ch1 shared variable resets:

    $ basement_1_talked = False
    $ basement_1_name_ask = False
    $ basement_1_eating_ask = False
    $ basement_1_name_ask_follow_up = False
    $ basement_1_threatening_tension = False
    $ basement_1_why_imprisoned = False
    $ basement_1_shared_task = False

    # ch1 knife variable resets



    $ ch1_razor_pulse = False
    $ cycle_1_princess_slain_offer_explore = False
    $ cycle_1_princess_slain_offer_rejected = False
    $ cycle_1_princess_slain_offer_heard_menu_explore = False
    $ basement_1_knife_dropped_task_shared = False
    $ basement_1_knife_dropped_relationship_explore = False
    $ basement_1_knife_dropped_awkward = False
    $ basement_1_knife_vague_count = 0
    $ basement_1_philosophy_knife_flag = False
    $ basement_1_knife_how_escape = False
    $ basement_1_knife_how_long = False
    $ basement_1_knife_why_here_explore = False
    $ nightmare_no_wounds = False
    $ basement_1_knife_rescue_door_try_explore = False
    $ basement_1_knife_rescue_door_force_explore = False
    $ basement_1_knife_rescue_door_shout_explore = False
    $ basement_1_knife_kill_joke = False
    $ basement_1_knife_confronted_steel = False
    $ knife_queue_undecided = False
    $ basement_1_nerves_steeled = False
    $ basement_1_nerves_steeled_hesitated = False
    $ basement_1_nerves_armed = False
    $ basement_1_nerves_fear = False
    $ basement_1_nerves_steeled_hesitated_explore = False
    $ basement_1_not_dropping_stare = False
    $ razor_pathetic = False

    $ ch1_mound_fresh = False

    # ch1 empty variable resets

    $ basement_1_empty_kill_joke = False
    $ basement_1_empty_save_explore = False
    $ basement_1_empty_save_lie_explore = False
    $ basement_1_empty_arm_loss_known = False
    $ basement_1_empty_wounded = False
    $ what_would_you_do_1 = False
    $ basement_1_empty_not_worth_risk = False
    $ basement_1_empty_rescue_dont_regret = False
    $ basement_1_empty_rescue_door_try_explore = False
    $ basement_1_empty_rescue_door_force_explore = False
    $ basement_1_empty_rescue_door_shout_explore = False
    $ beast_1_both_arms = False
    $ basement_1_empty_retrieve_knife_stairs_explore_hello = False
    $ basement_1_empty_knife_hesitate = False
    $ loop_1_locked = False
    $ forest_1_flee_hero_spoke = False
    # can_knife is unnecessary because too many ch2's are reliant on knife
    #default ch1_can_knife = True

    #if adversary_encountered and prisoner_encountered and spectre_encountered and razor_encountered and tower_encountered:
    #    $ ch1_can_knife = False

    default ch1_can_empty = True

    if damsel_encountered and beast_encountered and witch_encountered:
        $ ch1_can_empty = False

    # reset mirror variables
    $ mirror_n_explore = False
    $ mirror_n_silence_flag = False

    # quiet variables reset

    # resetting loop_1_killed variable

    $ loop_1_princess_killed = False

    $ quiet_slay_current = False

    # resetting current_princess
    $ current_princess = ""
    # reset current loop
    $ current_loop = 1
    jump start

return
