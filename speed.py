# pip install pyspeedtest
# pip install speedtest
# pip install speedtest-cli


import speedtest

speedTest = speedtest.Speedtest()
print(speedTest.get_best_server())


print(speedTest.download())
print(speedTest.upload())

import pyspeedtest
st = pyspeedtest.SpeedTest()
st.ping()
st.download()
st.upload()