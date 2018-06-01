# Booglan Language

[![Build Status](https://travis-ci.org/willianribeiro/booglan-language.svg?branch=master)](https://travis-ci.org/willianribeiro/booglan-language)

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


# Answers:
```
# TEXT B:

- Total of prepositions: 67
- Total of verbs: 71
- Total of verbs in the subjunctive form: 47
- Total of pretty numbers: 142
- Vocabulary list: ttcv twhhp twz twmbx twpzb thdwkrmf tzhhm tzcm tznkx tfgr tvwkwb tvb tcgtxw tjfglj tjphzphw tjbtkwp txh tlfcmw trhm trrzq tndsshj tqznjxw tqcglfb tgbf tgbgsgkk tppgq tbkbhkj whjpz whrrvv whqs wzgctbnl wklqzbv wdczjl wdcp wdn wdqr wfs wfbgktm wxnzwrkl wrtpzj wrnh wqd wqpfzj wmgtm wggrxsgv wgbj wpwvqhqg wsf wsfzsjtw wscbg wsntdfw wbnl wbmh htfx htp hwlfxmg hwsnlh hhxqdzx hzvvt hzlcgwgb hkkcvns hdtsb hfrcwxxb hvjrpqjl hjq hltpv hlvmrnpm hlrkwf hlnf hqlxsmzw hqrwq hmkrdc hmmwsnk hmptcqlv hgncbbjh hgsc hphrqqd hphgxtbr hpqk hsfj hbdqsbl hbqz hbp hbsf ztwtmwl ztwcfq ztwgjrwg zwtskvw zwh zwhhrrd zzcm zzcgdl zkhfqnlw zkc zknspwl zdvrwkz zdqkv zdm zdp zftk zfdwv zfqvbw zvvfkz zvrlj zctbl zcddhx zcg zcszw zxtfnll zxn zxsndg zlpjk zrmh zmwxqhj zgtqxrz zgz zgvz zgvmbbs zgqhvhqp zgs zptzwfh zppxnjql zslbzz zsmstwk zbtns zbgpm ktmh ktmhkx kwzrmld khcpkl kzzvplf kzktrvzg kzdq kzpdffgb kkscv kdkc kdj kfmgz kvfn kvc kvbwcw kccl kjcxrgz kjgmtxvs kxkczmd klfqccx klvslp klrqzsdc kls krtzx krdjjdd kgbx kppq kpsfjvmp kpbnbws kszcqm ksv ksxxsw kssz ksbbvw dtg dwkfp dwq dhz dhvz dhxf dhms dzxjcp dkw dknspp dddwp dfwxhwpq dfjp dvfswgpw dcvvtqd dcvgtdxb djn dxw dxlcjtql dxrlfcc dlhwpkg dlhzbwqz dlvrwms dnqh dqdf dqcfq dqgwfcjw dmrk dghkxgn dgqsrfml dgmg dpbkjglj dsclq dsx dbjqgbsz dbgkqjmm fwtngzq fwhhbp fwlxrl fhdsvjh fzxqv fzxgsrv fzrr fzbqfvw fkt fkfchpvm fdwsd fvttnv fvd fckczmjr fcnjkzf fjzcjgt fjxvwfqc fjbvx fxmq fxghv flzq flvvqw fllhsgpb flmnzn flg fnk fqwv fmmtkb fgt fgz fgcltmlv fphv fpzzfs fbmgck vtgqxbwz vww vzckfjhx vznm vdh vdc vfmcgq vfbn vvdldzw vvxtd vvpb vcjhrxxk vcrzwgn vcrqb vjd vxx vxxsfj vltqgfvd vll vlnvm vrnwl vrghmnnb vrsg vnkjbl vnsppv vqxtz vqlqn vqqlvpxr vmtf vmbdrcp vgbgpjth vszqglqq vsfwrmk vssnlv ctkhk ctlnv cht chcfdj chbnltpr czmrsfk ckttxjzw ckwpnskt ckhwjfsg cksqhgnx cdh cdlss cfhxcg cvm cvsch cjt cldnp crt crk crntslnh crscbznr cqfqf cqpprm cmw cgk cgkrn cgksrct cgbbdm cslq cbhkhv cbs jtdl jwjjsndt jhzvkwm jhvfwf jhrhv jzt jzhs jkdtx jkc jkxw jkxhqq jkqldq jkpcq jdvsnnw jdrj jfhphpd jcdmckbb jcjnphr jjdxk jjlc jxw jxvxxw jqgb jmmsm jgzlmml jgvjhhps jptn jpwbvnmr jstcv jslwxgjj jbx xtwjmqwv xwwtbh xwkknr xwcwkhq xwppdz xhh xhrtwbxr xhpwf xzmnwb xdhdkx xdkkg xdgxft xdbnb xfgxjvts xvdfcslp xjlvqmvt xjpkpgxt xxhjgs xxzdbwk xlrqjnfh xlghbtmj xnwzv xqqgtmn xqqp xmcddbn xgws xpn xbxdn ltkpxt ltll ltsdw lwkxjmtf lhc lhrs lzvfrbkp lzjftjl lzrrgdf ldths ldfqkpz ldx lfftwmw lfcfh lvcrbms lvqhvlv lcxcftm lcl lcn ljnfwmt llrlwkdl lnh lnkqmcb lnjnk lmzzqk lgvwlp lgrb lgqpdw lpl lsxpds lsgdgj rwz rhngpzt rhggsk rkmhph rdrtf rvvvrk rvlwpbb rczp rcnv rjprjpt rxngmrv rxgpkh rrpfjck rnpcdk rmvzbx rmvgjxtv rgjbnrnc rstnhrb rsh rsfpp rsr ntj ntmbc nwxdpwvd nhtspn nhnmlkk nzkvk ncm ncgsq njqc nxztbqdk nxf nxvfgxn nxlmhgk nxrs nlcmcp nrw nrwbhq nndbv nnqf nmvs ngrqxb ngp npg nspfs nbvmv nbjc nbjp nbm qtgb qhlww qhbqslp qdkxddbk qdbzm qfln qfrzjb qvcpdh qvb qcwrv qcvqgz qccxb qjkfs qjfhmh qxb qxbjnqzn qlcgcxzf qrlx qnmdxgmx qqwpppfq qqhx qqlr qmbvtrcd qptb qpmlpbcz qbkr qbpl mtl mwvxbg mwrjw mwrqh mhgh mkg mdbvdjks mfkvgms mffgf mcsdj mlnsj mrvkjdr mrlqtwwr mqjhshs mqsgqvg mmj mmjjnm mmrvcn mgsjdsv mpds mpntrzt mpgk mszwfkw msjdjwxk mslz mbfd mbng gwd gwfd ghw gzwgxmj gzzvncct gdwwv gdckm gfjffg gfrdzf gvb gjhxqf gxdgrqlc gxqvvk glsl grplsh gnn gnspkh gqjcl gqrk gmt gmlws gmgzdx gms gmbjbg ggw gpch gbtjpc gbvdx gbpckhbc pwmb phczb pkkqz pvzkmj pvkz pvmlbnnf pjhf pjk pjcxr pjngm pjm pjpv pxwtzf pxh pxxph pxscnhc pntrwc pqzkmwzf pqckzf pglxhxp pgqhcgc ppvr pprsft swkwk swg szk szfxh sfsgt svhpjc svzs sccfq scxp scbndf sxw sxdcq sxfhcjp sxbhfmz slm snvm snvmdz sqtsvhzx sqjtlpgd sgnjl sbdldxb sbc sbjbp sbqrzrrg bttz btkkls btxkcdgg bwkq bhrnlp bkfbjpf bdf bdvvvwcz bdp bffcbxp bflrklbq bfgdsft bvkqw bcfrs bcvhcb bjn bxlzqzb bxqdfmc bxp blzfq blbxrqzj brzkgvwg brfl brxb brq brgswx brsjxrx bnkkpfpf bqfmjbz bqv bmp bgmlbht bstfdcgx bsdjnhz bsbzz
```


# Dependencies:
- [Python 2.7](https://wiki.python.org/moin/BeginnersGuide/Download)


# Running locally:

On terminal, open project root folder and run:

```
python main.py
```


# Running tests:

On terminal, open project root folder and run:

```
python tests.py -v
```
