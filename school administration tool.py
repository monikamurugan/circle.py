#project : School administration tool

#importing csv

import csv

#Creating a function with imported csv


def write_into_csv(info_list):

  with open('student_info.csv','a',newline='')as csv_file:

     writer=csv.writer(csv_file)


#write the top row with the wanted details

     if csv_file.tell()==0:

       writer.writerow(["Name","Age","Contact number","E-mail ID"])

     writer.writerow(info_list)


if __name__== '__main__':

 condition=True

 student_num=1

#condition checking and entering information

 while(condition):

        student_info=input("Enter the details for student #{} in the following format(Name Age Contact_Number Email_ID):".format(student_num))

        student_info_list=student_info.split(' ')

        print("\nThe entered information is-\nName:{}\nAge:{}\nContact_number:{}\nE-mail ID:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check=input("Is the entered information correct?(yes/No):")


#If the entered information is correct

        if choice_check =="yes":

            write_into_csv(student_info_list)

            condition_check=input("Enter(yes/no)if you want to enter the information of another student:")


 #If want to enter more number of students information

            if condition_check=="yes":

                condition=True

                student_num=student_num+1


            elif condition_check=="no":

                condition=False


#If the entered information is wrong


        elif choice_check=="no":

            print("\n please reenter the values!")
