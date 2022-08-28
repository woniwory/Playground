def main(player):
    status = 0
    count = 0
    
    while status == 0:
        for p in player:
            print(count, "번째 턴입니다")
            assume = input()
            for i in range(3):
                sc = 0
                bc = 0
                
                if assume in p:
                    if assume[i] == p[i]:
                        sc += 1
                        print(sc)
                    else:
                        bc += 1
                        
             if sc == 3:
                print("correct")
                
