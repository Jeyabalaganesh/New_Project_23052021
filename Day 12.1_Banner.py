def banner(text:str,set_screen=80)-> str:
    """

    Args: Just to show the banner msg
        text: any "str' value
        set_screen: Keyword only arg, By defalut the value assigned as 80

    Returns: nothing

    """
    if len(text)-4 > set_screen:
        print("The entered text is too long for the screen")
    elif text == "*":
        print(text * set_screen)
    else:
        centered_text = text.center(set_screen-4)
        print("**{}**".format(centered_text))

banner("*",60)
banner("",60)
banner("",60)
banner("Hello",60)
banner("My name is Jeyabalaganesh",60)
banner("",60)
banner("",60)
banner("*", 60)


