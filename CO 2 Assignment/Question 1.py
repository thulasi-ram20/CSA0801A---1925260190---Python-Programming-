households = [    (100, False, False), (101, True, False),  
              (200, True, False), (201, False, True),   
              (99, True, False), (150, False, False),   
              (250, True, False), (250, False, True) ] 
print("IF-ELIF-ELSE RESULTS")
for units, ration, senior in households: 
  if units <= 100:     
    result = "Full subsidy"  
  elif 101 <= units <= 200 and 
  ration:       
    result = "Partial subsidy"  
  elif units > 200 and senior:
    result = "Special senior consideration" 
  else:
    result = "No subsidy"
    print(units, ration, senior, ":", result)
    print("\nIndependent IF example (may print more than one result)") 
    units, ration, senior = 100, True, True
    if units <= 100: 
      print("Full subsidy") 
      if 101 <= units <= 200 and ration:
        print("Partial subsidy") 
        if units > 200 and senior: 
          print("Special senior consideration")
