from datetime import datetime
now = datetime.now()
var = now.strftime("%Y-%m-%d-%H:%M:%S")
var = "webstatic_" + var + ".tgz"
print(var)
