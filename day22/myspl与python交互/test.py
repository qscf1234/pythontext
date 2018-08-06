from sunckSql import SunckSql

s = SunckSql("localhost", "root", "root", "kaige")

res = s.get_all("select * from bandcard where money>400")
for row in res:
    print("%d--%d" % (row[0], row[1]))
