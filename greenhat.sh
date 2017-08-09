#!/bin/bash
# DEBUG, in case \r error occurs
#awk '{ sub("\r$", ""); print }' git-copy.sh > git-copy2.sh
#mv git-copy2.sh git-copy.sh
echo 'Starting Script'
echo $1
echo $2
echo $3
rem=$(( $2 % 2 ))
bakup=".bak"
FILES="$(ls)"
for f in $FILES
do
  echo $f
  if [ $rem -eq 1 ]
  then
    echo "Odd"
	printf "\n#^^^()()^^^" >> $f
  else
	echo "Even"
	cp $f $f$bakup
	sed '$ d' $f$bakup > $f
	rm -f $f$bakup
  fi
  git add $f
  GIT_AUTHOR_DATE=$1 GIT_COMMITTER_DATE=$1 git commit -m $f
  git push
  # take action on each file. $f store current file name
done
git rm realwork.txt
git commit -m 'delete'
git push




