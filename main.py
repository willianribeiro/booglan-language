# -*- coding: utf-8 -*-
import booglan
from texts import text_a, text_b

# TEXT A
print '# TEXT A:'
print ''
print '- Total of prepositions:', booglan.count_prepositions(text_a)
print '- Total of verbs:', booglan.count_verbs(text_a)
print '- Total of verbs in the subjunctive form:', booglan.count_verbs_in_subjunctive_form(text_a)
print '- Total of pretty numbers:', booglan.count_pretty_numbers(text_a)
print '- Vocabulary list:', booglan.create_vocabulary_list(text_a)

print ''
print ''

# TEXT B
print '# TEXT B:'
print ''
print '- Total of prepositions:', booglan.count_prepositions(text_b)
print '- Total of verbs:', booglan.count_verbs(text_b)
print '- Total of verbs in the subjunctive form:', booglan.count_verbs_in_subjunctive_form(text_b)
print '- Total of pretty numbers:', booglan.count_pretty_numbers(text_b)
print '- Vocabulary list:', booglan.create_vocabulary_list(text_b)
