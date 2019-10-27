if [ ! -d ~/bin/ ]
then
    mkdir ~/bin/
fi

ln -s -f $PWD/src/passgen.py ~/bin/passgen
