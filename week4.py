def file_read_write():
    # input from user
    filename = input("Enter the name of the file to read: ")
    
    try:
        #open and read the file
        with open(filename, "r") as infile:
            content = infile.read()
            print("\nOriginal Content:\n", content)

        # Modify the content 
        modified_content = content.upper()
    
        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"\nModified content written to '{new_filename}' successfully!")
        # Display the modified content
        print("modified content:\n", modified_content)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
file_read_write()
