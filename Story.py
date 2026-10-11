print('\n -------Choose Your Faith-----------')

print('Your Genre are :  Action, Comedy, Horror, Romance, Drama , Scifi ,Mystery,Western')
name = input('Enter your Hero name:')

choice = input('What is your Genre?:')
if choice == 'Action':
    print('You have chosen Action')
    print('Option A: Jumping an open bridge to escape police chase')
    print('Option B: Fighting an army against hero, one vs many\n')
    option = input("Choose Option A or B: ")
    if option == 'A':
        print('\nNervous,', name, 'presses on the accelerator as he gets sweaty.')
        print('The car hits 200km/h on the dash with the bridge ramp just 100 meters away.')
        print('He takes the huge jump! The car hangs in mid-air for three seconds,')
        print('crashing down onto the other side and escaping the chaos.\n')

        print("Choose your next action:")
        print("1) Hide in the warehouse with the car until the police stop searching.")
        print("2) Leave the car behind and escape on foot by mixing with the crowd in the city.")
        opt = input("Enter your choice (1 or 2): ")

        if opt == '1':
            print('\n', name, 'Finds a concealed warehouse and parks the car within it immediately.')
            print(' He switches off the engine and crouches in the dark shadows, waiting for the cops to abandon their mission.')
            print(',But time passes by, and finally, he hears the sounds of sirens disappear in the distance.\n')
        elif opt == '2':
            print('\n', name, 'abandons the car and slips into the bustling city streets.')
            print('He blends in with the crowd, using his knowledge of the city to navigate through alleyways and side streets.')
            print('After a tense few hours, he finds a safe place to rest, knowing he has successfully escaped the police.\n')

    elif option == 'B':
        print('\n', name, 'faces the army head-on, using his combat skills to take down multiple enemies.')
        print('Despite being outnumbered, he manages to hold his ground and defeat the army, emerging victorious.\n')

        print("Choose your next action:")
        print("1) Call for backup to secure the area.")
        print("2) Retreat to a safe location to regroup.")
        opt = input("Enter your choice (1 or 2): ")

        if opt == '1':
            print('\n', name, 'calls for backup and soon reinforcements arrive to secure the area.')
            print('Together, they ensure that the threat is neutralized and the mission is completed .\n')
        elif opt == '2':
            print('\n', name, 'decides to retreat to a safe location to regroup with his team and plan his next move.')
            print('He finds a secluded spot and plans the next move before futher action.\n')
        else:
            print('Invaild choice, Pls try again')
  
elif choice == 'Comedy':
    print('You have chosen Comedy')
    print('Option A: Slapstick comedy in a busy restaurant')
    print('Option B: A series of funny misunderstandings at a wedding\n')
    opt=input('Choose Option A or B: ')
    if opt == 'A':
     print('\n',name,'dresses up as a waiter in a high-class five-star hotel.')
     print('As he maintains an impossible tower of soup bowls, his foot trips on a fallen breadstick.')
     print('With the grace of a fumbling dancer, he twirls around and dumps a bowl of tomato soup onto the desk of the most fearsome food critic at the restaurant.\n')
     print('Option (1):Apologize while trying to remove it using a cloth napkin')
     print('option (2):Assume that it was deliberate and shout “Artistic soup drizzle!”')
     opt1=input('choose your next action (1 or 2):')
     if opt1=='1':
            print('\n',name,'scrubs wildly, leaving the vibrant red soup smeared into a huge heart shape.')
            print('Looking at his shoes, he laughs at the ridiculousness and demands to meet the bumbling cook.\n')
     elif opt1=='2':
           print('\n',name,'bows in astonishment as everyone in the dining room looks on.')
           print('A critic at the table claps and says it is "daring culinary theater" and the shift is saved.\n')
    elif opt=='B':
     print('\n',name,' appears for the wedding ceremony with the wrong gift box.')
     print('Misunderstanding unfolds dramatically when everyone believes that he is the fugitive bridegroom!.\n')
     print('Option (1): Seize the microphone and make an attempt to explain the truth in the entire hall')
     print('Option (2): Use the multi-layered wedding cake as a cover to make your way out.')
     opt2=input('choose your next action (1 or 2):')
     if opt2=='1':
       print('\n',name,'coughs but is met by a screeching microphone.')
       print('The people start laughing, believing that it was a prepared joke in a toast.\n')
     elif opt2=='2':
       print('\n',name,'Inadvertently knocks into the table, making the cake wobble about violently.')
       print('He manages to grab the highest level just in time, earning applause for his fast reflexes!\n')
    else:
       print('Invaild choice, Please try again')


elif choice == 'Horror':
        print('You have chosen Horror')
        print('Option A: Investigating an old mental hospital at night in the mist')
        print('Option B: Imprisoned in a silent basement during electrical interruptions\n')
        opt=input('Choose Option A or B: ')
        if opt == 'A':
            print('\n', name,'past rusted iron gates amidst the thick fog rolling through the courtyard.')
            print('The cold air makes his face feel cold, and there is a floorboard creaking from upstairs.')
            print('Option (1): Activate your flashlight and climb up the spiraling staircase')
            print('Option (2): Sneak into the archive and crouch under an ancient steel desk.')
            act=input('Choose your next action:')
            if act == '1':
              print('\n',name,'points the thin stream up, showing the shadows scurrying about the corner')
              print('He feels his heart beat fast while he hangs on to the railing and keeps quiet.\n')
            elif act == '2':
              print('\n',name,"crouches under the table as footsteps tread heavily by the entrance to the room.")
              print('He waits silently until the sound of footsteps recedes into the distance.\n')
        elif opt =='B':
          print('\n',name,'hears the loud slam of the cellar door being shut and locked.')
          print('The single overhead bulb buzzes, flickers, and completely dies out.')
          print('Option (1): Feel along the stone wall to search for an old circuit breaker box. ')
          print('Option (2): Light one match and shout out loud to see if there’s anybody else in the room with you.')
          act2 = input('Choose Your Option(1/2):')
          if act2 == "1":
            print('\n',name,'runs his hands over the cool, wet bricks until he feels a metal lever.')
            print('"Upward he flicks the switch with a resounding clank, and the emergency lights begin to glow."\n')
          elif act2 == '2':
            print('\n',name,'sets the flame alight; a small flame highlights a dark shape sitting opposite.')
            print('The flame goes out abruptly with a soft hiss, leaving only the sound of heavy breathing.\n')
          else:
            print('Invaild choice ,Try again')

elif choice == 'Drama':
    print('You Have Choosen Drama')
    print('Option A: The meeting with the business partner who took your plans')
    print('Option B: Returning to a quiet hometown to face an unresolved family secret\n')
    opt = input('Choose your Option(A/B):')
    if opt == "A":
        print("\n",name,"enters the private office late in the night through stealth..")
        print('Across the mahogany desk from him sits his old partner, clutching the fake contract.\n')
        print("Option (1): Open the wax seal and immediately read the letter.")
        print("Option (2): Knock on the heavy oak door and confront the past directly.")
        act = input("Choose Your Option(1/2):")
        if act =='1':
            print('\n',name,'Slams the old ledger on the desk; silence falls in the room.')
            print('She realizes that the game is over, and then reluctantly gives him the access keys.\n')
        elif act =='2':
            print("\n",name,"moves the amended agreement along with a resolute stare.")
            print('He has his accomplice smirk, sign the deal, and agrees to keep the past buried.')
    elif opt =='B':
        print('\n',name,'is standing in front of the family’s old house during a rainy day.')
        print('A letter unopened is lying on the table in the front porch, sealed with red wax.')
        print('Option (1): Break the seal on the letter and read it immediately.')
        print('Option (2): Knock on the hefty oak door and face up to the past.')
        act2 = input('Choose Your Option(1/2):')
        if act2 == '1':
         print('\n',name,'reads his handwriting, and discovers that his estate was never lost.')
         print('Now that he knows the truth, he enters fully prepared to take back what is rightfully his.\n')
        elif act2 == '2':
          print('\n',name,'hears the footsteps approaching before the door slowly creaks open.')
          print('An older mentor comes out crying with apologies that he should have offered years ago.\n')
        else:
             print('Invalid choice, Pls try again')


elif choice == 'Romance':
    print('You Have Choosen Romance')
    print('Option A: Meeting an acquaintance in a busy train station when it is raining')
    print('Option B: Discovering a long-forgotten handwritten letter hidden in a dusty library book.\n ')
    opt = input('Choose your Option(A/B):')
    if opt =='A':
        print('\n',name,'races under the station roof as soon as the rains start..')
        print('There is a person standing on the platform carrying an umbrella.\n')
        print('Option (1): Go up to them and start talking about the late train.')
        print('Option (2): Offer him a steaming coffee mug and wait outside under the covered awning.')
        act = input('Choose Your Option(1/2): ')
        if act == '1':
           print('\n',name,'laughs about the delay in commuting; the silence is broken.')
           print('They smile at each other and agree to sit together during the journey.\n')
        elif act == '2':
           print('\n',name,'hands over the warm drink with a genuine smile')
           print('A calm, cozy discussion starts as the rain gently leaves.')
    elif opt == 'B':
        print('\n',name,'pulls an old book from the shelf in a secluded corner.')
        print('From between the pages falls a folded envelope, marked by dried lavender flowers.')
        print('Option (1): Open the letter immediately to determine who left it.')
        print('Option (2): Leave something in the reply to check if they will come back. ')
        act2 = input('Choose Your Option(1/2):')
        if act2 == '1':
            print('\n',name,"sees the note and understands that the writer is sitting at a table nearby.")
            print('Now knowing the truth, a new conversation starts across the room.\n')
        elif act2 == '2':
            print('\n',name,'Slips the note back and waits silently beside the window.')
            print('The stranger returns later that afternoon, noticing your response with a smile.')
        else:
            print('Invalid choice, Pls try again')

elif choice == "Scifi" or 'Sci-fi':
    print('You Have choosen Scifi')
    print('Option A: Exploring distress signal from a deserted research facility')
    print('Option B: Flying a damaged reconnaissance spacecraft through an unknown asteroid belt')
    opt = input('Choose Your Option(A/B): ')
    if opt == 'A':
        print('\n',name,"lands at the silent station airlock amid flashing red emergency lights.")
        print('Further down the hallway, the principal terminal continues to blink with encoded telemetry data.\n')
        print('Option (1): Interfacing with the core of the AI system to download mission logs.')
        print('Option (2): Manually bypass the reactor door to bring back auxiliary power.')
        next= input('What is your Next Act: ')
        if next == '1':
         print('\n',name,'Decodes core telemetry; the terminal shows coordinates of planets.')
         print('The secret logs expose a mysterious jump gate orbiting the outer rim.\n')
        elif next == '2':
         print('\n',name,'triggers the reactor release mechanism, ensuring containment fields stability.')
         print('The lights in the station flicker on, ensuring your path back to the spaceship.\n')
    elif opt == 'B':
        print('\n',name,'grasps the steering wheels while sirens wail throughout the instrument panel.')
        print('A cloud of high-density orbital debris rapidly approaches your flight path.\n')
        print('Option(1): Divert the backups from the rear shields and engage the full thrust.')
        print('Option(2): Turn off primary radar system to move stealthily within the gravity well.') 
        act2 = input('What is Your Next Act: ')
        if act2 =='1':
         print('\n',name,"maximizes energy usage; the ship cuts through the drift.")
         print("With clear trajectory, Astra-9 attains its cruising velocity in orbit and escapes.\n")
        elif act2 == '2':
         print('\n',name,'glides through the dark field, slipping beneath enemy sensor scans.')
         print('The thrusters fire up again on the other side, putting the danger well behind them.\n')
        else:
          print('Invalid choice, Pls try again')

elif choice == "Mystery":
        print('You Have Choosen Mystery')
        print('Option A: Examining a ransacked office located in a harbor warehouse')
        print('Option B: Crime scene examination at an abandoned train station clock tower.\n')
        opt = input("What is your Option (A/B): ")
        if opt =="A":
           print('\n',name,'Steps across the shattered doorframe, flashlight beam slicing through airborne dust.')
           print('The papers are strewn about on the wooden floor, and an open floor safe is visible.\n')
           print('Option(1):Check the scratch marks on the safe door to see who opened it.')
           print('Option(2): Check the rear emergency exit for any footprints left in the mud.')
           act = input('What is Your Next Act(1/2): ')
           if act == '1':
              print('\n',name,'discovers fine metal filings and a distinctive monogrammed tool mark.')
              print('The signature points straight to a notorious syndicate safe-cracker.\n')
           elif act == '2':
              print('\n',name,'boot prints can be seen heading towards the docks.')
              print('Following the trail closely, you catch sight of a suspect boarding a cargo tug.\n')
        elif opt == 'B':
           print('\n',name,'climbs the spiral staircase into the hollow interior of the clocktower.')
           print('The giant brass gears click overhead, and a vintage pocket watch lies on the ledge.')
           print('Option(1):Take the pocket watch while covering your hands with a handkerchief')
           print('Option(2): Peer through the damaged glass of the clock to get a view of the railway yard below.')
           act2 = input('What is Your Next Act: ')
           if act2 == "1":
              print('\n',name,'pops the watch open to see a schedule slip that is encrypted')
              print('The departure times reveal exactly which freight carriage holds the contraband.\n')
           elif act2 == '2':
              print('\n',name,'Sees through the window and notices an erratic signal light near track number four.')
              print('The suspect is signaling an accomplice; you descend quickly to cut them off.\n')

elif choice == "Western":
   print('You Have Choosen Western')
   print('Option(A):Defense of a desert canyon outpost against a gang of outlaws')
   print('Option(B):Tracking a runaway steam locomotive across an abandoned mountain pass\n')
   opt = input('What is Your Option(A/B):')
   if opt == "A":
      print('\n',name,'ducks hiding behind the aged timber water tower as sand flies above the ridge.')
      print('A bunch of bandits rides into the canyon and blocks the main exit route.\n')
      print('Option (1): Shoot from atop the ridge to break up their advancing scouts.')
      print('Option (2): Hold your ground at the saloon doors and confront their leader head-on.')
      nxt = input('What is Your Next Action')
      if nxt == '1':
        print('\n',name,'fires a warning burst to blow up the rocky ledge above them')
        print('The reverberating explosion causes rocks to fall, causing the riders to flee from the spot.\n')
      elif nxt =='2':
        print('\n',name,'steps forward into the clearing with a steady gaze and a calm demeanor.')
        print('Outmaneuvered by his resolve, the gang leader backs down and rides away before sundown.\n')
   elif opt =='B':
        print('\n',name,'steps forward to the clearing with his eyes focused and a composed demeanor.')
        print('The steam engine runs out of control, leaving behind dark smoke on its way to a destroyed bridge.\n')
        print('Option (1): Jump onto the back freight car ladder and start climbing towards the emergency brake.')
        print('Option(2):Proceed to the manual switch on the side track to reroute the train safely.')
        act2 = input('What Your Next Act: ')
        if act2 == '1':
           print('\n',name,'jumps across and grasps the iron rung and opens the pressure release valve.')
           print('The sparks fly off the metal wheels as the motor slowly stops grinding to a halt.\n')
        elif act2 == '2':
           print('\n',name,'hits the track switch and flips the old rusty switch before the train comes.')
           print('The train veers off onto the sandy bypass track and comes to a halt.\n')
        else:
           print('Invaild choice , Try Again')


print('\nThank you For playing ')
print('Make sure to Rate it so i know whether it is soild or not.\n')

rate = int(input("Rate it out of 5: "))
if rate > 3:
   print('I will take it')
elif rate <= 3:
   print('I guess i will fine with that')


            
              
