
---
title: 'OC底层原理（八）：objc_msgSend快速查找的分析下'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c4295dd4e3f455abe3b51dcfc886b04~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 22:35:58 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c4295dd4e3f455abe3b51dcfc886b04~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本章节是对于上个章节的补充说明，通过流程图与真机汇编解析快速查找，随便引出下一章的慢速查找。而最后的cache_t的扩容是对cache_t的补充说明！</p>
</blockquote>
<h2 data-id="heading-0">缓存查询流程图</h2>
<p>流程图:</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TB
A[objc_msgSend] -->B&#123;cmp p0, #0<br>判断接受者是否存在?<br>&#125;
    B -->|否| D[通过对象isa获取class]
    B -->|是| C&#123;是否支持<br>taggegpointer对象&#125;
    C -->|是| E&#123;小对象或者空 <br>判断LNilOrTagged<br>&#125;
    D --> G[获取isa完毕 LGetIsaDone]
    E -->|小对象Isa处理| G
    C -->|否| F[直接返回空LReturnZero]
    E -->|空| F
    G --> H[开去缓存查找流程 <br>CacheLookup NORMAL<br>]
    H --> I[通过类的指针平移16得到<br>cacheldr p11,x16 #CACHE<br>]
    I --> J[通过获取的mask_buckets掩码运算得到<br>bucketsand p10,p11, #0x0000ffffffffffff<br>]
    I --> K1[通过逻辑右移得到<br>mask p11, LSR #48<br>]
    K1 --> K2[通过and p12, p1 计算哈希函数<br>得到下标 _cmd &mask<br>]
    J --> K["p12=buckets+((_cmd & mask)<<(1+PTRSHIFT))<br>通过内存平移得到bucket<br>"]
    K2 --> K
    K --> L["通过bucket结构体得到<br>&#123;imp,sel&#125;=*bucket<br>"]
    L --> M&#123;判断要查询sel和当前_cmd<br>是否相等<br>&#125;
    M -->|是| N[命中缓存CacheHit $0]
    M --> M1[如果从最后一个元素遍历过来<br>还是找不到CheckMiss<br>]
    M -->|否| O&#123;"判断当前查询bucket是否为<br>第一个元素bucket == buckets<br>"&#125;
    O -->|是| P["把当前查询bucket设置为最后一个元素<br>p12 = buckets + (mask << 1+PTRSHIFT)<br>"]
    O -->|否| Q["向前查找<br>&#123;imp,sel&#125; = *--bucket<br>"]
    Q -->|递归查找| M
    P --> Q
</code></pre>
<h2 data-id="heading-1">汇编流程图简化讲解</h2>
<ul>
<li>1.判断当前<code>接收者</code>是否存在</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">cmpp0, #<span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.通过<code>isa</code>拿到<code>class</code></li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">GetClassFromIsa_p16 p13, <span class="hljs-number">1</span>, x0
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.进入<code>CacheLookup</code>流程,两种结果，找到并抛出<code>imp</code>，没找到通过<code>__objc_msgSend_uncached</code>进入后续的<code>慢速查找</code>流程</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">CacheLookup NORMAL, _objc_msgSend,__objc_msgSend_uncached
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>4.<code>LLookupStart</code>，查找开始，这里分解<code>模拟器</code>、<code>真机</code>、<code>arm64</code>架构，<code>A12</code>以上芯片汇编，下面只列出满足此条件的汇编</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">//模拟器</span>
CACHE_MASK_STORAGE == CACHE_MASK_STORAGE_HIGH_16_BIG_ADDRS <span class="hljs-comment">//mac电脑(x86-64)、arm64的模拟器</span>
<span class="hljs-comment">//真机</span>
CACHE_MASK_STORAGE == CACHE_MASK_STORAGE_HIGH_16
    <span class="hljs-comment">//amr64真机</span>
    CONFIG_USE_PREOPT_CACHES = <span class="hljs-number">1</span>
    <span class="hljs-comment">//是判断编译器是否支持指针身份验证功能，针对arm64e</span>
    <span class="hljs-comment">//A12以上芯片（支持arm64e结构）</span>
     __has_feature(ptrauth_calls)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>5.将<code>isa</code>偏移<code>16</code>个字节，由<code>p11 = mask|buckets</code>得到<code>cache_t</code></li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">ldrp11, [x16, #CACHE]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>6.判断<code>cache_t</code>的<code>0号</code>位置是否为<code>0</code>，如果<code>不</code>为0，执行<code>LLookupPreopt</code>，去找<code>共享缓存</code>，如果为0，将<code>cache_t(_bucketsAndMaybeMask) & #0x0000ffffffffffff</code>,得到了<code>bucekts</code></li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">tbnzp11, #<span class="hljs-number">0</span>, LLookupPreopt\Function
<span class="hljs-keyword">and</span>p10, p11, #<span class="hljs-number">0x0000ffffffffffff</span><span class="hljs-comment">// p10 = buckets</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>7.将<code>sel右移7位</code>在与自己做逻辑<code>异或^</code>赋值给<code>p12</code>,将<code>cache_t(_bucketsAndMaybeMask)</code>右移<code>48</code>位，即清空了<code>buckets</code>，可以得到<code>mask</code>，最后将<code>p12 & mask</code>，得到了第一次查找<code>bucket_t</code>的<code>index</code>，即<code>first_probed</code></li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">//p1 = _cmd, eor是异或,p12 = p1 ^(p1 >> 7) = _cmd ^ (_cmd >> 7)</span>
eor p12, p1, p1, LSR #<span class="hljs-number">7</span>
<span class="hljs-comment">//p11 >> 48 = _bucketsAndMaybeMask >> 48 = mask</span>
<span class="hljs-comment">//p12 = p12 & (p11 >> 48) = _cmd ^ (_cmd >> 7) & mask</span>
<span class="hljs-comment">//p12 = (_cmd ^ (_cmd >> 7)) & mask 这一步的作用就是hash求下标index</span>
<span class="hljs-keyword">and</span> p12, p12, p11, LSR #<span class="hljs-number">48</span> <span class="hljs-comment">// x12 = (_cmd ^ (_cmd >> 7)) & mask</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>7.1<code>clang</code>得到c++源码：</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">inline</span> <span class="hljs-keyword">mask_t</span> <span class="hljs-title">cache_hash</span><span class="hljs-params">(SEL sel, <span class="hljs-keyword">mask_t</span> mask)</span> 
</span>&#123;
    <span class="hljs-keyword">uintptr_t</span> value = (<span class="hljs-keyword">uintptr_t</span>)sel;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> CONFIG_USE_PREOPT_CACHES</span>
    value ^= value >> <span class="hljs-number">7</span>;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
    <span class="hljs-keyword">return</span> (<span class="hljs-keyword">mask_t</span>)(value & mask);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>8.由于上面可知第一个查找的<code>bucket_t</code>的下标<code>index</code>，那么接下来就是通过<code>偏移</code>到这个<code>bucket_t</code>拿到里面的<code>sel</code>与<code>imp</code>，这里是将<code>index</code>向左偏移<code>4</code>位，理解为<code>index * （1 << 4</code>）即<code>index * 16</code>，得到的是<code>偏移距离</code>。偏移<code>4位</code>是因为一个<code>bucket_t</code>占<code>16字节</code>，最后在加上<code>buckets</code>地址，就得到了第一个要比较的<code>bucket_t</code>。</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">addp13, p10, p12, LSL #(<span class="hljs-number">1</span>+PTRSHIFT)<span class="hljs-comment">// p13 = buckets + ((_cmd & mask) << (1+PTRSHIFT))</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>9.1将<code>p13</code>内的<code>imp</code>和<code>sel</code>拿出来分别存在<code>p17</code>和<code>p9</code>，执行<code>bucket--</code>。如果<code>sel != _cmd</code>,执行<code>3f</code>，判断<code>sel</code>是否存在，有值，将<code>bucket（当前</code>）与<code>bucekts（bucket首位）</code>比较，如果>0，继续循环，回到<code>1b</code>，执行<code>bucket--</code>。如果这个过程找到了目标<code>_cmd</code>,跳转到<code>2</code>，命中缓存，结束查找。</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">                                            <span class="hljs-comment">// do&#123;</span>
<span class="hljs-number">1</span>:ldpp17, p9, [x13], #-BUCKET_SIZE  <span class="hljs-comment">//   &#123;imp, sel&#125; = *bucket--</span>
cmpp9, p1      <span class="hljs-comment">//   if (sel != _cmd) &#123;</span>
b.ne<span class="hljs-number">3f</span>            <span class="hljs-comment">//      scan more </span>
                                           <span class="hljs-comment">//    &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-cpp copyable" lang="cpp">                                           <span class="hljs-comment">//    else &#123;</span>
<span class="hljs-number">2</span>:CacheHit \Mode                       <span class="hljs-comment">//     hit:    call or return imp</span>
                                           <span class="hljs-comment">//    &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-number">3</span>:cbzp9, \MissLabelDynamic         <span class="hljs-comment">//    if (sel == 0) goto Miss;</span>
cmpp13, p10                      <span class="hljs-comment">//   &#125; while (bucket >= buckets)</span>
b.hs<span class="hljs-number">1b</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>9.2如果找到<code>bucket</code>首位都未匹配到目标<code>_cmd</code>，则直接跳转至<code>mask</code>处<code>bucket</code>（末位<code>bucket_t</code>），查找缓存内剩余的<code>buckets</code>，这里还获取了第一次探查的位置<code>index</code>，为了避免重复探查。<code>4</code>内操作为将<code>bucket_t</code>的<code>imp</code>和<code>sel</code>拿出来赋值给<code>p17</code>和<code>p9</code>，<code>bucket--</code>，比较<code>sel</code>与<code>_cmd</code>，如果成功，执行<code>2b</code>，命中缓存，判断<code>p9</code>是否存在，判断当前<code>bucket</code>是否大于第一次探查的<code>bucket</code>，如果上述条件都满足，则继续循环<code>4b</code>，直到命中缓存。如果全部都搜索完还没有命中，进入<code>慢速查找</code>流程。</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">elif</span> CACHE_MASK_STORAGE == CACHE_MASK_STORAGE_HIGH_16<span class="hljs-comment">///arm64真机</span></span>
addp13, p10, p11, LSR #(<span class="hljs-number">48</span> - (<span class="hljs-number">1</span>+PTRSHIFT)) <span class="hljs-comment">// p13 = buckets + (mask << 1+PTRSHIFT)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-cpp copyable" lang="cpp">add p12, p10, p12, LSL #(<span class="hljs-number">1</span>+PTRSHIFT)<span class="hljs-comment">// p12 = first probed bucket</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-cpp copyable" lang="cpp">                                            <span class="hljs-comment">// do &#123;</span>
<span class="hljs-number">4</span>:ldpp17, p9, [x13], #-BUCKET_SIZE<span class="hljs-comment">//  &#123;imp, sel&#125; = *bucket--</span>
cmpp9, p1<span class="hljs-comment">//  if (sel == _cmd)</span>
b.eq<span class="hljs-number">2b</span>      <span class="hljs-comment">//      goto hit</span>
cmpp9, #<span class="hljs-number">0</span><span class="hljs-comment">// &#125; while (sel != 0 &&</span>
ccmpp13, p12, #<span class="hljs-number">0</span>, ne      <span class="hljs-comment">// bucket > first_probed)</span>
b.hi<span class="hljs-number">4b</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">真机调试（汇编分析）</h2>
<p>案例源码：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-meta">#import <span class="hljs-meta-string"><UIKit/UIKit.h></span></span>
<span class="hljs-meta">#import <span class="hljs-meta-string">"AppDelegate.h"</span></span>

<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">CJPerson</span> : <span class="hljs-title">NSObject</span></span>
- (<span class="hljs-keyword">void</span>)saySomething;
<span class="hljs-keyword">@end</span>

<span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">FFPerson</span></span>
- (<span class="hljs-keyword">void</span>)saySomething&#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%s"</span>,__func__);
&#125;
<span class="hljs-keyword">@end</span>
<span class="hljs-keyword">int</span> main(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span> * argv[]) &#123;
    <span class="hljs-keyword">@autoreleasepool</span> &#123;

        CJPerson *p = [CJPerson alloc];
        [p saySomething];
        appDelegateClassName = <span class="hljs-built_in">NSStringFromClass</span>([AppDelegate <span class="hljs-keyword">class</span>]);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">UIApplicationMain</span>(argc, argv, <span class="hljs-literal">nil</span>, appDelegateClassName);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">确认当前探索的类与方法</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c4295dd4e3f455abe3b51dcfc886b04~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-19 上午10.28.49.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">真机汇编分解图解：</h3>
<pre><code class="hljs language-mm copyable" lang="mm">libobjc.A.dylib`objc_msgSend:
    <span class="hljs-comment">//x0为消息接收者receiver，比较x0与0，如果没有接收者，则此次objc_msgSend没有意义(x0 = 0x00000002803b8180)</span>
->  <span class="hljs-number">0x19ef9b1c0</span> <+<span class="hljs-number">0</span>>:   cmp    x0, #<span class="hljs-number">0x0</span>                  ; =<span class="hljs-number">0x0</span> 

    <span class="hljs-number">0x19ef9b1c4</span> <+<span class="hljs-number">4</span>>:   b.le   <span class="hljs-number">0x19ef9b28c</span>               ; <+<span class="hljs-number">204</span>>
    <span class="hljs-comment">//将x0里面的实例对象p的isa赋值给x13</span>
    <span class="hljs-comment">//即将寄存器x0地址为0x00000002803b8180的字数据读入到寄存器x13(x13 = 0x01000001026cd441 (0x00000001026cd441) (void *)0x4800000001026cd4)</span>
    <span class="hljs-comment">//具体可以看`底层原理（三）`里的x/4gx 0x00000002803b8180</span>
    <span class="hljs-number">0x19ef9b1c8</span> <+<span class="hljs-number">8</span>>:   ldr    x13, [x0]
    <span class="hljs-comment">//将x13&0x7ffffffffffff8(即isa & ISA_MASK获取到类CJPerson)赋值给x16(x16 = 0x00000001026cd440  (void *)0x00000001026cd418: CJPerson)</span>
    <span class="hljs-number">0x19ef9b1cc</span> <+<span class="hljs-number">12</span>>:  and    x16, x13, #<span class="hljs-number">0x7ffffffffffff8</span>
    <span class="hljs-comment">//将 x0赋值给x10(即将实例对象p复制到x10 = 0x00000002803b8180)</span>
    <span class="hljs-number">0x19ef9b1d0</span> <+<span class="hljs-number">16</span>>:  mov    x10, x0
    <span class="hljs-comment">//将x10内的内容数据从48位开始更为0x6ae1(x10 = 0x6ae10002803b8180)</span>
    <span class="hljs-number">0x19ef9b1d4</span> <+<span class="hljs-number">20</span>>:  movk   x10, #<span class="hljs-number">0x6ae1</span>, lsl #<span class="hljs-number">48</span>
    <span class="hljs-comment">//(x16 = 0x00000001026cd440  (void *)0x00000001026cd418: CJPerson)</span>
    <span class="hljs-number">0x19ef9b1d8</span> <+<span class="hljs-number">24</span>>:  autda  x16, x10
    <span class="hljs-comment">//将x16赋值给x15(x15 = 0x00000001026cd440  (void *)0x00000001026cd418: CJPerson)</span>
    <span class="hljs-number">0x19ef9b1dc</span> <+<span class="hljs-number">28</span>>:  mov    x15, x16
    <span class="hljs-comment">//将CJPerson的isa右移16位读取cache_t, px16+0x10(x/4gx 0x00000001026cd440)后读取内容数据到(x11 = 0x00010002801be4a0)</span>
    <span class="hljs-number">0x19ef9b1e0</span> <+<span class="hljs-number">32</span>>:  ldr    x11, [x16, #<span class="hljs-number">0x10</span>]
    <span class="hljs-comment">//判断w11(w11 = 0x801be4a0)的第0位是否为0,为0继续往下走，不为0跳转到下面0x19ef9b240地址执行</span>
    <span class="hljs-number">0x19ef9b1e4</span> <+<span class="hljs-number">36</span>>:  tbnz   w11, #<span class="hljs-number">0x0</span>, <span class="hljs-number">0x19ef9b240</span>    ; <+<span class="hljs-number">128</span>>
    <span class="hljs-comment">//x10 = x11 & 0xffffffffffff(即x10 = 0x00000002801be4a0)</span>
    <span class="hljs-number">0x19ef9b1e8</span> <+<span class="hljs-number">40</span>>:  and    x10, x11, #<span class="hljs-number">0xffffffffffff</span>
    <span class="hljs-comment">//x12 = _cmd ^ (_cmd >> 7)即(传入方法参数x1 = 0x00000001026c718e  "saySomething")(x12为0x000000010068a96d = 0x00000001026c718e ^ 0x000000000204d8e3)</span>
    <span class="hljs-number">0x19ef9b1ec</span> <+<span class="hljs-number">44</span>>:  eor    x12, x1, x1, lsr #<span class="hljs-number">7</span>
    <span class="hljs-comment">//mask = x11 >> 48 即(0x00010002801be4a0 >> 48 = 0x0000000000000001)</span>
    <span class="hljs-comment">//x12 = mask & x12 即(x12 = 0x0000000000000001)为第一个检索位置即first_prepot</span>
    <span class="hljs-number">0x19ef9b1f0</span> <+<span class="hljs-number">48</span>>:  and    x12, x12, x11, lsr #<span class="hljs-number">48</span>
    <span class="hljs-comment">//buckets + first_preop 即 x13 = (0x00000002801be4a0 + (0x01 << 4 = 0x10)) = 0x00000002801be4b0</span>
    <span class="hljs-number">0x19ef9b1f4</span> <+<span class="hljs-number">52</span>>:  add    x13, x10, x12, lsl #<span class="hljs-number">4</span>
    <span class="hljs-comment">//p x13 - 0x10得到老版本地区 即x/4gx 0x00000002801be4b0取出前两位分别赋值 x17 = 0xdd1a3d019efbeb34, x9 = 0x00000001da0a38ae</span>
    <span class="hljs-number">0x19ef9b1f8</span> <+<span class="hljs-number">56</span>>:  ldp    x17, x9, [x13], #<span class="hljs-number">-0x10</span>
    <span class="hljs-comment">//比较x9与x1，x9 == x1 即0x00000001da0a38ae == 0x00000001026c718e</span>
    <span class="hljs-number">0x19ef9b1fc</span> <+<span class="hljs-number">60</span>>:  cmp    x9, x1
    <span class="hljs-comment">//不等跳转到0x19ef9b210</span>
    <span class="hljs-number">0x19ef9b200</span> <+<span class="hljs-number">64</span>>:  b.ne   <span class="hljs-number">0x19ef9b210</span>               ; <+<span class="hljs-number">80</span>>
    <span class="hljs-comment">// x10 = x10异或x1</span>
    <span class="hljs-number">0x19ef9b204</span> <+<span class="hljs-number">68</span>>:  eor    x10, x10, x1
    <span class="hljs-comment">// x10 = x10 ^ x16</span>
    <span class="hljs-number">0x19ef9b208</span> <+<span class="hljs-number">72</span>>:  eor    x10, x10, x16
    <span class="hljs-comment">//</span>
    <span class="hljs-number">0x19ef9b20c</span> <+<span class="hljs-number">76</span>>:  brab   x17, x10
    <span class="hljs-comment">// </span>
    <span class="hljs-number">0x19ef9b210</span> <+<span class="hljs-number">80</span>>:  cbz    x9, <span class="hljs-number">0x19ef9b600</span>           ; _objc_msgSend_uncached
    <span class="hljs-comment">//比较x13与x10 即0x00000002801be4a0 == 0x00000002801be4a0</span>
    <span class="hljs-number">0x19ef9b214</span> <+<span class="hljs-number">84</span>>:  cmp    x13, x10
    <span class="hljs-comment">//相等时跳转到0x19ef9b1f8从新开始 但是x13 = 0x00000002801be4a0比之前0x00000002801be4b0-0x10</span>
    <span class="hljs-number">0x19ef9b218</span> <+<span class="hljs-number">88</span>>:  b.hs   <span class="hljs-number">0x19ef9b1f8</span>               ; <+<span class="hljs-number">56</span>>
    <span class="hljs-comment">//不相等时，x13 = (x10 = 0x00000002801be4a0) + ((x11 = 0x00010002801be4a0)>>44 = 0x0000000000000010) = 0x00000002801be4b0</span>
    <span class="hljs-number">0x19ef9b21c</span> <+<span class="hljs-number">92</span>>:  add    x13, x10, x11, lsr #<span class="hljs-number">44</span>
    <span class="hljs-comment">//x12 = (x10 = 0x00000002801be4a0) + (x12 = 0x0000000000000001 << 4) = 0x00000002801be4b0</span>
    <span class="hljs-number">0x19ef9b220</span> <+<span class="hljs-number">96</span>>:  add    x12, x10, x12, lsl #<span class="hljs-number">4</span>
    <span class="hljs-comment">//取出x13指向数据前两位x17 = 0xdd1a3d019efbeb34, x9 = 0x00000001da0a38ae</span>
    <span class="hljs-number">0x19ef9b224</span> <+<span class="hljs-number">100</span>>: ldp    x17, x9, [x13], #<span class="hljs-number">-0x10</span>
    <span class="hljs-comment">//比较x9与x1 x9 = 0x00000001da0a38ae x1 = 0x00000001026c718e  "saySomething"</span>
    <span class="hljs-number">0x19ef9b228</span> <+<span class="hljs-number">104</span>>: cmp    x9, x1
    <span class="hljs-comment">//相等时跳转0x19ef9b204</span>
    <span class="hljs-number">0x19ef9b22c</span> <+<span class="hljs-number">108</span>>: b.eq   <span class="hljs-number">0x19ef9b204</span>               ; <+<span class="hljs-number">68</span>>
    <span class="hljs-comment">//判断x9是否为0x00</span>
    <span class="hljs-number">0x19ef9b230</span> <+<span class="hljs-number">112</span>>: cmp    x9, #<span class="hljs-number">0x0</span>                  ; =<span class="hljs-number">0x0</span> 
    <span class="hljs-comment">//x13 = 0x00000002801be4a0, x12 = 0x00000002801be4b</span>
    <span class="hljs-number">0x19ef9b234</span> <+<span class="hljs-number">116</span>>: ccmp   x13, x12, #<span class="hljs-number">0x0</span>, ne

    <span class="hljs-number">0x19ef9b238</span> <+<span class="hljs-number">120</span>>: b.hi   <span class="hljs-number">0x19ef9b224</span>               ; <+<span class="hljs-number">100</span>>
    <span class="hljs-comment">//跳转到0x19ef9b600执行_objc_msgSend_uncached(慢速查找)</span>
    <span class="hljs-number">0x19ef9b23c</span> <+<span class="hljs-number">124</span>>: b      <span class="hljs-number">0x19ef9b600</span>               ; _objc_msgSend_uncached
    <span class="hljs-comment">//x10 = x11 & 0x7ffffffffffffe</span>
    <span class="hljs-number">0x19ef9b240</span> <+<span class="hljs-number">128</span>>: and    x10, x11, #<span class="hljs-number">0x7ffffffffffffe</span>
    
    <span class="hljs-number">0x19ef9b244</span> <+<span class="hljs-number">132</span>>: autdb  x10, x16

    <span class="hljs-number">0x19ef9b248</span> <+<span class="hljs-number">136</span>>: adrp   x9, <span class="hljs-number">239235</span>

    <span class="hljs-number">0x19ef9b24c</span> <+<span class="hljs-number">140</span>>: add    x9, x9, #<span class="hljs-number">0x4ae</span>            ; =<span class="hljs-number">0x4ae</span> 

    <span class="hljs-number">0x19ef9b250</span> <+<span class="hljs-number">144</span>>: sub    x12, x1, x9

    <span class="hljs-number">0x19ef9b254</span> <+<span class="hljs-number">148</span>>: lsr    x17, x11, #<span class="hljs-number">55</span>

    <span class="hljs-number">0x19ef9b258</span> <+<span class="hljs-number">152</span>>: lsr    w9, w12, w17

    <span class="hljs-number">0x19ef9b25c</span> <+<span class="hljs-number">156</span>>: lsr    x17, x11, #<span class="hljs-number">60</span>

    <span class="hljs-number">0x19ef9b260</span> <+<span class="hljs-number">160</span>>: mov    x11, #<span class="hljs-number">0x7fff</span>

    <span class="hljs-number">0x19ef9b264</span> <+<span class="hljs-number">164</span>>: lsr    x11, x11, x17

    <span class="hljs-number">0x19ef9b268</span> <+<span class="hljs-number">168</span>>: and    x9, x9, x11

    <span class="hljs-number">0x19ef9b26c</span> <+<span class="hljs-number">172</span>>: ldr    x17, [x10, x9, lsl #<span class="hljs-number">3</span>]

    <span class="hljs-number">0x19ef9b270</span> <+<span class="hljs-number">176</span>>: cmp    x12, w17, uxtw

    <span class="hljs-number">0x19ef9b274</span> <+<span class="hljs-number">180</span>>: b.ne   <span class="hljs-number">0x19ef9b280</span>               ; <+<span class="hljs-number">192</span>>

    <span class="hljs-number">0x19ef9b278</span> <+<span class="hljs-number">184</span>>: sub    x17, x16, x17, lsr #<span class="hljs-number">32</span>

    <span class="hljs-number">0x19ef9b27c</span> <+<span class="hljs-number">188</span>>: br     x17

    <span class="hljs-number">0x19ef9b280</span> <+<span class="hljs-number">192</span>>: ldursw x9, [x10, #<span class="hljs-number">-0x8</span>]

    <span class="hljs-number">0x19ef9b284</span> <+<span class="hljs-number">196</span>>: add    x16, x16, x9

    <span class="hljs-number">0x19ef9b288</span> <+<span class="hljs-number">200</span>>: b      <span class="hljs-number">0x19ef9b1e0</span>               ; <+<span class="hljs-number">32</span>>

    <span class="hljs-number">0x19ef9b28c</span> <+<span class="hljs-number">204</span>>: b.eq   <span class="hljs-number">0x19ef9b2b0</span>               ; <+<span class="hljs-number">240</span>>

    <span class="hljs-number">0x19ef9b290</span> <+<span class="hljs-number">208</span>>: and    x10, x0, #<span class="hljs-number">0x7</span>

    <span class="hljs-number">0x19ef9b294</span> <+<span class="hljs-number">212</span>>: asr    x11, x0, #<span class="hljs-number">55</span>

    <span class="hljs-number">0x19ef9b298</span> <+<span class="hljs-number">216</span>>: cmp    x10, #<span class="hljs-number">0x7</span>                 ; =<span class="hljs-number">0x7</span> 

    <span class="hljs-number">0x19ef9b29c</span> <+<span class="hljs-number">220</span>>: csel   x12, x11, x10, eq

    <span class="hljs-number">0x19ef9b2a0</span> <+<span class="hljs-number">224</span>>: adrp   x10, <span class="hljs-number">320424</span>

    <span class="hljs-number">0x19ef9b2a4</span> <+<span class="hljs-number">228</span>>: add    x10, x10, #<span class="hljs-number">0x820</span>          ; =<span class="hljs-number">0x820</span> 

    <span class="hljs-number">0x19ef9b2a8</span> <+<span class="hljs-number">232</span>>: ldr    x16, [x10, x12, lsl #<span class="hljs-number">3</span>]

    <span class="hljs-number">0x19ef9b2ac</span> <+<span class="hljs-number">236</span>>: b      <span class="hljs-number">0x19ef9b1dc</span>               ; <+<span class="hljs-number">28</span>>

    <span class="hljs-number">0x19ef9b2b0</span> <+<span class="hljs-number">240</span>>: mov    x1, #<span class="hljs-number">0x0</span>

    <span class="hljs-number">0x19ef9b2b4</span> <+<span class="hljs-number">244</span>>: movi   d0, #<span class="hljs-number">0000000000000000</span>

    <span class="hljs-number">0x19ef9b2b8</span> <+<span class="hljs-number">248</span>>: movi   d1, #<span class="hljs-number">0000000000000000</span>

    <span class="hljs-number">0x19ef9b2bc</span> <+<span class="hljs-number">252</span>>: movi   d2, #<span class="hljs-number">0000000000000000</span>

    <span class="hljs-number">0x19ef9b2c0</span> <+<span class="hljs-number">256</span>>: movi   d3, #<span class="hljs-number">0000000000000000</span>

    <span class="hljs-number">0x19ef9b2c4</span> <+<span class="hljs-number">260</span>>: ret    

    <span class="hljs-number">0x19ef9b2c8</span> <+<span class="hljs-number">264</span>>: nop    

    <span class="hljs-number">0x19ef9b2cc</span> <+<span class="hljs-number">268</span>>: nop    

    <span class="hljs-number">0x19ef9b2d0</span> <+<span class="hljs-number">272</span>>: nop    

    <span class="hljs-number">0x19ef9b2d4</span> <+<span class="hljs-number">276</span>>: nop    

    <span class="hljs-number">0x19ef9b2d8</span> <+<span class="hljs-number">280</span>>: nop    

    <span class="hljs-number">0x19ef9b2dc</span> <+<span class="hljs-number">284</span>>: nop    

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">补充内容</h2>
<h3 data-id="heading-6">关于类cache_t内存扩容在真机情况下的源码模拟</h3>
<p>Demo地址
部分关键源码：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-keyword">typedef</span> uint32_t mask_t;  <span class="hljs-comment">// x86_64 & arm64 asm are less efficient</span>

<span class="hljs-comment">//preopt_cache_entry_t源码模仿</span>
<span class="hljs-keyword">struct</span> ff_preopt_cache_entry_t &#123;
    uint32_t sel_offs;
    uint32_t imp_offs;
&#125;;

<span class="hljs-comment">//preopt_cache_t源码模仿</span>
<span class="hljs-keyword">struct</span> ff_preopt_cache_t &#123;
    int32_t  fallback_class_offset;
    <span class="hljs-keyword">union</span> &#123;
        <span class="hljs-keyword">struct</span> &#123;
            uint16_t shift       :  <span class="hljs-number">5</span>;
            uint16_t mask        : <span class="hljs-number">11</span>;
        &#125;;
        uint16_t hash_params;
    &#125;;
    uint16_t occupied    : <span class="hljs-number">14</span>;
    uint16_t has_inlines :  <span class="hljs-number">1</span>;
    uint16_t bit_one     :  <span class="hljs-number">1</span>;
    <span class="hljs-keyword">struct</span> ff_preopt_cache_entry_t entries;
    
    <span class="hljs-keyword">inline</span> <span class="hljs-keyword">int</span> capacity() <span class="hljs-keyword">const</span> &#123;
        <span class="hljs-keyword">return</span> mask + <span class="hljs-number">1</span>;
    &#125;
&#125;;

<span class="hljs-comment">//bucket_t源码模仿</span>
<span class="hljs-keyword">struct</span> ff_bucket_t &#123;
    IMP _imp;
    SEL _sel;
&#125;;

<span class="hljs-comment">//cache_t源码模仿</span>
<span class="hljs-keyword">struct</span> ff_cache_t &#123;
    uintptr_t _bucketsAndMaybeMask; <span class="hljs-comment">// 8</span>
    <span class="hljs-keyword">struct</span> ff_preopt_cache_t _originalPreoptCache; <span class="hljs-comment">// 8</span>

    <span class="hljs-keyword">static</span> constexpr uintptr_t maskShift = <span class="hljs-number">48</span>;

    <span class="hljs-keyword">static</span> constexpr uintptr_t maskZeroBits = <span class="hljs-number">4</span>;

    <span class="hljs-keyword">static</span> constexpr uintptr_t maxMask = ((uintptr_t)<span class="hljs-number">1</span> << (<span class="hljs-number">64</span> - maskShift)) - <span class="hljs-number">1</span>;
    
    <span class="hljs-keyword">static</span> constexpr uintptr_t bucketsMask = ((uintptr_t)<span class="hljs-number">1</span> << (maskShift - maskZeroBits)) - <span class="hljs-number">1</span>;
    
    <span class="hljs-keyword">static</span> constexpr uintptr_t preoptBucketsMarker = <span class="hljs-number">1</span>ul;

    <span class="hljs-keyword">static</span> constexpr uintptr_t preoptBucketsMask = <span class="hljs-number">0x007ffffffffffffe</span>;
    
    ff_bucket_t *buckets() &#123;
        <span class="hljs-keyword">return</span> (ff_bucket_t *)(_bucketsAndMaybeMask & bucketsMask);
    &#125;
    
    uint32_t mask() <span class="hljs-keyword">const</span> &#123;
        <span class="hljs-keyword">return</span> _bucketsAndMaybeMask >> maskShift;
    &#125;
    
&#125;;

<span class="hljs-comment">//class_data_bits_t源码模仿</span>
<span class="hljs-keyword">struct</span> ff_class_data_bits_t &#123;
    uintptr_t objc_class;
&#125;;

<span class="hljs-comment">//类源码模仿</span>
<span class="hljs-keyword">struct</span> ff_objc_class &#123;
    Class isa;
    Class superclass;
    <span class="hljs-keyword">struct</span> ff_cache_t cache;
    <span class="hljs-keyword">struct</span> ff_class_data_bits_t bits;
&#125;;


<span class="hljs-keyword">void</span> test(Class cls) &#123;
    
    <span class="hljs-comment">//将person的类型转换成自定义的源码ff_objc_class类型，方便后续操作</span>
    <span class="hljs-keyword">struct</span> ff_objc_class *pClass = (__bridge <span class="hljs-keyword">struct</span> ff_objc_class *)(cls);
    
    <span class="hljs-keyword">struct</span> ff_cache_t cache = pClass->cache;
    <span class="hljs-keyword">struct</span> ff_bucket_t * buckets = cache.buckets();
    <span class="hljs-keyword">struct</span> ff_preopt_cache_t origin = cache._originalPreoptCache;
    uintptr_t _bucketsAndMaybeMask = cache._bucketsAndMaybeMask;
    uintptr_t mask = cache.mask();
    
    
    
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"class: %p"</span>, pClass);
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"_bucketsAndMaybeMask: 0x%lx, mask: %lu"</span>, _bucketsAndMaybeMask, mask);
    
    <span class="hljs-comment">//打印当前有多少个方法缓存与最大缓存数量</span>
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%u-%u"</span>,origin.occupied,origin.capacity());
    
    <span class="hljs-comment">//打印buckets</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < mask + <span class="hljs-number">1</span>; i++ ) &#123;
        SEL sel = buckets[i]._sel;
        IMP imp = buckets[i]._imp;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@-%p"</span>,<span class="hljs-built_in">NSStringFromSelector</span>(sel),imp);
    &#125;
&#125;

<span class="hljs-keyword">int</span> main(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span> * argv[]) &#123;

    <span class="hljs-keyword">@autoreleasepool</span> &#123;
        
        <span class="hljs-comment">//给person分配内存</span>
        FFPerson *person = [FFPerson alloc];
        <span class="hljs-comment">//调用方法</span>
        [person likeGirls];
        test(person.class);
        [person likeFoods];
        test(person.class);
        [person likeflower];
        test(person.class);
        [person likeStudy];
        test(person.class);
        [person enjoyLift];
        test(person.class);
        [person lnspireCreativity];
        test(person.class);
        
       ......

    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">UIApplicationMain</span>(argc, argv, <span class="hljs-literal">nil</span>, <span class="hljs-built_in">NSStringFromClass</span>([AppDelegate <span class="hljs-keyword">class</span>]));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.523507</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] -[FFPerson likeGirls]
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.524594</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-class"><span class="hljs-keyword">class</span>:</span> <span class="hljs-number">0x102ef9680</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.524617</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] _bucketsAndMaybeMask: <span class="hljs-number">0x10002835b60e0</span>, mask: <span class="hljs-number">1</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.524633</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-number">1</span><span class="hljs-number">-1025</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.524651</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] (null)<span class="hljs-number">-0x0</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.524706</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeGirls<span class="hljs-number">-0xe00f9f8102ef148c</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.524728</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] -[FFPerson likeFoods]
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.524868</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-class"><span class="hljs-keyword">class</span>:</span> <span class="hljs-number">0x102ef9680</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525038</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] _bucketsAndMaybeMask: <span class="hljs-number">0x10002835b60e0</span>, mask: <span class="hljs-number">1</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525138</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-number">2</span><span class="hljs-number">-1025</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525253</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeFoods<span class="hljs-number">-0xf64c0b0102ef1504</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525279</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeGirls<span class="hljs-number">-0xe00f9f8102ef148c</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525298</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] -[FFPerson likeflower]
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525312</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-class"><span class="hljs-keyword">class</span>:</span> <span class="hljs-number">0x102ef9680</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525326</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] _bucketsAndMaybeMask: <span class="hljs-number">0x30002820b4c40</span>, mask: <span class="hljs-number">3</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525437</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-number">1</span><span class="hljs-number">-1025</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525517</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] (null)<span class="hljs-number">-0x0</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525783</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] (null)<span class="hljs-number">-0x0</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.525910</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] (null)<span class="hljs-number">-0x0</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.526071</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeflower<span class="hljs-number">-0x2d78768102ef14c8</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.526236</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] -[FFPerson likeStudy]
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.526347</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-class"><span class="hljs-keyword">class</span>:</span> <span class="hljs-number">0x102ef9680</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.526438</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] _bucketsAndMaybeMask: <span class="hljs-number">0x30002820b4c40</span>, mask: <span class="hljs-number">3</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.526548</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-number">2</span><span class="hljs-number">-1025</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.526643</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] (null)<span class="hljs-number">-0x0</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.526745</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] (null)<span class="hljs-number">-0x0</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.526900</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeStudy<span class="hljs-number">-0xf26c730102ef1540</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527019</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeflower<span class="hljs-number">-0x2d78768102ef14c8</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527098</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] -[FFPerson enjoyLift]
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527195</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-class"><span class="hljs-keyword">class</span>:</span> <span class="hljs-number">0x102ef9680</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527316</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] _bucketsAndMaybeMask: <span class="hljs-number">0x30002820b4c40</span>, mask: <span class="hljs-number">3</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527427</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-number">3</span><span class="hljs-number">-1025</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527520</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] (null)<span class="hljs-number">-0x0</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527626</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] enjoyLift<span class="hljs-number">-0x8e617e8102ef157c</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527728</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeStudy<span class="hljs-number">-0xf26c730102ef1540</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.527829</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeflower<span class="hljs-number">-0x2d78768102ef14c8</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.528005</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] -[FFPerson lnspireCreativity]
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.528130</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-class"><span class="hljs-keyword">class</span>:</span> <span class="hljs-number">0x102ef9680</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.528236</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] _bucketsAndMaybeMask: <span class="hljs-number">0x30002820b4c40</span>, mask: <span class="hljs-number">3</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.528349</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] <span class="hljs-number">4</span><span class="hljs-number">-1025</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.528450</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] lnspireCreativity<span class="hljs-number">-0xc6607b8102ef15b8</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.528536</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] enjoyLift<span class="hljs-number">-0x8e617e8102ef157c</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.528705</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeStudy<span class="hljs-number">-0xf26c730102ef1540</span>
<span class="hljs-number">2021</span><span class="hljs-number">-06</span><span class="hljs-number">-30</span> <span class="hljs-number">23</span>:<span class="hljs-number">38</span>:<span class="hljs-number">39.528804</span>+<span class="hljs-number">0800</span> <span class="hljs-number">002</span>-cache真机源码还原[<span class="hljs-number">2001</span>:<span class="hljs-number">757686</span>] likeflower<span class="hljs-number">-0x2d78768102ef14c8</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-s copyable" lang="s">INIT_CACHE_SIZE_LOG2
#if CACHE_END_MARKER || (__arm64__ && !__LP64__)
    INIT_CACHE_SIZE_LOG2 = 2,
#else
    INIT_CACHE_SIZE_LOG2 = 1,
#endif
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-s copyable" lang="s">cache_fill_ratio
#if __arm__  ||  __x86_64__  ||  __i386__

#define CACHE_END_MARKER 1

static inline mask_t cache_fill_ratio(mask_t capacity) &#123;
    return capacity * 3 / 4;
&#125;

#elif __arm64__ && !__LP64__

#define CACHE_END_MARKER 0

static inline mask_t cache_fill_ratio(mask_t capacity) &#123;
    return capacity * 3 / 4;
&#125;

#elif __arm64__ && __LP64__

#define CACHE_END_MARKER 0

static inline mask_t cache_fill_ratio(mask_t capacity) &#123;
    return capacity * 7 / 8;
&#125;

#define CACHE_ALLOW_FULL_UTILIZATION 1

#else
#error unknown architecture
#endif
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论：</p>
<blockquote>
<ul>
<li><code>iPhoneXs</code>，初始缓存容量为2（<code>INIT_CACHE_SIZE = (1 << 1)</code>）</li>
<li>真机扩容按照7/8的规则，2倍扩容，所以扩容规律2-> 4 -> 8 -> 16 -> 2^n</li>
<li><code>x86_64</code>架构初始容量为4（<code>INIT_CACHE_SIZE = (1 << 2)</code>）</li>
<li>模拟器扩容按照3/4的规则，2倍扩容，扩容规律4 -> 8 -> 16 -> 2^(n+1)</li>
</ul>
</blockquote></div>  
</div>
            