#! /usr/bin/bash

repo=$1
branch=$2
filepath=$3

if [ $# -lt 3 ]
then
    echo "Usage: $0 <repository url> <branch> <filepath>"
    echo ""
    echo "reposity url : repository on which copy operation to be performed"
    echo "branch: branch name from whcih file to be copied to master branch"
    echo "filepath: path of file which is to be copied. Do not add repository name at the beginning"
    echo ""
    echo "Example: $0 'https://github.com/membrandt/Migration-Test.git' 'Client-App-1' 'SmartReviews/Info.plist'"
fi

repo_dir=`echo $repo | sed -e "s#.*\/##" | cut -d '.' -f1`

#### Delete existing clone repository ####
rm -rf ${repo_dir}

#### Clone and checkout source branch ####
git clone $repo
mv $repo_dir ${repo_dir}_tmp
cd ${repo_dir}_tmp
git checkout $branch
cd ..

#### Clone and checkout master branch ####
git clone $repo

#### Copy from source to master branch ####
cp -rf ${repo_dir}_tmp/${filepath} ${repo_dir}/${filepath}

#### Delete source branch ####
rm -rf ${repo_dir}_tmp
