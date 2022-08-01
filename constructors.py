# class animal:

#     def __init__(self):
#         print('yes, am really a constructor')

# dog = animal()


# constructor variables 
class animal:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print(f' this a {self.name} of {self.age} months living in a {self.address}')
        # print(self, )

sheep = animal('lamb', 2, 'bush')

        
