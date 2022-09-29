gradeScale = {
  "A" : 4.00,
  "A-" : 3.67,
  "B+" : 3.33,
  "B" : 3.00,
  "B-" : 2.67,
  "C+" : 2.33,
  "C" : 2.00,
  "C-" : 1.67,
  "D+" : 1.33,
  "D" : 1.00,
  "D-" : .67,
  "F" : .00
}
  

def gradeLetter():
  grade = int(input("Please enter your grade: "))
  match grade:
      case num if num in range (93, 101):
          return("A")
      case num if num in range (90, 93):
          return("A-")
      case num if num in range (87, 90):
          return("B+")
      case num if num in range (83, 87):
          return("B")
      case num if num in range (80, 83):
          return("B-")
      case num if num in range (77, 80):
          return("C+")
      case num if num in range (73, 77):
          return("C")
      case num if num in range (70, 73):
          return("C-")
      case num if num in range (67, 70):
          return("D+")
      case num if num in range (63, 67):
          return("D")
      case num if num in range (60, 63):
          return("D-")
      case num if num in range (0, 60):
          return("F")
      case invalid_grade:
          return(f"Invalid grade: {invalid_grade}")
  
    
def addToLst():
  lst = []
  for i in range(3):
    x =  gradeLetter()
    lst.append(x)
  print("This is the list: ", lst)
  return lst
            

def gradeSearch(lst):
  gradeList = []
  found = False
  keyList = gradeScale.keys()
  for element in lst:
    for key in keyList:
        if key == element:
            result = gradeScale.get(key)
            print("Grade was found in the dictionary: ", result)
            found = True
            gradeList.append(result)
  if found == False:
      print("Grade was not found in the dictionary")
  else:
      return(gradeList)
      

def gpaCalculator(lst):
  count = 0
  sum = 0
  for i in lst:
      sum += i
      count += 1
  gpa = sum / count
  return gpa
                            
            
def main():
    gradeLetterList = addToLst()
    gradeScaleList = gradeSearch(gradeLetterList)
    gpa = gpaCalculator(gradeScaleList)
    print("This is your gpa for the term: ", gpa)
    

if __name__ == "__main__":
    main()  