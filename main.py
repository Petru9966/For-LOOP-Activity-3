print("What level of brightness is required?")
level=int(input())
print("\nAdjusting brightness...\n")
for brightness in range(2,level+1,2):
  print("Beep's brightness level is :","*"* brightness)
  print("Bop's brightness level is:","*"*brightness)
print("Adjustment complete!")
