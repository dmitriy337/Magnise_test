## Test task for Magnise company

### For start:
```docker-compose up```

### Usage
1. ##### Create new user:

​	curl --location --request POST 'localhost:6999/users/create-user' \
​					--header 'Content-Type: application/json' \
​					--data-raw '{
​					    "username": "test_username8",
​					    "email": "test9@mail.com",
​					    "password": "password"
​					}'

2. ##### Update password:

   curl --location --request PUT 'localhost:6999/users/update-password' \

   ​		--header 'Content-Type: application/json' \

   ​		--data-raw '{

   ​		    "id": 145,

   ​		    "password":"new_pass"

   ​		}'

3. ##### Get user list: 

   curl --location --request GET 'localhost:6999/users/get-user-list'

4. ##### Delete user:

   curl --location --request DELETE 'localhost:6999/users/delete-user/145/'

5. ##### Search:

   curl --location --request POST 'localhost:6999/users/search/' \

   --header 'Content-Type: application/json' \

   --data-raw '{

   ​    "email": "test8",

   ​    "username": "test_"

   }'

   ###### These fields are available for search:

   ​	Id, email, username

​	![image-20211117110739121](/Users/vuhiza/Library/Application Support/typora-user-images/image-20211117110739121.png)

