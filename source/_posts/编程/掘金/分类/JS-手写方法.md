
---
title: 'JS-手写方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4864'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 18:40:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=4864'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">手写call方法</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.newCall = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">context</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(context === <span class="hljs-literal">null</span> || context === <span class="hljs-literal">undefined</span>)&#123;
        context = <span class="hljs-built_in">window</span>;
    &#125;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> context != <span class="hljs-string">"object"</span> && <span class="hljs-keyword">typeof</span> context!= <span class="hljs-string">"function"</span>)&#123;
        context = <span class="hljs-built_in">Object</span>(context)
    &#125;
    <span class="hljs-keyword">var</span> arr = <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>).slice(<span class="hljs-number">1</span>);
    <span class="hljs-keyword">var</span> key = <span class="hljs-built_in">Date</span>.now().toString(<span class="hljs-number">36</span>);
    context[key] = <span class="hljs-built_in">this</span>;
    <span class="hljs-built_in">eval</span>(<span class="hljs-string">"context[key]("</span>+arr.toString()+<span class="hljs-string">")"</span>);
    <span class="hljs-keyword">delete</span> context[key]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">手写Tab切换</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取元素</span>
<span class="hljs-keyword">var</span> mTitle = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'title'</span>);
<span class="hljs-keyword">var</span> mCon = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'con'</span>);
<span class="hljs-keyword">var</span> mH2s = oTitle.getElementsByTagName(<span class="hljs-string">"h2"</span>);
<span class="hljs-keyword">var</span> mLis = oCon.getElementsByTagName(<span class="hljs-string">"li"</span>);

<span class="hljs-comment">// 减少读取次数</span>
<span class="hljs-keyword">var</span> mH2sLength = mH2s.length;

<span class="hljs-comment">// 外边的for仅仅是为了给所有的h2绑定点击事件</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;i<mH2sLength;i++)&#123;
    mH2s[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 内层的for是为了遍历所有的h2 判断哪一个是点击的h2</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<mH2sLength;i++)&#123;
            <span class="hljs-keyword">if</span>(mH2s[i] === <span class="hljs-built_in">this</span>)&#123;
                mH2s[i].classList.add(<span class="hljs-string">"active"</span>);
                mLis[i].classList.add(<span class="hljs-string">"show"</span>);
            &#125;<span class="hljs-keyword">else</span>&#123;
                mH2s[i].classList.remove(<span class="hljs-string">"active"</span>);
                mLis[i].classList.remove(<span class="hljs-string">"show"</span>);
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">手写斐波那契数列</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
需求require:使用一个数组，保存50长度的斐波那契数列值
斐波那契数列前两个值是0和1
0 1 1 2 3 5 8 13 21 34
*/</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>];
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i =<span class="hljs-number">2</span>;i<<span class="hljs-number">50</span>;i++)&#123;
    arr[i] = arr[i-<span class="hljs-number">1</span>] + arr[i-<span class="hljs-number">2</span>];
&#125;
<span class="hljs-built_in">console</span>.log(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">手写快排</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr =[<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">6</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">7</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">6</span>,<span class="hljs-number">9</span>,<span class="hljs-number">7</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>];
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">quickSort</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(arr.length<=<span class="hljs-number">1</span>)&#123;
        <span class="hljs-keyword">return</span> arr;
    &#125;
    <span class="hljs-keyword">var</span> center = arr.pop();
    <span class="hljs-keyword">var</span> left = [],
        right = [];
    arr.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item,index</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(item>center)&#123;
            right.push(item);
        &#125;<span class="hljs-keyword">else</span>&#123;
            left.push(item);
        &#125;
    &#125;)
    <span class="hljs-keyword">var</span> re = quickSort(left).concat(center,quickSort(right));
    <span class="hljs-keyword">return</span> re;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">手写冒泡</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//手写冒泡</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">maopao</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i =<span class="hljs-number">0</span>;i<arr.length;i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>;j<arr.length-i;j++)&#123;
            <span class="hljs-keyword">if</span>(arr[j]>arr[j+<span class="hljs-number">1</span>])&#123;
                <span class="hljs-keyword">var</span> temp = arr[j+<span class="hljs-number">1</span>];
                arr[j+<span class="hljs-number">1</span>] = arr[j];
                arr[j] = temp;
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;


<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">6</span>,<span class="hljs-number">3</span>];
maopao(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">手写拼接时间戳（yyyy-mmm-dd hh:ms:ss）</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTime</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> nowDate = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
    <span class="hljs-keyword">var</span> yy = nowDate.getFullYear();
    <span class="hljs-keyword">var</span> mm = nowDate.getMonth()+<span class="hljs-number">1</span>;
    <span class="hljs-keyword">var</span> dd = nowDate.getDate();
    
    <span class="hljs-keyword">var</span> hh = nowDate.getHours();
    <span class="hljs-keyword">var</span> ms = nowDate.getMinutes();
    <span class="hljs-keyword">var</span> ss = nowDate.getSeconds();
    <span class="hljs-keyword">var</span> re = yy +<span class="hljs-string">"-"</span>+ mm +<span class="hljs-string">"-"</span>+ dd +<span class="hljs-string">" "</span>+hh+<span class="hljs-string">":"</span>+ms+<span class="hljs-string">":"</span>+ss;
    <span class="hljs-built_in">console</span>.log(re)
    
&#125;
<span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    getTime()
&#125;,<span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">手写浅拷贝</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">"小明"</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-number">12</span>,
    <span class="hljs-attr">say</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"会说"</span>);
    &#125;,
    <span class="hljs-attr">skill</span>:[<span class="hljs-string">"篮球"</span>,<span class="hljs-string">"足球"</span>,<span class="hljs-string">"羽毛球"</span>],
    <span class="hljs-attr">score</span>:&#123;
        <span class="hljs-attr">china</span>:<span class="hljs-number">120</span>,
        <span class="hljs-attr">english</span>:<span class="hljs-number">130</span>,
        <span class="hljs-attr">math</span>:<span class="hljs-number">140</span>
    &#125;
&#125;

<span class="hljs-keyword">var</span> newObj = &#123;&#125;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> obj)&#123;
    newObj[key] = obj[key]
&#125;

<span class="hljs-built_in">console</span>.log(newObj);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">手写深拷贝</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">"小明"</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-number">12</span>,
    <span class="hljs-attr">say</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"会说"</span>);
    &#125;,
    <span class="hljs-attr">skill</span>:[<span class="hljs-string">"篮球"</span>,<span class="hljs-string">"足球"</span>,<span class="hljs-string">"羽毛球"</span>],
    <span class="hljs-attr">score</span>:&#123;
        <span class="hljs-attr">china</span>:<span class="hljs-number">120</span>,
        <span class="hljs-attr">english</span>:<span class="hljs-number">130</span>,
        <span class="hljs-attr">math</span>:<span class="hljs-number">140</span>
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkType</span>(<span class="hljs-params">o</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(o).slice(<span class="hljs-number">8</span>,-<span class="hljs-number">1</span>).toLowerCase();
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(checkType(obj) === <span class="hljs-string">"object"</span>)&#123;
        <span class="hljs-keyword">var</span> newObj = &#123;&#125;;
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(checkType(obj)===<span class="hljs-string">"Array"</span>)&#123;
        <span class="hljs-keyword">var</span> newObj = [];
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">return</span> obj;
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> obj)&#123;
        newObj[key] = deepCopy(obj[key]);
    &#125;
    <span class="hljs-keyword">return</span> newObj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">手写数组去重</h1>
<h2 data-id="heading-9">数组去重方法1</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">`创建一个新数组，把值依次添加到新数组中，如果新数组已经存在，则忽略不再添加`</span>

<span class="hljs-string">``</span><span class="hljs-string">`js
var arr = [1,2,4,2,1,5,7,2,3,8,3,5,7];
var newArr = [];
arr.forEach(function(item,index)&#123;
    if(newArr.indexOf(item)===-1)&#123;
        newArr.push(item);
    &#125;
&#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">数组去重方法2</h2>
<p><code>for for嵌套</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">7</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">8</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">7</span>];
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i =<span class="hljs-number">0</span>;i<arr.length;i++)&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> j = i+<span class="hljs-number">1</span>;j<arr.length;i++)&#123;
        <span class="hljs-keyword">if</span>(arr[i]===arr[j])&#123;
            arr.splice(j,<span class="hljs-number">1</span>);
            j--;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">数组去重方法3</h2>
<p><code>检测每一个值的第一次出现的位置 是不是当前值的下标，如果是则第一次出现，否则已经出现过了</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">7</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">8</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">7</span>];
arr.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item,index</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(arr.indexOf(item)===index)&#123;
        newArr.push(item)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">数组去重方法4</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">7</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">8</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">7</span>];
<span class="hljs-keyword">var</span> newArr = arr.filter(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item,index</span>)</span>&#123;
    <span class="hljs-keyword">return</span> arr.indexOf(item) === index;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">手写随机数</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">newRandom</span>(<span class="hljs-params">a,b</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random()*(b-a)+a);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            