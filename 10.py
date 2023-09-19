day = int(input('Input birthday:'))
month = input('Input month of birth (e.g. march, july etc):')
if((month == 'March' and day >= 21) or (month == 'April' and day <= 19)):
    print('Your Astrological sign is: Aries')
if((month == 'April' and day >= 21) or (month == 'May' and day <= 20)):
    print('Your Astrological sign is: Taurus')
if((month == 'May' and day >= 21) or (month == 'June' and day <= 21)):
    print('Your Astrological sign is: Gemini')
if((month == 'June' and day >= 22) or (month == 'July' and day <= 22)):
    print('Your Astrological sign is: Cancer')
if((month == 'July' and day >= 23) or (month == 'August' and day <= 22)):
    print('Your Astrological sign is: Leo')
if((month == 'August' and day >= 23) or (month == 'September' and day <= 22)):
    print('Your Astrological sign is: Virgo')
if((month == 'Septenber' and day >= 23) or (month == 'October' and day <= 23)):
    print('Your Astrological sign is: Libra')
if((month == 'October' and day >= 24) or (month == 'November' and day <= 22)):
    print('Your Astrological sign is: Scorpio')
if((month == 'November' and day >= 23) or (month == 'December' and day <= 21)):
    print('Your Astrological sign is: Sagittatius')
if((month == 'December' and day >= 22) or (month == 'January' and day <= 19)):
    print('Your Astrological sign is: Capricorn')
if((month == 'January' and day >= 20) or (month == 'February' and day <= 18)):
    print('Your Astrological sign is: Aquarius')
if((month == 'February' and day >= 19) or (month == 'March' and day <= 20)):
    print('Your Astrological sign is: Pisces')