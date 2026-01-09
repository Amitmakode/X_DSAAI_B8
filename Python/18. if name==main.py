class person4:              

    name = "amit"
    surname = "kumar"
    yob = 1990

    def age(self , current_year ):
        return current_year - self.yob
    
    def age1(self , current_year ):
        return current_year - self.yob



class employee(person4):            
    name = "amit"
    surname = "singh"
    yob = 1991




if __name__ == "__main__":
    string_var = "hello!"
    list_var = [1,2,3,4,5]  
    print(string_var, list_var)