label quiet_staging:
    define mound = Character("???", color = "#ffffff00", what_color = "#fadbe4", what_outlines=[ (2, "#622929") ], what_style = "mound_style", ctc="ctc_blink_princess_default", ctc_position="nestled")
    define moundmid = Character("???", color = "#ffffff00", what_color = "#fadbe4", what_outlines=[ (2, "#622929") ], what_style = "mound_mid_style", ctc="ctc_blink_princess_default", ctc_position="nestled")

    define mounds = Character("???", color = "#ffffff00", what_color = "#e44646", what_outlines=[ (2, "#4f1313") ], what_style = "mound_style", ctc="ctc_blink_princess_spooky", ctc_position="nestled")


    default mound_pretention_explore = False

    default mound_can_attempt_flee = True

    default quiet_slay_current = False
    default quiet_slay_count = 0

    default quiet_attack = False
    default quiet_suicide_attempt = False

    default quiet1_direct = False

    default quiet_threaten_count = 0

    # quiet 1 variables

    default quiet1_what = False
    default quiet1_lights = False
    default quiet1_mirror = False
    default quiet1_fragile = False
    default quiet1_narrator = False
    default quiet1_trapped = False
    default quiet1_worlds_beyond = False
    default quiet1_are_you_princess = False
    default quiet1_know_each_other = False


    default quiet1_kill_explore = False
    default quiet1_forget_explore = False
    default quiet1_pieces_explore = False
    default quiet1_refuse_explore = False
    default quiet1_destroy_explore = False

    default quiet1_mound_attacked = False
    default quiet1_attack_count = False
    default quiet1_suicide = False
    default quiet1_stay_forever_attempt = False
    default persistent.quiet_gimmick = False
    default persistent.quiet_gimmick_stage_2 = False
    default quiet_date_1 = 0
    default quiet_date_2 = 0
    default quiet_date_delta = 0
    default quiet_date_delta_days = 0

return
