
---
title: '重学JavaScript基础知识，看着一篇就够了。持续更新中...'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/364e6794ab434130b5ac1270a12904fa~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 19:23:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/364e6794ab434130b5ac1270a12904fa~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">附上学习路径图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/364e6794ab434130b5ac1270a12904fa~tplv-k3u1fbpfcp-watermark.image" alt="大前端学习路线.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">字符串操作方法：</h3>
<h4 data-id="heading-2"><strong>1. charAt()</strong></h4>
<p>charAt()方法可用来获取指定位置的字符串，index为字符串索引值，从0开始到string.leng – 1，若不在这个范围将返回一个空字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'abcde'</span>;
<span class="hljs-built_in">console</span>.log(str.charAt(<span class="hljs-number">2</span>));     <span class="hljs-comment">//返回c</span>
<span class="hljs-built_in">console</span>.log(str.charAt(<span class="hljs-number">8</span>));     <span class="hljs-comment">//返回空字符串</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3"><strong>2. charCodeAt()</strong></h4>
<p>charCodeAt()方法可返回指定位置的字符的Unicode编码。charCodeAt()方法与charAt()方法类似，都需要传入一个索引值作为参数，区别是前者返回指定位置的字符的编码，而后者返回的是字符子串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'abcde'</span>;
<span class="hljs-built_in">console</span>.log(str.charCodeAt(<span class="hljs-number">0</span>));     <span class="hljs-comment">//返回97</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4"><strong>3. fromCharCode()</strong></h4>
<p>fromCharCode()可接受一个或多个Unicode值，然后返回一个字符串。另外该方法是String 的静态方法，字符串中的每个字符都由单独的数字Unicode编码指定。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">97</span>, <span class="hljs-number">98</span>, <span class="hljs-number">99</span>, <span class="hljs-number">100</span>, <span class="hljs-number">101</span>)   <span class="hljs-comment">//返回abcde</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><strong>4. indexOf()</strong></h4>
<p>indexOf(<strong>searchvalue</strong>,<strong>fromindex</strong>)用来检索指定的字符串值在字符串中首次出现的位置。它可以接收两个参数，<strong>searchvalue</strong>表示要查找的子字符串，<strong>fromindex</strong>表示查找的开始位置，省略的话则从开始位置进行检索。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'abcdeabcde'</span>;
<span class="hljs-built_in">console</span>.log(str.indexOf(<span class="hljs-string">'a'</span>));  <span class="hljs-comment">// 返回0</span>
<span class="hljs-built_in">console</span>.log(str.indexOf(<span class="hljs-string">'a'</span>, <span class="hljs-number">3</span>));   <span class="hljs-comment">// 返回5</span>
<span class="hljs-built_in">console</span>.log(str.indexOf(<span class="hljs-string">'bc'</span>)); <span class="hljs-comment">// 返回1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6"><strong>5. lastIndexOf()</strong></h4>
<p>lastIndexOf()语法与indexOf()类似，它返回的是一个指定的子字符串值最后出现的位置，其检索顺序是从后向前。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'abcdeabcde'</span>;
<span class="hljs-built_in">console</span>.log(str.lastIndexOf(<span class="hljs-string">'a'</span>));  <span class="hljs-comment">// 返回5</span>
<span class="hljs-built_in">console</span>.log(str.lastIndexOf(<span class="hljs-string">'a'</span>, <span class="hljs-number">3</span>));   <span class="hljs-comment">// 返回0 从第索引3的位置往前检索</span>
<span class="hljs-built_in">console</span>.log(str.lastIndexOf(<span class="hljs-string">'bc'</span>)); <span class="hljs-comment">// 返回6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7"><strong>6. search()</strong></h4>
<p>stringObject.search(substr)</p>
<p>stringObject.search(regexp)</p>
<p>search()方法用于检索字符串中指定的子字符串，或检索与正则表达式相匹配的子字符串。它会返回第一个匹配的子字符串的起始位置，如果没有匹配的，则返回-1。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'abcDEF'</span>;
<span class="hljs-built_in">console</span>.log(str.search(<span class="hljs-string">'c'</span>));   <span class="hljs-comment">//返回2</span>
<span class="hljs-built_in">console</span>.log(str.search(<span class="hljs-string">'d'</span>));   <span class="hljs-comment">//返回-1</span>
<span class="hljs-built_in">console</span>.log(str.search(<span class="hljs-regexp">/d/i</span>));  <span class="hljs-comment">//返回3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8"><strong>7. match()</strong></h4>
<p>stringObject.match(substr)</p>
<p>stringObject.match(regexp)</p>
<p>match()方法可在字符串内检索指定的值，或找到一个或多个正则表达式的匹配。</p>
<p>如果参数中传入的是子字符串或是没有进行全局匹配的正则表达式，那么match()方法会从开始位置执行一次匹配，如果没有匹配到结果，则返回null。否则则会返回一个数组，该数组的第0个元素存放的是匹配文本，除此之外，返回的数组还含有两个对象属性index和input，分别表示匹配文本的起始字符索引和stringObject 的引用(即原字符串)。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'1a2b3c4d5e'</span>;
<span class="hljs-built_in">console</span>.log(str.match(<span class="hljs-string">'h'</span>));    <span class="hljs-comment">//返回null</span>
<span class="hljs-built_in">console</span>.log(str.match(<span class="hljs-string">'b'</span>));    <span class="hljs-comment">//返回["b", index: 3, input: "1a2b3c4d5e"]</span>
<span class="hljs-built_in">console</span>.log(str.match(<span class="hljs-regexp">/b/</span>));    <span class="hljs-comment">//返回["b", index: 3, input: "1a2b3c4d5e"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果参数传入的是具有全局匹配的正则表达式，那么match()从开始位置进行多次匹配，直到最后。如果没有匹配到结果，则返回null。否则则会返回一个数组，数组中存放所有符合要求的子字符串，并且没有index和input属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'1a2b3c4d5e'</span>;
<span class="hljs-built_in">console</span>.log(str.match(<span class="hljs-regexp">/h/g</span>));   <span class="hljs-comment">//返回null</span>
<span class="hljs-built_in">console</span>.log(str.match(<span class="hljs-regexp">/\d/g</span>));  <span class="hljs-comment">//返回["1", "2", "3", "4", "5"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9"><strong>8. substring()</strong></h4>
<p>stringObject.substring(start,end)</p>
<p>substring()是最常用到的字符串截取方法，它可以接收两个参数(参数不能为负值)，分别是要截取的开始位置和结束位置，它将返回一个新的字符串，其内容是从start处到end-1处的所有字符。若结束参数(end)省略，则表示从start位置一直截取到最后。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'abcdefg'</span>;
<span class="hljs-built_in">console</span>.log(str.substring(<span class="hljs-number">1</span>, <span class="hljs-number">4</span>));   <span class="hljs-comment">//返回bcd</span>
<span class="hljs-built_in">console</span>.log(str.substring(<span class="hljs-number">1</span>));  <span class="hljs-comment">//返回bcdefg</span>
<span class="hljs-built_in">console</span>.log(str.substring(-<span class="hljs-number">1</span>)); <span class="hljs-comment">//返回abcdefg，传入负值时会视为0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10"><strong>9. substring()</strong></h4>
<p>stringObject.slice(start,end)</p>
<p>slice()方法与substring()方法非常类似，它传入的两个参数也分别对应着开始位置和结束位置。而区别在于，slice()中的参数可以为负值，如果参数是负数，则该参数规定的是从字符串的尾部开始算起的位置。也就是说，-1 指字符串的最后一个字符。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'abcdefg'</span>;
<span class="hljs-built_in">console</span>.log(str.slice(<span class="hljs-number">1</span>, <span class="hljs-number">4</span>));   <span class="hljs-comment">//返回bcd</span>
<span class="hljs-built_in">console</span>.log(str.slice(-<span class="hljs-number">3</span>, -<span class="hljs-number">1</span>)); <span class="hljs-comment">//返回ef</span>
<span class="hljs-built_in">console</span>.log(str.slice(<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>));  <span class="hljs-comment">//返回bcdef</span>
<span class="hljs-built_in">console</span>.log(str.slice(-<span class="hljs-number">1</span>, -<span class="hljs-number">3</span>)); <span class="hljs-comment">//返回空字符串，若传入的参数有问题，则返回空</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11"><strong>10. substr()</strong></h4>
<p>stringObject.substr(start,length)</p>
<p>substr()方法可在字符串中抽取从start下标开始的指定数目的字符。其返回值为一个字符串，包含从 stringObject的start（包括start所指的字符）处开始的length个字符。如果没有指定 length，那么返回的字符串包含从start到stringObject的结尾的字符。另外如果start为负数，则表示从字符串尾部开始算起。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'abcdefg'</span>;
<span class="hljs-built_in">console</span>.log(str.substr(<span class="hljs-number">1</span>, <span class="hljs-number">3</span>))   <span class="hljs-comment">//返回bcd</span>
<span class="hljs-built_in">console</span>.log(str.substr(<span class="hljs-number">2</span>))  <span class="hljs-comment">//返回cdefg</span>
<span class="hljs-built_in">console</span>.log(str.substr(-<span class="hljs-number">2</span>, <span class="hljs-number">4</span>))  <span class="hljs-comment">//返回fg，目标长度较大的话，以实际截取的长度为准</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12"><strong>11. replace()</strong></h4>
<p>stringObject.replace(regexp/substr,replacement)</p>
<p>replace()方法用来进行字符串替换操作，它可以接收两个参数，前者为被替换的子字符串（可以是正则），后者为用来替换的文本。
如果第一个参数传入的是子字符串或是没有进行全局匹配的正则表达式，那么replace()方法将只进行一次替换（即替换最前面的），返回经过一次替换后的结果字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'abcdeabcde'</span>;
<span class="hljs-built_in">console</span>.log(str.replace(<span class="hljs-string">'a'</span>, <span class="hljs-string">'A'</span>)); <span class="hljs-comment">// 返回Abcdeabcde</span>
<span class="hljs-built_in">console</span>.log(str.replace(<span class="hljs-regexp">/a/</span>, <span class="hljs-string">'A'</span>)); <span class="hljs-comment">// 返回Abcdeabcde</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果第一个参数传入的全局匹配的正则表达式，那么replace()将会对符合条件的子字符串进行多次替换，最后返回经过多次替换的结果字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'abcdeabcdeABCDE'</span>;
<span class="hljs-built_in">console</span>.log(str.replace(<span class="hljs-regexp">/a/g</span>, <span class="hljs-string">'A'</span>));    <span class="hljs-comment">//返回AbcdeAbcdeABCDE</span>
<span class="hljs-built_in">console</span>.log(str.replace(<span class="hljs-regexp">/a/gi</span>, <span class="hljs-string">'$'</span>));   <span class="hljs-comment">//返回$bcde$bcde$BCDE</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13"><strong>12. split()</strong></h4>
<p>stringObject.split(separator,howmany)</p>
<p>split()方法用于把一个字符串分割成字符串数组。第一个参数separator表示分割位置(参考符)，第二个参数howmany表示返回数组的允许最大长度(一般情况下不设置)。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'a|b|c|d|e'</span>;
<span class="hljs-built_in">console</span>.log(str.split(<span class="hljs-string">'|'</span>));    <span class="hljs-comment">//返回["a", "b", "c", "d", "e"]</span>
<span class="hljs-built_in">console</span>.log(str.split(<span class="hljs-string">'|'</span>, <span class="hljs-number">3</span>)); <span class="hljs-comment">//返回["a", "b", "c"]</span>
<span class="hljs-built_in">console</span>.log(str.split(<span class="hljs-string">''</span>)); <span class="hljs-comment">//返回["a", "|", "b", "|", "c", "|", "d", "|", "e"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以用正则来进行分割</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'a1b2c3d4e'</span>;
<span class="hljs-built_in">console</span>.log(str.split(<span class="hljs-regexp">/\d/</span>)); <span class="hljs-comment">//返回["a", "b", "c", "d", "e"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14"><strong>13.  toLowerCase()和toUpperCase()</strong></h4>
<p>stringObject.toLowerCase()
stringObject.toUpperCase()</p>
<p>toLowerCase()方法可以把字符串中的大写字母转换为小写，toUpperCase()方法可以把字符串中的小写字母转换为大写。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'JavaScript'</span>;
<span class="hljs-built_in">console</span>.log(str.toLowerCase()); <span class="hljs-comment">//返回javascript</span>
<span class="hljs-built_in">console</span>.log(str.toUpperCase()); <span class="hljs-comment">//返回JAVASCRIPT</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">数组操作方法：</h3>
<h4 data-id="heading-16">1. ES6 Array.of()</h4>
<p>Array.of() 方法创建一个具有可变数量参数的新数组实例，而不考虑参数的数量或类型。</p>
<p>Array.of() 和 Array 构造函数之间的区别在于处理整数参数：Array.of(7) 创建一个具有单个元素 7 的数组，而 Array(7) 创建一个长度为7的空数组（注意：这是指一个有7个空位(empty)的数组，而不是由7个undefined组成的数组）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.of(<span class="hljs-number">7</span>);       <span class="hljs-comment">// [7]</span>
<span class="hljs-built_in">Array</span>.of(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>); <span class="hljs-comment">// [1, 2, 3]</span>

<span class="hljs-built_in">Array</span>(<span class="hljs-number">7</span>);          <span class="hljs-comment">// [ , , , , , , ]</span>
<span class="hljs-built_in">Array</span>(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>);    <span class="hljs-comment">// [1, 2, 3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">2. ES6 Array.from()</h4>
<p>Array.from() 方法从一个类似数组或可迭代对象创建一个新的，浅拷贝的数组实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.from(<span class="hljs-string">'foo'</span>) <span class="hljs-comment">// ['f', 'o', 'o']</span>

<span class="hljs-built_in">Array</span>.from([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], <span class="hljs-function"><span class="hljs-params">x</span> =></span> x + x) <span class="hljs-comment">// [2, 4, 6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">3. ES6 find()</h4>
<p>find() 方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 undefined。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">5</span>, <span class="hljs-number">12</span>, <span class="hljs-number">8</span>, <span class="hljs-number">130</span>, <span class="hljs-number">44</span>];

<span class="hljs-keyword">const</span> found = array1.find(<span class="hljs-function"><span class="hljs-params">element</span> =></span> element > <span class="hljs-number">10</span>);

<span class="hljs-built_in">console</span>.log(found); <span class="hljs-comment">// expected output: 12</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">4. ES6 findIndex()</h4>
<p>findIndex()方法返回数组中满足提供的测试函数的第一个元素的索引。若没有找到对应元素则返回-1。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">5</span>, <span class="hljs-number">12</span>, <span class="hljs-number">8</span>, <span class="hljs-number">130</span>, <span class="hljs-number">44</span>];

<span class="hljs-keyword">const</span> isLargeNumber = <span class="hljs-function">(<span class="hljs-params">element</span>) =></span> element > <span class="hljs-number">13</span>;

<span class="hljs-built_in">console</span>.log(array1.findIndex(isLargeNumber)); <span class="hljs-comment">// expected output: 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">5. ES6 fill()</h4>
<p>fill() 方法用一个固定值填充一个数组中从起始索引到终止索引内的全部元素。不包括终止索引。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];

<span class="hljs-comment">// fill with 0 from position 2 until position 4</span>
<span class="hljs-built_in">console</span>.log(array1.fill(<span class="hljs-number">0</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>));
<span class="hljs-comment">// expected output: [1, 2, 0, 0]</span>

<span class="hljs-comment">// fill with 5 from position 1</span>
<span class="hljs-built_in">console</span>.log(array1.fill(<span class="hljs-number">5</span>, <span class="hljs-number">1</span>));
<span class="hljs-comment">// expected output: [1, 5, 5, 5]</span>

<span class="hljs-built_in">console</span>.log(array1.fill(<span class="hljs-number">6</span>));
<span class="hljs-comment">// expected output: [6, 6, 6, 6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">6. ES6 includes()</h4>
<p>includes() 方法用来判断一个数组是否包含一个指定的值，根据情况，如果包含则返回 true，否则返回false。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

<span class="hljs-built_in">console</span>.log(array1.includes(<span class="hljs-number">2</span>)); <span class="hljs-comment">// expected output: true</span>

<span class="hljs-keyword">const</span> pets = [<span class="hljs-string">'cat'</span>, <span class="hljs-string">'dog'</span>, <span class="hljs-string">'bat'</span>];

<span class="hljs-built_in">console</span>.log(pets.includes(<span class="hljs-string">'cat'</span>)); <span class="hljs-comment">// expected output: true</span>

<span class="hljs-built_in">console</span>.log(pets.includes(<span class="hljs-string">'at'</span>)); <span class="hljs-comment">// expected output: false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">7. concat()</h4>
<p>concat() 方法用于连接两个或多个数组。该方法不会改变现有的数组，仅会返回被连接数组的一个副本。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">let</span> arr2 = [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
<span class="hljs-keyword">let</span> arr3 = arr1.concat(arr2)
<span class="hljs-built_in">console</span>.log(arr1) <span class="hljs-comment">// [1, 2, 3]</span>
<span class="hljs-built_in">console</span>.log(arr3) <span class="hljs-comment">// [1, 2, 3 , 4, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">8. join()</h4>
<p>join() 方法用于把数组中的所有元素放入一个字符串。元素是通过指定的分隔符进行分隔的，默认使用’,'号分割，不改变原数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-built_in">console</span>.log(arr.join()); <span class="hljs-comment">// 2, 3, 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">9. push()</h4>
<p>push() 方法可向数组的末尾添加一个或多个元素，并返回新的长度。末尾添加，返回的是长度，会改变原数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> animals = [<span class="hljs-string">'pigs'</span>, <span class="hljs-string">'goats'</span>, <span class="hljs-string">'sheep'</span>];

<span class="hljs-keyword">const</span> count = animals.push(<span class="hljs-string">'cows'</span>);
<span class="hljs-built_in">console</span>.log(count);
<span class="hljs-comment">// expected output: 4</span>
<span class="hljs-built_in">console</span>.log(animals);
<span class="hljs-comment">// expected output: Array ["pigs", "goats", "sheep", "cows"]</span>

animals.push(<span class="hljs-string">'chickens'</span>, <span class="hljs-string">'cats'</span>, <span class="hljs-string">'dogs'</span>);
<span class="hljs-built_in">console</span>.log(animals);
<span class="hljs-comment">// expected output: Array ["pigs", "goats", "sheep", "cows", "chickens", "cats", "dogs"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">10. pop()</h4>
<p>pop() 方法用于删除并返回数组的最后一个元素。返回最后一个元素，会改变原数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> plants = [<span class="hljs-string">'broccoli'</span>, <span class="hljs-string">'cauliflower'</span>, <span class="hljs-string">'cabbage'</span>, <span class="hljs-string">'kale'</span>, <span class="hljs-string">'tomato'</span>];

<span class="hljs-built_in">console</span>.log(plants.pop());
<span class="hljs-comment">// expected output: "tomato"</span>

<span class="hljs-built_in">console</span>.log(plants);
<span class="hljs-comment">// expected output: Array ["broccoli", "cauliflower", "cabbage", "kale"]</span>

plants.pop();

<span class="hljs-built_in">console</span>.log(plants);
<span class="hljs-comment">// expected output: Array ["broccoli", "cauliflower", "cabbage"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">11. shift()</h4>
<p>shift() 方法用于把数组的第一个元素从其中删除，并返回第一个元素的值。返回第一个元素，改变原数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

<span class="hljs-keyword">const</span> firstElement = array1.shift();

<span class="hljs-built_in">console</span>.log(array1);
<span class="hljs-comment">// expected output: Array [2, 3]</span>

<span class="hljs-built_in">console</span>.log(firstElement);
<span class="hljs-comment">// expected output: 1</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">12. unshift()</h4>
<p>unshift() 方法可向数组的开头添加一个或更多元素，并返回新的长度。返回新长度，改变原数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

<span class="hljs-built_in">console</span>.log(array1.unshift(<span class="hljs-number">4</span>, <span class="hljs-number">5</span>));
<span class="hljs-comment">// expected output: 5</span>

<span class="hljs-built_in">console</span>.log(array1);
<span class="hljs-comment">// expected output: Array [4, 5, 1, 2, 3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">13. slice()</h4>
<p>返回一个新的数组，包含从 start 到 end （不包括该元素）的 arrayObject 中的元素。返回选定的元素，该方法不会修改原数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> animals = [<span class="hljs-string">'ant'</span>, <span class="hljs-string">'bison'</span>, <span class="hljs-string">'camel'</span>, <span class="hljs-string">'duck'</span>, <span class="hljs-string">'elephant'</span>];

<span class="hljs-built_in">console</span>.log(animals.slice(<span class="hljs-number">2</span>));
<span class="hljs-comment">// expected output: Array ["camel", "duck", "elephant"]</span>

<span class="hljs-built_in">console</span>.log(animals.slice(<span class="hljs-number">2</span>, <span class="hljs-number">4</span>));
<span class="hljs-comment">// expected output: Array ["camel", "duck"]</span>

<span class="hljs-built_in">console</span>.log(animals.slice(<span class="hljs-number">1</span>, <span class="hljs-number">5</span>));
<span class="hljs-comment">// expected output: Array ["bison", "camel", "duck", "elephant"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">14. splice()</h4>
<p>splice() 方法可删除从 index 处开始的零个或多个元素，并且用参数列表中声明的一个或多个值来替换那些被删除的元素。如果从 arrayObject 中删除了元素，则返回的是含有被删除的元素的数组。splice() 方法会直接对数组进行修改。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> months = [<span class="hljs-string">'Jan'</span>, <span class="hljs-string">'March'</span>, <span class="hljs-string">'April'</span>, <span class="hljs-string">'June'</span>];
months.splice(<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-string">'Feb'</span>);
<span class="hljs-comment">// inserts at index 1</span>
<span class="hljs-built_in">console</span>.log(months);
<span class="hljs-comment">// expected output: Array ["Jan", "Feb", "March", "April", "June"]</span>

months.splice(<span class="hljs-number">4</span>, <span class="hljs-number">1</span>, <span class="hljs-string">'May'</span>);
<span class="hljs-comment">// replaces 1 element at index 4</span>
<span class="hljs-built_in">console</span>.log(months);
<span class="hljs-comment">// expected output: Array ["Jan", "Feb", "March", "April", "May"]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">15. sort()</h4>
<p>按照 Unicode code 位置排序，默认升序</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> months = [<span class="hljs-string">'March'</span>, <span class="hljs-string">'Jan'</span>, <span class="hljs-string">'Feb'</span>, <span class="hljs-string">'Dec'</span>];
months.sort();
<span class="hljs-built_in">console</span>.log(months);
<span class="hljs-comment">// expected output: Array ["Dec", "Feb", "Jan", "March"]</span>

<span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">1</span>, <span class="hljs-number">30</span>, <span class="hljs-number">4</span>, <span class="hljs-number">21</span>, <span class="hljs-number">100000</span>];
array1.sort();
<span class="hljs-built_in">console</span>.log(array1);
<span class="hljs-comment">// expected output: Array [1, 100000, 21, 30, 4]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">16. reverse()</h4>
<p>reverse() 方法用于颠倒数组中元素的顺序。返回的是颠倒后的数组，会改变原数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-string">'one'</span>, <span class="hljs-string">'two'</span>, <span class="hljs-string">'three'</span>];
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'array1:'</span>, array1);
<span class="hljs-comment">// expected output: "array1:" Array ["one", "two", "three"]</span>

<span class="hljs-keyword">const</span> reversed = array1.reverse();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'reversed:'</span>, reversed);
<span class="hljs-comment">// expected output: "reversed:" Array ["three", "two", "one"]</span>

<span class="hljs-comment">// Careful: reverse is destructive -- it changes the original array.</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'array1:'</span>, array1);
<span class="hljs-comment">// expected output: "array1:" Array ["three", "two", "one"]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">17. every()</h4>
<p>对数组的每一项都运行给定的函数，每一项都返回 ture,则返回 true</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isBelowThreshold = <span class="hljs-function">(<span class="hljs-params">currentValue</span>) =></span> currentValue < <span class="hljs-number">40</span>;

<span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">1</span>, <span class="hljs-number">30</span>, <span class="hljs-number">39</span>, <span class="hljs-number">29</span>, <span class="hljs-number">10</span>, <span class="hljs-number">13</span>];

<span class="hljs-built_in">console</span>.log(array1.every(isBelowThreshold));
<span class="hljs-comment">// expected output: true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">18. some()</h4>
<p>对数组的每一项都运行给定的函数，任意一项都返回 ture,则返回 true</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];

<span class="hljs-comment">// checks whether an element is even</span>
<span class="hljs-keyword">const</span> even = <span class="hljs-function">(<span class="hljs-params">element</span>) =></span> element % <span class="hljs-number">2</span> === <span class="hljs-number">0</span>;

<span class="hljs-built_in">console</span>.log(array.some(even));
<span class="hljs-comment">// expected output: true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">19. filter()</h4>
<p>对数组的每一项都运行给定的函数，返回 结果为 ture 的项组成的数组</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> words = [<span class="hljs-string">'spray'</span>, <span class="hljs-string">'limit'</span>, <span class="hljs-string">'elite'</span>, <span class="hljs-string">'exuberant'</span>, <span class="hljs-string">'destruction'</span>, <span class="hljs-string">'present'</span>];

<span class="hljs-keyword">const</span> result = words.filter(<span class="hljs-function"><span class="hljs-params">word</span> =></span> word.length > <span class="hljs-number">6</span>);

<span class="hljs-built_in">console</span>.log(result);
<span class="hljs-comment">// expected output: Array ["exuberant", "destruction", "present"]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">20. map()</h4>
<p>对数组的每一项都运行给定的函数，返回每次函数调用的结果组成一个新数组</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">9</span>, <span class="hljs-number">16</span>];

<span class="hljs-comment">// pass a function to map</span>
<span class="hljs-keyword">const</span> map1 = array1.map(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x * <span class="hljs-number">2</span>);

<span class="hljs-built_in">console</span>.log(map1);
<span class="hljs-comment">// expected output: Array [2, 8, 18, 32]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">21. forEach()</h4>
<p>forEach 数组遍历</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>];

array1.forEach(<span class="hljs-function"><span class="hljs-params">element</span> =></span> <span class="hljs-built_in">console</span>.log(element));

<span class="hljs-comment">// expected output: "a"</span>
<span class="hljs-comment">// expected output: "b"</span>
<span class="hljs-comment">// expected output: "c"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">对象操作方法：</h3>
<h3 data-id="heading-38">1. 判断对象是否为空</h3>
<ul>
<li>
<h4 data-id="heading-39">使用ES6的Object.keys()方法</h4>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> data = &#123;&#125;
<span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">Object</span>.keys(data)
<span class="hljs-built_in">console</span>.log(arr.length) <span class="hljs-comment">//0 </span>
<span class="hljs-built_in">console</span>.log(arr) <span class="hljs-comment">// []</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-40">转换成字符串进行比对</h4>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> data = &#123;&#125;;
<span class="hljs-keyword">let</span> flag = (<span class="hljs-built_in">JSON</span>.stringify(data) == <span class="hljs-string">"&#123;&#125;"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-41">for in 循环判断</h4>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> data = &#123;&#125;;

<span class="hljs-keyword">let</span> a = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;

  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> data) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;

&#125;

a(); <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-42">jquery的isEmptyObject方法</h4>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> data = &#123;&#125;;
<span class="hljs-keyword">var</span> a = $.isEmptyObject(data);
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">2. 删除对象中某个属性</h3>
<p>delete</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = &#123;<span class="hljs-attr">a</span> : <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>&#125;;
<span class="hljs-keyword">delete</span> a.b;
<span class="hljs-built_in">console</span>.log(a);  <span class="hljs-comment">//&#123;a: 1&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">3. 添加对象属性</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;;
a.b = <span class="hljs-number">2</span>;
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// &#123;a: 1,b: 2&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-45">4. 浅拷贝</h3>
<p>当一个对象拷贝另一个对象的数据的时候，只要一个对象的数据发生改变另一个对象的数据也会发生改变
因为浅拷贝拷贝的是引用的地址，（所以必须在对象是多层才能拷贝，单层拷贝的是数值，多层说明里面套着对象，所以拷贝的是地址。）</p>
<ul>
<li>
<h4 data-id="heading-46">方法一（ES6的方法）：</h4>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">var</span> obj = &#123;<span class="hljs-attr">a</span>:&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"kaiqin"</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">19</span>&#125;&#125;;
 <span class="hljs-keyword">var</span> obj1 = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;,obj);
 obj1.a.name=<span class="hljs-string">"wang"</span>
 <span class="hljs-built_in">console</span>.log(obj1) <span class="hljs-comment">// name已经被改变</span>
 <span class="hljs-built_in">console</span>.log(obj) <span class="hljs-comment">//name已经被改变</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-47">方法二：使用  for  in 循环，遍历每一个属性，将他们赋值给新的对象。要求对象必须是多层的状态下才能实现浅拷贝</h4>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123; <span class="hljs-attr">a</span>: &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"kaiqin"</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">19</span> &#125; &#125; ;
<span class="hljs-keyword">var</span> obj2 = &#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">b</span>:<span class="hljs-number">2</span>,<span class="hljs-attr">c</span>:<span class="hljs-number">3</span>&#125;;
<span class="hljs-comment">//多层</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copy</span>(<span class="hljs-params">obj</span>)</span>&#123;
      <span class="hljs-keyword">var</span> newObj = &#123;&#125;;
      <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> obj)&#123;
            newObj[key] = obj[key];
       &#125;
<span class="hljs-keyword">return</span> newObj;
&#125;
<span class="hljs-comment">//单层</span>
<span class="hljs-keyword">var</span> obj1 = copy(obj);
obj1.a.name=<span class="hljs-string">"wang"</span>
<span class="hljs-built_in">console</span>.log(obj1)
<span class="hljs-built_in">console</span>.log(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-48">5. 深拷贝</h3>
<p>当一个对象拷贝另一个对象的数据的时候，其中一个对象的数据发生变化不会影响另一个对象的数据
因为深考贝拷贝的是对象的数据而不是地址</p>
<ul>
<li>
<h4 data-id="heading-49">方法一：对象是单层的情况下</h4>
</li>
</ul>
<p>Object.assign()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">b</span>:<span class="hljs-number">2</span>,<span class="hljs-attr">c</span>:<span class="hljs-number">3</span>&#125;
<span class="hljs-keyword">var</span> obj1 = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;,obj);
obj1.a = <span class="hljs-number">30</span>;
<span class="hljs-built_in">console</span>.log(obj1,obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-50">方法二：JSON.parse(JSON.stringify())</h4>
</li>
</ul>
<p>用JSON.stringify将对象转成JSON字符串，再用JSON.parse()把字符串解析成对象，一去一来，新的对象产生了，而且对象会开辟新的栈，实现深拷贝。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'kobe'</span>&#125;]
<span class="hljs-keyword">let</span> newArr = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(arr))
arr[<span class="hljs-number">2</span>].name = <span class="hljs-string">'jodan'</span>
<span class="hljs-built_in">console</span>.log(arr)
<span class="hljs-built_in">console</span>.log(newArr)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-51">前端敏捷开发流程</h3>
<h4 data-id="heading-52">markdown</h4>
<p>markdown是一类标记类语言，具有纯文本语法格式。通常用于格式化的自述文件</p>
<h4 data-id="heading-53">apipost</h4>
<p>用于请求接口，也可用于生成文档。</p>
<h3 data-id="heading-54">练手项目</h3>
<ul>
<li>若依 / RuoYi-Vue <a href="https://gitee.com/y_project/RuoYi-Vue" target="_blank" rel="nofollow noopener noreferrer">gitee.com/y_project/R…</a></li>
</ul>
<p><strong>持续更新中</strong>.........................................................................................</p>
<p><strong>微信技术交流群：cbq2393159
群内有免费的前端教程资料，需要的欢迎进群。</strong></p></div>  
</div>
            