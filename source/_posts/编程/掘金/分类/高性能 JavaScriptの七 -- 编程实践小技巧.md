
---
title: '高性能 JavaScriptの七 -- 编程实践小技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b56c0a99fa0b4cec96874659b076bc85~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 07:04:32 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b56c0a99fa0b4cec96874659b076bc85~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>随着web开发者对JavaScript和浏览器的推动，<strong>在JavaScript中出现了一些十分特别的模式，有精华也有糟粕</strong>（对js性能上来说的），毕竟JavaScript可以是前端最重要的组成之一，“人红是非多”。</p>
<p>这些模式的出现是由于Web中JavaScript的特性决定的，<strong>前端你没得选，后端还可以换语言</strong>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b56c0a99fa0b4cec96874659b076bc85~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<br>
<h1 data-id="heading-0">避免双重求值（Double Evaluation）</h1>
<p>JavaScript 与很多其他语言一样，<strong>允许你在程序中提取一个包含代码的字符串，然后动态执行</strong></p>
<p>四种实现的标准方法：</p>
<blockquote>
<ul>
<li>Function() 构造函数</li>
<li>eval()</li>
<li>setTimeout()</li>
<li>setInterval()</li>
</ul>
</blockquote>
<p>例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> num1 = <span class="hljs-number">1</span>,num2 = <span class="hljs-number">6</span>;
<span class="hljs-comment">//eval()执行代码字符串</span>
sum = <span class="hljs-built_in">eval</span>(<span class="hljs-string">"num1 + num2"</span>);
<span class="hljs-comment">//Function()构造函数执行代码字符串</span>
sum = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">"num1"</span>, <span class="hljs-string">"num2"</span>, <span class="hljs-string">"return num1 +num2"</span>);
<span class="hljs-comment">//setTimeout()执行代码字符串</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-string">"sum = num1 +num2"</span>, <span class="hljs-number">100</span>);
<span class="hljs-comment">//setInterval()执行代码字符串</span>
<span class="hljs-built_in">setInterval</span>(<span class="hljs-string">"sum = num1 +num2"</span>, <span class="hljs-number">100</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当在JavaScript代码中执行另一段JavaScript代码时，都会导致双重求值的性能消耗</p>
<p> 上面这些代码首先会以正常方式求值，然后在执行过程中对包<strong>含于字符串中的代码</strong>发起另一个求值运算
<br></p>
<p>双重求值和直接求值性能对比：
 （<strong>如果觉得测试代码不对的朋友，可以在评论区留言告诉我，不断修正</strong>）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num1 = <span class="hljs-number">1</span>,num2 = <span class="hljs-number">6</span>;
<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'双重求值'</span>)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
   <span class="hljs-comment">//eval()执行代码字符串</span>
    sum = <span class="hljs-built_in">eval</span>(<span class="hljs-string">"num1 + num2"</span>);
&#125;
<span class="hljs-built_in">console</span>.log(sum)
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'双重求值'</span>)
<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'直接求值'</span>)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
   sum = num1 + num2;
&#125;
<span class="hljs-built_in">console</span>.log(sum)
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'直接求值'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>chrome浏览器：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab3d43f5b38d49ac873cf0cb0f66357c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>IE浏览器：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0ad2429d02549c78506b4ab1adbdadd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>火狐浏览器：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86281cbee22b4f45b1b84b9014bb859a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的测试可以看出，<strong>双重求值的速度远远不如直接求值。</strong></p>
<p><em><strong>原因</strong></em>：每次调用eval()都要创建一个新的解释器/编译器实例，另外三个也是一样，所以这必然会导致代码执行速度变慢
<br></p>
<p><strong>像<code>setTimeout</code>和<code>setInterval</code>两个延时函数，第一个参数最好传入函数而不是字符串</strong>。
当然了，正经人谁在延时函数上不写函数写字符串代码呀！ 狗头.jpg</p>
<p>避免双重求值能大大提高JavaScript运行期的性能效率
<br>
<br>
<br></p>
<h1 data-id="heading-1">使用Object/Array直接量</h1>
<p>在JavaScript中创建对象和数组的方法有很多种，但是<strong>使用对象和数组直接量是最快的方式</strong></p>
<hr>
<p>直接量赋值和new Object赋值对比：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.time(<span class="hljs-string">'对象直接量'</span>)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
    <span class="hljs-keyword">var</span> obj = &#123;
        <span class="hljs-attr">name</span>:<span class="hljs-string">'空城机'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">25</span>,
        <span class="hljs-attr">sex</span>: <span class="hljs-string">'男'</span>
    &#125;
&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'对象直接量'</span>)

<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'new Object方式'</span>)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
   <span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
   obj.name = <span class="hljs-string">'空城机'</span>;
   obj.age = <span class="hljs-number">25</span>;
   obj.sex = <span class="hljs-string">'男'</span>;
&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'new Object方式'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>chrome浏览器:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07bbf2e006be46f4986133bf09a4ab95~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>火狐浏览器：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ae1c56d863d4181978f91457d333d93~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>因为在22年IE浏览器即将退出历史舞台，微软一些系统不会支持IE11了，所以这里就不提供IE的测试结果了</strong>
虽然也是一样的，大家可以自己尝试下</p>
<hr>
<br>
<p>数组直接量和new Array对比
 （<strong>如果觉得测试代码不对的朋友，可以在评论区留言告诉我，不断修正</strong>）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-built_in">console</span>.time(<span class="hljs-string">'数组直接量'</span>)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
        <span class="hljs-keyword">var</span> arr = [<span class="hljs-number">30</span>, <span class="hljs-string">'1'</span>, <span class="hljs-literal">null</span>]
    &#125;
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'数组直接量'</span>)
    <span class="hljs-built_in">console</span>.time(<span class="hljs-string">'new Array方式'</span>)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
       <span class="hljs-keyword">var</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
       arr[<span class="hljs-number">0</span>] = <span class="hljs-number">30</span>,
       arr[<span class="hljs-number">1</span>] = <span class="hljs-string">'1'</span>,
       arr[<span class="hljs-number">2</span>] = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'new Array方式'</span>)
 </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>chrome浏览器:</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaa1e1be6f8f462dad0d2a65769e26cd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>下面这里划重点了</strong>，在火狐浏览器测试结果很令我惊讶：</p>
<p><strong>火狐浏览器：</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/010551d6b1ed40f38f4b6b50767a1b49~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>火狐浏览器测试出来数组直接量的时间反倒更长，这河里吗？</p>
<p>然后我赶紧测试了下<strong>IE浏览器</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ff83afa696e4c40a1088d934a6015b3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>IE也符合之前的结论，那是什么原因导致火狐浏览器结果不同？</strong></p>
<p>我又直接在火狐浏览器控制条输入代码，发现结果正确
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/335ba64401434b83b39b8b6826200ea9~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我有两个猜测：
<del>1. 测试的数据量不够大</del>
2. 火狐引擎的调整</p>
<p>接下来我调整了循环次数，但是火狐浏览器控制台结果两种性能差别不大，多次测试还是数组直接量的方式要慢一些</p>
<p>然后我调换了测试方法的位置，让new Array在上面先执行
新的测试代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-built_in">console</span>.time(<span class="hljs-string">'new Array方式'</span>)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
       <span class="hljs-keyword">var</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
       arr[<span class="hljs-number">0</span>] = <span class="hljs-number">30</span>,
       arr[<span class="hljs-number">1</span>] = <span class="hljs-string">'1'</span>,
       arr[<span class="hljs-number">2</span>] = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'new Array方式'</span>)
    <span class="hljs-built_in">console</span>.time(<span class="hljs-string">'数组直接量'</span>)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
        <span class="hljs-keyword">var</span> arr = [<span class="hljs-number">30</span>, <span class="hljs-string">'1'</span>, <span class="hljs-literal">null</span>]
    &#125;
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'数组直接量'</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>火狐：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf0e8808540a484295826f2443b7b8eb~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样结果就很明显了，数组直接量性能更快</p>
<p>好家伙，我直接 ？号就出来了</p>
<p><strong>这是火狐引擎运行js的“小彩蛋”吗，上网找了半天资料也没找到</strong>，可能就是引擎加载的时候的差异吧</p>
<p>之后测试就直接在控制台输入测试了
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d834606b6d1142498a257e347df6bf52~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<br>
<h1 data-id="heading-2">避免重复工作</h1>
<p><strong>性能优化说的最多的就是避免重复工作</strong></p>
<p>方式：</p>
<ul>
<li>
<p>延迟加载</p>
<ul>
<li>在方法被第一次调用时，检查决定使用那种方法去绑定事件处理起，然后原始函数被新函数覆盖</li>
<li>延时函数第一次调用会消耗时间较长</li>
<li>当一个函数在页面中不会立刻调用，可以使用延迟加载优化性能</li>
</ul>
</li>
<li>
<p>条件预加载</p>
<ul>
<li>在脚本加载前检测，适用于一个函数马上要被用到，并且在整个页面的生命周期中频繁出现的场合</li>
</ul>
</li>
<li>
<p>位操作</p>
<ul>
<li>在JavaScript中也有与或等操作，这些操作可以加快js的运算性能</li>
</ul>
</li>
<li>
<p>原生方法</p>
<ul>
<li>无论你的JavaScript代码如何优化，都不会比JavaScript引擎提供的原生方法更快</li>
<li>JavaScript原生方法依旧提取存在浏览器中了，被编译成了机器码</li>
<li>比如Math方法，进行复杂数学运算时，可以使用内置的Math对象中的方法</li>
<li>菜鸟教程：<a href="https://www.runoob.com/jsref/jsref-obj-math.html" target="_blank" rel="nofollow noopener noreferrer">JavaScript Math 对象</a></li>
</ul>
</li>
</ul>
 <br>
 <hr>
<br><br>
<h1 data-id="heading-3">小节</h1>
<p><strong>平时写代码时可以优化的点①</strong>：
避免使用双重求值的方法，比如eval和Function构造器，如果必须要用也没什么办法了。延迟函数记得写方法而不是代码字符串作为第一个参数。</p>
<p><strong>平时写代码时可以优化的点②</strong>：
对象直接量和数组直接量的性能优于于new出来的Object和Array  （虽然数组直接量在火狐浏览器有点奇怪）</p>
<p><strong>平时写代码时可以优化的点③</strong>：
去看上面如何避免重复工作</p>
<br>
<br>
<br>
 建议把这些知识的应用变成习惯
 <br>
<br>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/769f66fc27964fa48607eab6e6a6a57d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            