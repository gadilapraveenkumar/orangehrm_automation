from behave.__main__ import main

main(["features/LHN.feature", "-t", "lhn_menu_validation","--no-capture"])
#main("features/LHN.feature -t lhn_menu_validation --no-capture")