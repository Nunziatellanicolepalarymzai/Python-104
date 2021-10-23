#descriptive data-->is the data which gives us some information
#central tendency->is a value that identifies the central position within the given data

#statistics->means collection of data
#descriptive statistics--> mean,median ,mode etc..which describes something about the data

#mean(average)=sum of values/the number of values

#median means ,situated in the middle 
# if there are two middle numbers ,find their mean.that's the median

#mode is used to find the most occuring value of a data set



#python has a collection module ,which has a counter method,which is basically a container 
#that keeps track of how many times the same values are added or repeated

from collections import Counter
new_data="whitehatjr"
data=Counter(new_data)
print(data)

#out put
#Counter({'h': 2, 't': 2, 'w': 1, 'i': 1, 'e': 1, 'a': 1, 'j': 1, 'r': 1})

new_list=data.items()
print(new_list)
#output
#dict_items([('w', 1), ('h', 2), ('i', 1), ('t', 2), ('e', 1), ('a', 1), ('j', 1), ('r', 1)])


#dictionary.items() method is used to return the list with all the dictionary keys with values.



value=data.values()
print(value)
#output
#dict_values([1, 2, 1, 2, 1, 1, 1, 1])

#dictionary_values() returns the list of all the values in the dictionary.
