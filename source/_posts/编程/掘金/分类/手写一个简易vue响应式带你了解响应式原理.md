
---
title: '手写一个简易vue响应式带你了解响应式原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ad4d2fcc15f47d9a3df0db8878ffba5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 21:42:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ad4d2fcc15f47d9a3df0db8878ffba5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<blockquote>
<p>这是小浪在学习<strong>Vue</strong>总结的一篇文章，在这篇文章我们来了解 <strong>Vue2.X</strong> 响应式原理，然后我们来实现一个 <strong>vue</strong> 响应式原理（写的内容简单）实现步骤和注释写的很清晰，大家有兴趣可以耐心观看，大家可以在评论多多交流，也希望大家能给 小浪一个 <strong>赞</strong></p>
</blockquote>
<h1 data-id="heading-1">Vue2.X响应式原理</h1>
<h2 data-id="heading-2">1.defineProperty 的应用</h2>
<p>在<strong>Vue2.X</strong> 响应式中使用到了 <strong>defineProperty</strong>  进行数据劫持，所以我们对它必须有一定的了解，那么我们先来了解它的使用方法把， 这里我们来使用 <strong>defineProperty</strong>来模拟 <strong>Vue</strong> 中的 <strong>data</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-comment">// 模拟 Vue的data</span>
        <span class="hljs-keyword">let</span> data = &#123;
            <span class="hljs-attr">msg</span>: <span class="hljs-string">''</span>,
        &#125;
        <span class="hljs-comment">// 模拟 Vue 实例</span>
        <span class="hljs-keyword">let</span> vm = &#123;&#125;
        <span class="hljs-comment">// 对 vm 的 msg 进行数据劫持</span>
        <span class="hljs-built_in">Object</span>.defineProperty(vm, <span class="hljs-string">'msg'</span>, &#123;
            <span class="hljs-comment">// 获取数据</span>
            <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> data.msg
            &#125;,
            <span class="hljs-comment">// 设置 msg</span>
            <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
                <span class="hljs-comment">// 如果传入的值相等就不用修改</span>
                <span class="hljs-keyword">if</span> (newValue === data.msg) <span class="hljs-keyword">return</span>
                <span class="hljs-comment">// 修改数据</span>
                data.msg = newValue
                <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#app'</span>).textContent = data.msg
            &#125;,
        &#125;)
        <span class="hljs-comment">// 这样子就调用了 defineProperty vm.msg 的 set</span>
        vm.msg = <span class="hljs-string">'1234'</span>
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ad4d2fcc15f47d9a3df0db8878ffba5~tplv-k3u1fbpfcp-zoom-1.image" alt="7" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看见 上面 <strong>vm.msg</strong> 数据是<strong>响应式</strong>的</p>
<h2 data-id="heading-3">2.defineProperty修改多个参数为响应式</h2>
<blockquote>
<p>修改多个参数</p>
</blockquote>
<p>看了上面的方法只能修改一个属性，实际上我们 <strong>data</strong> 中数据不可能只有一个,我们何不定义一个方法把<strong>data</strong>中的数据进行遍历都修改成响应式呢</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-comment">// 模拟 Vue的data</span>
        <span class="hljs-keyword">let</span> data = &#123;
            <span class="hljs-attr">msg</span>: <span class="hljs-string">'哈哈'</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-string">'18'</span>,
        &#125;
        <span class="hljs-comment">// 模拟 Vue 实例</span>
        <span class="hljs-keyword">let</span> vm = &#123;&#125;
        <span class="hljs-comment">// 把多个属性转化 响应式</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxyData</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-comment">// 把data 中每一项都[msg,age] 拿出来操作</span>
            <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
                <span class="hljs-comment">// 对 vm 的 属性 进行数据劫持</span>
                <span class="hljs-built_in">Object</span>.defineProperty(vm, key, &#123;
                    <span class="hljs-comment">// 可枚举</span>
                    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
                    <span class="hljs-comment">// 可配置</span>
                    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
                    <span class="hljs-comment">// 获取数据</span>
                    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
                        <span class="hljs-keyword">return</span> data[key]
                    &#125;,
                    <span class="hljs-comment">// 设置 属性值</span>
                    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
                        <span class="hljs-comment">// 如果传入的值相等就不用修改</span>
                        <span class="hljs-keyword">if</span> (newValue === data[key]) <span class="hljs-keyword">return</span>
                        <span class="hljs-comment">// 修改数据</span>
                        data[key] = newValue
                        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#app'</span>).textContent = data[key]
                    &#125;,
                &#125;)
            &#125;)
        &#125;
        <span class="hljs-comment">// 调用方法</span>
        proxyData(data)

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3.Proxy</h2>
<blockquote>
<p>在<strong>Vue3</strong> 中使用 <strong>Proxy</strong> 来设置响应式的属性</p>
</blockquote>
<p>先来了解下 <strong>Proxy</strong> 的两个参数</p>
<p><code>new Proxy(target,handler)</code></p>
<ul>
<li><code>target</code> ：要使用 <code>Proxy</code> 包装的目标对象（可以是任何类型的对象，包括原生数组，函数，甚至另一个代理）</li>
<li><code>handler</code>：一个通常以函数作为属性的对象，各属性中的函数分别定义了在执行各种操作时代理 <code>p</code> 的行为</li>
</ul>
<p>其实 和 Vue2.X实现的逻辑差不多，不过实现的方法不一样</p>
<p>那么就放上代码了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
            <span class="hljs-comment">// 模拟 Vue data</span>
            <span class="hljs-keyword">let</span> data = &#123;
                <span class="hljs-attr">msg</span>: <span class="hljs-string">''</span>,
                <span class="hljs-attr">age</span>: <span class="hljs-string">''</span>,
            &#125;
            <span class="hljs-comment">// 模拟 Vue 的一个实例</span>
            <span class="hljs-comment">// Proxy 第一个</span>
            <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(data, &#123;
                <span class="hljs-comment">// get() 获取值</span>
                <span class="hljs-comment">// target 表示需要代理的对象这里指的就是 data</span>
                <span class="hljs-comment">// key 就是对象的 键</span>
                <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
                    <span class="hljs-keyword">return</span> target[key]
                &#125;,
                <span class="hljs-comment">// 设置值</span>
                <span class="hljs-comment">// newValue 是设置的值</span>
                <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, newValue</span>)</span> &#123;
                    <span class="hljs-comment">// 也先判断下是否和之前的值一样 节省性能</span>
                    <span class="hljs-keyword">if</span> (target[key] === newValue) <span class="hljs-keyword">return</span>
                    <span class="hljs-comment">// 进行设置值</span>
                    target[key] = newValue
                    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#app'</span>).textContent = target[key]
                &#125;,
            &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>触发<strong>set</strong> 和 <strong>get</strong> 的方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 触发了set方法</span>
vm.msg = <span class="hljs-string">'haha'</span>
<span class="hljs-comment">// 触发了get方法</span>
<span class="hljs-built_in">console</span>.log(vm.msg)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">4.发布订阅模式</h2>
<blockquote>
<p>在Vue 响应式中应用到了 发布订阅模式 我们先来了解下</p>
</blockquote>
<p>首先来说简单介绍下 一共有三个角色</p>
<p><strong>发布者</strong>、 <strong>订阅者</strong>、  <strong>信号中心</strong>  举个现实中例子 作者(发布者)写一篇文章 发到了掘金(信号中心) ,掘金可以处理文章然后推送到了首页，然后各自大佬(订阅者)就可以订阅文章</p>
<p>在Vue 中的例子 就是<strong>EventBus</strong> <code>$on</code> <code>$emit</code></p>
<blockquote>
<p>那么我们就简单模仿一下 Vue 的事件总线吧</p>
</blockquote>
<p>之前代码缩进4个单位有点宽，这里改成2个</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 用来存储事件</span>
        <span class="hljs-comment">// 存储的 例子 this.subs = &#123; 'myclick': [fn1, fn2, fn3] ,'inputchange': [fn1, fn2] &#125;</span>
        <span class="hljs-built_in">this</span>.subs = &#123;&#125;
      &#125;
      <span class="hljs-comment">// 实现 $on 方法 type是任务队列的类型 ,fn是方法</span>
      $on(type, fn) &#123;
        <span class="hljs-comment">// 判断在 subs是否有当前类型的 方法队列存在</span>
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.subs[type]) &#123;
          <span class="hljs-comment">// 没有就新增一个 默认为空数组</span>
          <span class="hljs-built_in">this</span>.subs[type] = []
        &#125;
        <span class="hljs-comment">// 把方法加到该类型中</span>
        <span class="hljs-built_in">this</span>.subs[type].push(fn)
      &#125;
      <span class="hljs-comment">// 实现 $emit 方法</span>
      $emit(type) &#123;
        <span class="hljs-comment">// 首先得判断该方法是否存在</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.subs[type]) &#123;
          <span class="hljs-comment">// 获取到参数</span>
          <span class="hljs-keyword">const</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>)
          <span class="hljs-comment">// 循环队列调用 fn</span>
          <span class="hljs-built_in">this</span>.subs[type].forEach(<span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> fn(...args))
        &#125;
      &#125;
    &#125;

    <span class="hljs-comment">// 使用</span>
    <span class="hljs-keyword">const</span> eventHub = <span class="hljs-keyword">new</span> Vue()
    <span class="hljs-comment">// 使用 $on 添加一个 sum 类型的 方法到 subs['sum']中</span>
    eventHub.$on(<span class="hljs-string">'sum'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">let</span> count = [...arguments].reduce(<span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> x + y)
      <span class="hljs-built_in">console</span>.log(count)
    &#125;)
    <span class="hljs-comment">// 触发 sum 方法</span>
    eventHub.$emit(<span class="hljs-string">'sum'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>, <span class="hljs-number">10</span>)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">5.观察者模式</h2>
<blockquote>
<p>与 发布订阅 的差异</p>
</blockquote>
<p>与发布订阅者不同 观察者中 发布者和订阅者(观察者)是相互依赖的 必须要求观察者订阅内容改变事件 ，而发布订阅者是由调度中心进行调度，那么看看观察者模式 是如何相互依赖，下面就举个简单例子</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 目标</span>
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.observerLists = []
      &#125;
      <span class="hljs-comment">// 添加观察者</span>
      <span class="hljs-function"><span class="hljs-title">addObs</span>(<span class="hljs-params">obs</span>)</span> &#123;
        <span class="hljs-comment">// 判断观察者是否有 和 存在更新订阅的方法</span>
        <span class="hljs-keyword">if</span> (obs && obs.update) &#123;
          <span class="hljs-comment">// 添加到观察者列表中</span>
          <span class="hljs-built_in">this</span>.observerLists.push(obs)
        &#125;
      &#125;
      <span class="hljs-comment">// 通知观察者</span>
      <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.observerLists.forEach(<span class="hljs-function">(<span class="hljs-params">obs</span>) =></span> &#123;
          <span class="hljs-comment">// 每个观察者收到通知后 会更新事件</span>
          obs.update()
        &#125;)
      &#125;
      <span class="hljs-comment">// 清空观察者</span>
      <span class="hljs-function"><span class="hljs-title">empty</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.subs = []
      &#125;
    &#125;

    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
      <span class="hljs-comment">// 定义观察者内容更新事件</span>
      <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 在更新事件要处理的逻辑</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'目标更新了'</span>)
      &#125;
    &#125;

    <span class="hljs-comment">// 使用</span>
    <span class="hljs-comment">// 创建目标</span>
    <span class="hljs-keyword">let</span> sub = <span class="hljs-keyword">new</span> Subject()
    <span class="hljs-comment">// 创建观察者</span>
    <span class="hljs-keyword">let</span> obs1 = <span class="hljs-keyword">new</span> Observer()
    <span class="hljs-keyword">let</span> obs2 = <span class="hljs-keyword">new</span> Observer()
    <span class="hljs-comment">// 把观察者添加到列表中</span>
    sub.addObs(obs1)
    sub.addObs(obs2)
    <span class="hljs-comment">// 目标开启了通知 每个观察者者都会自己触发 update 更新事件</span>
    sub.notify()
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">6.模拟Vue的响应式原理</h2>
<blockquote>
<p>这里来实现一个小型简单的 <strong>Vue</strong> 主要实现以下的功能</p>
</blockquote>
<ul>
<li>接收初始化的参数，这里只举几个简单的例子 <strong>el</strong> <strong>data</strong> <strong>options</strong></li>
<li>通过私有方法 <strong>_proxyData</strong> 把<strong>data</strong> 注册到 <strong>Vue</strong> 中 转成<strong>getter</strong> <strong>setter</strong></li>
<li>使用 <strong>observer</strong> 把 <strong>data</strong> 中的属性转为 响应式 添加到 自身身上</li>
<li>使用 <strong>observer</strong> 方法监听 <strong>data</strong> 的所有属性变化来 通过观察者模式 更新视图</li>
<li>使用 <strong>compiler</strong> 编译元素节点上面指令 和 文本节点差值表达式</li>
</ul>
<h3 data-id="heading-8">1.vue.js</h3>
<p>在这里获取到 <code>el</code> <code>data</code></p>
<p>通过 <strong>_proxyData</strong> 把 <strong>data</strong>的属性 注册到<strong>Vue</strong> 并转成 <strong>getter</strong> <strong>setter</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* vue.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// 获取到传入的对象 没有默认为空对象</span>
    <span class="hljs-built_in">this</span>.$options = options || &#123;&#125;
    <span class="hljs-comment">// 获取 el</span>
    <span class="hljs-built_in">this</span>.$el =
      <span class="hljs-keyword">typeof</span> options.el === <span class="hljs-string">'string'</span>
        ? <span class="hljs-built_in">document</span>.querySelector(options.el)
        : options.el
    <span class="hljs-comment">// 获取 data</span>
    <span class="hljs-built_in">this</span>.$data = options.data || &#123;&#125;
    <span class="hljs-comment">// 调用 _proxyData 处理 data中的属性</span>
    <span class="hljs-built_in">this</span>._proxyData(<span class="hljs-built_in">this</span>.$data)
  &#125;
  <span class="hljs-comment">// 把data 中的属性注册到 Vue</span>
  <span class="hljs-function"><span class="hljs-title">_proxyData</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
      <span class="hljs-comment">// 进行数据劫持</span>
      <span class="hljs-comment">// 把每个data的属性 到添加到 Vue 转化为 getter setter方法</span>
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, key, &#123;
        <span class="hljs-comment">// 设置可以枚举</span>
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 设置可以配置</span>
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 获取数据</span>
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> data[key]
        &#125;,
        <span class="hljs-comment">// 设置数据</span>
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
          <span class="hljs-comment">// 判断新值和旧值是否相等</span>
          <span class="hljs-keyword">if</span> (newValue === data[key]) <span class="hljs-keyword">return</span>
          <span class="hljs-comment">// 设置新值</span>
          data[key] = newValue
        &#125;,
      &#125;)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.observer.js</h3>
<p>在这里把 <strong>data</strong> 中的 属性变为响应式加在自身的身上，还有一个主要功能就是 观察者模式在 第 <code>4.dep.js</code> 会有详细的使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* observer.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-comment">// 用来遍历 data</span>
    <span class="hljs-built_in">this</span>.walk(data)
  &#125;
  <span class="hljs-comment">// 遍历 data 转为响应式</span>
  <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-comment">// 判断 data是否为空 和 对象</span>
    <span class="hljs-keyword">if</span> (!data || <span class="hljs-keyword">typeof</span> data !== <span class="hljs-string">'object'</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 遍历 data</span>
    <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
      <span class="hljs-comment">// 转为响应式</span>
      <span class="hljs-built_in">this</span>.defineReactive(data, key, data[key])
    &#125;)
  &#125;
  <span class="hljs-comment">// 转为响应式</span>
  <span class="hljs-comment">// 要注意的 和vue.js 写的不同的是</span>
  <span class="hljs-comment">// vue.js中是将 属性给了 Vue 转为 getter setter</span>
  <span class="hljs-comment">// 这里是 将data中的属性转为getter setter</span>
  <span class="hljs-function"><span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj, key, value</span>)</span> &#123;
    <span class="hljs-comment">// 如果是对象类型的 也调用walk 变成响应式，不是对象类型的直接在walk会被return</span>
    <span class="hljs-built_in">this</span>.walk(value)
    <span class="hljs-comment">// 保存一下 this</span>
    <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
      <span class="hljs-comment">// 设置可枚举</span>
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-comment">// 设置可配置</span>
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-comment">// 获取值</span>
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> value
      &#125;,
      <span class="hljs-comment">// 设置值</span>
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        <span class="hljs-comment">// 判断旧值和新值是否相等</span>
        <span class="hljs-keyword">if</span> (newValue === value) <span class="hljs-keyword">return</span>
        <span class="hljs-comment">// 设置新值</span>
        value = newValue
        <span class="hljs-comment">// 赋值的话如果是newValue是对象，对象里面的属性也应该设置为响应式的</span>
        self.walk(newValue)
      &#125;,
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在html中引入的话注意顺序</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/observer.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在<strong>vue.js</strong> 中使用 <strong>Observer</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* vue.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    ...
    <span class="hljs-comment">// 使用 Obsever 把data中的数据转为响应式</span>
    <span class="hljs-keyword">new</span> Observer(<span class="hljs-built_in">this</span>.$data)
  &#125;
  <span class="hljs-comment">// 把data 中的属性注册到 Vue</span>
  <span class="hljs-function"><span class="hljs-title">_proxyData</span>(<span class="hljs-params">data</span>)</span> &#123;
   ...
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到这里为什么做了两个重复性的操作呢？重复性两次把 <strong>data</strong>的属性转为响应式</p>
<p>在<strong>obsever.js</strong> 中是把 <strong>data</strong> 的所有属性 加到 <strong>data</strong> 自身 变为响应式 转成 <strong>getter</strong> <strong>setter</strong>方式</p>
<p>在<strong>vue.js</strong> 中 也把 <strong>data</strong>的 的所有属性 加到 <strong>Vue</strong> 上,是为了以后方面操作可以用 <strong>Vue</strong> 的实例直接访问到 或者在 <strong>Vue</strong> 中使用 <strong>this</strong> 访问</p>
<blockquote>
<p>使用例子</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/observer.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
          <span class="hljs-attr">msg</span>: <span class="hljs-string">'123'</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">21</span>,
        &#125;,
      &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/792a2a311f044c3a8d153c4fad2f0c46~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725162744305" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样在<code>Vue</code> 和 <code>$data</code> 中都存在了 所有的<strong>data</strong> 属性了 并且是响应式的</p>
<h3 data-id="heading-10">3.compiler.js</h3>
<p><strong>comilper.js</strong>在这个文件里实现对文本节点 和 元素节点指令编译 主要是为了举例子 当然这个写的很简单 指令主要实现 <strong>v-text</strong> <strong>v-model</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* compiler.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compiler</span> </span>&#123;
  <span class="hljs-comment">// vm 指 Vue 实例</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm</span>)</span> &#123;
    <span class="hljs-comment">// 拿到 vm</span>
    <span class="hljs-built_in">this</span>.vm = vm
    <span class="hljs-comment">// 拿到 el</span>
    <span class="hljs-built_in">this</span>.el = vm.$el
    <span class="hljs-comment">// 编译模板</span>
    <span class="hljs-built_in">this</span>.compile(<span class="hljs-built_in">this</span>.el)
  &#125;
  <span class="hljs-comment">// 编译模板</span>
  <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// 获取子节点 如果使用 forEach遍历就把伪数组转为真的数组</span>
    <span class="hljs-keyword">let</span> childNodes = [...el.childNodes]
    childNodes.forEach(<span class="hljs-function">(<span class="hljs-params">node</span>) =></span> &#123;
      <span class="hljs-comment">// 根据不同的节点类型进行编译</span>
      <span class="hljs-comment">// 文本类型的节点</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isTextNode(node)) &#123;
        <span class="hljs-comment">// 编译文本节点</span>
        <span class="hljs-built_in">this</span>.compileText(node)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isElementNode(node)) &#123;
        <span class="hljs-comment">//元素节点</span>
        <span class="hljs-built_in">this</span>.compileElement(node)
      &#125;
      <span class="hljs-comment">// 判断是否还存在子节点考虑递归</span>
      <span class="hljs-keyword">if</span> (node.childNodes && node.childNodes.length) &#123;
        <span class="hljs-comment">// 继续递归编译模板</span>
        <span class="hljs-built_in">this</span>.compile(node)
      &#125;
    &#125;)
  &#125;
  <span class="hljs-comment">// 编译文本节点(简单的实现)</span>
  <span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-comment">// 核心思想利用把正则表达式把&#123;&#123;&#125;&#125;去掉找到里面的变量</span>
    <span class="hljs-comment">// 再去Vue找这个变量赋值给node.textContent</span>
    <span class="hljs-keyword">let</span> reg = <span class="hljs-regexp">/\&#123;\&#123;(.+?)\&#125;\&#125;/</span>
    <span class="hljs-comment">// 获取节点的文本内容</span>
    <span class="hljs-keyword">let</span> val = node.textContent
    <span class="hljs-comment">// 判断是否有 &#123;&#123;&#125;&#125;</span>
    <span class="hljs-keyword">if</span> (reg.test(val)) &#123;
      <span class="hljs-comment">// 获取分组一  也就是 &#123;&#123;&#125;&#125; 里面的内容 去除前后空格</span>
      <span class="hljs-keyword">let</span> key = <span class="hljs-built_in">RegExp</span>.$1.trim()
      <span class="hljs-comment">// 进行替换再赋值给node</span>
      node.textContent = val.replace(reg, <span class="hljs-built_in">this</span>.vm[key])
    &#125;
  &#125;
  <span class="hljs-comment">// 编译元素节点这里只处理指令</span>
  <span class="hljs-function"><span class="hljs-title">compileElement</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-comment">// 获取到元素节点上面的所有属性进行遍历</span>
    ![...node.attributes].forEach(<span class="hljs-function">(<span class="hljs-params">attr</span>) =></span> &#123;
      <span class="hljs-comment">// 获取属性名</span>
      <span class="hljs-keyword">let</span> attrName = attr.name
      <span class="hljs-comment">// 判断是否是 v- 开头的指令</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isDirective(attrName)) &#123;
        <span class="hljs-comment">// 除去 v- 方便操作</span>
        attrName = attrName.substr(<span class="hljs-number">2</span>)
        <span class="hljs-comment">// 获取 指令的值就是  v-text = "msg"  中msg</span>
        <span class="hljs-comment">// msg 作为 key 去Vue 找这个变量</span>
        <span class="hljs-keyword">let</span> key = attr.value
        <span class="hljs-comment">// 指令操作 执行指令方法</span>
        <span class="hljs-comment">// vue指令很多为了避免大量个 if判断这里就写个 uapdate 方法</span>
        <span class="hljs-built_in">this</span>.update(node, key, attrName)
      &#125;
    &#125;)
  &#125;
  <span class="hljs-comment">// 添加指令方法 并且执行</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">node, key, attrName</span>)</span> &#123;
    <span class="hljs-comment">// 比如添加 textUpdater 就是用来处理 v-text 方法</span>
    <span class="hljs-comment">// 我们应该就内置一个 textUpdater 方法进行调用</span>
    <span class="hljs-comment">// 加个后缀加什么无所谓但是要定义相应的方法</span>
    <span class="hljs-keyword">let</span> updateFn = <span class="hljs-built_in">this</span>[attrName + <span class="hljs-string">'Updater'</span>]
    <span class="hljs-comment">// 如果存在这个内置方法 就可以调用了</span>
    updateFn && updateFn(node, key, <span class="hljs-built_in">this</span>.vm[key])
  &#125;
  <span class="hljs-comment">// 提前写好 相应的指定方法比如这个 v-text</span>
  <span class="hljs-comment">// 使用的时候 和 Vue 的一样</span>
  <span class="hljs-function"><span class="hljs-title">textUpdater</span>(<span class="hljs-params">node, key, value</span>)</span> &#123;
    node.textContent = value
  &#125;
    
  <span class="hljs-comment">// v-model</span>
  <span class="hljs-function"><span class="hljs-title">modelUpdater</span>(<span class="hljs-params">node, key, value</span>)</span> &#123;
    node.value = value
  &#125;
    
  <span class="hljs-comment">// 判断元素的属性是否是 vue 指令</span>
  <span class="hljs-function"><span class="hljs-title">isDirective</span>(<span class="hljs-params">attr</span>)</span> &#123;
    <span class="hljs-keyword">return</span> attr.startsWith(<span class="hljs-string">'v-'</span>)
  &#125;
  <span class="hljs-comment">// 判断是否是元素节点</span>
  <span class="hljs-function"><span class="hljs-title">isElementNode</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">return</span> node.nodeType === <span class="hljs-number">1</span>
  &#125;
  <span class="hljs-comment">// 判断是否是 文本 节点</span>
  <span class="hljs-function"><span class="hljs-title">isTextNode</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">return</span> node.nodeType === <span class="hljs-number">3</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">4.dep.js</h3>
<p>写一个<strong>Dep</strong>类 它相当于 观察者中的发布者  每个响应式属性都会创建这么一个 <strong>Dep</strong> 对象 ，负责收集该依赖属性的<strong>Watcher</strong>对象 （是在使用响应式数据的时候做的操作）</p>
<p>当我们对响应式属性在 <strong>setter</strong> 中进行更新的时候，会调用 <strong>Dep</strong> 中 <strong>notify</strong> 方法发送更新通知</p>
<p>然后去调用 <strong>Watcher</strong> 中的 <strong>update</strong> 实现视图的更新操作（是当数据发生变化的时候去通知观察者调用观察者的update更新视图）</p>
<p>总的来说 在<strong>Dep</strong>(这里指发布者) 中负责收集依赖 添加观察者(这里指<strong>Wathcer</strong>)，然后在 <strong>setter</strong> 数据更新的时候通知观察者</p>
<p>说的这么多重复的话，大家应该知道是在哪个阶段 收集依赖 哪个阶段 通知观察者了吧，下面就来实现一下吧</p>
<blockquote>
<p>先写<strong>Dep</strong>类</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* dep.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 存储观察者</span>
    <span class="hljs-built_in">this</span>.subs = []
  &#125;
  <span class="hljs-comment">// 添加观察者</span>
  <span class="hljs-function"><span class="hljs-title">addSub</span>(<span class="hljs-params">sub</span>)</span> &#123;
    <span class="hljs-comment">// 判断观察者是否存在 和 是否拥有update方法</span>
    <span class="hljs-keyword">if</span> (sub && sub.update) &#123;
      <span class="hljs-built_in">this</span>.subs.push(sub)
    &#125;
  &#125;
  <span class="hljs-comment">// 通知方法</span>
  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 触发每个观察者的更新方法</span>
    <span class="hljs-built_in">this</span>.subs.forEach(<span class="hljs-function">(<span class="hljs-params">sub</span>) =></span> &#123;
      sub.update()
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在 <strong>obsever.js</strong> 中使用<strong>Dep</strong></p>
</blockquote>
<p>在 <strong>get</strong> 中添加 <strong>Dep.target</strong> (观察者)</p>
<p>在 <strong>set</strong> 中 触发 <strong>notify</strong> (通知)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* observer.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  ...
  &#125;
  <span class="hljs-comment">// 遍历 data 转为响应式</span>
  <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">data</span>)</span> &#123;
   ...
  &#125;
  <span class="hljs-comment">// 这里是 将data中的属性转为getter setter</span>
  <span class="hljs-function"><span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj, key, value</span>)</span> &#123;
...
    <span class="hljs-comment">// 创建 Dep 对象</span>
    <span class="hljs-keyword">let</span> dep = <span class="hljs-keyword">new</span> Dep()
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
  ...
      <span class="hljs-comment">// 获取值</span>
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 在这里添加观察者对象 Dep.target 表示观察者</span>
        Dep.target && dep.addSub(Dep.target)
        <span class="hljs-keyword">return</span> value
      &#125;,
      <span class="hljs-comment">// 设置值</span>
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (newValue === value) <span class="hljs-keyword">return</span>
        value = newValue
        self.walk(newValue)
        <span class="hljs-comment">// 触发通知 更新视图</span>
        dep.notify()
      &#125;,
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">5.watcher.js</h3>
<p>**watcher **的作用 数据更新后 收到通知之后 调用 <strong>update</strong> 进行更新</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* watcher.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm, key, cb</span>)</span> &#123;
    <span class="hljs-comment">// vm 是 Vue 实例</span>
    <span class="hljs-built_in">this</span>.vm = vm
    <span class="hljs-comment">// key 是 data 中的属性</span>
    <span class="hljs-built_in">this</span>.key = key
    <span class="hljs-comment">// cb 回调函数 更新视图的具体方法</span>
    <span class="hljs-built_in">this</span>.cb = cb
    <span class="hljs-comment">// 把观察者的存放在 Dep.target</span>
    Dep.target = <span class="hljs-built_in">this</span>
    <span class="hljs-comment">// 旧数据 更新视图的时候要进行比较</span>
    <span class="hljs-comment">// 还有一点就是 vm[key] 这个时候就触发了 get 方法</span>
    <span class="hljs-comment">// 之前在 get 把 观察者 通过dep.addSub(Dep.target) 添加到了 dep.subs中</span>
    <span class="hljs-built_in">this</span>.oldValue = vm[key]
    <span class="hljs-comment">// Dep.target 就不用存在了 因为上面的操作已经存好了</span>
    Dep.target = <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-comment">// 观察者中的必备方法 用来更新视图</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 获取新值</span>
    <span class="hljs-keyword">let</span> newValue = <span class="hljs-built_in">this</span>.vm[<span class="hljs-built_in">this</span>.key]
    <span class="hljs-comment">// 比较旧值和新值</span>
    <span class="hljs-keyword">if</span> (newValue === <span class="hljs-built_in">this</span>.oldValue) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 调用具体的更新方法</span>
    <span class="hljs-built_in">this</span>.cb(newValue)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么去哪里创建 <strong>Watcher</strong> 呢？还记得在 <strong>compiler.js</strong>中 对文本节点的编译操作吗</p>
<p>在编译完文本节点后 在这里添加一个 <strong>Watcher</strong></p>
<p>还有 <strong>v-text</strong> <strong>v-model</strong> 指令 当编译的是元素节点 就添加一个 <strong>Watcher</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* compiler.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compiler</span> </span>&#123;
  <span class="hljs-comment">// vm 指 Vue 实例</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm</span>)</span> &#123;
    <span class="hljs-comment">// 拿到 vm</span>
    <span class="hljs-built_in">this</span>.vm = vm
    <span class="hljs-comment">// 拿到 el</span>
    <span class="hljs-built_in">this</span>.el = vm.$el
    <span class="hljs-comment">// 编译模板</span>
    <span class="hljs-built_in">this</span>.compile(<span class="hljs-built_in">this</span>.el)
  &#125;
  <span class="hljs-comment">// 编译模板</span>
  <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-keyword">let</span> childNodes = [...el.childNodes]
    childNodes.forEach(<span class="hljs-function">(<span class="hljs-params">node</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isTextNode(node)) &#123;
        <span class="hljs-comment">// 编译文本节点</span>
        <span class="hljs-built_in">this</span>.compileText(node)
      &#125; 
       ...
  &#125;
  <span class="hljs-comment">// 编译文本节点(简单的实现)</span>
  <span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">let</span> reg = <span class="hljs-regexp">/\&#123;\&#123;(.+)\&#125;\&#125;/</span>
    <span class="hljs-keyword">let</span> val = node.textContent
    <span class="hljs-keyword">if</span> (reg.test(val)) &#123;
      <span class="hljs-keyword">let</span> key = <span class="hljs-built_in">RegExp</span>.$1.trim()
      node.textContent = val.replace(reg, <span class="hljs-built_in">this</span>.vm[key])
      <span class="hljs-comment">// 创建观察者</span>
      <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.vm, key, <span class="hljs-function"><span class="hljs-params">newValue</span> =></span> &#123;
        node.textContent = newValue
      &#125;)
    &#125;
  &#125;
  ...
  <span class="hljs-comment">// v-text </span>
  <span class="hljs-function"><span class="hljs-title">textUpdater</span>(<span class="hljs-params">node, key, value</span>)</span> &#123;
    node.textContent = value
     <span class="hljs-comment">// 创建观察者2</span>
    <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.vm, key, <span class="hljs-function">(<span class="hljs-params">newValue</span>) =></span> &#123;
      node.textContent = newValue
    &#125;)
  &#125;
  <span class="hljs-comment">// v-model</span>
  <span class="hljs-function"><span class="hljs-title">modelUpdater</span>(<span class="hljs-params">node, key, value</span>)</span> &#123;
    node.value = value
    <span class="hljs-comment">// 创建观察者</span>
    <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.vm, key, <span class="hljs-function">(<span class="hljs-params">newValue</span>) =></span> &#123;
      node.value = newValue
    &#125;)
    <span class="hljs-comment">// 这里实现双向绑定 监听input 事件修改 data中的属性</span>
    node.addEventListener(<span class="hljs-string">'input'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.vm[key] = node.value
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 我们改变 响应式属性的时候 触发了 <strong>set()</strong> 方法 ，然后里面 发布者 <strong>dep.notify</strong> 方法启动了，拿到了 所有的 观察者 <strong>watcher</strong> 实例去执行 <strong>update</strong> 方法调用了回调函数 <strong>cb(newValue)</strong> 方法并把 新值传递到了 <strong>cb()</strong> 当中 <strong>cb</strong>方法是的具体更新视图的方法 去更新视图</p>
<p>比如上面的例子里的第三个参数 <strong>cb</strong>方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.vm, key, <span class="hljs-function"><span class="hljs-params">newValue</span> =></span> &#123;
    node.textContent = newValue
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一点要实现<strong>v-model</strong>的双向绑定</p>
<p>不仅要通过修改数据来触发更新视图，还得为<strong>node</strong>添加 <strong>input</strong> 事件 改变 <strong>data</strong>数据中的属性</p>
<p>来达到双向绑定的效果</p>
<h2 data-id="heading-13">7.测试下自己写的</h2>
<blockquote>
<p>到了目前为止 响应式 和 双向绑定 都基本实现了 那么来写个例子测试下</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    &#123;&#123;msg&#125;&#125; <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
    &#123;&#123;age&#125;&#125; <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-text</span>=<span class="hljs-string">"msg"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"msg"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/dep.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/watcher.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/compiler.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/observer.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
      <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">msg</span>: <span class="hljs-string">'123'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">21</span>,
      &#125;,
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1e875a85d8845f7b6a92e98ba7d1f3a~tplv-k3u1fbpfcp-zoom-1.image" alt="8" loading="lazy" referrerpolicy="no-referrer"></p>
<p>OK 基本实现了 通过 观察者模式 来 实现 响应式原理</p>
<h2 data-id="heading-14">8.五个文件代码</h2>
<p>这里直接把5个文件个代码贴出来 上面有的地方省略了,下面是完整的方便大家阅读</p>
<blockquote>
<p>vue.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* vue.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// 获取到传入的对象 没有默认为空对象</span>
    <span class="hljs-built_in">this</span>.$options = options || &#123;&#125;
    <span class="hljs-comment">// 获取 el</span>
    <span class="hljs-built_in">this</span>.$el =
      <span class="hljs-keyword">typeof</span> options.el === <span class="hljs-string">'string'</span>
        ? <span class="hljs-built_in">document</span>.querySelector(options.el)
        : options.el
    <span class="hljs-comment">// 获取 data</span>
    <span class="hljs-built_in">this</span>.$data = options.data || &#123;&#125;
    <span class="hljs-comment">// 调用 _proxyData 处理 data中的属性</span>
    <span class="hljs-built_in">this</span>._proxyData(<span class="hljs-built_in">this</span>.$data)
    <span class="hljs-comment">// 使用 Obsever 把data中的数据转为响应式</span>
    <span class="hljs-keyword">new</span> Observer(<span class="hljs-built_in">this</span>.$data)
    <span class="hljs-comment">// 编译模板</span>
    <span class="hljs-keyword">new</span> Compiler(<span class="hljs-built_in">this</span>)
  &#125;
  <span class="hljs-comment">// 把data 中的属性注册到 Vue</span>
  <span class="hljs-function"><span class="hljs-title">_proxyData</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
      <span class="hljs-comment">// 进行数据劫持</span>
      <span class="hljs-comment">// 把每个data的属性 到添加到 Vue 转化为 getter setter方法</span>
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, key, &#123;
        <span class="hljs-comment">// 设置可以枚举</span>
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 设置可以配置</span>
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 获取数据</span>
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> data[key]
        &#125;,
        <span class="hljs-comment">// 设置数据</span>
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
          <span class="hljs-comment">// 判断新值和旧值是否相等</span>
          <span class="hljs-keyword">if</span> (newValue === data[key]) <span class="hljs-keyword">return</span>
          <span class="hljs-comment">// 设置新值</span>
          data[key] = newValue
        &#125;,
      &#125;)
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>obsever.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* observer.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-comment">// 用来遍历 data</span>
    <span class="hljs-built_in">this</span>.walk(data)
  &#125;
  <span class="hljs-comment">// 遍历 data 转为响应式</span>
  <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-comment">// 判断 data是否为空 和 对象</span>
    <span class="hljs-keyword">if</span> (!data || <span class="hljs-keyword">typeof</span> data !== <span class="hljs-string">'object'</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 遍历 data</span>
    <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
      <span class="hljs-comment">// 转为响应式</span>
      <span class="hljs-built_in">this</span>.defineReactive(data, key, data[key])
    &#125;)
  &#125;
  <span class="hljs-comment">// 转为响应式</span>
  <span class="hljs-comment">// 要注意的 和vue.js 写的不同的是</span>
  <span class="hljs-comment">// vue.js中是将 属性给了 Vue 转为 getter setter</span>
  <span class="hljs-comment">// 这里是 将data中的属性转为getter setter</span>
  <span class="hljs-function"><span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj, key, value</span>)</span> &#123;
    <span class="hljs-comment">// 如果是对象类型的 也调用walk 变成响应式，不是对象类型的直接在walk会被return</span>
    <span class="hljs-built_in">this</span>.walk(value)
    <span class="hljs-comment">// 保存一下 this</span>
    <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>
    <span class="hljs-comment">// 创建 Dep 对象</span>
    <span class="hljs-keyword">let</span> dep = <span class="hljs-keyword">new</span> Dep()
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
      <span class="hljs-comment">// 设置可枚举</span>
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-comment">// 设置可配置</span>
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,

      <span class="hljs-comment">// 获取值</span>
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 在这里添加观察者对象 Dep.target 表示观察者</span>
        Dep.target && dep.addSub(Dep.target)
        <span class="hljs-keyword">return</span> value
      &#125;,
      <span class="hljs-comment">// 设置值</span>
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        <span class="hljs-comment">// 判断旧值和新值是否相等</span>
        <span class="hljs-keyword">if</span> (newValue === value) <span class="hljs-keyword">return</span>
        <span class="hljs-comment">// 设置新值</span>
        value = newValue
        <span class="hljs-comment">// 赋值的话如果是newValue是对象，对象里面的属性也应该设置为响应式的</span>
        self.walk(newValue)
        <span class="hljs-comment">// 触发通知 更新视图</span>
        dep.notify()
      &#125;,
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>compiler.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* compiler.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compiler</span> </span>&#123;
  <span class="hljs-comment">// vm 指 Vue 实例</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm</span>)</span> &#123;
    <span class="hljs-comment">// 拿到 vm</span>
    <span class="hljs-built_in">this</span>.vm = vm
    <span class="hljs-comment">// 拿到 el</span>
    <span class="hljs-built_in">this</span>.el = vm.$el
    <span class="hljs-comment">// 编译模板</span>
    <span class="hljs-built_in">this</span>.compile(<span class="hljs-built_in">this</span>.el)
  &#125;
  <span class="hljs-comment">// 编译模板</span>
  <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// 获取子节点 如果使用 forEach遍历就把伪数组转为真的数组</span>
    <span class="hljs-keyword">let</span> childNodes = [...el.childNodes]
    childNodes.forEach(<span class="hljs-function">(<span class="hljs-params">node</span>) =></span> &#123;
      <span class="hljs-comment">// 根据不同的节点类型进行编译</span>
      <span class="hljs-comment">// 文本类型的节点</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isTextNode(node)) &#123;
        <span class="hljs-comment">// 编译文本节点</span>
        <span class="hljs-built_in">this</span>.compileText(node)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isElementNode(node)) &#123;
        <span class="hljs-comment">//元素节点</span>
        <span class="hljs-built_in">this</span>.compileElement(node)
      &#125;
      <span class="hljs-comment">// 判断是否还存在子节点考虑递归</span>
      <span class="hljs-keyword">if</span> (node.childNodes && node.childNodes.length) &#123;
        <span class="hljs-comment">// 继续递归编译模板</span>
        <span class="hljs-built_in">this</span>.compile(node)
      &#125;
    &#125;)
  &#125;
  <span class="hljs-comment">// 编译文本节点(简单的实现)</span>
  <span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-comment">// 核心思想利用把正则表达式把&#123;&#123;&#125;&#125;去掉找到里面的变量</span>
    <span class="hljs-comment">// 再去Vue找这个变量赋值给node.textContent</span>
    <span class="hljs-keyword">let</span> reg = <span class="hljs-regexp">/\&#123;\&#123;(.+?)\&#125;\&#125;/</span>
    <span class="hljs-comment">// 获取节点的文本内容</span>
    <span class="hljs-keyword">let</span> val = node.textContent
    <span class="hljs-comment">// 判断是否有 &#123;&#123;&#125;&#125;</span>
    <span class="hljs-keyword">if</span> (reg.test(val)) &#123;
      <span class="hljs-comment">// 获取分组一  也就是 &#123;&#123;&#125;&#125; 里面的内容 去除前后空格</span>
      <span class="hljs-keyword">let</span> key = <span class="hljs-built_in">RegExp</span>.$1.trim()
      <span class="hljs-comment">// 进行替换再赋值给node</span>
      node.textContent = val.replace(reg, <span class="hljs-built_in">this</span>.vm[key])
      <span class="hljs-comment">// 创建观察者</span>
      <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.vm, key, <span class="hljs-function">(<span class="hljs-params">newValue</span>) =></span> &#123;
        node.textContent = newValue
      &#125;)
    &#125;
  &#125;
  <span class="hljs-comment">// 编译元素节点这里只处理指令</span>
  <span class="hljs-function"><span class="hljs-title">compileElement</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-comment">// 获取到元素节点上面的所有属性进行遍历</span>
    ![...node.attributes].forEach(<span class="hljs-function">(<span class="hljs-params">attr</span>) =></span> &#123;
      <span class="hljs-comment">// 获取属性名</span>
      <span class="hljs-keyword">let</span> attrName = attr.name
      <span class="hljs-comment">// 判断是否是 v- 开头的指令</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isDirective(attrName)) &#123;
        <span class="hljs-comment">// 除去 v- 方便操作</span>
        attrName = attrName.substr(<span class="hljs-number">2</span>)
        <span class="hljs-comment">// 获取 指令的值就是  v-text = "msg"  中msg</span>
        <span class="hljs-comment">// msg 作为 key 去Vue 找这个变量</span>
        <span class="hljs-keyword">let</span> key = attr.value
        <span class="hljs-comment">// 指令操作 执行指令方法</span>
        <span class="hljs-comment">// vue指令很多为了避免大量个 if判断这里就写个 uapdate 方法</span>
        <span class="hljs-built_in">this</span>.update(node, key, attrName)
      &#125;
    &#125;)
  &#125;
  <span class="hljs-comment">// 添加指令方法 并且执行</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">node, key, attrName</span>)</span> &#123;
    <span class="hljs-comment">// 比如添加 textUpdater 就是用来处理 v-text 方法</span>
    <span class="hljs-comment">// 我们应该就内置一个 textUpdater 方法进行调用</span>
    <span class="hljs-comment">// 加个后缀加什么无所谓但是要定义相应的方法</span>
    <span class="hljs-keyword">let</span> updateFn = <span class="hljs-built_in">this</span>[attrName + <span class="hljs-string">'Updater'</span>]
    <span class="hljs-comment">// 如果存在这个内置方法 就可以调用了</span>
    updateFn && updateFn.call(<span class="hljs-built_in">this</span>, node, key, <span class="hljs-built_in">this</span>.vm[key])
  &#125;
  <span class="hljs-comment">// 提前写好 相应的指定方法比如这个 v-text</span>
  <span class="hljs-comment">// 使用的时候 和 Vue 的一样</span>
  <span class="hljs-function"><span class="hljs-title">textUpdater</span>(<span class="hljs-params">node, key, value</span>)</span> &#123;
    node.textContent = value
    <span class="hljs-comment">// 创建观察者</span>
    <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.vm, key, <span class="hljs-function">(<span class="hljs-params">newValue</span>) =></span> &#123;
      node.textContent = newValue
    &#125;)
  &#125;
  <span class="hljs-comment">// v-model</span>
  <span class="hljs-function"><span class="hljs-title">modelUpdater</span>(<span class="hljs-params">node, key, value</span>)</span> &#123;
    node.value = value
    <span class="hljs-comment">// 创建观察者</span>
    <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.vm, key, <span class="hljs-function">(<span class="hljs-params">newValue</span>) =></span> &#123;
      node.value = newValue
    &#125;)
    <span class="hljs-comment">// 这里实现双向绑定</span>
    node.addEventListener(<span class="hljs-string">'input'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.vm[key] = node.value
    &#125;)
  &#125;

  <span class="hljs-comment">// 判断元素的属性是否是 vue 指令</span>
  <span class="hljs-function"><span class="hljs-title">isDirective</span>(<span class="hljs-params">attr</span>)</span> &#123;
    <span class="hljs-keyword">return</span> attr.startsWith(<span class="hljs-string">'v-'</span>)
  &#125;
  <span class="hljs-comment">// 判断是否是元素节点</span>
  <span class="hljs-function"><span class="hljs-title">isElementNode</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">return</span> node.nodeType === <span class="hljs-number">1</span>
  &#125;
  <span class="hljs-comment">// 判断是否是 文本 节点</span>
  <span class="hljs-function"><span class="hljs-title">isTextNode</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">return</span> node.nodeType === <span class="hljs-number">3</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>dep.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* dep.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 存储观察者</span>
    <span class="hljs-built_in">this</span>.subs = []
  &#125;
  <span class="hljs-comment">// 添加观察者</span>
  <span class="hljs-function"><span class="hljs-title">addSub</span>(<span class="hljs-params">sub</span>)</span> &#123;
    <span class="hljs-comment">// 判断观察者是否存在 和 是否拥有update方法</span>
    <span class="hljs-keyword">if</span> (sub && sub.update) &#123;
      <span class="hljs-built_in">this</span>.subs.push(sub)
    &#125;
  &#125;
  <span class="hljs-comment">// 通知方法</span>
  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 触发每个观察者的更新方法</span>
    <span class="hljs-built_in">this</span>.subs.forEach(<span class="hljs-function">(<span class="hljs-params">sub</span>) =></span> &#123;
      sub.update()
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>watcher.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* watcher.js */</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm, key, cb</span>)</span> &#123;
    <span class="hljs-comment">// vm 是 Vue 实例</span>
    <span class="hljs-built_in">this</span>.vm = vm
    <span class="hljs-comment">// key 是 data 中的属性</span>
    <span class="hljs-built_in">this</span>.key = key
    <span class="hljs-comment">// cb 回调函数 更新视图的具体方法</span>
    <span class="hljs-built_in">this</span>.cb = cb
    <span class="hljs-comment">// 把观察者的存放在 Dep.target</span>
    Dep.target = <span class="hljs-built_in">this</span>
    <span class="hljs-comment">// 旧数据 更新视图的时候要进行比较</span>
    <span class="hljs-comment">// 还有一点就是 vm[key] 这个时候就触发了 get 方法</span>
    <span class="hljs-comment">// 之前在 get 把 观察者 通过dep.addSub(Dep.target) 添加到了 dep.subs中</span>
    <span class="hljs-built_in">this</span>.oldValue = vm[key]
    <span class="hljs-comment">// Dep.target 就不用存在了 因为上面的操作已经存好了</span>
    Dep.target = <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-comment">// 观察者中的必备方法 用来更新视图</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 获取新值</span>
    <span class="hljs-keyword">let</span> newValue = <span class="hljs-built_in">this</span>.vm[<span class="hljs-built_in">this</span>.key]
    <span class="hljs-comment">// 比较旧值和新值</span>
    <span class="hljs-keyword">if</span> (newValue === <span class="hljs-built_in">this</span>.oldValue) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 调用具体的更新方法</span>
    <span class="hljs-built_in">this</span>.cb(newValue)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            