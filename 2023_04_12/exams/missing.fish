function missing -a student -d "Check missing exercises"
    for exam in (seq 1 25)
        set pexam (string pad -w 6 --char=0 $exam.py)
        if ! test -f $student/$pexam
            echo $pexam
        end
    end
end
