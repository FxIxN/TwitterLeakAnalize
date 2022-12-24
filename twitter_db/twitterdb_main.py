import json
import sqlite3

def main():
    # функии
    inserting(sq_conn_cur(), sq_conn_cur())

def sq_conn_cur():
    conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\twitter.db')
    cur = conn.cursor()
    return conn, cur

def inserting(conn, cur):
    with open(r'D:\projects\dbase\twitter.json') as tw_file:
        try:
            tw_str = tw_file.readline()
            while tw_str:
                tw = json.loads(tw_str)
                tw_str = tw_file.readline()

                if tw['url'] == None:
                    tw['url'] = ""

                query = (f"INSERT INTO accounts(twitter_id, name, location, description, followers, friends, listed, created_at, favourites, statuses, email, url) VALUES(" + str(tw.get('id')) + "," + "'" + tw.get('name') + "'" + "," + "'" + tw.get('location') + "'" + "," + "'" + tw.get('description') + "'" + "," + str(tw.get('followers_count')) + "," + str(tw.get('friends_count')) + "," + str(tw.get('listed_count')) + "," + "'" + str(tw.get('created_at')) + "'" + "," + str(tw.get('favourites_count')) + "," + str(tw.get('statuses_count')) + "," + "'" + tw.get('email') + "'" + "," + "'" + tw.get('url') + "'" + ");")

                cur.execute(query)
                conn.commit()
                # print(id, name, location, description, followers, friends, listed, created_at, favourites, statuses, email)
        except:
            print("Warning: query - " + query + " not work!")

if __name__ == "__main__":
    main()


