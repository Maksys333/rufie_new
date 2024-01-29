txt_res1 = "низька. Терміново зверніться до лікаря!"
txt_res2 = "задовільна. Зверніться до лікаря!"
txt_res3 = "середня. Можливо, варто додатково обстежитись у лікаря."
txt_res4 = "вище середнього"
txt_res5 = "висока"
class Experiment():
    
    def __init__(self, age, t1, t2, t3):
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.index = 0

def results(a):
        
        if a.exp.age < 7:
            a.index = 0
            return "Немає даних про такий вік"
 
        a.index = (4 * (int(a.exp.t1) + int(a.exp.t2) + int(a.exp.t3)) - 200) / 10
 
        if a.exp.age in {7, 8}:
            if a.index >= 21:
                return txt_res1
            elif 17 <= a.index < 21:
                return txt_res2
            elif 12 <= a.index < 17:
                return txt_res3
            elif 6.5 <= a.index < 12:
                return txt_res4
            else:
                return txt_res5
 
        elif a.exp.age in {9, 10}:
            if a.index >= 19.5:
                return txt_res1
            elif 15.5 <= a.index < 19.4:
                return txt_res2
            elif 10.5 <= a.index < 15.4:
                return txt_res3
            elif 5 <= a.index < 10.4:
                return txt_res4
            else:
                return txt_res5
       
        elif a.exp.age in {11, 12}:
            if a.index >= 18:
                return txt_res1
            elif 14 <= a.index < 17.9:
                return txt_res2
            elif 9 <= a.index < 13.9:
                return txt_res3
            elif 3.5 <= a.index < 8.9:
                return txt_res4
            else:
                return txt_res5
       
        elif a.exp.age in {13, 14}:
            if a.index >= 16.5:
                return txt_res1
            elif 12.5 <= a.index < 16.4:
                return txt_res2
            elif 7.5 <= a.index < 12.4:
                return txt_res3
            elif 2 <= a.index < 7.4:
                return txt_res4
            else:
                return txt_res5
           
        elif a.exp.age in {a.index > 15}:
            if a.index >= 15:
                return txt_res1
            elif 11 <= a.index < 14.9:
                return txt_res2
            elif 6 <= a.index < 10.9:
                return txt_res3
            elif 0.5 <= a.index < 5.9:
                return txt_res4
            else:
                return txt_res5