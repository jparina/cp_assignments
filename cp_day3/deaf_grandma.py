def deaf_grandma():
    grandma_says = "HEY KID!"
    second_goodbye = False
    
    while True:
        print(f"{grandma_says}")
        response = input()
        
        if response == "GOODBYE!" and second_goodbye == True:
            grandma_says = "LATER, SKATER!"
            break
        elif response == "GOODBYE!" and second_goodbye == False:
            second_goodbye = True
            grandma_says = "LEAVING SO SOON?"
            continue
        elif response == "":
            grandma_says = "WHAT?!"    
        elif response.upper() == response:
            grandma_says = "NO, NOT SINCE 1946!"  
        else:
            grandma_says = "SPEAK UP, KID!"
        second_goodbye = None
    
deaf_grandma()