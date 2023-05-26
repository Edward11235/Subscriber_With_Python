def compare_files(file1, file2):
    # Open both files in read mode
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Read the lines of each file
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # Check if number of lines is the same
        if len(lines1) != len(lines2):
            print("Files are not the same: different number of lines.")
            return False

        # Compare each line
        for line1, line2 in zip(lines1, lines2):
            if line1 != line2:
                print(f"Files are not the same: \n{line1}\ndoes not match\n{line2}")
                return False

    print("Files are identical.")
    return True


# Test the function
compare_files('received_text.txt', 'random_message.txt')
