# Especias
Orthographic/phonetic dictionaries for Plover

This is a set of phonetic and orthographic dictionaries for Plover. I'm adding a Finnish one first, but I plan to add a Spanish one too. By phonetic I mean that you write how something is pronounced, and then the dictionary figures out how to spell that. That will probably make more sense in Spanish, as Finnish spelling is so phonetic, you can't really tell if the strokes represent spelling or pronunciation.

I first considered having two ways to write each letter, then use the distinction to add spaces, but that would be somewhat inefficient, and it would make you use some fingers significantly more than others.

I made a layout for Finnish first, and I think the Spanish one would be similar, except the colon keys (W- and -B on the Ireland steno layout) would probably do something else than in Finnish, since Spanish doesn't have as many vowels as Finnish. They would probably add a consonant at the end or something like that.

The layout that it emulates allows writing two "vowels" and two "consonants" per stroke. The available consonants include a few consonant clusters, and the first vowel must be from a list of mostly short vowels and the second vowel is chosen from one of two lists to match the frontness of the first vowel. The following arrangements can be fit in one stroke:

* (C)(V)(C)(V)
* (C)(V)(V)(C)
* (V)(C)(V)(C)
* (V)(C)(C)(V)
* Sometimes also VCiCV, but only when the software would deem the corresponding VCCV doesn't fit the phonotactics. I've could use some feedback on this one.

Any part of those can be left out, but that means some sequences of characters can be written in more than one way, which should probably be used to make briefs.

The name refers to the fact that the Spanish dictionary would allow words like "especias" to be written in a single stroke. The e would be added when starting a word with SP, there would be a consonant chord for "ci" (though it would probably write something else if the vowel after it were an I). And AS is such a common ending in Spanish that I would either be able to write it entirely with the AIU vowel keys or by having the colon keys add an S.

## About the languages
I don't speak Finnish, but someone wanted to write Finnish with an orthographic system, and it had to be able to write Swedish loanwords too. Since the loanwords could contain the characters å and é, it had to be possible to write those characters without loosing too much speed every time they came up, so rather than suggesting a proprietary system whose only publicly available documentation didn't state whether it could handle those characters. I do plan on using a variant for writing in Spanish though.

## Spanish
So far, I've figured I can use three keys per vowel and use the other vowel keys for adding S, then find out what to do with the "impossible" vowel key combinations: diphtongs or vowel+consonants? Here's what I'm considering to do for now:

    #SPTK * KTPS+
    #FR:A * AsRF+
       IU   UI
The same layout as Finnish, except for one of the colon keys being replaced with an s to write plurals. The left hand colon key could indicate whether or not the "word" is stressed on the first syllable. It can then use simple rules that add an accent to one of the vowels when necessary. I'd still have to figure out which consonant clusters to allow, and what to do with IU and AIU.

Also, K would be written as C or QU depending on the vowel, and there would be some combination (probably PTK) to write the letter C. And standalone q (q without u) should be writable somehow, but probably won't allow multiple vowels in the same stroke. But standalone q is very rare in Spanish, more so than in Danish. I'll probably use PT for /g/ and maybe PTKV for /x/ (spelled j and sometimes g). And I don't need double-same-consonants, so I might repurpose those for /tʃ/ (ch), /ɳ/ (ñ), /r/ (rr) and /ʎ/ (ll).

# Configuration
This system is implemented as a Python dictionary for Plover. I'm using all of the keys on the Ireland stenotype, including the number bar, even though it currently doesn't write numbers. Also, you need the Python dictionaries plugin for the Python dictionary to work, and you probably want to have at least one editable dictionary on a higher priority so that you can override the orthographic rules.

And you should set the top half of the S- key to -Z. You can do that from Plover's machine tab with its configuration window. On a qwerty keyboard, that's the Q position, unless you've made some other change, such as moving the whole thing a row up, but if you've changed the layout, you probably know which keys are which.

## Documentation
Currently, you'll have to read the source code. The person who wanted to write in Finnish also wanted to program, so I figured out I could release the code first, then work on documentation later. That's what happens when stuff like this is made for programmers, documentation gets a lower priority. Since I don't speak Finnish, I figured I needed to be able to get feedback early in development, and if I change the rules in the code, I would have to edit the documentation anyway if it existed. Sorry for the inconvenience that this may suppose, especially to non-programmers.

# Todo:
Making it work for Spanish has a pretty high priority, as does adding documentation. I probably won't be adding Danish to this, because the spelling of its words can't be easily generated from their pronunciations, and because I'm also playing with a dictionary-based system for that language, and that can write more characters per stroke at the expense of a steeper learning curve.
