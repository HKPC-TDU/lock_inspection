## This file help to change the "LockData" folder into "train_input"

import re,os
from pathlib import Path

CWD = os.getcwd() + '../'
annotation_path = CWD + "/LockData/Annotation/"
annotation_file = os.listdir(annotation_path)

for i in annotation_file:
    with open(annotation_path+i, 'r') as prev_f, open(CWD+'/train_inputs/annotation/'+i, 'w') as new_f:
        content = prev_f.readline()

        #Continue processing the line before it reaches the end
        while content:

            #Find the original absolute path and pic name (hard code)
            pic = re.findall(r'/LockData(/[^,]+)(/[^,]+.jpg)', content)[0]

            if not os.path.exists(CWD+'/train_inputs/images'+pic[0]):
                # os.mkdir(CWD+'/train_inputs/images'+pic[0])
                Path(CWD+'/train_inputs/images'+pic[0]).mkdir(parents=True, exist_ok=True)

            #Move the file into a new dir and rename the absolute path
            os.rename(CWD+'/LockData'+pic[0]+pic[1], CWD+'/train_inputs/images'+pic[0]+pic[1])
            new_f.write(re.sub(r'/[^,]+/', '/train_inputs/images'+pic[0] + '/', content))

            #Read the next line
            content = prev_f.readline()

            #!Debugger
            # break
"""
"""