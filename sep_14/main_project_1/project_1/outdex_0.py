# this is imported from git hub sep 14 2020

import os
import csv

class smart_ass_machine:
    def __init__(self):
        self.file_containing_all_eva_and_evo = 'all_eva_and_evos.csv'
        self.file_that_contains_array_that_contains_all_eva_and_evo_fieldnames = ['this', 'are', 'all', 'evos', 'and',
                                                                             'evas', 'found']
        self.array_that_contains_all_eva_and_evos = []

        self.file_containing_all_SubFlow = 'all_SubFlows.csv'
        self.file_containing_all_VALID_SubFLow = 'all_VALID_SubFlow.csv'

        self.SubFlow_header = ['file name', 'line', 'index']
        self.array_that_contains_SubFlow = []

        self.starting_keyword = 'SubFlow'
        self.tempo_SubFlow_files = 'tempo_SubFlow_files.txt'

        self.tempo_csv_file = 'tempo_csv_file.csv'
        self.tempo_txt_file = 'tempo_txt_file.txt'

    def return_this_column(self, column, input_array, delimiter = ',', enable_debug = False):
        ''' given an input_array that contains another array of format [<value_1>, <value_2>,...<value_n>], return the specified column
            if not, process the array first using self.transform_this_array_to_format_for_csv_writing'''
        input_array = input_array
        enable_debug = enable_debug
        column = column
        delimiter = delimiter

        tempo_array = []
        tempo_tempo_array = []
        desired_column = ''

        for entry in input_array:
            tempo_array = entry[0].split(delimiter)
            desired_column = tempo_array[column]
            tempo_tempo_array.append(desired_column)
            if enable_debug: print(desired_column)

        return tempo_tempo_array

    def transform_this_array_to_format_for_csv_writing(self, input_array, enable_debug = False):
        ''' if entries of arrays are not arrays themselves, it will not format correctly when written to csv '''
        enable_debug = enable_debug
        input_array = input_array

        tempo_array_array = []

        for entry in input_array:
            tempo_array_array.append([entry])

        return tempo_array_array

    def write_to_file(self, input_array, output_file = 'tempo_file.txt', enable_debug=False):
        ''' write array to .txt format '''
        with open(output_file, 'w') as my_file_0:
            for entry in input_array:
                my_file_0.write(entry)

    def write_to_file_as_csv(self, input_array: object, output_file: object, fieldnames: object = None, enable_debug: object = False) -> object:
        ''' given an array, write to file. be careful when using as an embeded function. if the target_folder
                for the main function is an entry, only the result from the last entry will be written by this function'''
        array_to_write = input_array
        output_file = output_file
        fieldnames = fieldnames
        enable_debug = enable_debug

        try:
            with open(output_file, 'w', newline='') as my_file_0:
                csv_writer = csv.writer(my_file_0)
                if fieldnames is not None: csv_writer.writerow(fieldnames)
                for entry in array_to_write:
                    if enable_debug: print(entry)
                    csv_writer.writerow(entry)
            return True
        except:
            raise Exception
        ##--------------------------------------------------------------------

    def find_all_eva_and_evo(self, target_folder, enable_debug = False, write_to_file_as_csv = False, output_file = ''):
        ''' walks through the given directory and returns files that are .eva and .evo '''
        if write_to_file_as_csv: output_file = output_file

        target_folder = target_folder
        enable_debug = enable_debug
        write_to_file_as_csv = write_to_file_as_csv

        tempo_array = []
        tempo_array_array = []

        for dirs, dirs_within_dirs, all_files in os.walk(target_folder):
            for entry in all_files:
                if '.evo' in entry or '.eva' in entry:
                    tempo_string = '/'.join((dirs, entry))
                    tempo_array.append(tempo_string)
                    if enable_debug: print(tempo_string)
                    if write_to_file_as_csv: tempo_array_array.append([tempo_string])
                else:
                    pass

        if write_to_file_as_csv: self.write_to_file_as_csv(tempo_array_array, output_file, None, False)

        return tempo_array
        ##---------------------------------------------------------------------------
    def search_this_keyword(self, keyword, target_file, enable_debug = False, write_to_file_as_csv = False, output_file = ''):
        ''' given a path, extract all subflows startstate and nodes '''
        if write_to_file_as_csv: output_file = output_file

        target_file = target_file
        enable_debug = enable_debug
        keyword = keyword

        idx = 1
        tempo_array = []
        array_to_write = []
        line_as_array = []

        with open(target_file, 'r', newline= '') as my_file_0:
            for line in my_file_0:
                if keyword in line:
                    line_as_array = [target_file,line.rstrip(),str(idx)]
                    tempo_array.append(line_as_array)
                    if enable_debug: print(line_as_array)
                    idx += 1
                else:
                    idx += 1

        if write_to_file_as_csv: self.write_to_file_as_csv(tempo_array, output_file, None, False)

        return tempo_array

    def array_filter_by_string(self, input_array, filter_string, location_of_filter_string = None, split_string = ' ', enable_debug = False):
        ''' given a normal array, filter by string  '''
        tempo_array = []
        split_string = split_string
        tempo_string = ''

        if location_of_filter_string is None:
            for entry in input_array:
                if filter_string in entry:
                    if enable_debug: print(entry)
                    tempo_array.append(entry)
                else:
                    pass ## discard that entry
            return tempo_array
        else: ## location has value
            for entry in input_array:
                if filter_string in entry:
                    tempo_tempo_array = entry.split(split_string)
                    tempo_string = tempo_tempo_array[location_of_filter_string]
                    tempo_array.append(tempo_string)
                    if enable_debug: print(tempo_string)
                else:
                    pass ## discard
            return tempo_array

    def process_string_by_type(self, type, input_string, keyword=None, column=None, enable_debug=False):
        ''' general processes for strings. input is string output is string
                A for split string then get column'''
        input_string = input_string
        keyword = keyword
        column = column

        tempo_string = ''
        tempo_array = []

        if type == 'A':
            tempo_array = input_string.split(' ')
            tempo_string = tempo_array[column]
            if enable_debug: print(tempo_string)
            return tempo_string

    def csv_array_filter_by_string_type_A(self, input_csv_array, string_location_on_the_csv_array_entry, column, filter_string, enable_debug = False, write_to_file_as_csv = False, output_file = ''):
        ''' filter each entry of input_csv_array by  '''
        input_csv_array = input_csv_array
        column = column
        filter_string = filter_string
        enable_debug = enable_debug
        string_location_on_the_csv_array_entry = string_location_on_the_csv_array_entry

        tempo_string = ''
        tempo_csv_array = []

        for entry in input_csv_array:
            tempo_string = entry[string_location_on_the_csv_array_entry]
            tempo_string = self.process_string_by_type('A', tempo_string, keyword=None, column=column, enable_debug=False) # get the column that contains 'SubFlow'
            if tempo_string == filter_string: # if the returned string indeed contains 'SubFlow', then
                tempo_csv_array.append(entry) # transfer the csv_array entry to new container
                if enable_debug: print(entry)
            else:
                pass # reject the entry. does not pass the requirement
        return tempo_csv_array

    def extract_section_give_start_string_and_end_string_type_idx(self, file_object, start_index, end_string, enable_debug):
        ''' '''
        my_file_0 = file_object

        trap = 0
        index = 1
        tempo_array = []

        for line in my_file_0:
            if trap == 0:
                if index == start_index:
                    if enable_debug: print(line)
                    tempo_array.append(line)
                    trap = 1  # flip the switch
                    index += 1
                    pass  # write the codes until the end keyword is reached
                else:  # target_index not yet found
                    index += 1
            else:  # target index was reached
                if end_string in line:
                    if enable_debug: print(line)
                    tempo_array.append(line)
                    break
                else:
                    if enable_debug: print(line)
                    tempo_array.append(line)
        return tempo_array

    def extract_section(self,search_type, target_file, start_index_or_string, last_string, enable_debug=False, write_to_file=False, output_file = ''):
        ''' type: 'str': read through the target file, start recording upon encountering the start string. end recording when last string is reached
                if type: 'idx', read through the target file, start recording upon encountering the idx, end recoring when last string is reached'''

        with open(target_file, 'r', newline='') as my_file_0:
            if search_type == 'str':
                return None
            elif search_type == 'idx':
                file_object = my_file_0
                start_index = int(start_index_or_string)
                last_string = last_string
                enable_debug = enable_debug
                write_to_file = write_to_file
                tempo_array = self.extract_section_give_start_string_and_end_string_type_idx(file_object, start_index, last_string, enable_debug)
                if write_to_file: self.write_to_file(tempo_array, output_file, False)
                return tempo_array
            else:
                return None

    def lines_to_list_by_keyword(self, keyword, input_array, enable_debug = False):
        ''' given an array represenation of a text file '''
        keyword_0 = keyword
        trap = 0

        array_0 = []
        array_1 = []
        for entry in input_array:
            if trap == 0:
                if keyword_0 in entry:
                    if enable_debug: print(entry)
                    array_0.append(entry)
                    trap = 1
                else:
                    pass
            else:
                if keyword_0 in entry:
                    array_1.append(array_0)
                    array_0 = []  # clear. do not use array.clear()
                    if enable_debug: print(entry)
                    array_0.append(entry)
                else:
                    if enable_debug: print(entry)
                    array_0.append(entry)
        array_1.append(array_0)

        return array_1

    def give_StartState_modify_tempo_entry(self, input_array, tempo_entry, enable_debug = False):
        ''' '''
        # extract the StartState value
        keyword = 'StartState ='
        tempo_array = input_array
        for entry in tempo_array:
            if keyword in entry:
                entry = entry.strip()
                tempo_string = self.process_string_by_type('A', entry, column=2)
                tempo_string = tempo_string.replace(';', '')
                pass  # print(tempo_string)
        # add the StartState to tempo_entry
        tempo_entry = tempo_entry + ['StartState', tempo_string]
        if enable_debug: print(tempo_entry)
        return tempo_entry

    def give_index_of_keyword(self, input_array, keyword, enable_debug = False):
        ''' '''
        tempo_entry = input_array
        keyword = keyword
        idx = 0
        tempo_array = []
        for entry in tempo_entry:
            if keyword in entry:
                if enable_debug: print(idx)
                tempo_array.append(idx)
            else:
                idx += 1
        return tempo_array
