import sqlHandel

conn = sqlHandel.MSSQL("10.0.0.53", "patching", "Patching123", "patching")

servers = conn.getServers

print(servers)