name = input("The king has sought for your help in saving the kingdom from the evil snake. "
             "Are you the Healer, Knight or Hunter?or q to quit ").lower()
healer_health = 100
knight_health = 100
Hunter_health = 100
while True:
    if name=="q":
        print("oops! You dont want to take part?")
        quit()
    
    if name == "healer":
        print("Thank you for answering this call.")
        plot=input("As you start the journey,you are asked if you would like to go through the forest or the city? ").lower()
        if plot=="forest":
            print("You get to pick up 5 powerful plants used to make a healing potion!")
            potion="healing alixur"
            potion=1
            plot=input("Somebody is crying for help,do you either help them or leave them?").lower()
            if plot==("help") or plot==("help them"):
                print("AHA! it turns out to be the evil snake's minion.You get caught!")
                continue
            elif plot=="leave" or plot==("leave them"):
                print("You are smart ! it turns out to be the evil snake's minion and you manage to slip out of the trap!")
                plot=input("Barely making it out alive ,you are contemplating to either use the healing alixur or to tough it out?").lower()
                if plot=="use potion" or plot=="use heaing alixur":
                    print("Your health is replenished!")
                    potion-=1
                elif plot=="tough it out" or plot=="no potion" or plot=="no healing alixur":
                    print("Welp! your health damage is 20!")
                    healer_health-=20
                    plot=input("You get sucked into a wormhole, you have two seconds to think of how to get out either run or do nothing: ").lower()
                if plot=="run" or plot=="do nothing":
                    print("Womp Womp! your time ends")
                    continue
                    

   
            elif plot=="city":
                print("When passing through ,you meet a friend who make a contribution to your quest be giving you 5 gold coins!")
                coins="gold coins"
                coins=1
                plot=input("A girl checks you out and asks you to follow here,do you go or not?").lower()
                
                if plot==("go"):
                    print("AHA! it turns out to be the evil snake's minion.You get caught!")
                    continue
                elif plot=="not" :
                    print("You are smart ! it turns out to be the evil snake's minion but since you dont have a healing portion , you get badly damaged!")
                    plot=input("Barely making it out alive ,you are contemplating to either buy the portion or to tough it out?").lower()
                    if plot=="buy potion" :
                        print("Your health is replenished!")
                        coins-=1
                    elif plot=="tough it out" or plot=="no potion" :
                        print("Welp! your health damage is 80!")
                        healer_health-=80
                        plot=input("Before continuing with your quest a hungry cute boy asks if you could buy him some bread,do you buy or send him of his way?").lower()
                        if coins==1:
                            print("Womp womp ,the boy gets an alergic reation and dies! yeah and you also die of shame")
                            continue
                        else:
                            print("Since you had no money left ,he died and you also died of shame!")
                            continue

    elif name=="knight":
            print("I trust the kingdom is in good hands.")
            plot=input("As you start the journey,you are asked if you would like to go through the forest or the city? ").lower()
            if plot=="forest":
                print("You dumbass!The evil snake had already layed traps and you didnt send a scout to check first!")
                knight_health-=30
                plot=input("You are left to either be selfless and stay with your men or you abandonded them...").lower()
                if plot==("stay") or plot==("help them"):
                      print("Very selfless but you guys still get defeated and you die as an hounarable man!")
                      continue
                elif plot=="abandon" or plot==("leave them"):
                      print("Yooh low blow ! you dont get very far because of your wounds and die painfully!!")
                      continue
            else:
                      plot==city
                      print("!Bad decision man, none like you over there cause you burnt down the market but in your defence, it was accidental")
                      plot=input("So do you still go through the city or not? ").lower()
                      if plot==("go through"):
                           print("Well... That was brave but the people didnt have it , so you and your men got into a bit fight.and died!!")
                           continue
                      elif plot=="not" :
                           print("Wise decision but your men called you a pussy and left you ,so you have to go on alone")
                           plot=input("Your men leaving you was devastating but you move on regardless, and it turns out the city dewellers are still out for head and send your former men after you , do you hide or fight?").lower()
                           if plot=="hide" :
                                print("Haha! they still find you and kill you!")
    elif plot=="FIGHT":
                                print("Welp! it was a fierce fight that left you with 90 damage")
                                knight_health-=90
                                plot=input("As you are taking in your final breaths ,you reminise about the life you had and in those final moments ,visions or your son come so what do you do? say sorry or laugh ").lower()
                                if plot=="sorry":
                                    print("Dude you left your child traumatized!!")
                                    continue
                                elif plot=="laugh":
                                     print("You left him double traumatized")
                                     continue
    else:
        name=="Hunter"
        print("May your quest be successful.")
        plot=input("As you start the journey,you are asked if you would like to go through the forest or the city? ").lower()
        if plot=="forest":
            print("You get to pick up 5 powerful plants used to make a healing potion!")
            potion="healing alixur"
            potion=1
            plot=input("Somebody is crying for help,do you either help them or leave them?").lower()
            
            if plot==("help") or plot==("help them"):
                        print("AHA! it turns out to be the evil snake's minion.You get caught!")
                        continue
            elif plot=="leave" or plot==("leave them"):
                        print("You are smart ! it turns out to be the evil snake's minion and you manage to slip out of the trap!")
                        plot=input("Barely making it out alive ,you are contemplating to either use the healing alixur or to tough it out?").lower()
                        if plot=="use potion" or plot=="use heaing alixur":
                            print("Your health is replenished!")
                            potion-=1
                        elif plot=="tough it out" or plot=="no potion" or plot=="no healing alixur":
                            print("Welp! your health damage is 20!")
                            healer_health-=20
                            plot=input("You get sucked into a wormhole, you have two seconds to think of how to get out either run or do nothing: ").lower()
                            if plot=="run" or plot=="do nothing":
                                print("Womp Womp! your time ends")
                                continue

    