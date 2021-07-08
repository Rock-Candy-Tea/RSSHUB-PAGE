
---
title: 'Javascript执行机制 - 宏任务与微任务、事件循环(Event Loop)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89c81a96556b4d78b5006a43f4ee7e5d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 02:06:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89c81a96556b4d78b5006a43f4ee7e5d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概括</h2>
<p>我们常说 <code>Javascript</code> （下面简称<code>JS</code>）是一门单线程编程语言，而单线程就意味着同一时刻只允许一个代码段在主线程上执行，那么对于执行一些需要长时间等待的任务来说，它们会占据线程不放，这会造成后续代码无法执行，程序无法正常使用。这是单线程的弊端，而 <code>JS</code> 是通过事件循环机制（<code>Event Loop</code>）来解决这一弊端。</p>
<blockquote>
<p><code>HTML5</code> 标准中提出的新技术 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWeb_Workers_API%2FUsing_web_workers" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Web_Workers_API/Using_web_workers" ref="nofollow noopener noreferrer">WebWork</a> 概念，它用来实现 “多线程” 技术，但这其实也是单线程模拟出来的，<code>JS</code> 单线程这一核心仍未改变，这点需要注意下噢。</p>
</blockquote>
<p>要理解清楚事件循环这个机制会涉及很多让人头疼的概念，如 <code>JS</code> 的执行机制、调用栈（执行栈）、任务队列（消息队列）、宏任务与微任务。当然，认识完这些东西，你对 <code>JS</code> 将会有更深层的认识，话不多说，我们开始本篇的愉快旅程吧。</p>
<h2 data-id="heading-1">栈、堆、队列</h2>
<p>在讲正题之前，我们先来了解一下三个数据结构类型，相信很多人也不是很陌生了，之所以讲这个，是因为下面可能会涉及这其中的概念，希望你能有个更好的认识。</p>
<ul>
<li>栈（Stack）：栈是一种特殊的列表，栈内的元素只能通过列表的一端访问，这一端称为栈顶。栈被称为是一种后入先出（LIFO，last-in-first-out）的数据结构。由于栈具有后入先出的特点，所以任何不在栈顶的元素都无法访问。为了得到栈底的元素，必须先拿掉上面的元素。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89c81a96556b4d78b5006a43f4ee7e5d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>队列（Queue）：栈数据结构的访问规则是LIFO(后进先出)，而队列数据结构的访问规则是FIFO(Fist-In-First-Out,先进先出)。队列在列表的末端添加项，从列表的前端移除项。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4173d61e89934909a49605cb350c56d1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>堆（Heap）：堆是一种经过排序的树形数据结构，每个结点都有一个值。通常我们所说的堆的数据结构，是指二叉堆。堆的特点是根结点的值最小（或最大），且根结点的两个子树也是一个堆。由于堆的这个特性，常用来实现优先队列，堆的存取是随意，这就如同我们在图书馆的书架上取书，虽然书的摆放是有顺序的，但是我们想取任意一本时不必像栈一样，先取出前面所有的书，我们只需要关心书的名字。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69483bda1b2c449698f9e33b9ffc090c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>其实感觉整那么多概念也没啥用，记不住(T＿T)。对于这三个数据结构，它们很重要，这点很明确，但要怎么记住它们呢？我是记住它的性质再结合例子记忆：</p>
<ul>
<li>栈：先进后出 or 后进先出。像子弹夹，先压入弹夹的子弹，最后才射出。</li>
<li>队列：先进先出 or 后进后出。像超市排队结算，先排队的人结算完肯定先走了。</li>
<li>堆：顺序排放，随意取用。像书架排列的书，我们按字母或者分类排放好，但取书的时候只要知道书名就能直接找到这本书了。</li>
</ul>
</blockquote>
<h2 data-id="heading-2">JS执行机制</h2>
<p>我们知道 <code>JS</code> 的执行顺序是从上到下一行一行顺序执行的，但是如果在执行过程中碰到耗时比较长的任务要怎么办呢？ <code>JS</code> 就只能傻等了吗？ 当然没那么傻了，聪明的程序猿把任务分成了同步任务和异步任务，避免了单线程的 <code>JS</code> 在执行过程被阻塞的问题，下面我画了个草图来描述这一执行过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/024e126b007f4846a4a85881144ca8ba~tplv-k3u1fbpfcp-watermark.image" alt="JS执行机制.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>图解：</strong></p>
<ul>
<li>
<p><code>JS</code> 在开始执行的时候，会把任务分为同步任务和异步任务。</p>
<blockquote>
<p>任务： 一个任务就是由执行诸如从头执行的一段程序、或执行一个事件回调或一个 <code>interval/timeout</code> 被触发之类的标准机制而被调度的任意 <code>JavaScript</code> 代码。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTML_DOM_API%2FMicrotask_guide" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTML_DOM_API/Microtask_guide" ref="nofollow noopener noreferrer">详细解释</a></p>
</blockquote>
<blockquote>
<p>同步任务：在主线程上排列执行的任务。只有前一个任务执行完毕，才能执行后一个任务。</p>
</blockquote>
<blockquote>
<p>异步任务：不进入主线程，而进入 “<code>任务队列</code>” 的任务。只有任务队列通知主线程，某个异步任务有结果了，可以执行了，该任务才会进入主线程执行。</p>
</blockquote>
</li>
<li>
<p>同步任务会直接进入主线程依次执行。</p>
</li>
<li>
<p>异步任务会进入到 “任务队列” 中，等待异步任务有了结果后，会将注册的回调函数放入任务队列中等待，当主线程空闲的时候（执行栈被清空），会被读取到执行栈等待主线程的执行。</p>
</li>
<li>
<p>异步任务可以再分为宏任务和微任务。</p>
</li>
</ul>
<h3 data-id="heading-3">宏任务与微任务</h3>
<p><code>JS</code> 把异步任务再分为宏任务和微任务。那么，它们俩又是什么呢？</p>
<ul>
<li>宏任务（Macrotask）：可以理解为每次执行栈执行的代码就是一个宏任务。（包括每次从事件队列中获取一个事件回调并放到执行栈中执行）。</li>
<li>微任务（Microtask）：可以理解为当前宏任务执行结束后立即执行的任务。也就是说，在当前宏任务后，下一个宏任务之前。微任务是在运行宏任务/同步任务的时候产生的，是属于当前任务的。</li>
</ul>
<p><strong>为什么会产生宏任务和微任务呢？<br></strong>
前面我们说过，异步任务会进入所谓的 “任务队列” 中了，而任务队列具有 <strong>队列</strong> 的性质，先进先出，也就是后加入的任务必须等待前面的任务执行完才能执行。如果在执行的过程中突然有重要的数据需要获取，或是说有事件突然需要处理一下，按照队列的先进先出顺序这些是无法得到及时处理的。这个时候就催生了宏任务和微任务，微任务使得一些异步任务得到及时的处理。</p>
<p><strong>举个例子形容宏任务和微任务？<br></strong>
曾经看到的一个例子很好，宏任务和微任务形象的来说就是：你去营业厅办一个业务会有一个排队号码，当叫到你的号码的时候你去窗口办充值业务(宏任务执行)，在你办理充值的时候你又想改个套餐(微任务)，这个时候工作人员会直接帮你办，不可能让你重新排队。<a href="https://juejin.cn/post/6844904106121936903" target="_blank" title="https://juejin.cn/post/6844904106121936903">例子来源</a></p>
<p><strong>产生宏任务和微任务分别有哪些？<br></strong></p>
<ul>
<li>
<p>宏任务：</p>
<ol>
<li><code>script</code>（整体的代码）</li>
<li><code>setTimeout</code></li>
<li><code>setInterval</code></li>
<li><code>I/O 操作</code></li>
<li><code>UI渲染</code></li>
<li><code>setImmediate</code> （Node.js 环境）</li>
</ol>
</li>
<li>
<p>微任务：</p>
<ol>
<li><code>Promise.then</code></li>
<li><code> Mutation Observer API</code> （<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMutationObserver%2FMutationObserver" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver/MutationObserver" ref="nofollow noopener noreferrer">具体使用</a>）</li>
<li><code>Process.nextTick</code>（Node独有）</li>
<li><code>Object.observe</code> （废弃）</li>
</ol>
</li>
</ul>
<p><strong>微任务与任务的区别？</strong></p>
<ol>
<li>
<p>首先，每当一个任务存在，事件循环都会检查该任务是否正把控制权交给其他 JavaScript 代码。如若不然，事件循环就会运行微任务队列中的所有微任务。接下来微任务循环会在事件循环的每次迭代中被处理多次，包括处理完事件和其他回调之后。</p>
</li>
<li>
<p>其次，如果一个微任务通过调用  <code>queueMicrotask()</code>, 向队列中加入了更多的微任务，则那些新加入的微任务 会早于下一个任务运行 。这是因为事件循环会持续调用微任务直至队列中没有留存的，即使是在有更多微任务持续被加入的情况下。</p>
</li>
</ol>
<blockquote>
<p>注意： 因为微任务自身可以入列更多的微任务，且事件循环会持续处理微任务直至队列为空，那么就存在一种使得事件循环无尽处理微任务的真实风险。如何处理递归增加微任务是要谨慎而行的。</p>
</blockquote>
<h3 data-id="heading-4">事件循环</h3>
<p>了解了 <code>JS</code> 的整个执行机制过程后，事件循环（<code>Event Loop</code>）就比较简单好理解了，开头我们提过它的出现是为了解决 <code>JS</code> 单线程带来的弊端，它也是整个 <code>JS</code> 单线程执行过程中最核心的一部分，也是最重要的一部分。</p>
<p>讲事件循环前，还要涉及一个 <strong>执行栈（也称调用栈）</strong> 的概念。它又是什么呢？网上的说法是，所有同步任务都在主线程上执行，形成一个执行栈。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2013%2F11%2Fstack.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2013/11/stack.html" ref="nofollow noopener noreferrer">详细解释</a></p>
<blockquote>
<p>你也可以简单理解为，它就是主线程上执行 <code>JS</code> 代码的地方，像 <code>console.log(1)</code> 这句代码在执行栈里执行后，控制台就能输出 1 。当然，从它的名字 <strong>执行栈</strong> 我们要清楚它具有 <strong>栈</strong> 先进后出的特点哦。</p>
</blockquote>
<p>还是一样，我们先上图再分析：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4058f6e9c5a944f887348359ab7c035e~tplv-k3u1fbpfcp-watermark.image" alt="JS事件循环.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>所有同步任务都在主线程上执行，形成一个执行栈。</li>
<li>主线程之外，还存在一个 “任务队列”，它是存放异步任务运行后的回调函数的，也就是异步任务有了运行结果，就在"任务队列"之中放置一个事件。</li>
<li>一旦 “执行栈” 中的所有同步任务执行完毕，主线程就会读取 “任务队列”，看看里面有哪些事件。然后把那些对应的异步任务，压入执行栈中，开始执行。</li>
</ol>
<p>而主线程不断重复上面的第三步，就形成了我们常说的事件循环了。</p>
<blockquote>
<p>我记忆的概念：主线程从任务队列中读取异步任务执行，不断循环重复的过程，就称为事件循环。</p>
</blockquote>
<h2 data-id="heading-5">举个栗子</h2>
<p>讲了那么多，举个栗子最实在，下面我们就来细细分析一下。</p>
<pre><code class="copyable">var p = new Promise((resolve, reject) => &#123;
    console.log('Promise - 初始化');
    resolve('Promise - 结果')
&#125;)

function fn1() &#123;
    console.log('fn1 - 执行');
&#125;

function fn2() &#123;
    console.log('fn2 - 开始执行');
    setTimeout(() => &#123;
        console.log('setTimeout - 执行');
    &#125;)
    fn1();
    console.log('fn2 - 再次执行');
    p.then(res => &#123;
        console.log('Promise - 第一个then ：' + res);
    &#125;).then(() => &#123;
        console.log('Promise - 第二个then');
    &#125;)
&#125;

fn2();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>首先，从上到下依次执行，先是会把 <code>Promise()</code> 对象压入 <code>执行栈</code> 中执行，输出 <strong>“Promise - 初始化”</strong> 并给 <code>p</code> 赋值了一个 <code>Promise</code> 对象，之后 <code>执行栈</code> 把 <code>Promise()</code> 对象弹出，也就是 <code>执行栈</code> 清空了。</li>
<li>继续往下，不管两个函数的声明，来到 <code>fn2()</code> 的调用，把 <code>fn2()</code> 压入栈中执行，输出 <strong>“fn2 - 开始执行”</strong>，继续把 <code>setTimeout()</code>压入栈中执行，会把它里面的 <code>console.log('setTimeout - 执行');</code> 语句放入 <code>任务队列</code>中，弹出 <code>setTimeout()</code>，<code>执行栈</code> 中 <code>fn2()</code> 继续调用。</li>
<li>往下，来到 <code>fn1()</code> 的调用，把 <code>fn1()</code> 压入栈中执行，输出 <strong>“fn1 - 执行”</strong>，弹出 <code>fn1()</code>，往下，再次打印输出 <strong>“fn2 - 再次执行”</strong>。</li>
<li>往下，来到第一个 <code>.then()</code>，把它压入栈中执行，会把它里面的 <code>console.log('Promise - 第一个then ：' + res);</code> 语句放入 <code>微任务队列</code> 中，弹出它，再压入第二个 <code>.then()</code> ，继续把 <code>console.log('Promise - 第二个then');</code> 语句放入 <code>微任务队列</code> 中， 弹出它。</li>
<li>到这里， <code>fn2()</code> 就执行完了，会被 <code>执行栈</code> 弹出，栈内又清空了。</li>
<li>同步任务都执行完了，主线程空闲了，开始读取 <code>微任务队列</code>，按照队列先进先出的性质，会先把 <code>console.log('Promise - 第一个then ：' + res);</code> 语句压入 <code>执行栈</code> 中执行，输出 <strong>“Promise - 第一个then ：Promise - 结果”</strong> ，然后弹出，再压入另一语句，输出 <strong>“Promise - 第二个then”</strong> 弹出。</li>
<li><code>执行栈</code> 又清空了，开始读取 <code>任务队列</code>，把 <code>console.log('setTimeout - 执行');</code> 语句压入栈中执行，输出 <strong>“setTimeout - 执行”</strong>，然后弹出。</li>
</ol>
<p>这就是整个执行过程了，文字有点多和乱，但仔细看应该能瞧明白的(-^〇^-) ，步骤中加黑文字对应下图的输出。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/514758f9ffe14ba0b1fdc6515d4e7bed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这上面的例子应该还比较好理解，但它还不是很能体现 <code>Event Loop</code> 的精髓，我们再来改造改造。</p>
<pre><code class="copyable">...
function fn2() &#123;
    console.log('fn2 - 开始执行');
    setTimeout(() => &#123;
        console.log('setTimeout - 执行');
        // start
        setTimeout(() => &#123;
            console.log('又一个宏任务')
        &#125;)
        p.then(() => &#123;
            console.log('Promise - 第三个then')
        &#125;)
        // end
    &#125;)
    fn1();
    console.log('fn2 - 再次执行');
    p.then(res => &#123;
        console.log('Promise - 第一个then ：' + res);
    &#125;).then(() => &#123;
        console.log('Promise - 第二个then')
    &#125;)
&#125;

fn2();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码我们在一个宏任务中再增加了一个宏任务和一个微任务，然后我们直接来看输出结果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e413b24462b5424082a48180d251b91a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是否符合你的预期呢？这里其实有个容易踩坑的点，既然 <code>.then()</code> 是一个微任务，我们新加的微任务，为什么它没有在上面提到的第 <strong>6</strong> 步骤中读取 <code>微任务队列</code> 的时候一起执行呢？原因很简单，就是下面红框的宏任务还没有执行。我们应该把它们看成一个整体，它们还没有细化。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b50e843b5b6c42968f1179a779dce3c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之所以来细说这个点，主要是想表明，执行一个宏任务可能会继续产生宏任务和微任务，然后主线程来继续读取 <code>微任务队列</code> 和 <code>任务队列</code>，以此来构成 <code>Event Loop</code> 的过程。</p>
<p><br><br>
至此，本篇文章就写完啦，撒花撒花。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2198fba2b674f1b935a63e4abb3cbd7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>希望本文对你有所帮助，如有任何疑问，期待你的留言哦。<br>
老样子，点赞+评论=你会了，收藏=你精通了。</p></div>  
</div>
            