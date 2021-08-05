
---
title: 'element 穿梭框性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 15:42:56 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>陈建波： 被写代码耽误的炉石玩家</p>
</blockquote>
<h1 data-id="heading-0">element 穿梭框性能优化</h1>
<h3 data-id="heading-1">背景</h3>
<p>穿梭框处理大数据量时,由于渲染的 DOM 节点过多，造成页面卡顿的问题。
在尽量不改变组件原有逻辑的前提下，进行优化。</p>
<h3 data-id="heading-2">解决思路</h3>
<p>懒加载 - InfiniteScroll 组件</p>
<p>先从 packages/transfer 中将原组件拷出（或者改源码重新打包维护私有库使用）</p>
<p>将</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        v-infinite-scroll=<span class="hljs-string">"pageDown"</span>
        :infinite-scroll-immediate=<span class="hljs-string">"false"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加到</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><el-checkbox-group
        v-show=<span class="hljs-string">"!hasNoMatch && data.length > 0"</span>
        v-model=<span class="hljs-string">"checked"</span>
        :size=<span class="hljs-string">"size"</span>
        :<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"&#123; 'is-filterable': filterable &#125;"</span>
        <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"el-transfer-panel__list"</span>
        v-infinite-scroll=<span class="hljs-string">"pageDown"</span>
        :infinite-scroll-immediate=<span class="hljs-string">"false"</span>
      >
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-checkbox</span>
          <span class="hljs-attr">class</span>=<span class="hljs-string">"el-transfer-panel__item"</span>
          <span class="hljs-attr">:label</span>=<span class="hljs-string">"item[keyProp]"</span>
          <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"item[disabledProp]"</span>
          <span class="hljs-attr">:key</span>=<span class="hljs-string">"item[keyProp]"</span>
          <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in filteredData"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">option-content</span> <span class="hljs-attr">:option</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"></<span class="hljs-name">option-content</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-checkbox</span>></span></span>
</el-checkbox-group>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>data</code>中定义
<code>pageSize: 20</code> 用来表示每页数据个数
<code>showData: []</code> 仅用来展示使用，替换上述代码中实际需要操作的数据 <code>filteredData</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> v-<span class="hljs-keyword">for</span>=<span class="hljs-string">"item in showData"</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时在<code>watch</code>中相应的处理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">data (data) &#123;
    <span class="hljs-keyword">const</span> checked = [];
    <span class="hljs-built_in">this</span>.showData = data.slice(<span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.pageSize);

    <span class="hljs-keyword">const</span> filteredDataKeys = <span class="hljs-built_in">this</span>.filteredData.map(
    <span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item[<span class="hljs-built_in">this</span>.keyProp]
    );
    <span class="hljs-built_in">this</span>.checked.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (filteredDataKeys.indexOf(item) > -<span class="hljs-number">1</span>) &#123;
        checked.push(item);
    &#125;
    &#125;);
    <span class="hljs-built_in">this</span>.checkChangeByUser = <span class="hljs-literal">false</span>;
    <span class="hljs-built_in">this</span>.checked = checked;
&#125;,
filteredData (filteredData) &#123;
    <span class="hljs-built_in">this</span>.showData = filteredData.slice(<span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.pageSize);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化展示数量随意这里取 20。</p>
<p>最后添加滚动到底部时调用的方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">pageDown () &#123;
    <span class="hljs-keyword">const</span> l = <span class="hljs-built_in">this</span>.showData.length;
    <span class="hljs-keyword">const</span> totalLength = <span class="hljs-built_in">this</span>.filteredData.length
    l < totalLength && 
    (<span class="hljs-built_in">this</span>.showData = <span class="hljs-built_in">this</span>.filteredData.slice(<span class="hljs-number">0</span>, l + <span class="hljs-built_in">this</span>.pageSize > totalLength ?
    totalLength : l + <span class="hljs-built_in">this</span>.pageSize));
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>往下滚动的时候 展示的数据长度增加 20（数量随意）, 超出时展示最大长度。</p>
<p>由此基本解决大数据量操作卡顿的问题。由于展示和逻辑层分开，组件的所有操作逻辑无须修改，最小程度减少差异。</p>
<h3 data-id="heading-3">新问题</h3>
<p>手动滚动到列表末端，再进行搜索操作依然存在卡顿问题。</p>
<h3 data-id="heading-4">进阶</h3>
<p>在滚动过程中，实际上顶端的数据依旧无法看见，该数据不展示，对用户体验也没有影响，
所以只需展示当前页的 20 条数据。
我们为<code>el-checkbox-group</code>添加一个 <code>ref=scrollContainer</code> 以便操作滚动条，</p>
<p>在<code>data</code>中定义当前页数 <code>curIndex: 1</code></p>
<p>并对 <code>pageDown</code> 方法进行修改</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    pageDown () &#123;
      <span class="hljs-keyword">const</span> totalLength = <span class="hljs-built_in">this</span>.filteredData.length
      <span class="hljs-keyword">if</span>((<span class="hljs-built_in">this</span>.curIndex*<span class="hljs-built_in">this</span>.pageSize) < totalLength)&#123;
        <span class="hljs-built_in">this</span>.curIndex ++
        <span class="hljs-keyword">const</span> targetLength = <span class="hljs-built_in">this</span>.curIndex * <span class="hljs-built_in">this</span>.pageSize 
        <span class="hljs-keyword">const</span> endPoint = targetLength > totalLength ? totalLength : targetLength
        <span class="hljs-keyword">const</span> startPoint = endPoint - <span class="hljs-built_in">this</span>.pageSize  > <span class="hljs-number">0</span> ? endPoint - <span class="hljs-built_in">this</span>.pageSize : <span class="hljs-number">0</span>
        <span class="hljs-built_in">this</span>.showData = <span class="hljs-built_in">this</span>.filteredData.slice(startPoint, endPoint);
        <span class="hljs-built_in">this</span>.$refs.scrollContainer.$el.scrollTop = <span class="hljs-string">"1px"</span> <span class="hljs-comment">//滚动条到最上端，衔接下一页，为 0 可能会触发边界问题</span>
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为此我们还需要添加向上翻页的方法
InfiniteScroll 指令 只提供向下滚动，我们可以拓展该指令亦可自行添加上滑滚动监听</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$refs.scrollContainer.$el.addEventListener(<span class="hljs-string">'scroll'</span>, <span class="hljs-built_in">this</span>.pageUp)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">beforeDestroy</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$refs.scrollContainer.$el.removeEventListener(<span class="hljs-string">'scroll'</span>, <span class="hljs-built_in">this</span>.pageUp)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注册<code>pageUp</code> 方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">pageUp</span>(<span class="hljs-params">e</span>)</span>&#123;
      <span class="hljs-keyword">if</span>(e.target.scrollTop ===<span class="hljs-number">0</span> && <span class="hljs-built_in">this</span>.curIndex><span class="hljs-number">1</span>)&#123;
        <span class="hljs-built_in">this</span>.curIndex --
        <span class="hljs-keyword">const</span> endPoint = <span class="hljs-built_in">this</span>.curIndex * <span class="hljs-built_in">this</span>.pageSize 
        <span class="hljs-keyword">const</span> startPoint = (<span class="hljs-built_in">this</span>.curIndex-<span class="hljs-number">1</span>)* <span class="hljs-built_in">this</span>.pageSize 
        <span class="hljs-built_in">this</span>.showData = <span class="hljs-built_in">this</span>.filteredData.slice(startPoint, endPoint);
        <span class="hljs-keyword">const</span> el = <span class="hljs-built_in">this</span>.$refs.scrollContainer.$el
        el.scrollTop = el.scrollHeight - el.clientHeight - <span class="hljs-number">1</span> <span class="hljs-comment">// 滚动到最底部，衔接上一页， -1 防止边界问题。</span>
      &#125;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当进行数据操作的时候，页面内容变化，滚动条也会随之变化，为防止不能预知的翻页，数据改变时，重置滚动条和当前页码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">initScroll</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.curIndex = <span class="hljs-number">1</span>
        <span class="hljs-built_in">this</span>.$refs.scrollContainer.$el.scrollTop = <span class="hljs-number">0</span>
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时地，在<code>watch</code>中相应时候执行 initScroll</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        ...
        <span class="hljs-built_in">this</span>.initScroll()
        ...
    &#125;,
    filteredData (filteredData) &#123;
      ...
      <span class="hljs-built_in">this</span>.initScroll()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此大数据量的穿梭框，性能大为改善。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/908fe137298a4f0e97ff785f04243fc8~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="3_自定义px_2021-08-04-0.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            