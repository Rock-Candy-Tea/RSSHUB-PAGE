
---
title: '写给程序员看的函数式对话 7 - Maybe 和模式匹配'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=328'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 23:49:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=328'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>学生：好久不见啊，今天又有时间来聊天啊</p>
<p>方：嗯，今天想跟你聊聊 Maybe 和模式匹配</p>
<p>直接上 TypeScript 代码：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> addMark = <span class="hljs-function">(<span class="hljs-params">whatever?: <span class="hljs-built_in">string</span></span>) =></span> whatever + <span class="hljs-string">'!'</span>
addMark(<span class="hljs-string">'Frank'</span>) 
<span class="hljs-comment">// 输出 Frank!</span>
addMark() 
<span class="hljs-comment">// 输出 undefined!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后输出的 undefined! 并不是我们想要的输出，一般你会怎么解决这样的问题？</p>
<p>学生：「判空」呗</p>
<p>方：没错，代码差不多是这样：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> addMark = <span class="hljs-function">(<span class="hljs-params">whatever?: <span class="hljs-built_in">string</span></span>) =></span> &#123;
  <span class="hljs-keyword">if</span>(whatever !== <span class="hljs-literal">undefined</span>)&#123;
    <span class="hljs-keyword">return</span> whatever + <span class="hljs-string">'!'</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'!'</span>
  &#125;
&#125;
 
addMark() 
<span class="hljs-comment">// 输出 !</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我问问你，现在 whatever 的类型是什么？</p>
<p>学生：string 呀</p>
<p>方：undefined 也是 string 吗？</p>
<p>学生：哦，我懂你意思了，whatever 的类型是 string | undefined</p>
<p>方：现在我给你介绍另一种思路，我们可以用 <code>Maybe<string></code> 表示 whatever 的类型</p>
<p>学生：听不懂，代码怎么写</p>
<p>方：代码：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Just<X> = &#123; <span class="hljs-attr">_type</span>: <span class="hljs-string">'Just'</span>, <span class="hljs-attr">value</span>: X &#125;
<span class="hljs-keyword">type</span> Nothing = &#123; <span class="hljs-attr">_type</span>: <span class="hljs-string">'Nothing'</span> &#125;
<span class="hljs-keyword">type</span> Maybe<X> = Nothing | Just<X>
<span class="hljs-keyword">const</span> createMaybe = 
  <T>(value:T): Maybe<T> => 
    value === <span class="hljs-literal">undefined</span> ? &#123;<span class="hljs-attr">_type</span>: <span class="hljs-string">'Nothing'</span>&#125; : &#123;<span class="hljs-attr">_type</span>: <span class="hljs-string">'Just'</span>, value&#125;


<span class="hljs-keyword">const</span> addMark = <span class="hljs-function">(<span class="hljs-params">whatever: Maybe<<span class="hljs-built_in">string</span>></span>) =></span> &#123;
  <span class="hljs-keyword">if</span>(whatever._type === <span class="hljs-string">'Just'</span> )&#123;
    <span class="hljs-keyword">return</span> whatever.value + <span class="hljs-string">'!'</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(whatever.type === <span class="hljs-string">'Nothing'</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'!'</span>
  &#125;
&#125;
<span class="hljs-keyword">const</span> readStringFromFile = <span class="hljs-function">()=></span>&#123;
  <span class="hljs-keyword">return</span> createMaybe<<span class="hljs-built_in">string</span>>(<span class="hljs-string">'hi'</span>)
&#125;

<span class="hljs-keyword">const</span> fileContent = readStringFromFile()

<span class="hljs-built_in">console</span>.log(addMark(fileContent))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>学生：确实是没有 undefined 和 null 了，但是你还是要判断 whatever._type 是 'Just' 还是 'Nothing' 不是吗？</p>
<p>方：是的，这是 JS 的表达能力有限所致，如果用 Haskell 写，配合模式匹配，代码就相当简洁了：</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-comment">-- [Char] 就是 String</span>
<span class="hljs-title">readStringFromFile</span> :: [<span class="hljs-type">Char</span>] -> <span class="hljs-type">Maybe</span> [<span class="hljs-type">Char</span>] 
<span class="hljs-title">readStringFromFile</span> path = <span class="hljs-type">Just</span> <span class="hljs-string">"hi"</span> 
<span class="hljs-comment">-- 文件可能不存在，返回空，这里我写死返回 "hi"</span>


<span class="hljs-title">addMark</span> :: <span class="hljs-type">Maybe</span> [<span class="hljs-type">Char</span>] -> [<span class="hljs-type">Char</span>]
<span class="hljs-title">addMark</span> (<span class="hljs-type">Just</span> str) = str ++ <span class="hljs-string">"!"</span>
<span class="hljs-title">addMark</span> <span class="hljs-type">Nothing</span> = <span class="hljs-string">"!"</span>


<span class="hljs-title">main</span> :: <span class="hljs-type">IO</span> ()
<span class="hljs-title">main</span> = <span class="hljs-keyword">do</span> 
  print $ addMark $ readStringFromFile <span class="hljs-string">"./1.txt"</span>

<span class="hljs-comment">-- 输出 "hi!"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你看，没有 null / undefined，也没有 if else。</p>
<p>学生：模式匹配是什么？</p>
<p>方：其实很简单，我们只看 addMark</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-title">addMark</span> :: <span class="hljs-type">Maybe</span> [<span class="hljs-type">Char</span>] -> [<span class="hljs-type">Char</span>]
<span class="hljs-comment">-- addMark 的参数类型是 Maybe [Char]</span>
<span class="hljs-comment">-- Maybe [Char] 只有两种情况：Just [Char] 和 Nothing</span>

<span class="hljs-comment">-- 如果是 Just [Char] 就给 str 后面加上感叹号</span>
<span class="hljs-title">addMark</span> (<span class="hljs-type">Just</span> str) = str ++ <span class="hljs-string">"!"</span>
<span class="hljs-comment">-- 如果是 Nothing 就直接返回感叹号</span>
<span class="hljs-title">addMark</span> <span class="hljs-type">Nothing</span> = <span class="hljs-string">"!"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>学生：看起来跟 switch ... case 差不多啊</p>
<p>方：不一样，switch ... case 是对具体的「值」做比较，模式匹配则是一种「形式上」的匹配，更抽象一些。</p>
<p>接下来我们来练习一下模式匹配，这是斐波那契：</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-title">fib</span> :: <span class="hljs-type">Integer</span> -> <span class="hljs-type">Integer</span>
<span class="hljs-title">fib</span> <span class="hljs-number">0</span> = <span class="hljs-number">0</span>
<span class="hljs-title">fib</span> <span class="hljs-number">1</span> = <span class="hljs-number">1</span>
<span class="hljs-title">fib</span> n = fib (n<span class="hljs-number">-1</span>) + fib (n<span class="hljs-number">-2</span>) 
<span class="hljs-comment">-- 这个版本极慢，有待优化</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是快排：</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-title">qs</span> :: [<span class="hljs-type">Int</span>] -> [<span class="hljs-type">Int</span>]
<span class="hljs-title">qs</span> [] = []
<span class="hljs-title">qs</span> (first:rest) =
  qs (filter (<= first) rest) 
    ++ [first] 
    ++ qs (filter (> first) rest)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以明显地看到，有了模式匹配，几乎就不用再写 if else 了。</p>
<p>学生：还挺方便，那 JS 为什么不引入模式匹配呢？</p>
<p>方：JS 也想引入，不过还在讨论阶段，这里有一个<a href="https://link.zhihu.com/?target=https%3A//github.com/tc39/proposal-pattern-matching%23motivating-examples" target="_blank" rel="nofollow noopener noreferrer">提案</a>，具体代码长这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> fetch(jsonService)
<span class="hljs-keyword">case</span> (res) &#123;
  when &#123;<span class="hljs-attr">status</span>: <span class="hljs-number">200</span>, <span class="hljs-attr">headers</span>: &#123;<span class="hljs-string">'Content-Length'</span>: s&#125;&#125; ->
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`size is <span class="hljs-subst">$&#123;s&#125;</span>`</span>),
  when &#123;<span class="hljs-attr">status</span>: <span class="hljs-number">404</span>&#125; ->
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'JSON not found'</span>),
  when &#123;status&#125; <span class="hljs-keyword">if</span> (status >= <span class="hljs-number">400</span>) -> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> RequestError(res)
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>case ... when ... 这样的代码就是模式匹配。</p>
<p>学生：模式匹配我大概了解了，就是高级版的 switch ... case。但是这个 Maybe 我还是不懂</p>
<p>方：在 Haskell 里，Maybe 的定义是</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-class"><span class="hljs-keyword">data</span> <span class="hljs-type">Maybe</span> a = <span class="hljs-type">Nothing</span> | <span class="hljs-type">Just</span> a <span class="hljs-comment">-- 其中 a 可以是 Int / [Char] 等</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>作为参考，你可以看看 Haskell 里 Bool 的定义</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-class"><span class="hljs-keyword">data</span> <span class="hljs-type">Bool</span> = <span class="hljs-type">True</span> | <span class="hljs-type">False</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你不用在意关键字 data 是什么意思，你只需要用代入法即可，即</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-type">Maybe</span> <span class="hljs-type">Int</span> = <span class="hljs-type">Nothing</span> | <span class="hljs-type">Just</span> <span class="hljs-type">Int</span>
<span class="hljs-type">Maybe</span> [<span class="hljs-type">Char</span>] = <span class="hljs-type">Nothing</span> | <span class="hljs-type">Maybe</span> [<span class="hljs-type">Char</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>学生：那 Just "hi" 中的 Just 是什么？函数？还是类？</p>
<p>方：都不是，Just 就如同 True 或 False 一样，是特殊的值。Just "hi" 是一个整体，它不等于 "hi"，其主要作用就是用来做模式匹配。</p>
<p>学生：那怎么从 Just "hi" 里取出 "hi" 呢？</p>
<p>方：你可以写一个 getValue</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-title">getValue</span> :: <span class="hljs-type">Maybe</span> [<span class="hljs-type">Char</span>] -> [<span class="hljs-type">Char</span>]
<span class="hljs-title">getValue</span> (<span class="hljs-type">Just</span> x) = x
<span class="hljs-title">getValue</span> <span class="hljs-type">Nothing</span> = error <span class="hljs-string">"无法读取值"</span>

<span class="hljs-title">main</span> = <span class="hljs-keyword">do</span> 
  print $ getValue $ <span class="hljs-type">Just</span> <span class="hljs-string">"hi"</span>  <span class="hljs-comment">-- 输出 "hi"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但这是一种非常不推荐的做法。</p>
<p>学生：那推荐做法是？</p>
<p>方：推荐「先不要把值从 Maybe 里取出来」，在真正需要用到值的时候用模式匹配即可：</p>
<pre><code class="hljs language-haskell copyable" lang="haskell"><span class="hljs-title">main</span> = <span class="hljs-keyword">do</span> 
  <span class="hljs-keyword">let</span> maybe = getContentFromFile <span class="hljs-string">"./1.txt"</span>
  <span class="hljs-keyword">case</span> maybe <span class="hljs-keyword">of</span>
    <span class="hljs-type">Just</span> x -> print $ <span class="hljs-string">"result: "</span> ++ x
    <span class="hljs-type">Nothing</span> -> print $ <span class="hljs-string">"we got nothing"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>学生：我不太懂，我先取出来，得到一个 string，不是更方便吗？</p>
<p>方：JS 里确实是这样的，但是 Haskell 是一个支持惰性求值的语言。JS 不支持惰性求值还真不好解释，我举个另外的例子吧，如果 getContentFromFile 是异步操作，你怎么取出值？虽然你取不出值，但是你可以先把后续操作先写上去。</p>
<p>学生：你让我想到了 Promise</p>
<p>方：没错，promise 的值可能要 3 秒钟后返回，你不可能在那傻等 3 秒，不如趁这个时间把后续操作先写到 then 里。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise = readFilePromise(<span class="hljs-string">"./1.txt"</span>)
promise.then(
  <span class="hljs-function"><span class="hljs-params">x</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"result: "</span> + x),
  <span class="hljs-function"><span class="hljs-params">error</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"we go nothing"</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有没有发现上面两段代码迷之相似？</p>
<p>学生：我怎么感觉，Maybe 就是同步的 Promise？<code>Maybe<string></code> 表示可能有 string 也可能为空，<code>Promise<User></code> 表示可能有 User 也可能为空。</p>
<p>方：有那么点意思，后面我们会发现它们的共通之处。</p>
<p>学生：JS 有了空，是不是就没有必要有 Maybe 类型了？</p>
<p>方：没错，就如同我们之前讲的「闭包和对象」一样，它们是殊途同归的，一门语言</p>
<ul>
<li>要么像 JS 那样，设 whatever 的类型为 string | undefined，你写 whatever.split('') 的时候不报错，运行</li>
<li>要么像 TS 那样，设 whatever 的类型为 string | undefined，但是 whatever.split('') 报错，要求你先判空</li>
<li>要么像 Haskell 那样，whatever 的类型为 Maybe [Char]，也就是 Just [Char] | Nothing，你无法直接通过 whatever 调用 string 的 API，除非你用模式匹配拿到 string 值</li>
</ul>
<p>三种方案都可以达到相同的目的，其中 JS 的做法最不安全，但新手最喜欢。TS 和 Haskell 的做法都安全，而且老手喜欢。</p>
<p>学生：原来学好编程要掌握这么多编程语言才行</p>
<p>方：没错！</p>
<p>未完待续……</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            