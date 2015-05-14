from random import shuffle
from json import load, dump

def who_absent(absent):
    j = str(raw_input("Who isn't here: "))
    if j == "done" or j == "none":
        return absent
    else:
        absent.append(j)
        who_absent(absent)
        return absent

def check_master(partner, master):
   for p in partner:
        for i in master:
            if p == i:
                return True
   return False
        
def create_partners(present):
    x = [k for k, v in present.iteritems()]
    shuffle(x)
    
    first = [e for i, e in enumerate(x) if i % 2 == 0]
    second = [e for i, e in enumerate(x) if i % 2 != 0]
    
    if len(first) == len(second):
        partners = [[first[i], second[i]] for i in range(len(first))]
    else:
        partners = [[first[i], second[i]] for i in range(len(first)-1)]
        partners.append([first[-1], first[-1]])
        
    with open('partners_master.json', 'r') as f:
        pm = load(f)
    f.close()
    n = pm["n_groups"]
    
    if n > 9:
        p = []
        n = 0
    else:
        p = pm["partners_master"]
    
    check = check_master(partners, pm)
    
    if check == True:
        create_partners(attend)
    else:
        for i in partners:
            p.append(i)
        
        names = [[competitors[k[0]], competitors[k[1]]] for k in partners]
    
        for j in names:
            print j[0] + " and " + j[1]
        print n + 1

        o = {"partners_master": p, "n_groups": n + 1}
        with open('partners_master.json', 'w') as f:
            dump(o, f)
        
        return names
 
competitors = {1: "Ann Cardona", 2: "Brian St. John", 3: "Cassi LeVesque", 4: "Courtland McCoy",
      5: "Hannah Townsend", 6: "Jake Kuhnmuench", 7: "Jame Lloyd", 8: "Joaquin Ramirez",
      9: "Josh Hanlon", 10: "Josh Legget", 11: "Kris Thompson", 12: "Lindsey Yoshida", 
      13: "Mitch Gritts", 14: "PJ Ablang", 15: "Sharae Townsend", 16: "Zach Inman", 17: "Jake Wellock"}

def main():
	absent = []
	present = who_absent(absent)
	present = [k for name in present for k, v in competitors.iteritems() if name in v]
	attend = competitors
	if len(present) != 0:
		for i in present:
			attend.pop(i)
	create_partners(attend)

if __name__ == '__main__':
	main()