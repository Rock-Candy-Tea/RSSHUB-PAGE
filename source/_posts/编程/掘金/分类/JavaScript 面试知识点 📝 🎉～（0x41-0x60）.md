
---
title: 'JavaScript 面试知识点 📝 🎉～（0x41-0x60）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58f0eeec2d8c44c58acb0c977dd3d750~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 19:58:02 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58f0eeec2d8c44c58acb0c977dd3d750~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">TOC</h2>
<ul>
<li><a href="https://juejin.cn/post/7001664785645305887" target="_blank" title="https://juejin.cn/post/7001664785645305887">JavaScript 面试知识点 📝 🎉～（0x01-0x20）</a></li>
<li><a href="https://juejin.cn/post/7001673224350072845" target="_blank" title="https://juejin.cn/post/7001673224350072845">JavaScript 面试知识点 📝 🎉～（0x21-0x40）</a></li>
<li><em><strong>> <a href="https://juejin.cn/post/7001689046213165093" target="_blank" title="https://juejin.cn/post/7001689046213165093">JavaScript 面试知识点 📝 🎉～（0x41-0x60）</a></strong></em></li>
<li><a href="https://juejin.cn/post/7001694334043029541" target="_blank" title="https://juejin.cn/post/7001694334043029541">JavaScript 面试知识点 📝 🎉～（0x61-0x80）</a></li>
</ul>
<h3 data-id="heading-1">记得<strong>三连+关注</strong>嗷嗷～</h3>
<h2 data-id="heading-2">0x41 JavaScript 的 Date 有什么缺点？有什么解决方案？</h2>
<p>JavaScript 的日期处理 API 比较糟糕，因为它是直接对 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fjavase%2F6%2Fdocs%2Fapi%2Fjava%2Futil%2FDate" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/javase/6/docs/api/java/util/Date" ref="nofollow noopener noreferrer">Java 的 <code>Date</code> 类</a> 进行复制来实现了 <code>Date</code> 对象，而 Java 维护者最终弃用了许多 <code>Date</code> 类的方法，并于 1997 年创建了 <code>Calendar</code> 类以取代它。</p>
<p>但是 JavaScript 的 <code>Date</code> API 还没有进行进一步修复，这就是为什么我们今天会遇到以下问题：</p>
<ul>
<li><code>Date</code> 对象是可变的</li>
<li>用于日期和时间计算的混乱 API（例如，天数的加减）</li>
<li>仅支持 UTC 和本地时区</li>
<li>从字符串中解析日期的不可靠</li>
<li>不支持公历以外的其他历法</li>
</ul>
<p>但由于目前 <code>Date</code> API 被广泛地应用于各种库和浏览器引擎中，我们暂时不可能修复其错误部分。如果我们更改它的底层实现，就会很可能对许多现有的网站和库造成破坏性影响。</p>
<p>新的 <code>Temporal</code> API 提案旨在解决 <code>Date</code> API 的问题，它对 JavaScript 的日期和时间操作进行了以下改进：</p>
<ul>
<li>仅创建和处理不可变的 <code>Temporal</code> 对象</li>
<li>用于日期和时间计算的简单 API</li>
<li>支持所有时区</li>
<li>遵循 ISO-8601 格式进行严格的日期解析</li>
<li>支持非公历的历法</li>
</ul>
<blockquote>
<p>请记住，<code>Temporal</code> 提案<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-temporal%23status" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tc39/proposal-temporal#status" ref="nofollow noopener noreferrer">当前处于第三阶段</a>，尚未准备好用于生产环境中。</p>
</blockquote>
<p>让我们借助代码示例理解 <code>Temporal</code> API 的功能吧。下文中的所有 <code>Temporal</code> API 代码都是使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fproposal-temporal" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/proposal-temporal" ref="nofollow noopener noreferrer">Temporal Polyfill</a> 创建的。</p>
<h3 data-id="heading-3">41.1 不可变的日期对象</h3>
<p>使用 JavaScript 的 <code>new Date()</code> 构造器创建的 <code>Date</code> 对象是可变的，意味着你可以在初始化以后修改它的值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">"2021-02-20"</span>);
<span class="hljs-built_in">console</span>.log(date); <span class="hljs-comment">// 2021-02-20T00:00:00.000Z</span>
date.setYear(<span class="hljs-number">2000</span>);
<span class="hljs-built_in">console</span>.log(date); <span class="hljs-comment">// 2000-02-20T00:00:00.000Z</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽管看似无关紧要，但这种可变的对象在处理不当时可能会导致错误，其中一种情况就是当我们尝试将天数添加到当前日期时。</p>
<p>例如，这是一个将当前日期增加一周的功能。 由于 <code>setDate</code> 会修改对象本身，因此我们会得到<strong>两个具有相同日期值的对象</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addOneWeek</span>(<span class="hljs-params">date</span>) </span>&#123;
    date.setDate(date.getDate() + <span class="hljs-number">7</span>);
    <span class="hljs-keyword">return</span> date;
&#125;

<span class="hljs-keyword">let</span> today = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">let</span> oneWeekLater = addOneWeek(today);

<span class="hljs-built_in">console</span>.log(today);
<span class="hljs-built_in">console</span>.log(oneWeekLater); <span class="hljs-comment">//  值和变量 today 一样</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Temporal</code> 提供了不直接修改对象的方法，进而修复了这个问题，例如下面就是使用 <code>Temporal</code> API 添加一周的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> date = Temporal.now.plainDateISO();
<span class="hljs-built_in">console</span>.log(date); <span class="hljs-comment">// 2021-02-20</span>
<span class="hljs-built_in">console</span>.log(date.add(&#123;<span class="hljs-attr">days</span>: <span class="hljs-number">7</span>&#125;)); <span class="hljs-comment">// 2021-02-27</span>
<span class="hljs-built_in">console</span>.log(date); <span class="hljs-comment">// 2021-02-20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上面的代码所示，<code>Temporal</code> 为我们提供了 <code>.add()</code> 方法，让我们能将天、周、月或年添加到当前日期对象中而不会修改原始值。</p>
<h3 data-id="heading-4">41.2 用于日期和时间计算的 API</h3>
<p>前面的 <code>Temporal</code> 示例中我们了解到了 <code>.add()</code> 方法，它能帮助我们对日期对象执行计算。我们现在使用的 <code>Date</code> API 仅提供了获取和设置日期值的方法，不如 <code>Temporal</code> 来得简单直接。</p>
<p><code>Temporal</code> 还为我们提供了多个 API 来计算日期值。比如说 <code>until()</code> 方法，它可以计算 <code>firstDate</code> 和 <code>secondDate</code> 之间的时间差。</p>
<p>而如果使用 <code>Date</code> API，我们需要手动计算两个日期之间的天数，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> oneDay = <span class="hljs-number">24</span> * <span class="hljs-number">60</span> * <span class="hljs-number">60</span> * <span class="hljs-number">1000</span>;
<span class="hljs-keyword">const</span> firstDate = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">2008</span>, <span class="hljs-number">1</span>, <span class="hljs-number">12</span>);
<span class="hljs-keyword">const</span> secondDate = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">2008</span>, <span class="hljs-number">1</span>, <span class="hljs-number">22</span>);

<span class="hljs-keyword">const</span> diffDays = <span class="hljs-built_in">Math</span>.round(<span class="hljs-built_in">Math</span>.abs((firstDate - secondDate) / oneDay));
<span class="hljs-built_in">console</span>.log(diffDays); <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是 <code>Temporal</code> API，我们可以通过 <code>until()</code> 方法简单地计算 <code>diffDays</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> firstDate = Temporal.PlainDate.from(<span class="hljs-string">"2008-01-12"</span>);
<span class="hljs-keyword">const</span> secondDate = Temporal.PlainDate.from(<span class="hljs-string">"2008-01-22"</span>);

<span class="hljs-keyword">const</span> diffDays = firstDate.until(secondDate).days;
<span class="hljs-built_in">console</span>.log(diffDays); <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他的帮助我们计算的方法还有：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fproposal-temporal%2Fdocs%2Fplaindate.html%23subtract" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/proposal-temporal/docs/plaindate.html#subtract" ref="nofollow noopener noreferrer"><code>.subtract()</code> 方法</a>，用于减少当前日期的天数、月数或年数。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fproposal-temporal%2Fdocs%2Fplaindate.html%23since" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/proposal-temporal/docs/plaindate.html#since" ref="nofollow noopener noreferrer"><code>.since()</code> 方法</a>，用于计算一个特定日期迄今为止所经历的天数、月数或年数。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fproposal-temporal%2Fdocs%2Fplaindate.html%23equals" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/proposal-temporal/docs/plaindate.html#equals" ref="nofollow noopener noreferrer"><code>.equals()</code> 方法</a>，用于比较两个日期是否相同。</li>
</ul>
<p>这些 API 能够帮助我们去完成计算，而无需自己创建解决方案。</p>
<h3 data-id="heading-5">41.3 支持所有时区</h3>
<p>当前的 <code>Date</code> API 在系统中以 UTC 标准跟踪时间，通常会在计算机的时区中生成日期对象，操纵时区没有简单的方法。</p>
<p>我发现操纵时区的一种方式是使用 <code>Date.toLocaleString()</code> 方法，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">let</span> tokyoDate = date.toLocaleString(<span class="hljs-string">"en-US"</span>, &#123;
    <span class="hljs-attr">timeZone</span>: <span class="hljs-string">"Asia/Tokyo"</span>,
&#125;);
<span class="hljs-keyword">let</span> singaporeDate = date.toLocaleString(<span class="hljs-string">"en-US"</span>, &#123;
    <span class="hljs-attr">timeZone</span>: <span class="hljs-string">"Asia/Singapore"</span>,
&#125;);

<span class="hljs-built_in">console</span>.log(tokyoDate); <span class="hljs-comment">// 2/21/2021, 1:36:46 PM</span>
<span class="hljs-built_in">console</span>.log(singaporeDate); <span class="hljs-comment">// 2/21/2021, 12:36:46 PM</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是由于此方法返回一个字符串，因此进一步的日期和时间操作要求我们先将字符串转换回日期。</p>
<p>而 <code>Temporal</code> API 允许我们在使用 <code>zonedDateTimeISO()</code> 方法创建日期的时候去定义时区。我们可以使用 <code>.now</code> 对象去获取当前的日期、时间：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> tokyoDate = Temporal.now.zonedDateTimeISO(<span class="hljs-string">"Asia/Tokyo"</span>);
<span class="hljs-keyword">let</span> singaporeDate = Temporal.now.zonedDateTimeISO(<span class="hljs-string">"Asia/Singapore"</span>);

<span class="hljs-built_in">console</span>.log(tokyoDate);
<span class="hljs-comment">// 2021-02-20T13:48:24.435904429+09:00[Asia/Tokyo]</span>
<span class="hljs-built_in">console</span>.log(singaporeDate);
<span class="hljs-comment">// 2021-02-20T12:48:24.429904404+08:00[Asia/Singapore]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于返回的值仍然是 <code>Temporal</code> 日期，因此我们可以使用 <code>Temporal</code> 本身的方法进一步对其进行操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> date = Temporal.now.zonedDateTimeISO(<span class="hljs-string">"Asia/Tokyo"</span>);
<span class="hljs-keyword">let</span> oneWeekLater = date.add(&#123;<span class="hljs-attr">weeks</span>: <span class="hljs-number">1</span>&#125;);

<span class="hljs-built_in">console</span>.log(oneWeekLater);
<span class="hljs-comment">// 2021-02-27T13:48:24.435904429+09:00[Asia/Tokyo]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Temporal</code> API 遵循使用类型的约定，其中以 <code>Plain</code> 开头的名称是没有时区的（<code>.PlainDate</code>、<code>.PlainTime</code>、<code>.PlainDateTime</code>），而 <code>.ZonedDateTime</code> 则相反。</p>
<h3 data-id="heading-6">41.4 遵循 ISO-8601 标准进行严格的日期解析</h3>
<p>现有的从字符串解析日期的方式是不可靠的，因为当我们传递 ISO-8601 格式的日期字符串时，返回值将根据是否传递了时区偏移量而有所不同。</p>
<p>考虑以下示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">"2021-02-20"</span>).toISOString();
<span class="hljs-comment">// 2021-02-20T00:00:00.000Z</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">"2021-02-20T05:30"</span>).toISOString();
<span class="hljs-comment">// 2021-02-20T10:30:00.000Z</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的第一个 <code>Date</code> 构造器将字符串视为 UTC+0 时区，而第二个构造器将字符串视为 UTC-5 时区（我当前所在的时区），因此返回值会被调整到 UTC+0 时区**（5:30 UTC-5 相当于 10:30 UTC+0）**。</p>
<p><code>Temposal</code> 提案通过区分 <code>PlainDateTime</code> 和 <code>ZonedDateTime</code> 来解决此问题，如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58f0eeec2d8c44c58acb0c977dd3d750~tplv-k3u1fbpfcp-watermark.image" alt="来源：临时提案文档" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们想要使日期成为包含时区的对象时，我们需要使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fproposal-temporal%2Fdocs%2Findex.html%23Temporal-ZonedDateTime" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/proposal-temporal/docs/index.html#Temporal-ZonedDateTime" ref="nofollow noopener noreferrer">ZonedDateTime</a> 对象，反之则使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fproposal-temporal%2Fdocs%2Findex.html%23Temporal-PlainDateTime" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/proposal-temporal/docs/index.html#Temporal-PlainDateTime" ref="nofollow noopener noreferrer">PlainDateTime</a> 对象。</p>
<p>通过分开创建包含时区和不包含时区的日期，<code>Temporal</code> API 可帮助我们从提供的字符串中解析正确的日期、时间组合：</p>
<pre><code class="hljs language-js copyable" lang="js">Temporal.PlainDateTime.from(<span class="hljs-string">"2021-02-20"</span>);
<span class="hljs-comment">// 2021-02-20T00:00:00</span>

Temporal.PlainDateTime.from(<span class="hljs-string">"2021-02-20T05:30"</span>);
<span class="hljs-comment">// 2021-02-20T05:30:00</span>

Temporal.ZonedDateTime.from(<span class="hljs-string">"2021-02-20T05:30[Asia/Tokyo]"</span>);
<span class="hljs-comment">// 2021-02-20T05:30:00+09:00[Asia/Tokyo]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的示例中可以看到，<code>Temporal</code> API 不会对你所在的时区进行预设。</p>
<h3 data-id="heading-7">41.5 支持公历以外的历法</h3>
<p>尽管公历是世界上使用最广泛的日历系统，但有时我们可能需要使用其他日历系统以查看具有文化或宗教意义的特殊日期。</p>
<p><code>Temporal</code> API 允许我们指定要用于日期、时间计算的日历系统。</p>
<p>日历的 NPM Polyfill 实现尚未完成，因此我们需要尝试使用 Browser Polyfill 中的 <code>withCalendar()</code> 方法。请访问 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fproposal-temporal%2Fdocs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/proposal-temporal/docs/" ref="nofollow noopener noreferrer">Temporal 文档页面</a>，然后将以下代码粘贴到浏览器的控制台中：</p>
<pre><code class="hljs language-js copyable" lang="js">Temporal.PlainDate.from(<span class="hljs-string">"2021-02-06"</span>).withCalendar(<span class="hljs-string">"gregory"</span>).day;
<span class="hljs-comment">// 6</span>

Temporal.PlainDate.from(<span class="hljs-string">"2021-02-06"</span>).withCalendar(<span class="hljs-string">"chinese"</span>).day;
<span class="hljs-comment">// 25</span>

Temporal.PlainDate.from(<span class="hljs-string">"2021-02-06"</span>).withCalendar(<span class="hljs-string">"japanese"</span>).day;
<span class="hljs-comment">// 6</span>

Temporal.PlainDate.from(<span class="hljs-string">"2021-02-06"</span>).withCalendar(<span class="hljs-string">"hebrew"</span>).day;
<span class="hljs-comment">// 24</span>

Temporal.PlainDate.from(<span class="hljs-string">"2021-02-06"</span>).withCalendar(<span class="hljs-string">"islamic"</span>).day;
<span class="hljs-comment">// 24</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦提案通过，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDateTimeFormat%2FDateTimeFormat%23parameters" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#parameters" ref="nofollow noopener noreferrer">Intl.DateTimeFormat</a> 中所有可能的日历值都将被实现。</p>
<h2 data-id="heading-8">0x42 逻辑赋值运算符是什么？</h2>
<p>逻辑赋值是对现有数学和二进制逻辑运算符的扩展。我们先复习一下，然后看看把它们结合在一起能得到什么。逻辑赋值运算符是 ES2021 新功能，目前被各主流浏览器支持。</p>
<h3 data-id="heading-9">42.1 什么是有条件赋值</h3>
<p>一般来说，我们在赋值一个变量前可能会做一定的条件判断，当符合条件后才进行赋值，或者针对不同的情况按照不同的表达式赋值。</p>
<p>针对二元逻辑运算符来说，我们可以使用 <code>&&</code>、<code>||</code>、<code>??</code> 赋值，其中：</p>
<ul>
<li><code>&&</code> 测试是否为真；</li>
<li><code>||</code> 测试是否为假；</li>
<li><code>??</code> 测试是否无效（<code>undefined</code>、<code>null</code>）；</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> x = <span class="hljs-literal">true</span> && <span class="hljs-number">2</span>;
<span class="hljs-built_in">console</span>.log(x); <span class="hljs-comment">// 2</span>
<span class="hljs-keyword">let</span> y = <span class="hljs-literal">false</span> || <span class="hljs-number">3</span>;
<span class="hljs-built_in">console</span>.log(y); <span class="hljs-comment">// 3</span>
<span class="hljs-keyword">let</span> z = <span class="hljs-literal">null</span> ?? <span class="hljs-number">4</span>;
<span class="hljs-built_in">console</span>.log(z); <span class="hljs-comment">// 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">42.2 &&=</h3>
<p>逻辑与赋值运算符 <code>x &&= y</code> 等同于 <code>x && (x = y)</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> x = <span class="hljs-number">20</span>;
x &&= <span class="hljs-number">100</span>;
<span class="hljs-built_in">console</span>.log(x); <span class="hljs-comment">// 100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">42.3 ||=</h3>
<p>逻辑或赋值运算符 <code>x ||= y</code> 等同于 <code>x || (x = y)</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> y = <span class="hljs-number">20</span>;
y ||= <span class="hljs-number">200</span>;
<span class="hljs-built_in">console</span>.log(y); <span class="hljs-comment">// 20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">42.4 ??=</h3>
<p>逻辑空赋值运算符 <code>x ??= y</code> 等同于 <code>x ?? (x = y)</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> z;
z ??= <span class="hljs-number">300</span>;
<span class="hljs-built_in">console</span>.log(z); <span class="hljs-comment">// 300</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">0x43 如何判断函数参数长度？</h2>
<p>在 #41 中我们介绍了 <code>arguments</code> 参数。我们可以直接使用 <code>arguments.length</code> 获取传参的总长度。</p>
<h2 data-id="heading-14">0x44 什么是 JavaScript 的 Label？</h2>
<p>JavaScript 的标签语句用于 <code>for</code> 和 <code>while</code> 循环，用与 <code>break</code> 和 <code>continue</code> 语句共同使用，常用于多重循环中循环体的中断与跳过，如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">loop1: <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++) &#123;
    <span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>;
    loop2: <span class="hljs-keyword">while</span> (j < <span class="hljs-number">6</span>) &#123;
        <span class="hljs-keyword">if</span> (~~(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">10</span>) < i) &#123;
            <span class="hljs-built_in">console</span>.log(i, j);
            <span class="hljs-keyword">break</span> loop1;
        &#125;
        j++;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述函数指示，如果随机数 * 10 小于 <code>i</code> 则终止整个 <code>loop1</code> 循环体（正常来说调用 <code>break</code> 只会终止 <code>loop2</code> 循环体）。</p>
<h3 data-id="heading-15">44.1 带标签的代码块</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">block: &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Hello"</span>);
    <span class="hljs-keyword">break</span> block;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"World"</span>);
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Hoarfroster"</span>);

<span class="hljs-comment">// 输出结果为：</span>
<span class="hljs-comment">//</span>
<span class="hljs-comment">// Hello</span>
<span class="hljs-comment">// Hoarfroster</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">44.2 带标签的函数声明</h3>
<p>需要注意的是，严格模式下不允许给函数加标签，而生成器函数无论是否严格模式都不允许被标签。</p>
<h2 data-id="heading-17">0x45 随机数的使用？</h2>
<p>随机数一直都是计算机编程中的一个常见内容，常用于作密钥种子、链接地址、会话 ID 等。随机数分为真随机数和伪随机数，JavaScript 内置的 <code>Math.random()</code> 和 <code>Crypto.getRandomValues()</code> 都是伪随机数算法。</p>
<h3 data-id="heading-18">45.1 Math.random()</h3>
<p><code>Math.random()</code> 用于生成 [0, 1) 范围内的伪随机浮点数，不接受种子，产生的数字为服从均匀分配的随机数。需要注意的是，ECMAScript 规范中只要求生成数符合范围，没有规定是否需要随机。</p>
<h4 data-id="heading-19">45.1.1 获取随机数</h4>
<p>封包一个 <code>Math.random()</code> 函数为 <code>getRandom()</code> 函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandom</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.random();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">45.1.2 获取两个数之间的随机数</h4>
<p>返回一个不小于最小值（可能等于 0，概率为 0），不大于等于最大值的随机数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomArbitrary</span>(<span class="hljs-params">min, max</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.random() * (max - min) + min;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">45.1.3 获取两个数之间的随机整数</h4>
<p>返回一个不小于最小值（可能等于 0，概率为 0），不大于等于最大值的随机整数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomArbitrary</span>(<span class="hljs-params">min, max</span>) </span>&#123;
    min = <span class="hljs-built_in">Math</span>.ceil(min);
    max = <span class="hljs-built_in">Math</span>.floor(max);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * (max - min) + min);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意：</strong> 使用 <code>Math.round()</code> 会导致随机数不服从均匀分布。</p>
</blockquote>
<h3 data-id="heading-22">45.2 Crypto.getRandomValues()</h3>
<p>该方法可以让我们获得加密后的强随机值，传参为 TypedArray，返回填充随机数的 TypedArray。该方法使用了伪随机数生成器，其种子值具有足够的熵。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> array = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint32Array</span>(<span class="hljs-number">10</span>);
<span class="hljs-built_in">window</span>.crypto.getRandomValues(array);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"你的幸运数字："</span>);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
    <span class="hljs-built_in">console</span>.log(array[i]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">45.3 正态分布随机数生成器</h3>
<p>正态分布的主要特征是平均值与方差，我们可以使用如下方法转换均匀分布为正态分布：</p>
<h4 data-id="heading-24">45.3.1 叠加法</h4>
<p>根据独立同分布的中心极限定理：设随机变量 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>x</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">x_1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>、<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>x</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">x_2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>、...、<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>x</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">x_n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> 相互独立，服从同一分布，且数学期望为 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>μ</mi></mrow><annotation encoding="application/x-tex">μ</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">μ</span></span></span></span></span>，标准差为 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>σ</mi></mrow><annotation encoding="application/x-tex">σ</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">σ</span></span></span></span></span>（<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>σ</mi><mo>></mo><mn>0</mn></mrow><annotation encoding="application/x-tex">σ>0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5782em;vertical-align:-0.0391em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">σ</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.64444em;vertical-align:0em;"></span><span class="mord">0</span></span></span></span></span>），则随机变量之和的标准化变量：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle scriptlevel="0" displaystyle="true"><mfrac><mrow><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>x</mi><mi>k</mi></msub><mo>−</mo><mi>n</mi><mo>×</mo><mi>μ</mi></mrow><mrow><msqrt><mi>n</mi></msqrt><mo>×</mo><msqrt><mi>σ</mi></msqrt></mrow></mfrac></mstyle></mrow><annotation encoding="application/x-tex">\displaystyle\frac&#123;\sum_&#123;k=1&#125;^n x_k - n\times μ&#125;&#123;\sqrt&#123;n&#125;\times \sqrt&#123;σ&#125;&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:2.424002em;vertical-align:-0.9300000000000002em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.494002em;"><span style="top:-2.30972em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8002800000000001em;"><span class="svg-align" style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord" style="padding-left:0.833em;"><span class="mord mathnormal">n</span></span></span><span style="top:-2.76028em;"><span class="pstrut" style="height:3em;"></span><span class="hide-tail" style="min-width:0.853em;height:1.08em;"><svg width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"/></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.23972em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8002800000000001em;"><span class="svg-align" style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord" style="padding-left:0.833em;"><span class="mord mathnormal" style="margin-right:0.03588em;">σ</span></span></span><span style="top:-2.76028em;"><span class="pstrut" style="height:3em;"></span><span class="hide-tail" style="min-width:0.853em;height:1.08em;"><svg width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"/></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.23972em;"><span></span></span></span></span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.6897100000000003em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.804292em;"><span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.03148em;">k</span><span class="mrel mtight">=</span><span class="mord mtight">1</span></span></span></span><span style="top:-3.2029em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29971000000000003em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord mathnormal">μ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.9300000000000002em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></p>
<p>特别的，当 n = 12，此时平均值为 6，方差为 1，上述分式分母恰好为 1，便于计算，因此我们可以用下面的代码生成服从正态分布的随机数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getNumberInNormalDistribution</span>(<span class="hljs-params">mean, std_dev</span>) </span>&#123;
    <span class="hljs-keyword">return</span> mean + uniform2NormalDistribution() * std_dev;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">uniform2NormalDistribution</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0.0</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">12</span>; i++) &#123;
        sum = sum + <span class="hljs-built_in">Math</span>.random();
    &#125;
    <span class="hljs-keyword">return</span> sum - <span class="hljs-number">6.0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">45.3.2 Box-Muller 法</h4>
<p>Box-Muller 变换是一个更高效的方法，实现代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateGaussianNoise</span>(<span class="hljs-params">mu, sigma</span>) </span>&#123;
    <span class="hljs-keyword">let</span> u, v, mag, z0, z1;
    <span class="hljs-keyword">do</span> &#123;
        u = <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">2</span> - <span class="hljs-number">1.0</span>;
        v = <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">2</span> - <span class="hljs-number">1.0</span>;
    &#125; <span class="hljs-keyword">while</span> (u <= <span class="hljs-built_in">Number</span>.EPSILON);

    mag = sigma * <span class="hljs-built_in">Math</span>.sqrt(-<span class="hljs-number">2.0</span> * <span class="hljs-built_in">Math</span>.log(u));
    z0 = mag * <span class="hljs-built_in">Math</span>.cos(<span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI * v) + mu;
    z1 = mag * <span class="hljs-built_in">Math</span>.sin(<span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI * v) + mu;
    <span class="hljs-keyword">return</span> [z0, z1];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过仍然存在一定的缺陷，即 <code>cos</code> 和 <code>sin</code> 值的计算性能不佳。</p>
<h4 data-id="heading-26">45.3.3 Marsaglia 极坐标法</h4>
<p>我们可以使用 Marsaglia 极坐标法计算，以进一步提高效率，不过，Ziggurat 算法计算效率更高：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateGaussianNoise</span>(<span class="hljs-params">mean, stdDev</span>) </span>&#123;
    <span class="hljs-keyword">let</span> u, v, s;
    <span class="hljs-keyword">do</span> &#123;
        u = <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">2</span> - <span class="hljs-number">1.0</span>;
        v = <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">2</span> - <span class="hljs-number">1.0</span>;
        s = u * u + v * v;
    &#125; <span class="hljs-keyword">while</span> (s >= <span class="hljs-number">1</span> || s == <span class="hljs-number">0</span>);

    s = <span class="hljs-built_in">Math</span>.sqrt((-<span class="hljs-number">2.0</span> * <span class="hljs-built_in">Math</span>.log(s)) / s);
    <span class="hljs-keyword">return</span> mean + stdDev * u * s;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">0x46 eval 和 Function？</h2>
<p><code>eval()</code> 和 <code>Fucntion()</code> 是两个用于解析字符串为函数的函数，其中 <code>eval()</code> 函数会将传入的字符串当做 JavaScript 代码解析为机器代码并运行求值，而 <code>Function()</code> 会将一个字符串转换为函数（函数对应的代码）。</p>
<p>这两个函数通常被大家用来计算一个字符串数学表达式的值，验证数据的正确与否，以及解析 JSON 字符串……</p>
<p>但需要注意的是，<code>eval</code> 有着不少缺点：</p>
<ul>
<li>容易被攻击（<code>eval</code> 有着与调用者相同的权限）；</li>
<li>（不留意）影响调用者的作用域，如不小心修改作用域的某一些值；</li>
<li>运行速度更慢（需要调用解析器）；</li>
<li>函数不可逆（<code>eval</code> 会编译字符串为机器代码，一旦修改字符串中的变量，会导致整个函数重新编译）；</li>
<li>不支持传参，不能重复执行，只会输出最后的值；</li>
</ul>
<blockquote>
<p><strong>提示：</strong> 虽然说 <code>eval</code> 危险，但并不代表不能使用，而是需要谨慎控制权限。</p>
</blockquote>
<p>针对运行速度与作用域和函数可逆性上的问题，推荐使用 <code>new Function(...args, body)</code>。</p>
<h2 data-id="heading-28">0x47 正则表达式是什么？JavaScript 有什么正则标识符？</h2>
<p>正则表达式是用于匹配字符串中字符组合的模式。在 JavaScript 中，正则表达式也是对象。这些模式被用于 <code>RegExp</code> 的 <code>exec</code> 和 <code>test</code> 方法, 以及 <code>String</code> 的 <code>match</code>、<code>matchAll</code>、<code>replace</code>、<code>search</code> 和 <code>split</code> 方法，常用于用户名的匹配、限定条件内容的寻找。</p>
<h3 data-id="heading-29">47.1 创建一个正则表达式</h3>
<p>我们可以用两种方法创建正则表达式，<strong>字面量</strong>和 <strong><code>RegExp</code> 构造函数</strong>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> re = <span class="hljs-regexp">/ab+c/g</span>;
<span class="hljs-keyword">const</span> anotherRe = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"ab+c"</span>, <span class="hljs-string">"g"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">47.2 字符串匹配与查找</h3>
<h4 data-id="heading-31">47.2.1 字符串的匹配</h4>
<p>正则表达式常常用于判断一个字符串中是否有指定子字符串，或判断字符串是否满足正则表达式，常见用例：</p>
<ul>
<li>URL 验证；</li>
<li>身份证验证；</li>
<li>邮箱验证；</li>
<li>用户名验证；</li>
</ul>
<p>具体用法见 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">#37 如何判断字符串是否包含特定字符串或正则表达式是否满足？</a>。</p>
<h4 data-id="heading-32">47.2.2 字符串的查找</h4>























<table><thead><tr><th></th><th>RegExp.exec</th><th>String.match</th><th>String.matchAll</th></tr></thead><tbody><tr><td>返回</td><td>匹配的结果，一个数组</td><td>匹配的结果，一个数组，如果有 <code>g</code> 标识符，返回匹配的内容</td><td>迭代器</td></tr><tr><td>要求</td><td>无</td><td>无</td><td>正则表达式需有 <code>g</code>（global）标识符</td></tr></tbody></table>
<p>我们可用 <code>exec</code>、<code>match</code>、<code>matchAll</code> 三种方法获取匹配到的内容：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> re = <span class="hljs-regexp">/a(.*)b/</span>;
<span class="hljs-keyword">let</span> exec = re.exec(<span class="hljs-string">"acbadb"</span>),
    match = <span class="hljs-string">"acbadb"</span>.match(re),
    matchAll = <span class="hljs-string">"acbadb"</span>.matchAll(re);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正则表达式执行后的返回信息：</p>



































<table><thead><tr><th>属性或索引</th><th>描述</th><th>值</th></tr></thead><tbody><tr><td>exec</td><td>匹配到的信息</td><td>["acbadb", "cbad"]</td></tr><tr><td>exec.index</td><td>匹配到的索引</td><td>0</td></tr><tr><td>exec.input</td><td>输入字符串</td><td>"acbadb"</td></tr><tr><td>re.lastIndex</td><td>下一个匹配的起始索引（仅在 <code>g</code> 标识符下可用）</td><td>0</td></tr><tr><td>re.source</td><td>输入字符串，自动更新</td><td>"acbadb"</td></tr></tbody></table>
<h4 data-id="heading-33">47.2.3 标识符</h4>
<p>正则表达式有六个可选参数（flags）允许全局和不分大小写搜索等特殊匹配，这些参数既可以单独使用也能以任意顺序一起使用, 并且被包含在正则表达式实例中：</p>
<pre><code class="hljs language-text copyable" lang="text">const re = /pattern/flags;
const anotherRe = new RegExp("pattern", "flags");
<span class="copy-code-btn">复制代码</span></code></pre>

































<table><thead><tr><th>标识符</th><th>描述</th></tr></thead><tbody><tr><td>g</td><td>全局搜索。</td></tr><tr><td>i</td><td>不区分大小写搜索。</td></tr><tr><td>m</td><td>多行搜索。</td></tr><tr><td>s</td><td>允许 <code>.</code> 匹配换行符。</td></tr><tr><td>u</td><td>使用 Unicode 码模式进行匹配。</td></tr><tr><td>y</td><td>执行粘性（sticky）搜索，匹配从目标字符串的当前位置开始。</td></tr></tbody></table>
<h2 data-id="heading-34">0x48 如何修改一个元素的样式？</h2>
<p>我们可以有两个思路，一个是添加 CSS <code><style></code> 节点到 DOM 中，一个是添加 <code><link></code> 引用一张 CSS 表，一个是修改一个元素的属性（<code>style</code>），一个是访问 <code>Element.style</code> 使用对应的接口直接赋值。</p>
<p>不过值得注意的是：</p>
<ul>
<li>添加节点会让 DOM 多出一堆节点，影响性能；</li>
<li>添加 <code>link</code> 适合添加一堆样式，有现成的网络样式表；</li>
<li>修改属性可能会覆盖掉一些希望存在的样式；</li>
</ul>
<p>因此一般我们会使用 <code>Element.style</code> 设置元素的样式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> button = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#btn"</span>);
button.style.margin = <span class="hljs-string">"10px"</span>; <span class="hljs-comment">// 访问 Element.style</span>
button.setAttribute(<span class="hljs-string">"style"</span>, <span class="hljs-string">"10px"</span>); <span class="hljs-comment">// 设置元素属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-35">0x49 HTTP 方法和状态码有哪些？</h2>
<p>不管是前端亦或是后端，在软件编程的不少领域都或多或少涉及到 HTTP 这一难以避免的网络传输协议。在深入研究 JavaScript 中的 HTTP 专题之前，让我们先来了解一下 HTTP 是什么。</p>
<p>超文本传输 ​​ 协议（HTTP）是一个用于传输超媒体文档（例如 HTML）的应用层协议。它是为 Web 浏览器与 Web 服务器之间的通信而设计的，但也可以用于其他目的。</p>
<h3 data-id="heading-36">49.1 HTTP 方法</h3>
<p>HTTP 请求可以是不同的方法，以表明要对给定资源执行的操作，指示针对给定资源要执行的期望动作。这些请求方法有时被称为 HTTP 动词，每一个请求方法都实现了不同的语义，但一些共同的特征由一组共享，例如一个请求方法可以是 <code>safe</code>、<code>idempotent</code> 或 <code>cacheable</code>。</p>









































































































<table><thead><tr><th>方法</th><th>描述</th><th>请求是否有主体</th><th>成功的响应是否有主体</th><th>安全</th><th>幂等</th><th>可缓存</th><th>可在表单中使用</th></tr></thead><tbody><tr><td>GET</td><td>GET 方法请求一个指定资源的表示形式. 使用 GET 的请求应该只被用于获取数据。</td><td>是</td><td>是</td><td>是</td><td>是</td><td>是</td><td>是</td></tr><tr><td>HEAD</td><td>HEAD 方法请求一个与 GET 请求的响应相同的响应，但没有响应体。</td><td>否</td><td>否</td><td>是</td><td>是</td><td>是</td><td>否</td></tr><tr><td>POST</td><td>POST 方法用于将实体提交到指定的资源，通常导致在服务器上的状态变化或副作用。</td><td>是 ｜ 是</td><td>否</td><td>否</td><td>仅在包括不可缓存信息时可以缓存</td><td>是</td><td></td></tr><tr><td>PUT</td><td>PUT 方法用请求有效载荷替换目标资源的所有当前表示。</td><td>是</td><td>否</td><td>否</td><td>是</td><td>否</td><td>否</td></tr><tr><td>DELETE</td><td>DELETE 方法删除指定的资源。</td><td>可能会有</td><td>可能会有</td><td>否</td><td>是</td><td>否</td><td>否</td></tr><tr><td>CONNECT</td><td>CONNECT 方法建立一个到由目标资源标识的服务器的隧道。</td><td>否</td><td>是</td><td>否</td><td>否</td><td>否</td><td>否</td></tr><tr><td>OPTIONS</td><td>OPTIONS 方法用于描述目标资源的通信选项。</td><td>否</td><td>是</td><td>是</td><td>是</td><td>否</td><td>否</td></tr><tr><td>TRACE</td><td>TRACE 方法沿着到目标资源的路径执行一个消息环回测试。</td><td>否</td><td>否 ｜ 是</td><td>是</td><td>否</td><td>否</td><td></td></tr><tr><td>PATCH</td><td>PATCH 方法用于对资源应用部分修改。</td><td>是</td><td>是</td><td>否</td><td>否 ｜ 否</td><td>否</td><td></td></tr></tbody></table>
<h3 data-id="heading-37">49.2 HTTP 状态码</h3>
<p>HTTP 响应状态代码指示特定 HTTP 请求是否已成功完成。响应分为五类：信息响应（100–199），成功响应（200–299），重定向（300–399），客户端错误（400–499）和服务器错误（500–599）。</p>
<h4 data-id="heading-38">49.2.1 信息响应</h4>
<p>这一类型的状态码，代表请求已被接受，需要继续处理。这类响应是临时响应，只包含状态行和某些可选的响应头信息，并以空行结束。由于 HTTP/1.0 协议中没有定义任何 <code>1xx</code> 状态码，所以除非在某些试验条件下，服务器禁止向客户端发送 <code>1xx</code> 响应。这些状态码代表的响应都是信息性的，标示客户应该等待服务器采取进一步行动。</p>
<h5 data-id="heading-39">100 Continue</h5>
<p>服务器已经接收到请求头，并且客户端应继续发送请求主体（在需要发送身体的请求的情况下：例如，POST 请求），或者如果请求已经完成，忽略这个响应。服务器必须在请求完成后向客户端发送一个最终响应。要使服务器检查请求的头部，客户端必须在其初始请求中发送 <code>Expect: 100-continue</code> 作为头部，并在发送正文之前接收 <code>100 Continue</code> 状态代码。响应代码 <code>417 Expectation Failed</code> 表示请求不应继续。</p>
<h5 data-id="heading-40">101 Switching Protocols</h5>
<p>服务器已经理解了客户端的请求，并将通过 Upgrade 消息头通知客户端采用不同的协议来完成这个请求。在发送完这个响应最后的空行后，服务器将会切换到在 Upgrade 消息头中定义的那些协议。 只有在切换新的协议更有好处的时候才应该采取类似措施。例如，切换到新的 HTTP 版本（如 HTTP/2）比旧版本更有优势，或者切换到一个实时且同步的协议（如 WebSocket）以传送利用此类特性的资源。</p>
<h5 data-id="heading-41">102 Processing</h5>
<p>WebDAV 请求可能包含许多涉及文件操作的子请求，需要很长时间才能完成请求。该代码表示服务器已经收到并正在处理请求，但无响应可用。这样可以防止客户端超时，并假设请求丢失。</p>
<h5 data-id="heading-42">103 Early Hints</h5>
<p>用来在最终的 HTTP 消息之前返回一些响应头。</p>
<h4 data-id="heading-43">49.2.2 成功响应</h4>
<p>这一类型的状态码，代表请求已成功被服务器接收、理解、并接受。</p>
<h5 data-id="heading-44">200 OK</h5>
<p>请求已成功，请求所希望的响应头或数据体将随此响应返回。实际的响应将取决于所使用的请求方法。在 GET 请求中，响应将包含与请求的资源相对应的实体。在 POST 请求中，响应将包含描述或操作结果的实体。</p>
<h5 data-id="heading-45">201 Created</h5>
<p>请求已经被实现，而且有一个新的资源已经依据请求的需要而创建，且其 URI 已经随 <code>Location</code> 头信息返回。假如需要的资源无法及时创建的话，应当返回 <code>202 Accepted</code>。</p>
<h5 data-id="heading-46">202 Accepted</h5>
<p>服务器已接受请求，但尚未处理。最终该请求可能会也可能不会被执行，并且可能在处理发生时被禁止。[8]</p>
<h5 data-id="heading-47">203 Non-Authoritative Information</h5>
<p>服务器是一个转换代理服务器（Transforming Proxy，例如网络加速器），以 <code>200 OK</code> 状态码为起源，但回应了原始响应的修改版本。</p>
<h5 data-id="heading-48">204 No Content</h5>
<p>服务器成功处理了请求，没有返回任何内容。在强制门户功能中，Wifi 设备连接到需要进行 Web 认证的 Wifi 接入点时，通过访问一个能生成 HTTP 204 响应的的网站，如果能正常收到 204 响应，则代表无需 Web 认证，否则会弹出网页浏览器界面，显示出 Web 网页认证界面用于让用户认证登录。</p>
<h5 data-id="heading-49">205 Reset Content</h5>
<p>服务器成功处理了请求，但没有返回任何内容。与 204 响应不同，此响应要求请求者重置文档视图。</p>
<h5 data-id="heading-50">206 Partial Content（RFC 7233）</h5>
<p>服务器已经成功处理了部分 GET 请求。类似于 FlashGet 或者迅雷这类的 HTTP 下载工具都是使用此类响应实现断点续传或者将一个大文档分解为多个下载段同时下载。</p>
<h5 data-id="heading-51">207 Multi-Status（WebDAV；RFC 4918）</h5>
<p>代表之后的消息体将是一个 XML 消息，并且可能依照之前子请求数量的不同，包含一系列独立的响应代码。</p>
<h5 data-id="heading-52">208 Already Reported （WebDAV；RFC 5842）</h5>
<p>DAV 绑定的成员已经在（多状态）响应之前的部分被列举，且未被再次包含。</p>
<h5 data-id="heading-53">226 IM Used （RFC 3229）</h5>
<p>服务器已经满足了对资源的请求，对实体请求的一个或多个实体操作的结果表示。</p>
<h4 data-id="heading-54">49.2.3 重定向</h4>
<p>这类状态码代表需要客户端采取进一步的操作才能完成请求。通常，这些状态码用来重定向，后续的请求地址（重定向目标）在本次响应的 Location 域中指明。</p>
<p>当且仅当后续的请求所使用的方法是 GET 或者 HEAD 时，用户浏览器才可以在没有用户介入的情况下自动提交所需要的后续请求。客户端应当自动监测无限循环重定向（例如：A→B→C→……→A 或 A→A），因为这会导致服务器和客户端大量不必要的资源消耗。按照 HTTP/1.0 版规范的建议，浏览器不应自动访问超过 5 次的重定向。</p>
<h5 data-id="heading-55">300 Multiple Choices</h5>
<p>被请求的资源有一系列可供选择的回馈信息，每个都有自己特定的地址和浏览器驱动的商议信息。用户或浏览器能够自行选择一个首选的地址进行重定向。 除非这是一个 HEAD 请求，否则该响应应当包括一个资源特性及地址的列表的实体，以便用户或浏览器从中选择最合适的重定向地址。这个实体的格式由 Content-Type 定义的格式所决定。浏览器可能根据响应的格式以及浏览器自身能力，自动作出最合适的选择。当然，RFC 2616 规范并没有规定这样的自动选择该如何进行。 如果服务器本身已经有了首选的回馈选择，那么在 Location 中应当指明这个回馈的 URI；浏览器可能会将这个 Location 值作为自动重定向的地址。此外，除非额外指定，否则这个响应也是可缓存的。</p>
<h5 data-id="heading-56">301 Moved Permanently</h5>
<p>被请求的资源已永久移动到新位置，并且将来任何对此资源的引用都应该使用本响应返回的若干个 URI 之一。如果可能，拥有链接编辑功能的客户端应当自动把请求的地址修改为从服务器反馈回来的地址。除非额外指定，否则这个响应也是可缓存的。 新的永久性的 URI 应当在响应的 Location 域中返回。除非这是一个 HEAD 请求，否则响应的实体中应当包含指向新的 URI 的超链接及简短说明。 如果这不是一个 GET 或者 HEAD 请求，那么浏览器禁止自动进行重定向，除非得到用户的确认，因为请求的条件可能因此发生变化。 注意：对于某些使用 HTTP/1.0 协议的浏览器，当它们发送的 POST 请求得到了一个 301 响应的话，接下来的重定向请求将会变成 GET 方式。</p>
<h5 data-id="heading-57">302 Found</h5>
<p>要求客户端执行临时重定向（原始描述短语为“Moved Temporarily”）。由于这样的重定向是临时的，客户端应当继续向原有地址发送以后的请求。只有在 Cache-Control 或 Expires 中进行了指定的情况下，这个响应才是可缓存的。 新的临时性的 URI 应当在响应的 Location 域中返回。除非这是一个 HEAD 请求，否则响应的实体中应当包含指向新的 URI 的超链接及简短说明。 如果这不是一个 GET 或者 HEAD 请求，那么浏览器禁止自动进行重定向，除非得到用户的确认，因为请求的条件可能因此发生变化。 注意：虽然 RFC 1945 和 RFC 2068 规范不允许客户端在重定向时改变请求的方法，但是很多现存的浏览器将 302 响应视作为 303 响应，并且使用 GET 方式访问在 Location 中规定的 URI，而无视原先请求的方法。</p>
<h5 data-id="heading-58">303 See Other</h5>
<p>对应当前请求的响应可以在另一个 URI 上被找到，当响应于 POST（或 PUT / DELETE）接收到响应时，客户端应该假定服务器已经收到数据，并且应该使用单独的 GET 消息发出重定向。这个方法的存在主要是为了允许由脚本激活的 POST 请求输出重定向到一个新的资源。这个新的 URI 不是原始资源的替代引用。同时，303 响应禁止被缓存。当然，第二个请求（重定向）可能被缓存。 新的 URI 应当在响应的 Location 域中返回。除非这是一个 HEAD 请求，否则响应的实体中应当包含指向新的 URI 的超链接及简短说明。 注意：许多 HTTP/1.1 版以前的浏览器不能正确理解 303 状态。如果需要考虑与这些浏览器之间的互动，302 状态码应该可以胜任，因为大多数的浏览器处理 302 响应时的方式恰恰就是上述规范要求客户端处理 303 响应时应当做的。</p>
<h5 data-id="heading-59">304 Not Modified</h5>
<p>表示资源在由请求头中的 If-Modified-Since 或 If-None-Match 参数指定的这一版本之后，未曾被修改。在这种情况下，由于客户端仍然具有以前下载的副本，因此不需要重新传输资源。</p>
<h5 data-id="heading-60">305 Use Proxy</h5>
<p>被请求的资源必须通过指定的代理才能被访问。Location 域中将给出指定的代理所在的 URI 信息，接收者需要重复发送一个单独的请求，通过这个代理才能访问相应资源。只有原始服务器才能创建 305 响应。许多 HTTP 客户端（像是 Mozilla 注意：RFC 2068 中没有明确 305 响应是为了重定向一个单独的请求，而且只能被原始服务器创建。忽视这些限制可能导致严重的安全后果。</p>
<h5 data-id="heading-61">306 Switch Proxy</h5>
<p>在最新版的规范中，306 状态码已经不再被使用。最初是指“后续请求应使用指定的代理”。</p>
<h5 data-id="heading-62">307 Temporary Redirect</h5>
<p>在这种情况下，请求应该与另一个 URI 重复，但后续的请求应仍使用原始的 URI。 与 302 相反，当重新发出原始请求时，不允许更改请求方法。 例如，应该使用另一个 POST 请求来重复 POST 请求。</p>
<h5 data-id="heading-63">308 Permanent Redirect (RFC 7538)</h5>
<p>请求和所有将来的请求应该使用另一个 URI 重复。 307 和 308 重复 302 和 301 的行为，但不允许 HTTP 方法更改。 例如，将表单提交给永久重定向的资源可能会顺利进行。</p>
<h4 data-id="heading-64">49.2.4 客户端错误</h4>
<p>这类的状态码代表了客户端看起来可能发生了错误，妨碍了服务器的处理。除非响应的是一个 HEAD 请求，否则服务器就应该返回一个解释当前错误状况的实体，以及这是临时的还是永久性的状况。这些状态码适用于任何请求方法。浏览器应当向用户显示任何包含在此类错误响应中的实体内容。</p>
<p>如果错误发生时客户端正在传送数据，那么使用 TCP 的服务器实现应当仔细确保在关闭客户端与服务器之间的连接之前，客户端已经收到了包含错误信息的数据包。如果客户端在收到错误信息后继续向服务器发送数据，服务器的 TCP 栈将向客户端发送一个重置数据包，以清除该客户端所有还未识别的输入缓冲，以免这些数据被服务器上的应用程序读取并干扰后者。</p>
<h5 data-id="heading-65">400 Bad Request</h5>
<p>由于明显的客户端错误（例如，格式错误的请求语法，太大的大小，无效的请求消息或欺骗性路由请求），服务器不能或不会处理该请求。</p>
<h5 data-id="heading-66">401 Unauthorized（RFC 7235）</h5>
<p>参见：HTTP 基本认证、HTTP 摘要认证 类似于 403 Forbidden，401 语义即“未认证”，即用户没有必要的凭据。如果当前请求已经包含了 Authorization 证书，那么 401 响应代表着服务器验证已经拒绝了那些证书。如果 401 响应包含了与前一个响应相同的身份验证询问，且浏览器已经至少尝试了一次验证，那么浏览器应当向用户展示响应中包含的实体信息，因为这个实体信息中可能包含了相关诊断信息。 注意：当网站（通常是网站域名）禁止 IP 地址时，有些网站状态码显示的 401，表示该特定地址被拒绝访问网站。</p>
<h5 data-id="heading-67">402 Payment Required</h5>
<p>该状态码是为了将来可能的需求而预留的。该状态码最初的意图可能被用作某种形式的数字现金或在线支付方案的一部分，但几乎没有哪家服务商使用，而且这个状态码通常不被使用。如果特定开发人员已超过请求的每日限制，Google Developers API 会使用此状态码。</p>
<h5 data-id="heading-68">403 Forbidden</h5>
<p>主条目：HTTP 403 服务器已经理解请求，但是拒绝执行它。与 401 响应不同的是，身份验证并不能提供任何帮助，而且这个请求也不应该被重复提交。如果这不是一个 HEAD 请求，而且服务器希望能够讲清楚为何请求不能被执行，那么就应该在实体内描述拒绝的原因。当然服务器也可以返回一个 404 响应，假如它不希望让客户端获得任何信息。</p>
<h5 data-id="heading-69">404 Not Found</h5>
<p>主条目：HTTP 404 请求失败，请求所希望得到的资源未被在服务器上发现，但允许用户的后续请求。没有信息能够告诉用户这个状况到底是暂时的还是永久的。假如服务器知道情况的话，应当使用 410 状态码来告知旧资源因为某些内部的配置机制问题，已经永久的不可用，而且没有任何可以跳转的地址。404 这个状态码被广泛应用于当服务器不想揭示到底为何请求被拒绝或者没有其他适合的响应可用的情况下。</p>
<h5 data-id="heading-70">405 Method Not Allowed</h5>
<p>请求行中指定的请求方法不能被用于请求相应的资源。该响应必须返回一个 Allow 头信息用以表示出当前资源能够接受的请求方法的列表。例如，需要通过 POST 呈现数据的表单上的 GET 请求，或只读资源上的 PUT 请求。 鉴于 PUT，DELETE 方法会对服务器上的资源进行写操作，因而绝大部分的网页服务器都不支持或者在默认配置下不允许上述请求方法，对于此类请求均会返回 405 错误。</p>
<h5 data-id="heading-71">406 Not Acceptable</h5>
<p>参见：内容协商 请求的资源的内容特性无法满足请求头中的条件，因而无法生成响应实体，该请求不可接受。 除非这是一个 HEAD 请求，否则该响应就应当返回一个包含可以让用户或者浏览器从中选择最合适的实体特性以及地址栏表的实体。实体的格式由 Content-Type 头中定义的媒体类型决定。浏览器可以根据格式及自身能力自行作出最佳选择。但是，规范中并没有定义任何作出此类自动选择的标准。</p>
<h5 data-id="heading-72">407 Proxy Authentication Required（RFC 2617）</h5>
<p>与 401 响应类似，只不过客户端必须在代理服务器上进行身份验证。代理服务器必须返回一个 Proxy-Authenticate 用以进行身份询问。客户端可以返回一个 Proxy-Authorization 信息头用以验证。</p>
<h5 data-id="heading-73">408 Request Timeout</h5>
<p>请求超时。根据 HTTP 规范，客户端没有在服务器预备等待的时间内完成一个请求的发送，客户端可以随时再次提交这一请求而无需进行任何更改。</p>
<h5 data-id="heading-74">409 Conflict</h5>
<p>表示因为请求存在冲突无法处理该请求，例如多个同步更新之间的编辑冲突。</p>
<h5 data-id="heading-75">410 Gone</h5>
<p>表示所请求的资源不再可用，将不再可用。当资源被有意地删除并且资源应被清除时，应该使用这个。在收到 410 状态码后，用户应停止再次请求资源。但大多数服务端不会使用此状态码，而是直接使用 404 状态码。</p>
<h5 data-id="heading-76">411 Length Required</h5>
<p>服务器拒绝在没有定义 Content-Length 头的情况下接受请求。在添加了表明请求消息体长度的有效 Content-Length 头之后，客户端可以再次提交该请求。</p>
<h5 data-id="heading-77">412 Precondition Failed（RFC 7232）</h5>
<p>服务器在验证在请求的头字段中给出先决条件时，没能满足其中的一个或多个。这个状态码允许客户端在获取资源时在请求的元信息（请求头字段数据）中设置先决条件，以此避免该请求方法被应用到其希望的内容以外的资源上。</p>
<h5 data-id="heading-78">413 Request Entity Too Large（RFC 7231）</h5>
<p>前称“Request Entity Too Large”，表示服务器拒绝处理当前请求，因为该请求提交的实体数据大小超过了服务器愿意或者能够处理的范围。此种情况下，服务器可以关闭连接以免客户端继续发送此请求。 如果这个状况是临时的，服务器应当返回一个 Retry-After 的响应头，以告知客户端可以在多少时间以后重新尝试。</p>
<h5 data-id="heading-79">414 Request-URI Too Long（RFC 7231）</h5>
<p>前称“Request-URI Too Long”，这比较少见，通常的情况包括： 本应使用 POST 方法的表单提交变成了 GET 方法，导致查询字符串过长。 重定向 URI“黑洞”，例如每次重定向把旧的 URI 作为新的 URI 的一部分，导致在若干次重定向后 URI 超长。 客户端正在尝试利用某些服务器中存在的安全漏洞攻击服务器。这类服务器使用固定长度的缓冲读取或操作请求的 URI，当 GET 后的参数超过某个数值后，可能会产生缓冲区溢出，导致任意代码被执行。没有此类漏洞的服务器，应当返回 414 状态码。</p>
<h5 data-id="heading-80">415 Unsupported Media Type</h5>
<p>对于当前请求的方法和所请求的资源，请求中提交的互联网媒体类型并不是服务器中所支持的格式，因此请求被拒绝。例如，客户端将图像上传格式为 svg，但服务器要求图像使用上传格式为 jpg。</p>
<h5 data-id="heading-81">416 Requested Range Not Satisfiable（RFC 7233）</h5>
<p>前称“Requested Range Not Satisfiable”。</p>
<h5 data-id="heading-82">417 Expectation Failed</h5>
<p>在请求头 Expect 中指定的预期内容无法被服务器满足，或者这个服务器是一个代理服显的证据证明在当前路由的下一个节点上，Expect 的内容无法被满足。</p>
<h5 data-id="heading-83">418 I'm a teapot（RFC 2324）</h5>
<p>本操作码是在 1998 年作为 IETF 的传统愚人节笑话, 在 RFC 2324 超文本咖啡壶控制协议'中定义的，并不需要在真实的 HTTP 服务器中定义。当一个控制茶壶的 HTCPCP 收到 BREW 或 POST 指令要求其煮咖啡时应当回传此错误。</p>
<h5 data-id="heading-84">421 Misdirected Request （RFC 7540）</h5>
<p>该请求针对的是无法产生响应的服务器（例如因为连接重用）。</p>
<h5 data-id="heading-85">422 Unprocessable Entity（WebDAV；RFC 4918 ）</h5>
<p>请求格式正确，但是由于含有语义错误，无法响应。</p>
<h5 data-id="heading-86">423 Locked（WebDAV；RFC 4918）</h5>
<p>当前资源被锁定。</p>
<h5 data-id="heading-87">424 Failed Dependency（WebDAV；RFC 4918）</h5>
<p>由于之前的某个请求发生的错误，导致当前请求失败，例如 PROPPATCH。</p>
<h5 data-id="heading-88">425 Too Early (RFC 8470)</h5>
<p>服务器拒绝处理在 Early Data 中的请求，以规避可能的重放攻击。</p>
<h5 data-id="heading-89">426 Upgrade Required（RFC 2817）</h5>
<p>客户端应切换到 Upgrade 头字段中给出的不同协议，如 TLS/1.0。</p>
<h5 data-id="heading-90">428 Precondition Required (RFC 6585)</h5>
<p>原服务器要求该请求满足一定条件。这是为了防止“未更新”问题，即客户端读取（GET）一个资源的状态，更改它，并将它写（PUT）回服务器，但这期间第三方已经在服务器上更改了该资源的状态，因此导致了冲突。”</p>
<h5 data-id="heading-91">429 Too Many Requests （RFC 6585）</h5>
<p>用户在给定的时间内发送了太多的请求。旨在用于网络限速。</p>
<h5 data-id="heading-92">431 Request Header Fields Too Large （RFC 6585）</h5>
<p>服务器不愿处理请求，因为一个或多个头字段过大。</p>
<h5 data-id="heading-93">451 Unavailable For Legal Reasons</h5>
<p>主条目：HTTP 451 该访问因法律的要求而被拒绝，由 IETF 在 2015 核准后新增加。</p>
<h4 data-id="heading-94">49.2.5 服务器错误</h4>
<p>表示服务器无法完成明显有效的请求。</p>
<h5 data-id="heading-95">500 Internal Server Error</h5>
<p>通用错误消息，服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。没有给出具体错误信息。</p>
<h5 data-id="heading-96">501 Not Implemented</h5>
<p>服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。（例如，网络服务 API 的新功能）</p>
<h5 data-id="heading-97">502 Bad Gateway</h5>
<p>作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。</p>
<h5 data-id="heading-98">503 Service Unavailable</h5>
<p>由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是暂时的，并且将在一段时间以后恢复。如果能够预计延迟时间，那么响应中可以包含一个 Retry-After 头用以标明这个延迟时间。如果没有给出这个 Retry-After 信息，那么客户端应当以处理 500 响应的方式处理它。</p>
<h5 data-id="heading-99">504 Gateway Timeout</h5>
<p>作为网关或者代理工作的服务器尝试执行请求时，未能及时从上游服务器（URI 标识出的服务器，例如 HTTP、FTP、LDAP）或者辅助服务器（例如 DNS）收到响应。 注意：某些代理服务器在 DNS 查询超时时会返回 400 或者 500 错误。</p>
<h5 data-id="heading-100">505 HTTP Version Not Supported</h5>
<p>服务器不支持，或者拒绝支持在请求中使用的 HTTP 版本。这暗示着服务器不能或不愿使用与客户端相同的版本。响应中应当包含一个描述了为何版本不被支持以及服务器支持哪些协议的实体。</p>
<h5 data-id="heading-101">506 Variant Also Negotiates（RFC 2295）</h5>
<p>由《透明内容协商协议》（RFC 2295）扩展，代表服务器存在内部配置错误，被请求的协商变元资源被配置为在透明内容协商中使用自己，因此在一个协商处理中不是一个合适的重点。</p>
<h5 data-id="heading-102">507 Insufficient Storage（WebDAV；RFC 4918）</h5>
<p>服务器无法存储完成请求所必须的内容。这个状况被认为是临时的。</p>
<h5 data-id="heading-103">508 Loop Detected （WebDAV；RFC 5842）</h5>
<p>服务器在处理请求时陷入死循环。 （可代替 208 状态码）</p>
<h5 data-id="heading-104">510 Not Extended（RFC 2774）</h5>
<p>获取资源所需要的策略并没有被满足。</p>
<h5 data-id="heading-105">511 Network Authentication Required （RFC 6585）</h5>
<p>客户端需要进行身份验证才能获得网络访问权限，旨在限制用户群访问特定网络。（例如连接 WiFi 热点时的强制网络门户）</p>
<h4 data-id="heading-106">49.2.6 非官方状态</h4>
<h5 data-id="heading-107">420 Enhance Your Calm</h5>
<p>Twitter Search 与 Trends API 在客户端被限速的情况下返回。</p>
<h5 data-id="heading-108">444 No Response</h5>
<p>Nginx 上 HTTP 服务器扩展。服务器不向客户端返回任何信息，并关闭连接（有助于阻止恶意软件）。</p>
<h5 data-id="heading-109">450 Blocked by Windows Parental Controls</h5>
<p>这是一个由 Windows 家庭控制（Microsoft）HTTP 阻止的 450 状态代码的示例，用于信息和测试。</p>
<h5 data-id="heading-110">494 Request Header Too Large</h5>
<p>在错误代码 431 提出之前 Nginx 上使用的扩展 HTTP 代码。</p>
<h2 data-id="heading-111">0x50 如何在 JavaScript 中发送 HTTP 请求？</h2>
<p>在 JavaScript 中，一般我们会使用 XHR 或 fetch 获取网络资源。</p>
<h3 data-id="heading-112">50.1 XMLHttpRequest</h3>
<p>XMLHttpRequest 一开始只是微软浏览器提供的一个接口，后来各大浏览器纷纷效仿也提供了这个接口，再后来 W3C 对它进行了标准化，提出了 XMLHttpRequest 标准。XMLHttpRequest 标准又分为 Level 1 和 Level 2。 XMLHttpRequest Level 1 主要存在以下缺点：</p>
<ul>
<li>
<p>受同源策略的限制，不能发送跨域请求；</p>
</li>
<li>
<p>不能发送二进制文件（如图片、视频、音频等），只能发送纯文本数据；</p>
</li>
<li>
<p>在发送和获取数据的过程中，无法实时获取进度信息，只能判断是否完成；</p>
</li>
</ul>
<p>那么 Level 2 对 Level 1 进行了改进，XMLHttpRequest Level 2 中新增了以下功能：</p>
<ul>
<li>
<p>可以发送跨域请求，在服务端允许的情况下；</p>
</li>
<li>
<p>支持发送和接收二进制数据；</p>
</li>
<li>
<p>新增 formData 对象，支持发送表单数据；</p>
</li>
<li>
<p>发送和获取数据时，可以获取进度信息；</p>
</li>
<li>
<p>可以设置请求的超时时间；</p>
</li>
</ul>
<h3 data-id="heading-113">50.2 fetch</h3>
<p>Fetch API 提供了一个获取资源的接口（包括跨域请求）。任何使用过 XMLHttpRequest 的人都能轻松上手，而且新的 API 提供了更强大和灵活的功能集。</p>
<p>Fetch 使用起来很简单，它返回的是一个 Promise，即使你没有 XHR 的开发经验也能快速上手。说了那么多，我们还是先睹为快吧，让我们快快下面的示例代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">fetch(<span class="hljs-string">"https://github.com/PassionPenguin/"</span>, &#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">"get"</span>,
&#125;)
    .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
    &#125;)
    .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
        <span class="hljs-comment">// Error</span>
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是简单的不能再简单了？好，既然我们 Fetch 有了简单的认识之后，那我们再来了解下 Fetch 的基本概念。</p>
<p>在 Fetch 中有四个基本概念，他们分别是 <code>Headers</code>、<code>Request</code>、<code>Response</code> 和 <code>Body</code>。为了更好的理解 Fetch，我们需要对这些概念做一个简单的了解。</p>
<p>在一个完整的 HTTP 请求中，其实就已经包含了这四个概念。请求中有请求头和请求体，响应中有响应头和响应体。所以我们有必要了解这些概念。</p>
<h4 data-id="heading-114">Headers</h4>
<p>Fetch API 的 Headers 接口允许您对 HTTP 请求和响应头执行各种操作。 这些操作包括检索，设置，添加和删除。 一个 Headers 对象具有关联的头列表，它最初为空，由零个或多个键值对组成。你可以使用 append() 方法添加 之类的方法添加到此(参见 Examples)。在该接口的所有方法中，标题名称由不区分大小写的字节序列匹配。</p>
<ul>
<li><code>Headers.append()</code> —— 给现有的 Header 添加一个值, 或者添加一个未存在的 Header 并赋值。</li>
<li><code>Headers.delete()</code> —— 从 Headers 对象中删除指定 Header。</li>
<li><code>Headers.entries()</code> —— 以迭代器的形式返回 Headers 对象中所有的键值对。</li>
<li><code>Headers.get()</code> —— 以 ByteString 的形式从 Headers 对象中返回指定 Header 的全部值。</li>
<li><code>Headers.has()</code> —— 以布尔值的形式从 Headers 对象中返回是否存在指定的 Header。</li>
<li><code>Headers.keys()</code> —— 以迭代器的形式返回 Headers 对象中所有存在的 Header 名。</li>
<li><code>Headers.set()</code> —— 替换现有的 Header 的值, 或者添加一个未存在的 Header 并赋值。</li>
<li><code>Headers.values()</code> —— 以迭代器的形式返回 Headers 对象中所有存在的 Header 的值。</li>
</ul>
<blockquote>
<p><strong>注意：</strong> 值得注意的是,在 Header 已存在或者有多个值的状态下 <code>Headers.set()</code> 和 <code>Headers.append()</code> 的使用有如下区别：<code>Headers.set()</code> 将会用新的值覆盖已存在的值, 但是 <code>Headers.append()</code> 会将新的值添加到已存在的值的队列末尾。</p>
</blockquote>
<blockquote>
<p><strong>注意：</strong> 如果您尝试传入名称不是有效的 HTTP 头名称的引用，则所有 <code>Headers</code> 方法都将引发 <code>TypeError</code>。 如果头部有一个不变的 Guard，则变异操作将会抛出一个 <code>TypeError</code>。 在其他任何失败的情况下，他们静默失败。</p>
</blockquote>
<h5 data-id="heading-115">Guard</h5>
<p>Guard 是 Headers 的一个特性。他充当一个守卫者的角色，影响着一些方法（像 <code>append</code>、<code>set</code>、<code>delete</code>）是否可以改变 Header 头。</p>
<p>它可以有以下取值：<code>immutable</code>、<code>request</code>、<code>request-no-cors</code>、<code>response</code> 或 <code>none。</code></p>
<p>这里你无需关心它，只是为你让你了解有这样个东西在影响着我们设置一些 <code>Headers</code>。你也无法去操作它，这是代理的事情。举个简单的例子，我们无法在响应的 Headers 中插入一个 <code>Set-Cookie</code>。</p>
<p>如果你想要了解更多的细节，具体的规范请参考 <code>concept-headers-guard</code> 和 MDN Guard。</p>
<h4 data-id="heading-116">Request</h4>
<p>Request 表示一个请求类，需要通过实例化来生成一个请求对象。通过该对象可以描述一个 HTTP 请求中的请求（一般含有请求头和请求体）。既然是用来描述请求对象，那么该请求对象应该具有修改请求头（Headers）和请求体（Body）的方式。下面我们先来看下规范中 Request 具有哪些接口：</p>
<p>规范中定义的接口我们可以对应着 MDN 进行查看，你可以点击这里更直观的看看它有哪些属性和方法供我们使用，这里不做一一解释。</p>
<p>注意这里的属性都是只读的，规范中我们可以看到构造函数的第一个参数为 Request 对象或字符串，我们一般采取字符串，即需要访问的资源地址（ HTTP 接口地址）。第二个参数接收一个 RequestInit 可选对象，而这个对象是一个字典。在 javascript 中，我们可以理解为一个对象（&#123;&#125;）。RequestInit 里面我们可以配置初始属性，告诉 Request 我们这个请求的一些配置信息。</p>
<p>这里我们需要对以下几个属性特别注意下。</p>
<ul>
<li>
<p><code>mode</code> 是一个 RequestMode 枚举类型，可取的值有 navigate, same-origin, no-cors, cors。它表示的是一个请求时否使用 CORS，还是使用严格同源模式。当处于跨域情况下，你应当设置为 cors。该值的默认值在使用 Request 初始化时，默认为 cors。当使用标记启动的嵌入式资源，例如 、 
</p></li>
<li>
<p><code>credentials</code> 是一个 RequestCredentials 枚举类型，可取的值有 omit, same-origin, include。它表示的是请求是否在跨域情况下发送 cookie。看到这，如果对 XHR 了解的同学应该很熟悉。这和 XHR 中的 withCredentials 很相似。但是 credentials 有三个可选值，它的默认值为 same-origin。当你需要跨域传递 cookie 凭证信息时，请设置它为 include。注意这里有一个细节，当设置为 include 时，请确保 Response Header 中 Access-Control-Allow-Origin 不能为 *，需要指定源（例如：<a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%3A4001%25EF%25BC%2589%25EF%25BC%258C%25E5%2590%25A6%25E5%2588%2599%25E4%25BC%259A%25E4%25BD%25A0%25E5%25B0%2586%25E4%25BC%259A%25E5%259C%25A8%25E6%258E%25A7%25E5%2588%25B6%25E5%258F%25B0%25E7%259C%258B%25E5%2588%25B0%25E5%25A6%2582%25E4%25B8%258B%25E9%2594%2599%25E8%25AF%25AF%25E4%25BF%25A1%25E6%2581%25AF%25E3%2580%2582%25E8%25AF%25A6%25E7%25BB%2586%25E4%25BF%25A1%25E6%2581%25AF%25E8%25AF%25B7%25E5%258F%2582%25E8%2580%2583" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1:4001%EF%BC%89%EF%BC%8C%E5%90%A6%E5%88%99%E4%BC%9A%E4%BD%A0%E5%B0%86%E4%BC%9A%E5%9C%A8%E6%8E%A7%E5%88%B6%E5%8F%B0%E7%9C%8B%E5%88%B0%E5%A6%82%E4%B8%8B%E9%94%99%E8%AF%AF%E4%BF%A1%E6%81%AF%E3%80%82%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF%E8%AF%B7%E5%8F%82%E8%80%83" ref="nofollow noopener noreferrer">http://127.0.0.1:4001），否则会你将会在控制台看到如下错误信息。详细信息请参考</a> whatwg 规范或 MDN 。</p>
</li>
</ul>
<p>你可以使用文章中提供的代码中启动 cors 示例代码，然后在浏览器中输入 <a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%3A4001%2Frequest%25EF%25BC%258C%25E5%25A6%2582%25E6%259E%259C%25E4%25B8%258D%25E5%2587%25BA%25E6%2584%258F%25E5%25A4%2596%25E7%259A%2584%25E8%25AF%259D%25EF%25BC%258C%25E4%25BD%25A0%25E5%258F%25AF%25E4%25BB%25A5%25E5%259C%25A8%25E6%258E%25A7%25E5%2588%25B6%25E5%258F%25B0%25E4%25B8%25AD%25E7%259C%258B%25E5%2588%25B0%25E4%25B8%258A%25E9%259D%25A2%25E7%259A%2584%25E9%2594%2599%25E8%25AF%25AF%25E6%258F%2590%25E7%25A4%25BA%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1:4001/request%EF%BC%8C%E5%A6%82%E6%9E%9C%E4%B8%8D%E5%87%BA%E6%84%8F%E5%A4%96%E7%9A%84%E8%AF%9D%EF%BC%8C%E4%BD%A0%E5%8F%AF%E4%BB%A5%E5%9C%A8%E6%8E%A7%E5%88%B6%E5%8F%B0%E4%B8%AD%E7%9C%8B%E5%88%B0%E4%B8%8A%E9%9D%A2%E7%9A%84%E9%94%99%E8%AF%AF%E6%8F%90%E7%A4%BA%E3%80%82" ref="nofollow noopener noreferrer">http://127.0.0.1:4001/request，如果不出意外的话，你可以在控制台中看到上面的错误提示。</a></p>
<ul>
<li><code>body</code> 是一个 BodyInit 类型。它可取的值有 Blob,BufferSource , FormData , URLSearchParams , ReadableStream , USVString。细心的同学不知道有没有发现，我们常见的 json 对象却不在其中。因此，我们如果需要传递 json 的话，需要调用 JSON.stringify 函数来帮助我们转换成字符串。</li>
</ul>
<h4 data-id="heading-117">Response</h4>
<p>Response 和 Request 类似，表示的是一次请求返回的响应数据。</p>
<p>规范中定义的接口我们可以对应着 MDN 进行查看，你可以点击这里更直观的看看它有哪些属性和方法供我们使用，这里不做一一解释。</p>
<p>其中 status, headers 属性最为常用。通过 status 状态码我们可以判断出服务端请求处理的结果，像 200, 403 等等常见状态码。这里举个例子，当 status 为 401 时，可以在前端进行拦截跳转到登录页面，这在现如今 SPA（单页面应用程序）中尤为常见。我们也可以利用 headers 来获取一些服务端返回给前端的信息，比如 token。</p>
<p>仔细看上面的接口的同学可以发现 Response includes Body; 这样的标识。在前面我们说过 Body 由 Request 和 Response 实现。所以 Body 具有的方法，在 Response 实例中都可以使用，而这也是非常重要的一部分，我们通过 Body 提供的方法（这里准确来说是由 Response 实现的）对服务端返回的数据进行处理。</p>
<h3 data-id="heading-118">50.3 XHR 和 Fetch</h3>
<p>Fetch 相对 XHR 来说具有简洁、易用、声明式、天生基于 Promise 等特点。XHR 使用方式复杂，接口繁多，最重要的一点个人觉得是它的回调设计，对于实现 try...catch 比较繁琐。</p>
<p>但是 Fetch 也有它的不足，相对于 XHR 来说，目前它具有以下劣势：</p>
<ul>
<li>不能取消（虽然 AbortController 能实现，但是目前兼容性基本不能使用，可以使用 polyfill ）</li>
<li>不能获取进度</li>
<li>不能设置超时（可以通过简单的封装来模拟实现）</li>
<li>兼容性目前比较差（可以使用 polyfill 间接使用 XHR 来优雅降级，这里推荐使用 isomorphic-fetch ）</li>
</ul>
<p>在了解 Fetch 和 XHR 的一些不同后，还是需要根据自身的业务需求来选择合适的技术，因为技术没有永远的好坏，只有合不合适。</p>
<p>下面章节我们将介绍如何“优雅”的使用 Fetch 以及如何尽量避免掉劣势。</p>
<h2 data-id="heading-119">0x51. 如何获取 window 的不同尺寸？</h2>
<ul>
<li>
<p>网页可见区域宽： document.body.clientWidth</p>
</li>
<li>
<p>网页可见区域高： document.body.clientHeight</p>
</li>
<li>
<p>网页可见区域宽： document.body.offsetWidth（包括边线和滚动条的宽）</p>
</li>
<li>
<p>网页可见区域高： document.body.offsetHeight（包括边线的宽）</p>
</li>
<li>
<p>网页正文全文宽： document.body.scrollWidth</p>
</li>
<li>
<p>网页正文全文高： document.body.scrollHeight</p>
</li>
<li>
<p>网页被卷去的高： document.body.scrollTop</p>
</li>
<li>
<p>网页被卷去的高（IE）： document.documentElement.scrollTop</p>
</li>
<li>
<p>网页被卷去的左： document.body.scrollLeft</p>
</li>
<li>
<p>网页正文部分上： window.screenTop</p>
</li>
<li>
<p>网页正文部分左： window.screenLeft</p>
</li>
<li>
<p>屏幕分辨率的高： window.screen.height</p>
</li>
<li>
<p>屏幕分辨率的宽： window.screen.width</p>
</li>
<li>
<p>屏幕可用工作区高度： window.screen.availHeight</p>
</li>
<li>
<p>屏幕可用工作区宽度： window.screen.availWidth</p>
</li>
<li>
<p>你的屏幕设置是： window.screen.colorDepth（位彩色）</p>
</li>
<li>
<p>你的屏幕设置： window.screen.deviceXDPI（像素/英寸）</p>
</li>
</ul>
<h2 data-id="heading-120">0x52. 如何获取用户语言？</h2>
<h3 data-id="heading-121">1. navigator.language</h3>
<p>该方法将返回字符串形式用户首选语言，如 <code>"en-US"</code>。</p>
<h3 data-id="heading-122">2. navigator.languages</h3>
<p>该方法将返回用户偏好的语言，按照系统顺序排列，以数组方式返回，如 <code>["en-US", "zh-CN", "ja-JP"]</code>。</p>
<h3 data-id="heading-123">3. 监听语言变化</h3>
<p>随着系统中用户首选语言的变化，该值也会变化。我们可以在 Window 对象上注册一个 <code>languagechange</code> 事件，以实现对用户首选语言的监听。</p>
<h3 data-id="heading-124">4. 语言格式</h3>
<p>返回格式的相关标准是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftools.ietf.org%2Frfc%2Fbcp%2Fbcp47.txt" target="_blank" rel="nofollow noopener noreferrer" title="https://tools.ietf.org/rfc/bcp/bcp47.txt" ref="nofollow noopener noreferrer">BCP-47</a>，有效语言代码的示例包括 <code>"en"</code>、<code>"en-US"</code>、<code>"fr"</code>、<code>"fr-FR"</code>、<code>"es-ES"</code>……</p>
<blockquote>
<ul>
<li>注意，在 iOS 10.2 之前的 Safari 中，返回的国家/地区代码是小写的：“en-us”、“fr-fr”等。</li>
</ul>
</blockquote>
<h2 data-id="heading-125">0x53. 如何判断用户是否处于暗黑模式？</h2>
<p>苹果系统（macOS、iOS）、大部分的国内 Android UI 以及 Android 10+（API 29+）、Windows 10（21H2+）、Windows 11 等系统都已经全面支持暗黑模式（也叫深色模式）啦！在众多的技术文章里都有介绍如何在网页中与暗黑模式打交道，最常见的是通过 CSS 中的 <code>prefers-color-scheme: dark</code> 来检测用户是否开启了 Dark Mode，以实现在 CSS 为不同颜色模式里定义不同的样式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> prefersDarkMode = <span class="hljs-built_in">window</span>.matchMedia(<span class="hljs-string">'(prefers-color-scheme: dark)'</span>).matches;
<span class="hljs-keyword">if</span> (prefersDarkMode) &#123;
    <span class="hljs-comment">// 搞事情</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>借以监听 <code>matchMedia</code> 的 <code>change</code> 事件，可以在用户切换深色 / 浅色模式的时候，我们可以将浏览器中已打开的页面自动切换为系统对应的模式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> media = <span class="hljs-built_in">window</span>.matchMedia(<span class="hljs-string">'(prefers-color-scheme: dark)'</span>);
<span class="hljs-keyword">let</span> callback = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> prefersDarkMode = e.matches;
    <span class="hljs-keyword">if</span> (prefersDarkMode) &#123;
        <span class="hljs-comment">// 搞事情</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 恢复</span>
    &#125;
&#125;;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> media.addEventListener === <span class="hljs-string">'function'</span>) &#123;
    media.addEventListener(<span class="hljs-string">'change'</span>, callback);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> media.addListener === <span class="hljs-string">'function'</span>) &#123;
    media.addListener(callback);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-126">0x54. 函数参数中剩余参数的使用方式？</h2>
<p>剩余参数语法允许我们将一个不定数量的参数表示为一个数组。</p>
<h3 data-id="heading-127">1. 语法</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">functionName</span>(<span class="hljs-params">a, b, ...theArgs</span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-128">2. 描述</h3>
<p>如果函数的最后一个命名参数以 <code>...</code> 为前缀，则它将成为一个由剩余参数组成的真数组，其中从 <code>0</code> 到 <code>theArgs.length</code> 左闭右开的元素由传递给函数的实际参数提供。</p>
<p>在上面的例子中，<code>theArgs</code> 将收集该函数的第三个参数（因为第一个参数被映射到 <code>a</code>，而第二个参数映射到 <code>b</code>）和所有后续的参数。</p>
<h3 data-id="heading-129">3. 剩余参数和 <code>arguments</code> 对象的区别</h3>
<p>剩余参数和 <code>arguments</code> 对象之间的区别主要有三个：</p>
<ol>
<li>剩余参数只包含那些没有对应形参的实参，而 <code>arguments</code> 对象包含了传给函数的所有实参。</li>
<li><code>arguments</code> 对象不是一个真正的数组，而剩余参数是真正的 <code>Array</code> 实例，也就是说你能够在它上面直接使用所有的数组方法，比如 <code>sort</code>、<code>map</code>、<code>forEach</code> 或 <code>pop</code>。</li>
<li><code>arguments</code> 对象还有一些附加的属性 （如 <code>callee</code> 属性）。</li>
</ol>
<h3 data-id="heading-130">4. 解构剩余参数</h3>
<p>剩余参数可以被解构，这意味着他们的数据可以被解包到不同的变量中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">...[a, b, c]</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b + c;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-131">0x55. 什么是 Set？</h2>
<h3 data-id="heading-132">Set</h3>
<p>Set 有点像是数组（Array），其中的元素（element）可以是任何数据类型。Set 和数组不同的地方在于 Set 中所有的值都是唯一的（unique values），不会有重复的值。当你存入重复值（duplicate values）时，重复值会被忽略。</p>
<p>当你向 Set 中加入新元素时，Set 内部会用 <code>===</code> 来判断是否有重复值，唯一的例外是 <code>NaN</code> 也会被判断作是重复的值（即便 <code>NaN !== NaN</code>）。</p>
<p>而 Set 中的数据也是有序的，当你遍历一个 Set 数据结构时，会依照先前写入/插入的顺序（insertion order）构建迭代器。</p>
<h4 data-id="heading-133">数组 -> Set</h4>
<p>Set 的构造函数 (constructor) 可以传入一个数组当作初始化参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">'value1'</span>, <span class="hljs-string">'value2'</span>, <span class="hljs-string">'value3'</span>]);

<span class="hljs-comment">// true</span>
mySet.has(<span class="hljs-string">'value1'</span>);

<span class="hljs-comment">// Set &#123;"value1", "value2", "value3"&#125;</span>
mySet;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-134">Set.prototype.size</h4>
<p>用来获取 Set 的大小，总共有几个元素。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();

mySet.add(<span class="hljs-number">1</span>);
mySet.add(<span class="hljs-number">5</span>);
mySet.add(<span class="hljs-string">'some text'</span>)

<span class="hljs-comment">// 3 mySet.size;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-135">Set.prototype.add(value)</h4>
<p>用来新增元素，add() 方法会返回 Set 本身。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();

mySet.add(<span class="hljs-number">1</span>);
mySet.add(<span class="hljs-number">5</span>)
mySet.add(<span class="hljs-string">'some text'</span>);

<span class="hljs-comment">// Set &#123;1, 5, "some text"&#125; mySet; 因为 add() 方法会返回 Set 本身，所以你可以用 chaining 的写法：</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();

mySet.add(<span class="hljs-number">1</span>)
    .add(<span class="hljs-number">5</span>)
    .add(<span class="hljs-string">'some text'</span>);

<span class="hljs-comment">// Set &#123;1, 5, "some text"&#125; mySet;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-136">Set.prototype.has(value)</h4>
<p>返回一个 boolean，判断 Set 中有没某个值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
mySet.add(<span class="hljs-string">'foo'</span>);

<span class="hljs-comment">// true mySet.has('foo'); // false mySet.has('bar');</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-137">Set.prototype.delete(value)</h4>
<p>删除某个值，如果删除成功会返回 true，反之返回 false。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
mySet.add(<span class="hljs-string">'foo'</span>);

<span class="hljs-comment">// false mySet.delete('bar'); // true mySet.delete('foo');</span>

<span class="hljs-comment">// false mySet.has('foo');</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-138">Set.prototype.clear()</h4>
<p>用来清空 Set，删除所有的元素，没有返回值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
mySet.add(<span class="hljs-number">1</span>);
mySet.add(<span class="hljs-string">'foo'</span>);

<span class="hljs-comment">// 2 mySet.size; // true mySet.has('foo');</span>

mySet.clear();

<span class="hljs-comment">// 0 mySet.size; // false mySet.has('bar');</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-139">Set.prototype.keys() Set.prototype.values()</h4>
<p><code>keys()</code> 和 <code>values()</code> 行为是一样的，返回一个迭代器存放所有的元素值。</p>
<p>Set 数据结构中没有 <code>key</code>，只有 <code>value</code>，或说在 Set 中 <code>key</code> 等于 <code>value</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">50</span>, <span class="hljs-string">'a'</span>, &#123;<span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>&#125;]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> mySet.values()) &#123;
    <span class="hljs-built_in">console</span>.log(v);
&#125;

<span class="hljs-comment">// 依序输出 50 a &#123;foo: "bar"&#125;</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">of</span> mySet.keys()) &#123;
    <span class="hljs-built_in">console</span>.log(k);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-140">Set.prototype.entries()</h4>
<p>返回一个迭代器，其中每一个值是 [value, value] 结构的数组。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
mySet.add(<span class="hljs-string">'foobar'</span>);
mySet.add(<span class="hljs-number">1</span>);
mySet.add(<span class="hljs-string">'baz'</span>);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> mySet.entries()) &#123;
    <span class="hljs-built_in">console</span>.log(item);
&#125;

<span class="hljs-comment">// 依序输出 // ["foobar", "foobar"]</span>
<span class="hljs-comment">// [1, 1]</span>
<span class="hljs-comment">// ["baz", "baz"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-141">Set.prototype.forEach(callbackFn[, thisArg])</h4>
<p><code>forEach()</code> 方法可以用来遍历 Set。</p>
<p>其中第一个参数 <code>callbackFn</code> 是一个函数，有三个参数：<code>value</code> <code>value</code> <code>Set</code> 本身</p>
<p>为什么要有两个同样的 <code>value</code>？为了和 Map 及数组的 <code>forEach</code> 用法一致。</p>
<p>第二个参数 <code>thisArg</code> 不是必要的参数，表示 <code>this</code> 指向的元素。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">logSetElements</span>(<span class="hljs-params">value1, value2, set</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'s['</span> + value1 + <span class="hljs-string">'] = '</span> + value2);
&#125;

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>, <span class="hljs-literal">undefined</span>]).forEach(logSetElements);

<span class="hljs-comment">// 依序输出 // "s[foo] = foo"</span>
<span class="hljs-comment">// "s[bar] = bar"</span>
<span class="hljs-comment">// "s[undefined] = undefined"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-142">for...of</h4>
<p>我们也可以用 for...of 来遍历 Set。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">50</span>, <span class="hljs-string">'a'</span>, &#123;<span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>&#125;]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> mySet) &#123;
    <span class="hljs-built_in">console</span>.log(v);
&#125;

<span class="hljs-comment">// 依序输出 50 a &#123;foo: "bar"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-143">WeakSet</h3>
<p>WeakSet 和 Set 数据结构基本上是类似的，唯一的区别是 WeakSet 只接受 object 当作元素值 (除了 null 以外，任何值也不可以是 null，会被当作是 undefined 看待)，基本数据格式（primitive data types）都不能被当作是值。</p>
<p>WeakSet 中的 object 不会被垃圾回收机制（garbage collection）计入参考，这也就是 weak 的意思 - 弱引用（weakly reference）。</p>
<p>因为 weakly reference，所以 WeakSet 中的 object 可能随时会被自动回收（garbage collected）。而当 object 被回收后，其所对应的元素也会自动被删除，所以说用 WeakSet 可以方便地避免内存泄露 (memory leak) 的问题。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();

<span class="hljs-comment">// 错误</span>
<span class="hljs-comment">// TypeError: Invalid value used in weak set</span>
ws.add(<span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 WeakSet weakly reference 的特性，WeakSet 不支援遍历类型的操作，只支持三个方法 <code>add()</code>、<code>has()</code>、<code>delete()</code>。</p>
<p>WeakSet 的操作基本上和 Set 相似：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();
<span class="hljs-keyword">var</span> obj = &#123;&#125;;
<span class="hljs-keyword">var</span> foo = &#123;&#125;;

ws.add(<span class="hljs-built_in">window</span>);
ws.add(obj);

<span class="hljs-comment">// true</span>
ws.has(<span class="hljs-built_in">window</span>);
<span class="hljs-comment">// false</span>
ws.has(foo);

<span class="hljs-comment">// 从 WeakSet 中删除 window</span>
ws.delete(<span class="hljs-built_in">window</span>);

<span class="hljs-comment">// false</span>
ws.has(<span class="hljs-built_in">window</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再举一个 WeakSet 实用的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> foos = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        foos.add(<span class="hljs-built_in">this</span>)
    &#125;

    <span class="hljs-function"><span class="hljs-title">method</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (!foos.has(<span class="hljs-built_in">this</span>)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Foo.prototype.method 只能在 Foo 对象上被调用'</span>);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码确保 Foo 的方法只能被 Foo 本身执行，用 WeakSet 你就可以在删除 Foo 对象时，不用管 foos 中的引用，也不会出现 memory leak。</p>
<h3 data-id="heading-144">WeakSet 和 Set 的区别？</h3>
<h2 data-id="heading-145">0x56. 什么是 Map？</h2>
<p>ES6 新增了 Map 和 WeakMap 数据结构。</p>
<h3 data-id="heading-146">Map</h3>
<p>Map 有点像是 object（键值对 key-value pairs），两者不同的地方在于 object 的 key 只能是字符串（string）；而 Map 的 key 则可以是任何的数据格式！</p>
<p>另外 Map 中的数据是有序的，当你遍历一个 Map 数据结构时，会依照 key-value pairs 先前插入的顺序（insertion order）。</p>
<h4 data-id="heading-147">数组 -> Map</h4>
<p>Map 的构造函数（constructor）可以传入一个数组当作初始化参数，数组中的元素是有两个值的数组用来表示 key-value pairs：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> kvArray = [[<span class="hljs-string">'key1'</span>, <span class="hljs-string">'value1'</span>], [<span class="hljs-string">'key2'</span>, <span class="hljs-string">'value2'</span>]];

<span class="hljs-keyword">var</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(kvArray);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-148">Map.prototype.size</h4>
<p>用来取得 Map 对象的大小，共有多少个 key/value pairs。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

map.set(<span class="hljs-string">'foo'</span>, <span class="hljs-number">1</span>);
map.set(<span class="hljs-string">'bar'</span>, <span class="hljs-number">2</span>);

map.size;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-149">Map.prototype.set(key, value)</h4>
<p>用来新增 key-value pair，如果 key 已经存在，其值会被新值覆盖过去。<code>set()</code> 方法会返回 Map 本身。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

m.set(<span class="hljs-string">'str'</span>, <span class="hljs-number">123</span>);
m.set(<span class="hljs-number">101</span>, [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);
m.set(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'blah'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 <code>set()</code> 方法会返回 Map 本身，所以你可以用链式写法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

m.set(<span class="hljs-string">'str'</span>, <span class="hljs-number">123</span>)
    .set(<span class="hljs-number">101</span>, [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>])
    .set(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'blah'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-150">Map.prototype.get(key)</h4>
<p>该方法用于获取某个 key 的值，如果没有这个 key 则返回 <code>undefined</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>]]);

<span class="hljs-comment">// 1</span>
m.get(<span class="hljs-string">'a'</span>);

<span class="hljs-comment">// undefined</span>
m.get(<span class="hljs-string">'c'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-151">Map.prototype.delete(key)</h4>
<p>删除某个 key，如果删除成功会返回 true，反之返回 false。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>]]);

<span class="hljs-comment">// true</span>
m.delete(<span class="hljs-string">'a'</span>);

<span class="hljs-comment">// false</span>
m.delete(<span class="hljs-string">'c'</span>);

<span class="hljs-comment">// Map &#123;"b" => 2&#125;</span>
m;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-152">Map.prototype.has(key)</h4>
<p>返回一个 boolean，判断 Map 中有没某个 key。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>]]);

<span class="hljs-comment">// true</span>
m.has(<span class="hljs-string">'b'</span>);

<span class="hljs-comment">// false</span>
m.has(<span class="hljs-string">'d'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-153">Map.prototype.clear()</h4>
<p>清空 Map，删除全部的 key/value pairs，没有返回值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>]]);

<span class="hljs-comment">// Map &#123;"a" => 1, "b" => 2&#125;</span>
m;

m.clear();

<span class="hljs-comment">// Map &#123;&#125;</span>
m;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-154">Map.prototype.keys()</h4>
<p>返回一个迭代器对象包含全部的 <code>keys</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>], [<span class="hljs-string">'c'</span>, <span class="hljs-number">3</span>]]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">of</span> m.keys()) &#123;
    <span class="hljs-built_in">console</span>.log(k);
&#125;

<span class="hljs-comment">// 依序输出 a b c</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-155">Map.prototype.values()</h4>
<p>返回一个迭代器对象包含全部的 <code>values</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>], [<span class="hljs-string">'c'</span>, <span class="hljs-number">3</span>]]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> m.values()) &#123;
    <span class="hljs-built_in">console</span>.log(v);
&#125;

<span class="hljs-comment">// 依序输出 1 2 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-156">Map.prototype.entries()</h4>
<p>返回一个迭代器，其中每一个值是 [key, value] 结构的数组。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>], [<span class="hljs-string">'c'</span>, <span class="hljs-number">3</span>]]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [k, v] <span class="hljs-keyword">of</span> m.entries()) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;k&#125;</span>=><span class="hljs-subst">$&#123;v&#125;</span>`</span>);
&#125;

<span class="hljs-comment">// 依序输出 a=>1 b=>2 c=>3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-157">Map.prototype.forEach(callbackFn[, thisArg])</h4>
<p><code>forEach()</code> 方法可以用来遍历 Map。</p>
<p>其中第一个参数 <code>callbackFn</code> 是一个函数，有三个参数：<code>value</code> <code>key</code> 和 Map 对象本身。第三个参数 <code>thisArg</code> 不是必要的参数，表示 <code>this</code> 指向的对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>], [<span class="hljs-string">'c'</span>, <span class="hljs-number">3</span>]]);

m.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value, key, map</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>=><span class="hljs-subst">$&#123;value&#125;</span>`</span>);
&#125;);

<span class="hljs-comment">// 依序输出 a=>1 b=>2 c=>3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-158">for...of</h4>
<p>我们也可以用 <code>for...of</code> 来遍历 Map。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>], [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>], [<span class="hljs-string">'c'</span>, <span class="hljs-number">3</span>]]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [k, v] <span class="hljs-keyword">of</span> m) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;k&#125;</span>=><span class="hljs-subst">$&#123;v&#125;</span>`</span>);
&#125;

<span class="hljs-comment">// 依序输出 a=>1 b=>2 c=>3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-159">WeakMap</h3>
<p>WeakMap 和 Map 数据结构基本上是类似的，唯一的区别是 WeakMap 只接受 object 当作 key (除了 null 以外，null 也不行当作是 key)，基本数据格式（primitive data types）都不能被当作是 key，例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> wm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();

<span class="hljs-comment">// 错误</span>
<span class="hljs-comment">// TypeError: Invalid value used as weak map key</span>
wm.set(<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>);

<span class="hljs-comment">// 错误</span>
<span class="hljs-comment">// TypeError: Invalid value used as weak map key</span>
wm.set(<span class="hljs-number">101</span>, <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>WeakMap 中的 key 所指向的 object 不会被垃圾回收机制（garbage collection）计入参考，这也就是 weak 的意思 - 弱引用（weakly reference）。</p>
<p>因为 weakly reference，所以 WeakMap 中的 object 可能随时会被自动回收（garbage collected），而当 object 被回收后，其所对应的 key-value pair 也会自动被删除。</p>
<p>WeakMap 的典型运用之一是引用 DOM 元素对象，当 DOM 元素被移除后，对应的 WeakMap 纪录也会自动被移除，所以说用 WeakMap 可以方便地避免内存泄露（memory leak）的问题。</p>
<p>WeakMap 的操作基本上和 Map 相似：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> wm1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>(),
    wm2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>(),
    wm3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
<span class="hljs-keyword">const</span> o1 = &#123;&#125;,
    o2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    &#125;,
    o3 = <span class="hljs-built_in">window</span>;

wm1.set(o1, <span class="hljs-number">37</span>);
wm1.set(o2, <span class="hljs-string">'azerty'</span>);
wm2.set(o1, o2); <span class="hljs-comment">// value 可以是任何格式，包含像 object 或 function</span>
wm2.set(o3, <span class="hljs-literal">undefined</span>);
wm2.set(wm1, wm2); <span class="hljs-comment">// key 和 value 可以是任何对象，甚至是个 WeakMaps</span>

wm1.get(o2); <span class="hljs-comment">// "azerty"</span>
wm2.get(o2); <span class="hljs-comment">// undefined 因为 wm2 没 o2 这 key</span>
wm2.get(o3); <span class="hljs-comment">// undefined 因为 o3 key 的 value 是设 undefined</span>

wm1.has(o2); <span class="hljs-comment">// true</span>
wm2.has(o2); <span class="hljs-comment">// false</span>
wm2.has(o3); <span class="hljs-comment">// true 就算 value 是设 undefined 还是有 o3 这 key 喔</span>

wm3.set(o1, <span class="hljs-number">37</span>);
wm3.get(o1); <span class="hljs-comment">// 37</span>

wm1.has(o1); <span class="hljs-comment">// true</span>
wm1.delete(o1);
wm1.has(o1); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 WeakMap weakly reference 的特性，WeakMap 不支持遍历类型的操作（如 <code>keys()</code>、<code>values()</code>、<code>entries()</code>、<code>forEach()</code>），也不支持 <code>size</code> 和 <code>clear()</code>，只支持四个方法 <code>set()</code>、<code>get()</code>、<code>has()</code> 和 <code>delete()</code>。</p>
<p>再举一个 WeakMap 实用的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> myBtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>);

<span class="hljs-keyword">let</span> wm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
wm.set(myBtn, &#123;<span class="hljs-attr">clickCnt</span>: <span class="hljs-number">0</span>&#125;);

myBtn.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> btnData = wm.get(myBtn);
    btnData.clickCnt++;
&#125;, <span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是一个记录 btn 元素被点击的次数的代码，我们把点击的数据存在一个 WeakMap 中，key 就是对应的 DOM 元素对象，而一但 btn 元素被从 DOM 中移除时，WeakMap 中对应的 key-value pair 也会一起被移除，也就是说不用特别做什么，就能确保不会造成 memory leak 的风险。</p>
<h3 data-id="heading-160">WeakMap 和 Map 的区别？</h3>
<h2 data-id="heading-161">0x57. Error 是什么？</h2>
<h2 data-id="heading-162">0x58. 什么是调用栈？</h2>
<p>调用栈是解释器（比如浏览器中的 JavaScript 解释器）追踪函数执行流的一种机制。当执行环境中调用了多个函数时，通过这种机制，我们能够追踪到哪个函数正在执行，执行的函数体中又调用了哪个函数。</p>
<ul>
<li>每调用一个函数，解释器就会把该函数添加进调用栈并开始执行。</li>
<li>正在调用栈中执行的函数还调用了其它函数，那么新函数也将会被添加进调用栈，一旦这个函数被调用，便会立即执行。</li>
<li>当前函数执行完毕后，解释器将其清出调用栈，继续执行当前执行环境下的剩余的代码。</li>
<li>当分配的调用栈空间被占满时，会引发“堆栈溢出”错误。</li>
</ul>
<h2 data-id="heading-163">0x59. 如何获取数组最大最小值？</h2>
<h3 data-id="heading-164">1.排序法</h3>
<p>首先我们给数组进行排序，可以按照从小到大的顺序来排，排序之后的数组中第一个和最后一个就是我们想要获取的最小值和最大值。</p>
<p>排序我们会用到数组的 <code>sort</code> 方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">12</span>, <span class="hljs-number">56</span>, <span class="hljs-number">25</span>, <span class="hljs-number">5</span>, <span class="hljs-number">82</span>, <span class="hljs-number">51</span>, <span class="hljs-number">22</span>];

arr.sort(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a - b;
&#125;); <span class="hljs-comment">// [5,12,22,25,51,56]</span>

<span class="hljs-keyword">var</span> min = arr[<span class="hljs-number">0</span>];  <span class="hljs-comment">// 5</span>

<span class="hljs-keyword">var</span> max = arr[arr.length - <span class="hljs-number">1</span>];  <span class="hljs-comment">// 56</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-165">2. 迭代法</h3>
<p>通过迭代，假设当前数组中的第一个值是最大值，然后拿这个最大值和后面的项逐一比较，如果后面的某一个值比假设的值还大，说明假设错了，我们把假设的值进行替换。最后得到的结果就是我们想要的。</p>
<p>获取最大值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">22</span>, <span class="hljs-number">13</span>, <span class="hljs-number">6</span>, <span class="hljs-number">55</span>, <span class="hljs-number">30</span>];
<span class="hljs-keyword">var</span> max = arr[<span class="hljs-number">0</span>];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i < arr.length; i++) &#123;
    <span class="hljs-keyword">var</span> cur = arr[i];
    cur > max ? max = cur : <span class="hljs-literal">null</span>
&#125;

<span class="hljs-built_in">console</span>.log(max); <span class="hljs-comment">// 55</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取最小值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">22</span>, <span class="hljs-number">13</span>, <span class="hljs-number">6</span>, <span class="hljs-number">55</span>, <span class="hljs-number">30</span>];
<span class="hljs-keyword">var</span> min = arr[<span class="hljs-number">0</span>];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i < arr.length; i++) &#123;
    <span class="hljs-keyword">var</span> cur = arr[i];
    cur < min ? min = cur : <span class="hljs-literal">null</span>
&#125;
<span class="hljs-built_in">console</span>.log(min)  <span class="hljs-comment">// 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-166">3. 使用 Math 中的 max/min 方法</h3>
<p>我们可以对 <code>Math.max</code> 和 <code>Math.min</code> 方法调用 <code>apply</code> 方法来实现，并传入需要获取值的数组。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">22</span>, <span class="hljs-number">13</span>, <span class="hljs-number">6</span>, <span class="hljs-number">55</span>, <span class="hljs-number">30</span>];

<span class="hljs-keyword">var</span> max = <span class="hljs-built_in">Math</span>.max.apply(<span class="hljs-literal">null</span>, arr);
<span class="hljs-keyword">var</span> min = <span class="hljs-built_in">Math</span>.min.apply(<span class="hljs-literal">null</span>, arr);

<span class="hljs-built_in">console</span>.log(max, min) <span class="hljs-comment">// 55,6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-167">4. 使用ES6的扩展运算符</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-keyword">var</span> arr = [<span class="hljs-number">22</span>, <span class="hljs-number">13</span>, <span class="hljs-number">6</span>, <span class="hljs-number">55</span>, <span class="hljs-number">30</span>];

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Math</span>.max(...arr)); <span class="hljs-comment">// 55</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Math</span>.min(...arr)); <span class="hljs-comment">// 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-168">0x60. 表单元素 <code>validity</code> 自带验证方法有什么？</h2>
<p>如果你想控制原生错误信息的界面外观，或者你想处理不支持HTML内置表单校验的浏览器，则必须使用 Javascript。</p>
<h3 data-id="heading-169">1. 约束校验的 API</h3>
<p>越来越多的浏览器支持限制校验API，并且这逐渐变得可靠。这些 API 由成组的方法和属性构成，可在特定的表单元素接口上调用：</p>
<ul>
<li><code>HTMLButtonElement</code></li>
<li><code>HTMLFieldSetElement</code></li>
<li><code>HTMLInputElement</code></li>
<li><code>HTMLOutputElement</code></li>
<li><code>HTMLSelectElement</code></li>
<li><code>HTMLTextAreaElement</code></li>
</ul>
<h3 data-id="heading-170">2. 约束校验的 API 及属性</h3>

























































<table><thead><tr><th>属性</th><th>描述</th></tr></thead><tbody><tr><td>validationMessage</td><td>一个本地化消息，描述元素不满足校验条件时（如果有的话）的文本信息。如果元素无需校验（willValidate 为 false），或元素的值满足校验条件时，为空字符串。</td></tr><tr><td>validity</td><td>一个 ValidityState 对象，描述元素的验证状态。详见有关可能的验证状态的文章。</td></tr><tr><td>validity.customError</td><td>如果元素设置了自定义错误，返回 true ；否则返回 false。</td></tr><tr><td>validity.patternMismatch</td><td>如果元素的值不匹配所设置的正则表达式，返回 true，否则返回 false。<br>当此属性为 true 时，元素将命中 <code>:invalid</code> CSS 伪类。</td></tr><tr><td>validity.rangeOverflow</td><td>如果元素的值高于所设置的最大值，返回 true，否则返回 false。<br>当此属性为 true 时，元素将命中 <code>:invalid</code> CSS 伪类。</td></tr><tr><td>validity.rangeUnderflow</td><td>如果元素的值低于所设置的最小值，返回 true，否则返回 false。<br>当此属性为 true 时，元素将命中 <code>:invalid</code> CSS 伪类。</td></tr><tr><td>validity.stepMismatch 如果元素的值不符合 step 属性的规则，返回 true，否则返回 false。<br>当此属性为 true 时，元素将命中 <code>:invalid</code> CSS 伪类。</td><td></td></tr><tr><td>validity.tooLong 如果元素的值超过所设置的最大长度，返回 true，否则返回 false。<br>当此属性为 true 时，元素将命中 <code>:invalid</code> CSS 伪类。</td><td></td></tr><tr><td>validity.typeMismatch 如果元素的值出现语法错误，返回 true，否则返回 false。<br>当此属性为 true 时，元素将命中 <code>:invalid</code> CSS 伪类。</td><td></td></tr><tr><td>validity.valid</td><td>如果元素的值不存在校验问题，返回 true，否则返回 false。<br>当此属性为 true 时，元素将命中 <code>:valid</code> CSS 伪类，否则命中 <code>:invalid</code> CSS 伪类。</td></tr><tr><td>validity.valueMissing</td><td>如果元素设置了 <code>required</code> 属性且值为空，返回 true，否则返回 false。<br>当此属性为 true 时，元素将命中 <code>:invalid</code> CSS 伪类。</td></tr><tr><td>willValidate</td><td>如果元素在表单提交时将被校验，返回 true，否则返回 false。</td></tr></tbody></table>
<h3 data-id="heading-171">3. 约束校验 API 的方法</h3>





















<table><thead><tr><th>方法</th><th>描述</th></tr></thead><tbody><tr><td>checkValidity()</td><td>如果元素的值不存在校验问题，返回 true，否则返回 false。如果元素校验失败，此方法会触发invalid (en-US) 事件。</td></tr><tr><td>HTMLFormElement.reportValidity()</td><td>如果元素或它的子元素控件符合校验的限制，返回 true . 当返回为 false 时, 对每个无效元素可撤销 invalid (en-US) 事件会被唤起并且校验错误会报告给用户。</td></tr><tr><td>setCustomValidity(message)</td><td>为元素添加一个自定义的错误消息；如果设置了自定义错误消息，该元素被认为是无效的，则显示指定的错误。这允许你使用 JavaScript 代码来建立校验失败，而不是用标准约束校验 API 所提供的。这些自定义信息将在向用户报告错误时显示。<br>如果参数为空，则清空自定义错误。</td></tr></tbody></table>
<p>对于旧版浏览器，可以使用 polyfill（例如 <code>Hyperform</code>），来弥补其对约束校验 API 支持的不足。既然你已经使用 JavaScript，在您的网站或 Web 应用程序的设计和实现中使用 polyfill 并不是累赘。</p></div>  
</div>
            