import sys
import pathlib

class Theater:

    def __init__(self, r, c):
        self.rows = r
        self.columns = c
        self.seating = [["e" for x in range(self.columns)] for y in range(self.rows)] 
        self.num_dict = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J"}
        self.reserved = {}

    # this method checks the seats for an consecutive number of empty seats that will fit the given amount of people
    def check_first_open(self, rev, num_people):
        # loops through all of the seats
        for i in range(len(self.seating)):
            for j in range(len(self.seating[i])):
                open = True
                seating_list = []
                # open is set to false if there is a seat that is not open given the number of people
                for k in range(num_people):
                    seating_list.append(self.num_dict[i] + str(j+k+1))
                    if j+k < self.columns:
                        if self.seating[i][j+k] == "f":
                            open = False
                            seating_list = []
                    else:
                        open = False
                        seating_list = []
                if open:
                    # if the seats are open, we want to set them to filled and also set the next three seats to filled
                    for k in range(num_people + 3):
                        if j+k < self.columns:
                            self.seating[i][j+k] = "f"
                    # we also want to set the seats above and below to filled
                    for k in range(num_people):
                        if i - 1 >= 0:
                            self.seating[i-1][j+k] = "f"
                        if i + 1 < self.rows:
                            self.seating[i+1][j+k] = "f"
                    self.reserved[rev] = seating_list
                    return 1
        return 0

    # this method finds the first open seats and allots it to the given number of people.
    def autofill(self, rev, num_people):
        seating_list = []
        ppl = num_people
        for i in range(len(self.seating)):
            for j in range(len(self.seating[i])):
                # checks to see if the given seat is avaliable 
                if self.seating[i][j] == "e":
                    ppl = ppl - 1
                    self.seating[i][j] = "f"
                    seating_list.append(self.num_dict[i] + str(j+1))
                    if i - 1 >= 0:
                        self.seating[i-1][j] = "f"
                    if i + 1 < self.rows:
                        self.seating[i+1][j] = "f"
                    if ppl <= 0: 
                        for k in range(3):
                            if j+k < self.columns:
                                self.seating[i][j+k] = "f"
                        return 1       
                    self.reserved[rev] = seating_list
                # if we are at the end, then that means all avaliable seats have filled up and we should tell the user
                if i == self.rows - 1 and j == self.columns - 1:
                    return 0

    def main(self):
        if len(sys.argv) != 2:
            print("Incorrect number of arguments for loading file")
        else:
            # gets the filepath from the command line
            filepath = sys.argv[1]
            with open(filepath) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            dic = {}
            # saves the reservation numbers and the number of people in a dictionary
            for res in content:
                new_res = res.split()
                dic[new_res[0]] = new_res[1]

            for d in dic:
                if self.check_first_open(d, int(dic[d])) == 0:
                    if self.autofill(d, int(dic[d])) == 0:
                        print("Unable to add anymore people into the theater")

            # writes the output to a file
            text_file = open("output3.txt", "w")
            for r in self.reserved:
                st = ""
                for k in range(len(self.reserved[r])):
                    if k != len(self.reserved[r]) - 1:
                        st = st + self.reserved[r][k] + ", "
                    else:
                        st = st + self.reserved[r][k]
                text_file.write(r + " " + st + "\n")
            text_file.close()
            print(str(pathlib.Path().absolute()) + "/output3.txt")

if __name__ == '__main__':
    thea = Theater(10, 20)
    thea.main()
