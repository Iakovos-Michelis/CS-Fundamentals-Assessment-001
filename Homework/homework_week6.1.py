def generate_usernames(students):
    usernames = []  
    counts = {} 

    for student in students:
       
        first, last = student.split()
        username = first[0].lower() + last.lower()
        
       
        if username in counts:
            counts[username] = counts[username] + 1
            unique_username = username + str(counts[username])
        else:
            counts[username] = 0
            unique_username = username
        
        usernames.append(unique_username) 
    
    return usernames

students = ['Isiah Caanan', 'Moses Wright', 'Thomas Walkup', 'Mike James', 'Evan Fournier', 'Draymond Green']
print(generate_usernames(students))