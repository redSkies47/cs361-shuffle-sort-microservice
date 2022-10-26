# Name:         Jonathan Chan
# OSU Email:    chanjon@oregonstate.edu
# Course:       CS361 - Software Engineering I
# Assignment:   Assignment 8
# Due Date:     10/31/2022
# Description:  A microservice that receives a playlist & command from a text 
#               file. Depending on the command, the microservice will either
#               shuffle or alphabetically sort the playlist.
import time

# configurations
input_playlist = 'songs.txt'

# receives command to either shuffle or sort
# replaced with either shuffled or sorted playlist
output = 'order.txt'
# output ='fakefile.txt'

# list for holding the contents of the initial playlist
initial_order = list()
song_quantity = 0
new_order_command = ''

# open text file or return error
# save command or use it to call a method for it
def get_valid_command():
    """
    Checks for a new order command in the output file. It confirms
    the command as either 'shuffle' or 'sort', no new valid command,
    or if there was an issue opening the text file.

    :return: True, String - a valid command & the command itself
    :return: False, String - an invalid command & command reset
    :return: False, String - an invalid command & file open failure
    """
    try:
        # get the new order command from the text file
        with open(output) as file:
            new_order_command = file.readline()

        if new_order_command == 'shuffle':
            return True, new_order_command
        elif new_order_command == 'sort':
            return True, new_order_command
        else:
            # reset new order command
            new_order_command = ''
            return False, new_order_command
    except:
        issue_message = 'Issue with opening output file.'
        return False, issue_message


# method for grabbing every line
def get_current_playlist():
    """
    Retrieves the current playlist in the initial playlist file.
    """

    # reset song quantity
    song_quantity = 0

    # build initial input playlist as a list
    with open(input_playlist) as file:
        for song in file:
            # song_quantity += 1
            initial_order.append(song.strip())

    song_quantity = len(initial_order)
    return song_quantity, initial_order

# method for shuffle

# method for sort
def sort(song_playlist):
    """
    Description here
    """
    new_sorted_playlist = sorted(song_playlist, key=str.lower)
    return new_sorted_playlist

# method for writing a new text file

# logic calling the methods

if __name__ == '__main__':

    # test if method works for both and properly fails for fake text file
    # results, my_command = get_valid_command()

    # print('the results are:', str(results))
    # print('the command is', my_command)


    # test getting all songs from text file
    song_num, my_order = get_current_playlist()
    print('\nthere are', str(song_num), 'songs in the playlist')
    print('the order is:\n')
    for song in my_order:
        print(song)
