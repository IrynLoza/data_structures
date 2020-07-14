"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    filename = open(filename)

    houses = set() 
    for line in filename:
      line = line.rstrip()
      list_line = line.split('|')
      word = list_line[2]
      if word != '':
        houses.add(word)
      
      
    # TODO: replace this with your code

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    filename = open(filename)
    
    students = []

    for line in filename:
      line = line.rstrip()
      list_line = line.split('|')

      if cohort == "All" and list_line[2] != '':
        student = list_line[0] + " " + list_line[1]
        students.append(student)

      if cohort == list_line[4]: 
        student = list_line[0] + " " + list_line[1]
        students.append(student)  

    # TODO: replace this with your code

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts 
    - Instructors / I

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    filename = open(filename)
    
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    for line in filename:
      line = line.rstrip()
      list_line = line.split('|')

      
      if list_line[2] == "Dumbledore's Army" and list_line[2] != '':
        student = list_line[0] + " " + list_line[1]
        dumbledores_army.append(student)
        
      if list_line[2] == "Gryffindor" and list_line[2] != '':
        student = list_line[0] + " " + list_line[1]
        gryffindor.append(student) 

      if list_line[2] == "Hufflepuff" and list_line[2] != '':
        student = list_line[0] + " " + list_line[1]
        hufflepuff.append(student) 

      if list_line[2] == "Ravenclaw" and list_line[2] != '':
        student = list_line[0] + " " + list_line[1]
        ravenclaw.append(student) 

      if list_line[2] == "Slytherin" and list_line[2] != '':
        student = list_line[0] + " " + list_line[1]
        slytherin.append(student)

      if list_line[4] == "G":
        student = list_line[0] + " " + list_line[1]
        ghosts.append(student)

      if list_line[4] == "I":
        student = list_line[0] + " " + list_line[1]
        instructors.append(student)

    dumbledores_army = sorted(dumbledores_army)
    gryffindor = sorted(gryffindor)
    hufflepuff = sorted(hufflepuff)
    ravenclaw = sorted(ravenclaw)
    slytherin = sorted(slytherin)
    ghosts = sorted(ghosts)
    instructors = sorted(instructors)      

    # TODO: replace this with your code

    return [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    filename = open(filename)

    all_data = []

    for line in filename:
      line = line.rstrip()
      list_line = line.split('|')
      list_line[0] = list_line[0] + " " + list_line[1]
      list_line.remove(list_line[1])
      tuple_list = tuple(list_line)
      all_data.append(tuple_list)

    # TODO: replace this with your code

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    filename = open(filename)

    for line in filename:
      line = line.rstrip()
      list_line = line.split('|')
      list_line[0] = list_line[0] + " " + list_line[1]
      if name in list_line:
        return list_line[4]


    

    # TODO: replace this with your code


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    filename = open(filename)

    all_last_names = []
    duped_names = []

    for line in filename:
      line = line.rstrip()
      list_line = line.split('|')
      last_name = list_line[1]
      all_last_names.append(last_name)
    
    temp_names = []
    for name in all_last_names:
      if name in temp_names:
        duped_names.append(name)
      else:
        temp_names.append(name) 


    #common_names_set = set(common_names)  
    
  
    return set(duped_names)


    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
    filename = open(filename)
    for line in filename:
      line = line.rstrip()
      list_line = line.split('|')
      name = list_line[0]

    return []

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
