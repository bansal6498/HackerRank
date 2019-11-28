def merge_the_tools(string, k):
    def Remove_the_common_elements(lst_aftr_devision): #function for removing common elements from list
        final_list = [] 
        for num in lst_aftr_devision: 
            if num not in final_list: 
                final_list.append(num) 
        return final_list
    for i in range(0,int(len(string)/k)):
        lst_aftr_devision = string[i*k:k*i+k]
        print(*Remove_the_common_elements(lst_aftr_devision),sep='')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)