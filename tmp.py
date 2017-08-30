import subprocess


hard_list = ['coupon', 'special coupon code', 'discount coupon code', 'discount offer off', 'promotion discount']
gender_list = ['women', 'men', 'girls', 'boys', 'babys', 'luggage']
gender_based_category_list = ['accessories', 'clothing', 'clothes', 'jewellery', 'beauty', 'health', 'fashion']
without_gender_based_category_list = ['books', 'text books', 'home', 'garden', 'furnitue', 'grocery', 'food', 'spa']

query_terms_generic_list = []


for required_word in hard_list:
    query_term = ''    
    query_term = query_term + required_word

    query_terms_generic_list.append(query_term)
    
    for gender_word in gender_list:
        gender_query_term = ''
        gender_query_term = query_term + ' ' + gender_word

        query_terms_generic_list.append(gender_query_term)

        for gender_based_word in gender_based_category_list:
            gender_based_query_term = ''
            gender_based_query_term = gender_query_term + ' ' + gender_based_word

            query_terms_generic_list.append(gender_based_query_term)

    for without_gender_based_word in without_gender_based_category_list:
            without_gender_based_query_term = ''
            without_gender_based_query_term = query_term + ' ' + without_gender_based_word

            query_terms_generic_list.append(without_gender_based_query_term)


print len(query_terms_generic_list[:5])

query_terms_generic_list[:5]
for item in query_terms_generic_list[5:7]:
    print item
    subprocess.Popen("python ./google-images-download.py -s \""  + item + "\"" ) 


