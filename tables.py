array  = [ ['ayo' , 'boy' , 12],
          [ 'vick', 'boy' , 14],
          ['favy', 'girl',  17],
        ];
print("name    sex    age");

for items in array:
    print( items[0]," "*(6-len(items[0])), items[1]," "*(6-len(items[1])), items[2]);
