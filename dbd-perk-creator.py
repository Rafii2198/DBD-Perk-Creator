#!/usr/bin/env python

from gimpfu import *
import json

def get_settings(settingsFile) :
    with open(settingsFile) as f :
        data = json.load(f)
    return(data)

def dbd_perk_creator(inputFolderBack, inputFolderIcons, outputFolder) :

    settings = get_settings(inputFolderBack + "\settings.json")
    for perk in settings:
        new_image = pdb.gimp_image_new(256,256,0)
        back_layer = pdb.gimp_file_load_layer(new_image, inputFolderBack + "/" + str(perk["tier"]) + ".png")
        pdb.gimp_image_insert_layer(new_image, back_layer, None, 0)
        main_layer = pdb.gimp_file_load_layer(new_image, inputFolderIcons + perk["dir"])
        pdb.gimp_image_insert_layer(new_image, main_layer, None, 0)
        pdb.gimp_file_save(new_image, pdb.gimp_image_merge_visible_layers(new_image, 1), outputFolder + perk["dir"], "?")
        pdb.gimp_image_delete(new_image)
    return

register(
    "python_fu_dbd_perk_creator",
    "Creates perk icons",
    "Creates perk icons from background images and perk icon folder. Supports multiple levels of perks.",
    "Rafii2198",
    "Open source",
    "2021",
    "<Image>/Tools/Rafii's DBD/Perk Creator",
    "*",
    [
        (PF_DIRNAME, "inputFolderBack", "Folder with background and settings files", ""),
        (PF_DIRNAME, "inputFolderIcon", "Folder with DBD icons", ""),
        (PF_DIRNAME, "outputFolder", "Output folder", ""),
    ],
    [],
    dbd_perk_creator, menu="<Image>/Tools/Rafii's DBD/Perk Creator")

main()
