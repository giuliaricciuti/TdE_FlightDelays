from database.DB_connect import DBConnect
from model.airport import Airport


class DAO():

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAirportsAirline():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID, f.AIRLINE_ID
                    FROM flights f"""

        cursor.execute(query)

        for row in cursor:
            result.append((row[0], row[1], row[2]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchiPeso(ORIGIN_ID, DESTINATION_ID):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT COUNT(*)
                    FROM flights f 
                    WHERE (f.ORIGIN_AIRPORT_ID = %s AND f.DESTINATION_AIRPORT_ID = %s)
                    OR (f.DESTINATION_AIRPORT_ID = %s AND f.ORIGIN_AIRPORT_ID=%s)"""

        cursor.execute(query, (ORIGIN_ID, DESTINATION_ID, DESTINATION_ID, ORIGIN_ID))

        for row in cursor:
            result.append((row))

        cursor.close()
        conn.close()
        return result[0][0]


    @staticmethod
    def getNumVoli(airport_id):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT a.ID , COUNT(*) as N
                    FROM flights f , airports a 
                    WHERE (a.ID = f.ORIGIN_AIRPORT_ID OR a.ID = f.DESTINATION_AIRPORT_ID)
                    AND a.ID = %s
                    GROUP BY a.ID """

        cursor.execute(query, (airport_id,))

        for row in cursor:
            result.append((row))

        cursor.close()
        conn.close()
        return result[0][0]