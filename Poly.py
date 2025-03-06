class Polynomial:
    def __init__(self):
        self.capacity = 0
        self.degCoeff = [0]*1  #Name of your array (Don't change this)


    def __call__(self, polynomial):
        self.degCoeff = polynomial.degCoeff
        self.capacity = polynomial.capacity


    # Complete the class
    def setCoefficient(self, degree, coff):
        if self.capacity <= degree:
            size = degree + 1
            new_degCoeff = [0] * size


            for i in range(self.capacity):
                new_degCoeff[i] = self.degCoeff[i]


            self.capacity = size
            self.degCoeff = new_degCoeff
        self.degCoeff[degree] += coff


    def __str__(self):
        output = ''
        for j in range(len(self.degCoeff)):
            if self.degCoeff[j] != 0:
                ad = '{}x{} '.format(self.degCoeff[j], j)
                output += ad
        return output


    def print(self):
        print(self)


    def __add__(self, other):
        i, j = 0, 0
        newPloy = Polynomial()
        while (i < self.capacity) and (j < other.capacity):
            deg = i
            coef = self.degCoeff[i] + other.degCoeff[j]
            newPloy.setCoefficient(deg, coef)
            i, j = i+1, j+1
        while i<self.capacity:
            newPloy.setCoefficient(i, self.degCoeff[i])
            i += 1
        while j < other.capacity:
            newPloy.setCoefficient(j, other.degCoeff[j])
            j += 1
        self.degCoeff = newPloy.degCoeff
        self.capacity = self.capacity + other.capacity
        return self


    def __sub__(self, other):
        i, j = 0, 0
        newPloy = Polynomial()
        while (i < self.capacity) and (j < other.capacity):
            deg = i
            coef = self.degCoeff[i] - other.degCoeff[j]
            newPloy.setCoefficient(deg, coef)
            i, j = i + 1, j + 1
        while i < self.capacity:
            newPloy.setCoefficient(i, self.degCoeff[i])
            i += 1
        while j < other.capacity:
            newPloy.setCoefficient(j, -other.degCoeff[j])
            j += 1
        self.degCoeff = newPloy.degCoeff
        self.capacity = self.capacity + other.capacity
        return self


    def getCoefficent(self,  degree):
        if degree >= self.capacity:
            return 0
        return self.degCoeff[degree]


    def __mul__(self, other):
        newPloy = Polynomial()
        for i in range(self.capacity):
            for j in range(other.capacity):
                deg = i+j
                coef = self.degCoeff[i] * other.degCoeff[j]
                newPloy.setCoefficient(deg, coef)

        self.degCoeff = newPloy.degCoeff
        self.capacity = newPloy.capacity
        return self


# ---------Derived Code-----------
def run():
    count1 = int(input())
    degree1 = list(map(int,input().split()))
    coeff1 = list(map(int,input().split()))

    first = Polynomial()
    for i in range(count1):
        first.setCoefficient(degree1[i], coeff1[i])

    count2 = int(input())
    degree2 = list(map(int,input().split()))
    coeff2 = list(map(int,input().split()))

    second = Polynomial()
    for i in range(count2) :
        second.setCoefficient(degree2[i], coeff2[i])

    choice = int(input())

    result = Polynomial()
    # Add 
    if choice == 1:
        result = first + second
        result.print()
    # Subtract
    elif choice == 2:
        result = first - second
        result.print()
    # Multiply
    elif choice == 3:
        result = first * second
        result.print()

    elif choice == 4: # Copy constructor
        third = deepcopy(first)
        if (third.degCoeff == first.degCoeff) :
            print("true")
        else :
            print("false")


    else: # Copy assignment operator
        fourth = deepcopy(first)
        if (fourth.degCoeff == first.degCoeff) :
            print("true")
        else :
            print("false")


run()
