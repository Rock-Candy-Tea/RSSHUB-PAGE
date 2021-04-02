
---
title: 'iOS autoreleasePool原理总结'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9744af04230946b7a705077d9e7ce51f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 09 Mar 2021 19:17:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9744af04230946b7a705077d9e7ce51f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">目录</h1>
<p><strong>1. autorelease的本质</strong></p>
<p><strong>2. autoreleasepool的源码解析</strong></p>
<p><strong>3. autoreleasePoolPage的结构</strong></p>
<p><strong>4. autoreleasePool的结构和工作原理</strong></p>
<p><strong>5.autoreleasepool的嵌套</strong></p>
<p><strong>6. autorelaeasepool、NSRunLoop 、子线程三者的关系</strong></p>
<hr>
<h3 data-id="heading-1">1.autorelease的本质</h3>
<ul>
<li>autorelease本质就是延迟调用release方法</li>
</ul>
<p>MRC环境下，通过[obj autorelease]来延迟内存的释放
ARC环境下，是不能手动调用，系统会自动给对象添加autorelease</p>
<h3 data-id="heading-2">2.autoreleasepool的源码解析</h3>
<p>进入工程main.m文件中</p>
<pre><code class="hljs language-swift copyable" lang="swift">int main(int argc, char <span class="hljs-operator">*</span> argv[]) &#123;
    <span class="hljs-meta">@autoreleasepool</span> &#123;
        <span class="hljs-comment">///ARC下会自动加入 autorelease方法</span>
        <span class="hljs-type">NSObject</span> <span class="hljs-operator">*</span> obj <span class="hljs-operator">=</span> [[<span class="hljs-type">NSObject</span> alloc] <span class="hljs-keyword">init</span>];
        <span class="hljs-comment">///MRC写法</span>
        <span class="hljs-comment">// NSObject * obj = [[[NSObject alloc] init] autorelease];</span>
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入终端,cd到main.m文件目录下，运行以下命令，将文件转换为main.cpp文件查看底层调用方法：
<code>xcrun -sdk iphoneos clang -arch arm64 -rewrite-objc main.m -o main.cpp </code>
在生成的main.cpp文件中我们可发现main函数被转化成下面C代码：</p>
<pre><code class="hljs language-swift copyable" lang="swift">int main(int argc, char <span class="hljs-operator">*</span> argv[]) &#123;
    <span class="hljs-comment">/* @autoreleasepool */</span> &#123; __AtAutoreleasePool __autoreleasepool; <span class="hljs-comment">///调用了objc_autoreleasePoolPush</span>
        <span class="hljs-type">NSObject</span> <span class="hljs-operator">*</span> obj <span class="hljs-operator">=</span> ((<span class="hljs-type">NSObject</span> <span class="hljs-operator">*</span>(<span class="hljs-operator">*</span>)(id, <span class="hljs-type">SEL</span>))(void <span class="hljs-operator">*</span>)objc_msgSend)((id)((<span class="hljs-type">NSObject</span> <span class="hljs-operator">*</span>(<span class="hljs-operator">*</span>)(id, <span class="hljs-type">SEL</span>))(void <span class="hljs-operator">*</span>)objc_msgSend)((id)objc_getClass(<span class="hljs-string">"NSObject"</span>), sel_registerName(<span class="hljs-string">"alloc"</span>)), sel_registerName(<span class="hljs-string">"init"</span>));
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看__AtAutoreleasePool发现是一个C的结构体</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">__AtAutoreleasePool</span> </span>&#123;
  __AtAutoreleasePool() &#123;atautoreleasepoolobj <span class="hljs-operator">=</span> objc_autoreleasePoolPush();&#125;
  <span class="hljs-operator">~</span>__AtAutoreleasePool() &#123;objc_autoreleasePoolPop(atautoreleasepoolobj);&#125;
  void <span class="hljs-operator">*</span> atautoreleasepoolobj;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里面主要包含了两个方法:</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-number">1</span>. __AtAutoreleasePool() &#123; atautoreleasepoolobj <span class="hljs-operator">=</span> objc_autoreleasePoolPush(); &#125;:构造函数，在创建结构体时调用

<span class="hljs-number">2</span>. <span class="hljs-operator">~</span>__AtAutoreleasePool() &#123; objc_autoreleasePoolPop(atautoreleasepoolobj); &#125;:析构函数，在销毁结构体时调用
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>为了方便，将代码转换为以下伪代码：</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift">int main (int argc, char <span class="hljs-operator">*</span> argv[]) &#123;
<span class="hljs-comment">// push </span>
void <span class="hljs-operator">*</span>poolToken <span class="hljs-operator">=</span> objc_autoreleasePoolPush();
  这中间为写在&#123;<span class="hljs-operator">...</span>&#125;中的代码
<span class="hljs-comment">// pop 将&#123;...&#125;中的对象都执行一次 release操作  </span>
objc_autoreleasePoolPop(哨兵对象地址);<span class="hljs-comment">//哨兵对象后面会讲到</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>-上面提到objc_autoreleasePoolPush()和 objc_autoreleasePoolPop(atautoreleasepoolobj)两个方法，看看源码实现(只保留重要部分)：</p>
<pre><code class="copyable">void *
objc_autoreleasePoolPush(void)
&#123;
    return AutoreleasePoolPage::push();
&#125;

void
objc_autoreleasePoolPop(void *ctxt)
&#123;
    AutoreleasePoolPage::pop(ctxt);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此发现autoreleasePool是依赖AutoreleasePoolPage实现的，具体里面实现后面再说，先来看看AutoreleasePoolPage的结构。</p>
<hr>
<h3 data-id="heading-3">3.autoreleasePoolPage的结构</h3>
<p>以下为AutoreleasePoolPage结构的主要部分</p>
<pre><code class="copyable">class AutoreleasePoolPage 
&#123;
    PAGE_MAX_SIZE；//最大size 4096字节
    magic_t const magic; //用来校验AutoreleasePoolPage的结构是否完整
    id *next;//指向下一个即将产生的autoreleased对象的存放位置（当next == begin()时，表示AutoreleasePoolPage为空；当next == end()时，表示AutoreleasePoolPage已满
    pthread_t const thread;//指向当前线程，一个AutoreleasePoolPage只会对应一个线程，但一个线程可以对应多个AutoreleasePoolPage；
    AutoreleasePoolPage * const parent;//指向父结点，第一个结点的 parent 值为 nil；
    AutoreleasePoolPage *child;//指向子结点，最后一个结点的 child 值为 nil；
    uint32_t const depth;//代表深度，第一个page的depth为0，往后每递增一个page，depth会加1；
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图：
<img alt="AutoreleasePoolPage结构图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9744af04230946b7a705077d9e7ce51f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>1.AutoreleasePoolPage 本质是这么一个节点对象，大小是4096字（PAGE_MAX_SIZE：4096）。</li>
<li>2.前7个变量都是8字节，剩下的4040字节存储着autorelease对象地址</li>
<li>4.push的调用分析</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift">void <span class="hljs-operator">*</span>
objc_autoreleasePoolPush(void)
&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-type">AutoreleasePoolPage</span>::push();
&#125;

<span class="hljs-keyword">static</span> inline void <span class="hljs-operator">*</span>push()
&#123;
    <span class="hljs-keyword">return</span> autoreleaseFast(<span class="hljs-type">POOL_BOUNDARY</span>);
&#125;

<span class="hljs-keyword">static</span> inline id <span class="hljs-operator">*</span>autoreleaseFast(id obj)
&#123;
   <span class="hljs-comment">//hotPage()表示当前页的 AutoreleasePoolPage 节点</span>
    <span class="hljs-type">AutoreleasePoolPage</span> <span class="hljs-operator">*</span>page <span class="hljs-operator">=</span> hotPage(); 
    <span class="hljs-keyword">if</span> (page <span class="hljs-operator">&&</span> <span class="hljs-operator">!</span>page->full()) &#123;
     <span class="hljs-comment">// 当前 page 存在且没有满时，直接将对象添加到当前 page 中，即 next 指向的位置</span>
        <span class="hljs-keyword">return</span> page->add(obj); 
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (page) &#123; 
       <span class="hljs-comment">// 当前 page 存在且已满时，创建一个新的 page ，并将对象添加到新创建的 page 中</span>
        <span class="hljs-keyword">return</span> autoreleaseFullPage(obj, page); 
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 当前 page 不存在时，即还没有 page 时，创建第一个 page ，并将对象添加到新创建的 page 中</span>
        <span class="hljs-keyword">return</span> autoreleaseNoPage(obj); 
    &#125;
&#125;
[obj autorelease], 给对象添加 autorelease 方法, 其实内部就是直接调用了 autoreleaseFast
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-4">4.autoreleasePool的结构和工作原理</h3>
<ul>
<li>autoreleasepool本质上就是一个指针堆栈,内部结构是由若干个以AutoreleasePoolPage对象为结点的双向链表组成，系统会在需要的时候动态地增加或删除page节点，如下图即为AutoreleasePoolPage组成的双向链表：</li>
</ul>
<p><img alt="截屏2021-03-05 下午4.39.46.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a1a03eb48fb4dffa9b0ac98f2577493~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>参考上图，整个流程大概如下：</li>
</ul>
<p>1.在运行循环开始前，系统会自动创建一个autoreleasepool(一个autoreleasepool会存在多个AutoreleasePoolPage)，此时会调用一次objc_autoreleasePoolPush函数，runtime会向当前的AutoreleasePoolPage中add进一个POOL_BOUNDARY（哨兵对象），代表autoreleasepool的起始边界地址），并返回此哨兵对象的内存地址。</p>
<p>2.这时候next指针则会指向POOL_BOUNDARY（哨兵对象）后面的地址（对象地址1）。</p>
<p>3.后面我们创建对象，如果对象调用了autorelease方法（ARC编译器会给对象自动插入autorelease），则会被添加进AutoreleasePoolPage中，位置是在next指针指向的位置，如上面next指向的是对象地址1，这是后添加的对象地址就在对象地址1这里，然后next就会 指向到对象地址2 ，以此类推，每添加一个地址就会向前移动一次，直到指向end()表示已存满。</p>
<p>4.当不断的创建对象时，AutoreleasePoolPage不断存储对象地址，直到存满后，则又会创建一个新的AutoreleasePoolPage，使用child指针和parent指针指向下一个和上一个page，从而形成一个双向链表，对象地址存储的顺序如图所示。</p>
<p>5.当调用objc_autoreleasePoolPop(哨兵对象地址)时（调用时机后面说），假设我们如上图，添加最后一个对象地址8，那么这时候就会依次由对象地址8 -> 对象地址1，每个对象都会调用release方法释放，直到遇到哨兵对象地址为止。</p>
<hr>
<h3 data-id="heading-5">5.autoreleasepool的嵌套</h3>
<p>当多个autoreleasepool嵌套，对象的释放，会是什么情况呢？
每次新建一个@ autoreleasepool,就会执行一次push操作，对应的具体实现就是往AutoreleasePoolPage中的next位置插入一个POOL_BOUNDARY（哨兵对象）。
如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-meta">@autoreleasepool</span>   &#123;<span class="hljs-comment">//autoreleasepool1</span>
       <span class="hljs-type">NSObject</span> <span class="hljs-operator">*</span> obj1 <span class="hljs-operator">=</span> [[<span class="hljs-type">NSObject</span> alloc] <span class="hljs-keyword">init</span>];
   
    <span class="hljs-meta">@autoreleasepool</span>  &#123;<span class="hljs-comment">//autoreleasepool2</span>
        <span class="hljs-type">NSObject</span> <span class="hljs-operator">*</span> obj2 <span class="hljs-operator">=</span> [[<span class="hljs-type">NSObject</span> alloc] <span class="hljs-keyword">init</span>];
        <span class="hljs-type">NSObject</span> <span class="hljs-operator">*</span> obj3 <span class="hljs-operator">=</span> [[<span class="hljs-type">NSObject</span> alloc] <span class="hljs-keyword">init</span>];
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="autoreleasepool的嵌套.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0ec324f6a8d443cacc1798c7a1cae94~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>释放流程：</p>
<ol>
<li>
<p>当autoreleasepool1创建时，会添加哨兵对象1，接着obj1的创建，则把obj1地址添加进来。</p>
</li>
<li>
<p>当autoreleasepool2创建，会添加哨兵对象2，位置是obj1后面（上面next指针指向原理），然后依次把obj2和obj3加进来。</p>
</li>
<li>
<p>当autoreleasepool2结束时，obj3，obj2，会找到离它们最近的autoreleasepool即
autoreleasepool2，然后依次调用release，直到哨兵对象2位置。</p>
</li>
<li>
<p>当autoreleasepool1结束时，当obj1调用release，直到哨兵对象1位置，</p>
</li>
</ol>
<hr>
<h3 data-id="heading-6">6. autorelaeasepool、NSRunLoop 、子线程三者的关系</h3>
<ol>
<li>
<p>主线程默认为我们开启 Runloop，Runloop 会自动帮我们创建Autoreleasepool，并进行Push、Pop 等操作来进行内存管理。</p>
</li>
<li>
<p>子线程默认不开启runloop,当产生autorelease对象时候，会将对象添加到AutoreleasePoolPage中，也就是不手动创建Autoreleasepool也能正确释放对象，线程销毁时release对象</p>
</li>
<li>
<p>自定义的 NSOperation 和 NSThread 需要手动创建自动释放池。比如： 自定义的 NSOperation 类中的 main 方法里就必须添加自动释放池。否则出了作用域后，自动释放对象会因为没有自动释放池去处理它，而造成内存泄露。但对于 blockOperation 和 invocationOperation 这种默认的Operation ，系统已经帮我们封装好了，不需要手动创建自动释放池。</p>
</li>
<li>
<p>AutoreleasePool是按线程一一对应的(结构中的thread指针指向当前线程）,每开一个线程，会有与之对应的AutoreleasePool。</p>
</li>
</ol>
<p>点个赞再走呗～</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            