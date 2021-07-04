def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

alpha = 2
beta = alpha-1

if alpha:
    print(colored(255,0,0, 'This is red'))
    if beta:
        print(colored(0,0,255, 'This is blue'))
        beta -= 1
        
        
