'''Self-building dictionary implementing Danish orthography.
This is a workaround until a Danish system can be working on its own.
It requires the python dictionaries plugin to work.'''

 #
 #  Copyright (C) 2017 Lars Rune Præstmark
 # This file is part of the HjejleOrdbog Danish stenography dictionary collection.
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program. If not, see <http://www.gnu.org/licenses/>.
 #

 # TODO: What's the point of allowing sv? Maybe between vowels it's okay,
 #  But before a space it would probably be better assigned to something else.
 #  Other similar rule changes may be sensible.
LONGEST_KEY = 1

def remakeConsonants(c):
    '''Replacemets to increase the amount of writable consonants'''
    r=c
    r=r.replace('vr','l')
    r=r.replace('ptk','c')
    r=r.replace('tk','b')
    r=r.replace('pk','d')
    r=r.replace('pt','g')
    r=r.replace('pv','m')
    r=r.replace('tv','j')
    r=r.replace('kv','q')
    r=r.replace('sm','w')
    r=r.replace('sj','n')
    r=r.replace('sq','x')
    r=r.replace('sb','f')
    r=r.replace('sd','z')
    r=r.replace('sg','h')
    r=r.replace('spr','pp')
    r=r.replace('str','tt')
    r=r.replace('skr','kk')
    r=r.replace('bv','f')
    r=r.replace('dv','ss')
    r=r.replace('gv','h')
    r=r.replace('sss','ll')
    return(r)

def remakeVowel1(v):
    # Individual vowel keys
    #  There are positive and negative versions.
    #  Negative means if there's an a, o or u later,
    #  it gets replaced by ä, ö or y.
    if(v=='a'): return('a') #+
    if(v=='o'): return('o') #+
    if(v=='e'): return('e') #- There's also a positive version, au
    if(v=='u'): return('u') #+

    if(v=='ao'): return('å') #+
    if(v=='ae'): return('ä') #-
    if(v=='au'): return('e') #+ Positive e
    # Positive and negative i
    if(v=='eu'): return('i') #-
    if(v=='aoe'): return('i') #+
    
    if(v=='oe'): return('ö') #-
    if(v=='ou'): return('é') #-
    if(v=='aou'): return('y')#-
    if(v=='oeu'): return('aa')#+
    if(v=='aeu'): return('ai')#+
    if(v=='aoeu'): return('')#- # This means no vowels, but negative
    if(v!=''): raise KeyError #Shouldn't happen anyway
    return('') # No vowel

def remakePositiveVowel(v):
    # Individual vowel keys
    #  There are positive and negative versions.
    #  Negative means if there's an a, o or u later,
    #  it gets replaced by ä, ö or y.

    # We get the vowel in AOEU format,
    # But A means long vowel and OEU means AIU.
    # Convert to AIU2 format for readability
    v2=''
    v2length=0
    if('o' in v): v2+='a'
    if('e' in v): v2+='i'
    if('u' in v): v2+='u'
    if('a' in v): v2length=1
    # Get the missing vowels back
    r=''
    if(v2=='a'): r='a'
    if(v2=='i'): r='i'
    if(v2=='u'): r='u'
    if(v2=='ai'): r='e'
    if(v2=='au'): r='o'
    if(v2=='iu'): r='au'
    if(v2=='aiu'): r='ai'
    if(v2length==1): #Apply vowel length
        if(len(r)==1): r*=2
        elif(v2=='iu'): r='uo'
        elif(v2=='aiu'): r='oa'
        elif(v2==''): r='oi'
    return(r)

def remakeNegativeVowel(v):
    r=remakePositiveVowel(v)
    r=r.replace('a','ä')
    r=r.replace('o','ö')
    r=r.replace('u','y')
    return(r)

def remakeVowel2(v, sign):
    if(sign): return(remakePositiveVowel(v))
    return(remakeNegativeVowel(v))

def getVowelSign(v):
    # Vowel signsare either positive or negative.
    # Negative means if there's an a, o or u later,
    # it gets replaced by ä, ö or y.
    if(v=='a'): return(True) # a
    if(v=='o'): return(True) # o
    if(v=='e'): return(False) # e
    if(v=='u'): return(True) # u

    if(v=='ao'): return(True) # å
    if(v=='ae'): return(False) # ä
    if(v=='au'): return(True) # e
    # Positive and negative i
    if(v=='eu'): return(False) # i
    if(v=='aoe'): return(True) # i
    
    if(v=='oe'): return(False) # ö
    if(v=='ou'): return(False) # é
    if(v=='aou'): return(False) # y
    if(v=='oeu'): return(True) # a
    if(v=='aeu'): return(True) # ai
    if(v=='aoeu'): return(False) # # This means no vowels, but negative
    return(True) # No vowel is positive

def remakeTop(r):
    r=r.replace('1','S')
    r=r.replace('2','T')
    r=r.replace('3','P')
    r=r.replace('4','H')
    r=r.replace('5','A')
    r=r.replace('0','O')
    r=r.replace('6','F')
    r=r.replace('7','P')
    r=r.replace('8','L')
    r=r.replace('9','T')
    return(r)

def lookup(key):
    '''Main lookup function:
Changes layout and reorders letters.
'''
    assert len(key) <= LONGEST_KEY
    # Constants for converting keys in the right order,
    #  Needed beacuse several steno keys have the same labels.
    STATE_CONSONANTS1=0 # These refer to the raw strokes
    STATE_VOWELS=1
    STATE_CONSONANTS2=3
    consonants1=[] # These are for generated syllables
    consonants2=[]
    vowels1=[]
    changedOrder1=False
    for i in '#0123456789':
        if (i in key[0]): # The number bar is pressed
            changedOrder1=True
    vowels2=[]
    layoutState=STATE_CONSONANTS1
    tkey=remakeTop(key[0])
    if(len(key)==1):
        if key[0]=='*': raise KeyError # Don't override delete-word!
        for i in tkey:
            if(layoutState==STATE_CONSONANTS1):
                if(i in 'AOEU*'):
                    layoutState=STATE_VOWELS
                elif(i in '-'):
                    layoutState=STATE_CONSONANTS2
                else:
                    if(i=='S'): consonants1+=[(4,'v')] # Numbers are used
                    elif(i=='T'): consonants1+=[(1,'p')] # for reordering
                    elif(i=='K'): consonants1+=[(5,'r')] # keys later.
                    elif(i=='P'): consonants1+=[(2,'t')]
                    elif(i=='W'): vowels1+=[(6,'a')]
                    elif(i=='H'): consonants1+=[(3,'k')]
                    elif(i=='R'): vowels1+=[(7,'o')]
            if(layoutState==STATE_VOWELS):
                if(i=='A'): vowels1+=[(8,'e')]
                elif(i=='O'): vowels1+=[(9,'u')]
                elif(i=='E'): vowels2+=[(9,'u')]
                elif(i=='U'): vowels2+=[(8,'e')]
                else: layoutState=STATE_CONSONANTS2
            if(layoutState==STATE_CONSONANTS2):
                if(i=='S'): consonants2+=[(4,'v')]
                elif(i=='T'): consonants2+=[(0,'s')]
                elif(i=='G'): consonants2+=[(5,'r')]
                elif(i=='L'): consonants2+=[(1,'p')]
                elif(i=='P'): consonants2+=[(2,'t')]
                elif(i=='B'): vowels2+=[(6,'a')]
                elif(i=='F'): consonants2+=[(3,'k')]
                elif(i=='R'): vowels2+=[(7,'o')]
                elif(i=='Z'): consonants1+=[(0,'s')]#changed layout
        # And now we use the numbers for the reordering:
        consonants1=[i[1]for i in sorted(consonants1)]
        vowels1=[i[1]for i in sorted(vowels1)]
        vowels2=[i[1]for i in sorted(vowels2)]
        consonants2=[i[1]for i in sorted(consonants2)]
        # Replace sequences with missing letters
        consonants1=remakeConsonants(''.join(consonants1))
        # We get the type before the vowel to avoid complications
        #  with diphtongs or long vowels. That's probably a sign
        #  that the code could be organised better.
        vowelSign=getVowelSign(''.join(vowels1)) # Get first vowel type
        vowels1=remakeVowel1(''.join(vowels1)) # Get the first vowel
        consonants2=remakeConsonants(''.join(consonants2))
        vowels2=remakeVowel2(''.join(vowels2), vowelSign) # Get second vowel
        syllable1=consonants1+vowels1 # Mora would be a more descriptive term,
                                  # since these aren't complete syllables.
                                  # But speakers of western languages don't
                                  # think in terms of moras.
        if(changedOrder1):
            syllable1=vowels1+consonants1
        syllable2=consonants2+vowels2
        if('D' in key[0]):
            syllable2=vowels2+consonants2
        r=syllable1+syllable2
        if('*' in key[0]):r=r+'{^}'
        return(r)
    raise KeyError
