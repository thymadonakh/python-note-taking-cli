# add a new note
def newNote(noteList, text):
    """Add a new note to the list of notes"""
    newNote = text
    noteList.append(newNote)
# delete a note
def deleteNote(noteList, index):
    noteList.pop(index)
# edit a note
def editNote(noteList, index, text):
    noteList[index] = text
# read file from notes.txt
def readFile(noteFile, noteList):
    with open(noteFile, 'r') as f:
        for line in f:
            noteList.append(line.strip())
# write file from notes txt
def writeFile(noteFile, noteList):
    with open(noteFile, 'w') as f:
        for note in noteList:
            f.write(note + '\n')

def main():
    #open notes txt for the note list
    noteList = []
    readFile('notes.txt', noteList)
    print('''
          ============================

          Welcome to your notes app! 😂

          ============================
          ''')

    while True:
        # instruction
        command = input("Enter a command, (new, delete, edit, list, exit): \n")
        if command == 'list':
            # print each note with index
            for note in noteList:
                index = noteList.index(note)
                print(index, "-", note)
        elif command == 'new':
            note = input("Enter a new note: ")
            newNote(noteList, note)
            writeFile('notes.txt', noteList)
        elif command == 'edit':
            index = int(input("Enter index: "))
            if index < 0 or index >= len(noteList):
                print("Invalid index 😩")
                continue
            else:
                print("Your current note is: \n",noteList[index])
            note = input("Enter a new note: ")
            editNote(noteList, index, note)
            writeFile('notes.txt', noteList)
        elif command == 'delete':
            index = int(input("Enter index: "))
            if index < 0 or index >= len(noteList):
                print("Invalid index 😩")
                continue
            else:
                confirm = input("Are you sure you want to delete this note? (y/n): ")
                if confirm == 'y':
                    deleteNote(noteList, index)
                else:
                    print("Note not deleted")
            writeFile('notes.txt', noteList)

        elif command == 'exit':
            break
        else:
            print("Invalid command 😩")

if __name__ == "__main__":
    main()

