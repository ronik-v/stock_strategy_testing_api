# Stock strategy testing web api
<div>
    <ul>
        <div class="details">
                <li>
                    <h3>Details</h3>
                    <div>
                        <b>Oversimplistic asynchronous web api for receiving data from the Moscow Exchange (<a href="https://www.moex.com/">MOEX</a>)</b>
                        <p>Through it you can get data on financial instruments, that is, prices (json): opening, closing, minimum prices, maximum prices.</p>
                        <p>You can also get indicators: <em>MACD, SIGNAL, SMA5, SMA12, EMA5, EMA12, VOLATILITY</em>.</p>
                    </div>
                </li>
                <li>
                    <h3>Using the api</h3>
                    <p>Request for get ticker data at 2022-05-01 to 2023-09-26:</p>
                    <div>
                        <pre>from requests import get<br>data = get('http://127.0.0.1:9999/api_sst/data/GAZP/2022-05-01/2023-09-26').json()<br>print(data)</pre>
                    </div>
                    <div>
                        <p>Request for strategy testing at 2022-05-01 to 2023-09-26:</p>
                        <pre>from requests import get<br>sst_strategies = get('http://127.0.0.1:9999/api_sst/strategy/GAZP/2022-05-01/2023-09-26').json()<br>print(sst_strategies)</pre>
                    </div>
                </li>
                <li>
                    <h3>Libraries to install</h3>
                    <a href="requirements.txt">requirements</a>
                    <p>You may use command for install all:</p>
                    <pre>pip install -r requirements.txt</pre>
                </li>
                <li>
                    <h3>Docker</h3>
                    <a href="Dockerfile">file is here</a>
                </li>
        </div>
    </ul>
</div>