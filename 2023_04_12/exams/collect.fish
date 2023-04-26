function collect -a exercise -d "Collect the specific exercise of all students"
    set dest __all__/$exercise.py
    rm -rf $dest
    for f in (find . -iname $exercise.py)
        echo -e "\n\n# -----------------------\n# $f\n#" >>$dest
        cat $f >>$dest
    end
end
