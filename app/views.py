from django.shortcuts import render, redirect
import mysql.connector
import re 
import os
from django.core.files.storage import default_storage
from werkzeug.utils import secure_filename
# Create your views here.


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mpwb06_2023"
)

#==================================================== HOME PAGE ==============================================================================
def home(request):
    return render(request, 'home.html')



#==================================================== SELLER PAGE =============================================================================
def seller_login(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM seller WHERE email = %s AND password = %s" , (email, password))
        account = cursor.fetchone()
        if account:
            global SellerId, UsedName, EmailId
            SellerId = account[0]
            UsedName = account[1]
            EmailId = account[2]
            
            return redirect('/seller_addre')
        else:
            msg2 = 'Incorrect username/password! Please login with correct credentials'
            return render(request, 'seller_login.html', {'msg': msg})
    return render(request, 'seller_login.html')

#==================================================== SELLER - VIEW PROFILE =============================================================================
def seller_addre(request):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM seller WHERE email=%s", (EmailId,))
    seller_info = cursor.fetchall()
    print("seller_info:", seller_info)
    cursor.close()
    seller_info = seller_info
    return render(request, 'seller_addre.html', {'seller_info': seller_info})
    # else:
    #     seller_info = ""     
    # return render(request, "seller_addre.html", {'seller_info': seller_info}) 


#==================================================== SELLER - UPDATE PROFILE =============================================================================
def seller_addres(request):
    if request.method == 'POST' and 'takeid' in request.POST:
        takeid = request.POST.get('takeid')
        resid = takeid
        resname = request.POST.get('resname')
        resloc = request.POST.get('resloc')

        cursor = mydb.cursor()
        cursor.execute("UPDATE seller SET resid=%s, resname=%s, resloc=%s WHERE rid=%s", (resid, resname, resloc, takeid))
        mydb.commit()
        cursor.close()
        msg= "Updated Profile"
        seller_info = get_seller_info()
        return render(request, 'seller_addre.html', {'msg': msg})

def get_seller_info():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM seller WHERE email=%s", (EmailId,))
    seller_info = cursor.fetchall()
    cursor.close()
    return seller_info

#==================================================== SELLER - ADD FOODS =============================================================================
def seller_addfoods(request):
    if request.method == "POST":
        fimage = request.FILES['fimage']
        fname = request.POST.get('fname')
        fdesc = request.POST.get('fdesc')

        fnam = secure_filename(fimage.name)
        print("fnam:", fnam)
        file_path = os.path.join("static/uploads/", fnam)
        print("file_path:", file_path)
        default_storage.save(file_path, fimage)

        cursor = mydb.cursor()
        cursor.execute("INSERT INTO foods (resid, resname, resloc, fimage, fname, fdesc, T1, T2, T3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (get_seller_info()[0][6], get_seller_info()[0][7], get_seller_info()[0][8], file_path, fname, fdesc, 'Available', 'Available', 'Available'))
        mydb.commit()
        cursor.close()
        msg="Food Added Successfully"
        return render(request, 'seller_addfoods.html', {'msg': msg})
    return render(request, 'seller_addfoods.html')

#==================================================== SELLER - ALL BOOKINGS =============================================================================
def seller_bookings(request):
    msg = ''
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM booktable WHERE resid=%s", (SellerId,))
    foods_data = cursor.fetchall()
    cursor.close()
    return render(request, 'seller_bookings.html', {'foods_data': foods_data})

#==================================================== SELLER - ALL BOOKINGS =============================================================================
def seller_updatebookings(request):
    msg = ''
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM booktable WHERE resid=%s", (SellerId,))
    foods_data = cursor.fetchall()
    cursor.close()
    return render(request, 'seller_updatebookings.html', {'foods_data': foods_data})

#==================================================== SELLER - ALL UPDATE BOOKINGS =============================================================================
def seller_updatebookingsss(request):
    if request.method =="POST" and 'fid' in request.POST and 'userid' in request.POST and 'resid' in request.POST:
        fid = request.POST.get('fid')
        userid = request.POST.get('userid')
        resid = request.POST.get('resid')

        cursor = mydb.cursor()
        cursor.execute("DELETE FROM booktable WHERE resid=%s", (resid,))
        mydb.commit()
        cursor.execute("UPDATE foods SET T1 = 'Available', T2 = 'Available', T3 = 'Available' WHERE T1 IS NOT NULL OR T2 IS NOT NULL OR T3 IS NOT NULL AND resid=%s", (resid,))
        mydb.commit()
        cursor.close()
        return render(request, 'seller_updatebookings.html')

#==================================================== USER PAGE =============================================================================
def user_login(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s AND password = %s" , (email, password))
        account = cursor.fetchone()
        if account:
            global UsedNames, EmailIds
            UsedNames = account[1]
            EmailIds = account[2]
            
            return redirect('/user_allfood')
        else:
            msg = 'Incorrect username/password! Please login with correct credentials'
    return render(request, 'user_login.html', {'msg': msg})

#==================================================== USER - ALL FOODS DISPLAY =============================================================================
def user_allfood(request):
    msg = ''
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM foods")
    foods_data = cursor.fetchall()
    cursor.close()
    return render(request, 'user_allfood.html', {'foods_data': foods_data})

#==================================================== USER - BOOK TABLE =============================================================================
def book_table(request):
    if request.method == 'POST' and 'resid' in request.POST and 'resname' in request.POST and 'resloc' in request.POST:
        resid = request.POST.get('resid')
        resname = request.POST.get('resname')
        resloc = request.POST.get('resloc')
        fid = request.POST.get('fid')
        food = request.POST.get('food')
        table = request.POST.get('table')
        dateandtime = request.POST.get('dateandtime')

        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM booktable WHERE fid=%s AND food=%s AND `table`=%s AND dateandtime=%s", (fid, food, table, dateandtime))
        existing_booking = cursor.fetchone()

        if existing_booking:
            msg = 'Table already booked for the selected date and time!'
            return render(request, 'user_allfood.html', {'fid': fid, 'msg': msg})

        cursor.execute("INSERT INTO booktable (resid, resname, resloc, userid, fid, food, `table`, dateandtime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (resid, resname, resloc, EmailIds, fid, food, table, dateandtime))
        mydb.commit()
        update_query = "UPDATE foods SET {} = %s WHERE resid = %s AND fname = %s".format(table)
        cursor.execute(update_query, (table, resid, food))
        mydb.commit()
        cursor.close()
        return redirect('/user_bookings')

    return render(request, 'user_allfood.html')


#==================================================== USER - ALL BOOKINGS =============================================================================
def user_bookings(request):
    msg = ''
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM booktable WHERE userid=%s", (EmailIds,))
    foods_data = cursor.fetchall()
    cursor.close()
    return render(request, 'user_bookings.html', {'foods_data': foods_data})



#==================================================== REGISTER PAGE ==========================================================================
def register(request):
    msg = ''
    if request.method == 'POST':
        # Create variables for easy access
        selloruser = request.POST.get('selloruser')
        usedname = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        mobile = request.POST.get('mobile')
        
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,10}$"
        pattern = re.compile(reg)
        cursor = mydb.cursor()
        # Check if account exists using MySQL)
        query = 'SELECT * FROM {} WHERE email = %s'.format(selloruser)
        cursor.execute(query, (email,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', usedname):
            msg = 'Usedname must contain only characters and numbers!'
        elif not re.search(pattern,password):
            msg = 'Password should contain atleast one number, one lower case character, one uppercase character,one special symbol and must be between 6 to 10 characters long'
        elif not usedname or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into employee table
            query2 = 'INSERT INTO {} VALUES (NULL, %s, %s, %s, %s,%s, NULL, NULL, NULL)'.format(selloruser)
            cursor.execute(query2, (usedname, email, password, dob, mobile))
            mydb.commit()
            msg = 'You have successfully registered! Please proceed for login!'
            return render(request, '{}_login.html'.format(selloruser), {'msg': msg})
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
        return msg
    return render(request, "register.html", {'msg': msg})
