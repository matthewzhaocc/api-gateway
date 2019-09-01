import mysql.connector

db = mysql.connector.connect(
    host = '10.20.0.171',
    user='matthew',
    passwd='YYq#^wy^cZ$&7vRS%_^Lz*Ld%LvRkU@*PsD_7S+PhNu@EhWztE5f2jth+Xw-hsM6g^G@Yq!9*-DBCYU8hQ*HcQVRThcB#b3^%$z5BA27XmK_LY3%AbXwGcD7dvhxV%wKA-DXYx3BCymn2rnyKL7=VE$8CH2k43sJT&cAGep$=X_$mCa!#48G#%BALQWsLD#=9QPek-EG!H$SkN+Yvy%5%XUns4gyfHQqR-9X$mcT?J@VJH_%pn&-6!^PyYqQspxwQv4FAB2C_+!sRs2mab#dw@uPprA8*V!#=g+7TqwQa??-#MWVtkP^%qfddbcAMWwd+d77g+cRDwKX2hrqH!A3-Z-z%2FXf6pj9XSadryh8f46dHSSvN3Z!FtRZC=J=-N#3k3XBG3%Pex9QkfAG5bK=&jJJ-RQmZWp^k9pXPtQ_Gr8RTFJy-?Z%+zqcL?#6pWE6-HHN2ELF_qMjrZaRqYrjUyt#?vg-DrMSK%LT8tA$3hd6CQGMGP&Cdn8_!#2x$Uuv--_!uh?@aJz32TuzN2WhyuKrH*$gxgZ5BA8MJ@vF@kL@AE6Ws&HFMhcyn&W?cq5*fQGRhEKqQQ3qKZpm9C9PGPA@xA?TCrUwEKMQD-W^Q%zEraZ9CSN@Qej7MAn++!9@zYh#wLZ4%Dq9Qj_pV@Xk8LCy?66b5NxS-Dp#LNeBwTFzB$WRKjBKjwUAEra&a&zaT?uU?yr7SneRCZS%ap$3G#TfJ%&3mGFbCK?rK3SK_9Q6e52eARFm6RN-tRhb*X#rrfR@Syw96-qR262Ah6?Fj68K*Jybq@9AfRRahC2b7?WMEF7Qrd&W?ScVKhm?2n^F3FeXMp8B&!^*M-k*Uxg-!%yUVzndQAgm^8Y=2k?u&8s4jx-G5h6M=M3gUShqF8_XksKCzg4!BhsN^MfXu3P_?xTH?CDe8$*LEz6cKmEfjHg*2=%!b2AArATzL?*je*?^rh!JvWbswbPvV*Juu&5jcU4qKYv7QZ4X$kM6&H=BEvL#7a_x9nynF5#ArsF!zdJ',
    database='apikey'
)

def new_user(name, apikey):    
    cursor = db.cursor()
    template = 'insert into apikeys (apikey, name) values (%s,%s)'
    value = (apikey, name)
    cursor.execute(template, value)
    db.commit()

def check_user(apikey):
    cursor = db.cursor()
    template = 'select name from apikeys where apikey = %s;'
    val = (apikey,)
    cursor.execute(template, val)
    result = cursor.fetchall()
    if result:
        return result[0][0]
    else:
        return None

