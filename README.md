```
A simple service to deal with a text in Booglan language.
```


# What is Booglan?
Archeologists found a misterious scroll containing two texts:

These texts are in the ancient and mysterious Booglan language. After many years of study, linguists have learned some of the fundamental characteristics of this language.

First, the Booglan letters are classified in two groups: the letters r, t, c, d and b are called "foo letters" while the other letters are called "bar letters".

The linguists have discovered that in the Booglan language, the prepositions are the words of exactly 5 letters which end in a bar letter and do not contain the letter l. Therefore, it is easy to see that there are 49 prepositions in Text A.

Another interesting fact discovered by linguists is that, in the Booglan language, verbs are words of 7 letters or more that end in a bar letter. Furthermore, if a verb starts in a bar letter, then the verb is inflected in its subjunctive form.

Thus, reading Text A, we can tell that there is a total of 71 verbs in the text of which 58 are in the subjunctive form.

A college professor will use Texts A and B to teach Booglan to her students. To help students understand the texts, she must prepare a vocabulary list for each of them. A vocabulary list is an ordered list (without duplicates) of all the words that occur in the text.

But how does alphabetical order work in Booglan? In Booglan, like in our system, words are always ordered lexicographically, but the challenge is that the order of the letters in the Booglan alphabet is different from ours. Their alphabet, in order, is: twhzkdfvcjxlrnqmgpsb. So, when preparing these vocabulary lists, the professor must respect the Booglan alphabetical order.

Not that words aren't fun, but one could ask: how do Booglans represent the numbers? Well, in Booglan, words also represent numbers given in base 20, where each letter is a digit. The digits are ordered from the least significant to the most significant, which is the opposite of our system. That is, the leftmost digit is the unit, the second digit is worth 20, the third one is worth 400, and so on and so forth. The values of the letters are given by the order they appear in the Booglan alphabet (which, as we saw, is ordered differently from our alphabet). That is, the first letter of the Booglan alphabet represents the digit 0, the second letter represents the digit 1, and the last one represents the digit 19.

As an exemple, the Booglan word hnh represents the number 1062.

Booglans consider a number to be pretty if it satisfies all of the following properties:

- it is greater than or equal to 422224
- it is divisible by 3

When we consider Text A as a list of numbers (that is, interpreting each word as a number as per the rules we explained above), we notice that there are 140 distinct pretty numbers.

# Questions:
- How many prepositions are there in Text B?
- How many verbs are there in Text B?
- How many of those verbs in Text B are in the subjunctive form?
- How many distinct pretty numbers are there in Text B?
- Make an ordered vocabulary list from Text B.


# Project dependencies:
- [Python 2.7](https://wiki.python.org/moin/BeginnersGuide/Download)


# Running locally:

On terminal, open project root folder and run:

```
python main.py
```


# Roadmap:
- Implement tests
- Translate and improve code comments
