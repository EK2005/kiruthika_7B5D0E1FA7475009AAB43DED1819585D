class player:
  def play(self):
    print("The player is playing cricket")

class Batsman(player):
  def play(self):
    print("The Batsman is Batting")
  

class Bowler(player):
  def play(self):
    print("The Bowler is Bowling")

obj1=Batsman()
obj2=Bowler()
obj1.play()
obj2.play()