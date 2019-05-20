#!/usr/bin/env python3
def main():
    text = "This is a string of data to be written\n"
    someBytes = b"This should also be written to the file\n"
    aByteArray = bytearray("Hello", "utf-8")
    moreBytes = bytes("\nConverting this to bytes", "ascii")
    try:
        # Write to the file
        with open("binarydata", "wb") as theFile:
            print("Type of stream:", type(theFile).__name__)
            print("Module:", type(theFile).__module__)
            theFile.write(text.encode())
            theFile.write(someBytes)
            theFile.write(aByteArray)
            theFile.write(moreBytes)

        # Read from the file
        with open("binarydata", "rb") as theFile:
            buffer = b''
            while True:
                theText = theFile.read(10)
                if not theText:
                    break
                buffer += theText
        print(buffer)
        print("*" * 50)
        print(buffer.decode())
    except OSError as err:
        print("IO Error:", err)

if __name__ == "__main__": main()