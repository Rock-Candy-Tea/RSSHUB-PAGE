
---
title: 'TS入门篇 _ 详解 TypeScript 类类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2563'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 18:05:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=2563'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADsAAAA6CAYAAAAOeSEWAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAABkLSURBVGhDtZoHnJ1llcbP3Om9ZiYzmfSQhCQQIbRQVQKI9CYC68qKriJK0UXcZRcINqStIoiIqKCi1NACQihBWiCkkJ5MJlMyvd7p7d759v989/sy34yTbIj48Atz71ff855znvOc971xDrB/EtoGI7a9Z8Aq+wZML0mNj7dE95NZ1OKsj1dHo1GbnJpss9OTbWJyonvun4VP1Njuoagtb+m0it4By0iIt8LEeMvkr8XFWcfgkA1gYDLf47i2PzpsyU7UspKSLDoctagTZ7Vc08MzClMS7awJ2ZaflBB78CeET8TYla1dtrKt2w5KS7YCDGzEoz2RqKUmhGw6x2bhuXyOp2BoRXef1Q1E7Lj8TIsMD1sbxu1kcnYSAX1810RMTUmyMB7f2j1gC7NS7byinNiL/kH8Q8a+2NRh77b32El56VaPAe0YeGR2mh2bm+FdMRqP1rbZe+3dFsHT35qcb/Oz0rwzo7Gxs9feYPLS4kM2h8lawee5hPmlJXneFQeGAzJ2F564v7rFzi7Msu3d/Xgjzq5g8ArX8VCNN2vJ28daey0zZJabmGCLslP5HOf+Oygr3UzDGOf+JxrauXfQjslJt+dbuuyMgiwmk+sPAB/b2Lt2NdoMZnuY21qHIvbvUyZ4Z0ZQiXGrWjvsmPxsK4R0nmHA8ZCTQvxVQn5eRipklIBtcVbV1WtHYsjati47ZWKuTUpP9Z4yGk/xDBGe3v1mW4/dOrvYO7P/2G9jRSjf31FnXyaUXiB8r51WaJkM3kcfOSa2FR6qarIenooTLQHPLcC4mYThyw1tVpKWYlVERlZ8nC3Oz3Jzdn1nn5uvQ8OOHYvhR/CvsqffJbkCkZTvcYZ6Z0WTfTovw5Y1dtjXp+TbFPhgf7FfxpYxuMfr2uwo8rEtMmwXF+d6Z8wGmIR2PLyjo8cqOFffP2SLGexJEJCP9R29thkPXlpa4A5Y3w/jmuVNYYwO2QkY7WMtz3mVcE1hkualJdmSolzX8GnpKd4VZq80d1o7zN0RdWxGaqItgbn3B/+vsasgh/UMNBOvzYMZDxtDKp289KGaVguFQvb1yQWWwuB97GaSXqUUnVaYbSUwrDCEBz/C2CM8EhNrP13fbkeSh3OJgCAe2N1CWXKsGOc6TOr5U4q8MwYhDtkTda02MyPN+nnGBQEH7A37NHYz5KOZVv08qyjbSseEzKauPnsMj98wc6Ibcj5UUv7M8QWZTE52jEwGOVaD8U1Dw1YNWX0qM8VKyb80L/TrOPYOzH4KBJQTrK8M7+7KZjuM63sHBt17FubGoibCuf+tarWFGUmuwWeT8/vCXo1tZOYeZcazCaez8MwEzzM+HqhqtiJI5twxL1jeGLYk7jmKMF1JOCbg6Qj5nAdRqX7q3BYm8VAmQvW1lfcMc58IT95uIA3q+gftrDHPXUXJWkVEHJme5Bp5UmHsvIZ/O3l8ECE/FWcsItX2hr0ae8O2Wjs+J43QTbOZzGYQ/7Wtxq6eXjRK3r0By4YJ6Ty8EiYSJqcm2eGeV4Pox/ANENJR49RiEdfqcLflUJrEBZqgxYHrBjn2ExFURqKdVETN9YirJxKxR2rbrYeQv5ISmB6IsiDGNfZGWPeMgkzr58xnPaJ5p6XDZPKz4T77wayJ7jGhhXLwanOHTWBgq5n5q6YUwNJ7l3kKcRl7OJ7fF56l1GzvHbSD8dghTPi0wIRfv6XafjJ3ssv0PnZQ7nZx/etwzO1zJ3lHR2OETTw8x0tOx1AN3De0D7YV+63oGthjaJQ5Ur7eVVZjcdGInUyuaT73ZWg3efV8fZs7cc2E777Qi5eunVbghvPPymrt/krKGfcLd8ybYjdxrK6333Z09rjHZkNuLYzz0uIc+xWCZzz8nbHbe4dsY1e/XUOY+nimvtUaSazv4jXhaQasSbmYmpuenGwHZ8TKggSEQm08rMD7ahBOoExcMqXQegjnZ+CEvaEa1ZQUQkt39dj0zDS7krq+ARmpdws/nlNqD9WFbWN7l5u3wr9MyrcXKUsqWy3jTOaoML4DdaQ83YIoT4VYpEXvYQZLmbX5SLohBrgOj186Kc/iKTUPUhq+Rrm5ekOl3TWv1Mr6hqwbY0VOQXwEo+Moq4Z47q5qsU489G944LyJOW4LOLZOKtT/iI6+nGe/0dhuEd4ltj2NmiuCU4hnk5fHIi7+RK4uTEu0e+s7rAiRcw1CYy3OejvcYz+eXeI9MYY9nu3lYZl0KavJJ7Vjibzgjp319rUZE20j7CkJqFr5JQYgQ39f3eQaKpQk0afy8nl4uBzvjUUTRk7k3iebOm0pabDiyFn2XGu3dRME41CGVeBVqSiVnc6hIUpekp1VjHLDSOEcQlui5W/U8C7IKREjv1Gabw3wRwUTvpv7jybPtzHmIPZ49q6KRjuccqBQVCOtGvqXhrCFUUXJzOYSHt7Kw5Ix9H08dSje1o1JyL73IYXpEMmE5CRbw6wuykx2pR+Pd6/J4JpLiJKV6N9OnrcQNfQ0Zem6qQX2MmFXyWTE+DMO0kGx4e08DEjnXbsYuOq7niHB8jdY/wQ8Srm2XCZZUrOakF1CY5EKX0h93Tu/1J4kRdbDMT8MamgZK9xe3uDcvrPe++Y4f61rcZr7B53rN1c5N2ytcV5rCrvHt3T2Og19g+5nH7dvq3bqunr4NOwgK2MHA1jeEDuG7HNuLmtw7qpocl5t6nCPvdTQ7v4N4u3WTqeyu9cZHIo4f6lqdFoHh7wzMbzDeeGv3Hvzjlrnh2W1zofhHuftxpFn3VFe7zxS0+p0DlKVPbhhvBxhvwiFMgfP+mjHA08gEC4pybeLyK1iZldh8zC5VJQyUl8l59KZ0WJk2xaiYWxNrkXXJhA8r3PvZRur7ZZZRfadaRPsfiTmX9HGajC2tXd6V8dQTMhX0h8rNdJx9Ra8F8SbRNLzhPRnJmTZIUTYueTyWxyr7uv3rjC3OkzE8495oS+4xq6D5WoI0bO5WVCOSerl8rIeBrOI/Hkaw6ME5W1zSuzx2la3CRdWi3zIG+FDBvUp9LMgI/vggUmE7KkT81yGvOOgEYa/aUahhRAF5xLec3OzbF1r2O17BbVxIi7hzJIC64IYhXdJA+nh/5xVbOmE9J0QqjSxWk0pp37M2YEtgjS8GpimACu7xkqxdKJ6fEXyYl2Lre0ZtC8yELVewtWUnbfCPIhrvgDFz8WI5yhJKgcnFMZWEFrwhgzo5uWDDDA1oGSOzcu0xfx7vTlsv6posIMpJ6cGWPiw/BxL4PU7vbrpjgf8bMdu5OYwOdhm83DARUSa0ELknYIeEAaILuWxlhGa0M8+EuJCrpJT+ymENhN60pXBxa3LZ5TsucnlGaCmIEQ4Evru91yuz0xMtKaeXluI5zdh9Mm8vAlBn4aR07X64EH3vEKdXQkZJXPP/JxMvNRpLxEtHZ5RQgmNewnpouvVTpYTHdfOnmy5kFUGnpRTfEhXD9DiBdFFJB0/YWS9aj6pmc89r0BaQmgTRkgI+EsdKsYasJZOBF+QqTH474NK7LbyBvf7W+RgOxNyxfQY2/2hrp2+NkroxrzrQ55fSZkpJIa28znCgF6rb7H1hOSslATyvNflAh9pvHcX3lVE/Ya8FjTJIexa2Rq77nfU96unTnD7aME3+TAm6BFKYrPnqCNIqV5sq0ZGCiEV+Db+qWMQqpFgb5KPx48R6omeDl2EuP9DTYt9iGA/f1KBS1w/La+H4ktsSmLItvZHXLUkrCeflVtJ9DVVg1H7+sxiGvVM975rZpfabuqHVhuP5F1vewav5O8GamUe91yDanoYw47FWzC929O+DJnKA2opFY1Rjru5CE7kOcO0jJtQVUIynzuZEMeb+1CEOFXN8iFSGeRpCm1BTlJxVg49Azm819SO7Bu0axEbwn27GuxMck+TMQHDP8fn48gfDVIL4R8xKVPJ73MQBUIfA/Z54LMw5vmlE+w+VFo2A78X/SsyPA/RMD0z3e2qVLtfo7aeBslpMX0N0TEnLcUlKym1jyBFqSohmYntI5enBhYB9CY/2kNarhwJhNiMtRGyWnkQdKaCFyQwgydjyNUw4VchKxXv2/DoKdC+lkQbCX1NlKCGvJiBJkSGbCus6jfo4yGBNySgr+u7e20BCsxdVAcFlJ/tHd32+cIsNxSXUULUUx+dg/d47g7OPYFw2MxkSuyMwLHVTI6PBN6dS8Sppw45zHJSgDXV3aQzmz40Z6fDgBfiAXU0uZxby2zejee+j3eltoQMzhV6qSBogXwrEXDj7ElWxUQ8RrnSaoU0dxIsKaiMvMykXTu90NqJsGHP4z78SdLigUrLKat32nFwy/E07pfDFRdQ/7N5r57pQ1482uvWhMGhQcviGkVrKDUp0ToCxfhQal5n4Hs/g1jOgH4LWdwFOd1b1WzHET4vLZppv+Czjxo840OrDlG8jAJzv2tp5mLK1dsU/lfIOeWy5NxFxfl2BoYImlQtx9QF6mJRQKBsQYYuO2yaLYPBUXvu/VqYPxtHhNy7Y4hCkNLGPtKSklzCVKSHtMQxcqm5Kw1DhI2PTGZtcGDAvoLQ/u7MifYtWFBlxz2H9zo8RkwKzC5UYiG+p44ccqE62YAxLeT/TOpf8MXx8Qk0IJFRY1Go+viQVJpE5Ehjf49xfAZeqGIy/7us3nqxwQfCkjZypPxobVr/6YpQHIalUvuCyEwbSXC9PC8QnkFcXlrgLpoLIhIfKuaqlQkYIAwQnr/f3eyu7KttOw2lNpv8/BPHyjzVNER3o72gvEBKqRMTflndbP8BMweRDyeciEj5bFayFXqTLzheivgYJC0jwzwHa0MDDEotm48ndze5BBBElAnxxcRYHAFh3FfZaA9UNRmC354kNwUx8eHkmVj5dcTE5ZMnuEyr1QqlhtaJLuOYZv4v3KNo0TKrGPUZ1NILPKuWcvVn5Trv10SMB6h0j/ARMnlOuafCBIfnSWEx/Raif3HDzofYMM31dOyY9LBaLK3TjoX2fEqT4+2qaUVWSTQvyM6wC8nNJyEetXIyuLKrx04P7MKNnbJZlKUtNAIHo7i2dA/YU3Vtdi5l6jCepXy8hOedSSSsI8/HQg5Q+gxTKXwkMHkbESo+hjG0lbRRzQ3Fc5LOzDuFhs3Ptumpie7ilRDhlEJOq/hjsZljCxjkt7fWuPS/EekpXMggJQIk0G+eN9Xu2VmHWIkJe0nJRN4ptBBit2yutG9ML7J1DHAxebiAMrZ4VZlduqGS8I2tJc2iborUxmIN79c+kTovFxivPvrcSaP3n7RSKYTUmKt4N3rMOcw4JOneD3sP956jNaMglIeTER5Xbdlt15Tm2W10NEsYrA/N5JLCHHsR9tSqwxq08G3bqm1ZTbOtagnbo6SLvH/VzBL7W7jPzqFea0LmMLFzUuLtdwumuO3i1Vtq7OK15Xgw3l1PDmIXak+6QBEkvB9YJIzBcc/L20JIYaSZ/qAzVm5Ut4oowk3QehC+N3xo/1wTqt7zsYawfX9no9XjqdPXVLhrwyo/wucJYQkE1e4j8rLcBuHUItQQKqgMXb6LGvxFQlXw33AdZLR0V5P9Fr29lP73scNnosoyvdWPv4fPJ+uJrLVtMakqaL1M1cTvv0OLIZE6wk2a2IcIRUQh+DaejpdcXepBa7bKDRGM9PIVxTl2EwarZ72rooVuY4RQtMypdk6e1lLLehhY2lt7QEd7WxlCDvdIli6E9B4+ZIodmZEMccUGqgiZOqru9tkR3iJ8nCcXRWRZCSPMLPEjlx2LjQL1OM5qKAm+vhSuRqSfV5Ttrg8FdWcrnhMqCTex7DEM6qTsVEuM1+8hovaHQ6e6a1Fz0xLd3nUt4ToWWuzWNkhcoAIIjUx2ZpxjLzWF9+SYmngR1lok4TEoJxGfuijhI/7OICoFmadl2llcL9b1oRVJtbD+JLlv1KrhHG5811t9ELbzgk14ICUwqE+TDzftqHPz98vUSy3jSIwP8dCpkNqLDPTx+rArz4T5qLG3G2PrvJKKPoLBWE501NC3ilUX5mVjVIb9nIbgWcpPMiSXjbcL8K62UkR86m1/yfkSeMaHFuK04X0CE3J6SWzFUxw0BSNHlSzi3RmIRJwHq5udO3c16quLp6sbnffbupxbt+12vzOrzuvNHc7ycRbIxuJHgYU7YSASdQgxp7qz2ynv6HJeqW91doa7nLruXof+17sqhhu31Xif9o7HalqczV29Dnrb/f5EXZvzdH27U98/6LR5i3N0UM5zjHU71/lwjRWWltU5CAIn7F1MqLp/r9hQ5RoaxG+qmrxP4yNKcfsFLwuiprffeb2l03m2scO5h3Or2rudzjGrhk8x4Cqu2xcexilBvNEcdi5Yu4tKF3Ue4tzPy+td5/1md4tzw5iJ27NuXEYobYUdlb8z6GTWkdxaCvk2zHjd5mpKQ459mv5TkAp6mQb9Aq9HHQ8S6mrZnuc6vUG6WHusIhCJGNXl9byvnJyaiE7+Eoz8c5TYNQiUveENGpJpcIJ+biS8R0+rlcazGNs7pKB+zPLTOSX2KNWhlDAf4r2Spj72JORB5OyHULX+dlD/FOky/HFy5ygYU0sey/i8moeqdunXK1qC3RuaMOYHlI/raQMl3M+EeTV5WxD3Km8a8PkM8nr648sQ9+esKbf5e/nxiKBfAOQkxbv3SU9LYmqPV9V/Pn+V20VwTyVjTqCI6edEQUOFUXs9WmfSll8DyX2dt7GlnwkswaM3l9XZ0oNK3MTXbxpOV2sGk69s6XCJw4cY8KbyRrt9TrHt7Bm0rRBQe1+fHUWNfaapU0KbqxzbORC1M/LS3dJwIl3KOrwykQG/E+61q+isgniztdOKqNOziDgZqZIzFwPvqGiyg5NCtoCqoG5NxHhPZTOsnORulKskjoKMDeLuXQ3OmnC3syxARFXdfc57LR3OrdtrvSOOs55rnqhtcdoGhpxHdjc5EfJUuHZTlftX+G15rXPlhkrnLe59F7Lz8VGHdg8c5y2OLeMZ126qduq9XC3v7nd+FchLvYPJd15gPCu8XQnh/qpm59WGVudZzvvQO97kXTcGxhnEuJvR39tWY8cwK4uhcikk4a3Gdstg9l5B2t0wfaTdWkEou5vCPOV5PH73vFL3+DfXltnh6OxjkJD6Wd5F3g88tMe6CW/7YmI99VIL4u0oqUK8ocW4d8hFrXMVoOQU8s3U97MnjvDD/XRYkyhHM1MT3GVZQR2Tdv70U8EbA5vlo+CaPAaaSWoZXm50otGodxQ6L6txGKxzw5ZYORrBsPPrykZKQIy1n8bTjwb2fO4Te3ue7x6KOKvaYns1wtIddd4nx3mwot55qyl2360cp81zurg+CGqwU8v4/Of5uAVvPgObrwvHomY8jOtZ4fXWLnefdHVXv9044+8ZklCx75DXwcV1Sb27y+vInUQEuVYSaMgRJYfAwtoj0raFxIUW1A8nz35f02qLc9Lc9lG7CBkwtUR7bf+A+5uL6ehnH9Lat+5sIEfj3Cbj3NKRvP7Rjlo7FSmqavKvpSP8MRZ7NVbQYLSkqlC9ZW4sPH18gBTcORjrhMWmQWzFmK2UsvO90qQ1oZcI8UhkCLZPtRqMy0NirobAvjIpb4/sW06qKGyPR2oGIdlazjOOTk+kLYzaaYGSp63Wz6HsXsQ51wd+LTAuZOy+8GBNq7tF+IOdDU4kENJthNID5YRafZtzZ3mDs9LbRgzixcZ2l1h83OKFbDmEd0/FiFp7DWHgp0AQGzq6nf8hPF+oa3EehOz0ziCWcm4NpBRMhX1hn571oR9wqVVSDVPtUi32sQ0vbu7scZdY9aOt2ZSEL9BEBIW+dv20AKDd9/ep09oimYqHpyImkKDuRllS4PrlHNuIqDmCJmNJQba7q1joEaUQJuR/WdXsLrJrq/L6cdJsPOyXscJ7GLKqo8cOpqhrO//yQG6oS3kZwS9xPkRB3wi7diFMtDN+PLk5m1ath+8f0Fy80dbjhvVXub+U5mEqeal27UP+dWpPlknNxW79Ak6/7Tg3UMOF52j1xA1qK7Trd6nXC+8P9ttYQcumIonLSnJtBdJNa77axw1C2x3qR4Wqnj73x9f6MbV+CCYFBZO6y51aSh3gzVrsmwzJnULEbCJC1oZ7vIZ/9Iqmfvn2u5oWO5n8fApxcuWUApum5diPgY9lrA9EtvUNOzYf8vqAcJPsU5iOh7XtXQgt2uZhjKU2amF7HQyfEYWcZk5yQ1RDKNrLcq02k/9IGmldrB93KiokPw8EB2SsoKWXO5FmxXhlckqi+3vEUvLqwok5PHVkIWAszlqzy1p54zuLpnPZ3q9bod08JlLSb5DrNxDm38Sbvsg5EBywsT7oH+3XNW3uasGirFSrxRNdCllKiPZHZzJYLZb5qEcpae3pxMCuu9oibS5/QCOiLcYUrp+MmtJeURjFdVlxzqiae6D4h40NQt54HyGv3JRo10aVfv8YhtC0pSlVKcPFuxIXahr08mzCO4VzMlLSsZuomZ+RaucU0rXsw/sfF5+osUFonWob/7TrLdaUgdpV93fl9X+VIC0Y6tek2uI8OD3J5gT2Vj9ZmP0f4IM4iY7RQ5gAAAAASUVORK5CYII=) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“这是我参与8月更文挑战的第16天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>”</p>
<hr>
<p>传统的面向对象语言都是基于类的，而JavaScript是基于原型的。在ES6中拥有了class关键字，虽然它的本质依旧是构造函数，但是能够让开发者更舒服的使用class了。 TypeScript 作为 JavaScript 的超集，自然也是支持 class 全部特性的，并且还可以对类的属性、方法等进行静态类型检测。下面就来看看 TypeScript 中的类类型。</p>
<h2 data-id="heading-0">一、类的概念</h2>
<h3 data-id="heading-1">1. 类的使用</h3>
<p>在开发过程中，任何实体都可以被抽象为一个使用类表达的类似对象的数据结构，这个数据结构既包含属性，又包含方法。在TypeScript 中可以这样来抽象一个坐标点类：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
  <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
  y: <span class="hljs-built_in">number</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x = x;
    <span class="hljs-built_in">this</span>.y = y;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getPosition</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`(<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.x&#125;</span>, <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.y&#125;</span>)`</span>;
  &#125;
&#125;

<span class="hljs-keyword">const</span> point = <span class="hljs-keyword">new</span> Point(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
point.getPosition()   <span class="hljs-comment">// (1, 2)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里定义了一个 Point 坐标点类，它拥有两个number类型的属性 x 和 y，一个构造器函数和一个getPosition方法。后面通过new实例化了一个Point，并将实例赋值给变量point，最后通过实例调用了类中定义的 getPosition 方法。
​</p>
<p>在ES6之前，需要使用<strong>函数+原型链</strong>的形式进行模拟定义类：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Point</span>(<span class="hljs-params">x, y</span>) </span>&#123;
<span class="hljs-built_in">this</span>.x = x;
  <span class="hljs-built_in">this</span>.y = y;
&#125;

Point.prototype.getPosition = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`(<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.x&#125;</span>, <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.y&#125;</span>)`</span>;
&#125;

<span class="hljs-keyword">const</span> point = <span class="hljs-keyword">new</span> Point(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
point.getPosition()   <span class="hljs-comment">// (1, 2)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开始定义了 Point 类的构造函数，并在构造函数内部定义了 x 和 y 属性，后面通过 Point 的原型链添加了 getPosition 方法。这样也模拟实现了 class 的功能，但是看起来麻烦很多，并且缺少静态类型检测。因此，类是 TypeScript 编程中十分有用且不得不掌握的工具。</p>
<h3 data-id="heading-2">2. 类的继承</h3>
<p>下面来看一下作为面向对象的三大也行之一的继承，在 TypeScript 中，可以使用 extends 关键字来定义类继承的抽象模式：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age: <span class="hljs-built_in">number</span></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.name = name;
      <span class="hljs-built_in">this</span>.age = age;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-attr">job</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age: <span class="hljs-built_in">number</span></span>)</span> &#123;
      <span class="hljs-built_in">super</span>(name, age);
      <span class="hljs-built_in">this</span>.job = <span class="hljs-string">"IT"</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getJob</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.job;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getNameAndJob</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">super</span>.getName() + <span class="hljs-built_in">this</span>.job;
  &#125;
&#125;

<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">new</span> B(<span class="hljs-string">"Tom"</span>, <span class="hljs-number">20</span>);
<span class="hljs-built_in">console</span>.log(b.name);
<span class="hljs-built_in">console</span>.log(b.age);
<span class="hljs-built_in">console</span>.log(b.getName());
<span class="hljs-built_in">console</span>.log(b.getJob());
<span class="hljs-built_in">console</span>.log(b.getNameAndJob());
<span class="hljs-comment">//输出：Tom，20，Tom，IT，TomIT</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，B继承A，那B被称为<strong>父类</strong>（超类），A被称为<strong>子类</strong>（派生类）。这就是类最基本的继承用法，B就是一个派生类，它派生自A类，此时B的实例继承了基类A的属性和方法。因此，实例 b 支持 name、age、getName 等属性和方法。
​</p>
<p>需要注意，派生类如果包含一个构造函数constructor，则必须在构造函数中调用 super() 方法，这是 TypeScript 强制执行的一条重要规则。否则就会报错：Constructors for derived classes must contain a 'super' call.
​</p>
<p>那这个 super() 有作用呢？其实这里的 super 函数会调用基类的构造函数，当我们把鼠标放在super方法上面时，可以看到一个提示，它的类型是基类 A 的构造函数：<code>constructorA(name: string,age: number): A</code>。并且指明了需要传递两个参数，不然TypeScript就会报错。</p>
<h2 data-id="heading-3">二、类的修饰符</h2>
<h3 data-id="heading-4">1. 访问修饰符</h3>
<p>在 ES6 标准类的定义中，默认情况下，定义在实例的属性和方法会在创建实例后添加到实例上；而如果是定义在类里没有定义在 this 上的方法，实例可以继承这个方法；而如果使用 static 修饰符定义的属性和方法，是静态属性和静态方法，实例是没法访问和继承到的。
​</p>
<p>传统面向对象语言通常都有访问修饰符，可以通过修饰符来控制可访问性。TypeScript 中有三类访问修饰符：</p>
<ul>
<li>public：修饰的是在任何地方可见、公有的属性或方法；</li>
<li>private：修饰的是仅在同一类中可见、私有的属性或方法；</li>
<li>protected：修饰的是仅在类自身及子类中可见、受保护的属性或方法。</li>
</ul>
<h4 data-id="heading-5">（1）public</h4>
<p><code>public</code>表示公共的，用来指定在创建实例后可以通过实例访问的，也就是类定义的外部可以访问的属性和方法。默认是 public，但是 TSLint 可能会要求必须用限定符来表明这个属性或方法是什么类型的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
  <span class="hljs-keyword">public</span> x: <span class="hljs-built_in">number</span>;
  <span class="hljs-keyword">public</span> y: <span class="hljs-built_in">number</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x = x;
    <span class="hljs-built_in">this</span>.y = y;
  &#125;
  <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">getPosition</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`(<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.x&#125;</span>, <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.y&#125;</span>)`</span>;
  &#125;
&#125;

<span class="hljs-keyword">const</span> point = <span class="hljs-keyword">new</span> Point(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)
<span class="hljs-built_in">console</span>.log(point.x)   <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(point.y)   <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(point.getPosition())  <span class="hljs-comment">// (1, 2)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">（2）private</h4>
<p><code>private</code>修饰符表示私有的，它修饰的属性在类的定义外面是没法访问的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-keyword">private</span> age: <span class="hljs-built_in">number</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;
&#125;
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Parent(<span class="hljs-number">18</span>);

<span class="hljs-built_in">console</span>.log(p);  <span class="hljs-comment">// &#123; age: 18 &#125;</span>
<span class="hljs-built_in">console</span>.log(p.age); <span class="hljs-comment">// error Property 'age' is private and only accessible within class 'Parent'.</span>
<span class="hljs-built_in">console</span>.log(Parent.age); <span class="hljs-comment">// error Property 'age' does not exist on type 'typeof Parent'.</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(age);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">super</span>.age); <span class="hljs-comment">// Only public and protected methods of the base class are accessible via the 'super' keyword.</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 age 属性使用 private 修饰符修饰，说明它是私有属性，打印创建的实例对象 p，发现它是有属性 age 的，但是当试图访问 p 的 age 属性时，编译器会报错，私有属性只能在类 Parent 中访问。</p>
<p>对于 super.age 的报错，在不同类型的方法里 super 作为对象代表着不同的含义，这里在 constructor 中访问 super，这的 super 相当于父类本身，使用 private 修饰的属性，在子类中是无法访问的。</p>
<h4 data-id="heading-7">（3） protected</h4>
<p><code>protected</code>是受保护修饰符，和<code>private</code>有些相似，但有一点不同，<code>protected</code>修饰的成员在继承该类的子类中可以访问。把上面那个例子父类 Parent 的 age 属性的修饰符 private 替换为</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-keyword">protected</span> age: <span class="hljs-built_in">number</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;
  <span class="hljs-keyword">protected</span> <span class="hljs-function"><span class="hljs-title">getAge</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.age;
  &#125;
&#125;
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Parent(<span class="hljs-number">18</span>);
<span class="hljs-built_in">console</span>.log(p.age); <span class="hljs-comment">// error Property 'age' is protected and only accessible within class 'Parent' and its subclasses.</span>
<span class="hljs-built_in">console</span>.log(Parent.age); <span class="hljs-comment">// error Property 'age' does not exist on type 'typeof Parent'.</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(age);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">super</span>.age); <span class="hljs-comment">// error Only public and protected methods of the base class are accessible via the 'super' keyword.</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">super</span>.getAge());
  &#125;
&#125;
<span class="hljs-keyword">new</span> Child(<span class="hljs-number">18</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>protected</code>还能用来修饰 constructor 构造函数，加了<code>protected</code>修饰符之后，这个类就不能再用来创建实例，只能被子类继承，ES6 的类需要用<code>new.target</code>来自行判断，而 TS 则只需用 protected 修饰符即可：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-keyword">protected</span> <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">//</span>
  &#125;
&#125;
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Parent(); <span class="hljs-comment">// error Constructor of class 'Parent' is protected and only accessible within the class declaration.</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
  &#125;
&#125;
<span class="hljs-keyword">const</span> c = <span class="hljs-keyword">new</span> Child();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2. 只读修饰符</h3>
<p>在类中可以使用<code>readonly</code>关键字将属性设置为只读：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserInfo</span> </span>&#123;
  <span class="hljs-keyword">readonly</span> name: <span class="hljs-built_in">string</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> UserInfo(<span class="hljs-string">"TypeScript"</span>);
user.name = <span class="hljs-string">"haha"</span>; <span class="hljs-comment">// error Cannot assign to 'name' because it is a read-only property</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置为只读的属性，实例只能读取这个属性值，但不能修改。
​</p>
<p>需要注意，如果只读修饰符和可见性修饰符同时出现，需要将只读修饰符写在可见修饰符后面。</p>
<h2 data-id="heading-9">三、类的类型</h2>
<h3 data-id="heading-10">1. 属性类型</h3>
<h4 data-id="heading-11">（1）参数属性</h4>
<p>在上面的例子中，都是在类的定义的顶部初始化实例属性，在 constructor 里接收参数然后对实例属性进行赋值，可以使用参数属性来简化这个过程。<strong>参数属性就是在 constructor 构造函数的参数前面加上访问限定符：</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;&#125;
&#125;
<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> A(<span class="hljs-string">"aaa"</span>);
<span class="hljs-built_in">console</span>.log(a.name); <span class="hljs-comment">// error 类型“A”上不存在属性“name”</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span></span>)</span> &#123;&#125;
&#125;
<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> B(<span class="hljs-string">"bbb"</span>);
<span class="hljs-built_in">console</span>.log(b.name); <span class="hljs-comment">// "bbb"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，在定义类 B 时，构造函数有一个参数 name，这个 name 使用访问修饰符 public 修饰，此时即为 name 声明了参数属性，也就无需再显式地在类中初始化这个属性了。</p>
<h4 data-id="heading-12">（2）静态属性</h4>
<p>在 TypeScript 中和 ES6 中一样使用<code>static</code>关键字来指定属性或方法是静态的，实例将不会添加这个静态属性，也不会继承这个静态方法。可以使用修饰符和 static 关键字来指定一个属性或方法：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> age: <span class="hljs-built_in">number</span> = <span class="hljs-number">18</span>;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getAge</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> Parent.age;
  &#125;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">//</span>
  &#125;
&#125;
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-built_in">console</span>.log(p.age); <span class="hljs-comment">// error Property 'age' is a static member of type 'Parent'</span>
<span class="hljs-built_in">console</span>.log(Parent.age); <span class="hljs-comment">// 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果使用了 private 修饰道理和之前的一样：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getAge</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> Parent.age;
  &#125;
  <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> age: <span class="hljs-built_in">number</span> = <span class="hljs-number">18</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">//</span>
  &#125;
&#125;
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-built_in">console</span>.log(p.age); <span class="hljs-comment">// error Property 'age' is a static member of type 'Parent'</span>
<span class="hljs-built_in">console</span>.log(Parent.age); <span class="hljs-comment">// error 属性“age”为私有属性，只能在类“Parent”中访问。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">（3）可选类属性</h4>
<p>TypeScript 还支持可选类属性，也是使用<code>?</code>符号来标记：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Info</span> </span>&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age?: <span class="hljs-built_in">number</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age?: <span class="hljs-built_in">number</span>, <span class="hljs-keyword">public</span> sex?: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;
&#125;
<span class="hljs-keyword">const</span> info1 = <span class="hljs-keyword">new</span> Info(<span class="hljs-string">"TypeScript"</span>);
<span class="hljs-keyword">const</span> info2 = <span class="hljs-keyword">new</span> Info(<span class="hljs-string">"TypeScript"</span>, <span class="hljs-number">18</span>);
<span class="hljs-keyword">const</span> info3 = <span class="hljs-keyword">new</span> Info(<span class="hljs-string">"TypeScript"</span>, <span class="hljs-number">18</span>, <span class="hljs-string">"man"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2. 类的类型</h3>
<p>类的类型和函数类似，即在声明类时，同时声明了一个特殊的类型，这个类型的名字就是类名，表示类实例的类型；在定义类的时候，声明的除构造函数外所有属性、方法的类型就是这个特殊类型的成员。
​</p>
<p>定义一个类，并创建实例后，这个实例的类型就是创建他的类：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span></span>)</span> &#123;&#125;
&#125;
<span class="hljs-keyword">let</span> people: People = <span class="hljs-keyword">new</span> People(<span class="hljs-string">"TypeScript"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建实例时指定 p 的类型为 People 并不是必须的，TS 会推断出他的类型。虽然指定了类型，但是当再定义一个和 People 类同样实现的类 Animal，并且创建实例赋值给 p 的时候，是没有问题的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span></span>)</span> &#123;&#125;
&#125;
<span class="hljs-keyword">let</span> people = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">"JavaScript"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，如果想实现对创建实例的类的判断，还是需要用到<code>instanceof</code>关键字。</p>
<h2 data-id="heading-15">四、类的使用</h2>
<h3 data-id="heading-16">1. 抽象类</h3>
<p>抽象类一般用来被其他类继承，而不直接用它创建实例。抽象类和类内部定义抽象方法，使用<code>abstract</code>关键字：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span></span>)</span> &#123;&#125;
  <span class="hljs-keyword">abstract</span> printName(): <span class="hljs-built_in">void</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Man</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">People</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-function"><span class="hljs-title">printName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
  &#125;
&#125;
<span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> Man(); <span class="hljs-comment">// error Expected 1 arguments, but got 0.</span>
<span class="hljs-keyword">const</span> man = <span class="hljs-keyword">new</span> Man(<span class="hljs-string">"TypeScript"</span>);
man.printName(); <span class="hljs-comment">// 'TypeScript'</span>
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> People(<span class="hljs-string">"TypeScript"</span>); <span class="hljs-comment">// error Cannot create an instance of an abstract class.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里定义了一个抽象类 People，在抽象类里定义 constructor 方法必须传入一个字符串类型参数，并把这个 name 参数值绑定在创建的实例上；使用<code>abstract</code>关键字定义一个抽象方法 printName，这个定义可以指定参数，指定参数类型，指定返回类型。当直接使用抽象类 People 实例化的时候，就会报错，只能创建一个继承抽象类的子类，使用子类来实例化。</p>
<p>再看下面的例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span></span>)</span> &#123;&#125;
  <span class="hljs-keyword">abstract</span> printName(): <span class="hljs-built_in">void</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Man</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">People</span> </span>&#123;  <span class="hljs-comment">// error Non-abstract class 'Man' does not implement inherited abstract member 'printName' from class 'People'</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> Man(<span class="hljs-string">"TypeScript"</span>);
m.printName(); <span class="hljs-comment">// error m.printName is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，第5行报错：非抽象类“Man”不会实现继承自“People”类的抽象成员"printName"。在抽象类里定义的抽象方法，在子类中是不会继承的，所以在子类中必须实现该方法的定义。</p>
<p>TypeScript 的<code>abstract</code>关键字不仅可以标记类和类里面的方法，还可以标记类中定义的属性和存取器：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span> </span>&#123;
  <span class="hljs-keyword">abstract</span> name: <span class="hljs-built_in">string</span>;
  <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">get</span> <span class="hljs-title">insideName</span>(): <span class="hljs-title">string</span>;
  <span class="hljs-title">abstract</span> <span class="hljs-title">set</span> <span class="hljs-title">insideName</span>(<span class="hljs-params">value: <span class="hljs-built_in">string</span></span>);
&#125;
<span class="hljs-title">class</span> <span class="hljs-title">Pp</span> <span class="hljs-title">extends</span> <span class="hljs-title">People</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  insideName: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong> 抽象方法和抽象存取器都不能包含实际的代码块。</p>
<h3 data-id="heading-17">2. 存取器</h3>
<p>存取器就是 ES6 标准中的存值函数和取值函数，也就是在设置属性值的时候调用的函数，和在访问属性值的时候调用的函数，用法和写法和 ES6 的没有区别，可以通过getter、setter截取对类成员的读写访问：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserInfo</span> </span>&#123;
  <span class="hljs-keyword">private</span> name: <span class="hljs-built_in">string</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">userName</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">userName</span>(<span class="hljs-params">value</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`setter: <span class="hljs-subst">$&#123;value&#125;</span>`</span>);
    <span class="hljs-built_in">this</span>.name = value;
  &#125;
&#125;
<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> UserInfo();
user.name = <span class="hljs-string">"TypeScript"</span>; <span class="hljs-comment">// "setter: TypeScript"</span>
<span class="hljs-built_in">console</span>.log(user.name); <span class="hljs-comment">// "TypeScript"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">五、类的接口</h2>
<h3 data-id="heading-19">1. 类类型接口</h3>
<p>使用接口可以强制一个类的定义必须包含某些内容：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> FoodInterface &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FoodClass</span> <span class="hljs-title">implements</span> <span class="hljs-title">FoodInterface</span> </span>&#123;
  <span class="hljs-comment">// error Property 'type' is missing in type 'FoodClass' but required in type 'FoodInterface'</span>
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面接口 FoodInterface 要求使用该接口的值必须有一个 type 属性，定义的类 FoodClass 要使用接口，需要使用关键字<code>implements</code>。<strong>implements</strong>关键字用来指定一个类要继承的接口，如果是接口和接口、类和类直接的继承，使用extends，如果是类继承接口，则用implements。</p>
<p>注意，<strong>接口检测的是使用该接口定义的类创建的实例</strong>，所以上面例子中虽然定义了静态属性 type，但静态属性不会添加到实例上，所以还是报错，可以这样改：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> FoodInterface &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FoodClass</span> <span class="hljs-title">implements</span> <span class="hljs-title">FoodInterface</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> <span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然也可以使用抽象类实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FoodAbstractClass</span> </span>&#123;
  abstract type: string;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Food</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">FoodAbstractClass</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">public type: string</span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">2. 接口继承类</h3>
<p>接口可以继承一个类，当接口继承了该类后，会继承类的成员，但是不包括其实现，也就是只继承成员以及成员类型。接口还会继承类的<code>private</code>和<code>protected</code>修饰的成员，当接口继承的这个类中包含这两个修饰符修饰的成员时，这个接口只可被这个类或他的子类实现：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-keyword">protected</span> name: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">interface</span> I <span class="hljs-keyword">extends</span> A &#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-title">implements</span> <span class="hljs-title">I</span> </span>&#123;&#125; <span class="hljs-comment">// error Property 'name' is missing in type 'B' but required in type 'I'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> <span class="hljs-title">implements</span> <span class="hljs-title">I</span> </span>&#123;
  <span class="hljs-comment">// error 属性“name”受保护，但类型“C”并不是从“A”派生的类</span>
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">D</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span> <span class="hljs-title">implements</span> <span class="hljs-title">I</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">六、其他</h2>
<h3 data-id="heading-22">1. 在泛型中使用类类型</h3>
<p>先来看个例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> create = <T>(c: &#123; <span class="hljs-keyword">new</span> (): T &#125;): <span class="hljs-function"><span class="hljs-params">T</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> c();
&#125;;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Info</span> </span>&#123;
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>;
&#125;
create(Info).age;
create(Info).name; <span class="hljs-comment">// error 类型“Info”上不存在属性“name”</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里创建了一个 create 函数，传入的参数是一个类，返回的是一个类创建的实例，注意：</p>
<ul>
<li>参数 c 的类型定义中，new()代表调用类的构造函数，他的类型也就是类创建实例后的实例的类型。</li>
<li>return new c()这里使用传进来的类 c 创建一个实例并返回，返回的实例类型也就是函数的返回值类型。</li>
</ul>
<p>所以通过这个定义，TypeScript 就知道，调用 create 函数，传入的和返回的值都应该是同一个类类型。</p></div>  
</div>
            