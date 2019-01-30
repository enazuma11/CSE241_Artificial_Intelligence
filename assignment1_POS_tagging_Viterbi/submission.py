from operator import itemgetter				#this functionality is NOT needed. It may help slightly, but you can definitely ignore it completely.

#DO NOT CHANGE!
def read_train_file():
	'''
	HELPER function: reads the training files containing the words and corresponding tags.
	Output: A tuple containing 'words' and 'tags'
	'words': This is a nested list - a list of list of words. See it as a list of sentences, with each sentence itself being a list of its words.
	For example - [['A','boy','is','running'],['Pick','the','red','cube'],['One','ring','to','rule','them','all']]
	'tags': A nested list similar to above, just the corresponding tags instead of words. 
	'''						
	f = open('train','r')
	words = []
	tags = []
	lw = []
	lt = []
	for line in f:
		s = line.rstrip('\n')
		w,t= s.split('/')[0],s.split('/')[1]
		if w=='###':
			words.append(lw)
			tags.append(lt)
			lw=[]
			lt=[]
		else:
			lw.append(w)
			lt.append(t)
	words = words[1:]
	tags = tags[1:]
	assert len(words) == len(tags)
	f.close()
        
	return (words,tags)


def train_func(train_list_words, train_list_tags):
    dict2_tag_follow_tag= {}
    dict2_word_tag = {}
    words=[]
    tags=[]
     
    for i in train_list_words:
        for w in i:
            words.append(w)
    for i in train_list_tags:
        for t in i:
            tags.append(t)
    for i in range(len(words)-1):
        ok=tags[i]
        ik=tags[i+1]
        dict2_tag_follow_tag[ok]=dict2_tag_follow_tag.get(ok,{})
        dict2_tag_follow_tag[ok][ik]=dict2_tag_follow_tag[ok].get(ik,0)
        dict2_tag_follow_tag[ok][ik]+=1
        ok=words[i]
        ik=tags[i]
        dict2_word_tag[ok]=dict2_word_tag.get(ok,{})
        dict2_word_tag[ok][ik]=dict2_word_tag[ok].get(ik,0)
        dict2_word_tag[ok][ik]+=1
    for k in dict2_tag_follow_tag:
        di= dict2_tag_follow_tag[k]
        s=sum(di.values())
        for i in di:
            di[i]/=s
    for k in dict2_word_tag:
        di= dict2_word_tag[k]
        s=sum(di.values())
        for i in di:
            di[i]/=s
            
    return (dict2_tag_follow_tag, dict2_word_tag)        
	



#NEEDS TO BE FILLED!
def assign_POS_tags(test_words, dict2_tag_follow_tag, dict2_word_tag):
    output_test_tags=[]
    line_tags=[]

    for line in test_words:
        line_tags=['']
        line_tags*=len(line)
        for i in range(len(line)):
            if i==0:
                di_transition_probs = dict2_tag_follow_tag['.']
            else:
                di_transition_probs = dict2_tag_follow_tag[line_tags[i-1]]
            di_emission_probs = dict2_word_tag.get(line[i],'')
            if di_emission_probs=='':
                line_tags[i]='N'
            else:
                max_prod_prob=0
                prob=0
                for k,trans_key in enumerate(di_transition_probs):
                    t_trans=trans_key
                    for j,emis_key in enumerate(di_emission_probs):
                        prob=di_transition_probs[trans_key]*di_emission_probs[emis_key]
                        if prob>max_prod_prob:
                            max_prod_prob=prob
                            line_tags[i]=emis_key
            if line_tags[i]=='':
                output_test = max(di_emission_probs, key=di_emission_probs.values())
                for key,value in di_emission_probs.iteritems():
                    if value==output_test:
                        line_tags[i]=key
        output_test_tags.append(line_tags)
        line_tags=[]
    return output_test_tags      









# DO NOT CHANGE!
def public_test(predicted_tags):
	'''
	HELPER function: Takes in the nested list of predicted tags on test set (prodcuced by the assign_POS_tags function above)
	and computes accuracy on the public test set. Note that this accuracy is just for you to gauge the correctness of your code.
	Actual performance will be judged on the full test set by the TAs, using the output file generated when your code runs successfully.
	'''

	f = open('test_public_labeled','r')
	words = []
	tags = []
	lw = []
	lt = []
	for line in f:
		s = line.rstrip('\n')
		w,t= s.split('/')[0],s.split('/')[1]
		if w=='###':
			words.append(lw)
			tags.append(lt)
			lw=[]
			lt=[]
		else:
			lw.append(w)
			lt.append(t)
	words = words[1:]
	tags = tags[1:]
	assert len(words) == len(tags)
	f.close()
	public_predictions = predicted_tags[:len(tags)]
	assert len(public_predictions)==len(tags)

	correct = 0
	total = 0
	flattened_actual_tags = []
	flattened_pred_tags = []
	for i in range(len(tags)):
		x = tags[i]
		y = public_predictions[i]
		if len(x)!=len(y):
			print(i)
			print(x)
			print(y)
			break
		flattened_actual_tags+=x
		flattened_pred_tags+=y
	assert len(flattened_actual_tags)==len(flattened_pred_tags)
	correct = 0.0
	for i in range(len(flattened_pred_tags)):
		if flattened_pred_tags[i]==flattened_actual_tags[i]:
			correct+=1.0
	print('Accuracy on the Public set = '+str(correct/len(flattened_pred_tags)))



# DO NOT CHANGE!
if __name__ == "__main__":
	words_list_train = read_train_file()[0]
	tags_list_train = read_train_file()[1]

	dict2_tag_tag = train_func(words_list_train,tags_list_train)[0]
	dict2_word_tag = train_func(words_list_train,tags_list_train)[1]

	f = open('test_full_unlabeled','r')

	words = []
	l=[]
	for line in f:
		w = line.rstrip('\n')
		if w=='###':
			words.append(l)
			l=[]
		else:
			l.append(w)
	f.close()
	words = words[1:]
	test_tags = assign_POS_tags(words, dict2_tag_tag, dict2_word_tag)
    
	assert len(words)==len(test_tags)
	public_test(test_tags)

	#create output file with all tag predictions on the full test set

	f = open('output','w')
	f.write('###/###\n')
	for i in range(len(words)):
		sent = words[i]
		pred_tags = test_tags[i]
		for j in range(len(sent)):
			word = sent[j]
			pred_tag = pred_tags[j]
			f.write(word+'/'+pred_tag)
			f.write('\n')
		f.write('###/###\n')
	f.close()

	print('OUTPUT file has been created')
