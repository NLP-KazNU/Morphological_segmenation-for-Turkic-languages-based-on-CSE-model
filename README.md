# CSE_morphological_segmenation

This morphological segmentation algorithms can be used to other Turkic language group as they have similarity in word formation affixes types as in Kazakh language.

Kazakh language has 4 types of affixes: number(singular,plural), possessives, cases, person. 

#All affixes added to the base/stem of word

#Morphology refers to the structures of words in terms of minimal semantic grammatical units known as morphemes. Morphemes are usually divided into two groups, i.e. stems and affixes; stem defines the basic meaning of a word, whereas affixes define the various forms of meaning of the word.

#In an agglutinative language, such a sequence of affixes after the stem is called the ending of the word. Tukeyev et al. defined the complete system of endings for the Kazakh language (Tukeyev et al., 2016).

# Universal morphological segmentation algorithm based on CSE-model
The algorithm for the morphological segmentation of words will be the same for all languages in the Turkic group. This algorithm includes two stages: 1) splitting of stems and word endings and 2) segmentation of word endings into component suffixes.

All agglutinative languages have strict systems of word formation and rules for affix conjunction. Kazakh, Uzbek, and Kyrgyz, like other Turkic languages, are grammatically similar in terms of the types of endings. Having studied the types of endings in Kyrgyz and Uzbek, the CSE-based method created for either of these languages could be applied to the segmentation algorithm based on the CSE-model of the Kazakh language. 

The algorithm for the morphological segmentation of words will be the same for all languages in the Turkic group. 
This algorithm includes two stages: 1) splitting of stems and word endings and 2) segmentation of word endings into component suffixes.

The stem and ending of a word can be split using a stemming algorithm, which is also based on the use of the CSE-model of the agglutinative languages in the Turkic group. The proposed algorithm is a lexicon-free stemming algorithm based on the CSE of Kazakh language (Tukeyev & Turganbaeva, 2016). Herein, this algorithm is proposed for all Turkic language group. All the endings in the set of endings of the agglutinative languages in the Turkic group are divided into classes according to their length. The algorithm first looks for an ending of maximum length for the given word, which will be two symbols less than the length of the word; it is assumed that the stem cannot contain less than two symbols. The assumed ending of length (L) is searched for in an appropriate class of endings of L. If the ending is not in this class; then, the length of the assumed ending is decreased by one (accordingly, the assumed ending of the word is decreased by one symbol on the left side, and this symbol is added to the assumed stem of the word), and the received ending is searched for in the appropriate ending class until the stemming procedure is complete or the word has no ending. 

# Steps of CSE-model algorithm 
The steps of the algorithm for splitting the stem and ending are as follows.

1. Determine L(w).

2. Determine the maximum length of an ending of the analysed word: L[e(w)]max = L(w)—2, where 2 is the minimum length of the word stem.

3. If L(w) ≤ L(e)max; then, assign to L[e(w)] the value of L[e(w)]max: L[e(w)] = L[e(w)]max.

4. Otherwise, assign to L[e(w)] the value of L(e)max: L[e(w)] = L(e)max.

5. Select ending e(w) of length L[e(w)] for analysed word w.

6. Check e(w) for matching with the endings from the list of endings of length L[e(w)]. If it matches, then the stem of the word is determined: st(w) = w—e(w). Go to step 9.

7. Otherwise, the calculated length of the ending of the analysed word is decreased by one: L[e(w)] = L[e(w)]—1.

8. If L[e(w)] < 1, then word w is without ending. Go to step 9. Otherwise, go to step 5.

9. End.

# What you need to use CSE-model
- ending lists(all possible affixes) (in .xls format)
- stems (words that can not be segmentted or ambiguous bases) (in .txt format)

# How to use
1. Download repository
2. Add any Turkic language possible endinds(affixes) list with extension .xls 
3. Add stopwords dictionary 
4. Prepare your train.txt file, which needed to segment
4. Run python file(.py) in any open command prompt(CMD)
5. Save the result of CSE-segmenatation into file. The output path you can change the file's output path to your own path.

# Related papers
1. Ualsher Tukeyev, Aidana Karibayeva. Inferring the Complete Set of Kazakh Endings as a Language Resource. International Conference on Computational Collective Intelligence, 2020. - pp. 741-751
2. Ualsher Tukeyev, Aidana Karibayeva and Zhandos Zhumanov. Morphological segmentation method for Turkic language neural machine translation. Cogent Engineering 7(1):1856500
DOI: 10.1080/23311916.2020.1856500



