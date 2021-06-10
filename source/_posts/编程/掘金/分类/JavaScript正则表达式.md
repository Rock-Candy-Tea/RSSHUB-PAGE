
---
title: 'JavaScript正则表达式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5ec91f8e8094b0c8fe988ada269c873~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 19:54:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5ec91f8e8094b0c8fe988ada269c873~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<blockquote>
<p>正则表达式是用于匹配字符串中字符组合的模式。在 JavaScript中，正则表达式也是对象。这些模式被用于 RegExp 的 exec 和 test 方法, 以及 String 的 match、matchAll、replace、search 和 split  方法。</p>
</blockquote>
<p>本章介绍 JavaScript 正则表达式。
通过使用正则表达式，可以：</p>
<ul>
<li>
<p>测试字符串内的模式，可以测试输入字符串，以查看字符串内是否出现电话号码模式或信用卡号码模式。这称为数据验证。</p>
</li>
<li>
<p>替换文本， 可以使用正则表达式来识别文档中的特定文本，完全删除该文本或者用其他文本替换它。</p>
</li>
<li>
<p>基于模式匹配从字符串中提取子字符串， 可以查找文档内或输入域内特定的文本。</p>
</li>
</ul>
<h1 data-id="heading-1">基础用法</h1>
<h2 data-id="heading-2">创建一个正则表达式</h2>
<p>使用一个正则表达式字面量，其由包含在斜杠之间的模式组成，如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> re = <span class="hljs-regexp">/ab+c/</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>脚本加载后，正则表达式字面量就会被编译。当正则表达式保持不变时，使用此方法可获得更好的性能。
或者调用 <code>RegExp</code> 对象的构造函数，如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> re = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"ab+c"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在脚本运行过程中，用构造函数创建的正则表达式会被编译。如果正则表达式将会改变，或者它将会从用户输入等来源中动态地产生，就需要使用构造函数来创建正则表达式。</p>
<h2 data-id="heading-3">js里使用正则</h2>





































<table><thead><tr><th><strong>方法</strong></th><th><strong>描述</strong></th></tr></thead><tbody><tr><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec" target="_blank" rel="nofollow noopener noreferrer">exec</a></td><td>一个在字符串中执行查找匹配的RegExp方法，它返回一个数组（未匹配到则返回 null）。</td></tr><tr><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test" target="_blank" rel="nofollow noopener noreferrer">test</a></td><td>一个在字符串中测试是否匹配的RegExp方法，它返回 true 或 false。</td></tr><tr><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/match" target="_blank" rel="nofollow noopener noreferrer">match</a></td><td>一个在字符串中执行查找匹配的String方法，它返回一个数组，在未匹配到时会返回 null。</td></tr><tr><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll" target="_blank" rel="nofollow noopener noreferrer">matchAll</a></td><td>一个在字符串中执行查找所有匹配的String方法，它返回一个迭代器（iterator）。</td></tr><tr><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/search" target="_blank" rel="nofollow noopener noreferrer">search</a></td><td>一个在字符串中测试匹配的String方法，它返回匹配到的位置索引，或者在失败时返回-1。</td></tr><tr><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/replace" target="_blank" rel="nofollow noopener noreferrer">replace</a></td><td>一个在字符串中执行查找匹配的String方法，并且使用替换字符串替换掉匹配到的子字符串。</td></tr><tr><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/split" target="_blank" rel="nofollow noopener noreferrer">split</a></td><td>一个使用正则表达式或者一个固定字符串分隔一个字符串，并将分隔后的子字符串存储到数组中的 <code>String</code> 方法。</td></tr></tbody></table>
<ul>
<li>
<p>Exec 和 match的区别</p>
<ul>
<li>
<p>分别是RegExp类和String类的方法</p>
</li>
<li>
<p>exec 只会匹配第一个符合的字符串（意味着g对其不起作用）, match 是否返回所有匹配的数组跟正则表达式里是否带着g有关系</p>
</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> str = <span class="hljs-string">'d3aish hello world d5aisy'</span>;
<span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/\dai/g</span>;
<span class="hljs-comment">//  先看没有g的情况</span>

<span class="hljs-built_in">console</span>.log(str.match(reg));  <span class="hljs-comment">// ['3ai', '5ai']</span>
<span class="hljs-built_in">console</span>.log(reg.exec(str)); <span class="hljs-comment">// ['3ai']</span>

<span class="hljs-comment">// 不带g</span>
<span class="hljs-keyword">const</span> str = <span class="hljs-string">'d3aish hello world d5aisy'</span>;
<span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/\dai/</span>;
<span class="hljs-comment">//  先看没有g的情况</span>

<span class="hljs-built_in">console</span>.log(str.match(reg));  <span class="hljs-comment">// ['3ai']</span>
<span class="hljs-built_in">console</span>.log(reg.exec(str)); <span class="hljs-comment">// ['3ai']</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">量词</h2>





































<table><thead><tr><th><strong>Characters</strong></th><th><strong>Meaning</strong></th></tr></thead><tbody><tr><td><code>x*</code></td><td>将前面的项“x”匹配0次或更多次。<br>例如，/bo*/匹配“A ghost booooed”中的“boooo”和“A bird warbled”中的“b”，但在“A goat grunt”中没有匹配。</td></tr><tr><td><code>x+</code></td><td>将前一项“x”匹配1次或更多次。等价于&#123;1,&#125;。<br>例如，/a+/匹配“candy”中的“a”和“caaaaaaandy”中的“a”。</td></tr><tr><td><code>x?</code></td><td>将前面的项“x”匹配0或1次。<br>例如,/e?le?/匹配angel中的el和angle中的le。<br>如果立即在任何量词*、+、?或&#123;&#125;之后使用，则使量词是非贪婪的(匹配最小次数)，而不是默认的贪婪的(匹配最大次数)。</td></tr><tr><td><code>x&#123;n&#125;</code></td><td>其中“n”是一个正整数，与前一项“x”的n次匹配。<br>例如，/a&#123;2&#125;/ 不匹配“candy”中的“a”，但它匹配“caandy”中的所有“a”，以及“caaandy”中的前两个“a”。</td></tr><tr><td><code>x&#123;n,&#125;</code></td><td>其中，“n”是一个正整数，与前一项“x”至少匹配“n”次。<br>例如，/a&#123;2，&#125;/不匹配“candy”中的“a”，但匹配“caandy”和“caaaaaaandy”中的所有a。</td></tr><tr><td><code>x&#123;n,m&#125;</code></td><td>其中，“n”是0或一个正整数，“m”是一个正整数，而m > n至少与前一项“x”匹配，最多与“m”匹配。例如，/a&#123;1,3&#125;/不匹配“cndy”中的“a”，“candy”中的“a”，“caandy”中的两个“a”，以及“caaaaaaandy”中的前三个“a”。注意，当匹配“caaaaaaandy”时，匹配的是“aaa”，即使原始字符串中有更多的“a”。</td></tr><tr><td><code>x*?</code><br><code>x+?</code><br><code>x??</code><br><code>x&#123;n&#125;?</code><br><code>x&#123;n,&#125;?</code><br><code>x&#123;n,m&#125;?</code></td><td>默认情况下，像 <code>*</code> 和 <code>+</code> 这样的量词是“贪婪的”，这意味着它们试图匹配尽可能多的字符串。?量词后面的字符使量词“非贪婪”：意思是它一旦找到匹配就会停止。例如，给定一个字符串“some   new   thing”:<br><code>/<.*>/</code>will match "  new  "<br><code>/<.*?>/</code> will match ""</td></tr></tbody></table>
<h2 data-id="heading-5">标志符</h2>
<p>正则表达式有六个可选参数 ( <code>flags</code> ) 允许全局和不分大小写搜索等。这些参数既可以单独使用也能以任意顺序一起使用, 并且被包含在正则表达式实例中。</p>

































<table><thead><tr><th><strong>标志</strong></th><th><strong>描述</strong></th></tr></thead><tbody><tr><td><code>g</code></td><td>全局搜索。</td></tr><tr><td><code>i</code></td><td>不区分大小写搜索。</td></tr><tr><td><code>m</code></td><td>多行搜索。</td></tr><tr><td><code>s</code></td><td>允许 <code>.</code> 匹配换行符。</td></tr><tr><td><code>u</code></td><td>使用unicode码的模式进行匹配。</td></tr><tr><td><code>y</code></td><td>执行“粘性( <code>sticky</code> )”搜索,匹配从目标字符串的当前位置开始。</td></tr></tbody></table>
<p>为了在正则表达式中包含标志，请使用以下语法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> re = <span class="hljs-regexp">/pattern/</span>flags;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> re = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"pattern"</span>, <span class="hljs-string">"flags"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>值得注意的是，标志是一个正则表达式的一部分，它们在接下来的时间将不能添加或删除。</strong></p>
<h3 data-id="heading-6">标志符g</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/abc/gi</span>;
<span class="hljs-keyword">const</span> str = <span class="hljs-string">'helloabc'</span>;

reg.test(str) <span class="hljs-comment">// true</span>
reg.test(str) <span class="hljs-comment">// false</span>
reg.test(str) <span class="hljs-comment">// true</span>
reg.test(str) <span class="hljs-comment">// false</span>


<span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/abc/i</span>;
<span class="hljs-keyword">const</span> str = <span class="hljs-string">'helloabc'</span>;

reg.test(str) <span class="hljs-comment">// true</span>
reg.test(str) <span class="hljs-comment">// true</span>
reg.test(str) <span class="hljs-comment">// true</span>
reg.test(str) <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>全局正则表达式的另一个属性</strong> <code>lastIndex</code> <strong>用于存放上一次匹配文本之后的第一个字符的位置。</strong>
<code>RegExp.prototype.exec()</code> 和 <code>RegExp.prototype.test()</code> 方法都以 <code>lastIndex</code> 属性中所存储的位置作为下次正则匹配检索的起点。连续调用这两个方法就可以遍历字符串中的所有匹配文本。
<code>lastIndex</code> 属性可读写，当 <code>RegExp.prototype.exec()</code> 或 <code>RegExp.prototype.test()</code> 再也找不到可以匹配的文本时，会自动把 lastIndex 属性重置为 0。
因此使用这两个方法来检索文本，是可以无限执行下去的。</p>
<h3 data-id="heading-7">标志符y</h3>
<p>执行“粘性( <code>sticky</code> )”搜索,匹配从目标字符串的当前位置开始</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> searchStrings, stickyRegexp;

stickyRegexp = <span class="hljs-regexp">/foo/y</span>;

searchStrings = [
    <span class="hljs-string">"foo"</span>,
    <span class="hljs-string">" foo"</span>,
    <span class="hljs-string">"  foo"</span>,
];
searchStrings.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">text, index</span>) </span>&#123;
    stickyRegexp.lastIndex = <span class="hljs-number">1</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"found a match at"</span>, index, <span class="hljs-string">":"</span>, stickyRegexp.test(text));
&#125;);

<span class="hljs-comment">// found a match at 0 : false</span>
<span class="hljs-comment">// found a match at 1 : true</span>
<span class="hljs-comment">// found a match at 2 : false</span>

<span class="hljs-comment">// 如果把y改成g</span>
<span class="hljs-comment">// found a match at 0 : false</span>
<span class="hljs-comment">// found a match at 1 : true</span>
<span class="hljs-comment">// found a match at 2 : true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以理解为必须为在lastIndex开头去匹配，即index为1时开始匹配 <code>/^abc/</code> ，实现更精准的位置控制。</p>
<h1 data-id="heading-8">高级用法</h1>
<h2 data-id="heading-9">贪婪模式和非贪婪模式</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str=<span class="hljs-string">'aacbacbc'</span>;
<span class="hljs-keyword">var</span> reg=<span class="hljs-regexp">/a.*b/</span>;
<span class="hljs-keyword">var</span> res=str.match(reg);
<span class="hljs-comment">// aacbacb index为0</span>
<span class="hljs-built_in">console</span>.log(res);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，匹配到第一个a后，开始匹配.*，由于是贪婪模式，它会一直往后匹配，直到最后一个满足条件的b为止，因此匹配结果是aacbacb</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str=<span class="hljs-string">'aacbacbc'</span>;
<span class="hljs-keyword">var</span> reg=<span class="hljs-regexp">/a.*?b/</span>;
<span class="hljs-keyword">var</span> res=str.match(reg);
<span class="hljs-comment">// acbacb index为1</span>
<span class="hljs-built_in">console</span>.log(res);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个匹配的是a，然后再匹配下一个字符a时，和正则不匹配，因此匹配失败，index挪到1，接下来匹配成功了ac，继续往下匹配，由于是贪婪模式，尽可能多的去匹配结果，直到最后一个符合要求的b为止，因此匹配结果是acbacb</p>
<h2 data-id="heading-10">捕获组</h2>
<p>对于要重复单个字符，非常简单，直接在字符后加上限定符即可，例如 a+ 表示匹配1个或一个以上的a，a?表示匹配0个或1个a。</p>
<p>但是我们如果要对多个字符进行重复怎么办呢？此时我们就要用到分组，我们可以使用小括号"()"来指定要重复的子表达式，然后对这个子表达式进行重复，例如：(abc)? 表示0个或1个abc 这里一 个括号的表达式就表示一个分组 。
非捕获组有很多种形式，其中包括：零宽度断言和模式修正符</p>
<h3 data-id="heading-11"><strong>反向引用</strong></h3>
<p>引用的是前面捕获组中的文本而不是正则，也就是说反向引用处匹配的文本应和前面捕获组中的文本相同。如
<code>/(["'])(abc).*\1/</code>
其中使用了分组，\1就是对引号这个分组的引用，它匹配包含在两个引号或者两个单引号中的所有字符串，如，"abc" 或 " ' " 或 ' " ' ，但是请注意，它并不会对" a'或者 'a"匹配。平时开发的时候也常用于html标签的匹配</p>
<h3 data-id="heading-12">命名捕获组</h3>
<p>捕获组其实是分为编号捕获组 <code>Numbered Capturing Groups</code> 和命名捕获组 <code>Named Capturing Groups</code> 的，我们上面说的捕获组，默认指的是编号捕获组。命名捕获组，也是捕获组，只是语法不一样。命名捕获组的语法如下： <code>(?<name>group)</code> 或 <code>(?'name'group)</code> ，其中 <code>name</code> 表示捕获组的名称， <code>group</code> 表示捕获组里面的正则。</p>
<h3 data-id="heading-13"><strong>非捕获组</strong></h3>
<blockquote>
<p><strong>语法：(?:Pattern)</strong></p>
</blockquote>
<p>如：匹配indestry或者indestries</p>
<p>我们可以使用indestr(y|ies)或者indestr(?:y|ies)</p>
<p>以 (?) 开头的组是纯的 <em>非捕获</em> 组，它不捕获文本 ，也不针对组合计进行计数。就是说， <strong>如果小括号中以?号开头，那么这个分组就不会捕获文本，当然也不会有组的编号</strong> ，因此也不存在反向引用。
我们通过捕获组就能够得到我们想要匹配的内容了，那为什么还要有非捕获组呢？
原因是捕获组捕获的内容是被存储在内存中，可供以后使用，比如反向引用就是引用的内存中存储的捕获组中捕获的内容。而非捕获组则不会捕获文本，也不会将它匹配到的内容单独分组来放到内存中。所以，使用非捕获组较使用捕获组更节省内存。</p>
<ul>
<li>实际应用场景，可以快速提取想要的信息</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">'https://www.toutiao.com'</span>.match(<span class="hljs-regexp">/(?:https?:\/\/)(.*)/</span>)
<span class="hljs-comment">// ["https://www.toutiao.com", "www.toutiao.com"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">断言</h2>
<p><strong>零宽度断言</strong></p>

























<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>(?=y)</td><td>匹配'x'仅仅当'x'后面跟着'y'.这种叫做先行断言。<br>例如，/Jack(?=Sprat)/会匹配到'Jack'仅当它后面跟着'Sprat'。<br>/Jack(?=Sprat|Frost)/匹配‘Jack’仅当它后面跟着'Sprat'或者是‘Frost’。<br>但是‘Sprat’和‘Frost’都不是匹配结果的一部分。</td></tr><tr><td>(?<=y)x</td><td>匹配'x'仅当'x'前面是'y'.这种叫做后行断言。<br>例如，/(?<=Jack)Sprat/会匹配到' Sprat '仅仅当它前面是' Jack '。<br>/(?<=Jack|Tom)Sprat/匹配‘ Sprat ’仅仅当它前面是'Jack'或者是‘Tom’。但是‘Jack’和‘Tom’都不是匹配结果的一部分。</td></tr><tr><td>x(?!y)</td><td>仅仅当'x'后面不跟着'y'时匹配'x'，这被称为正向否定查找。<br>例如，仅仅当这个数字后面没有跟小数点的时候，/\d+(?!.)/ 匹配一个数字。<br>正则表达式/\d+(?!.)/.exec("3.141")匹配‘141’而不是‘3.141’</td></tr><tr><td>(?<!y)x</td><td>仅仅当'x'前面不是'y'时匹配'x'，这被称为反向否定查找。<br>例如, 仅仅当这个数字前面没有负号的时候，/(?<!-)\d+/ 匹配一个数字。<br>/(?<!-)\d+/.exec('3') 匹配到 "3"。<br>/(?<!-)\d+/.exec('-3') 因为这个数字前有负号，所以没有匹配到。</td></tr></tbody></table>
<p>这四个非捕获组用于匹配表达式X，但是不包含表达式的文本。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5ec91f8e8094b0c8fe988ada269c873~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">例子</h3>
<blockquote>
<p><strong>如何把一串整数转换成千位分隔形式，例如10000000000，转换成10,000,000,000。</strong></p>
</blockquote>
<p>除了常规的方法，可以使用正则解这个题</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> str = <span class="hljs-string">"100000000000"</span>;
<span class="hljs-keyword">const</span> reg= <span class="hljs-regexp">/(?=(\B\d&#123;3&#125;)+$)/g</span>;
<span class="hljs-built_in">console</span>.log(str.replace(reg, <span class="hljs-string">","</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">回溯</h2>
<p>原字符串</p>
<p>"Regex"</p>
<h3 data-id="heading-17">贪婪匹配过程分析</h3>
<p><code>".*"</code>
第一个 <code>"</code> 取得控制权，匹配正则中的 <code>"</code> ，匹配成功，控制权交给 <code>.*</code></p>
<p><code>.</code>取得控制权后，匹配接下来的字符。<code>.</code>代表匹配任何字符，代表可匹配可不匹配，这属于贪婪模式的标识符，会优先尝试匹配，于是接下来从1位置处的R开始匹配，依次成功匹配了R，e，g，e，x，接着继续匹配最后一个字符 <code>"</code> ，匹配成功，这时候已经匹配到了字符串的结尾，所以 <code>.*</code> 匹配结束，将控制符交给正则式中最后的 <code>"</code></p>
<p><code>"</code> 取得控制权后，由于已经是到了字符串的结尾，因此匹配失败，向前查找可供回溯的状态，控制权交给 <code>.*</code> ，<code>.*</code> 让出一个字符 <code>"</code> ，再把控制权交给<code>"</code>，此时刚好匹配成功。</p>
<p>至此，整个正则表达式匹配完毕，匹配结果为”Regex”，匹配过程中回溯了1次</p>













































<table><thead><tr><th>"</th><th>"</th></tr></thead><tbody><tr><td>".*</td><td>"Re</td></tr><tr><td>".*</td><td>"Reg</td></tr><tr><td>".*</td><td>"Rege</td></tr><tr><td>".*</td><td>"Rege</td></tr><tr><td>".*</td><td>"Regex</td></tr><tr><td>".*</td><td>"Regex"</td></tr><tr><td>".*"</td><td>"Regex"</td></tr><tr><td>".*</td><td>"Regex</td></tr><tr><td>".*"</td><td>"Regex"</td></tr></tbody></table>
<h3 data-id="heading-18">回溯陷阱</h3>
<p>下面的例子会让你的浏览器的cpu达到100%，就是回溯太多的导致的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.time(<span class="hljs-string">'reg'</span>)
<span class="hljs-keyword">var</span> reg =  <span class="hljs-regexp">/(a*)*b/</span> 

<span class="hljs-keyword">var</span> str = <span class="hljs-string">'a'</span>.repeat(<span class="hljs-number">28</span>); <span class="hljs-comment">// aaaaaaaaaaaaa...</span>

reg.exec(str)
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'reg'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先简单了解一下正则的实现引擎，主要分为DFA和NFA</p>
<h4 data-id="heading-19">DFA与NFA</h4>
<h4 data-id="heading-20">原因分析</h4>
<ol>
<li><code>a*</code> 由于贪婪模式可以直接匹配整个字符串, 但是由于b的存在，所以需要回溯，但是无论怎么回溯都不可能成功，但是NFA是机器，会一直不断的进行回溯，由于 <code>(a*)*</code> 可以认为是两层的量词组合，所以复杂度会随着字符串的长度指数级的升高。</li>
</ol>
<p><strong>由于是有限状态机，所以并不会死循环，只是会占用大量的cpu，在一定时间之后会完成。</strong></p>
<h2 data-id="heading-21">工具</h2>
<p>在线网站：</p>
<p><a href="https://regex101.com/" target="_blank" rel="nofollow noopener noreferrer">regex101.com/</a></p>
<p><a href="https://regexr.com/" target="_blank" rel="nofollow noopener noreferrer">regexr.com/</a></p>
<p>付费软件：</p>
<p><a href="http://www.regexbuddy.com/buynow.html?" target="_blank" rel="nofollow noopener noreferrer">www.regexbuddy.com/buynow.html…</a></p></div>  
</div>
            