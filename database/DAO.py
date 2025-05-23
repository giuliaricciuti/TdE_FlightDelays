from database.DB_connect import DBConnect
from model.airport import Airport
from model.arco import Arco


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
    def getAllNodes(nMin, idMapAirports):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT t.ID, t.IATA_CODE, count(*) as N
                    FROM (SELECT a.ID, a.IATA_CODE , f.AIRLINE_ID, count(*)
                    FROM airports a, flights f 
                    WHERE a.ID = f.ORIGIN_AIRPORT_ID or a.ID = f.DESTINATION_AIRPORT_ID 
                    GROUP BY a.ID, a.IATA_CODE , f.AIRLINE_ID) t
                    GROUP BY t.ID, t.IATA_CODE
                    having N >= %s
                    order by N asc"""

        cursor.execute(query, (nMin,))

        for row in cursor:
            result.append(idMapAirports[row["ID"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesV1(idMapAirports):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID , count(*)
                    FROM flights f 
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID
                    order by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID """

        cursor.execute(query)

        for row in cursor:
            # result.append(idMapAirports[row["ORIGIN_AIRPORT_ID"]],
            #               idMapAirports[row["ORIGIN_AIRPORT_ID"]],
            #               row["n"])

            result.append(Arco(idMapAirports[row["ORIGIN_AIRPORT_ID"]],
                           idMapAirports[row["ORIGIN_AIRPORT_ID"]],
                           row["n"]))

        cursor.close()
        conn.close()
        return result