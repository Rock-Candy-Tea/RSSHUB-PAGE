
---
title: 'js事件委托(事件代理)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8947'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 20:01:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=8947'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>起因：</strong></p>
<p>1、这是前端面试的经典题型，要去找工作的小伙伴看看还是有帮助的；</p>
<p>2、其实我一直都没弄明白，写这个一是为了备忘，二是给其他的知其然不知其所以然的小伙伴们以参考；</p>
<p><strong>概述：</strong></p>
<p>那什么叫事件委托呢？它还有一个名字叫事件代理，JavaScript高级程序设计上讲：事件委托就是利用事件冒泡，只指定一个事件处理程序，就可以管理某一类型的所有事件。那这是什么意思呢？网上的各位大牛们讲事件委托基本上都用了同一个例子，就是取快递来解释这个现象，我仔细揣摩了一下，这个例子还真是恰当，我就不去想别的例子来解释了，借花献佛，我摘过来，大家认真领会一下事件委托到底是一个什么原理：</p>
<p>有三个同事预计会在周一收到快递。为签收快递，有两种办法：一是三个人在公司门口等快递；二是委托给前台MM代为签收。现实当中，我们大都采用委托的方案（公司也不会容忍那么多员工站在门口就为了等快递）。前台MM收到快递后，她会判断收件人是谁，然后按照收件人的要求签收，甚至代为付款。这种方案还有一个优势，那就是即使公司里来了新员工（不管多少），前台MM也会在收到寄给新员工的快递后核实并代为签收。</p>
<p>这里其实还有2层意思的：</p>
<p>第一，现在委托前台的同事是可以代为签收的，即程序中的现有的dom节点是有事件的；</p>
<p>第二，新员工也是可以被前台MM代为签收的，即程序中新添加的dom节点也是有事件的。</p>
<p>为什么要用事件委托：</p>
<p>一般来说，dom需要有事件处理程序，我们都会直接给它设事件处理程序就好了，那如果是很多的dom需要添加事件处理呢？比如我们有100个li，每个li都有相同的click点击事件，可能我们会用for循环的方法，来遍历所有的li，然后给它们添加事件，那这么做会存在什么影响呢？</p>
<p>在JavaScript中，添加到页面上的事件处理程序数量将直接关系到页面的整体运行性能，因为需要不断的与dom节点进行交互，访问dom的次数越多，引起浏览器重绘与重排的次数也就越多，就会延长整个页面的交互就绪时间，这就是为什么性能优化的主要思想之一就是减少DOM操作的原因；如果要用事件委托，就会将所有的操作放到js程序里面，与dom的操作就只需要交互一次，这样就能大大的减少与dom的交互次数，提高性能；</p>
<p>每个函数都是一个对象，是对象就会占用内存，对象越多，内存占用率就越大，自然性能就越差了（内存不够用，是硬伤，哈哈），比如上面的100个li，就要占用100个内存空间，如果是1000个，10000个呢，那只能说呵呵了，如果用事件委托，那么我们就可以只对它的父级（如果只有一个父级）这一个对象进行操作，这样我们就需要一个内存空间就够了，是不是省了很多，自然性能就会更好。</p>
<p><strong>事件委托的原理：</strong></p>
<p>事件委托是利用事件的冒泡原理来实现的，何为事件冒泡呢？就是事件从最深的节点开始，然后逐步向上传播事件，举个例子：页面上有这么一个节点树，div>ul>li>a;比如给最里面的a加一个click点击事件，那么这个事件就会一层一层的往外执行，执行顺序a>li>ul>div，有这样一个机制，那么我们给最外面的div加点击事件，那么里面的ul，li，a做点击事件的时候，都会冒泡到最外层的div上，所以都会触发，这就是事件委托，委托它们父级代为执行事件。</p>
<p><strong>事件委托怎么实现：</strong></p>
<p>终于到了本文的核心部分了，哈哈，在介绍事件委托的方法之前，我们先来看一段一般方法的例子：</p>
<p>子节点实现相同的功能：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><ul id=<span class="hljs-string">"ul1"</span>>
    <li>111</li>
    <li>222</li>
    <li>333</li>
    <li>444</li>
</ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现功能是点击li，弹出123：</p>
<pre><code class="hljs language-bash copyable" lang="bash">window.onload = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
    var oUl = document.getElementById(<span class="hljs-string">"ul1"</span>);
    var aLi = oUl.getElementsByTagName(<span class="hljs-string">'li'</span>);
    <span class="hljs-keyword">for</span>(var i=0;i<aLi.length;i++)&#123;
        aLi[i].onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
            alert(123);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码的意思很简单，相信很多人都是这么实现的，我们看看有多少次的dom操作，首先要找到ul，然后遍历li，然后点击li的时候，又要找一次目标的li的位置，才能执行最后的操作，每次点击都要找一次li；</p>
<p>那么我们用事件委托的方式做又会怎么样呢？</p>
<pre><code class="hljs language-bash copyable" lang="bash">window.onload = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
    var oUl = document.getElementById(<span class="hljs-string">"ul1"</span>);
   oUl.onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
        alert(123);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里用父级ul做事件处理，当li被点击时，由于冒泡原理，事件就会冒泡到ul上，因为ul上有点击事件，所以事件就会触发，当然，这里当点击ul的时候，也是会触发的，那么问题就来了，如果我想让事件代理的效果跟直接给节点的事件效果一样怎么办，比如说只有点击li才会触发，不怕，我们有绝招：</p>
<p>Event对象提供了一个属性叫target，可以返回事件的目标节点，我们成为事件源，也就是说，target就可以表示为当前的事件操作的dom，但是不是真正操作dom，当然，这个是有兼容性的，标准浏览器用ev.target，IE浏览器用event.srcElement，此时只是获取了当前节点的位置，并不知道是什么节点名称，这里我们用nodeName来获取具体是什么标签名，这个返回的是一个大写的，我们需要转成小写再做比较（习惯问题）：</p>
<pre><code class="hljs language-bash copyable" lang="bash">window.onload = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
　　var oUl = document.getElementById(<span class="hljs-string">"ul1"</span>);
　　oUl.onclick = <span class="hljs-keyword">function</span>(ev)&#123;
　　　　var ev = ev || window.event;
　　　　var target = ev.target || ev.srcElement;
　　　　<span class="hljs-keyword">if</span>(target.nodeName.toLowerCase() == <span class="hljs-string">'li'</span>)&#123;
　 　　　　　　 alert(123);
　　　　　　　  alert(target.innerHTML);
　　　　&#125;
　　&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样改下就只有点击li会触发事件了，且每次只执行一次dom操作，如果li数量很多的话，将大大减少dom的操作，优化的性能可想而知！</p>
<p>上面的例子是说li操作的是同样的效果，要是每个li被点击的效果都不一样，那么用事件委托还有用吗？</p>
<pre><code class="hljs language-bash copyable" lang="bash"><div id=<span class="hljs-string">"box"</span>>
        <input <span class="hljs-built_in">type</span>=<span class="hljs-string">"button"</span> id=<span class="hljs-string">"add"</span> value=<span class="hljs-string">"添加"</span> />
        <input <span class="hljs-built_in">type</span>=<span class="hljs-string">"button"</span> id=<span class="hljs-string">"remove"</span> value=<span class="hljs-string">"删除"</span> />
        <input <span class="hljs-built_in">type</span>=<span class="hljs-string">"button"</span> id=<span class="hljs-string">"move"</span> value=<span class="hljs-string">"移动"</span> />
        <input <span class="hljs-built_in">type</span>=<span class="hljs-string">"button"</span> id=<span class="hljs-string">"select"</span> value=<span class="hljs-string">"选择"</span> />
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">window.onload = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
            var Add = document.getElementById(<span class="hljs-string">"add"</span>);
            var Remove = document.getElementById(<span class="hljs-string">"remove"</span>);
            var Move = document.getElementById(<span class="hljs-string">"move"</span>);
            var Select = document.getElementById(<span class="hljs-string">"select"</span>);
            
            Add.onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                alert(<span class="hljs-string">'添加'</span>);
            &#125;;
            Remove.onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                alert(<span class="hljs-string">'删除'</span>);
            &#125;;
            Move.onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                alert(<span class="hljs-string">'移动'</span>);
            &#125;;
            Select.onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                alert(<span class="hljs-string">'选择'</span>);
            &#125;
            
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面实现的效果我就不多说了，很简单，4个按钮，点击每一个做不同的操作，那么至少需要4次dom操作，如果用事件委托，能进行优化吗？</p>
<pre><code class="hljs language-bash copyable" lang="bash">window.onload = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
            var oBox = document.getElementById(<span class="hljs-string">"box"</span>);
            oBox.onclick = <span class="hljs-keyword">function</span> (ev) &#123;
                var ev = ev || window.event;
                var target = ev.target || ev.srcElement;
                <span class="hljs-keyword">if</span>(target.nodeName.toLocaleLowerCase() == <span class="hljs-string">'input'</span>)&#123;
                    switch(target.id)&#123;
                        <span class="hljs-keyword">case</span> <span class="hljs-string">'add'</span> :
                            alert(<span class="hljs-string">'添加'</span>);
                            <span class="hljs-built_in">break</span>;
                        <span class="hljs-keyword">case</span> <span class="hljs-string">'remove'</span> :
                            alert(<span class="hljs-string">'删除'</span>);
                            <span class="hljs-built_in">break</span>;
                        <span class="hljs-keyword">case</span> <span class="hljs-string">'move'</span> :
                            alert(<span class="hljs-string">'移动'</span>);
                            <span class="hljs-built_in">break</span>;
                        <span class="hljs-keyword">case</span> <span class="hljs-string">'select'</span> :
                            alert(<span class="hljs-string">'选择'</span>);
                            <span class="hljs-built_in">break</span>;
                    &#125;
                &#125;
            &#125;
            
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用事件委托就可以只用一次dom操作就能完成所有的效果，比上面的性能肯定是要好一些的
现在讲的都是document加载完成的现有dom节点下的操作，那么如果是新增的节点，新增的节点会有事件吗？也就是说，一个新员工来了，他能收到快递吗？
看一下正常的添加节点的方法：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><input <span class="hljs-built_in">type</span>=<span class="hljs-string">"button"</span> name=<span class="hljs-string">""</span> id=<span class="hljs-string">"btn"</span> value=<span class="hljs-string">"添加"</span> />
    <ul id=<span class="hljs-string">"ul1"</span>>
        <li>111</li>
        <li>222</li>
        <li>333</li>
        <li>444</li>
    </ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在是移入li，li变红，移出li，li变白，这么一个效果，然后点击按钮，可以向ul中添加一个li子节点</p>
<pre><code class="hljs language-bash copyable" lang="bash">window.onload = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
            var oBtn = document.getElementById(<span class="hljs-string">"btn"</span>);
            var oUl = document.getElementById(<span class="hljs-string">"ul1"</span>);
            var aLi = oUl.getElementsByTagName(<span class="hljs-string">'li'</span>);
            var num = 4;
            
            //鼠标移入变红，移出变白
            <span class="hljs-keyword">for</span>(var i=0; i<aLi.length;i++)&#123;
                aLi[i].onmouseover = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                    this.style.background = <span class="hljs-string">'red'</span>;
                &#125;;
                aLi[i].onmouseout = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                    this.style.background = <span class="hljs-string">'#fff'</span>;
                &#125;
            &#125;
            //添加新节点
            oBtn.onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                num++;
                var oLi = document.createElement(<span class="hljs-string">'li'</span>);
                oLi.innerHTML = 111*num;
                oUl.appendChild(oLi);
            &#125;;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一般的做法，但是你会发现，新增的li是没有事件的，说明添加子节点的时候，事件没有一起添加进去，这不是我们想要的结果，那怎么做呢？一般的解决方案会是这样，将for循环用一个函数包起来，命名为mHover，如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">window.onload = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
            var oBtn = document.getElementById(<span class="hljs-string">"btn"</span>);
            var oUl = document.getElementById(<span class="hljs-string">"ul1"</span>);
            var aLi = oUl.getElementsByTagName(<span class="hljs-string">'li'</span>);
            var num = 4;
            
            <span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">mHover</span></span> () &#123;
                //鼠标移入变红，移出变白
                <span class="hljs-keyword">for</span>(var i=0; i<aLi.length;i++)&#123;
                    aLi[i].onmouseover = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                        this.style.background = <span class="hljs-string">'red'</span>;
                    &#125;;
                    aLi[i].onmouseout = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                        this.style.background = <span class="hljs-string">'#fff'</span>;
                    &#125;
                &#125;
            &#125;
            mHover ();
            //添加新节点
            oBtn.onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                num++;
                var oLi = document.createElement(<span class="hljs-string">'li'</span>);
                oLi.innerHTML = 111*num;
                oUl.appendChild(oLi);
                mHover ();
            &#125;;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然功能实现了，看着还挺好，但实际上无疑是又增加了一个dom操作，在优化性能方面是不可取的，那么有事件委托的方式，能做到优化吗？</p>
<pre><code class="hljs language-bash copyable" lang="bash">window.onload = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
            var oBtn = document.getElementById(<span class="hljs-string">"btn"</span>);
            var oUl = document.getElementById(<span class="hljs-string">"ul1"</span>);
            var aLi = oUl.getElementsByTagName(<span class="hljs-string">'li'</span>);
            var num = 4;
            
            //事件委托，添加的子元素也有事件
            oUl.onmouseover = <span class="hljs-keyword">function</span>(ev)&#123;
                var ev = ev || window.event;
                var target = ev.target || ev.srcElement;
                <span class="hljs-keyword">if</span>(target.nodeName.toLowerCase() == <span class="hljs-string">'li'</span>)&#123;
                    target.style.background = <span class="hljs-string">"red"</span>;
                &#125;
                
            &#125;;
            oUl.onmouseout = <span class="hljs-keyword">function</span>(ev)&#123;
                var ev = ev || window.event;
                var target = ev.target || ev.srcElement;
                <span class="hljs-keyword">if</span>(target.nodeName.toLowerCase() == <span class="hljs-string">'li'</span>)&#123;
                    target.style.background = <span class="hljs-string">"#fff"</span>;
                &#125;
                
            &#125;;
            
            //添加新节点
            oBtn.onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>()&#123;
                num++;
                var oLi = document.createElement(<span class="hljs-string">'li'</span>);
                oLi.innerHTML = 111*num;
                oUl.appendChild(oLi);
            &#125;;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看，上面是用事件委托的方式，新添加的子元素是带有事件效果的，我们可以发现，当用事件委托的时候，根本就不需要去遍历元素的子节点，只需要给父级元素添加事件就好了，其他的都是在js里面的执行，这样可以大大的减少dom操作，这才是事件委托的精髓所在。</p>
<p>现在给一个场景 ul > li > div > p，div占满li，p占满div，还是给ul绑定事件，需要判断点击的是不是li（假设li里面的结构是不固定的），那么e.target就可能是p，也有可能是div，这种情况你会怎么处理呢？</p>
<pre><code class="hljs language-bash copyable" lang="bash">　　<ul id=<span class="hljs-string">"test"</span>>
    <li>
        <p>11111111111</p>
    </li>
    <li>
        <div>
            22222222
        </div>
    </li>
    <li>
        <span>3333333333</span>
    </li>
    <li>4444444</li>
</ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上列表，有4个li，里面的内容各不相同，点击li，event对象肯定是当前点击的对象，怎么指定到li上，下面我直接给解决方案：</p>
<pre><code class="hljs language-bash copyable" lang="bash">　var oUl = document.getElementById(<span class="hljs-string">'test'</span>);
oUl.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-keyword">function</span>(ev)&#123;
    var target = ev.target;
    <span class="hljs-keyword">while</span>(target !== oUl )&#123;
        <span class="hljs-keyword">if</span>(target.tagName.toLowerCase() == <span class="hljs-string">'li'</span>)&#123;
            console.log(<span class="hljs-string">'li click~'</span>);
            <span class="hljs-built_in">break</span>;
        &#125;
        target = target.parentNode;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>核心代码是while循环部分，实际上就是一个递归调用，你也可以写成一个函数，用递归的方法来调用，同时用到冒泡的原理，从里往外冒泡，知道currentTarget为止，当当前的target是li的时候，就可以执行对应的事件了，然后终止循环，恩，没毛病！</p>
<p><strong>总结：</strong></p>
<p>那什么样的事件可以用事件委托，什么样的事件不可以用呢？</p>
<p>适合用事件委托的事件：click，mousedown，mouseup，keydown，keyup，keypress。</p>
<p>值得注意的是，mouseover和mouseout虽然也有事件冒泡，但是处理它们的时候需要特别的注意，因为需要经常计算它们的位置，处理起来不太容易。</p>
<p>不适合的就有很多了，举个例子，mousemove，每次都要计算它的位置，非常不好把控，在不如说focus，blur之类的，本身就没用冒泡的特性，自然就不能用事件委托了。</p>
<p>好了，今天就到这里，下次我想介绍一下事件绑定，欢迎大家关注和阅读，以上纯属个人见解，如有不对的地方，万望指正，不胜感谢！
<strong>转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fliugang-vip%2Fp%2F5616484.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/liugang-vip/p/5616484.html" ref="nofollow noopener noreferrer">www.cnblogs.com/liugang-vip…</a></strong></p></div>  
</div>
            