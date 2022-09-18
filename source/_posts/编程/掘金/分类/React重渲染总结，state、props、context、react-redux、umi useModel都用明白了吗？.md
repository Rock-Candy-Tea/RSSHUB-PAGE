
---
title: 'React重渲染总结，state、props、context、react-redux、umi useModel都用明白了吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7b5c29b73c04b80a6c87a2a7b92d5bf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sun, 18 Sep 2022 01:40:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7b5c29b73c04b80a6c87a2a7b92d5bf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<p>这篇文章主要<strong>探讨和组件重渲染有关的种种问题，以解决日常开发中的疑问，做到心中有🌲</strong>。文章中包含了日常开发中常用的state，props，context，react-redux以及umi usemodel等和组件状态有关的实践，并浅述了一些原理。（只针对函数式组件哦～）</p>
<p><strong>目录</strong></p>
<ol>
<li>什么是组件重渲染？</li>
<li>引起组件重渲染的原因有哪些？</li>
<li>如何避免不必要的重渲染？</li>
<li>使用 react-redux 要注意什么？</li>
<li>使用 umi useModel 要注意什么？</li>
</ol>
<h1 data-id="heading-0">什么是组件重渲染？</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">component</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> [state, setState] = <span class="hljs-title function_">useState</span>(<span class="hljs-number">0</span>);
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'component render'</span>);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;state&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如代码所示，不管是第一次渲染或是state改变，都会触发这个组件函数的执行，控制台将打印“component render”。函数组件执行后返回一个JSX，后面react将执行一系列操作以更新页面UI。除去第一次渲染，后面每次组件函数的执行我们都叫做这个组件的重渲染。</p>
<h1 data-id="heading-1">引起组件重渲染的原因有哪些？</h1>
<p>原因可以归为以下三点：</p>
<ol>
<li><strong>组件本身的state改变</strong></li>
<li><strong>父组件重渲染</strong></li>
<li><strong>context改变</strong></li>
</ol>
<h2 data-id="heading-2">1. 组件本身的state改变</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7b5c29b73c04b80a6c87a2a7b92d5bf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="img" loading="lazy" referrerpolicy="no-referrer">
如图，调用 <code>setState</code> 改变 state 值时将触发组件的重渲染。不过，如果调用 setState 时传入了一个相同的值，如<code>setState(state => state)</code>，则不会触发重渲染。<code>useReducer</code>同理，当调用 <code>dispatch</code>修改state值时也将触发组件重渲染。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [state, dispatch] = <span class="hljs-title function_">useReducer</span>(reducer, initialArg, init);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，还有一些隐藏起来的state，比如自定义hook。以官方给的自定义hook为例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 自定义hook</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">useFriendStatus</span>(<span class="hljs-params">friendID</span>) &#123;
  <span class="hljs-keyword">const</span> [isOnline, setIsOnline] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">null</span>);

  <span class="hljs-title function_">useEffect</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">function</span> <span class="hljs-title function_">handleStatusChange</span>(<span class="hljs-params">status</span>) &#123;
      <span class="hljs-title function_">setIsOnline</span>(status.<span class="hljs-property">isOnline</span>);
    &#125;

    <span class="hljs-title class_">ChatAPI</span>.<span class="hljs-title function_">subscribeToFriendStatus</span>(friendID, handleStatusChange);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-title class_">ChatAPI</span>.<span class="hljs-title function_">unsubscribeFromFriendStatus</span>(friendID, handleStatusChange);
    &#125;;
  &#125;);

  <span class="hljs-keyword">return</span> isOnline;
&#125;

<span class="hljs-comment">// 组件中使用</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">FriendStatus</span>(<span class="hljs-params">props</span>) &#123;
  <span class="hljs-keyword">const</span> isOnline = <span class="hljs-title function_">useFriendStatus</span>(props.<span class="hljs-property">friend</span>.<span class="hljs-property">id</span>);
  <span class="hljs-keyword">if</span> (isOnline === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'Loading...'</span>;
  &#125;
  <span class="hljs-keyword">return</span> isOnline ? <span class="hljs-string">'Online'</span> : <span class="hljs-string">'Offline'</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件中使用<code>useFriendStatus</code>也可能引起重渲染，不过其根本原因也是因为<code>useState</code>中的状态改变了。</p>
<h2 data-id="heading-3">2. 父组件重渲染</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ac4b6ea47d4445884e246025f4061e3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="img" loading="lazy" referrerpolicy="no-referrer">
如图，父组件的重渲染也将引起所有子组件的重渲染。但反过来，子组件的重渲染不会影响父组件。父组件可以通过props传值给子组件，但这和重渲染没有直接关系。在下图中，即使<code>value</code>值没有变化，父组件重渲染仍然会引起子组件的重渲染。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/724f01d7c64344c4b488935bd99ccc5b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">3. context改变</h2>
<p>当一个Context Provider中的值改变时，所有使用了这个Context的组件都将重渲染，即使它们没有直接用到Context中改变的那部分值。如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">App</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">AppContext.Provider</span>
      <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;contextValue&#125;</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">Component1</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">Component2</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">AppContext.Provider</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">const</span> <span class="hljs-title function_">Component1</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> &#123; value1 &#125; = <span class="hljs-title function_">useContext</span>(<span class="hljs-title class_">AppContext</span>); <span class="hljs-comment">// AppContextValue.value2变化也将导致这个组件的重渲染</span>
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;;

<span class="hljs-keyword">const</span> <span class="hljs-title function_">Component1</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> &#123; value2 &#125; = <span class="hljs-title function_">useContext</span>(<span class="hljs-title class_">AppContext</span>);<span class="hljs-comment">// AppContextValue.value1变化也将导致这个组件的重渲染</span>
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码示例中，当 contextValue 改变时，Component1和Component2都会重渲染，即使它们用到的<code>value1</code>或<code>value2</code>并没有改变。</p>
<h1 data-id="heading-5">🌟如何避免不必要的重渲染？</h1>
<p>一个组件的重渲染可能做两件事情，一是更新页面内容（DOM），二是执行hook，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">Component</span> = (<span class="hljs-params">props</span>) => &#123;
  <span class="hljs-comment">// 执行 hook</span>
  <span class="hljs-title function_">useEffect</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-variable language_">document</span>.<span class="hljs-property">title</span> = props.<span class="hljs-property">title</span>;
  &#125;, [props.<span class="hljs-property">title</span>]);

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;props.title&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>; <span class="hljs-comment">// 更新页面内容</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而如果一个组件触发了重渲染，却一没有页面内容更新，二没有执行hook逻辑，那么这次重渲染就是没有任何作用的，也就是不必要的重渲染。但实际开发中，这种情况常常发生，比如你在一个input框中输入内容，结果整个页面的组件都在重渲染（但由于React做了优化，这种看起来“高代价”的重渲染实际上对用户体验影响不大）。</p>
<p>那如何避免不必要的重渲染呢？我们可以分别从上面三个引起组件重渲染的原因入手。</p>
<h2 data-id="heading-6">1. 组件内部状态变化🤔</h2>
<p>组件内部的state改变会使组件重渲染，所以我们只要记住<strong>只在需要的时候使用state</strong>即可。如果一些值的变化对页面渲染无影响，那么我们可以将这些值维护在函数组件外，或使用<code>useRef</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> value = &#123;&#125;; <span class="hljs-comment">// 这里的值改变不会影响组件渲染</span>

<span class="hljs-keyword">const</span> <span class="hljs-title function_">App</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> valueRef = <span class="hljs-title function_">useRef</span>(); <span class="hljs-comment">// 这里的值改变不会影响组件渲染</span>
  
  <span class="hljs-comment">//...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">2. 父组件重渲染😨</h2>
<p>这一部分需要注意的就比较多了，而且经常是容易忽略的部分。</p>
<h3 data-id="heading-8">state影响最小化原则</h3>
<p><strong>方法一：抽离子组件</strong>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef3869bd218467597b7bff890f9942d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如图所示，父组件中的状态变化将导致所有子组件的重渲染，但如果将这个state抽离到一个子组件中，那它影响的范围就变小了。所以抽离组件是一个好习惯，这样state变化只会影响到和它相关的组件。</p>
<p><strong>方法二：将组件作为props</strong>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8451afd7021c451486d5e1d09c34b7e7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这种方法同样也是抽离组件，只不过方式和第一种不同。这里将原组件变成了一个高阶组件，并将没有用到state的组件抽离出去，通过props传入。其实同理，也是将state的影响最小化。</p>
<h3 data-id="heading-9">使用缓存</h3>
<p>相比抽离组件，一种更简单的方法是使用React.memo。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0562ff5b358b4884a8d510d3e81eef0a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在上图中，使用<code>React.memo</code>包裹子组件后，父组件的重渲染将不会影响子组件。然而，当子组件接收props时，我们却需要额外注意了。</p>
<p>如果props为基本类型，如字符串或数字，则不需要做任何处理。但如果props为对象、数组或函数等类型时，则需要引入useMemo或useCallback。因为这类变量在每次组件函数执行时都会更新，就像<code>&#123;&#125; !== &#123;&#125;</code>，所以需要对这类变量进行缓存。如下图所示：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3d88db50cda4a2b9964fc6a8d06484c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
不过，使用useMemo，useCallback以及React.memo本身也是有开销的，在一些简单场景下使用它们可能并不会有性能上的提升，所以切记不要滥用。</p>
<p>在一个组件内我们也可以单独使用useMemo来对开销大的子组件做缓存优化，如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f92d50eb7ac48ddbd177a3ae61d4a9f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">3. 使用context😣</h2>
<p>前面有提到，当Context Provider中的值改变时，所有使用了这个Context的组件都将重渲染。由于这个特性，使用context时很容易就产生不必要的重渲染。但下面有一些方法可以帮助我们缓解这个问题。</p>
<h3 data-id="heading-11">缓存context值</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3572e981670c4b42b52496ec0a5a3623~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如上图所示，如果Context Provider的value值不是基本类型，我们可以将这个值进行缓存，这样可以避免组件重渲染时改变context值。</p>
<h3 data-id="heading-12">分离Context</h3>
<p>前面有提到state影响最小化，使用context时也是一样。我们可以将一个context进行拆分来避免不必要的重渲染。</p>
<p>在下图右侧的示例中，通过拆分conetext，<code>first</code>和<code>second</code>就不会相互影响了。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/162227dc779e4e0d844463508eb80bea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同理，我们也可以将data与setData的context分开。如下图，右侧示例中使用ApiContext的组件不会因为DataContext的值改变而重渲染。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a9cf57c480d4a219c4bb96a52b485ac~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">在context消费者中使用缓存</h3>
<p>如果不能拆分context，我们也可以通过缓存来避免重渲染。如下面两个示例所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">Button</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> appContextValue = <span class="hljs-title function_">useContext</span>(<span class="hljs-title class_">AppContext</span>);
  <span class="hljs-keyword">const</span> theme = appContextValue.<span class="hljs-property">theme</span>; <span class="hljs-comment">// Your "selector"</span>
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ThemedButton</span> <span class="hljs-attr">theme</span>=<span class="hljs-string">&#123;theme&#125;</span> /></span></span>
&#125;

<span class="hljs-keyword">const</span> <span class="hljs-title class_">ThemedButton</span> = <span class="hljs-title function_">memo</span>(<span class="hljs-function">(<span class="hljs-params">&#123; theme &#125;</span>) =></span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ExpensiveTree</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;theme&#125;</span> /></span></span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">Button</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> appContextValue = <span class="hljs-title function_">useContext</span>(<span class="hljs-title class_">AppContext</span>);
  <span class="hljs-keyword">const</span> theme = appContextValue.<span class="hljs-property">theme</span>; <span class="hljs-comment">// Your "selector"</span>

  <span class="hljs-keyword">return</span> <span class="hljs-title function_">useMemo</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ExpensiveTree</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;theme&#125;</span> /></span></span>;
  &#125;, [theme])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">使用 react-redux</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.redux.js.org%2Ftutorials%2Ffundamentals%2Fpart-1-overview" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.redux.js.org/tutorials/fundamentals/part-1-overview" ref="nofollow noopener noreferrer">redux</a>是一个管理和更新应用状态的模式和工具库，它可以搭配react一起使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Provider</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>;

<span class="hljs-comment">// redux的数据store</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span> ></span>
   <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码所示，官方建议<strong>一个应用中所有的数据都维护在一个公共的store中</strong>。那我们不禁疑问，它有没有类似context的问题呢？会不会部分数据的改变也会导致所有数据的消费者都受影响呢？</p>
<p>这里我们就需要了解一个重要的概念了——<strong>selector</strong>（选择器）。</p>
<h2 data-id="heading-15">使用useSelector读取state</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">selectStatus</span> = (<span class="hljs-params">state</span>) => state.<span class="hljs-property">counter</span>.<span class="hljs-property">status</span>; <span class="hljs-comment">// 一个selector</span>
<span class="hljs-keyword">const</span> status = <span class="hljs-title function_">useSelector</span>(selectStatus);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.redux.js.org%2Ftutorials%2Ffundamentals%2Fpart-5-ui-react%23%25E4%25BD%25BF%25E7%2594%25A8-useselector-%25E4%25BB%258E-store-%25E4%25B8%25AD%25E8%25AF%25BB%25E5%258F%2596-state" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.redux.js.org/tutorials/fundamentals/part-5-ui-react#%E4%BD%BF%E7%94%A8-useselector-%E4%BB%8E-store-%E4%B8%AD%E8%AF%BB%E5%8F%96-state" ref="nofollow noopener noreferrer">useSelector</a> 可以将组件更新仅与选择的这部分数据绑定</strong>。如果 selector 返回的值与上次运行时相比发生了变化，<code>useSelector</code> 将强制组件使用新值重新渲染，反之则没有任何影响。这样就避免了context的问题。</p>
<p>这里state影响最小化原则同样适用，即selector返回的值是组件需要用到的最小范围值。下面有一些好的做法🙂️和一些不好的做法🙁️：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// bad 🙁️ 多选择了</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">selectCounter</span> = (<span class="hljs-params">state</span>) => state.<span class="hljs-property">counter</span>;
<span class="hljs-keyword">const</span> arr = <span class="hljs-title function_">useSelector</span>(selectCounter).<span class="hljs-property">arr</span>; <span class="hljs-comment">// 只用到 counter.arr！</span>

<span class="hljs-comment">// good 🙂️ 选择的刚刚好</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">selectArr</span> = (<span class="hljs-params">state</span>) => state.<span class="hljs-property">counter</span>.<span class="hljs-property">arr</span>;
<span class="hljs-keyword">const</span> arr = <span class="hljs-title function_">useSelector</span>(selectArr);

<span class="hljs-comment">// bad 🙁️ 多选择了</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">selectArr</span> = (<span class="hljs-params">state</span>) => state.<span class="hljs-property">counter</span>.<span class="hljs-property">arr</span>;
<span class="hljs-keyword">const</span> arrlength = <span class="hljs-title function_">useSelector</span>(selectArr).<span class="hljs-property">length</span>; <span class="hljs-comment">// 只用到 counter.arr.length！</span>

<span class="hljs-comment">// good 🙂️ 选择的刚刚好</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">selectArrLength</span> = (<span class="hljs-params">state</span>) => state.<span class="hljs-property">counter</span>.<span class="hljs-property">arr</span>.<span class="hljs-property">length</span>;
<span class="hljs-keyword">const</span> arrlength = <span class="hljs-title function_">useSelector</span>(selectArrLength);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">在selector中使用自定义比较</h2>
<p>需要注意，<strong><code>useSelector</code> 使用严格的 <code>===</code> 来比较结果，因此只要 selector 函数返回的结果是新地址引用，组件就会重新渲染！</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// bad 🙁️</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">selectTodoDescriptions</span> = state => &#123;
  <span class="hljs-comment">// 这会创建一个新的数组引用！</span>
  <span class="hljs-keyword">return</span> state.<span class="hljs-property">todos</span>.<span class="hljs-title function_">map</span>(<span class="hljs-function"><span class="hljs-params">todo</span> =></span> todo.<span class="hljs-property">text</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以使用<code>useSelector</code>的第二个参数来自定义比较函数，从而避免不必要的重渲染。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// react-redux中有一个shallowEqual函数可以对数组和对象进行浅层比较</span>
<span class="hljs-keyword">const</span> todoIds = <span class="hljs-title function_">useSelector</span>(selectTodoIds, shallowEqual);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>另外，还可以使用一种称为<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.redux.js.org%2Ftutorials%2Ffundamentals%2Fpart-7-standard-patterns" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.redux.js.org/tutorials/fundamentals/part-7-standard-patterns" ref="nofollow noopener noreferrer">"记忆（memoized）selector"</a> 的特殊 selector 函数来改进组件渲染。</p>
</blockquote>
<p><strong>【多说一句】</strong> 为什么react-redux没有context的问题呢？原因是虽然react-redux里用了context来传递store的值，但并没有通过更新store值来更新UI，而是实现了一套发布订阅模式，根据seletor的值变化来更新，这样就避免了context的问题。这里可以参考一个简单版本的实现<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fpeaceful-river-dj5ps" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/peaceful-river-dj5ps" ref="nofollow noopener noreferrer">代码</a>。而在最新版本的react-redux 8中，使用了react18的<code>use-sync-external-store</code>API来替换这套逻辑，其原因还稍微复杂一些，这里就不细究了（赶紧去学习🫢）。</p>
<h1 data-id="heading-17">使用 umi useModel</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.umijs.org%2Fzh-CN" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.umijs.org/zh-CN" ref="nofollow noopener noreferrer">umi</a>的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.umijs.org%2Fzh-CN%2Fplugins%2Fplugin-model" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.umijs.org/zh-CN/plugins/plugin-model" ref="nofollow noopener noreferrer">useModel</a>同样是一个全局状态的管理方案，不过它相比redux更轻量，使用也简单很多。即然是全局状态，那也得扣一扣问题了。下面是一个<code>useModel</code>的使用示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 一个自定义的useModel</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">useValueModel</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> [value1, setValue1] = <span class="hljs-title function_">useState</span>(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [value2, setValue2] = <span class="hljs-title function_">useState</span>(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">return</span> &#123;
    value1,
    setValue1,
    value2,
    setValue2,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件中使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">Component1</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> &#123; value1, setValue1 &#125; = <span class="hljs-title function_">useModel</span>(<span class="hljs-string">'useValueModel'</span>);
&#125;;

<span class="hljs-keyword">const</span> <span class="hljs-title function_">Component2</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> &#123; value2, setValue2 &#125; = <span class="hljs-title function_">useModel</span>(<span class="hljs-string">'useValueModel'</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过前面的铺垫，相信大家对这里也会有疑问，<code>value1</code>变化会不会影响使用<code>value2</code>的组件呢？答案是，会的！解决方法和前面类似，使用selector。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> &#123; value1, setValue1 &#125; = <span class="hljs-title function_">useModel</span>(<span class="hljs-string">'useValueModel'</span>, <span class="hljs-function">(<span class="hljs-params">model</span>) =></span> (&#123;
    <span class="hljs-attr">value1</span>: model.<span class="hljs-property">value1</span>,
    <span class="hljs-attr">setValue1</span>: model.<span class="hljs-property">setValue1</span>,
  &#125;)); <span class="hljs-comment">// 第二个参数是selector，只在选择的状态变化时才更新</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>【多说一句】</strong> useModel是怎么实现的呢？seletor的原理又是什么呢？看了下源码，useModel中也使用了context传递数据，但传入的Context Provider的值是一个不变的对象（又是这一招😄）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> dispatcher = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Dispatcher</span>!();
<span class="hljs-comment">//...</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">UmiContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;dispatcher&#125;</span>></span>...<span class="hljs-tag"></<span class="hljs-name">UmiContext.Provider</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么数据更新怎么触发视图更新呢，方法还是发布订阅。订阅就在useModel里实现了（源码 <em>.umi/plugin-model/useModel.tsx</em>），它将回调绑定在了特定的namespace上，比如下面的<code>useValueModel</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; value1, setValue1 &#125; = <span class="hljs-title function_">useModel</span>(<span class="hljs-string">'useValueModel'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而发布靠的是react原生的hook（源码 <em>.umi/plugin-model/helpers/executor.tsx</em>），当<code>setValue1</code>执行时，将执行<code>useValueModel</code>这个namespace的回调函数，从而触发视图更新。回调函数的核心逻辑如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 如果存在updater（即selector），则对比前后的state</span>
<span class="hljs-keyword">if</span>(updater && updaterRef.<span class="hljs-property">current</span>)&#123;
  <span class="hljs-keyword">const</span> currentState = updaterRef.<span class="hljs-title function_">current</span>(e);
  <span class="hljs-keyword">const</span> previousState = stateRef.<span class="hljs-property">current</span>
  <span class="hljs-keyword">if</span>(!<span class="hljs-title function_">isEqual</span>(currentState, previousState))&#123;
    <span class="hljs-title function_">setState</span>(currentState); <span class="hljs-comment">// 通过react setState更新视图</span>
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-title function_">setState</span>(e); <span class="hljs-comment">// 通过react setState更新视图</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-18">总结</h1>
<p>虽然上面有那么多示例，但也可以用几句话总结。</p>
<ul>
<li>将state影响最小化，抽离组件或拆分状态</li>
<li>合理使用缓存</li>
<li>全局状态使用注意添加<strong>selector</strong></li>
</ul>
<p>其实很多项目中过早的使用优化手段并没有必要，但了解一些优秀的实践和内部的原理还是大有裨益的，做到心中有🌲。</p>
<h1 data-id="heading-19">参考</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.developerway.com%2Fposts%2Freact-re-renders-guide" target="_blank" rel="nofollow noopener noreferrer" title="https://www.developerway.com/posts/react-re-renders-guide" ref="nofollow noopener noreferrer">react-re-renders-guide</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-redux.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react-redux.js.org/" ref="nofollow noopener noreferrer">react redux</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fissues%2F15156%23issuecomment-474590693" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/issues/15156#issuecomment-474590693" ref="nofollow noopener noreferrer">Preventing rerenders with React.memo and useContext hook</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2Fasync%2Fhow-useselector-can-trigger-an-update-only-when-we-want-it-to-a8d92306f559" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/async/how-useselector-can-trigger-an-update-only-when-we-want-it-to-a8d92306f559" ref="nofollow noopener noreferrer">How useSelector can trigger an update only when we want it to</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.redux.js.org%2Ftutorials%2Ffundamentals%2Fpart-1-overview" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.redux.js.org/tutorials/fundamentals/part-1-overview" ref="nofollow noopener noreferrer">Redux 深入浅出</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F502917860" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/502917860" ref="nofollow noopener noreferrer">如何理解 React 18 中的 useSyncExternalStore？</a></li>
</ul></div>  
</div>
            