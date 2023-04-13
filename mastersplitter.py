"""
   _____                   __                   _________      .__  .__  __    __                
  /     \ _____    _______/  |_  ___________   /   _____/_____ |  | |__|/  |__/  |_  ___________ 
 /  \ /  \\__  \  /  ___/\   __\/ __ \_  __ \  \_____  \\____ \|  | |  \   __\   __\/ __ \_  __ \
/    Y    \/ __ \_\___ \  |  | \  ___/|  | \/  /        \  |_> >  |_|  ||  |  |  | \  ___/|  | \/
\____|__  (____  /____  > |__|  \___  >__|    /_______  /   __/|____/__||__|  |__|  \___  >__|   
        \/     \/     \/            \/                \/|__|                            \/      

Author: Brenton Bowen
Creation Date: 2023-04-13
Description: This script reads a large CSV file, splits it into smaller files with 1,000,000 lines each, 
and saves the out to a directory. Update as needed!
"""

import os
import sys

if len(sys.argv) != 2:
    print("Usage: python split_csv.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

file_number = 1
line_count = 0
max_lines = 1000000

output_directory = os.path.dirname(os.path.abspath(input_file))

with open(input_file, 'r') as infile:
    outfile = None
    for line in infile:
        if line_count == 0:
            outfile = open(os.path.join(output_directory, f'split_{file_number:02d}.csv'), 'w')
            file_number += 1

        outfile.write(line)
        line_count += 1

        if line_count >= max_lines:
            outfile.close()
            outfile = None
            line_count = 0

    if outfile:
        outfile.close()

print("Master Splitter job is complete.")
