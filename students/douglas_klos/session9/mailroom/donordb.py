#!/usr/bin/env python3
#pylint: disable=R1710
""" Mailroom OO DonorDB class """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# donordb.py

import os
import pickle
from donor import Donor


class DonorDB():
    """
    DonorDB class

    Properties:
        database:   Data structure containing donors
    """

    def __init__(self, donor=None):
        self._database = {}
        # self._database = []
        if donor:
            self._database[donor.name] = donor
            # self._database.append(donor)

    def __str__(self):
        return self.display_database()

    def __repr__(self):
        return self.display_database()

    def display_database(self):
        """ Displays the database """
        return_string = ''
        for key in self.database:
            return_string += f'{self.database[key].name:>24} : {self.database[key].donations}\n'
        return return_string

    def add_donor(self, donor):
        """
        Add a donor to the database

        :param donor: Donor to be added to database
        """
        if isinstance(donor, Donor):
            self.database[donor.name] = donor
        elif donor in self.database.keys():
            return f'{donor} already exists in database'
        else:
            self.database[donor] = Donor(donor)
        
        return f'{donor} has been added to the database'

    def add_donation(self, donor, donation):
        """ Add a donation to the database """

        try:
            float(donation)
        except ValueError:
            return f'{donation} is not a valid donation amount'

        if donation <= 0:
            return f'{donation} is not a valid donation amount'

        try:
            self.database[donor].add_donation(donation)
            return f'\nDonation {donation} has been added to donor {donor}'
        except KeyError:
            return f'{donor} not found in database'

    def remove_donor(self, donor):
        """
        Remove a donor from the database

        :param donor: Donor to be removed from database
        """
        try:
            del self.database[donor]
            return f'{donor} removed from database'
        except KeyError:
            return f'{donor} not found in database'
            
    def remove_donation(self, donor, donation):
        """
        Remove a donation from the database

        :param donor: Name of donor to remove donation from
        :param donation: Donation to be added to the database
        """

        try:
            return self.database[donor].remove_donation(donation)
        except KeyError:
            return f'\nDonation {donation} from donor {donor} not found in database'
    
    def display_report(self):
        """ Prints a report of donors and their donations """

        report = '\n' + "-" * 79 + '\n'
        report += 'Donor Name\t\t|           Total Given | Num Gifts |      Average Gift\n'
        report += "-" * 79 + '\n'

        for key in self.database:
            if self.database[key].donations == []:
                report += f'{self.database[key].name:24s}\t\t\t\t  0\n'
            else:
                report += (f'{self.database[key].name:24s}   '
                           f'$ {self.database[key].total_donations:18,.2f}  '
                           f'{len(self.database[key].donations):10}    '
                           f'$ {self.database[key].average_donation:14,.2f}\n')

        report += "-" * 79 + '\n'

        return report

    def thank_you_note(self, donor):
        """
        Returns a thank you note for the specified donor

        :param donor: Name of the donor to send the note to
        """
        try:
            return self.database[donor].display_thank_you_letter()
        except KeyError:
            return f'\nDonor {name} not found.'

    def thank_you_files(self, path):
        """
        Write thank you files to ./<path>/donor <date>.txt for each donor

        :param path: Path where files are to be written. Defaults to './thanks/
        """
        # Create directory and parents if they do not exist

        if path == '':
            path = './thanks/'
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except PermissionError:
            return f'Permission denied, {path} is not writeable'

        for key in self.database:
            # No donations from donor, no thank you note needed
            if self.database[key].donations == []:
                continue
            try:
                self.database[key].write_thank_you_letter(path)
            except PermissionError:
                return f'Permission denied, {path} is not writeable'

        return f'Thank you files written to {path}'

    def save_db_to_disk(self, filename='./mailroom_db.pkl'):
        """
        Save database to disk using pickle

        :param filename: Filename to be written to the disk
        """
        with open(filename, 'wb') as file:
            pickle.dump(self._database, file)
        return f'Database has been pickled to {filename}'

    def read_db_from_disk(self, filename='./mailroom_db.pkl'):
        """
        Load database from disk using pickle

        :param filename: Filename to be read from disk
        """
        try:
            with open(filename, 'rb') as file:
                self._database = pickle.load(file)
            return f'Database restored from pickle {filename}'
        except FileNotFoundError:
            raise FileNotFoundError

    def rename_donor(self, name, new_name):
        """
        Renames a donor

        :param name: Donor to be renamed
        :param new_name: New name for donor
        """

        try:
            self.database[new_name] = self.database[name]
            self.database[new_name].name = new_name
            del self.database[name]
        except KeyError:
            return f'{name} not found in database'


    @property
    def database(self):
        """ Gets the database """
        return self._database
