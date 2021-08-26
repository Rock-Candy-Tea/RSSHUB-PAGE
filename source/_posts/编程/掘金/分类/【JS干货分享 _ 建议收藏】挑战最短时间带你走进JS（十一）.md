
---
title: '【JS干货分享 _ 建议收藏】挑战最短时间带你走进JS（十一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3512711a57bf4ad9b6f0593a53ecf373~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 18:12:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3512711a57bf4ad9b6f0593a53ecf373~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 26 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><strong>感激相遇 你好 我是阿ken</strong></p>
<blockquote>
<p>作者：请叫我阿ken<br>
链接：<a href="https://juejin.cn/user/1091187754155048/posts" title="https://juejin.cn/user/1091187754155048/posts" target="_blank">juejin.cn/user/109118…</a><br>
来源：掘金<br>
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。</p>
</blockquote>
<h1 data-id="heading-0"><strong>🌊🌈关于前言：</strong></h1>
<p><strong>文章部分内容及图片出自网络，如有问题请与我本人联系(主页介绍中有公众号)</strong></p>
<p><strong>本博客暂适用于刚刚接触<code>JS</code>以及好久不看想要复习的小伙伴。</strong></p>
<h1 data-id="heading-1"><strong>🌊🌈关于内容：</strong></h1>
<h2 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.6_字符串对象</h2>
<p>在 JavaScript 中，字符串对象提供了些用于对字符串进行处理的属性和方法，可以很方便地实现字符串的查找、截取、替换、大小写转换等操作。</p>
<h2 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.6.1_字符串对象的使用</h2>
<p><strong>字符串对象使用 new String() 来创建，在String 构造函数中传入字符串， 就会在返回的字符串对象中保存这个字符串。</strong></p>
<p>案例：演示，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//创建字符串对象</span>
<span class="hljs-keyword">var</span> str = <span class="hljs-keyword">new</span> string(<span class="hljs-string">'apple'</span>);
<span class="hljs-comment">// 创建字符串对象</span>
<span class="hljs-built_in">console</span>.log (str);
<span class="hljs-comment">// 输出结果: string&#123;"apple"&#125;</span>

<span class="hljs-comment">// 获取字符串长度，输出结果:5</span>
<span class="hljs-built_in">console</span>.log(str.length);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>细心的读者会发现，在前面的学习中，可以使用 “ 字符串变量.length " 的方式进行获取，这种方式很像是在访问一个对象的 length 属性。</p>
<p>案例：演示，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'apple'</span>;
<span class="hljs-built_in">console</span>.log (str.length);
<span class="hljs-comment">// 输出结果: 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，字符串在 JavaScript 中是一种基本包装类型。JavaScript 中的基本包装类型包括String、Number 和 Boolean ，用来把基本数据类型包装成为复杂数据类型，从而使基本数据类型也有了属性和方法。</p>
<p><strong>需要注意的是，虽然 Javascript 基本包装类型的机制可以使普通变量也能像对象一样访问属性和方法，但它们并不属于对象类型。</strong></p>
<p>案例：演示，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">'Hello'</span>);
<span class="hljs-built_in">console</span>.log (<span class="hljs-keyword">typeof</span> obj); 
<span class="hljs-comment">// 输出结果: object</span>

<span class="hljs-built_in">console</span>.log (obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">String</span>); 
<span class="hljs-comment">//输出结果: true</span>

<span class="hljs-keyword">var</span> str = <span class="hljs-string">'Hello'</span>;
<span class="hljs-built_in">console</span>.log (<span class="hljs-keyword">typeof</span> str); 
<span class="hljs-comment">// 输出结果: string</span>

<span class="hljs-built_in">console</span>.log (str <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">String</span>); 
<span class="hljs-comment">// 输出结果: false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3512711a57bf4ad9b6f0593a53ecf373~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>从上述代码可以看出，使用 new String() 返回的 obj 是一个对象，但是普通的字符串变量并不是一个对象，它只是一个字符串类型的数据。</strong></p>
<h2 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.6.2_根据字符返回位置</h2>
<p><strong>字符串对象提供了用于检索元素的属性和方法</strong></p>
<p><strong>字符串对象用于检索元素的属性和方法</strong>：</p>

















<table><thead><tr><th>成员</th><th>作用</th></tr></thead><tbody><tr><td>indexOf( search Value )</td><td>获取 search Value 在字符串中首次出现的位置</td></tr><tr><td>lastIndexOf( search Value )</td><td>获取 search Value 在字符串中最后出现的位置</td></tr></tbody></table>
<p>案例：演示 indexOf() 和 lastIndexOf() 方法的使用，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'HelloWorld'</span> ;

<span class="hljs-built_in">console</span>.log( str.indexOf(<span class="hljs-string">'o'</span>) );
<span class="hljs-comment">// 获取"o"在字符串中首次出现的位置，返回结果:4</span>
<span class="hljs-built_in">console</span>.log( str.lastIndexOf(<span class="hljs-string">'o'</span>)  );
<span class="hljs-comment">// 获取"o"在字符串中最后出现的位置，返回结果:6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3534968a977b49e58119c2568a56fe56~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过返回结果可以看出，位置从 0 开始计算，字符串第一个字符的位置是 0 ， 第2个字符为1，以此类推，最后一个字符的位置是字符串的长度减1。</p>
<p>案例：在一组字符串中，找到所有指定元素出现的位置以及次数。字符串为 ’ Hello World, Hello JavaScript ’ 。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'Hello World,Hello Javascript'</span>;
<span class="hljs-keyword">var</span> index = str.indexOf(<span class="hljs-string">'o'</span>); <span class="hljs-comment">// 先找到第一个 o 出现的位置。</span>
<span class="hljs-keyword">var</span> num = <span class="hljs-number">0</span>; <span class="hljs-comment">// 设置 o 出现的次数初始值为0。</span>
<span class="hljs-keyword">while</span>(index != -<span class="hljs-number">1</span>)&#123;  <span class="hljs-comment">// 通过 while 语句判断 indexOf 返回值的结果</span>
<span class="hljs-comment">//如果不是-1就继续往后进行查找，这是因为 indexOf 只能查找到第1个，</span>
<span class="hljs-comment">//所以后面的查找需要利用第2个参数来实现，给当前的索引 index 加1，</span>
<span class="hljs-comment">//从而实现继续查找。</span>
<span class="hljs-built_in">console</span>.log (index);<span class="hljs-comment">// 依次输出:4、7、17</span>
index = str.indexOf(<span class="hljs-string">'o'</span>, index + <span class="hljs-number">1</span>);
num++;
&#125;
<span class="hljs-built_in">console</span>.log (<span class="hljs-string">'o出现的次数是:'</span> + num);<span class="hljs-comment">// o 出现的次数是:3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，字符串中的空格也会被当作一个字符来处理。</p>
<h2 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.6.3_根据位置返回字符</h2>
<p>在JavaScript中，<strong>字符串对象提供了用于获取字符串中的某一个字符的方法。</strong></p>
<p><strong>字符串对象用于获取某一个字符的方法</strong></p>





















<table><thead><tr><th>成员</th><th>作用</th></tr></thead><tbody><tr><td>charAt(index)</td><td>获取 index 位置的字符，位置从 0 开始计算</td></tr><tr><td>charCodeAt(index)</td><td>获取 index 位置的字符的 ASCII 码</td></tr><tr><td>str [ index ]</td><td>获取指定位置处的字符( HTML5新增 )</td></tr></tbody></table>
<p>案例：了解 charAt()、charCodeAt()、str[ 下标 ]的使用，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'Apple'</span>;
<span class="hljs-built_in">console</span>.log (str.charAt(<span class="hljs-number">3</span>));<span class="hljs-comment">// 输出结果:1</span>
<span class="hljs-built_in">console</span>.log (str.charCodeAt(<span class="hljs-number">0</span>));<span class="hljs-comment">// 输出结果: 65(字符A的 ASCII 码为65)</span>
<span class="hljs-built_in">console</span>.log(str[<span class="hljs-number">0</span>]);<span class="hljs-comment">// 输出结果:A</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.6.4_[案例]统计出现最最多的字符和次数</h2>
<p>案例：演示 charAt() 方法的使用。通过程序来统计字符串中出现最多的字符和次数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'Apple'</span>;
<span class="hljs-comment">//第1步 统计每个字符的出现次数</span>
<span class="hljs-keyword">var</span> o = &#123; &#125;;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < str.length; i++) &#123;
<span class="hljs-keyword">var</span> chars = str.charAt(i); 
<span class="hljs-comment">// 利用 chars 保存字符串中的每一个字符</span>
<span class="hljs-keyword">if</span>( o[chars] ) &#123;   
<span class="hljs-comment">// 利用对象的属性来方便查找元素</span>
o[chars]++;
&#125;<span class="hljs-keyword">else</span>&#123;
o[chars] = <span class="hljs-number">1</span>;
&#125;
&#125;

<span class="hljs-built_in">console</span>.log(o); <span class="hljs-comment">// 输出结果:&#123;A: 1, p: 2, 1:1,e:1&#125;</span>

<span class="hljs-keyword">var</span> max = <span class="hljs-number">0</span>;    <span class="hljs-comment">// 保存出现次数最大值</span>
<span class="hljs-keyword">var</span> ch = <span class="hljs-string">''</span>;    <span class="hljs-comment">// 保存出现次数最多的字符</span>

<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> k <span class="hljs-keyword">in</span> o)&#123;
<span class="hljs-keyword">if</span> (o[k] > max)&#123;
max = o[k];
ch = k;
&#125;
&#125;

<span class="hljs-comment">// 输出结果:"出现最多的字符是:p,共出现了2次"</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'出现最多的字符是:'</span> + ch + <span class="hljs-string">',共出现了'</span> + max + <span class="hljs-string">'次'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f810b78990634615b82bcdcd3b2b6e94~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.6.5_字符串操作方法</h2>
<p><strong>字符串对象提供了一些用于截取字符串、连接字符串、替换字符串的属性和方法</strong></p>
<p><strong>字符串对象用于截取、连接和替换字符串的方法</strong>：</p>









































<table><thead><tr><th>成员</th><th>作用</th></tr></thead><tbody><tr><td>concat(strl, str2, str3…)</td><td>连接多个字符串</td></tr><tr><td>slice(start,[ end ])</td><td>截取从 start 位置到 end 位置之间的一个子字符串</td></tr><tr><td>substring(start [,end] )</td><td>截取从 start 位置到 end 位置之间的一个子字符串，基本和 slice 相同，但是不接收负值</td></tr><tr><td>substr(start [, length] )</td><td>截取从 start 位置开始到 length 长度的子字符串</td></tr><tr><td>toLowerCase()</td><td>获取字符串的小写形式</td></tr><tr><td>toUpperfCase()</td><td>获取字符串的大写形式</td></tr><tr><td>split( [ sparator [, limit] )</td><td>使用 separator 分隔符将字符串分隔成数组，limit 用于限制数量</td></tr><tr><td>replace(str1, str2)</td><td>使用 str2 替换字符串中的 str1 ，返回替换结果，只会替换第一个字符</td></tr></tbody></table>
<p>在使用上表中的方法对字符串进行操作时，处理结果是通过方法的返回值直接返回的，并不会改变字符串本身。</p>
<p>案例：演示，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'HelloWorld'</span>;
str.concat(<span class="hljs-string">'!'</span>);     <span class="hljs-comment">// 在字符串末尾拼接字符，结果:HelloWorld!</span>
str.slice(<span class="hljs-number">1</span>, <span class="hljs-number">3</span>);     <span class="hljs-comment">// 截取从位置1 开始到位置3 范围内的内容，结果：el</span>
str.substring (<span class="hljs-number">5</span>);  <span class="hljs-comment">// 截取从位置5 开始到最后的内容，结果: World</span>
str.substring(<span class="hljs-number">5</span>, <span class="hljs-number">7</span>);  <span class="hljs-comment">// 截取从位置5 开始到位置7 范围内的内容，结果：Wo</span>
str.substr(<span class="hljs-number">5</span>);      <span class="hljs-comment">// 截取从位置5 开始到字符串结尾的内容，结果: World</span>
str.substring(<span class="hljs-number">5</span>, <span class="hljs-number">7</span>);<span class="hljs-comment">// 截取从位置5 开始到位置7 范围内的内容，结果：Wo</span>
str.toLowerCase();  <span class="hljs-comment">// 将字符串转换为小写，结果：helloworld</span>
str.toUpperCase();  <span class="hljs-comment">// 将字符串转换为大写，结果：HELLOWORLD</span>
str.split(<span class="hljs-string">'1'</span>);    <span class="hljs-comment">// 使用"1"切割字符串，结果：["He","","oWor","d"]</span>
str.split(<span class="hljs-string">'1'</span>, <span class="hljs-number">3</span>);  <span class="hljs-comment">// 限制最多切割3次，结果：["He","","oWor"]</span>
str.replace(<span class="hljs-string">'World'</span>,<span class="hljs-string">'!'</span>);<span class="hljs-comment">// 替换字符串，结果："Hello!"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.6.6_[案例]判断用户名是否合法</h2>
<p>案例：要求用户名长度在 3 ~ 10 范围内，不允许出现敏感词 admin 的任何大小写形式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> name = prompt(<span class="hljs-string">'请输人用户名'</span>);
<span class="hljs-keyword">if</span> (name.length < <span class="hljs-number">3</span> || name.length > <span class="hljs-number">10</span>)&#123;
alert(<span class="hljs-string">'用户名长度必须在3 ~ 10之间。'</span>);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (name.toLowerCase().indexOf(<span class="hljs-string">'admin'</span>) !== -<span class="hljs-number">1</span>)&#123;
alert(<span class="hljs-string">'用户名中不能包含敏感词: admin。'</span>);
&#125;<span class="hljs-keyword">else</span>&#123;
alert(<span class="hljs-string">'恭喜您，该用户名可以使用'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码通过判断 length 属性来验证用户名长度 ; 通过将用户名转换为小写后查找里面是否包含敏感词 admin 。实现时 name 先转换为小写后再进行查找，可以使用户名无论使用哪种大小写组合，都能检查出来。indexOf() 方法在查找失败时会返回 -1，因此判断该方法的返回值即可知道用户名中是否包含敏感词。</p>
<h2 data-id="heading-9"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>5.7_值类型和引用类型</h2>
<p>在 JavaScript 中，<strong>基本数据类型 ( 如字符串型、数字型、布尔型、undefined、null )又称为值类型，复杂数据类型(对象)又称为引用类型。引用类型的特点是，变量中保存的仅是一个引用的地址，当对变量进行赋值时，并不是将对象复制了一份，而是将两个变量指向同一个对象的引用。</strong></p>
<p>案例： 例如，下列代码中的 obj1 和 obj2 指向了同一个对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//创建一个对象，并通过变量 obj1 保存对象的引用</span>
<span class="hljs-keyword">var</span> obj1 = &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'小明'</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">18</span>&#125;;
<span class="hljs-comment">// 此时并没有复制对象，而是 obj2 和 obj1 两个变量引用了同一个对象</span>

<span class="hljs-keyword">var</span> obj2 = objl;
<span class="hljs-comment">// 比较两个变量是否引用同一个对象</span>
<span class="hljs-built_in">console</span>.log (obj2 == obj1); <span class="hljs-comment">// 输出结果:true</span>
<span class="hljs-comment">// 通过 obj2 修改对象的属性</span>
obj2.name = <span class="hljs-string">'小红'</span>;
<span class="hljs-comment">// 通过 obj1 访向对象的 name 属性</span>
<span class="hljs-built_in">console</span>.log (obj1.name) <span class="hljs-comment">// 输出结果:小红</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码执行后，obj1 和 obj2 两个变量引用了同一个对象，此时，无论是使用 obj1 操作对象还是使用 obj2 操作对象，实际操作的都是同一个对象。</p>
<p><strong>当 obj1 和 obj2 两个变量指向了同一个对象后，如果给其中一个变量( 如 obj1 ) 重新赋值为其他对象，或者重新赋值为其他值，则 obj1 将不再引用原来的对象，但 obj2 仍然在引用原来的对象。</strong></p>
<p>案例：演示上述概述：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> objl = name:<span class="hljs-string">'小明'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;;
<span class="hljs-keyword">var</span> obj2 = objl;
<span class="hljs-comment">// obj1 指向了一个新创建的对象</span>
obj1 = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'小红'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">17</span> &#125;;
<span class="hljs-comment">// obj2 仍然指向原来的对象</span>
<span class="hljs-built_in">console</span>.log (obj2.name); <span class="hljs-comment">//输出结果:小明</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，第1行代码创建的 name 为小明的对象，最开始只有 obj1 引用，在执行第2行代码后，obj1 和 obj2 都引用该对象，执行第4行代码后，只有 obj2 引用该对象。当一个对象只被一个变量引用的时候，如果这个变量又被重新赋值，则该对象就会变成没有任何变量引用的情况，这时候就会由 JavaScript 的垃圾回收机制自动释放。</p>
<p><strong>当引用类型的变量作为函数的参数来传递时，其效果和变量之间的赋值类似。如果在函数的参数中修改对象的属性或方法，则在函数外面通过引用这个对象的变量访问到的结果也是修改后的。</strong></p>
<p>案例：演示上述概述，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">change</span>(<span class="hljs-params">obj</span>)</span>&#123;
obj.name = <span class="hljs-string">'小红'</span>; <span class="hljs-comment">// 在函数内修改了对象的属性</span>
&#125;
<span class="hljs-keyword">var</span> stu = &#123; <span class="hljs-attr">name</span>:<span class="hljs-string">'小明'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;;
change(stu);
<span class="hljs-built_in">console</span>.log (stu.name); <span class="hljs-comment">// 输出结果:小红</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，当调用 change() 函数后，在 chang() 函数中修改了 obj.name 的值。修改后，在函数外面超过 stu 变量访问到的结果是修改后的值，说明变量 stu 和参数 obj 引用的是同一个对象。</p>
<p><strong>今日入门学习暂时告一段落<br>
Peace</strong></p>
<h1 data-id="heading-10"><strong>🌊🌈往期回顾：</strong></h1>
<p><a href="https://juejin.cn/post/6987731486707286030" title="https://juejin.cn/post/6987731486707286030" target="_blank"><strong>阿ken的HTML、CSS的入门指南(一)_HTML基础</strong></a><br>
<a href="https://juejin.cn/post/6988080294242811918/" title="https://juejin.cn/post/6988080294242811918/" target="_blank"><strong>阿ken的HTML、CSS的入门指南(二)_HTML页面元素和属性</strong></a><br>
<a href="https://juejin.cn/post/6988714719125176351" title="https://juejin.cn/post/6988714719125176351" target="_blank"><strong>阿ken的HTML、CSS的入门指南(三)_文本样式属性</strong></a><br>
<a href="https://juejin.cn/post/6991276111527149605" title="https://juejin.cn/post/6991276111527149605" target="_blank"><strong>阿ken的HTML、CSS的入门指南(四)_CSS3选择器</strong></a><br>
<a href="https://juejin.cn/post/6991769219910074399" title="https://juejin.cn/post/6991769219910074399" target="_blank"><strong>阿ken的HTML、CSS的入门指南(五)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992015827692159007" title="https://juejin.cn/post/6992015827692159007" target="_blank"><strong>阿ken的HTML、CSS的入门指南(六)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992383017834512421" title="https://juejin.cn/post/6992383017834512421" target="_blank"><strong>阿ken的HTML、CSS的入门指南(七)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992747291685699614" title="https://juejin.cn/post/6992747291685699614" target="_blank"><strong>阿ken的HTML、CSS的入门指南(八)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6993130330479656968#heading-6" title="https://juejin.cn/post/6993130330479656968#heading-6" target="_blank"><strong>阿ken的HTML、CSS的入门指南(九)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6993487356665790495" title="https://juejin.cn/post/6993487356665790495" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6993855890856083487" title="https://juejin.cn/post/6993855890856083487" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十一)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6994207456041631780" title="https://juejin.cn/post/6994207456041631780" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十二)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6994610939089649678" title="https://juejin.cn/post/6994610939089649678" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十三)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6994995902825906207" title="https://juejin.cn/post/6994995902825906207" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十四)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6995318091039113253" title="https://juejin.cn/post/6995318091039113253" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十五)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6995721790550966302" title="https://juejin.cn/post/6995721790550966302" target="_blank"><strong>阿ken的HTML、CSS的入门指南（十六）_多媒体技术</strong></a><br>
<a href="https://juejin.cn/post/6996068586783506463" title="https://juejin.cn/post/6996068586783506463" target="_blank"><strong>阿ken的HTML、CSS的入门指南（十七）_多媒体技术</strong></a></p>
<p><a href="https://juejin.cn/post/6997535282757287950" title="https://juejin.cn/post/6997535282757287950" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（十八）</strong></a><br>
<a href="https://juejin.cn/post/6997953156730585119" title="https://juejin.cn/post/6997953156730585119" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（十九）</strong></a><br>
<a href="https://juejin.cn/post/6998293783968219149" title="https://juejin.cn/post/6998293783968219149" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（二十）</strong></a></p>
<p><a href="https://juejin.cn/post/6985072343257677855" title="https://juejin.cn/post/6985072343257677855" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（一）</strong></a><br>
<a href="https://juejin.cn/post/6987241984154927134" title="https://juejin.cn/post/6987241984154927134" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（二）</strong></a><br>
<a href="https://juejin.cn/post/6985456953661063204" title="https://juejin.cn/post/6985456953661063204" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（三）</strong></a><br>
<a href="https://juejin.cn/post/6996434668908183566" title="https://juejin.cn/post/6996434668908183566" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（四）</strong></a><br>
<a href="https://juejin.cn/post/6996819069504585736" title="https://juejin.cn/post/6996819069504585736" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（五）</strong></a><br>
<a href="https://juejin.cn/post/6997220640759496734" title="https://juejin.cn/post/6997220640759496734" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（六）</strong></a><br>
<a href="https://juejin.cn/post/6999229094839713822" title="https://juejin.cn/post/6999229094839713822" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（七）</strong></a><br>
<a href="https://juejin.cn/post/6999431171121610788" title="https://juejin.cn/post/6999431171121610788" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（八）</strong></a><br>
<a href="https://juejin.cn/post/6999797569056423967" target="_blank" title="https://juejin.cn/post/6999797569056423967"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（九）</strong></a><br>
<a href="https://juejin.cn/post/7000175914680057870" target="_blank" title="https://juejin.cn/post/7000175914680057870"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十）</strong></a></p>
<h1 data-id="heading-11"><strong>🌊🌈关于后记：</strong></h1>
<p><strong>感谢阅读，希望能对你有所帮助 博文若有瑕疵请在评论区留言或在主页个人介绍中添加联系方式私聊我 感谢每一位小伙伴不吝赐教</strong></p>
<p>原创不易，<strong>「点赞」+「关注」</strong> 谢谢支持❤</p></div>  
</div>
            