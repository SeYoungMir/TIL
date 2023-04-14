# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 19:34:04 2023

@author: PC
"""

import pandas as pd
from pandas.io.json import json_normalize
uniqin=pd.read_csv('F:\\Ndjango\\branch_test\\uniqingred.csv',header=None)
uniqin[0].values
uniqin_list=uniqin[0].values.tolist()
enrecipe=pd.read_csv('F:\\Ndjango\\branch_test\\archive\\recipeenglish.csv')
enrecipe.columns
#enrecipe=enrecipe.drop(columns='Ingredients',axis=1)
Instructions=enrecipe['Instructions'].astype(str)
Instructionslist=Instructions.apply(lambda x: x.split('\n'))
list_lengths = Instructionslist.apply(lambda x: len(x))
enrecipe = pd.concat([enrecipe, list_lengths.rename('Instructions_length')], axis=1)
ingredient=enrecipe[['Ingredients','Cleaned_Ingredients']]
print(ingredient)
min(list_lengths)
enrecipe.columns
enrecipe=enrecipe.drop('Unnamed: 0',axis=1)


from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 데이터프레임에서 식재료 추출
ingredients = enrecipe['Cleaned_Ingredients']
'''
# TF-IDF 벡터화
tfidf_vectorizer = TfidfVectorizer(max_features=len(set(ingredients)))
tfidf_matrix = tfidf_vectorizer.fit_transform(ingredients)

# 벡터화된 식재료 딕셔너리 생성
ingredient_dict = {}
terms = tfidf_vectorizer.get_feature_names()
for i, term in enumerate(terms):
    ingredient_dict[term] = tfidf_matrix.getcol(i).sum()

# 딕셔너리를 데이터프레임으로 변환
df_ingredients = pd.DataFrame.from_dict(ingredient_dict, orient='index', columns=['tfidf'])
df_ingredients = df_ingredients.sort_values(by=['tfidf'], ascending=False)
'''
import re
import ast
all_ingredients = []
for ingredients in enrecipe['Cleaned_Ingredients']:
    list_ingredients = ast.literal_eval(ingredients)
    all_ingredients.append(list_ingredients)

ingredients_list2 = [item for sublist in all_ingredients for item in sublist]
merged_ingre_list = list(set(ingredients_list2))

ingredients_lower = [ingredient.lower() for ingredient in ingredients_list2]
def clean_ingredients_list(ingredients_list):
    cleaned_list = []
    for ingredient in ingredients_list:
        ingredient = re.sub(r'\d+x|\d+x\d+|\dx', '', ingredient)
        cleaned_list.append(ingredient)
    return cleaned_list
ingredients4=clean_ingredients_list(ingredients_lower)
print(ingredients4)
print(ingredients_lower[0:])
ingredients4 = list(filter(lambda x: len(x) > 0, ingredients4))



import re
'''
def clean_ingredients(ingredients):
    cleaned_ingredients = []
    for ingredient in ingredients:
        # 괄호 내용 제거
        ingredient = re.sub(r'\(.*?\)', '', ingredient)
        
        # 연결어 기준으로 분리
        ingredient = re.split(r'\s*(?:and|or)\s+', ingredient)
        
        # 숫자와 단위, 특수문자 분수 제거
        ingredient = [re.sub(r'[-\d\s¼½⅓⅔⅛⅜⅝⅞]|tsp|tablespoon|cup|pound|ounce|quart|gallon|pint|inch|cm|mm|\'|"|\.(?!\d)', '', item, flags=re.IGNORECASE) for item in ingredient]
        
        # 공백 제거
        ingredient = [item.strip() for item in ingredient if item]
        
        # 결과물 저장
        cleaned_ingredients.extend(ingredient)
        
    return cleaned_ingredients
'''

import re

def clean_recipe(recipe):
    clean_recipe = []
    for r in recipe:
        # 괄호와 내용물 제거
        r = re.sub(r'\(.*?\)', '', r)
        # 숫자와 분수 제거
        r = re.sub(r'\d+[\d\/]*', '', r)
        # 하이픈 제거
        r = re.sub(r'-', '', r)
        # 특수문자 제거
        r = re.sub(r'[^\w\s]', '', r)
        r = re.sub(r'[-\d⅓⅔¼¾½⅛⅜]+|\.\s|\s?(tsp|tbsp|teaspoon|tablespoon|ounce|oz|cup|pound|lb)s?', '', r)

        clean_recipe.append(r.strip())
    return clean_recipe
ingredients5= clean_recipe(ingredients4)
ingredients5 = list(filter(lambda x: len(x) > 0, ingredients5))
print(ingredients5[0:10])
print(ingredients6[0:10])
'''
def clean_ingredients(ingredients):
    cleaned_ingredients = []
    for ingredient in ingredients:
        # Remove parentheses and contents inside them
        ingredient = re.sub(r'\(.*\)', '', ingredient)
        # Split connected ingredients by 'and', 'or', 'as'
        ingredient = re.split(r'\s+(?:(?:and|or|as)\s+)+', ingredient)

        # Remove whitespace and append to cleaned_ingredients
        for sub_ingredient in ingredient:
            cleaned_sub_ingredient = ' '.join(sub_ingredient.split())
            if cleaned_sub_ingredient:
                cleaned_ingredients.append(cleaned_sub_ingredient)
        
    return cleaned_ingredients
ingredients5= clean_ingredients(ingredients4)


def clean2_ingredients(ingredients):
    cleaned_ingredients = []
    for ingredient in ingredients:
        # 괄호 안 내용 제거
        ingredient = re.sub(r'\([^)]*\)', '', ingredient)

        # 연결어 분리
        ingredient = re.sub(r'and |or |,', '\n', ingredient)

        # 숫자, 분수, 단위 제거
        ingredient = re.sub(r'(?i)\b(?:(?:\d+\s*(?:-?\s*\b)?)+|[-⅓⅔¼¾½⅛⅜]+)\s*(?:cup|tablespoon|teaspoon|pound|ounce|quart|gallon|pint|inch|cm|mm|\')?\.?\s*(?:minced|chopped|diced|sliced)?\s*', '', ingredient)
        ingredient = re.sub(r'[-\d⅓⅔¼¾½⅛⅜]+|\.\s|\s?(tsp|tbs|teaspoon|tablespoon|ounce|oz|cup|pound|lb)s?', '', ingredient)

        # 마침표(.) 제거
        ingredient = re.sub(r'\.', '', ingredient)

        # 공백 제거
        ingredient = ' '.join(ingredient.split())

        cleaned_ingredients.append(ingredient)
    return cleaned_ingredients
'''
ingredients6= clean2_ingredients(ingredients5)
ingredients6 = list(filter(lambda x: len(x) > 0, ingredients6))
'''
def clean_ingredients(ingredients):
    cleaned_ingredients = []
    for ingredient in ingredients:
        # 단위 삭제
        ingredient = re.sub(r'\b\d+\/\d+\b\s*(?:-?\s*\b)?|\b\d+\s*(?:-?\s*\b)?', '', ingredient)
        ingredient = ingredient.replace('at room temperature', 'atroomtemperature')
        ingredient = re.sub(r'\b(a|an|the|such)\b', '', ingredient)
        ingredient = re.sub(r'[-⅓⅔¼¾½⅛⅜]|one|two|three|four|[0-9]+\/[0-9]+', '', ingredient)
        ingredient = re.sub(r'\b(cut|add|any|additional|also|adding|very)\b', '', ingredient)
        ingredient = re.sub(r'\b(?:or\s)?', '', ingredient)
        ingredient = re.sub(r'\b\d* ?x ?\d*\b|\bx\b|\bx ?\b|\b ?x\b', '', ingredient)
        ingredient = re.sub(r'\b\d*x\d*\b|x\b\d*x\d*\b|\b\d*x\d*x\s*inch\b|\b\d*x\s*inch\b|\bx\s*\d*inch\b', '', ingredient)
        ingredient = ingredient.replace('allpurpose', 'all-purpose')
        ingredient = ingredient.replace('all purpose', 'all-purpose')
        ingredient = ingredient.replace('activedry', 'active dry')
        ingredient = ingredient.replace('aluminumfree', 'aluminum free')
        ingredient = ingredient.replace('americanstyle', 'american style')
        ingredient = ingredient.replace('americanstyle', 'american style')
        ingredient = ingredient.replace('store bought', 'storebought')
        ingredient = ingredient.replace('bamboo shoot', 'bambooshoot')
        ingredient = ingredient.replace('bamboo shoots', 'bambooshoots')
        ingredient = re.sub(r'\s+(not|all|another|until|before|being|below|storebought|against|after|as|to|according|about|of|if|for|in|by|into)\s+', '', ingredient)
        ingredient = re.sub(r'^(not|all|about|added|adjoining|adjustivefree|adjustable|another|until|before|being|below|storebought|against|after|as|to|according|about|of|if|for|in|by|into)\s+', '', ingredient)
        ingredient = re.sub(r'\(.*oz.*\)|\(.*lb.*\)|\(.*g.*\)|\d+ ?- ?inch|\d+ ?- ?ounce|\d+ ?- ?cm', '', ingredient)
        ingredient = re.sub(r'\s+(fresh|big|small|medium|mediumsize|diagonal|diagonally|cold|cooked|colored|large|extra|but|⅛|color|combination|discolored|completely|discarded|approximately|freshly|thin|necessary|adjusted|adjustableblade|across|roughly|more|pure|superfine|finely|thinly|coarsely|)\b', '', ingredient)
        ingredient = re.sub(r'(x9x2inch|x9x2|x8x2inch|x8x2|x8x1|x5x3inch|x4x1|x3x1|x3x1inch|x30cm|x1x1|x13x1|oz|lb|accompaniment|g|bin|addition|box|dozen|tablespoon|cm|container|diameter|brick|date|scoop|bulk|bundle|bowl|tsp|tbsp|block|ml|cup|lb|piece|bag|quarts|mg|gram|inchthick|inchlong|cube|lengthwise|teaspoon|kg|ounce|tablespoon|inch|pound|piece|bunch|package|batch)s?\b', '', ingredient)
        ingredient = re.sub(r'\b(halved|diced|baked|countrystyle|welltrimmed|welltoasted|wellstirred|wellseasd|cured|cubed|decorative|cutup|boiled|cheap|buttered|breifly|brinecured|brined|boiling|bless|blanched|blended|needed|cooled|beaten|called|known|additive|kneading|serving|spraying|unfiltered|brushing|activated|shaved|torn|crushed|chilled|quartered|skinned|mixed|granulated|toasted|peeled|sliced|frozen|thawed|seeded|grated|roasted|seperated|minced|cored|sifted|chopped|trimmed|bottled|assorted|bruised|drained|rinsed|softened|cleaned|divided)s?\b', '', ingredient)
        ingredient = re.sub(r'\W', ' ', ingredient)
        ingredient = re.sub(r'\b(oz|lb|bitesize|handful|spoonful|dropperful|barton|dash|bd|bar|spoon|barspoon|layer|can|slice|half|bottle|batch|inchwide|g|cm|tsp|tbsp|ml|cup|lb|piece|bag|quarts|mg|gram|inchthick|inchlong|cube|lengthwise|teaspoon|kg|ounce|tablespoon|inch|pound|piece|bunch|package|batch)s?\b', '', ingredient)
        ingredient = re.sub(r'\b(crumbled|allnatural|imported|prepared|brewed|deveined|braised|blend|finely|bestquality|better|beaten|aged|aluminumfoillined|packed|ameasuring|superpremium|milled|greasing|drizzling|sprinkling|dusting|coating|buttering||melted|lightly)\b', '', ingredient)
        ingredient = re.sub(r'\b(unsalted|whole|whippeddirected|blue|defrosted|taste|tops|above|basic|flavor|following|large|size|spice|type|variation|variety|again|small|leaves)\b(?! [a-z])', '', ingredient)
        ingredient = re.sub(r'\b(oz|lb|g|cm|tsp|b|box|tbsp|block|couple|box|branch|bowl|ml|cup|lb|piece|bag|quarts|mg|gram|inchthick|inchlong|cube|lengthwise|teaspoon|kg|ounce|tablespoon|inch|pound|piece|bunch|package|batch)es?\b', '', ingredient)
        ingredient = re.sub(r'\b(pan|skillet|www|which|when|whatever||pans| com|would|wooden|without|your|online|cutter|iron|plate|jar|jars|plates|thermometer|skewer|skewers|directions|ramekins|toppings|bowl|griddle)\b', '', ingredient)
        ingredient = re.sub(r'\b(slicer|shop|cloth|market|youll|markets|shops|spoon|minutes|discard|disposable|discarding|minute|cool|you|ovenproof|pot|info|steamer|combine|choose|straws|shaker|castiron|ingredient|removed|amys|blender|dishes|pan|pans|supermarkets|bundt|brushed||tweezers|metal|acrylic|are|dish|foil|bamboo)\b|\W', ' ', ingredient)
        ingredient = re.sub(r'\b(at|available|check|crosswise|desired|depending|will|work|scoop|scooped|because|becomes|broken|ingredient info|store|stores)\b|\W', ' ', ingredient)
        ingredient = re.sub(r'\b(atroomtemperature|storebought|roomtemperature)\b', '', ingredient)
        ingredient = re.sub(r'\b(halved|diced|baked|unpeeled|cultivated|countrystyle|cubed|boiled|cheap|buttered|breifly|brinecured|brined|boiling|bless|blanched|blended|needed|cooled|beaten|called|known|additive|kneading|serving|spraying|unfiltered|brushing|activated|shaved|torn|crushed|chilled|quartered|skinned|mixed|granulated|toasted|peeled|sliced|frozen|thawed|seeded|grated|roasted|seperated|minced|cored|sifted|chopped|trimmed|bottled|assorted|bruised|drained|rinsed|softened|cleaned|divided)s?\b', '', ingredient)
        ingredient = re.sub(r'\b\w*proof\w*\b|\W', ' ', ingredient)
        ingredient = re.sub(r'\b(baking sheet)s?\b', '', ingredient)
        ingredient = re.sub(r'\b(baking|covered)\b(?! [a-z])', '', ingredient)
        ingredient = re.sub(r'^(not|all|about|added|adjoining|adjustivefree|adjustable|adjusting|adjustments|another|until|before|being|below|storebought|against|after|as|to|according|about|of|if|for|in|by|into)\s+', '', ingredient)

        ingredient = ingredient.replace('bambooshoot', 'bamboo shoot')
        ingredient = ingredient.replace('bambooshoots', 'bamboo shoots')


        # 공백 제거
        ingredient = ' '.join(ingredient.split())
        cleaned_ingredients.append(ingredient)
    return cleaned_ingredients
'''
unique_ingredients=list(set(ingredients4))
uniqueingre=pd.DataFrame(list(unique_ingredients))
uniqueingre.to_csv('uniqingred.csv',header=None,index=None)

from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from gensim.models import Word2Vec
from keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer()
tokenizer.fit_on_texts(unique_ingredients)

# 각 식재료를 토큰화하여 숫자 시퀀스로 변환
sequences = tokenizer.texts_to_sequences(unique_ingredients)

# 토큰과 해당하는 숫자를 딕셔너리 형태로 출력
word_index = tokenizer.word_index

# TF-IDF 벡터화
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(unique_ingredients)

# K-means 클러스터링(2500개의 클러스터)
kmeans = KMeans(n_clusters=2500).fit(X)
kmeans2 = KMeans(n_clusters=2000).fit(X)
kmeans3 = KMeans(n_clusters=1500).fit(X)
kmeans4 = KMeans(n_clusters=1000).fit(X)
kmeans5 = KMeans(n_clusters=500).fit(X)
# 카테고리 생성 2500
categories = {}
for i, ingredient in enumerate(unique_ingredients):
    category = kmeans.labels_[i]
    if category not in categories:
        categories[category] = []
    categories[category].append(ingredient)


