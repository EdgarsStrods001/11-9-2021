#klases nosaukums
class Robots:
  """klases reprezents robota ar specifisko vardu"""

  #klases konstruktors inicilizacijas.
   def_init_(self, vards) :
    """Datu inicializacija"""

    #ipashibas defineshana
    self.vards=vards
   
   print(f"Incializejam {self.vards}")

   def sasveicinaties(self):
   print(f"sveiks! mani sauc {self.vards}")



   rob1 = robots("R")

   rob1.sasveicinaties()

