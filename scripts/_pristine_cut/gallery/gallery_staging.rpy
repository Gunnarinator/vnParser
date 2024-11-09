init -1 python:

    routesParent = []
    routesParentLower = []
    altRoutesParent = []

##################lower galleries
    class GalleryAchievementChecker:
        def __init__(self):
            self.isAchieved = False

        def checkAchievement(self):
            for routeIndex in range(0,len(routesParent)):
                if not routesParent[routeIndex].get_flag():
                    return
                for itemIndex in range (0, len(routesParent[routeIndex].items)):
                    if not routesParent[routeIndex].items[itemIndex].get_flag():
                        return
            for routeIndex in range(0,len(routesParentLower)):
                if not routesParentLower[routeIndex].get_flag():
                    return
                for itemIndex in range (0, len(routesParentLower[routeIndex].items)):
                    if not routesParentLower[routeIndex].items[itemIndex].get_flag():
                        return
            for routeIndex in range(0,len(altRoutesParent)):
                if not altRoutesParent[routeIndex].get_flag():
                    return
                for itemIndex in range (0, len(altRoutesParent[routeIndex].items)):
                    if not altRoutesParent[routeIndex].items[itemIndex].get_flag():
                        return

            achievement.grant("ACH_GALLERY_FIXED")

        def printAchievementStatus(self):
            result = "row 1\n"
            for routeIndex in range(0,len(routesParent)):
                result += "\n" + routesParent[routeIndex].get_flag_key() + " " + str(routesParent[routeIndex].get_flag() == False) + "\n"
                for itemIndex in range (0, len(routesParent[routeIndex].items)):
                    result += routesParent[routeIndex].items[itemIndex].get_flag_key() + " " + str(routesParent[routeIndex].items[itemIndex].get_flag() == False) + ", "
            result += "\nrow 2\n"
            for routeIndex in range(0,len(routesParentLower)):
                result += "\n" + routesParentLower[routeIndex].get_flag_key() + " " + str(routesParentLower[routeIndex].get_flag() == False) + "\n"
                for itemIndex in range (0, len(routesParentLower[routeIndex].items)):
                    result += " " + routesParentLower[routeIndex].items[itemIndex].get_flag_key() + " " + str(routesParentLower[routeIndex].items[itemIndex].get_flag() == False) + " "
            result += "\nrow 3\n"
            for routeIndex in range(0,len(altRoutesParent)):
                result += "\n" + altRoutesParent[routeIndex].get_flag_key() + " " + str(altRoutesParent[routeIndex].get_flag() == False) + "\n"
                for itemIndex in range (0, len(altRoutesParent[routeIndex].items)):
                    result += altRoutesParent[routeIndex].items[itemIndex].get_flag_key() + " " + str(altRoutesParent[routeIndex].items[itemIndex].get_flag() == False) + " "
            file = open("achievementstatus.txt", "w")
            file.write(result)
            file.close()



    galleryAchievementChecker = GalleryAchievementChecker()

    class GalleryParent:
        def __init__(self, imagesLength, key, routeName, routeHintUnlocked, routeHint):
                self.imagesLength = imagesLength
                self.key = key
                self.flag = str(key)+"_flag"
                self.routeHint = routeHint
                self.routeName = routeName
                self.routeHintUnlocked = routeHintUnlocked
                self.routeImageSource = "images/_gallery/_" + str(key)+ "/" + str(key) +"_"
                self.routeTrack = "audio/_gallery/"+ str(key) + ".flac"
                self.items = []
                self.hints = []

        def get_flag(self):
            return getattr(persistent, self.flag, False)

        def get_flag_key(self):
            return self.flag

        def add_images(self):
            for i in range (1, self.imagesLength+1):
                self.items.append(GalleryItem(self.key, i))

        def clear_images(self):
            self.items = []

        def clear_hints(self):
            self.hints = []

        def unlock_item(self, index, checkAchievement = True ):
            setattr(persistent, "gallery_" + str(self.key) + "_" + str(index), True)
            if checkAchievement == True:
                galleryAchievementChecker.checkAchievement()

        def unlock_gallery(self):
            setattr(persistent, self.flag, True)

        def lock_gallery(self):
            setattr(persistent, self.flag, False)

        def lock_item(self, index):
            setattr(persistent, "gallery_" + str(self.key)+ "_" + str(index), False)

    class GalleryItem:
        def __init__(self, parentKey, itemNumber):
            self.image = "images/_gallery/_" + str(parentKey)+ "/big/"+ str(parentKey)+"_"+str(itemNumber)+".jpg"


            self.thumb = "images/_gallery/_" + str(parentKey)+ "/thumb/"+ str(parentKey)+ "_" + str(itemNumber) + "_thumb_idle.png"
            self.hoveredthumb = "images/_gallery/_" + str(parentKey)+ "/thumb/"+ str(parentKey)+ "_" + str(itemNumber) + "_thumb_hovered.png"
            #self.thumbLocked = "images/_gallery/_" + str(parentKey)+ "/thumb/"+ str(parentKey)+"_thumb"+str(itemNumber)+"_locked.png"
            self.itemNumber = itemNumber
            self.parentKey = parentKey
            self.hint = ""

        def get_flag_key(self):
            return "gallery_" + str(self.parentKey)+"_"+str(self.itemNumber)

        def get_flag(self):
            return getattr(persistent, "gallery_" + str(self.parentKey)+"_"+str(self.itemNumber), False)


##############Route & Gallery setup


#Beginnings & endings
    gallery_zch1 = GalleryParent(18, "zch1", _("The Hero and the Princess"), _("The Hero and the Princess"), _("Start the game."))
    altRoutesParent.append(gallery_zch1)

    gallery_ztlq = GalleryParent(9, "ztlq", _("The Spaces Between"), _("The Spaces Between"), _("Reach the mirror."))
    altRoutesParent.append(gallery_ztlq)

    gallery_zfinale = GalleryParent(20, "zfinale", _("The End of Everything"), _("The End of Everything"), _("Reach the end of everything."))
    altRoutesParent.append(gallery_zfinale)

#1st row
    gallery_adversary = GalleryParent(20, "adversary", _("The Adversary"), _("The Adversary — The song we write in our blood."), _("Meet your equal in combat."))
    routesParent.append(gallery_adversary)

    gallery_tower = GalleryParent(13, "tower", _("The Tower"), _("The Tower — Doubt forces the hand of fealty."), _("Die, pathetically, to an abrasive prisoner."))
    routesParent.append(gallery_tower)

    gallery_spectre = GalleryParent(18, "spectre", _("The Spectre"), _("The Spectre — The remains of violence free from hesitation."), _("Slay her without a moment's hesitation."))
    routesParent.append(gallery_spectre)

    gallery_nightmare = GalleryParent(19, "nightmare", _("The Nightmare"), _("The Nightmare — Fear locked away in the basement of your mind."), _("Lock your fears away."))
    routesParent.append(gallery_nightmare)

    gallery_razor = GalleryParent(20, "razor", _("The Razor"), _("The Razor — To look too closely is to redraw the lines."), _("She isn't armed... is she?"))
    routesParent.append(gallery_razor)

    gallery_beast = GalleryParent(17, "beast", _("The Beast"), _("The Beast — Softness cornered turns to viciousness."), _("Fall to a feral captive."))
    routesParent.append(gallery_beast)

    gallery_witch = GalleryParent(20, "witch", _("The Witch"), _("The Witch — Offering one hand, while concealing the other."), _("Betray her, before she can betray you."))
    routesParent.append(gallery_witch)

    gallery_stranger = GalleryParent(12, "stranger", _("The Stranger"), _("The Stranger — A peek behind the curtains, likely far too soon."), _("You can't know someone you've never met."))
    routesParent.append(gallery_stranger)

    gallery_prisoner = GalleryParent(17, "prisoner", _("The Prisoner"), _("The Prisoner — Doubt breaks one shackle while forcing another."), _("Free an abrasive prisoner."))
    routesParent.append(gallery_prisoner)

    gallery_damsel = GalleryParent(20, "damsel", _("The Damsel"), _("The Damsel — Unquestioning commitment to the other."), _("Free a gentle captive."))
    routesParent.append(gallery_damsel)


#2nd row

    gallery_needle = GalleryParent(20, "needle", _("The Eye of the Needle"), _("The Eye of the Needle — For those who dwell in caves, meaning lies beyond the shadows dancing on the walls."), _("You need more space. A narrow cave is no place to fight, and it's no place to stay forever."))
    routesParentLower.append(gallery_needle)

    gallery_fury = GalleryParent(20, "fury", _("The Fury"), _("The Fury — An angel felled is a demon scorned."),  _("Angels and Demons are cut from the same cloth, and it's best not to deny a proud being."))
    routesParentLower.append(gallery_fury)

    gallery_apotheosis = GalleryParent(20, "apotheosis", _("The Apotheosis"), _("The Apotheosis — To struggle and fail against the divine is to welcome it into your heart."), _("One might resist the divine, but it is very hard to kill a god. There is no shame in failing."))
    routesParentLower.append(gallery_apotheosis)

    gallery_dragon = GalleryParent(20, "dragon", _("The Princess and the Dragon"), _("The Princess and the Dragon — To excise another is to excise one's self."), _("Sometimes, when you cut something out of you, a piece of you leaves with it."))
    routesParentLower.append(gallery_dragon)

    gallery_wraith = GalleryParent(11, "wraith", _("The Wraith"), _("The Wraith — A broken doll, a spirit slain."), _("Kill your worst dreams, or be killed by the ghost of your past."))
    routesParentLower.append(gallery_wraith)

    gallery_clarity = GalleryParent(14, "clarity", _("The Moment of Clarity"), _("The Moment of Clarity — Bear witness to one's darkest fears."), _("Better to linger with your nightmares than to let them run wild."))
    routesParentLower.append(gallery_clarity)

    gallery_den = GalleryParent(20, "den", _("The Den"), _("The Den — A creature's lair."), _("There are other ways to die to nature than to let it swallow you whole."))
    routesParentLower.append(gallery_den)

    gallery_wild = GalleryParent(12, "wild", _("The Wild"), _("The Wild — Bodies fused. Where does one thing begin and another end?"), _("Become one with the Princess, in a very literal sense. May involve, but does not necessitate, being eaten."))
    routesParentLower.append(gallery_wild)

    gallery_thorn = GalleryParent(19, "thorn", _("The Thorn"), _("The Thorn — Redemption in the thicket of distrust."), _("Sometimes the only way to break a vicious cycle is to put your heart on the line."))
    routesParentLower.append(gallery_thorn)

    gallery_cage = GalleryParent(20, "cage", _("The Cage"), _("The Cage — A vicious cycle framed in chain."), _("When you've seen the worst sights the prison of the world can offer, you can always choose to walk away empty-handed."))
    routesParentLower.append(gallery_cage)

    gallery_grey = GalleryParent(20, "grey", _("The Grey"), _("The Grey — Feelings buried like knives in hearts."), _("There are many reasons spirits may linger. The flames of passion. The flood of words left unspoken."))
    routesParentLower.append(gallery_grey)

    gallery_happy = GalleryParent(20, "happy", _("Happily Ever After"), _("Happily Ever After — Everything you didn't know you wanted."), _("You don't need the world for your happy ending."))
    routesParentLower.append(gallery_happy)

#################Gallery Hints

    class GalleryInitializer:
        def set_galleries(self):
            for i in range(0,len(routesParent)):
                routesParent[i].add_images()
            for i in range(0,len(altRoutesParent)):
                altRoutesParent[i].add_images()
            for i in range(0,len(routesParentLower)):
                routesParentLower[i].add_images()

        def clear_galleries(self):
            for i in range(0,len(routesParent)):
                routesParent[i].clear_images()
            for i in range(0,len(altRoutesParent)):
                altRoutesParent[i].clear_images()
            for i in range(0,len(routesParentLower)):
                routesParentLower[i].clear_images()

        def clear_hints(self):
            for i in range(0,len(routesParent)):
                routesParent[i].clear_hints()
            for i in range(0,len(altRoutesParent)):
                altRoutesParent[i].clear_hints()
            for i in range(0,len(routesParentLower)):
                routesParentLower[i].clear_hints()

        # def unlock_all_galleries_debug(self):
        #     for routeIndex in range(0,len(routesParent)):
        #         routesParent[routeIndex].unlock_gallery()
        #         for itemIndex in range (0, len(routesParent[routeIndex].items)):
        #             routesParent[routeIndex].unlock_item(routesParent[routeIndex].items[itemIndex].itemNumber, False)

        #     for routeIndex in range(0,len(altRoutesParent)):
        #         altRoutesParent[routeIndex].unlock_gallery()
        #         for itemIndex in range (0, len(altRoutesParent[routeIndex].items)):
        #             altRoutesParent[routeIndex].unlock_item(altRoutesParent[routeIndex].items[itemIndex].itemNumber, False)

        #     for routeIndex in range(0,len(routesParentLower)):
        #         routesParentLower[routeIndex].unlock_gallery()
        #         for itemIndex in range (0, len(routesParentLower[routeIndex].items)):
        #             routesParentLower[routeIndex].unlock_item(routesParentLower[routeIndex].items[itemIndex].itemNumber, False)

        def reset_galleries(self):
            for routeIndex in range(0,len(routesParent)):
                routesParent[routeIndex].lock_gallery()
                for itemIndex in range (0, len(routesParent[routeIndex].items)):
                    routesParent[routeIndex].lock_item(routesParent[routeIndex].items[itemIndex].itemNumber)

            for routeIndex in range(0,len(altRoutesParent)):
                altRoutesParent[routeIndex].lock_gallery()
                for itemIndex in range (0, len(altRoutesParent[routeIndex].items)):
                    altRoutesParent[routeIndex].lock_item(altRoutesParent[routeIndex].items[itemIndex].itemNumber)

            for routeIndex in range(0,len(routesParentLower)):
                routesParentLower[routeIndex].lock_gallery()
                for itemIndex in range (0, len(routesParentLower[routeIndex].items)):
                    routesParentLower[routeIndex].lock_item(routesParentLower[routeIndex].items[itemIndex].itemNumber)

        def set_hints(self):
            # Ch1 hints
            gallery_zch1.items[0].hint = _("You're on a path in the woods...")
            gallery_zch1.items[1].hint = _("And at the end of that path is a cabin.")
            gallery_zch1.items[2].hint = _("And in the basement of that cabin...")
            gallery_zch1.items[3].hint = _("Is a Princess.")
            gallery_zch1.items[4].hint = _("Find the Tower.")
            gallery_zch1.items[5].hint = _("Find the Damsel.")
            gallery_zch1.items[6].hint = _("Find the Nightmare.")
            gallery_zch1.items[7].hint = _("Find the Prisoner.")
            gallery_zch1.items[8].hint = _("Find the Spectre.")
            gallery_zch1.items[9].hint = _("Find the Razor.")
            gallery_zch1.items[10].hint = _("Find the Witch.")
            gallery_zch1.items[11].hint = _("Find the Beast.")
            gallery_zch1.items[12].hint = _("Find the Adversary.")
            gallery_zch1.items[13].hint = _("Find the Stranger.")
            gallery_zch1.items[14].hint = _("I thought you said she wasn't armed!")
            gallery_zch1.items[15].hint = _("Get her to break her own chains.")
            gallery_zch1.items[16].hint = _("Always leave a means of easy egress.")
            gallery_zch1.items[17].hint = _("Everything would be so easy if you would just do exactly as I say as quickly as you can.")

            # Mirror hints
            gallery_ztlq.items[0].hint = _("The 'woods.'")
            gallery_ztlq.items[1].hint = _("The 'cabin.'")
            gallery_ztlq.items[2].hint = _("It's you.")
            gallery_ztlq.items[3].hint = _("You've grown.")
            gallery_ztlq.items[4].hint = _("You've withered.")
            gallery_ztlq.items[5].hint = _("You've unraveled.")
            gallery_ztlq.items[6].hint = _("You are nothing at all.")
            gallery_ztlq.items[7].hint = _("The Narrator.")
            gallery_ztlq.items[8].hint = _("Damn both of you to an incomplete existence.")

            # Finale hints

            gallery_zfinale.items[0].hint = _("Finish the game.")
            gallery_zfinale.items[1].hint = _("Finish the game.")
            gallery_zfinale.items[2].hint = _("Find your freedom as gods forever.")
            gallery_zfinale.items[3].hint = _("Find your freedom as gods forever.")
            gallery_zfinale.items[4].hint = _("Go back to where it all started.")
            gallery_zfinale.items[5].hint = _("Go back to where it all started, and meet her face to face.")
            gallery_zfinale.items[6].hint = _("The end is never the end is never the end.")
            gallery_zfinale.items[7].hint = _("Return to your beginning and slay her once and for all.")
            gallery_zfinale.items[8].hint = _("Leave with her, at the end of everything.")
            gallery_zfinale.items[9].hint = _("Leave with her, at the end of everything.")
            gallery_zfinale.items[10].hint = _("Go back to where it all started. You always were a bit of a contrarian, weren't you?")
            gallery_zfinale.items[11].hint = _("We don't think there's a way for us to leave, but maybe there doesn't have to be an ending.")
            gallery_zfinale.items[12].hint = _("We want whatever might be on the other side of this door. Something new, that we'll experience together.")
            gallery_zfinale.items[13].hint = _("Return to your strange beginning and slay her once and for all.")
            gallery_zfinale.items[14].hint = _("The fruits of your labor. A world free from death.")
            gallery_zfinale.items[15].hint = _("Destroy her. Without any outside help.")
            gallery_zfinale.items[16].hint = _("Destroy her. Without any outside help.")
            gallery_zfinale.items[17].hint = _("Destroy her. Without any outside help.")
            gallery_zfinale.items[18].hint = _("Destroy her without any outside help. And then find your new world.")
            gallery_zfinale.items[19].hint = _("Defeat her without any outside help, and then offer her grace.")

    #####Vessels

            # adversary hints
            gallery_adversary.items[0].hint = _("I thought this was supposed to be a cabin.")
            gallery_adversary.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_adversary.items[2].hint = _("Ignore the whiners. If she blocks your attack, you just have to push harder.")
            gallery_adversary.items[3].hint = _("Heeeeeere's Princess!")
            gallery_adversary.items[4].hint = _("Die to her upstairs. Armed.")
            gallery_adversary.items[5].hint = _("Die to her upstairs. Unarmed.")
            gallery_adversary.items[6].hint = _("Witness her resurrection.")
            gallery_adversary.items[7].hint = _("Goad her into giving you a free shot, and then take it.")
            gallery_adversary.items[8].hint = _("Make an obscene gesture, possibly against your will.")
            gallery_adversary.items[9].hint = _("That which cannot die is that which cannot die is that which cannot die.")
            gallery_adversary.items[10].hint = _("You don't need a weapon to win a fight.")
            gallery_adversary.items[11].hint = _("Maybe you do need a weapon, but it's too late now.")
            gallery_adversary.items[12].hint = _("Hey, Princess... I didn't hear no bell.")
            gallery_adversary.items[13].hint = _("Sometimes you have to try and free people even if they don't realize they want to be free.")
            gallery_adversary.items[14].hint = _("Agility is the only way to overcome brute strength.")
            gallery_adversary.items[15].hint = _("It's not a fight if you refuse to strike back.")
            gallery_adversary.items[16].hint = _("It's not a fight if you refuse to strike back.")
            gallery_adversary.items[17].hint = _("You've been here before.")
            gallery_adversary.items[18].hint = _("A bold heart.")
            gallery_adversary.items[19].hint = _("See through her eyes at the end of everything.")

            # apotheosis hints

            gallery_apotheosis.items[0].hint = _("Oh, let me guess! And as the end of the path... is a cabin!")
            gallery_apotheosis.items[1].hint = _("This is how it always was going to end, and this is how it always was going to begin.")
            gallery_apotheosis.items[2].hint = _("Do it, then. Show me what you think it takes to end what's destined to end everything.")
            gallery_apotheosis.items[3].hint = _("Allow an ungrounded voice to tap into your potential.")
            gallery_apotheosis.items[4].hint = _("Walk the razor's edge between courage and madness.")
            gallery_apotheosis.items[5].hint = _("Overpower a psychic barrier.")
            gallery_apotheosis.items[6].hint = _("Make her feel what you have felt.")
            gallery_apotheosis.items[7].hint = _("Her touch is soft.")
            gallery_apotheosis.items[8].hint = _("Carve into her divine heart.")
            gallery_apotheosis.items[9].hint = _("Gift a spiteful reminder to an arrogant god.")
            gallery_apotheosis.items[10].hint = _("Watch as the kindling of your soul burns to ash.")
            gallery_apotheosis.items[11].hint = _("We could have had everything.")
            gallery_apotheosis.items[12].hint = _("If only you'd given me a little more.")
            gallery_apotheosis.items[13].hint = _("What remnant of the old could possibly be left to defy me?")
            gallery_apotheosis.items[14].hint = _("She is drowning.")
            gallery_apotheosis.items[15].hint = _("I am sorry.")
            gallery_apotheosis.items[16].hint = _("Fly, little bird.")
            gallery_apotheosis.items[17].hint = _("You've been here before.")
            gallery_apotheosis.items[18].hint = _("A terrifying and divine heart.")
            gallery_apotheosis.items[19].hint = _("See through her eyes at the end of everything.")

            # beast hints
            gallery_beast.items[0].hint = _("This cabin's seen better days, hasn't it?")
            gallery_beast.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_beast.items[2].hint = _("Get swallowed up by the beast.")
            gallery_beast.items[3].hint = _("Make your way to her heart and end this.")
            gallery_beast.items[4].hint = _("Free her.")
            gallery_beast.items[5].hint = _("Fight her to the death.")
            gallery_beast.items[6].hint = _("Fight her to the death.")
            gallery_beast.items[7].hint = _("Fight her to the death.")
            gallery_beast.items[8].hint = _("What great big eyes you have.")
            gallery_beast.items[9].hint = _("Dodge.")
            gallery_beast.items[10].hint = _("Dodge again.")
            gallery_beast.items[11].hint = _("Dodge until you can dodge no longer.")
            gallery_beast.items[12].hint = _("That hurt. Are you just the cornered animal you seem to be, or could you be a rival?")
            gallery_beast.items[13].hint = _("I didn't mean to do that. I still need to devour you, and it doesn't count if you're dead..")
            gallery_beast.items[14].hint = _("You've been here before.")
            gallery_beast.items[15].hint = _("A cunning heart.")
            gallery_beast.items[16].hint = _("See through her eyes at the end of everything.")

            # cage hints

            gallery_cage.items[0].hint = _("These aren't the same woods. We must be getting closer.")
            gallery_cage.items[1].hint = _("Because getting to the cabin was too easy last time.")
            gallery_cage.items[2].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_cage.items[3].hint = _("You make out a figure standing in the gloom, obscured in shadow.")
            gallery_cage.items[4].hint = _("You give me your implement. See? You already did that part.")
            gallery_cage.items[5].hint = _("This is all getting so predictable, isn't it? Pop.")
            gallery_cage.items[6].hint = _("You only ever thought you were in control. Isn't it so much nicer to let go?")
            gallery_cage.items[7].hint = _("You only ever thought you were in control. Isn't it so much nicer to let go?")
            gallery_cage.items[8].hint = _("You only ever thought you were in control. Isn't it so much nicer to let go?")
            gallery_cage.items[9].hint = _("Both hers and yours collapse, their dance complete.")
            gallery_cage.items[10].hint = _("A peace offering.")
            gallery_cage.items[11].hint = _("The things we leave behind.")
            gallery_cage.items[12].hint = _("At the edge of freedom.")
            gallery_cage.items[13].hint = _("It's a little cold out here, isn't it?")
            gallery_cage.items[14].hint = _("All of that, just to take it all away. You're cold.")
            gallery_cage.items[15].hint = _("I cut myself free.")
            gallery_cage.items[16].hint = _("I cut myself free.")
            gallery_cage.items[17].hint = _("You've been here before.")
            gallery_cage.items[18].hint = _("An open or watchful heart.")
            gallery_cage.items[19].hint = _("See through her eyes at the end of everything.")

            # clarity hints
            gallery_clarity.items[0].hint = _("These aren't the same woods.")
            gallery_clarity.items[1].hint = _("And this isn't the same cabin.")
            gallery_clarity.items[2].hint = _("You're just an object.")
            gallery_clarity.items[3].hint = _("A tool.")
            gallery_clarity.items[4].hint = _("You once were something else, a long time ago.")
            gallery_clarity.items[5].hint = _("But was that something you?")
            gallery_clarity.items[6].hint = _("Or is it just a dull and jaded memory?")
            gallery_clarity.items[7].hint = _("There is no other ending here.")
            gallery_clarity.items[8].hint = _("Just take her hand and set her free.")
            gallery_clarity.items[9].hint = _("For all her past cruelties, the moment feels gentle, tender even.")
            gallery_clarity.items[10].hint = _("And that's the end! I wonder what we're going to do next.")
            gallery_clarity.items[11].hint = _("You've been here before.")
            gallery_clarity.items[12].hint = _("A wise heart.")
            gallery_clarity.items[13].hint = _("See through her eyes at the end of everything.")

            # damsel hints
            gallery_damsel.items[0].hint = _("A prison fitting a royal prisoner.")
            gallery_damsel.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_damsel.items[2].hint = _("Free her from her bindings.")
            gallery_damsel.items[3].hint = _("Free her from her bindings.")
            gallery_damsel.items[4].hint = _("Leave with her.")
            gallery_damsel.items[5].hint = _("Leave with her.")
            gallery_damsel.items[6].hint = _("Leave with her.")
            gallery_damsel.items[7].hint = _("Is it just me or is she... changing?")
            gallery_damsel.items[8].hint = _("No, she's not just changing, she's becoming worse.")
            gallery_damsel.items[9].hint = _("Really worse.")
            gallery_damsel.items[10].hint = _("Oh no.")
            gallery_damsel.items[11].hint = _("Slay her.")
            gallery_damsel.items[12].hint = _("She's changing. You have to slay her. Now!")
            gallery_damsel.items[13].hint = _("She's changing. You have to slay her. Now!")
            gallery_damsel.items[14].hint = _("She's changing. You have to slay her. Now!")
            gallery_damsel.items[15].hint = _("Give her everything she didn't know she wanted.")
            gallery_damsel.items[16].hint = _("You've been here before.")
            gallery_damsel.items[17].hint = _("A gentle heart.")
            gallery_damsel.items[18].hint = _("A pliable heart.")
            gallery_damsel.items[19].hint = _("See through her eyes at the end of everything.")

            # den hints

            gallery_den.items[0].hint = _("The woods are... denser than I remember them.")
            gallery_den.items[1].hint = _("Maybe this used to be a cabin.")
            gallery_den.items[2].hint = _("To be torn between thought and action is to hesitate. And to hesitate is to die.")
            gallery_den.items[3].hint = _("Reject instinct. Fight her to the end.")
            gallery_den.items[4].hint = _("Reject instinct. Fight her to the end.")
            gallery_den.items[5].hint = _("Give yourself to instinct.")
            gallery_den.items[6].hint = _("To consume is to become.")
            gallery_den.items[7].hint = _("Now that's she's stuck, there's nothing stopping you from ending this.")
            gallery_den.items[8].hint = _("I told you not to flinch, I told you.")
            gallery_den.items[9].hint = _("Your work is done. Leave her to starve.")
            gallery_den.items[10].hint = _("Wait in silence for your end.")
            gallery_den.items[11].hint = _("Maybe there's more to her than we thought.")
            gallery_den.items[12].hint = _("Your mouths are full of dirt.")
            gallery_den.items[13].hint = _("She has left you to die.")
            gallery_den.items[14].hint = _("Are we free?")
            gallery_den.items[15].hint = _("Reach the crossroads of will and instinct.")
            gallery_den.items[16].hint = _("What once was you, now is me.")
            gallery_den.items[17].hint = _("You've been here before.")
            gallery_den.items[18].hint = _("A ravenous heart.")
            gallery_den.items[19].hint = _("See through her eyes at the end of everything.")

            # Dragon hints

            gallery_dragon.items[0].hint = _("So that's you.")
            gallery_dragon.items[1].hint = _("There has to be something for you to do other than wait, but that won't stop you from waiting as long as you can.")
            gallery_dragon.items[2].hint = _("Observe your new form.")
            gallery_dragon.items[3].hint = _("A figure emerges, shrouded in a feathered darkness, the world trailing behind it.")
            gallery_dragon.items[4].hint = _("Reveal your identity to some old friends. A brash enough host might do this for you.")
            gallery_dragon.items[5].hint = _("Keep your identity hidden from some old friends. Might require a more receptive host.")
            gallery_dragon.items[6].hint = _("Abandon a gentle companion to her fate.")
            gallery_dragon.items[7].hint = _("What once was one, then was two...")
            gallery_dragon.items[8].hint = _("And then was one again.")
            gallery_dragon.items[9].hint = _("Welcome back! I'm so disappointed in you.")
            gallery_dragon.items[10].hint = _("Fail to disarm a harsh companion.")
            gallery_dragon.items[11].hint = _("Welcome back! Life is all about taking the easy wins, isn't it?")
            gallery_dragon.items[12].hint = _("Attempt to free a gentle companion on your own.")
            gallery_dragon.items[13].hint = _("Leave with a harsh companion.")
            gallery_dragon.items[14].hint = _("Leave with a gentle companion.")
            gallery_dragon.items[15].hint = _("Step into your freedom, together.")
            gallery_dragon.items[16].hint = _("You've been here before.")
            gallery_dragon.items[17].hint = _("An empathetic heart.")
            gallery_dragon.items[18].hint = _("An empathetic heart, held in stencil.")
            gallery_dragon.items[19].hint = _("See through her eyes at the end of everything.")

            # needle hints
            gallery_needle.items[0].hint = _("These aren't the same woods.")
            gallery_needle.items[1].hint = _("And this isn't the same cabin.")
            gallery_needle.items[2].hint = _("I thought this was supposed to be a cabin.")
            gallery_needle.items[3].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_needle.items[4].hint = _("The only mistake you made last time was not pushing yourself hard enough.")
            gallery_needle.items[5].hint = _("The only mistake you made last time was not pushing yourself hard enough.")
            gallery_needle.items[6].hint = _("Give chase. The only way out is through the eye of the needle.")
            gallery_needle.items[7].hint = _("Give chase. The only way out is through the eye of the needle.")
            gallery_needle.items[8].hint = _("Thread the eye of the needle and slay her once and for all.")
            gallery_needle.items[9].hint = _("Thread the eye of the needle and slay her once and for all.")
            gallery_needle.items[10].hint = _("Thread the eye of the needle and slay her once and for all.")
            gallery_needle.items[11].hint = _("Thread the eye of the needle and slay her once and for all.")
            gallery_needle.items[12].hint = _("Thread the eye of the needle and slay her once and for all.")
            gallery_needle.items[13].hint = _("With a skeptic companion, thread the eye of the needle and lead her to the other side.")
            gallery_needle.items[14].hint = _("Give chase, but fail to thread the eye of the needle.")
            gallery_needle.items[15].hint = _("Give chase, but fail to thread the eye of the needle.")
            gallery_needle.items[16].hint = _("Give chase, but fail to thread the eye of the needle.")
            gallery_needle.items[17].hint = _("You've been here before.")
            gallery_needle.items[18].hint = _("A burning heart.")
            gallery_needle.items[19].hint = _("See through her eyes at the end of everything.")

            # FURY hints

            gallery_fury.items[0].hint = _("I thought this was supposed to be a cabin.")
            gallery_fury.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_fury.items[2].hint = _("You are deconstructed. You are reconstructed.")
            gallery_fury.items[3].hint = _("The ball is unraveled into the shape of a body.")
            gallery_fury.items[4].hint = _("The blade is still here, even after everything.")
            gallery_fury.items[5].hint = _("Give her your hand.")
            gallery_fury.items[6].hint = _("I feel so cold. Is it because you're gone?")
            gallery_fury.items[7].hint = _("If only you could remember what I remember. If only you weren't so weak.")
            gallery_fury.items[8].hint = _("A towering heart wounded and alone. One that is familiar to you, if distant.")
            gallery_fury.items[9].hint = _("What are you? You're clearly not your skin.")
            gallery_fury.items[10].hint = _("Come on. One more step. Do it! Hit me! Show me what you're made of!")
            gallery_fury.items[11].hint = _("Preserved, perfectly, in the amber of her torment.")
            gallery_fury.items[12].hint = _("It's not over. We're a god killer. We've returned from death itself twice.")
            gallery_fury.items[13].hint = _("Now, little bird, what was it you wanted to tell me?")
            gallery_fury.items[14].hint = _("Let's see what meaning we can find together. Let's see what we're made of.")
            gallery_fury.items[15].hint = _("We don't need to count anymore.")
            gallery_fury.items[16].hint = _("And then the forces disappear. The bonds holding your cells together break.")
            gallery_fury.items[17].hint = _("A weathered heart.")
            gallery_fury.items[18].hint = _("A weathered heart, held in ribbons.")
            gallery_fury.items[19].hint = _("See through her eyes at the end of everything.")

            # grey hints
            gallery_grey.items[0].hint = _("These aren't the same woods. It wasn't raining before.")
            gallery_grey.items[1].hint = _("These aren't the same woods as before. They're more of a rolling plain.")
            gallery_grey.items[2].hint = _("I can smell the wood rot.")
            gallery_grey.items[3].hint = _("More of a museum than a cabin.")
            gallery_grey.items[4].hint = _("A drowned body.")
            gallery_grey.items[5].hint = _("A desiccated body.")
            gallery_grey.items[6].hint = _("Burning down the house.")
            gallery_grey.items[7].hint = _("What the water gave me.")
            gallery_grey.items[8].hint = _("Burning down the house.")
            gallery_grey.items[9].hint = _("What the water gave me.")
            gallery_grey.items[10].hint = _("Burning down the house.")
            gallery_grey.items[11].hint = _("What the water gave me.")
            gallery_grey.items[12].hint = _("Burning down the house.")
            gallery_grey.items[13].hint = _("Burning down the house.")
            gallery_grey.items[14].hint = _("You've been here before the flames took it all away.")
            gallery_grey.items[15].hint = _("A bright heart.")
            gallery_grey.items[16].hint = _("You've been here before the flood took it all away.")
            gallery_grey.items[17].hint = _("A deep heart.")
            gallery_grey.items[18].hint = _("See through her burning eyes at the end of everything.")
            gallery_grey.items[19].hint = _("See through her drowned eyes at the end of everything.")

            # happy hints

            gallery_happy.items[0].hint = _("Mate, we're clearly already in the cabin.")
            gallery_happy.items[1].hint = _("If the Princess lives here, slaying her would probably... agh, no that's not right.")
            gallery_happy.items[2].hint = _("Deduce the identity of the shadow with the help of a nervous voice.")
            gallery_happy.items[3].hint = _("Dinner's ready.")
            gallery_happy.items[4].hint = _("Finish playing a game with the help of a manipulative voice.")
            gallery_happy.items[5].hint = _("Keep the last flame lit. Forever.")
            gallery_happy.items[6].hint = _("An important part of me is gone, but I'm still here.")
            gallery_happy.items[7].hint = _("It's finally over.")
            gallery_happy.items[8].hint = _("Offer her your hand.")
            gallery_happy.items[9].hint = _("There might be worse things than the end of the world.")
            gallery_happy.items[10].hint = _("Leave with her, hand not in hand.")
            gallery_happy.items[11].hint = _("I meant it, when I said I wanted to dance.")
            gallery_happy.items[12].hint = _("I meant it, when I said I wanted to dance.")
            gallery_happy.items[13].hint = _("I meant it, when I said I wanted to dance.")
            gallery_happy.items[14].hint = _("I meant it, when I said I wanted to dance.")
            gallery_happy.items[15].hint = _("I meant it, when I said I wanted to dance.")
            gallery_happy.items[16].hint = _("You've been here before.")
            gallery_happy.items[17].hint = _("An honest heart.")
            gallery_happy.items[18].hint = _("See through her seated eyes at the end of everything.")
            gallery_happy.items[19].hint = _("See through her eyes at the end of everything as you dance under the stars.")

            # nightmare hints
            gallery_nightmare.items[0].hint = _("Why does nobody ever mention the eyes?")
            gallery_nightmare.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_nightmare.items[2].hint = _("Meet your nightmare.")
            gallery_nightmare.items[3].hint = _("Set your nightmare loose upon the world.")
            gallery_nightmare.items[4].hint = _("Set your nightmare loose upon the world.")
            gallery_nightmare.items[5].hint = _("Set your nightmare loose upon the world.")
            gallery_nightmare.items[6].hint = _("Set your nightmare loose upon the world.")
            gallery_nightmare.items[7].hint = _("Get shoved into a bottomless pit.")
            gallery_nightmare.items[8].hint = _("Get shoved into a bottomless pit.")
            gallery_nightmare.items[9].hint = _("Slay your only exit.")
            gallery_nightmare.items[10].hint = _("See what's behind the mask.")
            gallery_nightmare.items[11].hint = _("See what's behind the mask.")
            gallery_nightmare.items[12].hint = _("See what's behind the mask.")
            gallery_nightmare.items[13].hint = _("See what's behind the mask.")
            gallery_nightmare.items[14].hint = _("See what's behind the mask.")
            gallery_nightmare.items[15].hint = _("See what's behind the mask.")
            gallery_nightmare.items[16].hint = _("You've been here before.")
            gallery_nightmare.items[17].hint = _("A tender heart.")
            gallery_nightmare.items[18].hint = _("See through her eyes at the end of everything.")

            # prisoner hints
            gallery_prisoner.items[0].hint = _("A prison. Just like it should be.")
            gallery_prisoner.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_prisoner.items[2].hint = _("I'm not locked in here with you. We're both locked in here together.")
            gallery_prisoner.items[3].hint = _("I'm not locked in here with you. We're both locked in here together.")
            gallery_prisoner.items[4].hint = _("I'm not locked in here with you. We're both locked in here together.")
            gallery_prisoner.items[5].hint = _("I'm not locked in here with you. We're both locked in here together.")
            gallery_prisoner.items[6].hint = _("What could go wrong with handing her your weapon? She's locked up.")
            gallery_prisoner.items[7].hint = _("Successfully free her.")
            gallery_prisoner.items[8].hint = _("Enter a violent confrontation.")
            gallery_prisoner.items[9].hint = _("Enter a violent confrontation.")
            gallery_prisoner.items[10].hint = _("Slay her.")
            gallery_prisoner.items[11].hint = _("Receive vital evidence of the Princess' wrongdoings.")
            gallery_prisoner.items[12].hint = _("You've been here before, and now you're here again. Whole.")
            gallery_prisoner.items[13].hint = _("A patient heart.")
            gallery_prisoner.items[14].hint = _("You've been here before, and now you're here again. But this time without a head.")
            gallery_prisoner.items[15].hint = _("A clever heart.")
            gallery_prisoner.items[16].hint = _("See through her eyes at the end of everything.")

            # razor hints
            gallery_razor.items[0].hint = _("What a mess.")
            gallery_razor.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_razor.items[2].hint = _("But her hands were behind her back!")
            gallery_razor.items[3].hint = _("Okay. I'm bored.")
            gallery_razor.items[4].hint = _("She said she wasn't armed. So what's the harm in getting a little closer?")
            gallery_razor.items[5].hint = _("Now hold on... these aren't the woods.")
            gallery_razor.items[6].hint = _("What... is this place? This is not the same cabin.")
            gallery_razor.items[7].hint = _("Meet her. Again.")
            gallery_razor.items[8].hint = _("Call an ambulance... but not for me!")
            gallery_razor.items[9].hint = _("Make her blush.")
            gallery_razor.items[10].hint = _("You've lost track of yourself, haven't you?")
            gallery_razor.items[11].hint = _("This isn't even my final form.")
            gallery_razor.items[12].hint = _("Meet a mutual end.")
            gallery_razor.items[13].hint = _("Empty your mind. Be formless. Shapeless. Like water.")
            gallery_razor.items[14].hint = _("Empty your mind. Be formless. Shapeless. Like water.")
            gallery_razor.items[15].hint = _("You've been here before, this time with a cage of iron.")
            gallery_razor.items[16].hint = _("A piercing heart in a cage of iron.")
            gallery_razor.items[17].hint = _("You've been here before, this time with a heart beating free.")
            gallery_razor.items[18].hint = _("A piercing heart beating free.")
            gallery_razor.items[19].hint = _("See through her eyes at the end of everything.")

            # spectre hints
            gallery_spectre.items[0].hint = _("It's been a long time since anyone's been here, hasn't it?")
            gallery_spectre.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_spectre.items[2].hint = _("Meet the Spectre.")
            gallery_spectre.items[3].hint = _("Let a spirit into your home.")
            gallery_spectre.items[4].hint = _("Let a spirit into your home.")

            gallery_spectre.items[5].hint = _("Free a lost soul.")
            gallery_spectre.items[6].hint = _("Free a lost soul.")
            gallery_spectre.items[7].hint = _("Free a lost soul.")

            gallery_spectre.items[8].hint = _("Provoke an angry spirit.")
            gallery_spectre.items[9].hint = _("Provoke an angry spirit.")
            gallery_spectre.items[10].hint = _("Take on a spirit and exorcise it from your body.")
            gallery_spectre.items[11].hint = _("Take on a spirit and exorcise it from your body.")

            gallery_spectre.items[12].hint = _("A spirit checks for a pulse.")
            gallery_spectre.items[13].hint = _("Attack a spirit with cold steel. No hesitation.")
            gallery_spectre.items[14].hint = _("Abandon a spirit to its torment.")
            gallery_spectre.items[15].hint = _("You've been here before.")
            gallery_spectre.items[16].hint = _("A yearning heart.")
            gallery_spectre.items[17].hint = _("See through her eyes at the end of everything.")

            # stranger hints
            gallery_stranger.items[0].hint = _("I thought this was supposed to be a cabin.")
            gallery_stranger.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_stranger.items[2].hint = _("And at the center of it all is something that can only be described as...")
            gallery_stranger.items[3].hint = _("What— what the hell was that?! What happened to us?")
            gallery_stranger.items[4].hint = _("Split her as much as you're able.")
            gallery_stranger.items[5].hint = _("To be everything is to be nothing at all.")
            gallery_stranger.items[6].hint = _("To be everything is to be nothing at all.")
            gallery_stranger.items[7].hint = _("To be everything is to be nothing at all.")
            gallery_stranger.items[8].hint = _("To be everything is to be nothing at all.")
            gallery_stranger.items[9].hint = _("You've been here before.")
            gallery_stranger.items[10].hint = _("A rich and vibrant heart.")
            gallery_stranger.items[11].hint = _("See through her eyes at the end of everything.")

            # thorn hints
            gallery_thorn.items[0].hint = _("These aren't the same woods.")
            gallery_thorn.items[1].hint = _("And this isn't the same cabin.")
            gallery_thorn.items[2].hint = _("I thought this was supposed to be a cabin.")
            gallery_thorn.items[3].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_thorn.items[4].hint = _("Strike at a thorny rose's heart.")
            gallery_thorn.items[5].hint = _("Share a thorny prison of your own making.")
            gallery_thorn.items[6].hint = _("She's going to swallow it out of spite, isn't she?")
            gallery_thorn.items[7].hint = _("Turn over a new leaf and learn to trust again.")
            gallery_thorn.items[8].hint = _("Turn over a new leaf and learn to trust again.")
            gallery_thorn.items[9].hint = _("Turn over a new leaf and learn to trust again.")
            gallery_thorn.items[10].hint = _("Turn over a new leaf and learn to trust again.")
            gallery_thorn.items[11].hint = _("Turn over a new leaf and learn to trust again.")
            gallery_thorn.items[12].hint = _("Turn over a new leaf and learn to trust again.")
            gallery_thorn.items[13].hint = _("Turn over a new leaf and learn to trust again.")
            gallery_thorn.items[14].hint = _("Kiss the girl.")
            gallery_thorn.items[15].hint = _("Kiss the girl.")
            gallery_thorn.items[16].hint = _("You've been here before.")
            gallery_thorn.items[17].hint = _("A cautious heart.")
            gallery_thorn.items[18].hint = _("See through her eyes at the end of everything.")

            # tower hints
            gallery_tower.items[0].hint = _("More like a temple than a cabin.")
            gallery_tower.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_tower.items[2].hint = _("Resist a god through force of arms.")
            gallery_tower.items[3].hint = _("Resist a god through force of arms, but ultimately succumb.")
            gallery_tower.items[4].hint = _("Try to resist a god purely through force of will. No weapons.")
            gallery_tower.items[5].hint = _("Free a god to bring about the end of everything.")
            gallery_tower.items[6].hint = _("Free a god to bring about the end of everything.")
            gallery_tower.items[7].hint = _("Fell a god.")
            gallery_tower.items[8].hint = _("Fell a god.")
            gallery_tower.items[9].hint = _("Fell a god.")
            gallery_tower.items[10].hint = _("You've been here before.")
            gallery_tower.items[11].hint = _("An overwhelming heart.")
            gallery_tower.items[12].hint = _("See through her eyes at the end of everything.")

            # wild hints
            gallery_wild.items[0].hint = _("We are a path in the woods.")
            gallery_wild.items[1].hint = _("A glimpse of freedom.")
            gallery_wild.items[2].hint = _("Gaze into the heart of darkness.")
            gallery_wild.items[3].hint = _("Separate doesn't mean over.")
            gallery_wild.items[4].hint = _("Separate doesn't mean over.")
            gallery_wild.items[5].hint = _("Separate before ending it all.")
            gallery_wild.items[6].hint = _("You've been here before, and now you're back. Even if you've been separated by forces beyond your will.")
            gallery_wild.items[7].hint = _("A curious and beautiful heart.")
            gallery_wild.items[8].hint = _("You've been here before. This time you've carried a wound.")
            gallery_wild.items[9].hint = _("A scarred and beautiful heart.")
            gallery_wild.items[10].hint = _("See through her woven eyes at the end of everything.")
            gallery_wild.items[11].hint = _("See through her wounded eyes at the end of everything.")

            # witch hints
            gallery_witch.items[0].hint = _("I thought this was supposed to be a cabin.")
            gallery_witch.items[1].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_witch.items[2].hint = _("Make a peace offering to someone you betrayed.")
            gallery_witch.items[3].hint = _("Fight dirty in a direct confrontation.")
            gallery_witch.items[4].hint = _("Fight dirty in a direct confrontation.")
            gallery_witch.items[5].hint = _("Fight dirty in a direct confrontation.")
            gallery_witch.items[6].hint = _("Fight dirty in a direct confrontation.")
            gallery_witch.items[7].hint = _("Fight her until the world itself swallows you up.")
            gallery_witch.items[8].hint = _("Fight her until the world itself swallows you up.")
            gallery_witch.items[9].hint = _("One of you has to go first. Might as well be you.")
            gallery_witch.items[10].hint = _("One of you was always going to betray the other. Might as well be you doing the betraying.")
            gallery_witch.items[11].hint = _("You're not turning your back to her.")
            gallery_witch.items[12].hint = _("You're not turning your back to her.")
            gallery_witch.items[13].hint = _("You're not turning your back to her.")
            gallery_witch.items[14].hint = _("You're not turning your back to her.")
            gallery_witch.items[15].hint = _("The entire cabin is collapsing around you. Maybe the two of you should stop fighting?")
            gallery_witch.items[16].hint = _("You've been here before.")
            gallery_witch.items[17].hint = _("A righteous heart.")
            gallery_witch.items[18].hint = _("See through her broken eyes at the end of everything.")
            gallery_witch.items[19].hint = _("See through her confident eyes at the end of everything.")

            # wraith_hints
            gallery_wraith.items[0].hint = _("These aren't the same woods.")
            gallery_wraith.items[1].hint = _("And this isn't the same cabin.")
            gallery_wraith.items[2].hint = _("I thought this was supposed to be a cabin.")
            gallery_wraith.items[3].hint = _("If the Princess lives here, slaying her would probably be doing her a favor.")
            gallery_wraith.items[4].hint = _("You are nothing but a passenger.")
            gallery_wraith.items[5].hint = _("Set your demons loose upon the world.")
            gallery_wraith.items[6].hint = _("You're the only prison that can hold your demons.")
            gallery_wraith.items[7].hint = _("There is no choice here. She will take what she is owed.")
            gallery_wraith.items[8].hint = _("You've been here before.")
            gallery_wraith.items[9].hint = _("A driven heart.")
            gallery_wraith.items[10].hint = _("See through her eyes at the end of everything.")

    galleryInitializer = GalleryInitializer()
    galleryInitializer.set_galleries()
