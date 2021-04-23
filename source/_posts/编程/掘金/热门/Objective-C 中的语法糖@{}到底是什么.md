
---
title: 'Objective-C 中的语法糖@&#123;&#125;到底是什么'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=1010'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 02:12:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=1010'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>欢迎各位 <strong>点赞评论</strong>，感觉有用的朋友可以关注笔者公众号 iOS 成长指北，持续更新</p>
</blockquote>
<p>最近在技术群里有一个群友提出了一个问题，就是为什么下面代码打印的结果不一样？</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-built_in">NSMutableDictionary</span> *mDic1 = [<span class="hljs-built_in">NSMutableDictionary</span> dictionaryWithDictionary:@&#123;<span class="hljs-string">@"a"</span>:@<span class="hljs-number">1</span>, <span class="hljs-string">@"a"</span>:@<span class="hljs-number">2</span>&#125;];
<span class="hljs-comment">//'a': 1</span>
<span class="hljs-built_in">NSMutableDictionary</span> *mDic2 = [<span class="hljs-built_in">NSMutableDictionary</span> dictionary];
[mDic2 setObject:@(<span class="hljs-number">1</span>) forKey:<span class="hljs-string">@"a"</span>];
[mDic2 setObject:@(<span class="hljs-number">2</span>) forKey:<span class="hljs-string">@"a"</span>];
   <span class="hljs-comment">//'a': 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对此，笔者进行了一些研究，期待能够解释这件问题。</p>
<h3 data-id="heading-0"><code>@&#123;&#125;</code> 到底是什么？</h3>
<p>造成这个数据结果的可能性之一，应该是</p>
<pre><code class="hljs language-swift copyable" lang="swift">@&#123;@<span class="hljs-string">"a"</span>:@<span class="hljs-number">1</span>, @<span class="hljs-string">"a"</span>:@<span class="hljs-number">2</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本身就是一个 <code>key</code> 为 <code>a</code>， 值为 <code>1</code> 的字典 。</p>
<p>通过测试代码，如下：</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-built_in">NSDictionary</span> *dic = @&#123;<span class="hljs-string">@"a"</span>:@<span class="hljs-number">1</span>, <span class="hljs-string">@"a"</span>:@<span class="hljs-number">2</span>&#125;;
<span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%@"</span>, dic);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现其本身就是一个 <code>key</code> 为 <code>a</code>， 值为 <code>1</code> 的字典 。</p>
<p>那么 <code>@&#123;&#125;</code>  到底是什么呢？其实如何操作的呢？他的分配方式究竟是什么？</p>
<h4 data-id="heading-1">实验步骤</h4>
<p>基于网上找到的 NSDictionary 的伪代码，无论如何，当我们创建一个字典时，其最终都会执行</p>
<pre><code class="hljs language-objc copyable" lang="objc">- (<span class="hljs-keyword">id</span>)initWithObjects:(<span class="hljs-keyword">const</span> <span class="hljs-keyword">id</span> [])objects forKeys:(<span class="hljs-keyword">const</span> <span class="hljs-keyword">id</span> <<span class="hljs-built_in">NSCopying</span>> [])keys count:(<span class="hljs-built_in">NSUInteger</span>)cnt
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么假使我们通过 hook 监听这个方法，我们就知道在初始化时传入的 <code>objects</code> 和 <code>keys</code> 究竟是什么？但是，可惜的是，没有 hook 住。</p>
<p>难道是我的做法有问题吗？</p>
<p>笔者发现在使用 <code>@&#123;&#125;</code> 时根本就不执行这个步骤？是其他的吗？</p>
<p>然后笔者选择通过添加符号断点 <code>+[NSDictionary dictionaryWithObjects:forKeys:count:]</code> 发现，当我们赋值时，其符号断点会挂住。</p>
<p>我们在使用  <code>@&#123;&#125;</code>  创建字典的时候会调用这个方法吗？值得一试？</p>
<p>通过 hook 了字典的这个方法，我们在分类中做一个接受，当系统调用时，挂上断点</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">+</span> (id)xxx_dictionaryWithObjects:(const id [])objects forKeys:(const id <span class="hljs-operator"><</span><span class="hljs-type">NSCopying</span><span class="hljs-operator">></span> [])keys count:(<span class="hljs-type">NSUInteger</span>)cnt&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-type">NSUInteger</span> i <span class="hljs-operator">=</span> <span class="hljs-number">0</span>; i <span class="hljs-operator"><</span> cnt; i<span class="hljs-operator">++</span>) &#123;
        id key <span class="hljs-operator">=</span> keys[i];
        id obj <span class="hljs-operator">=</span> objects[i];
        <span class="hljs-type">NSLog</span>(@<span class="hljs-string">"key = %@"</span>, key);
        <span class="hljs-type">NSLog</span>(@<span class="hljs-string">"obj = %@"</span>, obj);
 &#125;
    <span class="hljs-keyword">return</span> [[<span class="hljs-type">NSDictionary</span> <span class="hljs-class"><span class="hljs-keyword">class</span>] <span class="hljs-title">xxx_dictionaryWithObjects</span>:<span class="hljs-title">objects</span> <span class="hljs-title">forKeys</span>:<span class="hljs-title">keys</span> <span class="hljs-title">count</span>:<span class="hljs-title">cnt</span>];
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-number">2021</span><span class="hljs-number">-03</span><span class="hljs-number">-30</span> <span class="hljs-number">17</span>:<span class="hljs-number">13</span>:<span class="hljs-number">40.971674</span>+<span class="hljs-number">0800</span> suspenseRoad[<span class="hljs-number">28886</span>:<span class="hljs-number">413231</span>] key = a
<span class="hljs-number">2021</span><span class="hljs-number">-03</span><span class="hljs-number">-30</span> <span class="hljs-number">17</span>:<span class="hljs-number">13</span>:<span class="hljs-number">40.971743</span>+<span class="hljs-number">0800</span> suspenseRoad[<span class="hljs-number">28886</span>:<span class="hljs-number">413231</span>] obj = <span class="hljs-number">1</span>
<span class="hljs-number">2021</span><span class="hljs-number">-03</span><span class="hljs-number">-30</span> <span class="hljs-number">17</span>:<span class="hljs-number">13</span>:<span class="hljs-number">40.971814</span>+<span class="hljs-number">0800</span> suspenseRoad[<span class="hljs-number">28886</span>:<span class="hljs-number">413231</span>] key = a
<span class="hljs-number">2021</span><span class="hljs-number">-03</span><span class="hljs-number">-30</span> <span class="hljs-number">17</span>:<span class="hljs-number">13</span>:<span class="hljs-number">40.971896</span>+<span class="hljs-number">0800</span> suspenseRoad[<span class="hljs-number">28886</span>:<span class="hljs-number">413231</span>] obj = <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并等到下面的结果，我们在初始化设置的时候，传入的值都已经进入代码中，但是结果并没有</p>
<p>继续探究一下  <code>+[NSDictionary dictionaryWithObjects:forKeys:count:]</code> 的方法</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">+ (id)dictionaryWithDictionary:(NSDictionary *)dict
&#123;
    size_t count = [dict count];
    id *objects = NULL;
    id *keys = NULL;

    if (count > 0) &#123;
        objects = malloc(sizeof(id) * count);
        if (UNLIKELY(objects == NULL)) &#123;
            return NULL;
        &#125;
        keys = malloc(sizeof(id) * count);
        if (UNLIKELY(keys == NULL)) &#123;
            free(objects);
            return NULL;
        &#125;
    &#125;
  
    [dict getObjects:objects andKeys:keys];
    id obj = [[self alloc] initWithObjects:objects forKeys:keys count:count];

    if (objects != NULL) &#123;
        free(objects);
    &#125;
    if (keys != NULL) &#123;
        free(keys);
    &#125;

    return [obj autorelease];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">猜测</h4>
<p>这时候可能会让改变数据的地方只有两个：</p>
<pre><code class="hljs language-objc copyable" lang="objc">  [dict getObjects:objects andKeys:keys];
<span class="hljs-comment">//或者</span>
  <span class="hljs-keyword">id</span> obj = [[<span class="hljs-keyword">self</span> alloc] initWithObjects:objects forKeys:keys count:count];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于上述两个问题笔者都无办法断点到，如果读者大大有办法的话，希望读者大大尝试。笔者根据两个方法的代码进行了自己的<strong>大胆猜测</strong>——也就是瞎猜</p>
<p>很可惜，都没有改掉。在代码中没看到任何一个方法可以做到对 <code>objects</code> 和 <code>keys</code> 的选择遍历。</p>
<h3 data-id="heading-3">CFBasicHashAddValue 和 CFBasicHashSetValue</h3>
<p>看来应该不是其初始化方法的问题，然后笔者比较了字典的 <code>setObject:forKey</code> 的实现。发现如题的两个方法：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function">CF_PRIVATE Boolean <span class="hljs-title">CFBasicHashAddValue</span><span class="hljs-params">(CFBasicHashRef ht, <span class="hljs-keyword">uintptr_t</span> stack_key, <span class="hljs-keyword">uintptr_t</span> stack_value)</span> </span>&#123;
    ···
    CFBasicHashBucket bkt = __CFBasicHashFindBucket(ht, stack_key);
    <span class="hljs-keyword">if</span> (<span class="hljs-number">0</span> < bkt.count) &#123;
        ht->bits.mutations++;
        <span class="hljs-keyword">if</span> (ht->bits.counts_offset && bkt.count < LONG_MAX) &#123; <span class="hljs-comment">// if not yet as large as a CFIndex can be... otherwise clamp and do nothing</span>
            __CFBasicHashIncSlotCount(ht, bkt.idx);
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        __CFBasicHashAddValue(ht, bkt.idx, stack_key, stack_value);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;

<span class="hljs-function">CF_PRIVATE <span class="hljs-keyword">void</span> <span class="hljs-title">CFBasicHashSetValue</span><span class="hljs-params">(CFBasicHashRef ht, <span class="hljs-keyword">uintptr_t</span> stack_key, <span class="hljs-keyword">uintptr_t</span> stack_value)</span> </span>&#123;
    ···
    CFBasicHashBucket bkt = __CFBasicHashFindBucket(ht, stack_key);
    <span class="hljs-keyword">if</span> (<span class="hljs-number">0</span> < bkt.count) &#123;
        __CFBasicHashReplaceValue(ht, bkt.idx, stack_key, stack_value);
    &#125; <span class="hljs-keyword">else</span> &#123;
        __CFBasicHashAddValue(ht, bkt.idx, stack_key, stack_value);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>感觉胜利不远了，因为<code>__CFBasicHashReplaceValue</code> 这个方法语义上是一个替换。那么其本质应该就是 <code>CFBasicHashAddValue</code> ，当存在同值的 key 的时候，并不会再次加入，并且也解释了，最终的结果是设置为前面的值而不是设置在后面的值。</p>
<p>同样你也可以得出下面的值了，欢迎把答案写在评论区哦。</p>
<pre><code class="hljs language-objc copyable" lang="objc">[<span class="hljs-built_in">NSDictionary</span> dictionaryWithObjects:@[@<span class="hljs-number">1</span>,@<span class="hljs-number">2</span>,@<span class="hljs-number">3</span>,@<span class="hljs-number">4</span>,@<span class="hljs-number">5</span>,@<span class="hljs-number">6</span>,@<span class="hljs-number">7</span>,@<span class="hljs-number">8</span>,@<span class="hljs-number">9</span>,@<span class="hljs-number">0</span>] forKeys:@[<span class="hljs-string">@"a"</span>,<span class="hljs-string">@"b"</span>, <span class="hljs-string">@"a"</span>, <span class="hljs-string">@"b"</span>, <span class="hljs-string">@"a"</span>, <span class="hljs-string">@"a"</span>, <span class="hljs-string">@"b"</span>, <span class="hljs-string">@"b"</span>, <span class="hljs-string">@"a"</span>, <span class="hljs-string">@"b"</span>]]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">其他</h3>
<p>在 hook 字典本身的<code>dictionaryWithObjects:forKeys:count:</code> 时，我们需要谨慎断点的时间，包括当不限于系统的状态栏等信息最终都会存进一个字典中，其存入的时机就是项目运行的时候，最好在<code>NSDictionary *dic = @&#123;@"a":@1, @"a":@2&#125;;</code>之前挂上断点，然后在放开<code>dictionaryWithObjects:forKeys:count:</code>  断点。</p>
<hr>
<p>如果你有任何问题、评论或反馈，请随时联系。如果你愿意，可以通过分享这篇文章来让更多的人发现它。</p>
<p>感谢你阅读本文！ 🚀</p></div>  
</div>
            