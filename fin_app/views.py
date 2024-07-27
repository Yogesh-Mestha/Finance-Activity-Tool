from django.shortcuts import render

def index(request): 
    return render(request,'home.html')

def home(request):
    return render(request,"home.html")

def pageplan(request):
    return render(request,'plans.html')

def pagejl(request):
    return render(request,'jeevanlabh.html')

def jl(request):
    saa=int(request.GET['saa'])
    pt=int(request.GET['policyTerm'])
    age=int(request.GET['age'])
    if saa<0:
        e1="Please provide valid input"
        return render(request,"jeevanlabh.html",{'e1':e1,'v1':saa,'v2':pt,'v3':age})
    if saa<200000:
        e1="Sum assured must be greter then 2,00,000"
        return render(request,"jeevanlabh.html",{'e1':e1,'v1':saa,'v2':pt,'v3':age})
    if saa>10000000:
        e1="Sum assured should not be greter then 1,00,00,000"
        return render(request,"jeevanlabh.html",{'e1':e1,'v1':saa,'v2':pt,'v3':age})
        
    if pt == 16:
        e2=""
    elif pt == 21:
        e2=""
    elif pt == 25:
        e2=""
    else:
        e2="Invalid policy term, Valid Premium Paying terms are  16,21,25 "
        return render(request,"jeevanlabh.html",{'e2':e2,'v1':saa,'v2':pt,'v3':age})
   
    if age<0:
        e3="Please provide valid value for age"
        return render(request,"jeevanlabh.html",{'e1':e1,'v1':saa,'v2':pt,'v3':age})
    if age<8:
        e3="policy holder should complete 8 years in jeevan labh-936"
        return render(request,"jeevanlabh.html",{'e3':e3,'v1':saa,'v2':pt,'v3':age})
    if age>59:
        e3="Maximum age of policy holder is 59 years"
        return render(request,"jeevanlabh.html",{'e3':e3,'v1':saa,'v2':pt,'v3':age})
        
    sum_assured=saa
    policy_term=pt
    premium_rate = 0
    if age >= 50 :
        if policy_term == 16:
            premium_rate = 0.5984
            py=10
        elif policy_term == 21:
            premium_rate = 0.4935
            py=15
        elif policy_term == 25:
            premium_rate = 0.4397
            py=16
    elif age >=45 :
        if policy_term == 16:
            premium_rate = 0.6146
            py=10
        elif policy_term == 21:
            premium_rate = 0.5069
            py=15
        elif policy_term == 25:
            premium_rate = 0.4406
            py=16           
    elif age >=40 :
        if policy_term == 16:
            premium_rate = 0.6308
            py=10
        elif policy_term == 21:
            premium_rate = 0.5203
            py=15
        elif policy_term == 25:
            premium_rate = 0.4445
            py=16    
    elif age >=35:
        if policy_term == 16:
            premium_rate = 0.6470
            py=10
        elif policy_term == 21:
            premium_rate = 0.5337
            py=15
        elif policy_term == 25:
            premium_rate = 0.4424
            py=16
    elif age >=30:
        if policy_term == 16:
            premium_rate = 0.6796
            py=10
        elif policy_term == 21:
            premium_rate = 0.5471
            py=15
        elif policy_term == 25:
            premium_rate = 0.4433
            py=16
    elif age >=25 :
        if policy_term == 16:
            premium_rate = 0.6632
            py=10
        elif policy_term == 21:
            premium_rate = 0.559
            py=15
        elif policy_term == 25:
            premium_rate = 0.4442
            py=16               
    else:
        if policy_term == 16:
            premium_rate = 0.6796
            py=10
        elif policy_term == 21:
            premium_rate = 0.5607
            py=15
        elif policy_term == 25:
            premium_rate = 0.5001
            py=16

    premium_amount_m = sum_assured * premium_rate / 100
    premium_amount=premium_amount_m*12
    premium_amount=premium_amount+premium_amount*0.024375
    premium_amount=round(premium_amount,2)
    maturity_amount = (premium_amount*py) + (premium_amount * policy_term)
    maturity_amount=round(maturity_amount,2)
    return render(request,"jeevanlabh.html",{'v1':saa,'v2':pt,'v3':age,'premium_amount':premium_amount,'maturity_amount':maturity_amount})

def resetjl(request):
    e1=""
    e2=""
    e3=""
    v1=""
    v2=""
    v3=""
    maturity_amount=""
    premium_amount=""
    return render(request,"jeevanlabh.html",{'e1':e1,'e2':e2,'e3':e3,'v1':v1,'v2':v2,'v3':v3,'premium_amount':premium_amount,'maturity_amount':maturity_amount})

def pageju(request):
    return render(request,'jeevanumang.html')

def ju(request):
    sum_assured = int(request.GET['sum_assured'])
    policy_term =  int(request.GET['policy_term'])
    premium_payment_term =  int(request.GET['premium_payment_term'])
    age= int(request.GET['age'])
    pt=premium_payment_term
    bonus_rate = 48
    premium_rate = 0.0
    survival_benefit_rate = 0.0
    
    if sum_assured<0:
        e1="please provide valid input"
        return render(request,"jeevanumang.html",{'e1':e1,'v1':sum_assured,'v2':pt,'v3':policy_term,'v4':age}) 
  
    if sum_assured<200000:
        e1="Minimum Sum Assured is 200000"
        return render(request,"jeevanumang.html",{'e1':e1,'v1':sum_assured,'v2':pt,'v3':policy_term,'v4':age}) 

    if sum_assured>1000000000:
        e1="Maximum Sum Assured is 1000000000"
        return render(request,"jeevanumang.html",{'e1':e1,'v1':sum_assured,'v2':pt,'v3':policy_term,'v4':age}) 
    
    if premium_payment_term == 15:
        premium_rate = 918.15
    elif premium_payment_term == 20:
        premium_rate = 716.80
    elif premium_payment_term == 25:
        premium_rate = 591.65
    elif premium_payment_term == 30:
        premium_rate = 499.10
    else:
        e2="Invalid Premium Payment Term "
        return render(request,"jeevanumang.html",{'e2':e2,'v1':sum_assured,'v2':pt,'v3':policy_term,'v4':age}) 
    
    if policy_term == 100:
        survival_benefit_rate = 55
    elif policy_term == 105:
        survival_benefit_rate = 60
    elif policy_term == 110:
        survival_benefit_rate = 65
    elif policy_term == 115:
        survival_benefit_rate = 70
    else:
        e3="Invalid Policy Term"
        return render(request,"jeevanumang.html",{'e3':e3,'v1':sum_assured,'v2':pt,'v3':policy_term,'v4':age}) 
    
    if age<10:
        survival_benefit_rate=survival_benefit_rate+38
        premium_rate=premium_rate+100
    elif age<15:
        survival_benefit_rate=survival_benefit_rate+35
        premium_rate=premium_rate+90
    elif age<20:
        survival_benefit_rate=survival_benefit_rate+32
        premium_payment_term=premium_payment_term+80      
    elif age<25:
        survival_benefit_rate=survival_benefit_rate+28
        premium_rate=premium_rate+70
    elif age<30:
        survival_benefit_rate=survival_benefit_rate+24
        premium_rate=premium_rate+60
    elif age<35:
        survival_benefit_rate=survival_benefit_rate+20
        premium_rate=premium_rate+50
    elif age<40:
        survival_benefit_rate=survival_benefit_rate+16
        premium_rate=premium_rate+40        
    elif age<45:
        survival_benefit_rate=survival_benefit_rate+12
        premium_rate=premium_rate+30
    elif age<50:
        survival_benefit_rate=survival_benefit_rate+8
        premium_rate=premium_rate+20
    elif age<56:
        survival_benefit_rate=survival_benefit_rate+4
        premium_rate=premium_rate+10
    
    if age<0:
        e4="Please Provide Valid Input"
        return render(request,"jeevanumang.html",{'e4':e4,'v1':sum_assured,'v2':pt,'v3':policy_term,'v4':age}) 
    
        
    if age>56:
        e4="Maximum age is 55 years "
        return render(request,"jeevanumang.html",{'e4':e4,'v1':sum_assured,'v2':pt,'v3':policy_term,'v4':age}) 

        
    maturity_amount = sum_assured + (sum_assured * bonus_rate / 100)
    maturity_amount += (survival_benefit_rate / 100) * maturity_amount
    maturity_amount -= (premium_rate * premium_payment_term)
    maturity_amount += (premium_rate * (policy_term - premium_payment_term))
    return render(request,"jeevanumang.html",{'v1':sum_assured,'v2':pt,'v3':policy_term,'v4':age,'maturity_amount':maturity_amount}) 
    


def resetju(request):
     v1=""
     v2=""
     v3=""
     r=""
     r2=""
     maturityamount=""
     return render(request,"jeevanumang.html",{'v1':v1,'v2':v2,'v3':v3,'r':r,'r2':r2,'maturityamount': maturityamount})

def pagebonus(request):
    return render(request,'bonus.html')

def bonusCal(request):
    salary=int(request.GET['salary'])
    percentage=eval(request.GET["percentage"])
    
    if salary < 0:
        e1="salary must not be negitive"
        return render(request,"bonus.html",{'e1':e1,'v1':salary,'v2':percentage})
    
    if salary < 5000:
        e1="salary must  be greater then 5000 "
        return render(request,"bonus.html",{'e1':e1,'v1':salary,'v2':percentage})
    
    if percentage<0:
        e2="Percentage should not be negitive"
        return render(request,"bonus.html",{'e2':e2,'v1':salary,'v2':percentage})
    
    bonus = (salary * percentage) / 100
    r=" Bonus Amount : "
    bonus=round(bonus,2)
    return render(request,"bonus.html",{'r':r,'result':bonus,'v1':salary,'v2':percentage})

def resetbonus(request):
    v1=""
    v2=""
    r=""
    result="" 
    return render(request,"bonus.html",{'v1':v1,'v2':v2,'r':r,'result':result})

def pageagent(request):
    return render(request,'agent.html')

def agentCal(request):
    years=int(request.GET['years'])
    salary=int(request.GET['salary1'])
    
    
    if years<0:
        e1=" Please provide valid year "
        return render(request,"agent.html",{'v1':years,'v2':salary,'e1':e1})
    
    if years<10:
        e1=" Agent work experience should not be less then 10 years "
        return render(request,"agent.html",{'v1':years,'v2':salary,'e1':e1})
        
    if years>25:
        e1=" Agent work experience should not be greter then 25 years "
        return render(request,"agent.html",{'v1':years,'v2':salary,'e1':e1})
        
    if salary<0:
        e2=" Please provide valid Amount  "
        return render(request,"agent.html",{'v1':years,'v2':salary,'e2':e2})
        
    if salary<39000:
        e2=" salary should not be less then 39,000"
        r=""
        e1=""
        result="" 
        return render(request,"agent.html",{'v1':years,'v2':salary,'r':r,'result':result,'e1':e1,'e2':e2})
    
    if salary>67000:
        e2=" salary should not be greater then 67,000"
        return render(request,"agent.html",{'v1':years,'v2':salary,'r':r,'result':result,'e1':e1,'e2':e2})
    
    r="  Gratuity Amount  : "
    gratuity = (salary * years) / 2
    return render(request,"agent.html",{'r':r,'result':gratuity,'v1':years,'v2':salary})

def resetagent(request):
    v1=""
    v2=""
    r=""
    result="" 
    return render(request,"agent.html",{'v1':v1,'v2':v2,'r':r,'result':result})



def pageequity(request):
    return render(request,'equity.html')

def epf(request):
    investmentamount=int(request.GET['investment-amount'])
    rate=eval(request.GET['rate-of-r'])
    investmentperiod=int(request.GET['investment-period'])
    if investmentamount<0:
        e1="Please provide valid input"
        return render(request,"equity.html",{'e1':e1,'v1':investmentamount,'v2':rate,'v3':investmentperiod})
    if investmentamount<500:
        e1="Investment amount should not less then 500"
        return render(request,"equity.html",{'e1':e1,'v1':investmentamount,'v2':rate,'v3':investmentperiod})
        
    if investmentamount>1000000:
        e1="Investment amount should not be greter then 10,00,000"
        return render(request,"equity.html",{'e1':e1,'v1':investmentamount,'v2':rate,'v3':investmentperiod})
        
    if rate<6.5:
        e2="Invalid input,Rate of return lies within 6.5 and 7.5"
        return render(request,"equity.html",{'e2':e2,'v1':investmentamount,'v2':rate,'v3':investmentperiod})
    if rate>7.5:
        e2="Invalid input,Rate of return lies within 6.5 to 7.5"
        return render(request,"equity.html",{'e2':e2,'v1':investmentamount,'v2':rate,'v3':investmentperiod})
    
        
    if investmentperiod<0:
        e3="Please provide valid input"
        return render(request,"equity.html",{'e3':e3,'v1':investmentamount,'v2':rate,'v3':investmentperiod})
    
    if investmentperiod>30:
        e3="Invest period should not be greter then 30 year"
        return render(request,"equity.html",{'e3':e3,'v1':investmentamount,'v2':rate,'v3':investmentperiod})

    maturityAmount = investmentamount * pow(1 + (rate / 100),investmentperiod )
    result=round(maturityAmount,2)
    r="    Maturity Amount   : "
    return render(request,"equity.html",{'r':r,'result':result,'v1':investmentamount,'v2':rate,'v3':investmentperiod})

def resetepf(request):
    v1=""
    v2=""
    v3=""
    r=""
    result=""
    return render(request,"equity.html",{'v1':v1,'v2':v2,'v3':v3,'r':r,'result':result})
 

def pagedebtfinal(request):
    return render(request,'debtfinal.html')

def dept(request):
    investmentamount=int(request.GET['investment-amount'])
    interestrate=11.54
    investmentperiod=int(request.GET['investment-period'])
    
    if investmentamount<0:
        e1="Please provide valid input"
        return render(request,"debtfinal.html",{'e1':e1,'v1':investmentamount,'v2':interestrate,'v3':investmentperiod})
    if investmentamount<500:
        e1="Investment amount should not less then 500"
        return render(request,"debtfinal.html",{'e1':e1,'v1':investmentamount,'v2':interestrate,'v3':investmentperiod})
       
    if investmentamount>1000000:
        e1="Investment amount should not be greter then 10,00,000"
        return render(request,"debtfinal.html",{'e1':e1,'v1':investmentamount,'v2':interestrate,'v3':investmentperiod})

        
    if investmentperiod<=-1:
        e3="Invest period should be negitive"
        return render(request,"debtfinal.html",{'e3':e3,'v1':investmentamount,'v2':interestrate,'v3':investmentperiod})
   
    if investmentperiod>30:
        e3="Invest period should be within  30 year"
        return render(request,"debtfinal.html",{'e3':e3,'v1':investmentamount,'v2':interestrate,'v3':investmentperiod})
    
    
    maturityAmount = investmentamount * pow(1 + ( interestrate / 100), investmentperiod)
    result=round(maturityAmount,2)
    r="    Maturity Amount : "
    return render(request,"debtfinal.html",{'r':r,'result':result,'v1':investmentamount,'v3':investmentperiod})

def resetdebt(request):
    e1=""
    e2=""
    e3=""
    r=""
    result=""
    investmentperiod=""
    investmentamount=""
    return render(request,"debtfinal.html",{'e1':e1,'e2':e2,'e3':e3,'r':r,'result':result,'v1':investmentamount,'v3':investmentperiod})


def pageppf(request):
    return render(request,'ppf.html')
    
def productppf(request):
    p=int(request.GET["yiv"])
    i=int(request.GET["tpv"])
    n=0.071
    
    if p<0:
        e1="Yearly investment should not be negitive"
        return render(request,"ppf.html",{'e1':e1,'v1':p,'v2':i})
    
    if p<500:
        e1="Yearly investment starts from 500rs"
        return render(request,"ppf.html",{'e1':e1,'v1':p,'v2':i})
    
    if p>150000:
        e1="Yearly investment should less then 150000"
        return render(request,"ppf.html",{'e1':e1,'v1':p,'v2':i})
    
    if i<15:
        e2="Time period starts from 15 years"
        return render(request,"ppf.html",{'e2':e2,'v1':p,'v2':i})
    
    if i>50:
        e2="Time period should not be greater then 50"
        return render(request,"ppf.html",{'e2':e2,'v1':p,'v2':i})
    
    Investmentamount=p*i
    TotaInterest=p*(i)*n*12
    MaturityValue=TotaInterest+Investmentamount
    Investmentamount=round(Investmentamount,2)
    TotaInterest=round(TotaInterest,2)
    MaturityValue=round(MaturityValue,2)
    return render(request,"ppf.html",{'Investmentamount':Investmentamount,'TotaInterest':TotaInterest,'MaturityValue':MaturityValue,'v1':p,'v2':i})

def resetppf(request):
    v1=""
    v2=""
    Investmentamount=""
    TotaInterest=""
    MaturityValue=""
    return render(request,"ppf.html",{'Investmentamount':Investmentamount,'TotaInterest':TotaInterest,'MaturityValue':MaturityValue,'v1':v1,'v2':v2})

def pagebp(request):
    return render(request,'b-pension.html')

def bp(request):
    salary=int(request.GET['salary'])
    years=int(request.GET['years'])
    
    if salary<0:
        e1="Provide valid salary amount"
        return render(request,"b-pension.html",{'v1':salary,'v2':years,'e1':e1})
      
    if years<0:
        e2="provide valid value"
        return render(request,"b-pension.html",{'v1':salary,'v2':years,'e2':e2})
    
    if years<10:
        e2="According to EPS, Empolyee must complete 10 years of experience in order to receive the pension"
        return render(request,"b-pension.html",{'v1':salary,'v2':years,'e2':e2})
        
    
    pensionAmount =  salary * years / 70
    pensionAmount=round(pensionAmount,2)
    return render(request,"b-pension.html",{'pensionAmountans':pensionAmount,'v1':salary,'v2':years})

def resetbp(request):
    v1=""
    v2=""
    pensionAmount=""
    e1=""
    e2=""
    return render(request,"b-pension.html",{'e1':e1,'e2':e2,'pensionAmountans':pensionAmount,'v1':v1,'v2':v2})
    

def pagefp(request):
    return render(request,'f-pension.html')

def fpcal(request):
    salary=int(request.GET['salary1'])
    rate=eval(request.GET['rate1'])
    if salary<0:
        e1="Please provide valid salary amount"
        return render(request,"f-pension.html",{'v1':salary,'v2':rate,'e1':e1})
    
    if rate<0:
        e2="Please provide valid input"
        return render(request,"f-pension.html",{'v1':salary,'v2':rate,'e2':e2})
  
    if rate>30:
        e2="family pesion rate must be less then 30%"
        return render(request,"f-pension.html",{'v1':salary,'v2':rate,'e1':e1})



    
    familyPensionAmount= ( salary * rate )/100
    familyPensionAmount=round(familyPensionAmount,2)
    return render(request,"f-pension.html",{'familyPensionAmount':familyPensionAmount,'v1':salary,'v2':rate})

def resetfp(request):
    v1=""
    v2=""
    familyPensionAmount=""
    return render(request,"f-pension.html",{'familyPensionAmount':familyPensionAmount,'v1':v1,'v2':v2})



def pageploan(request):
    return render(request,"index.html")

def pl(request):
    p1=int(request.GET["amt1"])
    ai1=eval(request.GET["rat1"])
    n1=int(request.GET["mnt1"])
    
    if p1<0:
        e1="Please provide valid amount"
        return render(request,"index.html",{'e1':e1,'v1':p1,'v2':ai1,'v3':n1})
        
    if p1<10000:
        e2="Amount must greter then 10,000"
        return render(request,"index.html",{'e2':e2,'v1':p1,'v2':ai1,'v3':n1})
    
    if p1>1000000:
        e3="Amount should be less then 10,00,000"
        return render(request,"index.html",{'e3':e3,'v1':p1,'v2':ai1,'v3':n1})
    
    if ai1<0:
        e4="Interst rate must not be negitive"
        return render(request,"index.html",{'e4':e4,'v1':p1,'v2':ai1,'v3':n1})
    if ai1<1:
        e5="Interst rate should not be greater then 1%"
        return render(request,"index.html",{'e5':e5,'v1':p1,'v2':ai1,'v3':n1})
    
    if ai1>30:
        e6="Interst rate should not be greater then 30%"
        return render(request,"index.html",{'e6':e6,'v1':p1,'v2':ai1,'v3':n1})
    
    if n1<0:
        e7="Place provide valid tenure"
        return render(request,"index.html",{'e7':e7,'v1':p1,'v2':ai1,'v3':n1})
    
    if n1<1:
        e8="loan tenure starts from 1"
        return render(request,"index.html",{'e8':e8,'v1':p1,'v2':ai1,'v3':n1})

    r1=ai1/(12*100)
    e1=p1*r1*((1+r1)**n1)/((1+r1)**n1-1)
    e1=round(e1,2)
    ans2=(e1*n1)-p1
    ans2=round(ans2,2)
    ans3=ans2+p1
    ans3=round(ans3,2)
    return render(request,"index.html",{'EMI1':e1,'ti1':ans2,'ta1':ans3,'v1':p1,'v2':ai1,'v3':n1})

def resetpl(request):
    v1=""
    v2=""
    v3=""
    EMI1="" 
    ti1=""
    ta1=""
    e=""
    return render(request,"index.html",{'v1':v1,'v2':v2,'v3':v3,'EMI':EMI1,'ti':ti1,'ta':ta1,'e':e})


def pagehloan(request):
    return render(request,"index1.html")

def hl(request):
    p=int(request.GET["amt"])
    ai=eval(request.GET["rat"])
    n=int(request.GET["mnt"])
    
    if p<100000:
        e6="Amount should not be less then 1,00,000"
        return render(request,"index1.html",{'v1':p,'v2':ai,'v3':n,'e6':e6})
 
    if ai<0:
        e2="Please provide valid value for intrest rate "
        return render(request,"index1.html",{'v1':p,'v2':ai,'v3':n,'e2':e2})
    
    if ai<8:
        e3="intrest rate should not be less then 8%"
        return render(request,"index1.html",{'v1':p,'v2':ai,'v3':n,'e3':e3})
        
    if n<0:
        e5="Please provide valid value for tenure,which should not be negitive"
        return render(request,"index1.html",{'v1':p,'v2':ai,'v3':n,'e5':e5})  
   
    r=ai/(12*100)
    e1=p*r*((1+r)**n)/((1+r)**n-1)
    e1=round(e1,2)
    ans2=(e1*n)-p
    ans2=round(ans2,2)
    e=""
    ans3=ans2+p
    ans3=round(ans3,2)
    return render(request,"index1.html",{'e':e,'EMI':e1,'ti':ans2,'ta':ans3,'v1':p,'v2':ai,'v3':n})


def resethl(request):
    v1=""
    v2=""
    v3=""
    EMI="" 
    ti=""
    ta=""
    e=""
    return render(request,"index1.html",{'e':e,'v1':v1,'v2':v2,'v3':v3,'EMI':EMI,'ti':ti,'ta':ta})




def brok(request):
    return render(request,"invest.html")

def broker(request):
    ss1=int(request.GET["sh"])
    by1=int(request.GET["by"])
    sl1=int(request.GET["se"])
     
    if ss1<1:
        e1="Please provide valid number of shares"
        return render(request,"invest.html",{'e1':e1,'v1':ss1,'v2':by1,'v3':sl1})
    
    if by1<0:
        e2="Buying price should not be negitive"
        return render(request,"invest.html",{'e2':e2,'v1':ss1,'v2':by1,'v3':sl1})
    
    if sl1<1:
        e3="Selling price should not be negitive"
        return render(request,"invest.html",{'e3':e3,'v1':ss1,'v2':by1,'v3':sl1})
   
    br=((ss1*by1)+(ss1*sl1))
    br=round(br,2)
    an2=br*0.05
    an2=round(an2,2)
    return render(request,"invest.html",{'Ans':an2,'v1':ss1,'v2':by1,'v3':sl1})
 
def resetbroker(request):
    e1=""
    e2=""
    e3=""
    an2=""
    v1=""
    v2=""
    v3=""
    return render(request,"invest.html",{'Ans':an2,'v1':v1,'v2':v2,'v3':v3,'e1':e1,'e2':e2,'e':e3})
    


def rein(request):
    return render(request,"roi.html")

def returnonin(request):
    amtin=int(request.GET["amin"])
    amtre=int(request.GET["amre"])
    
    if amtin<0:
        e1="Please provide valid input"
        e2=""
        ans1=""
        ans2=""
        return render(request,"roi.html",{'a3':amtin,'a4':amtre,'e1':e1})
    
    if amtre<0:
        e2="Please provide valid input"
        return render(request,"roi.html",{'a3':amtin,'a4':amtre,'e2':e2})
        
    ans1=amtre-amtin
    ans1=round(ans1,2)

    ans2=((amtre-amtin)/amtin)*100
    
    ans2=round(ans2,2)
    a3=amtin
    a4=amtre
    e1=""
    e2=""
    return render(request,"roi.html",{'a3':a3,'a4':a4,'A1':ans1,'A2':ans2,'e1':e1,'e2':e2})

def resetROI(request):
    a3=""
    a4=""
    A1=""
    A2=""
    return render(request,"roi.html",{'a3':a3,'a4':a4,'A1':A1,'A2':A2})


def pagehelp(request):
    return render(request,"help.html")

def pageabout(request):
    return render(request,"about.html")





