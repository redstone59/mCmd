import argparse

parser = argparse.ArgumentParser(
    description="Compiler for mCmd",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

parser.add_argument("in",
                    type = argparse.FileType("r"),
                    help = "Input file, typically an .mcmd file"
                    )

parser.add_argument("-u","--unorganised",
                    action = "store_true",
                    help = "Does not seperate functions into seperate towers. Useful for shorter programs."
                    )

parser.add_argument("-c","--comments",
                    action = "store_true",
                    help = "Include comments as signs"
                    )

parser.add_argument("facing",
                    choices = ["north","east","south","west"],
                    default = "north",
                    metavar = "dir",
                    help = "Changes the direction that the command block towers face"
                    )

parser.add_argument("out",
                    type = argparse.FileType("w")
                    )

arguments = parser.parse_args()