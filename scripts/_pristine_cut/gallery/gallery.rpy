
style tooltip_style is text:
    xalign 0.5
    yalign 0.95
    size 35

init python:
    gallery = Gallery()
    #persistent._clear()

    routesMaxX = 10
    routesMaxY = 1

    routesLowerMaxX = 12
    routesLowerMaxY = 1

    gridMaxX = 5
    gridMaxY = 4

screen gallery():
    tag menu
    key "K_ESCAPE" action[Return(), PauseAudio("music", False), PauseAudio("music2", False), PauseAudio("music3", False), PauseAudio("music4", False), PauseAudio("music5", False), PauseAudio("sound", False), PauseAudio("secondary", False), PauseAudio("tertiary", False), Stop("musicgallery")]


    key "K_BACKSPACE" action[Return(), PauseAudio("music", False), PauseAudio("music2", False),PauseAudio("music3", False),PauseAudio("music4", False),PauseAudio("music5", False),PauseAudio("sound", False),PauseAudio("secondary", False),PauseAudio("tertiary", False), Stop("musicgallery")]

    key "pad_start_press" action[Return(), PauseAudio("music", False), PauseAudio("music2", False),PauseAudio("music3", False),PauseAudio("music4", False),PauseAudio("music5", False),PauseAudio("sound", False),PauseAudio("secondary", False),PauseAudio("tertiary", False), Stop("musicgallery")]
    key "pad_b_press" action[Return(), PauseAudio("music", False), PauseAudio("music2", False),PauseAudio("music3", False),PauseAudio("music4", False),PauseAudio("music5", False),PauseAudio("sound", False),PauseAudio("secondary", False),PauseAudio("tertiary", False), Stop("musicgallery")]

    #key "K_ESCAPE" action[Return(), Play("music", "audio/_music/main_menu.flac")]
    #key "K_BACKSPACE" action[Return(), Play("music", "audio/_music/main_menu.flac")]
    #add "images/_gallery/UI/gallery_BG.png"
    add "farback quiet"
    add "mound hands oblivion early"

    $galleryInitializer.clear_galleries()
    $galleryInitializer.set_galleries()

    $galleryInitializer.clear_hints()
    $galleryInitializer.set_hints()

    vbox:
        xalign 0.5
        yalign 0.10
        spacing 5

        text _("Memories") xalign 0.5 size 90
        text " "

        text _("Beginnings and Endings") xalign 0.5 size 50

        grid 3 1:
            xalign 0.5
            spacing 40
            ypos 50

            for i in range(0, len(altRoutesParent)):

                if altRoutesParent[i].get_flag():
                    imagebutton:
                        auto str(altRoutesParent[i].routeImageSource) +"%s.png"
                        action [ShowMenu("this_gallery", altRoutesParent[i]), Hide("gallery"), Play("musicgallery", str(altRoutesParent[i].routeTrack))]
                        hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
                        tooltip str(altRoutesParent[i].routeName)

                else:
                    imagebutton:
                        idle str(altRoutesParent[i].routeImageSource)+"insensitive.png"
                        hover str(altRoutesParent[i].routeImageSource)+"insensitive_hover.png"
                        hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
                        action NullAction()
                        tooltip str(altRoutesParent[i].routeHint)

        text " "
        text _("Vessels") xalign 0.5 size 50 ypos 30

        # $routesX = routesMaxX
        # $routesY = (len(routesParent)//routesMaxY) +1

        # if (len(routesParent)<routesMaxX):
        #     $routesX = len(routesParent)

        grid 10 1:
            xalign 0.5
            spacing 20
            ypos 60

            for i in range(0, len(routesParent)):

                if routesParent[i].get_flag():
                    imagebutton:
                        auto str(routesParent[i].routeImageSource) +"%s.png"
                        action [Show("this_gallery", dissolve, routesParent[i]), Hide("gallery"), Play("musicgallery", str(routesParent[i].routeTrack))]
                        hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
                        tooltip str(routesParent[i].routeHintUnlocked)

                else:
                    imagebutton:
                        idle str(routesParent[i].routeImageSource)+"insensitive.png"
                        hover str(routesParent[i].routeImageSource)+"insensitive_hover.png"
                        hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
                        action NullAction()
                        tooltip str(routesParent[i].routeHint)


            #required to fill in empty grid items
            # for i in range(len(routesParent), routesX*routesY):
            #     null

        text " "
        # $routesLowerX = routesLowerMaxX
        # $routesLowerY = (len(routesParentLower)//routesLowerMaxY) +1

        # if (len(routesParentLower)<routesLowerMaxX):
        #     $routesLowerX = len(routesParentLower)

        grid 12 1:
            xalign 0.5
            spacing 20
            ypos 60

            for i in range(0, len(routesParentLower)):

                if routesParentLower[i].get_flag():
                    imagebutton:
                        auto str(routesParentLower[i].routeImageSource) +"%s.png"
                        action [Show("this_gallery", dissolve, routesParentLower[i]), Hide("gallery"), Play("musicgallery", str(routesParentLower[i].routeTrack))]
                        hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
                        tooltip str(routesParentLower[i].routeHintUnlocked)

                else:
                    imagebutton:
                        idle str(routesParentLower[i].routeImageSource)+"insensitive.png"
                        hover str(routesParentLower[i].routeImageSource)+"insensitive_hover.png"
                        hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
                        action NullAction()
                        tooltip str(routesParentLower[i].routeHint)


            #required to fill in empty grid items
            # for i in range(len(routesParentLower), routesLowerX*routesLowerY):
            #     null

    #imagebutton auto "images/_gallery/ui/backbutton_%s.png" action[Return(), Play("music", "audio/_music/main_menu.flac")] ypos 20 xpos 30
    if _preferences.language is not None:
        imagebutton auto "images/_gallery/ui/backbutton_%s.png" action[Return(), PauseAudio("music", False), PauseAudio("music2", False),PauseAudio("music3", False),PauseAudio("music4", False),PauseAudio("music5", False),PauseAudio("sound", False),PauseAudio("secondary", False),PauseAudio("tertiary", False), Stop("musicgallery")] ypos 20 xpos 30
    else:
        imagebutton auto "images/_gallery/ui/backbutton_eng_%s.png" action[Return(), PauseAudio("music", False), PauseAudio("music2", False),PauseAudio("music3", False),PauseAudio("music4", False),PauseAudio("music5", False),PauseAudio("sound", False),PauseAudio("secondary", False),PauseAudio("tertiary", False), Stop("musicgallery")] ypos 20 xpos 30
    $tooltip = GetTooltip()
    if tooltip:
        text "[tooltip!t]":
            xmaximum 1000
            text_align 0.5
            style "tooltip_style"


##########2nd level gallery

screen this_gallery(galleryParent):

    key "K_ESCAPE" action [Show("gallery"), Hide("this_gallery", Dissolve(0.5)), Play("musicgallery", "audio/_music/mound/Oblivion.flac")]
    key "K_BACKSPACE" action [Show("gallery"), Hide("this_gallery", Dissolve(0.5)), Play("musicgallery", "audio/_music/mound/Oblivion.flac")]

    key "pad_start_press" action [Show("gallery"), Hide("this_gallery", Dissolve(0.5)), Play("musicgallery", "audio/_music/mound/Oblivion.flac")]
    key "pad_b_press" action [Show("gallery"), Hide("this_gallery", Dissolve(0.5)), Play("musicgallery", "audio/_music/mound/Oblivion.flac")]

    imagebutton idle "farback quiet"
    text "[galleryParent.routeName!t]" ypos 40 xalign 0.5 size 80

    #$ this_gallery_key = galleryParent.key
    #$galleryParent.clear_images()
    #$galleryParent.add_images()
    #$galleryParent.clear_hints()
    #$galleryHints.set_hints()
    #$galleryHints.clear_all_hints()


    $gridX = gridMaxX
    if (len(galleryParent.items)%gridMaxX) == 0:
        $gridY = (len(galleryParent.items)//gridMaxX)
    else:
        $gridY = (len(galleryParent.items)//gridMaxX) + 1

    if (len(galleryParent.items)<gridMaxX):
        $gridX = len(galleryParent.items)

    grid gridX gridY:
        #ypos 750
        xalign 0.5
        yalign 0.5
        spacing 50

        for i in range(0, len(galleryParent.items)):

            if galleryParent.items[i].get_flag():
                imagebutton:
                    idle galleryParent.items[i].thumb
                    hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
                    hover galleryParent.items[i].hoveredthumb
                    action [Show("gallery_large", dissolve, galleryParent.items[i], galleryParent), Hide("this_gallery")]
                    tooltip str(galleryParent.items[i].hint)
            else:
                imagebutton:
                    #idle galleryParent.items[i].thumbLocked
                    hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
                    idle "gallery_locked_idle"
                    hover "gallery_locked_hover"
                    action NullAction()
                    tooltip str(galleryParent.items[i].hint)


        #required to fill in empty grid items
        for i in range(len(galleryParent.items), gridX*gridY):
            null

    if _preferences.language is not None:
        imagebutton auto "images/_gallery/ui/backbutton_%s.png" action[Show("gallery"), Hide("this_gallery", Dissolve(0.5)), Play("musicgallery", "audio/_music/mound/Oblivion.flac")] ypos 20 xpos 30
    else:
        imagebutton auto "images/_gallery/ui/backbutton_eng_%s.png" action[Show("gallery"), Hide("this_gallery", Dissolve(0.5)), Play("musicgallery", "audio/_music/mound/Oblivion.flac")] ypos 20 xpos 30
    $tooltip = GetTooltip()
    if tooltip:
        text "[tooltip!t]":
            style "tooltip_style"

############Fullscreen gallery

screen gallery_large(thisGalleryItem, thisGalleryParent):

    key "K_ESCAPE" action[Show("this_gallery", dissolve, thisGalleryParent), Hide("gallery_large", dissolve)]
    key "K_BACKSPACE" action[Show("this_gallery", dissolve, thisGalleryParent), Hide("gallery_large", dissolve)]
    key "pad_start_press" action[Show("this_gallery", dissolve, thisGalleryParent), Hide("gallery_large", dissolve)]
    key "pad_b_press" action[Show("this_gallery", dissolve, thisGalleryParent), Hide("gallery_large", dissolve)]


    if (thisGalleryItem.get_flag()):
        add thisGalleryItem.image
    else:
        add "farback quiet"
        add "mound hands oblivion early"
        text thisGalleryItem.hint:
            size 50
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            text_align 0.5

    if (thisGalleryItem.itemNumber > 1):
        key "K_LEFT" action [Show("gallery_large", dissolve, thisGalleryParent.items[(thisGalleryItem.itemNumber-2)], thisGalleryParent), Play("sound", "audio/one_shot/page_turn_short.flac")]
        imagebutton:
            auto "images/_gallery/UI/left_%s.png"
            #hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
            action [Show("gallery_large", dissolve, thisGalleryParent.items[(thisGalleryItem.itemNumber-2)], thisGalleryParent), Play("sound", "audio/one_shot/page_turn_short.flac")]
            xalign 0.0
            yalign 0.5

    if (thisGalleryItem.itemNumber < len(thisGalleryParent.items)):
        key "K_RIGHT" action [Show("gallery_large", dissolve, thisGalleryParent.items[(thisGalleryItem.itemNumber)], thisGalleryParent), Play("sound", "audio/one_shot/page_turn_short.flac")]
        imagebutton:
            #hovered [Play("sound", "audio/one_shot/page_turn_short.flac")]
            auto "images/_gallery/UI/right_%s.png"
            action [Show("gallery_large", dissolve, thisGalleryParent.items[(thisGalleryItem.itemNumber)], thisGalleryParent), Play("sound", "audio/one_shot/page_turn_short.flac")]
            xalign 1.0
            yalign 0.5

    if _preferences.language is not None:
        imagebutton auto "images/_gallery/ui/backbutton_%s.png" action[Show("this_gallery", dissolve, thisGalleryParent), Hide("gallery_large", dissolve)] ypos 20 xpos 30
    else:
        imagebutton auto "images/_gallery/ui/backbutton_eng_%s.png" action[Show("this_gallery", dissolve, thisGalleryParent), Hide("gallery_large", dissolve)] ypos 20 xpos 30
