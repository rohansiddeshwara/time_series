import nsetools
import os
import smtplib



def get_data():
    data=nse.get_quote("SBIN")
    msg=str(data['buyQuantity1'])
    quantity=data['quantityTraded']
    avg_price=data['averagePrice']
    date_time=data['secDate']

    m=f"quantityTraded ={quantity} ,\n average price = {avg_price},\n date time = {date_time}"
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login("rohansiddeshwara02@gmail.com","olwbghisbdgqtzeg")
        smtp.sendmail("rohansiddeshwara02@gmail.com","rohansiddeshwara@gmail.com",m)


if __name__=="__main__":
    nse=nsetools.nse.Nse()
    get_data()