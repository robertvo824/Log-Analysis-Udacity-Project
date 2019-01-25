# !/usr/bin/env python
import psycopg2

# connect to db
db = psycopg2.connect('dbname=news')
c = db.cursor()


def popular_three_articles():

    query = """
            SELECT articles.title, count(*) AS views
            FROM   log,
                   articles
            WHERE  log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3;
    """
    c.execute(query)
    results = c.fetchall()

    print('\n1) What are the most popular three articles of all time?\n')

    for result in results:
        print('"{}" - {} views'
              .format(result[0], result[1]))


def popular_authors():

    query = '''
            SELECT authors.name, count(*) AS views
            FROM log, articles, authors
            WHERE log.path = '/article/' || articles.slug
            AND articles.author = authors.id
            GROUP BY authors.name
            ORDER BY views DESC;
    '''

    c.execute(query)
    results = c.fetchall()

    print('\n2) Who are the most popular article authors of all time?\n')

    for result in results:
        print('{} - {} views'.format(result[0], result[1]))


def requests_errors():

    query = """
            WITH requests AS (
                SELECT date(TIME) AS day, count(*)
                FROM log
                GROUP BY day
                ORDER BY day
              ), errors AS (
                SELECT date(TIME) AS day, count(*)
                FROM log
                WHERE status LIKE '404%'
                GROUP BY day
                ORDER BY day
              ), error_rate AS (
                SELECT requests.day,
                  CAST(errors.count AS float) / CAST(requests.count AS float) * 100
                  AS error_percent
                FROM requests, errors
                WHERE requests.day = errors.day
              )
            SELECT * FROM error_rate WHERE error_percent > 1;
    """
    c.execute(query)
    results = c.fetchall()

    print('\n3) On which days did more than 1% of requests lead to errors?\n')

    for result in results:
        print('{} - {}\n'.format(result[0].strftime('%B %d, %Y'), str(round(result[1], 1)) + '% errors'))


if __name__ == '__main__':
    popular_three_articles()
    popular_authors()
    requests_errors()
