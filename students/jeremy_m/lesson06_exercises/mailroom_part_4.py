#!/usr/bin/env python3

# lesson 03 Exercise - String Formatting Lab
# Jeremy Monroe

import os
import pathlib
import time

donors = {'Charlize Theron': [134000],
          'Charlie Boorman': [15, 5],
          'James Franco': [25, 250, 2, 500],
          'Nike': [22000],
          'Count Chocula': [1257633, 2532790]
          }

# donor_totals = {}

user_input = ''

messages = {'start': ("What would you like to do?\n"
                      "1: to Send a Thank You\n"
                      "2: Create a Report\n"
                      "3 to create letters for all donors\n"
                      "quit: to Quit"
                      ),
            'thanks': ("Please input the donors name "),
            'thank_you_message': ("{:^42}\n"
                                  "{:^42}\n"
                                  "For your incredibly generous donation of:\n"
                                  "{:>19}{:<23,}\n\n"),
            'donor_letter': ("{:^41}\n"
                             "Thank you so much for your generous donation of:\n"
                             "{:>21}{:,}\n"
                             "We will always remember your money fondly."),
            'letters_confirmation': 'Is this ok?\nType y or n:'
            }


def letters_for_all():
    """ This function creates a directory in the cwd and fills that with an
        individual file (letter) for each donor.
    """

    clear_screen()
    print('Note: This operation will create a directory in the current working directory')
    if get_user_input(messages['letters_confirmation']).lower() == 'y':
        dir_path = os.getcwd() + '/letters'
        os.mkdir(dir_path)

        clear_screen()
        for donor in donors:
            donor_filename = '_'.join(donor.split(' ')) + '.txt'
            with open(dir_path + '/' + donor_filename, 'w+') as new_file:
                new_file.write(messages['donor_letter'].format(
                    donor, '$', int(donors[donor][-1])))
        else:
            print("Letters Created at:\n{}\n\n".format(dir_path))


def send_a_thank_you():
    """ Gives a user the option to list all donors, or else will create a new
        donor using the inputted name and adds their new donation using the
        inputted amount """
    clear_screen()

    # Ask user for the donors name
    donor_name_input = get_user_input(messages['thanks'])

    if donor_name_input == 'list':
        clear_screen()
        print("All donors:")
        for donor in donors:
            print(donor)

        donor_name_input = get_user_input('\n\n' + messages['thanks'])

    # Keep asking for donation_amount until user enters a number.
    while True:
        try:
            donation_amount = int(get_user_input(
                'How much did {} contribute?'.format(donor_name_input)))
            break
        except ValueError:
            print('Please enter a number.')

    add_donor(donor_name_input, donation_amount)

    clear_screen()
    # Print a formatted message with donors name and recent donation amount
    print(messages['thank_you_message'].format('Thank you so much',
                                               donor_name_input, '$', int(donors[donor_name_input][-1])))


def add_donor(donor_name_input, donation_amount):
    """ Adds a donor and their donation to the donors dict.
        Called in send_a_thank_you()
    """
    if donor_name_input in donors.keys():
        donors[donor_name_input].append(donation_amount)
    else:
        donors[donor_name_input] = [donation_amount]


def create_a_report():
    """ Prints a formatted report showing donor name, total donations, number of
        donations, and average donation amount. """
    clear_screen()

    donor_sums = sum_donors_donations()
    sorted_donor_sums = sort_by_values(donor_sums)

    print_report(sorted_donor_sums)


def sum_donors_donations():
    """ Returns a dict based off donors dict with the structure; key: sum(value)
    """
    donor_sums = {donor: sum(donations)
                  for donor, donations in donors.items()}

    return donor_sums


def sort_by_values(to_sort):
    """ Takes in a dict and returns that dict now sorted by its values. """
    sorted_by_values = sorted((value, key)
                              for (key, value) in to_sort.items())

    return sorted_by_values


def print_report(sorted_donor_totals):
    """ Prints a formatted report showing info for each donor in order from
        highest total donations to least.
    """
    # This prints the top of the table
    print("{:25} | {:12} | {:<19} | {:<16}".format(
        'Name', 'Total Given', 'Number of Donations', 'Average Donation'))
    print('-' * 81)

    for total_donor in sorted_donor_totals[::-1]:
        print('{:25} | ${:<11,} | {:^19} | ${:<16,}'.format(
            total_donor[1], total_donor[0], len(donors[total_donor[1]]), (total_donor[0] / len(donors[total_donor[1]]))))
    print('\n\n')


def get_user_input(msg):
    """ Gets a users input using msg as the prompt """
    return input(msg + '\n\n---->')


def clear_screen():
    """ Clears the terminal screen """
    os.system('cls') if os.name == 'nt' else os.system('clear')


main_menu_answers = {'1': send_a_thank_you,
                     '2': create_a_report, '3': letters_for_all}

if __name__ == "__main__":
    clear_screen()

    # Continue getting input until user types quit
    while user_input.lower() != 'quit':
        user_input = get_user_input(messages['start'])

        try:
            main_menu_answers.get(user_input, 'nothing')()
        except TypeError:
            clear_screen()
            continue
