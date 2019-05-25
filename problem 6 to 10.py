
#PF-Prac-6
def list123(nums):
    for i in range(0,len(nums)-1):
        if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
                return True
    return False

    
nums=[1,2,3,4,5]
print(list123(nums))


#PF-Prac-7
def seed_no(number,ref_no):
    t=number
    while(number!=0):
        rem=number%10
        t*=rem
        number//=10
    if(t==ref_no):
        return True
    else:
        return False
    
number=123
ref_no=738
print(seed_no(number,ref_no))


#PF-Prac-8
def calculate_net_amount(trans_list):
    net_amount=0
    for i in trans_list:
        a=[]
        a=i.split(":")
        if(a[0]=='D'):
            net_amount+=int(a[1])
        else:
            net_amount-=int(a[1])
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))


#PF-Prac-9
def generate_dict(number):
	#start writing your code here
	new_dict={}
	for i in range(1,number+1):
	    new_dict[i]=i**2

	
	return new_dict

number=10
print(generate_dict(number))


#PF-Prac-10
def string_both_ends(input_string):
	if(len(input_string)<2):
	    return -1
	else:
	    s=""
	    s=input_string[0:2]+input_string[len(input_string)-2:len(input_string)]
	    return s

input_string="w3"
print(string_both_ends(input_string))
