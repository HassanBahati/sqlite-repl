from prompt_toolkit import PromptSession

def main():
    session = PromptSession()

    while True:
        # prompt user for text input 
        try:
            text = session.prompt('> ')
        # continue to next line and get more user input when ctrlC has been pressed
        except KeyboardInterrupt:
            continue
        # exit the terminal when ctrlD has been pressed
        except EOFError:
            break
        else:
            print('Goodbye!')

main()