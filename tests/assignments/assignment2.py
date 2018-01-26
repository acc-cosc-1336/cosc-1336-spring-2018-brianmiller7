def faculty_evaluation_result(nev, rar, som, oft, voft, alw):
    '''
    Write code to calculate faculty evaluation rating according to assignment instructions

    :param nev: Never
    :param rar: Rarely
    :param som: Sometimes
    :param oft: Often
    :param voft: Very Often
    :param alw: Always
    :return: rating as a string
    '''
	totalResp = nev + rar + som + oft + voft + alw
	alw_ratio = alw // totalResp
	voft_ratio = voft // totalResp
	oft_ratio = oft // totalResp
	som_ratio = som // totalResp
	rar_ratio = rar // totalResp
	nev_ratio = nev // totalResp
	
	# Test for Excellent
	if (alw_ratio + voft_ratio_ratio) >= .9 :
		return 'Excellent'
	# Test for Very Good
	elif (oft_ratio + voft_ratio_ratio + alw_ratio) >= .8 :
		return 'Very Good'
	# Test for Good
	elif (som_ratio + oft_ratio + voft_ratio_ratio + alw_ratio) >= .7 :
		return 'Good'
	# Test for NI
	elif (rar_ratio + som_ratio + oft_ratio + voft_ratio_ratio + alw_ratio) >= .6 :
		return 'NI'
	# Test for Unacceptable
	else :
		return 'Unacceptable'

def get_ratings(nev,rar,som, oft,voft, alw):
    '''
    Students aren't expected to know this material yet!
    '''
    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings
    

    
