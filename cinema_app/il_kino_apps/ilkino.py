import random
from datetime import datetime
import argparse

class Seat:
    def __init__(self,seat_number):
        self.number = seat_number
        self.__availability = True
        self.__booked_by = None
        self.__symbol = seat_number

    def get_availability(self):
        return self.__availability
    
    def get_booked_by(self):
        return self.__booked_by
    
    def get_seat_symbol(self):
        return self.__symbol

    def set_booked_seat(self,name):
        avail = self.get_availability()
        if avail == True:
            self.__availability = False
            self.__booked_by = name

    def set_symbol(self, symbol):  
        if self.number < 10:
            self.__symbol = symbol
        else:
            self.__symbol = symbol + ' '


class Gift:
    def __init__(self):
        self.all_gifts = None

    def add_gifts(self,all_gift):
        self.__all_gifts = all_gift

    def get_one_random_gift(self):
        gift = random.choice(self.__all_gifts)
        self.__all_gifts.remove(gift)
        return gift

    def get_all_gift(self):
        return self.__all_gifts


class SpecialSeat(Seat):
    def __init__(self, seat_number):
        super().__init__(seat_number)
        self.gift = None
    
    def set_special_seat(self,gift):
        self.__gift = gift
    
    def get_gift(self):
        return self.__gift
    

class Ilkino:
    def __init__(self):
        self.__max_capacity = 36
        self.__all_seats = [_ for _ in range(1,self.__max_capacity+1)]
        self.__left_special_seats = []
        self.__right_special_seats = []
        self.__distributed_gifts = []
        self.__booking_hours = {}
        self.__report = []
    
    def add_left_special_seats(self,gift:Gift):
        count = 0
        while count != 5:
            special_seat_number = random.randrange(1,self.__max_capacity,2)
            if special_seat_number not in self.__left_special_seats:
                special_seat = SpecialSeat(special_seat_number)
                special_seat_gift = gift.get_one_random_gift()
                special_seat.set_special_seat(special_seat_gift)
                self.__all_seats[special_seat_number-1] = special_seat
                self.__left_special_seats.append(special_seat_number)
                count += 1

    def add_right_special_seats(self,gift:Gift):
        count = 0
        while count != 5:
            special_seat_number = random.randrange(2,self.__max_capacity,2)
            if special_seat_number not in self.__right_special_seats:
                special_seat = SpecialSeat(special_seat_number)
                special_seat_gift = gift.get_one_random_gift()
                special_seat.set_special_seat(special_seat_gift)
                self.__all_seats[special_seat_number-1] = special_seat
                self.__right_special_seats.append(special_seat_number)
                count += 1

    def add_left_normal_seats(self):
        for i in range(1,self.__max_capacity+1,2):
            if isinstance(self.__all_seats[i-1],SpecialSeat) is False:
                seat = Seat(i)
                self.__all_seats[i-1] = seat

    def add_right_normal_seats(self):
        for i in range(2,self.__max_capacity+1,2):
            if isinstance(self.__all_seats[i-1],SpecialSeat) is False:
                seat = Seat(i)
                self.__all_seats[i-1] = seat

    def set_up(self,left_gift:Gift,right_gift:Gift):
        self.add_left_special_seats(left_gift)
        self.add_right_special_seats(right_gift)
        self.add_left_normal_seats()
        self.add_right_normal_seats()

    def set_report(self,time,num_of_seats):
        if len(self.__report) == 0:
            self.__report.append((time,num_of_seats))
        else:
            for i in range(len(self.__report)):
                if time == self.__report[i][0]:
                    self.__report[i][0] += num_of_seats
        if len(self.__report) != 0:
            self.__report.append((time,num_of_seats))

    def set_distributed_gift(self,num,gift):
        self.__distributed_gifts.append((num,gift))

    def set_booking_hours(self, booking_hour, num_of_seats):
        if booking_hour in self.__booking_hours:
            self.__booking_hours[booking_hour] += num_of_seats
        else:
            self.__booking_hours[booking_hour] = num_of_seats

    def get_booked_by_hour(self):
        return self.__booking_hours

    def get_left_special_seats(self):
        return self.__left_special_seats

    def get_right_special_seats(self):
        return self.__right_special_seats
    
    def get_all_seats(self):
        return self.__all_seats
    
    def get_all_distributed_gifts(self):
        return self.__distributed_gifts

    def gui(self):
        all_seats = self.get_all_seats()
        for i in range(0,self.__max_capacity,6):
            print("+-----------------+      +-----------------+")
            if i == 0:
                print(f"|  {all_seats[0].get_seat_symbol()}  |  {all_seats[2].get_seat_symbol()}  |  {all_seats[4].get_seat_symbol()}  |      |  {all_seats[1].get_seat_symbol()}  |  {all_seats[3].get_seat_symbol()}  |  {all_seats[5].get_seat_symbol()}  |")
            elif i == 6:
                print(f"|  {all_seats[6].get_seat_symbol()}  |  {all_seats[8].get_seat_symbol()}  |  {all_seats[10].get_seat_symbol()} |      |  {all_seats[7].get_seat_symbol()}  |  {all_seats[9].get_seat_symbol()} |  {all_seats[11].get_seat_symbol()} |")
            else:
                print(f"|  {all_seats[i].get_seat_symbol()} |  {all_seats[i+2].get_seat_symbol()} |  {all_seats[i+4].get_seat_symbol()} |      |  {all_seats[i+1].get_seat_symbol()} |  {all_seats[i+3].get_seat_symbol()} |  {all_seats[i+5].get_seat_symbol()} |")
        print("+-----------------+      +-----------------+")

class Kiosk:
    def run(self, ilkino):
        while True:
            self.display_menu(ilkino)
            choice = input("Enter your choice: ")

            if choice == "1":
                self.book(ilkino)
            elif choice == "2":
                self.search(ilkino)
            elif choice == "3":
                self.kiosk_report(ilkino)
            elif choice == "4":
                print("Closing program...")
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press 'Enter' to continue.")
                print("|" + "-" * 60 + "|")
                print()

    def display_menu(self, ilkino):
        print("+------------------------------------------+")
        print("|                 IL Kino                  |")
        print("|             Nansenstrasse 22,            |")
        print("|               12047 Berlin               |")
        print("+------------------------------------------+")

        print()
        print("+------------------------------------------+")
        print("|                  SCREEN                  |")
        print("+------------------------------------------+")
        print()

        ilkino.gui()  # Display seat availability

        print()
        print("1. Seat Booking")
        print("2. Find by Name")
        print("3. Report")
        print("4. Exit")
        print()

    def report(self, ilkino: Ilkino):
        print("+----------------------------------------------+")
        print("|        Hour             Number of Bookings   |")
        print("+----------------------------------------------+")

        booking_hours = ilkino.get_booked_by_hour()  # Retrieve the booking hours dictionary

        for hour, num_of_bookings in booking_hours.items():
            # Format the output using f-strings
            if num_of_bookings < 10:
                print(
                    f"|        {hour}                    {num_of_bookings}            |"
                )
            else:
                print(
                    f"|        {hour}                    {num_of_bookings}           |"
                )

        print("+" + "-" * 46 + "+")
        print("| All distributed SeatNumber-Gift:" + " " * 13 + "|")

        distributed_gifts = ilkino.get_all_distributed_gifts()  # Retrieve the distributed gifts list

        if not distributed_gifts:
            print("| None." + " " * 40 + "|")
        else:
            for seat_num, gift in distributed_gifts:
                gift_description = gift 
                if seat_num<10:
                    print(
                        f"| {seat_num:2d} - {gift_description}"
                        + " " * (46 - (len(str(seat_num)) + len(gift_description))-5)
                        + "|"
                    )
                else:
                    print(
                        f"| {seat_num} - {gift_description}"
                        + " " * (46 - (len(str(seat_num)) + len(gift_description) + 4))
                        + "|"
                    )
        print("+----------------------------------------------+")
        print()


    def book(self, ilkino: Ilkino):
        name = input("Enter your name: ")
        seat_numbers = input("Enter seat numbers (space-separated): ").split()
        all_seats = ilkino.get_all_seats()
        string_seats = ''
        chosen_seats = []
        special = 0

        current_time = str(datetime.now().time().strftime('%H')) + ':00'

        for num in seat_numbers:
            num = int(num)
            if num < 1 or num > 36:
                print('Invalid number of seats\n Plese try again.')
                input("Press 'Enter' to continue.")
                print("|" + "-" * 60 + "|")
                print()
                return 
            if isinstance(all_seats[num - 1], SpecialSeat) and all_seats[num - 1].get_availability():
                chosen_seats.append(num)
            elif isinstance(all_seats[num - 1], Seat) and all_seats[num - 1].get_availability():
                chosen_seats.append(num)
            else:
                print(f"Seats {num} have been booked.")

        if len(chosen_seats) == len(seat_numbers):
            for num in seat_numbers:
                num = int(num)
                if isinstance(all_seats[num - 1], SpecialSeat):
                    seat_gift = all_seats[num - 1].get_gift()  
                    ilkino.set_distributed_gift(num, seat_gift)
                    all_seats[num - 1].set_booked_seat(name)
                    all_seats[num-1].set_symbol('G')
                    special +=1
                else: 
                    all_seats[num - 1].set_booked_seat(name)
                    all_seats[num - 1].set_symbol('X')
                # Update booking hours
                ilkino.set_booking_hours(current_time, 1)

        for i in range(len(seat_numbers)):
            if i == len(seat_numbers) - 1:
                string_seats += str(seat_numbers[i])
            else:
                string_seats += str(seat_numbers[i]) + ', '

        if len(chosen_seats) == len(seat_numbers) and special != 0:
            receipt = open(f"{name}_" + "_".join(map(str, string_seats)) + ".txt", "w")
            receipt.write('+' + '-' * 60 + '+\n')
            receipt.write('|' + 'IL Kino Receipt'.center(60) + '|\n')
            receipt.write('+' + '-' * 60 + '+\n')
            receipt.write('|' + ' Name                    :   ' + \
            f'{name}'.ljust(31) + '|\n')
            receipt.write('|' + ' Seat Number             :   ' + \
            f'{string_seats}'.ljust(31) + '|\n')
            receipt.write('+' + '-' * 60 + '+\n')
            receipt.write('|' + \
            'Please check below your seat to get your gift.'.center(60) + '|\n')
            receipt.write('|' + \
            'Please arrive 15 minutes before.'.center(60) + '|\n')
            receipt.write('+' + '-' * 60 + '+\n')
            receipt.close()
        elif len(chosen_seats) == len(seat_numbers) and special == 0:
            receipt = open(f"{name}_" + "_".join(map(str, string_seats)) + ".txt", "w")
            receipt.write('+' + '-' * 60 + '+\n')
            receipt.write('|' + 'IL Kino Receipt'.center(60) + '|\n')
            receipt.write('+' + '-' * 60 + '+\n')
            receipt.write('|' + ' Name                    :   ' + \
            f'{name}'.ljust(31) + '|\n')
            receipt.write('|' + ' Seat Number             :   ' + \
            f'{string_seats}'.ljust(31) + '|\n')
            receipt.write('+' + '-' * 60 + '+\n')
            receipt.write('|' + \
            'Please arrive 15 minutes before.'.center(60) + '|\n')
            receipt.write('+' + '-' * 60 + '+\n')
            receipt.close()

        input("Press 'Enter' to continue.")
        print("|" + "-" * 60 + "|")
        print()


    def search(self, ilkino:Ilkino):
        name = input("Enter the name to find bookings: ")
        booked_seats = []
        string_seats = ''
        for seat in ilkino.get_all_seats():
            if seat.get_booked_by() == name:
                booked_seats.append(seat.number)
        
        if len(booked_seats) != 0:                   
            for i in range(len(booked_seats)):
                if i == len(booked_seats)-1:
                    string_seats += str(booked_seats[i]) 
                else: 
                    string_seats += str(booked_seats[i]) + ', '
            print(f"Seats {string_seats} are booked by {name}.")
        else:
            print(f"No bookings found for {name}.")

        input("Press 'Enter' to continue.")
        print("|" + "-" * 60 + "|")
        print()

    def kiosk_report(self, ilkino):
        self.report(ilkino)
        input("Press 'Enter' to continue.")
        print("|" + "-" * 60 + "|")
        print()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gift')
    args = parser.parse_args()
    gift_list= args.gift.split(',')

    left = Gift()
    right = Gift()
    left.add_gifts(gift_list)
    right.add_gifts(gift_list)

    ilkino = Ilkino()
    ilkino.set_up(left, right)

    kiosk = Kiosk()
    kiosk.run(ilkino)


if __name__ == '__main__':
    main()