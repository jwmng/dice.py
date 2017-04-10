# dice.py

Generate a password from a wordlist and punctuation.
Inspired by [Diceware](http://world.std.com/~reinhold/diceware.html)

## Usage

~~~
dice.py [-h] [-n NWORDS] [-p PUNCT] [-c CAP] [-w WORDLIST]

optional arguments:
  -h, --help                    show this help message and exit
  -n NWORDS, --nwords NWORDS    No. of words
  -p PUNCT, --punct PUNCT       No. of added punctuation characters
  -c CAP, --cap CAP             No. of capitalized Words
  -w WORDLIST, --wordlist WORDLIST
                        Path to word list
~~~

## Examples

### Default: 3 words, 1 character, one capital:
~~~
python dice.py
Grove}pairchum
Sable[calebpull
Lugesequin;prof
~~~

### Diceware: 6 words, no punctuation, no capitals:
~~~
python dice.py -p 0 -n 6
helenluxksrhodablastpare
guitarsrillumecunyfyhatch
perilkurtpreylewshinsewn
~~~

### Unix word lists
This requires the `words` package on some distributions. 
With each word capitalized and no punctuation:

~~~
python dice.py -p 0 -n 6 -w /usr/share/dict/british
BucketsTasselsRegradePilafs
FetteredWhoopsInfighterEinsteins
NumbskullsPhobicGarlandIssue

python dice.py -p 0 -n 6 -w /usr/share/dict/ngerman
KorkenzieherSchlinggewächsKreditwünscheBerufungsrecht
KleidZuchtmeisterEbendahinPhönix
AtomstreitkraftWertenErkenntnisgrundlageSeehäfen
~~~
