
---
title: 'vite+vue3+ts+elementplus'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a1feb9139a74e8b87195a78549c861b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 00:24:43 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a1feb9139a74e8b87195a78549c861b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADsAAAA6CAYAAAAOeSEWAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAABkLSURBVGhDtZoHnJ1llcbP3Om9ZiYzmfSQhCQQIbRQVQKI9CYC68qKriJK0UXcZRcINqStIoiIqKCi1NACQihBWiCkkJ5MJlMyvd7p7d759v989/sy34yTbIj48Atz71ff855znvOc971xDrB/EtoGI7a9Z8Aq+wZML0mNj7dE95NZ1OKsj1dHo1GbnJpss9OTbWJyonvun4VP1Njuoagtb+m0it4By0iIt8LEeMvkr8XFWcfgkA1gYDLf47i2PzpsyU7UspKSLDoctagTZ7Vc08MzClMS7awJ2ZaflBB78CeET8TYla1dtrKt2w5KS7YCDGzEoz2RqKUmhGw6x2bhuXyOp2BoRXef1Q1E7Lj8TIsMD1sbxu1kcnYSAX1810RMTUmyMB7f2j1gC7NS7byinNiL/kH8Q8a+2NRh77b32El56VaPAe0YeGR2mh2bm+FdMRqP1rbZe+3dFsHT35qcb/Oz0rwzo7Gxs9feYPLS4kM2h8lawee5hPmlJXneFQeGAzJ2F564v7rFzi7Msu3d/Xgjzq5g8ArX8VCNN2vJ28daey0zZJabmGCLslP5HOf+Oygr3UzDGOf+JxrauXfQjslJt+dbuuyMgiwmk+sPAB/b2Lt2NdoMZnuY21qHIvbvUyZ4Z0ZQiXGrWjvsmPxsK4R0nmHA8ZCTQvxVQn5eRipklIBtcVbV1WtHYsjati47ZWKuTUpP9Z4yGk/xDBGe3v1mW4/dOrvYO7P/2G9jRSjf31FnXyaUXiB8r51WaJkM3kcfOSa2FR6qarIenooTLQHPLcC4mYThyw1tVpKWYlVERlZ8nC3Oz3Jzdn1nn5uvQ8OOHYvhR/CvsqffJbkCkZTvcYZ6Z0WTfTovw5Y1dtjXp+TbFPhgf7FfxpYxuMfr2uwo8rEtMmwXF+d6Z8wGmIR2PLyjo8cqOFffP2SLGexJEJCP9R29thkPXlpa4A5Y3w/jmuVNYYwO2QkY7WMtz3mVcE1hkualJdmSolzX8GnpKd4VZq80d1o7zN0RdWxGaqItgbn3B/+vsasgh/UMNBOvzYMZDxtDKp289KGaVguFQvb1yQWWwuB97GaSXqUUnVaYbSUwrDCEBz/C2CM8EhNrP13fbkeSh3OJgCAe2N1CWXKsGOc6TOr5U4q8MwYhDtkTda02MyPN+nnGBQEH7A37NHYz5KOZVv08qyjbSseEzKauPnsMj98wc6Ibcj5UUv7M8QWZTE52jEwGOVaD8U1Dw1YNWX0qM8VKyb80L/TrOPYOzH4KBJQTrK8M7+7KZjuM63sHBt17FubGoibCuf+tarWFGUmuwWeT8/vCXo1tZOYeZcazCaez8MwEzzM+HqhqtiJI5twxL1jeGLYk7jmKMF1JOCbg6Qj5nAdRqX7q3BYm8VAmQvW1lfcMc58IT95uIA3q+gftrDHPXUXJWkVEHJme5Bp5UmHsvIZ/O3l8ECE/FWcsItX2hr0ae8O2Wjs+J43QTbOZzGYQ/7Wtxq6eXjRK3r0By4YJ6Ty8EiYSJqcm2eGeV4Pox/ANENJR49RiEdfqcLflUJrEBZqgxYHrBjn2ExFURqKdVETN9YirJxKxR2rbrYeQv5ISmB6IsiDGNfZGWPeMgkzr58xnPaJ5p6XDZPKz4T77wayJ7jGhhXLwanOHTWBgq5n5q6YUwNJ7l3kKcRl7OJ7fF56l1GzvHbSD8dghTPi0wIRfv6XafjJ3ssv0PnZQ7nZx/etwzO1zJ3lHR2OETTw8x0tOx1AN3De0D7YV+63oGthjaJQ5Ur7eVVZjcdGInUyuaT73ZWg3efV8fZs7cc2E777Qi5eunVbghvPPymrt/krKGfcLd8ybYjdxrK6333Z09rjHZkNuLYzz0uIc+xWCZzz8nbHbe4dsY1e/XUOY+nimvtUaSazv4jXhaQasSbmYmpuenGwHZ8TKggSEQm08rMD7ahBOoExcMqXQegjnZ+CEvaEa1ZQUQkt39dj0zDS7krq+ARmpdws/nlNqD9WFbWN7l5u3wr9MyrcXKUsqWy3jTOaoML4DdaQ83YIoT4VYpEXvYQZLmbX5SLohBrgOj186Kc/iKTUPUhq+Rrm5ekOl3TWv1Mr6hqwbY0VOQXwEo+Moq4Z47q5qsU489G944LyJOW4LOLZOKtT/iI6+nGe/0dhuEd4ltj2NmiuCU4hnk5fHIi7+RK4uTEu0e+s7rAiRcw1CYy3OejvcYz+eXeI9MYY9nu3lYZl0KavJJ7Vjibzgjp319rUZE20j7CkJqFr5JQYgQ39f3eQaKpQk0afy8nl4uBzvjUUTRk7k3iebOm0pabDiyFn2XGu3dRME41CGVeBVqSiVnc6hIUpekp1VjHLDSOEcQlui5W/U8C7IKREjv1Gabw3wRwUTvpv7jybPtzHmIPZ49q6KRjuccqBQVCOtGvqXhrCFUUXJzOYSHt7Kw5Ix9H08dSje1o1JyL73IYXpEMmE5CRbw6wuykx2pR+Pd6/J4JpLiJKV6N9OnrcQNfQ0Zem6qQX2MmFXyWTE+DMO0kGx4e08DEjnXbsYuOq7niHB8jdY/wQ8Srm2XCZZUrOakF1CY5EKX0h93Tu/1J4kRdbDMT8MamgZK9xe3uDcvrPe++Y4f61rcZr7B53rN1c5N2ytcV5rCrvHt3T2Og19g+5nH7dvq3bqunr4NOwgK2MHA1jeEDuG7HNuLmtw7qpocl5t6nCPvdTQ7v4N4u3WTqeyu9cZHIo4f6lqdFoHh7wzMbzDeeGv3Hvzjlrnh2W1zofhHuftxpFn3VFe7zxS0+p0DlKVPbhhvBxhvwiFMgfP+mjHA08gEC4pybeLyK1iZldh8zC5VJQyUl8l59KZ0WJk2xaiYWxNrkXXJhA8r3PvZRur7ZZZRfadaRPsfiTmX9HGajC2tXd6V8dQTMhX0h8rNdJx9Ra8F8SbRNLzhPRnJmTZIUTYueTyWxyr7uv3rjC3OkzE8495oS+4xq6D5WoI0bO5WVCOSerl8rIeBrOI/Hkaw6ME5W1zSuzx2la3CRdWi3zIG+FDBvUp9LMgI/vggUmE7KkT81yGvOOgEYa/aUahhRAF5xLec3OzbF1r2O17BbVxIi7hzJIC64IYhXdJA+nh/5xVbOmE9J0QqjSxWk0pp37M2YEtgjS8GpimACu7xkqxdKJ6fEXyYl2Lre0ZtC8yELVewtWUnbfCPIhrvgDFz8WI5yhJKgcnFMZWEFrwhgzo5uWDDDA1oGSOzcu0xfx7vTlsv6posIMpJ6cGWPiw/BxL4PU7vbrpjgf8bMdu5OYwOdhm83DARUSa0ELknYIeEAaILuWxlhGa0M8+EuJCrpJT+ymENhN60pXBxa3LZ5TsucnlGaCmIEQ4Evru91yuz0xMtKaeXluI5zdh9Mm8vAlBn4aR07X64EH3vEKdXQkZJXPP/JxMvNRpLxEtHZ5RQgmNewnpouvVTpYTHdfOnmy5kFUGnpRTfEhXD9DiBdFFJB0/YWS9aj6pmc89r0BaQmgTRkgI+EsdKsYasJZOBF+QqTH474NK7LbyBvf7W+RgOxNyxfQY2/2hrp2+NkroxrzrQ55fSZkpJIa28znCgF6rb7H1hOSslATyvNflAh9pvHcX3lVE/Ya8FjTJIexa2Rq77nfU96unTnD7aME3+TAm6BFKYrPnqCNIqV5sq0ZGCiEV+Db+qWMQqpFgb5KPx48R6omeDl2EuP9DTYt9iGA/f1KBS1w/La+H4ktsSmLItvZHXLUkrCeflVtJ9DVVg1H7+sxiGvVM975rZpfabuqHVhuP5F1vewav5O8GamUe91yDanoYw47FWzC929O+DJnKA2opFY1Rjru5CE7kOcO0jJtQVUIynzuZEMeb+1CEOFXN8iFSGeRpCm1BTlJxVg49Azm819SO7Bu0axEbwn27GuxMck+TMQHDP8fn48gfDVIL4R8xKVPJ73MQBUIfA/Z54LMw5vmlE+w+VFo2A78X/SsyPA/RMD0z3e2qVLtfo7aeBslpMX0N0TEnLcUlKym1jyBFqSohmYntI5enBhYB9CY/2kNarhwJhNiMtRGyWnkQdKaCFyQwgydjyNUw4VchKxXv2/DoKdC+lkQbCX1NlKCGvJiBJkSGbCus6jfo4yGBNySgr+u7e20BCsxdVAcFlJ/tHd32+cIsNxSXUULUUx+dg/d47g7OPYFw2MxkSuyMwLHVTI6PBN6dS8Sppw45zHJSgDXV3aQzmz40Z6fDgBfiAXU0uZxby2zejee+j3eltoQMzhV6qSBogXwrEXDj7ElWxUQ8RrnSaoU0dxIsKaiMvMykXTu90NqJsGHP4z78SdLigUrLKat32nFwy/E07pfDFRdQ/7N5r57pQ1482uvWhMGhQcviGkVrKDUp0ToCxfhQal5n4Hs/g1jOgH4LWdwFOd1b1WzHET4vLZppv+Czjxo840OrDlG8jAJzv2tp5mLK1dsU/lfIOeWy5NxFxfl2BoYImlQtx9QF6mJRQKBsQYYuO2yaLYPBUXvu/VqYPxtHhNy7Y4hCkNLGPtKSklzCVKSHtMQxcqm5Kw1DhI2PTGZtcGDAvoLQ/u7MifYtWFBlxz2H9zo8RkwKzC5UYiG+p44ccqE62YAxLeT/TOpf8MXx8Qk0IJFRY1Go+viQVJpE5Ehjf49xfAZeqGIy/7us3nqxwQfCkjZypPxobVr/6YpQHIalUvuCyEwbSXC9PC8QnkFcXlrgLpoLIhIfKuaqlQkYIAwQnr/f3eyu7KttOw2lNpv8/BPHyjzVNER3o72gvEBKqRMTflndbP8BMweRDyeciEj5bFayFXqTLzheivgYJC0jwzwHa0MDDEotm48ndze5BBBElAnxxcRYHAFh3FfZaA9UNRmC354kNwUx8eHkmVj5dcTE5ZMnuEyr1QqlhtaJLuOYZv4v3KNo0TKrGPUZ1NILPKuWcvVn5Trv10SMB6h0j/ARMnlOuafCBIfnSWEx/Raif3HDzofYMM31dOyY9LBaLK3TjoX2fEqT4+2qaUVWSTQvyM6wC8nNJyEetXIyuLKrx04P7MKNnbJZlKUtNAIHo7i2dA/YU3Vtdi5l6jCepXy8hOedSSSsI8/HQg5Q+gxTKXwkMHkbESo+hjG0lbRRzQ3Fc5LOzDuFhs3Ptumpie7ilRDhlEJOq/hjsZljCxjkt7fWuPS/EekpXMggJQIk0G+eN9Xu2VmHWIkJe0nJRN4ptBBit2yutG9ML7J1DHAxebiAMrZ4VZlduqGS8I2tJc2iborUxmIN79c+kTovFxivPvrcSaP3n7RSKYTUmKt4N3rMOcw4JOneD3sP956jNaMglIeTER5Xbdlt15Tm2W10NEsYrA/N5JLCHHsR9tSqwxq08G3bqm1ZTbOtagnbo6SLvH/VzBL7W7jPzqFea0LmMLFzUuLtdwumuO3i1Vtq7OK15Xgw3l1PDmIXak+6QBEkvB9YJIzBcc/L20JIYaSZ/qAzVm5Ut4oowk3QehC+N3xo/1wTqt7zsYawfX9no9XjqdPXVLhrwyo/wucJYQkE1e4j8rLcBuHUItQQKqgMXb6LGvxFQlXw33AdZLR0V5P9Fr29lP73scNnosoyvdWPv4fPJ+uJrLVtMakqaL1M1cTvv0OLIZE6wk2a2IcIRUQh+DaejpdcXepBa7bKDRGM9PIVxTl2EwarZ72rooVuY4RQtMypdk6e1lLLehhY2lt7QEd7WxlCDvdIli6E9B4+ZIodmZEMccUGqgiZOqru9tkR3iJ8nCcXRWRZCSPMLPEjlx2LjQL1OM5qKAm+vhSuRqSfV5Ttrg8FdWcrnhMqCTex7DEM6qTsVEuM1+8hovaHQ6e6a1Fz0xLd3nUt4ToWWuzWNkhcoAIIjUx2ZpxjLzWF9+SYmngR1lok4TEoJxGfuijhI/7OICoFmadl2llcL9b1oRVJtbD+JLlv1KrhHG5811t9ELbzgk14ICUwqE+TDzftqHPz98vUSy3jSIwP8dCpkNqLDPTx+rArz4T5qLG3G2PrvJKKPoLBWE501NC3ilUX5mVjVIb9nIbgWcpPMiSXjbcL8K62UkR86m1/yfkSeMaHFuK04X0CE3J6SWzFUxw0BSNHlSzi3RmIRJwHq5udO3c16quLp6sbnffbupxbt+12vzOrzuvNHc7ycRbIxuJHgYU7YSASdQgxp7qz2ynv6HJeqW91doa7nLruXof+17sqhhu31Xif9o7HalqczV29Dnrb/f5EXZvzdH27U98/6LR5i3N0UM5zjHU71/lwjRWWltU5CAIn7F1MqLp/r9hQ5RoaxG+qmrxP4yNKcfsFLwuiprffeb2l03m2scO5h3Or2rudzjGrhk8x4Cqu2xcexilBvNEcdi5Yu4tKF3Ue4tzPy+td5/1md4tzw5iJ27NuXEYobYUdlb8z6GTWkdxaCvk2zHjd5mpKQ459mv5TkAp6mQb9Aq9HHQ8S6mrZnuc6vUG6WHusIhCJGNXl9byvnJyaiE7+Eoz8c5TYNQiUveENGpJpcIJ+biS8R0+rlcazGNs7pKB+zPLTOSX2KNWhlDAf4r2Spj72JORB5OyHULX+dlD/FOky/HFy5ygYU0sey/i8moeqdunXK1qC3RuaMOYHlI/raQMl3M+EeTV5WxD3Km8a8PkM8nr648sQ9+esKbf5e/nxiKBfAOQkxbv3SU9LYmqPV9V/Pn+V20VwTyVjTqCI6edEQUOFUXs9WmfSll8DyX2dt7GlnwkswaM3l9XZ0oNK3MTXbxpOV2sGk69s6XCJw4cY8KbyRrt9TrHt7Bm0rRBQe1+fHUWNfaapU0KbqxzbORC1M/LS3dJwIl3KOrwykQG/E+61q+isgniztdOKqNOziDgZqZIzFwPvqGiyg5NCtoCqoG5NxHhPZTOsnORulKskjoKMDeLuXQ3OmnC3syxARFXdfc57LR3OrdtrvSOOs55rnqhtcdoGhpxHdjc5EfJUuHZTlftX+G15rXPlhkrnLe59F7Lz8VGHdg8c5y2OLeMZ126qduq9XC3v7nd+FchLvYPJd15gPCu8XQnh/qpm59WGVudZzvvQO97kXTcGxhnEuJvR39tWY8cwK4uhcikk4a3Gdstg9l5B2t0wfaTdWkEou5vCPOV5PH73vFL3+DfXltnh6OxjkJD6Wd5F3g88tMe6CW/7YmI99VIL4u0oqUK8ocW4d8hFrXMVoOQU8s3U97MnjvDD/XRYkyhHM1MT3GVZQR2Tdv70U8EbA5vlo+CaPAaaSWoZXm50otGodxQ6L6txGKxzw5ZYORrBsPPrykZKQIy1n8bTjwb2fO4Te3ue7x6KOKvaYns1wtIddd4nx3mwot55qyl2360cp81zurg+CGqwU8v4/Of5uAVvPgObrwvHomY8jOtZ4fXWLnefdHVXv9044+8ZklCx75DXwcV1Sb27y+vInUQEuVYSaMgRJYfAwtoj0raFxIUW1A8nz35f02qLc9Lc9lG7CBkwtUR7bf+A+5uL6ehnH9Lat+5sIEfj3Cbj3NKRvP7Rjlo7FSmqavKvpSP8MRZ7NVbQYLSkqlC9ZW4sPH18gBTcORjrhMWmQWzFmK2UsvO90qQ1oZcI8UhkCLZPtRqMy0NirobAvjIpb4/sW06qKGyPR2oGIdlazjOOTk+kLYzaaYGSp63Wz6HsXsQ51wd+LTAuZOy+8GBNq7tF+IOdDU4kENJthNID5YRafZtzZ3mDs9LbRgzixcZ2l1h83OKFbDmEd0/FiFp7DWHgp0AQGzq6nf8hPF+oa3EehOz0ziCWcm4NpBRMhX1hn571oR9wqVVSDVPtUi32sQ0vbu7scZdY9aOt2ZSEL9BEBIW+dv20AKDd9/ep09oimYqHpyImkKDuRllS4PrlHNuIqDmCJmNJQba7q1joEaUQJuR/WdXsLrJrq/L6cdJsPOyXscJ7GLKqo8cOpqhrO//yQG6oS3kZwS9xPkRB3wi7diFMtDN+PLk5m1ath+8f0Fy80dbjhvVXub+U5mEqeal27UP+dWpPlknNxW79Ak6/7Tg3UMOF52j1xA1qK7Trd6nXC+8P9ttYQcumIonLSnJtBdJNa77axw1C2x3qR4Wqnj73x9f6MbV+CCYFBZO6y51aSh3gzVrsmwzJnULEbCJC1oZ7vIZ/9Iqmfvn2u5oWO5n8fApxcuWUApum5diPgY9lrA9EtvUNOzYf8vqAcJPsU5iOh7XtXQgt2uZhjKU2amF7HQyfEYWcZk5yQ1RDKNrLcq02k/9IGmldrB93KiokPw8EB2SsoKWXO5FmxXhlckqi+3vEUvLqwok5PHVkIWAszlqzy1p54zuLpnPZ3q9bod08JlLSb5DrNxDm38Sbvsg5EBywsT7oH+3XNW3uasGirFSrxRNdCllKiPZHZzJYLZb5qEcpae3pxMCuu9oibS5/QCOiLcYUrp+MmtJeURjFdVlxzqiae6D4h40NQt54HyGv3JRo10aVfv8YhtC0pSlVKcPFuxIXahr08mzCO4VzMlLSsZuomZ+RaucU0rXsw/sfF5+osUFonWob/7TrLdaUgdpV93fl9X+VIC0Y6tek2uI8OD3J5gT2Vj9ZmP0f4IM4iY7RQ5gAAAAASUVORK5CYII=) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>公司一直用的<code>Vue2</code>开发的项目，上次开会主管说：“我们下次的后台项目用vue3吧，之前项目清闲的时候也跟你们说过，不知道你们学了没有。。。。。”，然后就让我去搭建整体的架构。emm。。总要找(编)一个合适的理由(-_-)，哈哈开个玩笑，希望大家可以从这篇文章借鉴吸收一点有用的东西，有问题的地方也欢迎各位指正。</p>
<p>demo地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FSrimr%2Fvite-vue3-ts-element-puls.git" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/Srimr/vite-vue3-ts-element-puls.git" ref="nofollow noopener noreferrer">gitee.com/Srimr/vite-…</a></p>
<h1 data-id="heading-1">创建项目</h1>
<p>这个<code>demo</code>只用到了部分<code>vite配置</code>，想要了解跟多<code>vite配置</code>请移步到：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.cn%2Fconfig%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.cn/config/" ref="nofollow noopener noreferrer">Vite配置</a></p>
<h3 data-id="heading-2">初始化</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a1feb9139a74e8b87195a78549c861b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>demo</code>用的是<code>vue-ts</code>模板，所以：<code>npm init @vitejs/app vite-app --template vue-ts</code>，安装完成之后我们需要<code>npm install</code>，之后就可以<code>npm run dev</code>查看初始的效果了，不得不说<code>vite</code>跑的真的是飞快~</p>
<h3 data-id="heading-3">安装依赖</h3>
<p>样式预处理：<code>npm install sass</code></p>
<p>要使用nodejs中的模块：<code>npm install @types/node -D</code>，否则：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5212c86148d14900be98bb1c60006038~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">做一些简单的修改</h3>
<p>主要修改的是<code>vite.config.ts</code>的配置。</p>
<h4 data-id="heading-5">1.模块配置路径别名</h4>
<pre><code class="copyable">import &#123; defineConfig &#125; from 'vite'
import vue from '@vitejs/plugin-vue'
import &#123; resolve &#125; from 'path'

export default defineConfig(&#123;
  base: '/', // 访问路径
  plugins: [vue()],
  resolve: &#123;
    alias: &#123;
      "@": resolve(__dirname, "src"), // 路径别名
      extensions: ['.js', '.vue', '.json', '.scss', '.ts', '*'], // 导入时想要省略的扩展名列表
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">2.打包配置</h4>
<pre><code class="copyable">  build: &#123; // 打包配置
    assetsDir: './static', // 路径
    rollupOptions: &#123;
      input: &#123;
        // 入口文件
        main: resolve(__dirname, 'index.html'),
        // 其他入口
        // nested: resolve(__dirname, 'xxxx.index')
      &#125;
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">3.本地代理</h4>
<pre><code class="copyable">  server: &#123;
    host: '0.0.0.0', // 指定服务器主机名
    port: 8084, // 指定服务器端口
    open: false, // 在服务器启动时是否自动在浏览器中打开应用程序，默认false
    proxy: &#123;
      '/api': &#123;
        target: '你要代理的地址',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      &#125;,
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后将<code>package.json</code>中的<code>build</code>命令修改为：<code>"build": "vite build"</code></p>
<h1 data-id="heading-8">开始</h1>
<h3 data-id="heading-9">vue-router4.x</h3>
<p>既然用的是<code>vue3</code>那我们就要用<code>vue-router 4.x</code>了，运行：<code>npm insrall vue-router@4.0.0</code>，让它先运行着，我们新建几个文件夹和文件：</p>
<ul>
<li>layouts/error.vue</li>
<li>router/index.ts</li>
<li>router/modules/business.ts //配置business模块下的路由</li>
<li>view/business/manage.vue</li>
<li>view/login/login.vue</li>
</ul>
<p>建好之后目录应该是这样：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/780568536df7466786d8994591e3300d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就可以在<code>router/index.ts</code>中配置路由啦~</p>
<pre><code class="copyable">#### router/index.ts

import &#123; createRouter, createWebHistory, RouteRecordRaw &#125; from 'vue-router'
const routes: Array<RouteRecordRaw> = [
  &#123;
    path: "/",
    redirect: "/login",
  &#125;,
  // **********登录**********
  &#123;
    path: "/login",
    name: "login",
    component: () => import("@/view/login/login.vue").catch(() => &#123; &#125;)
  &#125;,
  // **********404**********
  &#123;
    path: "/:catchAll(.*)",
    name: '404',
    component: () => import("@/layouts/error.vue").catch(() => &#123; &#125;)
  &#125;,
];
const Router = createRouter(&#123;
  history: createWebHistory(), //使用history模式
  routes,
&#125;);
export default Router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>main.ts</code>中引入：</p>
<pre><code class="copyable">#### main.ts

import &#123; createApp &#125; from 'vue'
import App from './App.vue'
import Router from './router' //引入

const app = createApp(App)
app.use(Router) // 使用

app.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后再修改<code>App.vue</code>的内容：</p>
<pre><code class="copyable">#### App.vue

<template>
  <router-view></router-view>
</template>

<script lang="ts">
import &#123; defineComponent &#125; from 'vue'
export default defineComponent(&#123;
  name: 'App',
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本以为大功告成，运行应该没有什么问题，结果~，它给我来了个Surprise！！
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a606480ca3743c49df4eb831ab0ad14~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
没有管它，继续打开<code>Network</code>的地址，控制台打印的是下面这个东西，好家伙~，没看懂 (0.0)！！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb08a34954ea4721b564e7f0b0ae5b13~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
大致意思是模块脚本不对。。。这不是搞心态？？然后百度了近半个小时，无果~，然后我就想是不是有些依赖没有安装或者是文件引用的路径不对？然后打开<code>Local</code>的地址，果然不出我所料。。。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53d1f95a2e2e468e9c1edcc201423545~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
随后就是顺藤摸瓜，找到了<code>node_modules/vite/dist/client/client.mjs</code>，<code>.mjs</code>文件搞得鬼(<code>vite</code>趁我没注意又更新了)~</p>
<p>更新前：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cb9a1c363824127ac2bd613dcd300a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更新后：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4b3f60d2dad49eebc2946d667e8212d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为在<code>vite-env.d.ts</code>文件里：</p>
<pre><code class="copyable">#### vite-env.d.ts

<reference types="vite/client" /> //这里找不到client.mjs文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以就在<code>导入时想要省略的扩展名列表</code>加入<code>.mjs</code>。</p>
<pre><code class="copyable">extensions: ['.js', '.vue', '.json', '.scss', '.ts', '.mjs', '*'],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再运行(应该)就没有问题了~_~。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/293c886134de46f985c196c0e96ba3c1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79d0221f519646fd95daf1c4203f139e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">element-plus</h3>
<p>同样<code>vue3</code>使用<code>element-plus</code>，执行：<code>npm install element-plus</code>，<code>element-plus</code>的组件内部默认使用英语，随后我们在<code>main.ts</code>中需要<a href="https://link.juejin.cn/?target=https%3A%2F%2Felement-plus.gitee.io%2F%23%2Fzh-CN%2Fcomponent%2Fi18n" target="_blank" rel="nofollow noopener noreferrer" title="https://element-plus.gitee.io/#/zh-CN/component/i18n" ref="nofollow noopener noreferrer">配置相关的语言</a>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30f2a202de834477a1c26d32b076b593~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#### main.ts

import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
import locale from 'element-plus/lib/locale/lang/zh-cn'; // 使用中文

app.use(ElementPlus,&#123;locale&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>assets</code>中添加<code>reset.scss</code>用来重置样式。</p>
<pre><code class="copyable">#### assets/reset.scss

body,dl,dd,h1,h2,h3,h4,h5,h6,p,form &#123;
    margin: 0;
&#125;

ol,ul &#123;
    margin: 0;
    padding: 0;
&#125;

li &#123;
    list-style: none
&#125;

input,button,textarea &#123;
    padding: 0;
&#125;

/*另外：button和input本身有2px的边框，textarea和select本身有1px的边框，根据实际情况调整，或是去掉边框*/
table &#123;
    /*为表格设置合并边框模型*/
    border-collapse: collapse;
    /*设置表格边框之间的空白*/
    border-spacing: 0px;
&#125;

/*去掉a链接的下划线*/
a &#123;
    text-decoration: none;
&#125;

a:hover &#123;
    text-decoration: none;
&#125;

/*个别浏览器对语义化标签的兼容*/
header,section,footer,aside,nav,main,article,figure &#123;
    display: block;
&#125;

h1,h2,h3,h4,h5,h6,em,i,b,cite &#123;
    /*字体样式不加粗*/
    font-weight: normal;
    font-style: normal;
&#125;

a,input,button &#123;
    /* 清除点击阴影 */
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
&#125;

body * &#123;
    /* 选中文字设置 */
    -weibkit-user-select: none;
    /* 禁止文字缩放 */
    -webkit-text-size-adjust: 100%;
&#125;
dl,dd,h1,h2,h3,h4,h5,h6,p,div,li,ul,ol&#123;
    box-sizing: border-box;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若是在使用<code>element字体图标</code>时，不幸出现了<code>字体图标</code>不显示，或者显示的是方框的情况。可以将文件<code>node_modules/element-plus/lib/theme-chalk/fonts</code>下的<code>.ttf</code>、<code>.woff</code>复制到src/assets中
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28a5e68d504a45f3a57be3aeb0e8403a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在<code>diystyle.scss</code>中处理字体图标，之后在<code>main.ts</code>中引入：</p>
<pre><code class="copyable">#### diystyle.scs

@font-face &#123;
    font-family: 'element-icons';
    src: url("./fonts/element-icons.woff") format("woff"), url("./fonts/element-icons.ttf") format("truetype");
    font-weight: normal;
    font-display: "auto";
    font-style: normal;
&#125;

[class^="el-icon-"],
[class*=" el-icon-"] &#123;
    font-family: 'element-icons' !important;
    speak: none;
    font-style: normal;
    font-weight: normal;
    font-variant: normal;
    text-transform: none;
    line-height: 1;
    vertical-align: baseline;
    display: inline-block;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
&#125;


#### main.ts

import '@/assets/diystyle.scss';
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">vuex4.x</h3>
<p>执行：<code>npm install vuex@4.0.1</code>，在<code>src</code>下新建：</p>
<ul>
<li>store/modules/menu.ts  // 用来模拟后端接口返回的菜单数据</li>
<li>store/getters.ts</li>
<li>store/index.ts</li>
</ul>
<p>在<code>store/modules/menu.ts</code>中模拟一个菜单的数据：</p>
<pre><code class="copyable">#### store/modules/menu.ts

interface MENU &#123;
    name: string;
    path: string;
    icon?: string;
    children?: MENU[]; //定义数组类型1
&#125;

interface STATE &#123;
    menus: Array<MENU>;//定义数组类型2
&#125;

const state: STATE = &#123;
    menus: [
        &#123;
            name: "商家",
            path: "/business",
            icon: "el-icon-s-shop",
            children: [
                &#123;
                    name: "商家管理",
                    path: "/business/businessManage",
                    icon: "",
                &#125;,
            ],
        &#125;,
    ]
&#125;
const mutations = &#123;
    SET_MENU: (state: any, data: any) => &#123;
        state.menu = data
    &#125;
&#125;
const action = &#123;&#125;

export default &#123;
    namespace: true,
    state,
    mutations,
    action
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>store/getters.ts</code>获取：</p>
<pre><code class="copyable">#### store/getters.ts

const getters = &#123;
    menus: (state: any) => state.menu.menus,
&#125;

export default getters
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>store/index.ts</code>引入<code>modules</code>的模块：</p>
<pre><code class="copyable">#### store/index.ts

import &#123; createStore &#125; from 'vuex'
import getters from './getters'

interface MODULES &#123;
    [key: string]: any;
&#125;

const modulesList = require.context("./modules", false, /\.ts$/); 

const modules: MODULES = &#123;&#125;

modulesList.keys().forEach((modulePath:any) => &#123;
    const moduleName: string = modulePath.replace(/^\.\/(.*)\.\w+$/, '$1') //取文件名
    const value: any = modulesList(modulePath) //取文件的内容
    modules[moduleName] = value.default //赋值
&#125;)

const Store = createStore(&#123;
    modules,
    getters
&#125;)

export default Store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一顿操作。。结果悲剧了。。。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3428fbbae44f43a291b46092dbec115e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e92836523104b5ca48917fca4cc8f00~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
然后去百度了半天，结果是<code>vite</code>无法使用<code>require</code>，oh my god！那我想<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.cn%2Fguide%2Ffeatures.html%23json" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.cn/guide/features.html#json" ref="nofollow noopener noreferrer">从文件系统导入多个模块</a>怎么办？不死心的我又去翻了翻文档，发现了我想要的(-_-)..</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1460d5ba32594a989a494b66d1c7df84~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
真是印证了那句话。。。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7f080f5f1f84a398f16e2ba8f1158a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我错了，我改，马上改~ ~，修改后的：</p>
<pre><code class="copyable">#### store/index.ts

import &#123; createStore &#125; from 'vuex'
import getters from './getters'

interface MODULES &#123;
    [key: string]: any;
&#125;

// const modulesList = require.context("./modules", false, /\.ts$/); 
const modulesList = import.meta.globEager("./modules/*.ts")

const modules: MODULES = &#123;&#125;
for (const key in modulesList) &#123;
    const moduleName: string = key.replace(/^\.\/modules\/(.*)\.\w+$/, '$1') //取文件名
    const value: any = modulesList[key] //取文件的内容
    modules[moduleName] = value.default //赋值
&#125;
// modulesList.keys().forEach((modulePath:any) => &#123;
//     const moduleName: string = modulePath.replace(/^\.\/(.*)\.\w+$/, '$1') //取文件名
//     const value: any = modulesList(modulePath) //取文件的内容
//     modules[moduleName] = value.default //赋值
// &#125;)

const Store = createStore(&#123;
    modules,
    getters
&#125;)

export default Store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，上面做了这么多的准备，总得写点什么来体现一下吧(手动狗头)，整个页面的结构布局大概是下面这个样子。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbdbafa9c51747e6a0fe3eeac132a4cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>界面的整体布局规划完后，接下来就是“组装”的环节了，(@_@)~</p>
<p>新建几个文件：</p>
<ul>
<li>layouts/main.vue //页面整体结构</li>
<li>layouts/components/crumbs.vue //面包屑</li>
<li>layouts/components/header.vue //头部</li>
<li>layouts/Interface //这是个文件夹，存放各个模块的interface(具体的代码就不在这里细说了)</li>
<li>src/common/beforRouter.ts //作个简单的路由拦截</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c16a4f2ee454fdb91572dc573e76fea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38cb23cf5c314bc6aa70d55bf05945fc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>路由拦截就是用<code>beforeEach</code>这个导航钩子，实现起来比较简单，然后在<code>main.ts</code>中引入就行：</p>
<pre><code class="copyable">#### common/beforRouter.ts

import Router from '@/router'
// 路由拦截
Router.beforeEach((to: any, form: any, next: any) => &#123;
    if (to.path === '/login') &#123;
        next();
    &#125; else &#123;
        if (localStorage.getItem('token')) &#123;
            next()
        &#125; else &#123;
            next(&#123; path: '/login' &#125;)
        &#125;
    &#125;
&#125;)


#### main.ts 

import './common/beforRouter'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们接着去完善登录页的类容：</p>
<pre><code class="copyable">#### view/login/login.vue

<template>
  <div class="login">
    <div class="forms">
      <div class="title">不知道什么平台</div>
      <el-form label-width="80px">
        <el-form-item
          label="用户名："
          class="is-required"
        >
          <el-input
            v-model="user"
            size="small"
            placeholder="请输入用户名"
            @keyup.enter="goIndex"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="密&nbsp;&nbsp;&nbsp;&nbsp;码："
          class="is-required"
        >
          <el-input
            v-model="pwd"
            size="small"
            placeholder="请输入密码"
            show-password
            @keyup.enter="goIndex"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="验证码："
          class="is-required"
        >
          <el-input
            v-model="verCode"
            size="small"
            placeholder="请输入验证码"
            @keyup.enter="goIndex"
            style="width:50%"
          ></el-input>
          <div class="code">
            <verificationCode :identify-code="code" />
          </div>

        </el-form-item>
      </el-form>
      <div class="btn">
        <el-button
          style="width:100%;"
          size="small"
          type="primary"
          @click="goIndex"
        >登录</el-button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
// reactive：实现响应式数据的方法
// toRefs：将对象的多个属性都变成响应式数据
// getCurrentInstance：获取当前实例
// onMounted：生命周期mounted
import &#123; reactive, toRefs, getCurrentInstance, onMounted &#125; from "vue";
import &#123; useRouter &#125; from "vue-router";
import &#123; useStore &#125; from "vuex";
import &#123; ElMessage &#125; from "element-plus";
import "./interface/Login"; //引入之前定义好的interface
import verificationCode from "@/components/verificationCode.vue"; //生成验证码的组件这里就不细说了
export default &#123;
  name: "Login",
  components: &#123;
    verificationCode,
  &#125;,
  setup() &#123;
    const _this: any = getCurrentInstance(); //获取当前实例
    const store = useStore<any>(); // 使用vuex
    const menus = store.state.menu.menus; //获取之前存在vuex中的菜单
    const data: LoginData = reactive(&#123;
      user: "admin", //用户名
      pwd: "123456", //密码
      verCode: "", //用户输入的验证码
      code: "", //随机生成的验证码
      router: useRouter(),
      // 登录 跳转到首页
      goIndex: () => &#123;
        if (!data.user) &#123;
          ElMessage(&#123;
            message: "请输入用户名~",
            type: "warning",
            duration: 2000,
          &#125;);
          return false;
        &#125;
        if (!data.pwd) &#123;
          ElMessage(&#123;
            message: "请输入密码~",
            type: "warning",
            duration: 2000,
          &#125;);
          return false;
        &#125;
        if (!data.verCode) &#123;
          ElMessage(&#123;
            message: "请输入验证码~",
            type: "warning",
            duration: 2000,
          &#125;);
          return false;
        &#125;
        if (data.verCode != data.code) &#123;
          ElMessage(&#123;
            message: "验证码错误~",
            type: "warning",
            duration: 2000,
          &#125;);
          return false;
        &#125;
        if (data.user === "admin" && data.pwd === "123456") &#123; //模拟登录
          const menuList: string | null = JSON.stringify(menus);
          localStorage.setItem("menuList", menuList);
          localStorage.setItem("token", "456456456456456");
          localStorage.setItem("userName", "admin");
          data.router.push(&#123; path: "/business" &#125;);
        &#125; else &#123;
          ElMessage(&#123;
            message: "用户名或密码错误~",
            type: "warning",
            duration: 2000,
          &#125;);
          return false;
        &#125;
      &#125;,
      //随机验证码数字
      rand(min: number, max: number) &#123;
        return Math.floor(Math.random() * (max - min)) + min;
      &#125;,
      //更新验证码
      updateCode() &#123;
        data.code = String(data.rand(1000, 9999)); //4位验证码
      &#125;,
    &#125;);
    onMounted(() => &#123;
      data.updateCode();
    &#125;);
    const refData = toRefs(data);
    return &#123;
      ...refData,
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式我就不在这里说了，直接上图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a953e95bec1a4d56bcc06bcfc9a766fc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>输入验证码登录之后就可以看到，结合之前的东西就可以看到一个大致大轮廓：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bda1014e2724be4b77ad9588e453176~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">axios</h3>
<p>执行：<code>npm install axios</code> 安装 <code>axios</code>，在 <code>src</code> 下新建几个文件，还是采用从文件系统导入多个模块的思想：</p>
<ul>
<li>api/modules/admin.ts //存放接口函数</li>
<li>api/apiList.ts //将modules中的文件按模块导入</li>
<li>api/axios.ts //简单的axios封装</li>
<li>api/url.ts //运行环境的接口地址---> baseURL</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e867f7cd418c402e9007922b84892cc6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>apiList.ts</code>中的逻辑跟使用<code>vuex</code>时的逻辑基本一致。</p>
<pre><code class="copyable">#### api/apiList.ts

const req = import.meta.globEager("./modules/*.ts") 
// 定义一个api的对象
interface ApiObj &#123;
    [key: string]: any;
&#125;
const api: ApiObj = &#123;&#125;
for (const key in req) &#123;
    const name: string = key.replace(/^\.\/modules\/(.*)\.\w+$/, '$1') //取文件名
    const value: any = req[key] //取文件的内容
    api[name] = value.default //赋值
&#125;

const API = api
export default API


#### api/modules/admin.ts

import &#123; AxiosPromise &#125; from "axios";
import http from "../axios"; //来自api/axios.ts中的封装

const admin =&#123;
  userLogin(params: any): AxiosPromise<any> &#123;
    return http(&#123;
      url: "/auth-service/common/login", //接口
      method: "POST",
      data:params,
    &#125;);
  &#125;
&#125;
export default admin;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后将 <code>API</code> 挂载到全局：</p>
<pre><code class="copyable">#### main.ts

import API from "./api/apiList"

// 挂载
app.config.globalProperties.$API = API
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>view/login/login.vue</code> 中使用：</p>
<pre><code class="copyable">#### view/login/login.vue

import &#123; getCurrentInstance &#125; from "vue";

export default &#123;
  setup() &#123;
    const _this: any = getCurrentInstance(); //获取当前实例
    const API: any = _this.ctx.$API; //拿到全局挂载的$API接口
    
    API.admin.userLogin(obj).then((res: any) => &#123;
       .....     
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">结束</h1>
<p>现在公司的pc端项目就是根据这个模板更改来的，大家可以根据自己的业务需求去修改哦~~</p>
<p>参考文献：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fmigration%2Fintroduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/migration/introduction.html" ref="nofollow noopener noreferrer">Vue3中文文档</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.cn/" ref="nofollow noopener noreferrer">Vite中文文档</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Felement-plus.gitee.io%2F%23%2Fzh-CN" target="_blank" rel="nofollow noopener noreferrer" title="https://element-plus.gitee.io/#/zh-CN" ref="nofollow noopener noreferrer">Element Plus</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.tslang.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.tslang.cn/" ref="nofollow noopener noreferrer">TypeScript</a></li>
</ul></div>  
</div>
            