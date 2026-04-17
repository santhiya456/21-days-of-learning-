units=350
if units<=100:
    bill=units*2
elif units<=300:
    bill=(100*2)+(units-100)*3
else:
      bill=(100*2)+(200*3)+(units-300)*5
bill=bill+100 
if bill>100:
    discount=bill*0.05
else:
    discount=0
final_bill=bill-discount
print("Units:",units)
print("Bill before discount:",bill)
print("Discount:",discount)
print("Final Bill:",final_bill)
        
