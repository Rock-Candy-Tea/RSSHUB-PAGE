
---
title: '深入浅出svelte.js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06b9697b49f540cebdee5701944b6490~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 02:50:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06b9697b49f540cebdee5701944b6490~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>    最近有一个官网页，打算用svelte体验一下，顺便学习了一下svelte(发音：[svelt])，整体来说，svelte是比较简洁的，上手很快。不过与其说是一个前端框架，不如说是一个“dom操作编译器”。svelte的开发代码，在编译阶段会被编译成一系列的dom操作的代码，运行时的代码很少。因此svelte.js的体积很小(只保留了脏值检测更新和封装dom操作API等core代码)。本文从一下几个方面聊一聊对于svelte的认识。</p>
<ul>
<li>svelte初体验</li>
<li>svelte的语法</li>
<li>Virtual Dom和Dom</li>
<li>优缺点</li>
<li>svelte源码阅读</li>
</ul>
<p>原文地址在我的博客： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fforthealllight%2Fblog%2Fissues%2F71" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/forthealllight/blog/issues/71" ref="nofollow noopener noreferrer">github.com/fortheallli…</a></p>
<hr>
<h2 data-id="heading-0">一、svelte初体验</h2>
<p>    我们直接来看官网的例子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06b9697b49f540cebdee5701944b6490~tplv-k3u1fbpfcp-watermark.image" alt="a1" loading="lazy" referrerpolicy="no-referrer"></p>
<p>    实现的功能也很简单，就是两个Input的值求和，然后展示出来。用svelte编写的代码为：</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
        <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>;
</script>

<input type="number" bind:value=&#123;a&#125;>
<input type="number" bind:value=&#123;b&#125;>

<p>&#123;a&#125; + &#123;b&#125; = &#123;a + b&#125;</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    上述代码很简洁，像vue一样也是类似style dom script的三段式写法，不过比vue更加简洁一点，比如dom不需要template包裹等等。</p>
<p>同样的上述的例子的代码如果用react书写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => &#123; 

    <span class="hljs-keyword">const</span> [a, setA] = useState(<span class="hljs-number">1</span>); 
    <span class="hljs-keyword">const</span> [b, setB] = useState(<span class="hljs-number">2</span>); 
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleChangeA</span>(<span class="hljs-params">event</span>) </span>&#123; setA(+event.target.value); &#125; 
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleChangeB</span>(<span class="hljs-params">event</span>) </span>&#123; setB(+event.target.value); &#125;

    <span class="hljs-keyword">return</span> ( 

       <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span> 
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;a&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;handleChangeA&#125;/</span>></span> 
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;b&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;handleChangeB&#125;/</span>></span> 
          <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;a&#125; + &#123;b&#125; = &#123;a + b&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span> 
       <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span> 

    );

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    上述react的写法，必须要先弄懂useState的含义等，此外缺少了默认的双向数据绑定，代码有一点冗余。</p>
<p>    同样的上述的例子的代码如果用vue书写：</p>
<pre><code class="hljs language-js copyable" lang="js"><template> 

    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span> 
       <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span> <span class="hljs-attr">v-model.number</span>=<span class="hljs-string">"a"</span>></span> 
       <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span> <span class="hljs-attr">v-model.number</span>=<span class="hljs-string">"b"</span>></span> 
       <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;a&#125;&#125; + &#123;&#123;b&#125;&#125; = &#123;&#123;a + b&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span> 
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span> 

<span class="hljs-tag"></<span class="hljs-name">template</span>></span> 

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"> 

    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
       <span class="hljs-attr">data</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; 
          <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span> &#125;; 
       &#125; 
    &#125;; 

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>三者对比：</p>

















<table><thead><tr><th>框架名称</th><th>svelte</th><th>react</th><th>vue</th></tr></thead><tbody><tr><td>demo字符数</td><td>145</td><td>445</td><td>263</td></tr></tbody></table>
<p>    单纯的说，svelte编码只需要145个字符，比vue和react少，因此得出说svelte的编码体积更小，这样是不对的，因为svelte会在编译阶段将代码编译到更加贴近dom操作的代码，上述例子的代码，编译后的结果为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* App.svelte generated by Svelte v3.38.3 */</span>

    <span class="hljs-keyword">import</span> &#123;
            SvelteComponent,
            append,
            attr,
            detach,
            element,
            init,
            insert,
            listen,
            noop,
            run_all,
            safe_not_equal,
            set_data,
            set_input_value,
            space,
            text,
            to_number

    &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"svelte/internal"</span>;



    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create_fragment</span>(<span class="hljs-params">ctx</span>) </span>&#123;
            <span class="hljs-keyword">let</span> input0;
            <span class="hljs-keyword">let</span> t0;
            <span class="hljs-keyword">let</span> input1;
            <span class="hljs-keyword">let</span> t1;
            <span class="hljs-keyword">let</span> p;
            <span class="hljs-keyword">let</span> t2;
            <span class="hljs-keyword">let</span> t3;
            <span class="hljs-keyword">let</span> t4;
            <span class="hljs-keyword">let</span> t5;
            <span class="hljs-keyword">let</span> t6_value = <span class="hljs-comment">/*a*/</span> ctx[<span class="hljs-number">0</span>] + <span class="hljs-comment">/*b*/</span> ctx[<span class="hljs-number">1</span>] + <span class="hljs-string">""</span>;
            <span class="hljs-keyword">let</span> t6;
            <span class="hljs-keyword">let</span> mounted;
            <span class="hljs-keyword">let</span> dispose;

            <span class="hljs-keyword">return</span> &#123;

                    <span class="hljs-function"><span class="hljs-title">c</span>(<span class="hljs-params"></span>)</span> &#123;
                            input0 = element(<span class="hljs-string">"input"</span>);
                            t0 = space();
                            input1 = element(<span class="hljs-string">"input"</span>);
                            t1 = space();
                            p = element(<span class="hljs-string">"p"</span>);
                            t2 = text(<span class="hljs-comment">/*a*/</span> ctx[<span class="hljs-number">0</span>]);
                            t3 = text(<span class="hljs-string">" + "</span>);
                            t4 = text(<span class="hljs-comment">/*b*/</span> ctx[<span class="hljs-number">1</span>]);
                            t5 = text(<span class="hljs-string">" = "</span>);
                            t6 = text(t6_value);
                            attr(input0, <span class="hljs-string">"type"</span>, <span class="hljs-string">"number"</span>);
                            attr(input1, <span class="hljs-string">"type"</span>, <span class="hljs-string">"number"</span>);
                    &#125;,

                    <span class="hljs-function"><span class="hljs-title">m</span>(<span class="hljs-params">target, anchor</span>)</span> &#123;
                            insert(target, input0, anchor);
                            set_input_value(input0, <span class="hljs-comment">/*a*/</span> ctx[<span class="hljs-number">0</span>]);
                            insert(target, t0, anchor);
                            insert(target, input1, anchor);
                            set_input_value(input1, <span class="hljs-comment">/*b*/</span> ctx[<span class="hljs-number">1</span>]);
                            insert(target, t1, anchor);
                            insert(target, p, anchor);
                            append(p, t2);
                            append(p, t3);
                            append(p, t4);
                            append(p, t5);
                            append(p, t6);

                            <span class="hljs-keyword">if</span> (!mounted) &#123;
                                    dispose = [
                                            listen(input0, <span class="hljs-string">"input"</span>, <span class="hljs-comment">/*input0_input_handler*/</span> ctx[<span class="hljs-number">2</span>]),
                                            listen(input1, <span class="hljs-string">"input"</span>, <span class="hljs-comment">/*input1_input_handler*/</span> ctx[<span class="hljs-number">3</span>])
                                    ];
                                    mounted = <span class="hljs-literal">true</span>;
                            &#125;

                    &#125;,

                    <span class="hljs-function"><span class="hljs-title">p</span>(<span class="hljs-params">ctx, [dirty]</span>)</span> &#123;

                            <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*a*/</span> <span class="hljs-number">1</span> && to_number(input0.value) !== <span class="hljs-comment">/*a*/</span> ctx[<span class="hljs-number">0</span>]) &#123;
                                    set_input_value(input0, <span class="hljs-comment">/*a*/</span> ctx[<span class="hljs-number">0</span>]);
                            &#125;

                            <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*b*/</span> <span class="hljs-number">2</span> && to_number(input1.value) !== <span class="hljs-comment">/*b*/</span> ctx[<span class="hljs-number">1</span>]) &#123;
                                    set_input_value(input1, <span class="hljs-comment">/*b*/</span> ctx[<span class="hljs-number">1</span>]);

                            &#125;

    

                            <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*a*/</span> <span class="hljs-number">1</span>) set_data(t2, <span class="hljs-comment">/*a*/</span> ctx[<span class="hljs-number">0</span>]);

                            <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*b*/</span> <span class="hljs-number">2</span>) set_data(t4, <span class="hljs-comment">/*b*/</span> ctx[<span class="hljs-number">1</span>]);

                            <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*a, b*/</span> <span class="hljs-number">3</span> && t6_value !== (t6_value = <span class="hljs-comment">/*a*/</span> ctx[<span class="hljs-number">0</span>] + <span class="hljs-comment">/*b*/</span> ctx[<span class="hljs-number">1</span>] + <span class="hljs-string">""</span>)) set_data(t6, t6_value);

                    &#125;,

                    <span class="hljs-attr">i</span>: noop,

                    <span class="hljs-attr">o</span>: noop,

                    <span class="hljs-function"><span class="hljs-title">d</span>(<span class="hljs-params">detaching</span>)</span> &#123;

                            <span class="hljs-keyword">if</span> (detaching) detach(input0);

                            <span class="hljs-keyword">if</span> (detaching) detach(t0);

                            <span class="hljs-keyword">if</span> (detaching) detach(input1);

                            <span class="hljs-keyword">if</span> (detaching) detach(t1);

                            <span class="hljs-keyword">if</span> (detaching) detach(p);

                            mounted = <span class="hljs-literal">false</span>;

                            run_all(dispose);

                    &#125;

            &#125;;

    &#125;

    

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">instance</span>(<span class="hljs-params">$$self, $$props, $$invalidate</span>) </span>&#123;

            <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;

            <span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>;

            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">input0_input_handler</span>(<span class="hljs-params"></span>) </span>&#123;

                    a = to_number(<span class="hljs-built_in">this</span>.value);

                    $$invalidate(<span class="hljs-number">0</span>, a);

            &#125;

            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">input1_input_handler</span>(<span class="hljs-params"></span>) </span>&#123;

                    b = to_number(<span class="hljs-built_in">this</span>.value);

                    $$invalidate(<span class="hljs-number">1</span>, b);

            &#125;
            <span class="hljs-keyword">return</span> [a, b, input0_input_handler, input1_input_handler];

    &#125;

    
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SvelteComponent</span> </span>&#123;
            <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
                    <span class="hljs-built_in">super</span>();
                    init(<span class="hljs-built_in">this</span>, options, instance, create_fragment, safe_not_equal, &#123;&#125;);
            &#125;

    &#125;

    

    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    在编译后生成的代码其实代码量也不小，是远远大于145个字符的，<strong>也不能说因为编译后的代码量大，所以说svelte有点名不副实，并不能减少运行时代码的体积</strong>。要考虑到svelte的运行时代码是很少的.我们来对比一下：</p>



















<table><thead><tr><th>框架名称</th><th>react</th><th>vue</th><th>angular</th><th>svelte</th></tr></thead><tbody><tr><td>体积</td><td>42k</td><td>22k</td><td>89.5k</td><td>1.6k</td></tr></tbody></table>
<p>    从上述对比中可以看出，svelte的体积很少，虽然其业务代码在编译后会生产较多的代码。<strong>得益于较少的运行时代码。虽然svelte代码的随着业务的编写增量速度比较快，得益于其很小的包体积1.6k，对于一般中小型项目而言，整体运行的代码（编译后的代码+包体积）还是比较小的</strong>，所以可以说svelte项目的代码较小。不过对于大型项目而言，因为svelte随着业务的进行，运行时代码增量陡峭，大型项目体积并不会比react、vue等小,因此需要辩证看待。</p>
<p>    此外虽说svelte的代码在编译后体积很大，但是在编译前的代码，其实很简洁，这种简洁，一定程度上，可以增强开发体验。</p>
<h2 data-id="heading-1">二、 svelte的语法</h2>
<p>    svelte的写法跟vue有点类似，是指令式和响应式的。</p>
<ol>
<li>
<h4 data-id="heading-2">基本用法</h4>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><script>
    <span class="hljs-keyword">let</span> name = <span class="hljs-string">'world'</span>;
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;name&#125;!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">

  <span class="hljs-selector-tag">h1</span>&#123;

    <span class="hljs-attribute">color</span>:red

  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个最简单的hello world的例子，上述代码中很简洁。在编译后的代码分为js编译和css编译。</p>
<ul>
<li>js编译</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* App.svelte generated by Svelte v3.38.3 */</span>

<span class="hljs-keyword">import</span> &#123;

        SvelteComponent,

        attr,

        detach,

        element,

        init,

        insert,

        noop,

        safe_not_equal

&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"svelte/internal"</span>;



<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create_fragment</span>(<span class="hljs-params">ctx</span>) </span>&#123;

        <span class="hljs-keyword">let</span> h1;



        <span class="hljs-keyword">return</span> &#123;

                <span class="hljs-function"><span class="hljs-title">c</span>(<span class="hljs-params"></span>)</span> &#123;

                        h1 = element(<span class="hljs-string">"h1"</span>);

                        h1.textContent = <span class="hljs-string">`Hello <span class="hljs-subst">$&#123;name&#125;</span>!`</span>;

                        attr(h1, <span class="hljs-string">"class"</span>, <span class="hljs-string">"svelte-khrn1o"</span>);

                &#125;,

                <span class="hljs-function"><span class="hljs-title">m</span>(<span class="hljs-params">target, anchor</span>)</span> &#123;

                        insert(target, h1, anchor);

                &#125;,

                <span class="hljs-attr">p</span>: noop,

                <span class="hljs-attr">i</span>: noop,

                <span class="hljs-attr">o</span>: noop,

                <span class="hljs-function"><span class="hljs-title">d</span>(<span class="hljs-params">detaching</span>)</span> &#123;

                        <span class="hljs-keyword">if</span> (detaching) detach(h1);

                &#125;

        &#125;;

&#125;



<span class="hljs-keyword">let</span> name = <span class="hljs-string">"world"</span>;



<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SvelteComponent</span> </span>&#123;

        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;

                <span class="hljs-built_in">super</span>();

                init(<span class="hljs-built_in">this</span>, options, <span class="hljs-literal">null</span>, create_fragment, safe_not_equal, &#123;&#125;);

        &#125;

&#125;



<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>svelte/internal包中是一些封装了dom操作的函数。</p>
<ul>
<li>
<p>css编译结果：</p>
<pre><code class="hljs language-js copyable" lang="js">h1.svelte-khrn1o&#123;<span class="hljs-attr">color</span>:red&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>css是通过创建style标签引入到最后的dom中的。</p>
<ol start="2">
<li>
<h4 data-id="heading-3">指令形式和数据绑定</h4>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><script>

    <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;

    <span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>;

    $: total =  a+b

</script>



<input type="number" bind:value=&#123;a&#125;>

<input type="number" bind:value=&#123;b&#125;>

<p>&#123;a&#125; + &#123;b&#125; = &#123;total&#125;</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是以上面的例子为例，上述就是一个指令形式+数据绑定的形式。跟vue的写法很相似，改例子绑定了input和a, input和b.效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b623972f2dd4e3d9acd4c198c16e186~tplv-k3u1fbpfcp-watermark.image" alt="a2" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的$total: 就是reactive statement. 类似vue中的计算属性。</p>
<ol start="3">
<li>
<h4 data-id="heading-4">组件compose</h4>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Name.svelte</span>

<script lang=<span class="hljs-string">'typescript'</span>>

    <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> name = <span class="hljs-string">"yuxl"</span>

</script>



<span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span>></span>

    &#123;name&#125;

<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>



<span class="hljs-comment">//Age.svelte</span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'typescript'</span>></span><span class="javascript">

    <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> age = <span class="hljs-number">18</span>

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>



<span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span>></span>

    &#123;age&#125;

<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>



<span class="hljs-comment">//index.svelte</span>



<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">import</span> Name <span class="hljs-keyword">from</span> <span class="hljs-string">'./Name.svelte'</span>

<span class="hljs-keyword">import</span> Age <span class="hljs-keyword">from</span> <span class="hljs-string">'./Age.svelte'</span> 

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>



<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>

   <span class="hljs-tag"><<span class="hljs-name">Name</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"some name"</span>/></span>

   <span class="hljs-tag"><<span class="hljs-name">Age</span> <span class="hljs-attr">age</span> = <span class="hljs-string">&#123;20&#125;</span> /></span>

<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在svelte中的组件的compose也是跟react中类似的，不同的是在react中export的属性就是组件的props，写法上比较简洁，此外，export const 和export function、export class这3个组件的props是只读的，不可写。</p>
<ol start="4">
<li>
<h4 data-id="heading-5">模版语法</h4>
</li>
</ol>
<p>    在svelte中，html相关的场景适用于模版语法，最简单的模版语法为：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;#<span class="hljs-keyword">if</span> answer === <span class="hljs-number">42</span>&#125; <p>what was the question?<<span class="hljs-regexp">/p> &#123;/i</span>f&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    这里介绍几个在svelte中几个比较有趣的模版语法。</p>
<ul>
<li>@debug</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script>  

    <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> name = <span class="hljs-string">"yuxl"</span>

</script>

 &#123;@debug name&#125;

  <span>

    &#123;name&#125;

  </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行debugger的结果为：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d3011e00b9447869396311b7a48eb13~tplv-k3u1fbpfcp-watermark.image" alt="a3" loading="lazy" referrerpolicy="no-referrer">
@debug 在后面跟的参数name发生变化的时候会进行debugger，从上图我们看到debugger的地方上下文的代码是编译后运行时，跟编码的时候有一点区别，也进一步说明，svelte可以看作是一个前端的编译框架，真正运行时的代码是编译后的结果。</p>
<ul>
<li>@html</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script lang=<span class="hljs-string">'typescript'</span>>

    <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> name = <span class="hljs-string">"yuxl"</span>

    <span class="hljs-keyword">const</span> age = <span class="hljs-string">'<span>20</span>'</span>

</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>

    &#123;@html age&#125;

<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>#await
用法为：&#123;#await expression&#125;...&#123;:then name&#125;...&#123;:catch name&#125;...&#123;/await&#125;</p>
<pre><code class="hljs language-js copyable" lang="js"><script lang=<span class="hljs-string">'typescript'</span>>

  <span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>)=></span>&#123;

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;

        resolve(<span class="hljs-string">"success"</span>)

    &#125;,<span class="hljs-number">2000</span>)

  &#125;)
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>

  &#123;#await promise&#125;

  <span class="hljs-comment"><!-- promise is pending --></span>

  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>waiting for the promise to resolve...<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

  &#123;:then value&#125;

      <span class="hljs-comment"><!-- promise was fulfilled --></span>

      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>The value is &#123;value&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

  &#123;/await&#125;

<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<ol start="5">
<li>
<h4 data-id="heading-6">动画效果</h4>
</li>
</ol>
<p>    在svelte中，对于原始的dom元素，自带了一些动画指令，在一般的官网或者活动页中，场景最多的就是动画效果，svelte自带的动画指令，因此在写官网的时候方便了不少。</p>
<p>以transition:fly为例：</p>
<pre><code class="hljs language-js copyable" lang="js"><script>

    <span class="hljs-keyword">import</span> &#123; fly &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;

    <span class="hljs-keyword">let</span> visible = <span class="hljs-literal">true</span>;

</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">label</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">bind:checked</span>=<span class="hljs-string">&#123;visible&#125;</span>></span>
    visible
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>



&#123;#if visible&#125;

    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">transition:fly</span>=<span class="hljs-string">"&#123;&#123; y: 200, duration: 2000 &#125;&#125;"</span>></span>
            Flies in and out
    <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;/if&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>最后的结果为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f07c2e4fd20e41638c943949d602d298~tplv-k3u1fbpfcp-watermark.image" alt="a4" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然在svelte中也支持自定义动画指令。</p>
<ol start="6">
<li>
<h4 data-id="heading-7">组件的生命周期</h4>
</li>
</ol>
<p>    svelte组件也提供了完整的生命周期。onMount、<code>beforeUpdate</code>、<code>afterUpdate</code>、<code>onDestroy</code>等。见名思意，这里不一一介绍，跟react & vue的组件生命周期近似。</p>
<p><strong>除了上述之外，svelte还支持自定义元素(custom element)， store以及context等等</strong>。</p>
<h2 data-id="heading-8">三、Virtual Dom和Dom</h2>
<p>    这个其实可以，比较客观的去看待，svelte的作者认为，Virtual Dom的性能并没有太大的问题，不管是diff算法还是render的过程都没有什么性能问题，不过作者认为，svelte不需要diff，还是有一点优势的。<strong>虽然<strong><strong>diff</strong></strong>很快，但是没有diff的话，显然会更快的得到渲染结果</strong>。</p>
<p>    svelte的编译后的结果来看，所有的dom的变动都变为了直接的dom操作行为，是不需要做diff的，这种方法，没有diff/patch，因此从速度来看，肯定更快一些。 比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><script>

<span class="hljs-keyword">import</span> &#123; fade &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"svelte/transition"</span>;

<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">false</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;

    visible = <span class="hljs-literal">true</span>

&#125;

</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>点击<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    &#123;#if visible&#125;

        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">transition:fade</span> =<span class="hljs-string">"&#123;&#123; duration: 2000 &#125;&#125;"</span> ></span>

            fades in and out

        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    &#123;/if&#125;

<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述这个例子中，修改了visible，编译后的代码知道这个行为，这是一个确定的会如何影响dom的行为，编译后的结果部分为：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86a1e40cf9554f25ba913098538e1de6~tplv-k3u1fbpfcp-watermark.image" alt="a5" loading="lazy" referrerpolicy="no-referrer"></p>
<p>    可以看到，state的改变如何影响dom在svelte的编译结果中都是很确定的。</p>
<p>    除了性能问题，svelte的作者认为，因为virtualDom的存在，需要保存new object和old object的虚拟dom对象，在react的编程中，每一次渲染都有这两个对象，这两个对象，在正常的开发中，很容易添加一些冗余代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MoreRealisticComponent</span>(<span class="hljs-params">props</span>) </span>&#123;

          <span class="hljs-keyword">const</span> [selected, setSelected] = useState(<span class="hljs-literal">null</span>);

          <span class="hljs-keyword">return</span> (

            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>

              <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Selected &#123;selected ? selected.name : 'nothing'&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

        

              <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>

                &#123;props.items.map(item =>

                  <span class="hljs-tag"><<span class="hljs-name">li</span>></span>

                    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setSelected(item)&#125;>

                      &#123;item.name&#125;

                    <span class="hljs-tag"></<span class="hljs-name">button</span>></span>

                  <span class="hljs-tag"></<span class="hljs-name">li</span>></span>

                )&#125;

              <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

          );

    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    在这个例子中，为每一个li都绑定了一个事件，这是不过度优化情况下的正常下发，因为virtualDom虚拟dom的存在，每一次state更新的时候，每一个new object和old object都包含了每一个li的绑定函数，这些是冗余的代码，增加了代码的体积等。</p>
<h2 data-id="heading-9">四、优缺点</h2>
<p>个人归纳了一下几个优缺点：</p>
<ul>
<li>
<p>优点：</p>
<ol>
<li>体积很小，是真的小，包体积只有1.6k，对于小型项目比如官网首页，活动页等确实可以拿来试试。上手也很快，很轻量级。类似活动页这种简单页面的lowcoder系统，也可以尝试一下，因为框架本身提供的api,应该是目前前端框架里面最简单的。</li>
<li>no virtual dom的形式一定程度上确实要快一些，没有了diff/path</li>
</ol>
</li>
<li>
<p>缺点</p>
<ol>
<li>虽然包的体积小，但是编译后的代码其实并不小，代码总量的增加曲线其实还是有一定陡峭的。在大型项目中没有证明自己。</li>
<li>生态问题，生态其实并不是很完善，虽然类似的比如组件库之类的都有，但是没有很完善。</li>
</ol>
<h2 data-id="heading-10">五、源码阅读</h2>
</li>
</ul>
<p>    首先svelte的源码分为两部分，compiler和runtime，compiler主要的作用是将开发代码编译成运行时的代码，具体如何编译不是本文所要关注的代码。本文主要关注的是编译后的运行时的代码runtime。</p>
<ol>
<li>
<h4 data-id="heading-11">dom操作相关core api</h4>
</li>
</ol>
<p>我们以最简单的hello world为例：
<strong>svelte编译前源码：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><h1>Hello world!</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>svelte编译后的代码</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;

        SvelteComponent,

        detach,

        element,

        init,

        insert,

        noop,

        safe_not_equal

&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"svelte/internal"</span>;



<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create_fragment</span>(<span class="hljs-params">ctx</span>) </span>&#123;

        <span class="hljs-keyword">let</span> h1;



        <span class="hljs-keyword">return</span> &#123;

                <span class="hljs-function"><span class="hljs-title">c</span>(<span class="hljs-params"></span>)</span> &#123;

                        h1 = element(<span class="hljs-string">"h1"</span>);

                        h1.textContent = <span class="hljs-string">"Hello world!"</span>;

                &#125;,

                <span class="hljs-function"><span class="hljs-title">m</span>(<span class="hljs-params">target, anchor</span>)</span> &#123;

                        insert(target, h1, anchor);

                &#125;,

                <span class="hljs-attr">p</span>: noop,

                <span class="hljs-attr">i</span>: noop,

                <span class="hljs-attr">o</span>: noop,

                <span class="hljs-function"><span class="hljs-title">d</span>(<span class="hljs-params">detaching</span>)</span> &#123;

                        <span class="hljs-keyword">if</span> (detaching) detach(h1);

                &#125;

        &#125;;

&#125;



<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SvelteComponent</span> </span>&#123;

        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;

                <span class="hljs-built_in">super</span>();

                init(<span class="hljs-built_in">this</span>, options, <span class="hljs-literal">null</span>, create_fragment, safe_not_equal, &#123;&#125;);

        &#125;

&#125;



<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的App就可以直接使用了，比如渲染到一个父dom中可以这样使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.svelte'</span>



<span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> App(&#123;

  <span class="hljs-attr">target</span>: <span class="hljs-built_in">document</span>.body,

&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> app;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述方法就可以把App这个编译后的运行时组件渲染到body中，我们来看编译后的代码。</p>
<ul>
<li>create_fragment</li>
</ul>
<p>在svelte组件中，与dom相关的部分封装在了create_fragment中，该函数创建了一个Fragment, 该函数返回一个包含dom操作的对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface Fragment &#123;

        <span class="hljs-attr">key</span>: string|<span class="hljs-literal">null</span>;

        first: <span class="hljs-literal">null</span>;

        <span class="hljs-comment">/* create  */</span> c: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* claim   */</span> l: <span class="hljs-function">(<span class="hljs-params">nodes: any</span>) =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* hydrate */</span> h: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* mount   */</span> m: <span class="hljs-function">(<span class="hljs-params">target: HTMLElement, anchor: any</span>) =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* update  */</span> p: <span class="hljs-function">(<span class="hljs-params">ctx: any, dirty: any</span>) =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* measure */</span> r: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* fix     */</span> f: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* animate */</span> a: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* intro   */</span> i: <span class="hljs-function">(<span class="hljs-params">local: any</span>) =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* outro   */</span> o: <span class="hljs-function">(<span class="hljs-params">local: any</span>) =></span> <span class="hljs-keyword">void</span>;

        <span class="hljs-comment">/* destroy */</span> d: <span class="hljs-function">(<span class="hljs-params">detaching: <span class="hljs-number">0</span>|<span class="hljs-number">1</span></span>) =></span> <span class="hljs-keyword">void</span>;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述的例子中，c对应创建一个子dom元素，m表示创建元素要渲染元素时需要执行的函数，d表示删除元素时的操作。上述的例子中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create_fragment</span>(<span class="hljs-params">ctx</span>) </span>&#123;

        <span class="hljs-keyword">let</span> h1;



        <span class="hljs-keyword">return</span> &#123;

                <span class="hljs-function"><span class="hljs-title">c</span>(<span class="hljs-params"></span>)</span> &#123;

                        h1 = element(<span class="hljs-string">"h1"</span>);

                        h1.textContent = <span class="hljs-string">"Hello world!"</span>;

                &#125;,

                <span class="hljs-function"><span class="hljs-title">m</span>(<span class="hljs-params">target, anchor</span>)</span> &#123;

                        insert(target, h1, anchor);

                &#125;,

                <span class="hljs-attr">p</span>: noop,

                <span class="hljs-attr">i</span>: noop,

                <span class="hljs-attr">o</span>: noop,

                <span class="hljs-function"><span class="hljs-title">d</span>(<span class="hljs-params">detaching</span>)</span> &#123;

                        <span class="hljs-keyword">if</span> (detaching) detach(h1);

                &#125;

        &#125;;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在m中的intert和d中的detach方法，都是原生的dom操作方法，上述Fragment的意思是创建了h1这个dom，并在渲染的时候插入到目标dom节点中，在Fragment这个组件元素被销毁的时候，销毁被创建的子dom元素 h1。</p>
<p>element、insert、detach等方法都是原生的dom操作，具体源码如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">element</span><<span class="hljs-title">K</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">HTMLElementTagNameMap</span>>(<span class="hljs-params">name: K</span>) </span>&#123;

        <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement<K>(name);

&#125;



<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insert</span>(<span class="hljs-params">target: NodeEx, node: NodeEx, anchor?: NodeEx</span>) </span>&#123;

        target.insertBefore(node, anchor || <span class="hljs-literal">null</span>);

&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">detach</span>(<span class="hljs-params">node: Node</span>) </span>&#123;

        node.parentNode.removeChild(node);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>SvelteComponent</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SvelteComponent</span> </span>&#123;

        <span class="hljs-attr">$$</span>: T$$;

        $$set?: <span class="hljs-function">(<span class="hljs-params">$$props: any</span>) =></span> <span class="hljs-keyword">void</span>;



        $destroy() &#123;

                destroy_component(<span class="hljs-built_in">this</span>, <span class="hljs-number">1</span>);

                <span class="hljs-built_in">this</span>.$destroy = noop;

        &#125;



        $on(type, callback) &#123;

                <span class="hljs-keyword">const</span> callbacks = (<span class="hljs-built_in">this</span>.$$.callbacks[type] || (<span class="hljs-built_in">this</span>.$$.callbacks[type] = []));

                callbacks.push(callback);



                <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;

                        <span class="hljs-keyword">const</span> index = callbacks.indexOf(callback);

                        <span class="hljs-keyword">if</span> (index !== -<span class="hljs-number">1</span>) callbacks.splice(index, <span class="hljs-number">1</span>);

                &#125;;

        &#125;



        $set($$props) &#123;

                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$$set && !is_empty($$props)) &#123;

                        <span class="hljs-built_in">this</span>.$$.skip_bound = <span class="hljs-literal">true</span>;

                        <span class="hljs-built_in">this</span>.$$set($$props);

                        <span class="hljs-built_in">this</span>.$$.skip_bound = <span class="hljs-literal">false</span>;

                &#125;

        &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SvelteComponent组件定义了如何销毁组件以及如何设置组件的属性，以及如何增加监听函数，其中最重要的是定义了组件的实例属性 .</p>
<pre><code class="hljs language-js copyable" lang="js">interface T$$ &#123;

        <span class="hljs-attr">dirty</span>: number[];

        ctx: <span class="hljs-literal">null</span>|any;

        bound: any;

        update: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>;

        callbacks: any;

        after_update: any[];

        props: Record<string, <span class="hljs-number">0</span> | string>;

        fragment: <span class="hljs-literal">null</span>|<span class="hljs-literal">false</span>|Fragment;

        not_equal: any;

        before_update: any[];

        context: <span class="hljs-built_in">Map</span><any, any>;

        on_mount: any[];

        on_destroy: any[];

        skip_bound: boolean;

        on_disconnect: any[];

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现SvelteComponent组件确实包含了ctx上下文内容，以及组件的生命周期属性，以及组件的脏值检测等相关的属性。</p>
<ul>
<li>
<p>init函数
`js
export function init(component, options, instance, create_fragment, not_equal, props, dirty = [-1]) &#123;</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> parent_component = current_component;

  set_current_component(component);



  <span class="hljs-keyword">const</span> $$: T$$ = component.$$ = &#123;

          <span class="hljs-attr">fragment</span>: <span class="hljs-literal">null</span>,

          <span class="hljs-attr">ctx</span>: <span class="hljs-literal">null</span>,



          <span class="hljs-comment">// state</span>

          props,

          <span class="hljs-attr">update</span>: noop,

          not_equal,

          <span class="hljs-attr">bound</span>: blank_object(),



          <span class="hljs-comment">// lifecycle</span>

          <span class="hljs-attr">on_mount</span>: [],

          <span class="hljs-attr">on_destroy</span>: [],

          <span class="hljs-attr">on_disconnect</span>: [],

          <span class="hljs-attr">before_update</span>: [],

          <span class="hljs-attr">after_update</span>: [],

          <span class="hljs-attr">context</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(parent_component ? parent_component.$$.context : options.context || []),



          <span class="hljs-comment">// everything else</span>

          <span class="hljs-attr">callbacks</span>: blank_object(),

          dirty,

          <span class="hljs-attr">skip_bound</span>: <span class="hljs-literal">false</span>

  &#125;;



  <span class="hljs-keyword">let</span> ready = <span class="hljs-literal">false</span>;



  $$.ctx = instance

          ? instance(component, options.props || &#123;&#125;, <span class="hljs-function">(<span class="hljs-params">i, ret, ...rest</span>) =></span> &#123;

                  <span class="hljs-keyword">const</span> value = rest.length ? rest[<span class="hljs-number">0</span>] : ret;

                  <span class="hljs-keyword">if</span> ($$.ctx && not_equal($$.ctx[i], $$.ctx[i] = value)) &#123;

                          <span class="hljs-keyword">if</span> (!$$.skip_bound && $$.bound[i]) $$.bound[i](value);

                          <span class="hljs-keyword">if</span> (ready) make_dirty(component, i);

                  &#125;

                  <span class="hljs-keyword">return</span> ret;

          &#125;)

          : [];



  $$.update();

  ready = <span class="hljs-literal">true</span>;

  run_all($$.before_update);



  <span class="hljs-comment">// `false` as a special case of no DOM component</span>

  $$.fragment = create_fragment ? create_fragment($$.ctx) : <span class="hljs-literal">false</span>;



  <span class="hljs-keyword">if</span> (options.target) &#123;

      flush();

  &#125;



  set_current_component(parent_component);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>init函数在SvelteComponent组件内部调用，用于实例属性的初始化。这里最重要的是$$.ctx的赋值部分，后续会用来做脏值检测。ctx中保存了所有的再多次渲染中都存在的值，包含了内部的state以及监听处理函数等等。</p>
<ol start="2">
<li>
<h4 data-id="heading-12">脏值检测和更新部分</h4>
</li>
</ol>
</li>
</ul>
<p>这里我们以一个带有鼠标时间的svelte组件为例，</p>
<p>编译前的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><script>

        <span class="hljs-keyword">let</span> m = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">0</span> &#125;;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleMousemove</span>(<span class="hljs-params">event</span>) </span>&#123;

                m.x = event.clientX;

                m.y = event.clientY;

        &#125;

</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">on:mousemove</span>=<span class="hljs-string">&#123;handleMousemove&#125;</span>></span>

        The mouse position is &#123;m.x&#125; x &#123;m.y&#125;

<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>svelte编译后的代码与hello world相比增加的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create_fragment</span>(<span class="hljs-params">ctx</span>) </span>&#123;

        <span class="hljs-keyword">let</span> div;

        <span class="hljs-keyword">let</span> t0;

        <span class="hljs-keyword">let</span> t1_value = <span class="hljs-comment">/*m*/</span> ctx[<span class="hljs-number">0</span>].x + <span class="hljs-string">""</span>;

        <span class="hljs-keyword">let</span> t1;

        <span class="hljs-keyword">let</span> t2;

        <span class="hljs-keyword">let</span> t3_value = <span class="hljs-comment">/*m*/</span> ctx[<span class="hljs-number">0</span>].y + <span class="hljs-string">""</span>;

        <span class="hljs-keyword">let</span> t3;

        <span class="hljs-keyword">return</span> &#123;

               ...

                <span class="hljs-function"><span class="hljs-title">p</span>(<span class="hljs-params">ctx, [dirty]</span>)</span> &#123;

                        <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*m*/</span> <span class="hljs-number">1</span> && t1_value !== (t1_value = <span class="hljs-comment">/*m*/</span> ctx[<span class="hljs-number">0</span>].x + <span class="hljs-string">""</span>)) set_data(t1, t1_value);

                        <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*m*/</span> <span class="hljs-number">1</span> && t3_value !== (t3_value = <span class="hljs-comment">/*m*/</span> ctx[<span class="hljs-number">0</span>].y + <span class="hljs-string">""</span>)) set_data(t3, t3_value);

                &#125;,

               ...

        &#125;;

&#125;



<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">instance</span>(<span class="hljs-params">$$self, $$props, $$invalidate</span>) </span>&#123;

        <span class="hljs-keyword">let</span> m = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">0</span> &#125;;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleMousemove</span>(<span class="hljs-params">event</span>) </span>&#123;

                $$invalidate(<span class="hljs-number">0</span>, m.x = event.clientX, m);

                $$invalidate(<span class="hljs-number">0</span>, m.y = event.clientY, m);

        &#125;

        <span class="hljs-keyword">return</span> [m, handleMousemove];

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里多了一个instance函数，而这个instance函数在svelteComponent的init函数中就是用作脏值检测和更新的。</p>
<pre><code class="hljs language-js copyable" lang="js">$$.ctx = instance

    ? instance(component, options.props || &#123;&#125;, <span class="hljs-function">(<span class="hljs-params">i, ret, ...rest</span>) =></span> &#123;

            <span class="hljs-keyword">const</span> value = rest.length ? rest[<span class="hljs-number">0</span>] : ret;

            <span class="hljs-keyword">if</span> ($$.ctx && not_equal($$.ctx[i], $$.ctx[i] = value)) &#123;

                    <span class="hljs-keyword">if</span> (!$$.skip_bound && $$.bound[i]) $$.bound[i](value);

                    <span class="hljs-keyword">if</span> (ready) make_dirty(component, i);

            &#125;

            <span class="hljs-keyword">return</span> ret;

    &#125;)

    : [];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果值发生了变动，就触发make_dirty函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">make_dirty</span>(<span class="hljs-params">component, i</span>) </span>&#123;

        <span class="hljs-keyword">if</span> (component.$$.dirty[<span class="hljs-number">0</span>] === -<span class="hljs-number">1</span>) &#123;

                dirty_components.push(component);

                schedule_update();

                component.$$.dirty.fill(<span class="hljs-number">0</span>);

        &#125;

        component.$$.dirty[(i / <span class="hljs-number">31</span>) | <span class="hljs-number">0</span>] |= (<span class="hljs-number">1</span> << (i % <span class="hljs-number">31</span>));

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>make_dirty标记了哪一些脏组件，然后对脏组件执行schedule_update方法来更新组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">schedule_update</span>(<span class="hljs-params"></span>) </span>&#123;

        <span class="hljs-keyword">if</span> (!update_scheduled) &#123;

                update_scheduled = <span class="hljs-literal">true</span>;

                resolved_promise.then(flush);

        &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>schedule_update在需要更新时候，在下一个微任务重执行flush：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flush</span>(<span class="hljs-params"></span>) </span>&#123;

        <span class="hljs-keyword">if</span> (flushing) <span class="hljs-keyword">return</span>;

        flushing = <span class="hljs-literal">true</span>;

        <span class="hljs-keyword">do</span> &#123;

                <span class="hljs-comment">// first, call beforeUpdate functions</span>

                <span class="hljs-comment">// and update components</span>

                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < dirty_components.length; i += <span class="hljs-number">1</span>) &#123;

                        <span class="hljs-keyword">const</span> component = dirty_components[i];

                        set_current_component(component);

                        update(component.$$);

                &#125;

                set_current_component(<span class="hljs-literal">null</span>);

                ...

                render_callbacks.length = <span class="hljs-number">0</span>;

        &#125; <span class="hljs-keyword">while</span> (dirty_components.length);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简化后的flush方法如上所示，就是遍历整个脏组件，执行所有的脏组件中的更新方法update.update方法的定义为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">$$</span>) </span>&#123;

        <span class="hljs-keyword">if</span> ($$.fragment !== <span class="hljs-literal">null</span>) &#123;

                $$.update();

                run_all($$.before_update);

                <span class="hljs-keyword">const</span> dirty = $$.dirty;

                $$.dirty = [-<span class="hljs-number">1</span>];

                $$.fragment && $$.fragment.p($$.ctx, dirty);



                $$.after_update.forEach(add_render_callback);

        &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>update方法标记自身组件为脏，并且制定自身组件fragment中的p(全名：update）也就是前面的fragment中的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">p</span>(<span class="hljs-params">ctx, [dirty]</span>)</span> &#123;

                        <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*m*/</span> <span class="hljs-number">1</span> && t1_value !== (t1_value = <span class="hljs-comment">/*m*/</span> ctx[<span class="hljs-number">0</span>].x + <span class="hljs-string">""</span>)) set_data(t1, t1_value);

                        <span class="hljs-keyword">if</span> (dirty & <span class="hljs-comment">/*m*/</span> <span class="hljs-number">1</span> && t3_value !== (t3_value = <span class="hljs-comment">/*m*/</span> ctx[<span class="hljs-number">0</span>].y + <span class="hljs-string">""</span>)) set_data(t3, t3_value);

                &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在p方法中，直接操作dom改变UI。</p>
<p>总结来看，组件更新的步骤为以下几步：</p>
<ol>
<li>事件或者其他操作出发更新流程</li>
<li>在instance的$$invalidate方法中，比较操作前后ctx中的值有没有发生改变，如果发生改变则继续往下</li>
<li>执行make_dirty函数标记为脏值，添加带有脏值需要更新的组件，从而继续触发更新</li>
<li>执行schedule_update函数</li>
<li>执行flush函数，将所有的脏值组件取出，以此执行其update方法</li>
<li>在update方法中，执行的是Fragment自身的p方法，p方法做的事情就是确定需要更新组件，并操作和更新dom组件，从而完成了最后的流程</li>
</ol></div>  
</div>
            