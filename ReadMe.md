### 域名whois查询

---

刚接触python时候写的代码，原理是通过socket向WhoisServer请求数据，然后通过re分割。理论上可以用于所有新顶级域的批量查询。
现在看来将接受信息通过“:”分割组成字典似乎是更高校的方式。

其中

`domains.txt`为待查询域名，自动生成‘result.txt’，查询字段为Domain Name、Registrant Phone、Registrant Email、Admin Name。