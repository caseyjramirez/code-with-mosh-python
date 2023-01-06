is_hot = False;
is_cold = False;

if is_hot:
    print('Drink Walker!')
    print('It is a hot day!')
elif is_cold:
    print('Wear warm clothes!')
    print('It is a cold day!')
else:
    print('What a nice day!')



has_high_income = False;
has_good_credit = True;
criminal_record = False;

# LOGICAL OPERATOR
if has_high_income and has_good_credit and not criminal_record:
    print('Good Candidate');
elif has_high_income or has_good_credit:
    print('Decent Candidate');
else:
    print('Bad Candidate');

# COMPARISON OPERATOR
age = 18;

if age < 5:
    print('You are bebe');
elif age >= 60:
    print('you are an elder');
elif age >= 18:
    print('you are an adult');