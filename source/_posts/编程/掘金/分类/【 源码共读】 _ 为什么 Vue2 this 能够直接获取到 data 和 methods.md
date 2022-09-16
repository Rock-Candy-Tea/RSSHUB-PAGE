
---
title: '【 源码共读】 _ 为什么 Vue2 this 能够直接获取到 data 和 methods'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb24f58d6e8b4a469d4ee3bd82269595~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Wed, 14 Sep 2022 19:21:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb24f58d6e8b4a469d4ee3bd82269595~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><em>本文参加了由</em><a href="https://link.juejin.cn/?target=https%3A%2F%2Flxchuan12.gitee.io" target="_blank" rel="nofollow noopener noreferrer" title="https://lxchuan12.gitee.io" ref="nofollow noopener noreferrer">公众号@若川视野</a> <strong>发起的每周源码共读活动，</strong><a href="https://juejin.cn/post/7079706017579139102" target="_blank" title="https://juejin.cn/post/7079706017579139102">点击了解详情一起参与。</a></p>
<p>【若川视野 x 源码共读】第23期 | 为什么 Vue2 this 能够直接获取到 data 和 methods <a href="https://juejin.cn/post/7082984422516981796" target="_blank" title="https://juejin.cn/post/7082984422516981796">点击了解本期详情一起参与</a>。</p>
<h2 data-id="heading-0">本文涉及</h2>
<blockquote>
<p>this指向</p>
<p>代码调试</p>
<p>bind函数使用</p>
</blockquote>
<h3 data-id="heading-1">示例代码</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.7.10"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vue</span>(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
          <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello JueJin'</span>
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
          <span class="hljs-title function_">getMessage</span>(<span class="hljs-params"></span>) &#123;
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">message</span>)
          &#125;
        &#125;
      &#125;)
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(vm)
      vm.<span class="hljs-title function_">getMessage</span>() <span class="hljs-comment">// Hello JueJin</span>
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道，运行时控制台会执行<code>vm.getMessage()</code>，输出<code>this.message</code>的数据。</p>
<p>我们尝试自己来实现一个对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Object</span>(&#123;
    <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello JueJin'</span>
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-title function_">getMessage</span>(<span class="hljs-params"></span>) &#123;
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">message</span>)
        &#125;
    &#125;
&#125;)
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(obj.<span class="hljs-title function_">getMessage</span>()) <span class="hljs-comment">// TypeError: obj.getMessage is not a function</span>
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(obj.<span class="hljs-property">methods</span>.<span class="hljs-title function_">getMessage</span>()) <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般而言我们是不能直接访问到<code>obj</code>里面的属性，而<code>vue</code>的对象可以这样使用，由此可得，<strong>是<code>this</code>指向问题。</strong></p>
<ul>
<li>我们来调试下代码</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb24f58d6e8b4a469d4ee3bd82269595~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image-20220915090209499" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在浏览器<code>Sources</code>中打上断点，进入<code>vue</code>的构造函数中</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b27951ee0874b4bbb1f533bec42b3dd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image-20220915090501873" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>继续进入<code>_init</code>函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">initMixin$1</span>(<span class="hljs-params">Vue</span>) &#123;
    <span class="hljs-title class_">Vue</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">_init</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) &#123;
        <span class="hljs-keyword">var</span> vm = <span class="hljs-variable language_">this</span>;
        <span class="hljs-comment">/* ... 中间省略 ... */</span>
        <span class="hljs-comment">// expose real self</span>
        vm.<span class="hljs-property">_self</span> = vm;
        <span class="hljs-title function_">initLifecycle</span>(vm);
        <span class="hljs-title function_">initEvents</span>(vm); 
        <span class="hljs-title function_">initRender</span>(vm);
        <span class="hljs-title function_">callHook$1</span>(vm, <span class="hljs-string">'beforeCreate'</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">false</span> <span class="hljs-comment">/* setContext */</span>);
        <span class="hljs-title function_">initInjections</span>(vm); <span class="hljs-comment">// resolve injections before data/props</span>


        <span class="hljs-comment">// 初始化状态</span>
        <span class="hljs-title function_">initState</span>(vm); 
        <span class="hljs-title function_">initProvide</span>(vm); <span class="hljs-comment">// resolve provide after data/props</span>
        <span class="hljs-title function_">callHook$1</span>(vm, <span class="hljs-string">'created'</span>);
        <span class="hljs-comment">/* istanbul ignore if */</span>
        <span class="hljs-keyword">if</span> (config.<span class="hljs-property">performance</span> && mark) &#123;
            vm.<span class="hljs-property">_name</span> = <span class="hljs-title function_">formatComponentName</span>(vm, <span class="hljs-literal">false</span>);
            <span class="hljs-title function_">mark</span>(endTag);
            <span class="hljs-title function_">measure</span>(<span class="hljs-string">"vue "</span>.<span class="hljs-title function_">concat</span>(vm.<span class="hljs-property">_name</span>, <span class="hljs-string">" init"</span>), startTag, endTag);
        &#125;
        <span class="hljs-keyword">if</span> (vm.<span class="hljs-property">$options</span>.<span class="hljs-property">el</span>) &#123;
            vm.$mount(vm.<span class="hljs-property">$options</span>.<span class="hljs-property">el</span>);
        &#125;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在<code>initState</code>中打上断点，F8调到该断点，进入函数</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e3d28d8d92f4f549b24ab5a05d09cfd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image-20220915102656691" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>根据函数名，我们可以得知这两个函数应该就是初始化方法和数据的，加上断点，进去查看一下</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">initMethods</span>(<span class="hljs-params">vm, methods</span>) &#123;
    <span class="hljs-keyword">var</span> props = vm.<span class="hljs-property">$options</span>.<span class="hljs-property">props</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> methods) &#123;
        &#123;
            <span class="hljs-comment">// 判断是否是函数</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> methods[key] !== <span class="hljs-string">'function'</span>) &#123;
                <span class="hljs-title function_">warn$2</span>(<span class="hljs-string">"Method \""</span>.<span class="hljs-title function_">concat</span>(key, <span class="hljs-string">"\" has type \""</span>).<span class="hljs-title function_">concat</span>(<span class="hljs-keyword">typeof</span> methods[key], <span class="hljs-string">"\" in the component definition. "</span>) +
                       <span class="hljs-string">"Did you reference the function correctly?"</span>, vm);
            &#125;
            <span class="hljs-comment">// 判断方法名字和props是否冲突</span>
            <span class="hljs-keyword">if</span> (props && <span class="hljs-title function_">hasOwn</span>(props, key)) &#123;
                <span class="hljs-title function_">warn$2</span>(<span class="hljs-string">"Method \""</span>.<span class="hljs-title function_">concat</span>(key, <span class="hljs-string">"\" has already been defined as a prop."</span>), vm);
            &#125;
            <span class="hljs-comment">// 判断方法是否已经存在vue实例中，并且方法名是否有$ _</span>
            <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> vm && <span class="hljs-title function_">isReserved</span>(key)) &#123;
                <span class="hljs-title function_">warn$2</span>(<span class="hljs-string">"Method \""</span>.<span class="hljs-title function_">concat</span>(key, <span class="hljs-string">"\" conflicts with an existing Vue instance method. "</span>) +
                       <span class="hljs-string">"Avoid defining component methods that start with _ or $."</span>);
            &#125;
        &#125;
        <span class="hljs-comment">// 函数绑定  bind</span>
        vm[key] = <span class="hljs-keyword">typeof</span> methods[key] !== <span class="hljs-string">'function'</span> ? noop : <span class="hljs-title function_">bind$1</span>(methods[key], vm);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上判断，将<code>methods</code>属性中的方法赋值给<code>vm</code>，并且通过<code>bind</code>将this指针指向vm，所以可以<code>this.methods===vm.methods</code></p>
<ul>
<li>断点查看<code>initData</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">function</span> <span class="hljs-title function_">initData</span>(<span class="hljs-params">vm</span>) &#123;
      <span class="hljs-keyword">var</span> data = vm.<span class="hljs-property">$options</span>.<span class="hljs-property">data</span>;
      data = vm.<span class="hljs-property">_data</span> = <span class="hljs-title function_">isFunction</span>(data) ? <span class="hljs-title function_">getData</span>(data, vm) : data || &#123;&#125;;
      <span class="hljs-keyword">if</span> (!<span class="hljs-title function_">isPlainObject</span>(data)) &#123;
          data = &#123;&#125;;
          <span class="hljs-title function_">warn$2</span>(<span class="hljs-string">'data functions should return an object:\n'</span> +
                  <span class="hljs-string">'https://v2.vuejs.org/v2/guide/components.html#data-Must-Be-a-Function'</span>, vm);
      &#125;
      <span class="hljs-comment">// proxy data on instance</span>
      <span class="hljs-keyword">var</span> keys = <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">keys</span>(data);
      <span class="hljs-keyword">var</span> props = vm.<span class="hljs-property">$options</span>.<span class="hljs-property">props</span>;
      <span class="hljs-keyword">var</span> methods = vm.<span class="hljs-property">$options</span>.<span class="hljs-property">methods</span>;
      <span class="hljs-keyword">var</span> i = keys.<span class="hljs-property">length</span>;
      <span class="hljs-keyword">while</span> (i--) &#123;
          <span class="hljs-keyword">var</span> key = keys[i];
          &#123;
              <span class="hljs-keyword">if</span> (methods && <span class="hljs-title function_">hasOwn</span>(methods, key)) &#123;
                  <span class="hljs-title function_">warn$2</span>(<span class="hljs-string">"Method \""</span>.<span class="hljs-title function_">concat</span>(key, <span class="hljs-string">"\" has already been defined as a data property."</span>), vm);
              &#125;
          &#125;
          <span class="hljs-keyword">if</span> (props && <span class="hljs-title function_">hasOwn</span>(props, key)) &#123;
              <span class="hljs-title function_">warn$2</span>(<span class="hljs-string">"The data property \""</span>.<span class="hljs-title function_">concat</span>(key, <span class="hljs-string">"\" is already declared as a prop. "</span>) +
                      <span class="hljs-string">"Use prop default value instead."</span>, vm);
          &#125;
          <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!<span class="hljs-title function_">isReserved</span>(key)) &#123;
              <span class="hljs-title function_">proxy</span>(vm, <span class="hljs-string">"_data"</span>, key);
          &#125;
      &#125;
      <span class="hljs-comment">// observe data</span>
      <span class="hljs-keyword">var</span> ob = <span class="hljs-title function_">observe</span>(data);
      ob && ob.<span class="hljs-property">vmCount</span>++;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过校验后，会用<code>proxy</code>做了数据代理</p>
<ul>
<li>查看<code>proxy</code>定义</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">function</span> <span class="hljs-title function_">proxy</span>(<span class="hljs-params">target, sourceKey, key</span>) &#123;
      sharedPropertyDefinition.<span class="hljs-property">get</span> = <span class="hljs-keyword">function</span> <span class="hljs-title function_">proxyGetter</span>(<span class="hljs-params"></span>) &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>[sourceKey][key];
      &#125;;
      sharedPropertyDefinition.<span class="hljs-property">set</span> = <span class="hljs-keyword">function</span> <span class="hljs-title function_">proxySetter</span>(<span class="hljs-params">val</span>) &#123;
          <span class="hljs-variable language_">this</span>[sourceKey][key] = val;
      &#125;;
      <span class="hljs-comment">// 定义vm对象的key值</span>
      <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, sharedPropertyDefinition);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义了<code>get</code>,<code>set</code>方法，我们可以知道，当我们获取数据，通过<code>this.xxx</code>时，实际上访问的是new Vue 实例中的<code>_data</code>对象，实际上就是<code>this._data.xxx</code></p>
<h3 data-id="heading-2">构造自己的简易版实例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sharedPropertyDefinition = &#123;
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> &#123;&#125;,
  <span class="hljs-attr">set</span>: <span class="hljs-function">() =></span> &#123;&#125;
&#125;
<span class="hljs-comment">// vue中的代理方法</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">proxy</span>(<span class="hljs-params">target, sourceKey, key</span>) &#123;
  sharedPropertyDefinition.<span class="hljs-property">get</span> = <span class="hljs-keyword">function</span> <span class="hljs-title function_">proxyGetter</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>[sourceKey][key]
  &#125;
  sharedPropertyDefinition.<span class="hljs-property">set</span> = <span class="hljs-keyword">function</span> <span class="hljs-title function_">proxySetter</span>(<span class="hljs-params">val</span>) &#123;
    <span class="hljs-variable language_">this</span>[sourceKey][key] = val
  &#125;
  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, sharedPropertyDefinition)
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">initMethods</span>(<span class="hljs-params">vm, methods</span>) &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> methods) &#123;
    <span class="hljs-comment">// 省略类型检查</span>
    vm[key] = <span class="hljs-keyword">typeof</span> methods[key] !== <span class="hljs-string">'function'</span> ? noop : methods[key].<span class="hljs-title function_">bind</span>(vm)
  &#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">initData</span>(<span class="hljs-params">vm</span>) &#123;
  <span class="hljs-keyword">const</span> data = (vm.<span class="hljs-property">_data</span> = vm.<span class="hljs-property">$options</span>.<span class="hljs-property">data</span>)
  <span class="hljs-keyword">const</span> keys = <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">keys</span>(data)
  <span class="hljs-keyword">var</span> i = keys.<span class="hljs-property">length</span>
  <span class="hljs-keyword">while</span> (i--) &#123;
    <span class="hljs-comment">// ... 省略类型检查</span>
    <span class="hljs-keyword">var</span> key = keys[i]
    <span class="hljs-title function_">proxy</span>(vm, <span class="hljs-string">'_data'</span>, key)
  &#125;
&#125;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">MyVue</span>(<span class="hljs-params">options</span>) &#123;
  <span class="hljs-keyword">let</span> vm = <span class="hljs-variable language_">this</span>
  vm.<span class="hljs-property">$options</span> = options
  <span class="hljs-keyword">const</span> opts = vm.<span class="hljs-property">$options</span>
  <span class="hljs-keyword">if</span> (opts.<span class="hljs-property">methods</span>) &#123;
    <span class="hljs-title function_">initMethods</span>(vm, opts.<span class="hljs-property">methods</span>)
  &#125;
  <span class="hljs-keyword">if</span> (opts.<span class="hljs-property">data</span>) &#123;
    <span class="hljs-title function_">initData</span>(vm)
  &#125;
&#125;

<span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MyVue</span>(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello JueJin'</span>
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-title function_">getMessage</span>(<span class="hljs-params"></span>) &#123;
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">message</span>)
    &#125;
  &#125;
&#125;)

vm.<span class="hljs-title function_">getMessage</span>() <span class="hljs-comment">// Hello JueJin</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">总结</h3>
<p>这个章节，我们尝试去看<code>vue2</code>的源码</p>
<ul>
<li>通过<code>bind</code>的函数去绑定方法</li>
<li>通过自定义<code>proxy</code>的方式去将<code>this</code>指向<code>vue</code>实例中的<code>_data</code>，从而实现<code>this.xxx</code>访问属性。</li>
<li>然后，我们用了一小段代码来实现了这个简易版的<code>vue</code>功能</li>
</ul></div>  
</div>
            