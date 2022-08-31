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
                status = 1
             elif sc > bc:
                print("strike")
             elif sc < bc:
                print("ball")
             else:
                print("out")
                
                
player1 = input("player1의 숫자 입력" :).split()
player2 = input("player2의 숫자 입력" :).split()                    
                
player = [player1, player2]
count = 1
status = 0
print("게임 시작 : player1의 선공. player2의 숫자를 맞춰주세요")

main(player)
