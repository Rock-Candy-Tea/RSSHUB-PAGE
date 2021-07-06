
---
title: '灵活运用JS开发技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3766'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 01:59:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=3766'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAdCAYAAABcz8ldAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAhgSURBVGhD7Zp7bBTHHcdn33t7vvOdzy+ITVKDU0xIKG2ABCPTRCCaUiEVKWoqRJuASAhCitRCVKSoalFUKZBiSmmFRRJKRUnUtIpo+aNqGgwoOCmuFUIRzxjwE4zte+97drYzztji8HPvtkit/PnH+n1397Tz+83vN/PbMZhmmmmm+d+BoX8n5diihcGqgFQf5vk6BMAskWUlw3GyFnIvtqWSf91w7mKC3npfOLX7wYeiIa6BBWCOLLFRF2NB0JvIOP/80YG+k2ev6S699b/OzOfKBW5l5KsgyC4DCFQDnpEAdE1goc/dlNPc/Up7P711UiYNSMuyxeUzZPnHgGHWh5XADEkSAcdiN+AnEXIBhBComgFU0/xQR+jnj51sOUMf9Z0NKyL8S9+JPBEN8zuCMrsqGOA5QWAAyzLAxe53HBeYFgJp1c5Cx33nyIfpV3e+22/Sx32nev/sMCgVnmM4bjOniAtZWQAsz315EfsGQQc4hgWcjHkCmOj1rheuNn95cXwmDMiVp5etC/D8m5FwUWVQUYYGPh6mZYFUOgsGVa1pXvOZzVT2jRuH54RM230jEuI3RcIiL4l4UkxAJmuD/riVsqD7ct2m9nep7BtVTbVfZ0uE/UIk+CQflAHDjf8+Lg6MldYATGpH3c/Ul7p3dWXppVGM6eElJSHmnQWPbSlRlN1lJcUBjqNRnwJZVQO3B5P/uq5rK1d90pakckFcaKp5UJHY92JR8YlwkUDVySEZfGfQdO7E7Z8s2HL9TSoXTPXRud9nA8IBqSwcZgWeqpPj6BYw7yTbXBN9q2v9lQEq5zBmWA8vWLCptCi4tzwW8RQMQlFQATPLSh6vCSh/plJBkMyQBHZfWYnkKRgEktEVpTJXERN2Xzo4ex2VC6K6qXYpF5b3ypVRT8EgcAERSJXRbwCBOTFzXblM5RxGBaRt+ZPYA+LO0mgxz5K1Ig+UgAzKIuGnz39z6S+olDeaibaXRsU1RUFvgx+GwTWgPCaDgMw2XXpr9gwq50XV0bkxJiYeEiNF5cwE5XsiOEkAUkXkUW51SSOVchjl8WKef604XFSRbzCGCYeCoESStv/p8QU1VPIM3knNDynctnBRfsEYhgSlNCIGgQv2UCkvGIHZgteMh1nBW9W4F16RAM6yDVV7amZTaYQcr59cuuhhWRTWBvAMLxQGeyFSHOLnh0MvUskz5RF+fbRYDEy0mZgqQYUHOLhr//b6rGoqeaLqQG0pw3PrBbyA+4EQUkRmhvgqNUfICUipKK4OKUqIJVPKB0jpEhjmWWp64jdbKmVZZNYogcJm493gsifOqhDyeh9GYR/FM7sW+DA5CKR0MSK3tvKZkpwB5gRE4tjFEr7RL0iWBGV51vHFCyupNGWWPqLgnoer9mtyEGSJAzwLllDTGzyznDjRN/CwOFkoFb4bm0eVIXICgpvdGoEvrF7fC89zfLkkeV5HbOhWiTwTpKYvCAJLGshRdXtKMKAWlyxq+MPQLk1h66g5RE5ABJYNFrqY3wvJklJRUKg5ZWLFXIA86yek2uDOPkBNb3CM5Pf7DL2QyIrUGiLH+xC5Bmmm/ARnHUhC6PnzxWDK0RH5HuIjZGy27erU9AZ0dTIWXyG+NpBBrSFySxZw220IqeUPFoS6jVAPNadM7yDsgNB1qOkLuAziMYIb1PQGA75wIaKGPyAb+9oF16g5RE5ALIQ+tSyLWoWDEAK6aXW3JlK9VJoyx1oyvVkNdvo5KXXDAVkdnaKmNwx0xjH98w3JNmTCm+Bc9hKVhsgJSI9pvp9Vdd++jmq6AXB2/HHrhcs5aTkVDv0DFzoHvKdq/mQsKX/4t7KJLDpOJW+IbAvMGoMkxfwAWZB8DT7W1diTE+WcgKz6pK1bs6z3daPwmJDsSKt6ZsCyjlLJMz0DsDGZ8SdlDROBjOb8YeWOjptU8kTXusuaazu7oJrfEnQvdkpVcUn6PTVHyAkIIW7br/Unklni0EJIZ1WgGsauZR+fvUglz6zY0dGfVp09ybRNlfwgi3k8YSbvJJ29VMoLt9v6rZVQL7hOYUubndHJGclBtzn1byqNMCogi09/2nFb01/oj+f/5TyjauBOKtPcZ1r7qZQ3f2lRfxZPWi2anp8TSDAGExZMa2jr8u03L1M5L7q3Xc+iAeuHRl/ScvPcjSLDBnZS/cjtNHd2v3171Ewbs9N5q7Pn4otVMx3btBsCsoRbk1FxG5dMVgMDqfTpXl1/tuFMa5zKefPROdX59qLQBwLnNog8Wy1OcjB1N+QEsW/QsFNZuO35Xb1v98QLX4/Sx+O3wqujrQ6013ABUWI8+AaqBjAH01+ghL22+5X2PirnMG7r+esbnae/V1neauvGSoHjigTcVU7UGFm2DeK4ttxKpQ+mLPvl+o/PjnkAkw9HTqSMmVHhyAMx9iFcSh/BHTfLceO/C8mKjApBf9zszGhoY92m9sN+BGOY9AeD7eGniv8OTaOB4dgyTsQd9wS+IQu4lciYdkI7CLrNH3Rvbb9FL41i0tbzVP2iWJkobpN5fmM4IJfJskTP1Bk8A9HQmbpmGDBrWqdVCN/Yd7PjxKGOXn+bmbto3feVVcVB9qehIL8EJy8nChwgr0O2xxBnhGU5eP2CfYbl/m4gBRsbtneMORP9oGpjpcCsiKzHHfdOPiQ/wMniyFEu2dbiTQCAeN/vavC466BGYLttXc9fmXBXMGlAhiHHur+sq6uPiUI9z7CVHMPwBnLSuuN8FuC48/Oaz1ylt94XfrW5ouyprwWfYRkwNyCyYYjwkBHows1fa+tV/fzGxlv39b9gqvfPmQ+i/HK8KlcBjhHwfl8HEHyOd1JnuzZd66S3TTPNNNP8/wDAfwDG7G0m9LKBpwAAAABJRU5ErkJggg==) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><h1 data-id="heading-0">灵活运用JS开发技巧</h1>
<p><a href="https://juejin.cn/post/6844903838449664013" target="_blank">原文链接：Joway Young</a></p>
<h3 data-id="heading-1">目录</h3>
<ul>
<li><code>String Skill</code>：<strong>字符串技巧</strong></li>
<li><code>Number Skill</code>：<strong>数值技巧</strong></li>
<li><code>Boolean Skill</code>：<strong>布尔技巧</strong></li>
<li><code>Array Skill</code>：<strong>数组技巧</strong></li>
<li><code>Object Skill</code>：<strong>对象技巧</strong></li>
<li><code>Function Skill</code>：<strong>函数技巧</strong></li>
<li><code>DOM Skill</code>：<strong>DOM技巧</strong></li>
</ul>
<p><a href="https://es6.ruanyifeng.com/" target="_blank" rel="nofollow noopener noreferrer">《ES6标准入门》</a></p>
<h2 data-id="heading-2">String Skill</h2>
<h3 data-id="heading-3">对比时间</h3>
<blockquote>
<p>时间个位数形式需补0</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> time1 = <span class="hljs-string">"2019-02-14 21:00:00"</span>;
<span class="hljs-keyword">const</span> time2 = <span class="hljs-string">"2019-05-01 09:00:00"</span>;
<span class="hljs-keyword">const</span> overtime = time1 > time2;
<span class="hljs-comment">// overtime => false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">格式化金钱</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ThousandNum = <span class="hljs-function"><span class="hljs-params">num</span> =></span> num.toString().replace(<span class="hljs-regexp">/\B(?=(\d&#123;3&#125;)+(?!\d))/g</span>, <span class="hljs-string">","</span>);
<span class="hljs-keyword">const</span> money = ThousandNum(<span class="hljs-number">20190214</span>);
<span class="hljs-comment">// money => "20,190,214"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">生成随机ID</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> RandomId = <span class="hljs-function"><span class="hljs-params">len</span> =></span> <span class="hljs-built_in">Math</span>.random().toString(<span class="hljs-number">36</span>).substr(<span class="hljs-number">3</span>, len);
<span class="hljs-keyword">const</span> id = RandomId(<span class="hljs-number">10</span>);
<span class="hljs-comment">// id => "jg7zpgiqva"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">生成随机HEX色值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> RandomColor = <span class="hljs-function">() =></span> <span class="hljs-string">"#"</span> + <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">0xffffff</span>).toString(<span class="hljs-number">16</span>).padEnd(<span class="hljs-number">6</span>, <span class="hljs-string">"0"</span>);
<span class="hljs-keyword">const</span> color = RandomColor();
<span class="hljs-comment">// color => "#f03665"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">生成星级评分</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> StartScore = <span class="hljs-function"><span class="hljs-params">rate</span> =></span> <span class="hljs-string">"★★★★★☆☆☆☆☆"</span>.slice(<span class="hljs-number">5</span> - rate, <span class="hljs-number">10</span> - rate);
<span class="hljs-keyword">const</span> start = StartScore(<span class="hljs-number">3</span>);
<span class="hljs-comment">// start => "★★★"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">操作URL查询参数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> params = <span class="hljs-keyword">new</span> URLSearchParams(location.search.replace(<span class="hljs-regexp">/\?/ig</span>, <span class="hljs-string">""</span>)); <span class="hljs-comment">// location.search = "?name=young&sex=male"</span>
params.has(<span class="hljs-string">"young"</span>); <span class="hljs-comment">// true</span>
params.get(<span class="hljs-string">"sex"</span>); <span class="hljs-comment">// "male"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">Number Skill</h2>
<h3 data-id="heading-10">取整</h3>
<blockquote>
<p>代替正数的 <code>Math.floor()</code>，代替负数的 <code>Math.ceil()</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> num1 = ~~ <span class="hljs-number">1.69</span>;
<span class="hljs-keyword">const</span> num2 = <span class="hljs-number">1.69</span> | <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> num3 = <span class="hljs-number">1.69</span> >> <span class="hljs-number">0</span>;
<span class="hljs-comment">// num1 num2 num3 => 1 1 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">补零</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> FillZero = <span class="hljs-function">(<span class="hljs-params">num, len</span>) =></span> num.toString().padStart(len, <span class="hljs-string">"0"</span>);
<span class="hljs-keyword">const</span> num = FillZero(<span class="hljs-number">169</span>, <span class="hljs-number">5</span>);
<span class="hljs-comment">// num => "00169"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">转数值</h3>
<blockquote>
<p>只对null、""、false、数值字符串有效</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> num1 = +<span class="hljs-literal">null</span>;
<span class="hljs-keyword">const</span> num2 = +<span class="hljs-string">""</span>;
<span class="hljs-keyword">const</span> num3 = +<span class="hljs-literal">false</span>;
<span class="hljs-keyword">const</span> num4 = +<span class="hljs-string">"169"</span>;
<span class="hljs-comment">// num1 num2 num3 num4 => 0 0 0 169</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">时间戳</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> timestamp = +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">"2019-02-14"</span>);
<span class="hljs-comment">// timestamp => 1550102400000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">精确小数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> RoundNum = <span class="hljs-function">(<span class="hljs-params">num, decimal</span>) =></span> <span class="hljs-built_in">Math</span>.round(num * <span class="hljs-number">10</span> ** decimal) / <span class="hljs-number">10</span> ** decimal;
<span class="hljs-keyword">const</span> num = RoundNum(<span class="hljs-number">1.69</span>, <span class="hljs-number">1</span>);
<span class="hljs-comment">// num => 1.7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">判断奇偶</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> RoundNum = <span class="hljs-function">(<span class="hljs-params">num, decimal</span>) =></span> <span class="hljs-built_in">Math</span>.round(num * <span class="hljs-number">10</span> ** decimal) / <span class="hljs-number">10</span> ** decimal;
<span class="hljs-keyword">const</span> num = RoundNum(<span class="hljs-number">1.69</span>, <span class="hljs-number">1</span>);
<span class="hljs-comment">// num => 1.7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">取最小最大值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
<span class="hljs-keyword">const</span> min = <span class="hljs-built_in">Math</span>.min(...arr);
<span class="hljs-keyword">const</span> max = <span class="hljs-built_in">Math</span>.max(...arr);
<span class="hljs-comment">// min max => 0 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">生成范围随机数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> RandomNum = <span class="hljs-function">(<span class="hljs-params">min, max</span>) =></span> <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * (max - min + <span class="hljs-number">1</span>)) + min;
<span class="hljs-keyword">const</span> num = RandomNum(<span class="hljs-number">1</span>, <span class="hljs-number">10</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">Boolean Skill</h2>
<h3 data-id="heading-19">短路运算</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = d && <span class="hljs-number">1</span>; <span class="hljs-comment">// 满足条件赋值：取假运算，从左到右依次判断，遇到假值返回假值，后面不再执行，否则返回最后一个真值</span>
<span class="hljs-keyword">const</span> b = d || <span class="hljs-number">1</span>; <span class="hljs-comment">// 默认赋值：取真运算，从左到右依次判断，遇到真值返回真值，后面不再执行，否则返回最后一个假值</span>
<span class="hljs-keyword">const</span> c = !d; <span class="hljs-comment">// 取假赋值：单个表达式转换为true则返回false，否则返回true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">判断数据类型</h3>
<pre><code class="copyable">可判断类型：undefined、null、string、number、boolean、array、object、symbol、date、regexp、function、asyncfunction、arguments、set、map、weakset、weakmap
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DataType</span>(<span class="hljs-params">tgt, type</span>) </span>&#123;
    <span class="hljs-keyword">const</span> dataType = <span class="hljs-built_in">Object</span>.prototype.toString.call(tgt).replace(<span class="hljs-regexp">/\[object (\w+)\]/</span>, <span class="hljs-string">"$1"</span>).toLowerCase();
    <span class="hljs-keyword">return</span> type ? dataType === type : dataType;
&#125;
DataType(<span class="hljs-string">"young"</span>); <span class="hljs-comment">// "string"</span>
DataType(<span class="hljs-number">20190214</span>); <span class="hljs-comment">// "number"</span>
DataType(<span class="hljs-literal">true</span>); <span class="hljs-comment">// "boolean"</span>
DataType([], <span class="hljs-string">"array"</span>); <span class="hljs-comment">// true</span>
DataType(&#123;&#125;, <span class="hljs-string">"array"</span>); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">是否为空数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [];
<span class="hljs-keyword">const</span> flag = <span class="hljs-built_in">Array</span>.isArray(arr) && !arr.length;
<span class="hljs-comment">// flag => true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">是否为空对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;&#125;;
<span class="hljs-keyword">const</span> flag = DataType(obj, <span class="hljs-string">"object"</span>) && !<span class="hljs-built_in">Object</span>.keys(obj).length;
<span class="hljs-comment">// flag => true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">满足条件时执行</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> flagA = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 条件A</span>
<span class="hljs-keyword">const</span> flagB = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 条件B</span>
(flagA || flagB) && Func(); <span class="hljs-comment">// 满足A或B时执行</span>
(flagA || !flagB) && Func(); <span class="hljs-comment">// 满足A或不满足B时执行</span>
flagA && flagB && Func(); <span class="hljs-comment">// 同时满足A和B时执行</span>
flagA && !flagB && Func(); <span class="hljs-comment">// 满足A且不满足B时执行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">为非假值时执行</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> flag = <span class="hljs-literal">false</span>; <span class="hljs-comment">// undefined、null、""、0、false、NaN</span>
!flag && Func();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">数组不为空时执行</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
arr.length && Func();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">对象不为空时执行</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-built_in">Object</span>.keys(obj).length && Func();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">函数退出代替条件分支退出</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (flag) &#123;
    Func();
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="hljs-comment">// 换成</span>
<span class="hljs-keyword">if</span> (flag) &#123;
    <span class="hljs-keyword">return</span> Func();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">switch/case 使用区间</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> age = <span class="hljs-number">26</span>;
<span class="hljs-keyword">switch</span> (<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-built_in">isNaN</span>(age):
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"not a number"</span>);
        <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> (age < <span class="hljs-number">18</span>):
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"under age"</span>);
        <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> (age >= <span class="hljs-number">18</span>):
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"adult"</span>);
        <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">default</span>:
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"please set your age"</span>);
        <span class="hljs-keyword">break</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">Array Skill</h2>
<h3 data-id="heading-30">克隆数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> _arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
<span class="hljs-keyword">const</span> arr = [..._arr];
<span class="hljs-comment">// arr => [0, 1, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">合并数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr1 = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
<span class="hljs-keyword">const</span> arr2 = [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
<span class="hljs-keyword">const</span> arr = [...arr1, ...arr2];
<span class="hljs-comment">// arr => [0, 1, 2, 3, 4, 5];</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">去重数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [...new <span class="hljs-built_in">Set</span>([<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>])];
<span class="hljs-comment">// arr => [0, 1, null]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">混淆数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>].slice().sort(<span class="hljs-function">() =></span> <span class="hljs-built_in">Math</span>.random() - <span class="hljs-number">.5</span>);
<span class="hljs-comment">// arr => [3, 4, 0, 5, 1, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">清空数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
arr.length = <span class="hljs-number">0</span>;
<span class="hljs-comment">// arr => []</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">截断数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>]
arr.length = <span class="hljs-number">2</span>;
<span class="hljs-comment">// arr => [0, 1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">交换赋值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-number">1</span>;
[a, b] = [b, a];
<span class="hljs-comment">// ab => 1 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">过滤空值</h3>
<blockquote>
<p>空值： undefined、null、""、0、false、NaN</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-literal">undefined</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">""</span>, <span class="hljs-number">0</span>, <span class="hljs-literal">false</span>, <span class="hljs-literal">NaN</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>].filter(<span class="hljs-built_in">Boolean</span>);
<span class="hljs-comment">// arr => [1, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">异步累计</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Func</span>(<span class="hljs-params">deps</span>) </span>&#123;
    <span class="hljs-keyword">return</span> deps.reduce(<span class="hljs-keyword">async</span>(t, v) => &#123;
        <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">await</span> t;
        <span class="hljs-keyword">const</span> version = <span class="hljs-keyword">await</span> Todo(v);
        dep[v] = version;
        <span class="hljs-keyword">return</span> dep
    &#125;, <span class="hljs-built_in">Promise</span>.resolve(&#123;&#125;));
&#125;

<span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> Func(); <span class="hljs-comment">// 需要async 包围下使用</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-39">数组首部插入成员</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]; <span class="hljs-comment">// 以下方法任选一种</span>
arr.unshift(<span class="hljs-number">0</span>);
arr = [<span class="hljs-number">0</span>].concat(arr);
arr = [<span class="hljs-number">0</span>,...arr];
<span class="hljs-comment">// arr => [0, 1, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">数组尾部插入成员</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>]; <span class="hljs-comment">// 以下方法任选一种</span>
arr.push(<span class="hljs-number">2</span>);
arr.concat(<span class="hljs-number">2</span>);
arr[arr.length] = <span class="hljs-number">2</span>;
arr = [...arr, <span class="hljs-number">2</span>];
<span class="hljs-comment">// arr => [0, 1, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">统计数组成员个数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>];
<span class="hljs-keyword">const</span> count = arr.reduce(<span class="hljs-function">(<span class="hljs-params">t, v</span>) =></span> &#123;
    t[v] = t[v] ? ++[v] : <span class="hljs-number">1</span>;
    <span class="hljs-keyword">return</span> t;
&#125;,&#123;&#125;);
<span class="hljs-comment">// count => &#123; 0: 1, 1: 2, 2: 3 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">解构数组成员嵌套</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>]]];
<span class="hljs-keyword">const</span> [a, b, [c, d, [e, f]]] = arr;
<span class="hljs-comment">// a b c d e f => 0 1 2 3 4 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">结构数组成员别名</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
<span class="hljs-keyword">const</span> &#123; <span class="hljs-number">0</span>: a, <span class="hljs-number">1</span>: b, <span class="hljs-number">2</span>: c &#125; = arr
<span class="hljs-comment">// a b c => 0 1 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">结构数组成员默认值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
<span class="hljs-keyword">const</span> [a, b, c = <span class="hljs-number">3</span>, d = <span class="hljs-number">4</span>] = arr;
<span class="hljs-comment">// a b c d => 0 1 2 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-45">获取随机数成员</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
<span class="hljs-keyword">const</span> randomItem = arr[<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * arr.length)];
<span class="hljs-comment">// randomItem => 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-46">创建指定长度数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [...new <span class="hljs-built_in">Array</span>(<span class="hljs-number">3</span>).keys()];
<span class="hljs-comment">// arr => [0, 1, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-47">创建指定长度且值相等的数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">3</span>).fill(<span class="hljs-number">0</span>);
<span class="hljs-comment">// arr => [0, 0, 0]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-48">reduce代替map和filter</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> _arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];

<span class="hljs-comment">// map</span>
<span class="hljs-keyword">const</span> arr = _arr.map(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v * <span class="hljs-number">2</span>);
<span class="hljs-keyword">const</span> arr = _arr.reduce(<span class="hljs-function">(<span class="hljs-params">t, v</span>) =></span> &#123;
    t.push(v * <span class="hljs-number">2</span>);
    <span class="hljs-keyword">return</span> t;
&#125;, []);
<span class="hljs-comment">// arr => [0, 2, 4]</span>

<span class="hljs-comment">// filter</span>
<span class="hljs-keyword">const</span> arr = _arr.filter(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v > <span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> arr = _arr.reduce(<span class="hljs-function">(<span class="hljs-params">t, v</span>) =></span> &#123;
    v > <span class="hljs-number">0</span> && t.push(v);
    <span class="hljs-keyword">return</span> t;
&#125;, []);
<span class="hljs-comment">// arr => [1, 2]</span>

<span class="hljs-comment">// map 和 filter</span>
<span class="hljs-keyword">const</span> arr = _arr.map(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v * <span class="hljs-number">2</span>).filter(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v > <span class="hljs-number">2</span>);
<span class="hljs-keyword">const</span> arr = _arr.reduce(<span class="hljs-function">(<span class="hljs-params">t, v</span>) =></span> &#123;
    v = v * <span class="hljs-number">2</span>;
    v > <span class="hljs-number">2</span> && t.push(v);
    <span class="hljs-keyword">return</span> t;
&#125;, []);
<span class="hljs-comment">// arr => [4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-49">Object Skill</h2>
<h3 data-id="heading-50">克隆对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> _obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">const</span> obj = &#123; ..._obj &#125;;
<span class="hljs-keyword">const</span> obj = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(_obj));
<span class="hljs-comment">// obj => &#123; a: 0, b: 1, c: 2 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-51">合并对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj1 = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">const</span> obj2 = &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">d</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">e</span>: <span class="hljs-number">5</span> &#125;;
<span class="hljs-keyword">const</span> obj = &#123; ...obj1, ...obj2 &#125;;
<span class="hljs-comment">// obj => &#123; a: 0, b: 1, c: 3, d: 4, e: 5 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-52">对象字面量</h3>
<blockquote>
<p>获取环境变量时必用此方法，用它一直爽，一直用它一直爽</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> env = <span class="hljs-string">"prod"</span>;
<span class="hljs-keyword">const</span> link = &#123;
    <span class="hljs-attr">dev</span>: <span class="hljs-string">"Development Address"</span>,
    <span class="hljs-attr">test</span>: <span class="hljs-string">"Testing Address"</span>,
    <span class="hljs-attr">prod</span>: <span class="hljs-string">"Production Address"</span>
&#125;[env];

<span class="hljs-comment">// link => "Production Address"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-53">对象变量属性</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> flag = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>,
    [flag ? <span class="hljs-string">"c"</span> : <span class="hljs-string">"d"</span>]: <span class="hljs-number">2</span>
&#125;;
<span class="hljs-comment">// obj => &#123; a: 0, b: 1, d: 2 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-54">创建纯空对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
<span class="hljs-built_in">Object</span>.prototype.a = <span class="hljs-number">0</span>;
<span class="hljs-comment">// obj => &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-55">删除对象无用属性</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">2</span> &#125;; <span class="hljs-comment">// 只想拿b和c</span>
<span class="hljs-keyword">const</span> &#123; a, ...rest &#125; = obj;
<span class="hljs-comment">// rest => &#123; b: 1, c: 2 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-56">解构对象属性嵌套</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">c</span>: &#123; <span class="hljs-attr">d</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">e</span>: <span class="hljs-number">3</span> &#125; &#125;;
<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">c</span>: &#123; d, e &#125; &#125; = obj;
<span class="hljs-comment">// d e => 2 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-57">解构对象属性别名</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">const</span> &#123; a, <span class="hljs-attr">b</span>: d, <span class="hljs-attr">c</span>: e &#125; = obj;
<span class="hljs-comment">// a d e => 0 1 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-58">解构对象属性默认值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">const</span> &#123; a, b = <span class="hljs-number">2</span>, d = <span class="hljs-number">3</span>&#125; = obj;
<span class="hljs-comment">// a b d => 0 1 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-59">Function Skill</h2>
<h3 data-id="heading-60">函数自执行</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Func = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;(); <span class="hljs-comment">// 常用</span>

(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;)(); <span class="hljs-comment">// 常用</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;()); <span class="hljs-comment">// 常用</span>
[<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;()];

+ <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
- <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
~ <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
! <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();

<span class="hljs-keyword">new</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
<span class="hljs-keyword">new</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
<span class="hljs-keyword">typeof</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
<span class="hljs-keyword">delete</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();

<span class="hljs-number">1</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
<span class="hljs-number">1</span> ^ <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
<span class="hljs-number">1</span> > <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-61">隐式函数返回值</h3>
<blockquote>
<p>只能用于<code>单语句返回值箭头函数</code>，如果返回值是对象必须使用()包住</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Func = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"I Love "</span> + name
&#125;

<span class="hljs-comment">// 换成</span>
<span class="hljs-keyword">const</span> Func = <span class="hljs-function"><span class="hljs-params">name</span> =></span> <span class="hljs-string">"I Love "</span> + name;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-62">一次性函数</h3>
<blockquote>
<p>适用于运行一些只需要执行一次的初始化代码</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Func</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"x"</span>)
    Func = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"y"</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-63">惰性载入函数</h3>
<blockquote>
<p>函数内判断分支较多较复杂时可以大大节约资源开销</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Func</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (a === b)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"x"</span>);
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Y"</span>);
    &#125;
&#125;

<span class="hljs-comment">// 换成</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Func</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span>(a === b) &#123;
        Func = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"x"</span>)
        &#125;
    &#125;<span class="hljs-keyword">else</span> &#123;
        Func = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"y"</span>)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> Func();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-64">检测非空参数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">IsRequired</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"param is required"</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Func</span>(<span class="hljs-params">name = IsRequired()</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"I Love"</span> + name)
&#125;
Func(); <span class="hljs-comment">// "param is required"</span>
Func(<span class="hljs-string">"You"</span>) <span class="hljs-comment">// "I Love You"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-65">字符串创建函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Func = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">"name"</span>, <span class="hljs-string">"console.log(\"I Love \" + name)"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-66">优雅处理错误信息</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
    Func();
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
    location.href = <span class="hljs-string">"https://stackoverflow.com/search?q=[js]+"</span> + e.message;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-67">优雅处理 Async/ Await 参数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">AsyncTo</span>(<span class="hljs-params">promise</span>) </span>&#123;
    <span class="hljs-keyword">return</span> promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> [<span class="hljs-literal">null</span>, data]).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> [err]);
&#125;
<span class="hljs-keyword">const</span> [err, res] = <span class="hljs-keyword">await</span> AsyncTo(Func());
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-68">优雅处理多个函数返回值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Func</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all([
        fetch(<span class="hljs-string">"/user"</span>),
        fetch(<span class="hljs-string">"/comment"</span>)
    ])
&#125;

<span class="hljs-keyword">const</span> [user, comment] = <span class="hljs-keyword">await</span> Func(); <span class="hljs-comment">// 需在async 包围下使用</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-69">DOM Skill</h2>
<h3 data-id="heading-70">显示全部DOM边框</h3>
<blockquote>
<p>调试页面元素边界时使用</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">[].forEach.call($$(<span class="hljs-string">"*"</span>), <span class="hljs-function"><span class="hljs-params">dom</span> =></span> &#123;
    dom.style.outline = <span class="hljs-string">"1px solid #"</span> + (~~(<span class="hljs-built_in">Math</span>.random() * (<span class="hljs-number">1</span> << <span class="hljs-number">24</span>))).toString(<span class="hljs-number">16</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-71">自适应页面</h3>
<blockquote>
<p>页面基于一张设计图但需要做多款机型自适应，元素尺寸使用rem进行设置</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">AutoResponse</span>(<span class="hljs-params">width = <span class="hljs-number">750</span></span>) </span>&#123;
    <span class="hljs-keyword">const</span> target = <span class="hljs-built_in">document</span>.documentElement;
    target.clientWidth >= <span class="hljs-number">600</span>
        ? (target.style.fontSize = <span class="hljs-string">"80px"</span>)
        : (target.style.fontSize = target.clientWidth / width * <span class="hljs-number">100</span> + <span class="hljs-string">"px"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-72">过滤XSS</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FilterXss</span>(<span class="hljs-params">content</span>) </span>&#123;
    <span class="hljs-keyword">let</span> elem = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
    elem.innerText = content;
    <span class="hljs-keyword">const</span> result = elem.innerHTML;
    elem = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-73">存取LocalStorage</h3>
<blockquote>
<p>反序列化取， 序列化存</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">"love"</span>, <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-string">"I Love You"</span>));
<span class="hljs-keyword">const</span> love = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">"love"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>键盘</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-params">_</span>=></span>[...<span class="hljs-string">"`1234567890-=~~QWERTYUIOP[]\\~ASDFGHJKL;'~~ZXCVBNM,./~"</span>].map(<span class="hljs-function"><span class="hljs-params">x</span>=></span>(o+=<span class="hljs-string">`/<span class="hljs-subst">$&#123;b=<span class="hljs-string">'_'</span>.repeat(w=x<y?<span class="hljs-number">2</span>:<span class="hljs-string">' 667699'</span>[x=[<span class="hljs-string">"Bs"</span>,<span class="hljs-string">"Tab"</span>,<span class="hljs-string">"Caps"</span>,<span class="hljs-string">"Enter"</span>][p++]||<span class="hljs-string">'Shift'</span>,p])&#125;</span>\\|`</span>,m+=y+(x+<span class="hljs-string">'    '</span>).slice(<span class="hljs-number">0</span>,w)+y+y,n+=y+b+y+y,l+=<span class="hljs-string">' __'</span>+b)[<span class="hljs-number">73</span>]&&(k.push(l,m,n,o),l=<span class="hljs-string">''</span>,m=n=o=y),m=n=o=y=<span class="hljs-string">'|'</span>,p=l=k=[])&&k.join<span class="hljs-string">`
`</span>)()
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            