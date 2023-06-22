import psycopg2

#Connecting postgres and running the script
try:
    connection = psycopg2.connect(user="postgres", password="cimcon@123", host="35.226.41.240", port="5432", database="thingsboard")
    cursor = connection.cursor()

    #Using the script to run in pgsql
    with open('/home/chirag/script.sql', 'r') as script_file:
        script = script_file.read()

    cursor.execute(script)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
    print("Inactivity timeout updated successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)
