# atcoder


## �t�@�C���̍쐬
seq -w 001 100 | xargs -I {} bash -c 'for letter in a b c; do touch "{}_${letter}.py"; done'