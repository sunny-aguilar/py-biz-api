#!/bin/bash
# this bash script helps in running various common tasks such as pushing the repo
# to github and running the script on the command line. Some commands are combined
# for greater efficiency.


# commit changes and push to repo
function push_commit()
{
    #commit changes
    git commit -am 'client work'
    # push to github
    git push
}


function commit()
{
    # commt changes only
    git commit -am 'client work'
}

# what to run
if [ "$1" == 'push' ]; then
    # call function
    push_commit
    exit 0
elif [ "$1" == 'commit' ]; then
    # call function
    commit
    exit 0

elif [ "$1" == 'run' ]; then
    # run Python script
    python3 changeImage.py $2 $3
    exit 0

elif [ "$1" == 'runs' ]; then
    # push
    push_commit
    # run Python script
    python3 changeImage.py $2 $3
    exit 0

fi