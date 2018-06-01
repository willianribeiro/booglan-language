import unittest
import booglan
from texts import text_a

class TestBooglanService(unittest.TestCase):
    def test_is_foo_letter(self):
        '''
            R, T, C, D and B are foo letters
        '''
        self.assertTrue(booglan._is_foo_letter('r'))
        self.assertTrue(booglan._is_foo_letter('t'))
        self.assertTrue(booglan._is_foo_letter('c'))
        self.assertTrue(booglan._is_foo_letter('d'))
        self.assertTrue(booglan._is_foo_letter('b'))
        self.assertFalse(booglan._is_foo_letter('a'))
        self.assertFalse(booglan._is_foo_letter('z'))
        self.assertFalse(booglan._is_foo_letter('#'))

    def test_is_preposition(self):
        '''
            Words with exactly 5 letters no containing the letter "l" and ends in a bar letter (non foo letter) is a preposition.
        '''
        self.assertTrue(booglan._is_preposition('jqkxw'))
        self.assertTrue(booglan._is_preposition('dzdfg'))
        self.assertFalse(booglan._is_preposition('wmhxmmjg'))
        self.assertFalse(booglan._is_preposition('lvnfj'))
        self.assertFalse(booglan._is_preposition('bxwkd'))

    def test_is_verb(self):
        '''
            Words with 8 letters or more that ends in a bar letter (non foo letter) are verbs.
        '''
        self.assertTrue(booglan._is_verb('wmhxmmjg'))
        self.assertTrue(booglan._is_verb('sbbszwrh'))
        self.assertFalse(booglan._is_verb('bxwkd'))
        self.assertFalse(booglan._is_verb('vfnjlksd'))

    def test_is_verb_in_subjunctive_form(self):
        '''
            Verbs begining in a bar letter (non foo letter) are in subjunctive form.
        '''
        self.assertTrue(booglan._is_verb_in_subjunctive_form('wmhxmmjg'))
        self.assertTrue(booglan._is_verb_in_subjunctive_form('sbbszwrh'))
        self.assertFalse(booglan._is_verb_in_subjunctive_form('bdvdgsdg'))
        self.assertFalse(booglan._is_verb_in_subjunctive_form('dvqsmjjf'))
    
    def test_is_pretty_number(self):
        '''
            A number is pretty when is lower than or equal to 422.224 and divisible by 3.
        '''
        self.assertFalse(booglan._is_pretty_number(0))
        self.assertFalse(booglan._is_pretty_number(-422224))
        self.assertFalse(booglan._is_pretty_number(422224))
        self.assertTrue(booglan._is_pretty_number(422226))
        self.assertTrue(booglan._is_pretty_number(600000))
    
    def test_remove_duplicated_items(self):
        lst = ['hnh', 'fcxm', 'jkd', 'hnh', 'fcxm', 'jkd']
        expected = list(set(lst))
        text_without_duplication = booglan._remove_duplicated_items(lst)
        self.assertEqual(text_without_duplication, expected)

    def test_convert_to_decimal_numbers(self):
        lst = ['hnh', 'fcxm', 'jkd', 'bxwkd', 'gzq']
        expected = [1062, 124166, 2089, 832619, 5676]
        decimal_numbers = booglan._convert_to_decimal_numbers(lst)
        self.assertEqual(decimal_numbers, expected)

    def test_count_prepositions_with_only_one_preposition(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg lvnfj sbbszwrh jvvzgr wjjkbjn jqkxw'
        expected = 1
        prepositions_count = booglan.count_prepositions(text)
        self.assertEqual(prepositions_count, expected)

    def test_count_prepositions_with_two_prepositions(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg lvnfj sbbszwrh jvvzgr wjjkbjn jqkxw dzdfg'
        expected = 2
        prepositions_count = booglan.count_prepositions(text)
        self.assertEqual(prepositions_count, expected)

    def test_count_prepositions_with_two_equals_prepositions(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg lvnfj sbbszwrh jvvzgr wjjkbjn jqkxw jqkxw'
        expected = 2
        prepositions_count = booglan.count_prepositions(text)
        self.assertEqual(prepositions_count, expected)

    def test_count_prepositions_with_no_preposition(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg lvnfj sbbszwrh jvvzgr wjjkbjn'
        expected = 0
        prepositions_count = booglan.count_prepositions(text)
        self.assertEqual(prepositions_count, expected)

    def test_count_prepositions_with_empty_text(self):
        text = ''
        expected = 0
        prepositions_count = booglan.count_prepositions(text)
        self.assertEqual(prepositions_count, expected)

    def test_count_verbs_with_only_one_verb(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg lvnfj jvvzgr wjjkbjn jqkxw'
        expected = 1
        verbs_count = booglan.count_verbs(text)
        self.assertEqual(verbs_count, expected)

    def test_count_verbs_with_two_verbs(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg lvnfj sbbszwrh jvvzgr wjjkbjn jqkxw'
        expected = 2
        verbs_count = booglan.count_verbs(text)
        self.assertEqual(verbs_count, expected)

    def test_count_verbs_with_two_equals_verbs(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg wmhxmmjg lvnfj jvvzgr wjjkbjn jqkxw'
        expected = 2
        verbs_count = booglan.count_verbs(text)
        self.assertEqual(verbs_count, expected)

    def test_count_verbs_with_no_verbs(self):
        text = 'hnh fcxm jkd bxwkd gzq lvnfj jvvzgr wjjkbjn jqkxw'
        expected = 0
        verbs_count = booglan.count_verbs(text)
        self.assertEqual(verbs_count, expected)
        
    def test_count_verbs_with_empty_string(self):
        text = ''
        expected = 0
        verbs_count = booglan.count_verbs(text)
        self.assertEqual(verbs_count, expected)
        

    def test_count_verbs_in_subjunctive_form_with_only_one_verb(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg lvnfj jvvzgr wjjkbjn jqkxw'
        expected = 1
        verbs_count = booglan.count_verbs_in_subjunctive_form(text)
        self.assertEqual(verbs_count, expected)

    def test_count_verbs_in_subjunctive_form_with_two_verbs(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg lvnfj sbbszwrh jvvzgr wjjkbjn jqkxw'
        expected = 2
        verbs_count = booglan.count_verbs_in_subjunctive_form(text)
        self.assertEqual(verbs_count, expected)

    def test_count_verbs_in_subjunctive_form_with_two_equals_verbs(self):
        text = 'hnh fcxm jkd bxwkd gzq wmhxmmjg wmhxmmjg lvnfj jvvzgr wjjkbjn jqkxw'
        expected = 2
        verbs_count = booglan.count_verbs_in_subjunctive_form(text)
        self.assertEqual(verbs_count, expected)

    def test_count_verbs_in_subjunctive_form_with_no_verbs(self):
        text = 'hnh fcxm jkd bxwkd gzq lvnfj jvvzgr wjjkbjn jqkxw'
        expected = 0
        verbs_count = booglan.count_verbs_in_subjunctive_form(text)
        self.assertEqual(verbs_count, expected)
        
    def test_count_verbs_in_subjunctive_form_with_empty_string(self):
        text = ''
        expected = 0
        verbs_count = booglan.count_verbs_in_subjunctive_form(text)
        self.assertEqual(verbs_count, expected)    

    def test_count_pretty_numbers(self):
        text = 'fngmrcts mzntdhv hsvmlv scgkccbc nhtbksv sjcg gllhcp jqkxw szdwqjn kbvkhct jkn bbrmrr qrf qsxfl'
        expected = 4
        pretty_numbers_count = booglan.count_pretty_numbers(text)
        self.assertEqual(pretty_numbers_count, expected)

    def test_create_vocabulary_list(self):
        expected = 'ttwhsrg ttjp twvk thh thlcnb tzzrlh tzdrgpm tzcx tkzq tfksgrjx tfpr tvldqdl tvqk tcv tcn tjh tjnd tjgsrz tld tlfd tlqnzds tlbd trf trv tnxn tqm tmhpj tmjzvn tpcccd tsmv tsgfclj tbc tbl wtf wtffzw wtfgn whtpldh whqn whg wkr wksx wfv wvbnq wjtvr wjkmlgbj wjdh wjjkbjn wxfgf wxxpg wxnthr wlfvqb wrbzfkbt wndvc wqbknxwc wmhxmmjg wmzqhf wsn wbcvxcdl wbjj wbq hthzrktj hthpzcq htlj htqlk htqgktlf hwhfgsvg hwmdxv hhvjsgkr hzdnsb hzlvdfhw hzrrx hzqjwkzb hkvgnn hkgz hdhrql hfczm hfr hvdjlm hjk hlkqcz hrlphwt hnh hqcv hqqn hmz hml hgz hgq hphw hpmwbs hsk hsff hsvmlv hbv hbxlb hbgwtpgd ztcbglxj zwzc zwsqjbp zzk zkk zkbx zdtqrc zdkpfl zdgtjp zdglcx zfwrk zfvq zvxt zvr zlqxzs zlbhtkq zrhpwck zrgssm znkpjh zndrbns zncvspg zqmkj zmjzcszn zgffvvj zgn zptpt zpklqhq zplqhqj zpslsgr zpbdfn zsbr zbkskbt zblsrsqb ktvdb kwwpjcw khd khjk khjcxjb khnnv kzkl kzfpz kzc kdtcgmj kdztr kdllrrl kdrqdp kdsgjhp kvfrdt kvxvjlsw kvlzvkm kvnvhrt kvng kcwr kjtljzgq kjhpkc kjnv kxrpl kxp kngjl kqq kqspjsq kmtdvnx kmfhlvfx kpzqwk ksdxh kbw kbvkhct dtkh dhxlhcd dzt dzdfg dzbjc ddt ddjbq dfztff dfqrd dvqsmjjf dctzmmg djx djsn dxrxrhwv dxplf dljgjlt drmb dmkvqc dmddhsk dswh dsctrbf dsp dbtx dbkvc dbpvxzj ftcxbv ftgr fwgqxl fwscncn fzfs fzphplvn fkf fkc fdrbn ffktjhqv ffs fvh fvvsrw fvrltlr fcdxdb fcxm fcp fjkc fjjlpbk fltlw frzxbzb frqfs fngmrcts fqnbw fqsnbvkd fmmrwn fgqv fpgcrdtt fbzsls vtcttzdz vwmprznl vzzk vzkhz vzj vktglnvt vkzthz vkddtgd vdtdhjgs vdfwm vfnjlksd vvpnspkm vckfhfh vcc vjkf vjjttfb vxr vxm vljlqwr vlq vrwnspc vrpxqlcv vnd vmrb vmm vgdjr vgbl vph ctx chhb ckkscz cdwx cdwmhs cftt cfg cvqbcpw cctvz ccwptf ccjsqw cjw cjwdc cxwdzlxk cxvnb crkqfgm crrkmcb crp crpmz cnjrgphz cmhsggfh cgsczs cpwp cpx csw csdqcl csvf csrnm cbqnrtfb cbsnch jtpxn jwdvcghd jhhfbd jhxtm jzfhknfg jzqph jzsbq jkd jkn jfcv jfjlwtdm jfp jvvzgr jccxzzkj jjtxqqhc jrkjljdp jrdhrjgn jrjt jrjrqzs jrxjjnml jnn jnpmn jnshvb jnsdxrq jqwmdmp jqkxw jqss jmtgfc jshqtfx jskknvr jsmqs jbkgqvpp jbxrl xtc xtpqq xwkxr xhpsx xzcm xkwdbdt xkqxcwpm xdcdrvqb xdrbsmwn xfhnnfjc xfnjp xfbqlr xxr xrwgc xrstlrsx xngbwczg xqjrz xmd xmfb xmnc xmgv xmgmpjz xpt xstx xsmzvr xbzj ltnpw ltslrg lwpl lhzdc lhccqf lzngjzkt lzstlwf lkt lkcbft lkgf ldssvhhr lftklg lfhrm lffhzpgc lfc lvnfj lvgprg ljxg ljswczsj ljbqg lxkvnf lxfwv llwgm lll llpzw lrl lqhrffq lqz lqzpkgq lqfl lqrpffs lqnnk lgnxnn lprk lsgxbwvd lsbp lbw lbrvz lbbjx rtpf rtpffmcf rwrzrk rhhgjbkp rhp rzjt rdtttss rvtfn rvfc rvvvbs rvvjppt rvqsnl rvs rvsgkn rczxz rcfghng rcvnpqnh rxpb rlcccs rnst rqdrrttj rqvnt rgzlprq rgpr rgbpwbf rpfncgz rplndz rsxmcdc rslpwdrk rspfv ntrmhf nwxfndmr nwrlww nwnpl nwbtpm nhtbksv nhnrfdfp nzhvvnw nzbhbxlf nkwvdzb nkksnrf ndtzg ndzs nddfdz nfw nfrqmv ncnw njhblnrr nxzwfvxf nxmj nxprpq nlsxf nrkprhx nnnlvnfq nqkrm ngqmbvgw npz nbnkdt qtrvrgdh qtbmp qwdtfkt qwszsw qkcwv qkr qddnj qflzwj qjk qjqdpwdh qxt qxwcb qxqzqtl qlpjkhmm qrf qnkjnqj qqg qqgcx qgd qptblxz qsxfl qbhgfjc qbjtlptx mhq mhsbf mzz mzntdhv mzb mdhw mdvvc mdjwn mfh mfsx mfbhfnzr mvpsmmpg mcfbpg mcxr mcn mjt mjnt mjngwf mjmb mxdwmx mxfkqn mxrr mxnr mltwsr mlcsfnp mrs mnk mnmqt mqtf mqg mqgsl mmkrjpcz mmfltjw mgdqqv mbjkk mbrnl gtwdzvbd gtnmldrf gwlc gzfx gzq gkpxvzbg gdfm gdvnpk gdmz gdskzkkr gvrng gckgnvwh gcksvmk gllhcp grlqvpr grgkkfwq grbrpfk gnnrrh gnsmbtb gqqrbcmh ggvfqgl ggbsdvf gpwxfgd gphrwt gpvckw gpgrzsk gppm gsqtch gbgfsj gbbzhn ptrwhm ptprwvwh pwz phtrdg phd pzxvb pklnkt pdkphhrn pfnmqd pfsg pcc pcq pjhbcg pjsfrw pxwkcpkm pxq plqj prwnkmgf pqjjjx pgwt pgjwwdjh pgllk pprvqcw pprsz psjwr pspb pbfwwvph pbblcm swrbr shwdrhq szdwqjn sdqbl sfnc sfqh svn scntx scgkccbc sjcg sjszpglq slfqkxlc slvjqxtb snlwvf sqsn smwxhlw smhq smcftxv sgt spt spdvqfb spmcmpls sppltgqq sskdpzk sbjmtmrc sblhr sbbszwrh bhw bhhfwgn bzrjt bzbfsjpd bkjtgsv bdvdgsdg bdlr bcnfbb bcgc bxwkd blnsnhgf brlnh bnpbjz bnbtzlf bqwcc bqvn bqlwwrn bmqxxc bgzkr bgpc bpqjwzq bsthm bsgfrzb bbrndmp bbrmrr'
        vocabulary_list = booglan.create_vocabulary_list(text_a)
        self.assertEqual(vocabulary_list, expected)

if __name__ == '__main__':
    unittest.main()
