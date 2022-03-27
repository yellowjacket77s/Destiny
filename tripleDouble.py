#Python Function To Keep Track Of Triple Tap + Fourth Times The Charm
def tripleDouble(num):
  #Counter to keep track of tripple tap
  countT = 0
  #Counter to keep track of Fourth Times The Charm
  countF = 0
  #Counter to keep track of the total amount of bullets
  bullet = 0
  #A loop for when your 'gun' still has bullets in the mag
  while num > 0:
    #Increases bullet shot count
    countT = countT + 1
    countF = countF + 1
    num = num - 1
    bullet = bullet + 1
    #Reset triple tap once it procs
    if countT == 3:
        countT = 0
        num = num + 1
    #Reset fourth times the charm once it procs
    if countF == 4:
        countF = 0
        num = num + 2
  #Display the total amount of bullets fired
  print ('Bullet Count: ', bullet)
