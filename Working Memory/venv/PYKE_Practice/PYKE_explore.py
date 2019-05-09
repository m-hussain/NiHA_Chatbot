from pyke import knowledge_engine, version
print(version)

print(__file__)

my_engine = knowledge_engine.engine('__file__')
print(my_engine)
# my_engine.assert_('family', 'son_of', ('felix_the_cat', 'david'))
# my_engine.activate('bc_related')
# my_engine.prove_1_goal('bc_related.father_son(bruce, $son, ())')

my_engine.add_universal_fact("family", "son_of(Bruce, Thomas)", "abc")