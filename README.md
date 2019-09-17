# Live_broadcast_danmaku_simulator

<p>
    <img src="dd_center.png"/>
</p>

### ⚡️Quick start
Get the value of SESSDATA and csrf from your cookies first. Then, at this part, add the values of your_SESSDATA, your_csrf, and roomid
```
def print_target_message(meg):
	os.system(f"node ./bilibili-live-danmaku-api/stdio.js your_csrf your_SESSDATA roomid {meg}")
```

After that, run
```
npm install got
```
At last, run 
```
python3 simulator.py
```
That's it.
