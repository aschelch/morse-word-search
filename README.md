# Find word to memorise Morse code

In order to memorise Morse code, let's search and learn words containing specifique vowels.  
See [Fabien Olicard's video](https://www.youtube.com/watch?v=F4N15Vr-D8A) (in French) that explain the method.

Let's set :  

`-` as the vowel `o`  
`.` as any other vowel `aeiu`  

Now to learn B (`-...`) in Morse, just remember **Bonaparte** (B `-` n `.` p `.` rt `.`)

This script allow you to find words to help you find your own  easy-to-memorise words

## Usage 

    python3 script.py morse_pattern [start_with]

For example to find a word for B (`-...`)

    python3 script.py -..

For a word for B (`-...`) start with letter B

    python3 script.py -.. b
