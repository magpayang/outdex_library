import outdex_0

procs = outdex_0.smart_ass_machine()

# catalogue all .eva and .evo
target_folder = '.'
output_file = procs.file_containing_all_eva_and_evo
array_of_files_that_contains_eva_and_evo = procs.find_all_eva_and_evo(target_folder, False, False, output_file)

# find 'SubFlows'
keyword = 'SubFlow'
tempo_csv_array = []
output_file = procs.file_containing_all_SubFlow
for entry in array_of_files_that_contains_eva_and_evo:
    target_folder = entry
    # append if adding individual entries, + if adding another array
    tempo_csv_array = tempo_csv_array + procs.search_this_keyword(keyword, target_folder, False, False, output_file)

# write to file
output_file = procs.file_containing_all_SubFlow
pseudo_fieldnames = procs.SubFlow_header
procs.write_to_file_as_csv(tempo_csv_array, output_file, fieldnames=pseudo_fieldnames, enable_debug=False)

# filter valid SubFlows
string_location_on_the_csv_array_entry = 1
column = 0
filter_string = 'SubFlow'
tempo_csv_array = procs.csv_array_filter_by_string_type_A(tempo_csv_array,
                                                          string_location_on_the_csv_array_entry,
                                                          column,
                                                          filter_string,
                                                          False,
                                                          False)

procs.write_to_file_as_csv(tempo_csv_array,
                           procs.file_containing_all_VALID_SubFLow,
                           fieldnames=None,
                           enable_debug=False)

tempo_entry = ['./MAX9293D_QUAD_P6.eva', 'SubFlow OnStart_Nominal {', '132']

target_file = tempo_entry[0]
target_string = tempo_entry[1]
target_index = int(tempo_entry[2])
end_keyword = 'StartState'
tempo_array = procs.extract_section('idx',
                                    target_file,
                                    target_index,
                                    end_keyword,
                                    False,
                                    False,
                                    output_file='all of SubFlow OnStart_Nominal.txt')
# # add StartState to tempo_entry
tempo_entry = procs.give_StartState_modify_tempo_entry(tempo_array, tempo_entry, False)
pass  # print(tempo_entry)

# convert to array the section of the code that contains the SubFlow
all_nodes = procs.lines_to_list_by_keyword(keyword_0, input_array, False)

# extract the Nodes then replace
input_array = all_nodes[0]  # sample entry
print(input_array)

keyword_0 = 'Node['
input_array = tempo_array

indices = []
tempo_string = ''

indices = procs.give_index_of_keyword(input_array, keyword_0, False)
if len(indices) == 1:
    idx = indices[0]
    tempo_string = input_array[idx].split(' ')
    print(tempo_string)
else:
    raise Exception  # should only have one index

