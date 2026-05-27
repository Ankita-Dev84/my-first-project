student={'name':'Anky','age':22,'course':'Python'}
print(student['name'])
print(student['age'])
print(student['course'])
student['age']=23 #update the value of age
print(student)
student['address']='India' #add a new key-value pair to the dictionary
print(student)
del student['course'] #remove the key-value pair with key 'course'
print(student)
