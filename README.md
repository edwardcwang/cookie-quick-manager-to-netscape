A script to convert JSON exports from Cookie Quick Manager for Firefox into the Netscape cookies format.

Once the cookies have been converted, you can use them in `http.cookiejar` as follows.

```python
s = requests.Session()
cj = http.cookiejar.MozillaCookieJar("mozilla.txt")
cj.load()
s.cookies = cj  # type: ignore
```

https://github.com/ysard/cookie-quick-manager

https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/
