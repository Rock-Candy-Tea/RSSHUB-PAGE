
---
title: '细谈Go引用的底层实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50fbe86e9d904098b24fc2fe70580745~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 22:37:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50fbe86e9d904098b24fc2fe70580745~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Go怎么可能有引用？得了吧~
有人要说了，那利用<code>make()</code>函数执行后得到的slice、map、channel等类型，不都是得到的引用吗？</p>
<p>我要说：那能叫<strong>引用</strong>吗？你能确定啥叫<strong>引用</strong>吗？
如果你有点迷糊，那么请听我往下讲：</p>
<p>这一切要从变量说起。</p>
<h2 data-id="heading-0">什么是变量</h2>
<p>无论是引用变量还是指针变量，都是变量；那么，什么叫变量？
其实变量本质就是一块内存。通常，我们对计算机内存进行操作，最直接的方式就是：“计算机，在0x0201地址内存一个整数100，在0x00202地址存一个浮点数10.6，读取0x00203的数据...” 这种方式让机器来操作还行，如果直接写成代码让人看的话，这一堆“0x0201、0x0202...”难记的地址能把人给整崩溃了~
于是，聪明的人们想出了一种方法：把一堆难记的地址用其他人类可以方便读懂的方式来间接表示。例如：将“0x0201”的地址命名为“id”，将“0x0202”命名为“score”...然后，代码编译期间，再将"name"等人类能读懂的文字转化为真实的内存地址；于是，变量诞生了~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50fbe86e9d904098b24fc2fe70580745~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，其实每个变量都代表了一块内存，变量名是我们给那块儿内存起的一个别名，内存中存的值就是我们给变量赋的值。变量名在程序编译期间会直接转化为内存地址。</p>
<h2 data-id="heading-1">什么是引用</h2>
<p>引用是指向另外一个变量的变量，或者说，叫一个已知变量的别名。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ccfb569f9834bb492df723fb64b6be0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意，引用和引用本身指向的变量对应的是同一块内存地址。引用本身也会在编译期间转化为真正的内存地址。当然咯，引用和它指向的变量在编译期间会转化为同一个内存地址。</p>
<h2 data-id="heading-2">什么是指针</h2>
<p>指针本身也是一个变量，需要分配内存地址，但是内存地址中存的是另一个变量的内存地址。有点绕口，请看图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/add1df1c84c0474b951e6057ca8d718f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">GO中的引用和指针</h2>
<p>我们先看看“正统”的引用的例子，在C++中(C中是没有引用的哈)：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><stdio.h></span></span>

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span>
</span>&#123;

        <span class="hljs-keyword">int</span> i = <span class="hljs-number">3</span>;
        <span class="hljs-keyword">int</span> *ptr = &i;
        <span class="hljs-keyword">int</span> &ref = i;

        <span class="hljs-built_in">printf</span>(<span class="hljs-string">"%p %p %p\n"</span>, &i, ptr, &ref); 
        <span class="hljs-comment">// 打印出：0x7ffeeac553a8 0x7ffeeac553a8 0x7ffeeac553a8</span>
        <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>变量地址、引用地址、指针的值 均相同；符合常理</p>
<p>那我们再试试Go中类似代码的例子:</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> <span class="hljs-string">"fmt"</span>

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
    i := <span class="hljs-number">3</span>
    ref := i
    ptr := &i
    
    fmt.Println(fmt.Sprintf(<span class="hljs-string">"%p %p %p"</span>, &i, &ref, ptr))
    <span class="hljs-comment">// 打印出 0xc000118000 0xc000118008 0xc000118000</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>变量i地址和指针ptr的值一样，这是符合预期的；但是：正如Go中没有特别的“引用符号”（C++中是<code>int &ref = i;</code>）一样，上述go代码中的<code>ref</code>压根就是个变量，根本不是引用。</p>
<p>可是，很多人不死心，是不是“实验对象”不对啊？代码中使用的是int整型，我们换做<code>slice</code>和<code>map</code>试试？毕竟网上的"资料"都是这么写的：
例如以下截图（只看标红部分就好）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e88a34661468475da089e5fde7e78141~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有如下截图（只看标红部分就好）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7919ab9108d54eaab58f47b9de5b1ac4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>ok，那我们可以试试如下map的代码，看到底有没有引用：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> <span class="hljs-string">"fmt"</span>

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span>&#123;
    i := <span class="hljs-built_in">make</span>(<span class="hljs-keyword">map</span>[<span class="hljs-keyword">string</span>]<span class="hljs-keyword">string</span>)
    i[<span class="hljs-string">"key"</span>]=<span class="hljs-string">"value"</span>

    ref := i

    fmt.Println(fmt.Sprintf(<span class="hljs-string">"%p %p"</span>, &i, &ref))
    <span class="hljs-comment">// 打印出：0xc00010e018 0xc00010e020</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哈哈！不对呀，如果是引用的话，打印的地址应该相同才对，但是现在不相同！所以不存在？
别着急，紧接着看下面的例子：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> <span class="hljs-string">"fmt"</span>

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span>&#123;
    i := <span class="hljs-built_in">make</span>(<span class="hljs-keyword">map</span>[<span class="hljs-keyword">string</span>]<span class="hljs-keyword">string</span>)
    i[<span class="hljs-string">"key"</span>]=<span class="hljs-string">"value"</span>

    ref := i
    ref[<span class="hljs-string">"key"</span>] = <span class="hljs-string">"value1"</span>

    fmt.Println(i[<span class="hljs-string">"key"</span>]) <span class="hljs-comment">// 打印结果：value1</span>
    fmt.Println(ref[<span class="hljs-string">"key"</span>]) <span class="hljs-comment">// 打印结果：value1</span>

    fmt.Println(fmt.Sprintf(<span class="hljs-string">"%p %p"</span>, &i, &ref))
    <span class="hljs-comment">// 打印结果：0xc00000e028 0xc00000e030</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>能猜出来打印了什么吗？变量地址是不对，但是，但是值居然变了！ref变量可以“操控”i变量的内容！就和引用一样！</p>
<p>这就很奇怪了~ 咋回事儿呢？</p>
<p>我们细细研究一下<code>map</code>、<code>slice</code>、<code>channel</code>等具体实现（详情请看：我的其他文章 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fi6448038.github.io%2F2018%2F08%2F26%2Fmap-secret%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://i6448038.github.io/2018/08/26/map-secret/" ref="nofollow noopener noreferrer">图解Go map底层实现</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fi6448038.github.io%2F2018%2F08%2F11%2Farray-and-slice-principle%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://i6448038.github.io/2018/08/11/array-and-slice-principle/" ref="nofollow noopener noreferrer">图解Go slice底层实现</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fi6448038.github.io%2F2019%2F04%2F11%2Fgo-channel%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://i6448038.github.io/2019/04/11/go-channel/" ref="nofollow noopener noreferrer">图解Go channel底层实现</a>）我们发现，这些类型的底层实现都是会有一个指针指向另外的存储地址，所以，在<code>make</code>函数创建了具体的类型实例后，实际上在内存空间中会开辟多个地址空间，而随着变量的赋值，指针引用的那个地址值也会跟着“复制”，因而其他变量可以改变原有变量的内容。</p>
<p>听着是不是有点绕？我们来看看图：</p>
<p>首先实例化了map并赋值</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e9be58c445c4d02988ec31079926585~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后又赋值给了另外一个变量ref</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd54cfcc77034a2aa1a0347b4f24664e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于对于指针变量的值而言，就是一个地址(程序实现上就是一串数字)，所以，在赋值的时候，就“复制”了一串数字，但是，这串数字背后的含义确是另外一个地址，而地址的内容，恰恰就是<code>map</code> <code>slice</code> <code>channel</code> 等数据结构真正底层存储的数据!</p>
<p>所以，两变量因为同一个指针变量指向的内存，而产生了类似于“引用”的效果。假如实例化的类型数据中，没有<code>指针</code>属性，则不会产生这种“类引用”的效果：
例如如下代码：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> <span class="hljs-string">"fmt"</span>

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span>&#123;
    i := <span class="hljs-number">3</span>

    ref := i
    ref = <span class="hljs-number">4</span>

    fmt.Println(i, ref) <span class="hljs-comment">// 打印输出：3 4</span>

    fmt.Println(fmt.Sprintf(<span class="hljs-string">"%p %p"</span>, &i, &ref))
    <span class="hljs-comment">// 打印输出：0xc000016070 0xc000016078</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以将代码上述仔细看看能输出什么，不出意外的话你会发现：“类引用”效果消失了~</p>
<p>要想再次展现“类引用”效果，只要创建一个带有指针属性的类型即可，我们自己实现都可以，无需依赖Go基础库中的<code>map</code>、<code>slice</code>、<code>channel</code>等</p>
<pre><code class="hljs language-Go copyable" lang="Go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> <span class="hljs-string">"fmt"</span>

<span class="hljs-keyword">type</span> Instance <span class="hljs-keyword">struct</span> &#123;
    Name <span class="hljs-keyword">string</span>
    Data *<span class="hljs-keyword">int</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(i Instance)</span> <span class="hljs-title">Store</span><span class="hljs-params">(num <span class="hljs-keyword">int</span>)</span></span> &#123;
    *(i.Data) = num
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(i Instance)</span> <span class="hljs-title">Show</span><span class="hljs-params">()</span> <span class="hljs-title">int</span></span>&#123;
    <span class="hljs-keyword">return</span> *(i.Data)
&#125;



<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span>&#123;
    data := <span class="hljs-number">5</span>

    i := Instance&#123;
        Name:<span class="hljs-string">"hello"</span>,
        Data:&data,
    &#125;

    ref := i
    ref.Store(<span class="hljs-number">7</span>)

    fmt.Println(i.Show(), ref.Show())
    <span class="hljs-comment">// 打印出：7 7</span>

    fmt.Println(fmt.Sprintf(<span class="hljs-string">"%p %p"</span>, &i, &ref))
    <span class="hljs-comment">// 打印出：0xc0000a6018 0xc0000a6030</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看以上代码，是不是实现了“类引用”？ 有人要说了<code>map</code>展示key值，<code>slice</code>展示某个下标的值，没有用方法呀？
这就不对了，其实<code>map</code>的展示key的值<code>mapData[key]</code>也好，更改值也好，<code>slice</code>展示下标值<code>sliceArray[0]</code>也好，更改值也好；背后底层实现也都是些“函数”和“方法”，只不过Go语言把这些函数和方法做成了语法糖，我们无感知罢了~</p>
<p>好了，现在我再问你：还敢说Go语言有引用类型吗？是不是感觉：也有、也没有了？ 😝</p>
<h2 data-id="heading-4">更多精彩内容，请关注我的微信公众号 <code>互联网技术窝</code></h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/795aa185e1914591812cf61fb521ea65~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            