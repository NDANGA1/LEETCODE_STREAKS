numbottles=9
numexchange=3
nofull=numbottles
drinks=0
noempty=nofull
while noempty>1:
    noempty=nofull
    drinks+=noempty
    nofull=noempty/numexchange
print(drinks)
