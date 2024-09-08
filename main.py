import pickle
from player import Player
from session import Session
from fight import clearTerm

print('''                                                                            
        *****    **                                                        
    ******  *  **** *                                     *               
    **   *  *   *****                                     ***              
    *    *  *    * *                                        *               
        *  *     *                ***  ****       ****                      
    ** **     *         ***     **** **** *   * ***  * ***        ****   
    ** **     *        * ***     **   ****   *   ****   ***      * ***  *
    ** ********       *   ***    **         **    **     **     *   **** 
    ** **     *      **    ***   **         **    **     **    **        
    ** **     **     ********    **         **    **     **    **        
    *  **     **     *******     **         **    **     **    **        
        *       **    **          **         **    **     **    **        
    ****        **    ****    *   ***         ******      **    ***     * 
    *  *****      **    *******     ***         ****       *** *  *******  
    *     **              *****                              ***    *****   
    *                                                                       
    **                                                                     
                                                                            
                                                                                                                                               
''')

def opening():
    print("START\nLOAD")
    i = input("S or L?\n> ")

    clearTerm()
    match i.capitalize():
        case "S":
            ses = Session(Player(150, 200))
            ses.run()
        case "L":
            p = pickle.load(open("saves/player", "rb"))
            ses = Session(p)
            ses.run()
        case _:
            return opening()

opening()


