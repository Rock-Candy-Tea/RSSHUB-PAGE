
---
title: '微信小程序this的挂载&获取闭包函数的this'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb958eadd9dd41138b6312dd5acf8e78~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 21:44:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb958eadd9dd41138b6312dd5acf8e78~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">挂载在页面和组件的this区别</h2>
<h3 data-id="heading-1">挂载在page的this</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">Page(&#123;
    <span class="hljs-attr">something</span>: <span class="hljs-string">"挂载在page的this变量"</span>,

    <span class="hljs-function"><span class="hljs-title">onLoad</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"page this内容"</span>, <span class="hljs-built_in">this</span>);
        <span class="hljs-built_in">this</span>.handleOther();
    &#125;,

    <span class="hljs-function"><span class="hljs-title">handleOther</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb958eadd9dd41138b6312dd5acf8e78~tplv-k3u1fbpfcp-watermark.image" alt="image-20210702112146601" loading="lazy" referrerpolicy="no-referrer"></p>
<p>something和handleOther都有，并且原型proto也存了一份。</p>
<h3 data-id="heading-2">挂载在component的this</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">Component(&#123;
    <span class="hljs-attr">something</span>: <span class="hljs-string">"挂载在component的this变量"</span>,
    <span class="hljs-attr">lifetimes</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">attached</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.componentTest = <span class="hljs-string">"componentTest"</span>;
            <span class="hljs-built_in">this</span>.handleOther();
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"component this内容"</span>, <span class="hljs-built_in">this</span>);        
        &#125;,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">handleOther</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
    &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65e244b5d0d347a795e1f5e31f1ccd34~tplv-k3u1fbpfcp-watermark.image" alt="image-20210702111901448" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只有componentTest变量，没有something变量。且方法存在了原型_proto_上。</p>
<p><strong>影响</strong>：如果认为跟UI渲染相关的数据存储在this.data对象上，而不需要用来渲染的数据，不放在this.data对象的开发者来说（这样某种程度可以加快渲染，减轻this.data的体量）。如果是把数据存储在this对象上，需要区分是page还是compenent：</p>
<ol>
<li>如果是page可以直接Page(&#123;xx: yy&#125;)，这时候可以通过this.xx来获取；</li>
<li>如果是component，不能直接Component(&#123;xx:yy&#125;)，需要在页面初始化的时候，手动绑定在this对象上，如attached() &#123;this.xx = yy;&#125;</li>
</ol>
<h2 data-id="heading-3">小程序Component组件在闭包函数内获取不到正确的this</h2>
<h4 data-id="heading-4">父组件wxml</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">testComponent</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"&#123;&#123;1&#125;&#125;"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">testComponent</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"&#123;&#123;2&#125;&#125;"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">testComponent</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"&#123;&#123;3&#125;&#125;"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">获取不到this的情况</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">Component(&#123;
    <span class="hljs-attr">properties</span>: &#123;
        <span class="hljs-attr">value</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
            <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>,
        &#125;,
    &#125;,

    <span class="hljs-attr">lifetimes</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">attached</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.handleTest(<span class="hljs-built_in">this</span>.data.value);
        &#125;,
    &#125;,

    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-attr">handleTest</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">undefined</span>;
            <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
                <span class="hljs-keyword">if</span> (!instance) &#123;
                    instance = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"test"</span>, value, <span class="hljs-built_in">this</span>);
                    &#125;;
                &#125;
                instance(value);
            &#125;;
        &#125;)(),
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5c3f2aefd0c4d74ae194e2d7ff1023d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210702162827057" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">获取到同一个this的情况</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">Component(&#123;
    <span class="hljs-attr">properties</span>: &#123;
        <span class="hljs-attr">value</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
            <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>,
        &#125;,
    &#125;,
    <span class="hljs-attr">lifetimes</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">attached</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.handleTest(<span class="hljs-built_in">this</span>.data.value);
        &#125;,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-attr">handleTest</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">undefined</span>;
            <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
                <span class="hljs-keyword">if</span> (!instance) &#123;
                    instance = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;<span class="hljs-comment">// 箭头函数创建时确定this指向</span>
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"test"</span>, value, <span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>.data.value);
                    &#125;;
                &#125;
                instance(value);
            &#125;;
        &#125;)(),
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/747a62e6c4e442d28131cd19c88d20ed~tplv-k3u1fbpfcp-watermark.image" alt="image-20210805113348726" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">方案1</h4>
<p>运行时执行闭包函数，在函数外部传递this值给内部函数。</p>
<p>缺点：通过传值的方式，欠缺优雅。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Component(&#123;
    <span class="hljs-attr">properties</span>: &#123;
        <span class="hljs-attr">value</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
            <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>,
        &#125;,
    &#125;,

    <span class="hljs-attr">lifetimes</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">attached</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.handleTest()(<span class="hljs-built_in">this</span>.data.value);<span class="hljs-comment">// 注意点</span>
        &#125;,
    &#125;,

    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-attr">handleTest</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">undefined</span>;
            <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>;<span class="hljs-comment">// 注意点</span>
            <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
                <span class="hljs-keyword">if</span> (!instance) &#123;
                    instance = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"test"</span>, value, that);<span class="hljs-comment">// 注意点</span>
                    &#125;;
                &#125;
                instance(value);
            &#125;;
        &#125;,
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59690b7a82b14454888ff25d0fd1645a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210702161036546" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">方案2</h4>
<p>闭包函数执行时，调用call方法传递this。</p>
<p>缺点：通过传值的方式，欠缺优雅。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Component(&#123;
    <span class="hljs-attr">properties</span>: &#123;
        <span class="hljs-attr">id</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
            <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>,
        &#125;,
    &#125;,

    <span class="hljs-attr">lifetimes</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">attached</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.handleTest(<span class="hljs-built_in">this</span>.id);
        &#125;
    &#125;,
    
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-attr">handleTest</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">undefined</span>;
            <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">id</span>) </span>&#123;
                <span class="hljs-keyword">if</span> (!instance) &#123;
                    instance = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">id</span>) </span>&#123;<span class="hljs-comment">// 注意点</span>
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"test"</span>, id, <span class="hljs-built_in">this</span>);
                    &#125;;
                &#125;
                instance.call(<span class="hljs-built_in">this</span>, id);<span class="hljs-comment">// 注意点</span>
            &#125;;
        &#125;)(),
    &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">方案3</h4>
<p>把instance变量定义成全局的，全局能拿到this。</p>
<p>缺点：instance实际是handleTest函数的业务（内部变量），只会在handleTest函数里面用，没必要定义成全局变量。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Component(&#123;
    <span class="hljs-attr">properties</span>: &#123;
        <span class="hljs-attr">value</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
            <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>,
        &#125;,
    &#125;,

    <span class="hljs-attr">lifetimes</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">attached</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.instance = <span class="hljs-literal">undefined</span>;<span class="hljs-comment">// 注意点</span>
            <span class="hljs-built_in">this</span>.handleTest(<span class="hljs-built_in">this</span>.data.value);
        &#125;
    &#125;,

    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-attr">handleTest</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">// 这里也可以不用再包一层函数</span>
            <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
                <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.instance) &#123;
                    <span class="hljs-built_in">this</span>.instance = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;<span class="hljs-comment">// 注意点</span>
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"test"</span>, value, <span class="hljs-built_in">this</span>);
                    &#125;;
                &#125;
                <span class="hljs-built_in">this</span>.instance(value);<span class="hljs-comment">// 注意点</span>
            &#125;;
        &#125;)(),
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">结合防抖节流函数的几种测试案例</h3>
<p>可以获取到变化的this，但无节流效果（每执行一次handleTest函数都打印一次日志，非3秒内只打印一次）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">handleTest: (<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">undefined</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.instance) &#123;
            instance = ThrottleUtil.throttle(<span class="hljs-number">3000</span>, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'test'</span>, <span class="hljs-built_in">this</span>);
            &#125;);
        &#125;
        instance(value);
    &#125;;
&#125;)(),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过传递this参数，有节流效果，但this获取不到。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">handleTest: (<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> ThrottleUtil.throttle(<span class="hljs-number">3000</span>, <span class="hljs-function">(<span class="hljs-params">value, that</span>) =></span> &#123;<span class="hljs-comment">// 此时的value是小程序action回调函数的evt参数，并不是this.data.value值</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'test'</span>, value, that);
    &#125;);
&#125;)(),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过传递this参数，有节流效果，但this获取不到。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">handleTest: ThrottleUtil.throttle(<span class="hljs-number">3000</span>, <span class="hljs-function">(<span class="hljs-params">value, that</span>) =></span> &#123;<span class="hljs-comment">// 此时的value是小程序action回调函数的evt参数，并不是this.data.value值</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'test'</span>, value, that);
&#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b62b8bb0cd654835a998b4587d946487~tplv-k3u1fbpfcp-watermark.image" alt="image-20210805171802572" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不传递this参数，闭包，有节流效果，this也能正确获取。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">handleTest: (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> instance = <span class="hljs-literal">undefined</span>;
    <span class="hljs-keyword">if</span> (!instance) &#123;
        instance = ThrottleUtil.throttle(
            <span class="hljs-number">3000</span>,
            <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'this'</span>, value, <span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>.data.value);<span class="hljs-comment">// 第一个参数value是小程序action回调函数的evt参数，并不是this.data.value值</span>
            &#125;
        );
    &#125;
    <span class="hljs-keyword">return</span> instance;
&#125;)(),
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e670e1aa9dc4cd5ac76d6260e81d10f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210813180629917" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ThrottleUtil</span> </span>&#123;
    <span class="hljs-comment">/**
     * 节流
     * 每隔一段时间，只执行一次函数。
     * <span class="hljs-doctag">@param </span>delay 判定时间
     * <span class="hljs-doctag">@param </span>action 实际方法
     * <span class="hljs-doctag">@param </span>options 选项对象：
     * &#123;
     *      toggleLastArg // boolean。在delay时间内多次触发的话，是否选择最后一次触发的参数来执行，默认为false（只触发第一次点击）
     * &#125;
     * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> </span>回调，回调实际的方法
     */</span>
    <span class="hljs-keyword">static</span> throttle = <span class="hljs-function">(<span class="hljs-params">delay, action = () => &#123;&#125;, options</span>) =></span> &#123;  <span class="hljs-comment">// 箭头函数</span>
        <span class="hljs-keyword">let</span> last = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">const</span> toggleLastArg = !!(options && options.toggleLastArg);
        <span class="hljs-keyword">let</span> toggleLastArgTimer = <span class="hljs-literal">null</span>;
        <span class="hljs-comment">// eslint-disable-next-line func-names</span>
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;  <span class="hljs-comment">// 匿名函数</span>
            <span class="hljs-keyword">if</span> (toggleLastArgTimer) <span class="hljs-built_in">clearTimeout</span>(toggleLastArgTimer);
            <span class="hljs-keyword">const</span> curr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
            <span class="hljs-keyword">if</span> (curr - last > delay) &#123;
                action.call(<span class="hljs-built_in">this</span>, ...args);  <span class="hljs-comment">// 用call把this绑定在回调函数上</span>
                last = curr;
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (toggleLastArg) &#123;
                toggleLastArgTimer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    action.call(<span class="hljs-built_in">this</span>, ...args);
                &#125;, delay);
            &#125;
        &#125;;
    &#125;

    <span class="hljs-comment">/**
     * 防抖
     * 定义：多次触发事件后，事件处理函数只执行一次，并且是在触发操作结束时执行
     * 原理：对处理函数进行延时操作，若设定的延时到来之前，再次触发事件，则清除上一次的延时操作定时器，重新定时。
     * <span class="hljs-doctag">@param </span>delay 判定时间
     * <span class="hljs-doctag">@param </span>action 实际方法
     * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> </span>回调，回调实际的方法
     */</span>
    <span class="hljs-keyword">static</span> debounce = <span class="hljs-function">(<span class="hljs-params">delay, action = () => &#123;&#125;</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
        <span class="hljs-comment">// eslint-disable-next-line func-names</span>
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (timer) &#123;
                <span class="hljs-built_in">clearTimeout</span>(timer);
            &#125;
            timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                action.call(<span class="hljs-built_in">this</span>, ...args);
            &#125;, delay);
        &#125;;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">参考资料</h5>
<p>bind/call/apply区别：</p>
<p>三个函数存在的区别, 用一句话来说的话就是: bind是返回对应函数(每一次返回一个新函数), 便于稍后调用; apply, call则是立即调用. 除此外, 在 ES6 的箭头函数下, call 和 apply 的this绑定失效，即就算手动call\apply绑定this,也不会改变它的指向。</p>
<p>箭头函数的this:</p>
<ul>
<li>函数体内的 this 对象, 就是定义时所在的对象, 而不是使用时所在的对象;</li>
<li>不可以当作构造函数, 也就是说不可以使用 new 命令, 否则会抛出一个错误;</li>
<li>不可以使用 arguments 对象, 该对象在函数体内不存在. 如果要用, 可以用 Rest 参数代替;</li>
<li>不可以使用 yield 命令, 因此箭头函数不能用作 Generator 函数;</li>
</ul></div>  
</div>
            