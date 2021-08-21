
---
title: '_React_--组件封装、父子组件传值、redux持久化保存公共数据、类v-model实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/731e17fa89c64156b533e16f4c1f9ded~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 00:32:49 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/731e17fa89c64156b533e16f4c1f9ded~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第9天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h1 data-id="heading-0">一、 react中父子组件传值</h1>
<h2 data-id="heading-1">1. 一个搜素组件利用父子组件传值实现隐藏显示功能</h2>
<h3 data-id="heading-2">1. 传递样式可以通过display：none，来隐藏搜索子组件，子组件通过props来接受</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 父组件中</span>
 <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">searchComponentStyle</span>: &#123;
                <span class="hljs-attr">display</span>: <span class="hljs-string">'none'</span>
            &#125;
        &#125;
<SearchComponent pageStyle=&#123;<span class="hljs-built_in">this</span>.state.searchComponentStyle&#125;></SearchComponent>

<span class="hljs-comment">// 子组件中</span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'component-search'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;this.props.pageStyle&#125;</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2. 子组件通过调用父组件的方法来实现传值隐藏功能</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 子组件中</span>
 <div className=<span class="hljs-string">"close-btn"</span> onClick=&#123;<span class="hljs-built_in">this</span>.props.changeStyle.bind(<span class="hljs-built_in">this</span>,<span class="hljs-string">'none'</span>)&#125;></div>
<span class="hljs-comment">// 父组件中</span>
 <span class="hljs-comment">// 显示隐藏搜索组件</span>
    <span class="hljs-function"><span class="hljs-title">changeSearchComponentShow</span>(<span class="hljs-params">style =<span class="hljs-string">'block'</span></span>)</span> &#123;
    
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">searchComponentStyle</span>: &#123;
                <span class="hljs-attr">display</span>: style
            &#125;
        &#125;)
    &#125;
  <div className=<span class="hljs-string">"search-container"</span> onClick=&#123; <span class="hljs-built_in">this</span>.changeSearchComponentShow.bind(<span class="hljs-built_in">this</span>,<span class="hljs-string">'block'</span>)&#125;>
                        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"search-btn"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
                        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"search-holder"</span>></span>请输入宝贝名称<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
                    </div>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/731e17fa89c64156b533e16f4c1f9ded~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-08-21 at 12.15.47.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">二、 在react中使用ant-mobile</h1>
<h2 data-id="heading-5">1. 安装npm install antd-mobile --save</h2>
<h2 data-id="heading-6">2. 按需引入安装： npm install babel-plugin-import --save-dev</h2>
<h3 data-id="heading-7">2.1 配置package.json中的babel</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"babel"</span>: &#123;
    <span class="hljs-string">"presets"</span>: [
      <span class="hljs-string">"react-app"</span>
    ],
    <span class="hljs-string">"plugins"</span>: [
      [
        <span class="hljs-string">"import"</span>,
        &#123;
          <span class="hljs-string">"libraryName"</span>: <span class="hljs-string">"antd-mobile"</span>,
          <span class="hljs-string">"style"</span>: <span class="hljs-string">"css"</span>
        &#125;
      ]
    ]
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.2 使用搜索组件删除历史记录的对话框</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span>  &#123;Modal&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd-mobile'</span>
<div className=<span class="hljs-string">"delete-icon"</span>  onClick=&#123;<span class="hljs-built_in">this</span>.openConfirmDeleteDialog.bind(<span class="hljs-built_in">this</span>)&#125;></div>
 <span class="hljs-comment">// 打开删除确认弹框</span>
    <span class="hljs-function"><span class="hljs-title">openConfirmDeleteDialog</span>(<span class="hljs-params"></span>)</span> &#123;
        Modal.alert(<span class="hljs-string">'确认要删除吗？'</span>,<span class="hljs-string">''</span>,[
            &#123;
                <span class="hljs-attr">text</span>:<span class="hljs-string">'取消'</span>,
                <span class="hljs-attr">onPress</span>: <span class="hljs-function">() =></span> &#123;&#125;
            &#125;,&#123;
                <span class="hljs-attr">text</span>:<span class="hljs-string">'确认'</span>,
                <span class="hljs-attr">onPress</span>: <span class="hljs-function">() =></span> &#123;&#125;
            &#125;,
        ])
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/829fd9749f5d4b94b04353f12924a87a~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-08-21 at 12.22.53.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">分模块使用redux</h1>
<ol>
<li>回顾在vuex的状态管理：</li>
</ol>
<p>无非是actions、mutation、state、getters这些，分模块加了个modules而已
2. 运用在readux中的状态管理：
少了state，getter，而用action和reducers代理
3. 运用redux的数据流</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 在src下建立actions和reducers两个目录，分模块方便后期公共数据的管理</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb34332ffe8748319d4f6e73100c2aa8~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-21 下午4.14.32.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最小粒度的redux分模块demo</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. actions</span>
<span class="hljs-comment">// historyKeywords.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addHistoryKeyword</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(data,<span class="hljs-string">'actions中来数据....'</span>)
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'addHistoryKeyword'</span>,
        data
    &#125;
&#125;

<span class="hljs-keyword">export</span>  &#123;
    addHistoryKeyword
&#125;
<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> historyKeywords <span class="hljs-keyword">from</span> <span class="hljs-string">"./historyKeywords"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    historyKeywords
&#125;

<span class="hljs-comment">// 2. reducers</span>
<span class="hljs-comment">// historyKeywords.js</span>
<span class="hljs-keyword">let</span> historyKeywords = <span class="hljs-built_in">localStorage</span>[<span class="hljs-string">'historyKeywords'</span>] ? <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>[<span class="hljs-string">'historyKeywords'</span>]) : []

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">historyKeywordsReducer</span>(<span class="hljs-params">state =&#123;historyKeywords&#125;,action</span>) </span>&#123;
    <span class="hljs-keyword">switch</span> (action.type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'addHistoryKeyword'</span>:
            <span class="hljs-built_in">console</span>.log(state,<span class="hljs-string">'原来的state'</span>)
            <span class="hljs-built_in">console</span>.log(action, <span class="hljs-string">'reducers中来数据...'</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.assign(&#123;&#125;,state,action),<span class="hljs-string">'后来的数据'</span>)
            <span class="hljs-keyword">return</span>   <span class="hljs-built_in">Object</span>.assign(&#123;&#125;,state,action)
        <span class="hljs-attr">default</span>:
            <span class="hljs-keyword">return</span>  state
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> historyKeywordsReducer

<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> &#123;combineReducers&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> historyKeywords <span class="hljs-keyword">from</span> <span class="hljs-string">"./historyKeywords"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> combineReducers(&#123;
    <span class="hljs-attr">hkReducers</span>:historyKeywords
&#125;)

<span class="hljs-comment">// 3. 入口文件的index.js</span>
<span class="hljs-comment">/*eslint-disable*/</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'babel-polyfill'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'url-search-params-polyfill'</span>;
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> RouterComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> serviceWorker <span class="hljs-keyword">from</span> <span class="hljs-string">'./serviceWorker'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./assets/js/libs/zepto.js"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./assets/css/common/public.css"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'whatwg-fetch'</span>
<span class="hljs-keyword">import</span> &#123;Provider&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>;
<span class="hljs-keyword">import</span> &#123;createStore&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> Reducers <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducers'</span>

<span class="hljs-keyword">let</span> store = createStore(Reducers)


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.Fragment</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">RouterComponent</span> /></span>
                <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">React.Fragment</span>></span></span>
        )
    &#125;
&#125;

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Index</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));

serviceWorker.unregister();

<span class="hljs-comment">// 4. 在业务组件中使用</span>
<span class="hljs-comment">// search.js 组件中</span>
<span class="hljs-keyword">import</span> &#123;connect&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>;
<span class="hljs-keyword">import</span> actions <span class="hljs-keyword">from</span> <span class="hljs-string">"../../actions"</span>;

<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
<span class="hljs-built_in">this</span>.historyKeywords = props.state.hkReducers.historyKeywords
&#125;
 
 <span class="hljs-comment">// 删除确认</span>
<span class="hljs-attr">onPress</span>: <span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">this</span>.setState(&#123;
                        <span class="hljs-attr">historyKeywordsShow</span>: <span class="hljs-literal">false</span>
                    &#125;)
                   <span class="hljs-built_in">this</span>.historyKeywords = []
                    <span class="hljs-built_in">this</span>.props.dispatch(actions.historyKeywords.addHistoryKeyword(&#123;
                        <span class="hljs-attr">historyKeywords</span>: <span class="hljs-built_in">this</span>.historyKeywords
                    &#125;))
                    <span class="hljs-built_in">localStorage</span>.removeItem(<span class="hljs-string">'historyKeywords'</span>)
                &#125;
  
  <span class="hljs-comment">// 添加</span>
  <span class="hljs-function"><span class="hljs-title">addHistoryKeywords</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.state.searchKeyword)&#123;
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">let</span> index  = <span class="hljs-built_in">this</span>.historyKeywords.findIndex(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v === <span class="hljs-built_in">this</span>.state.searchKeyword)
        <span class="hljs-keyword">if</span>(index !== -<span class="hljs-number">1</span>) &#123;
            <span class="hljs-built_in">this</span>.historyKeywords.splice(index,<span class="hljs-number">1</span>)
        &#125;
        <span class="hljs-built_in">this</span>.historyKeywords.unshift(<span class="hljs-built_in">this</span>.state.searchKeyword)
        <span class="hljs-built_in">this</span>.props.dispatch(actions.historyKeywords.addHistoryKeyword(&#123;<span class="hljs-attr">historyKeywords</span>:<span class="hljs-built_in">this</span>.historyKeywords &#125;))
        <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'historyKeywords'</span>,<span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-built_in">this</span>.historyKeywords))
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.state.historyKeywordsShow) &#123;
            <span class="hljs-built_in">this</span>.setState(&#123;
                <span class="hljs-attr">historyKeywordsShow</span>: <span class="hljs-literal">true</span>
            &#125;)
        &#125;
    &#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(<span class="hljs-function"><span class="hljs-params">state</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(state,<span class="hljs-string">'search中的state....'</span>)
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">state</span>:state
    &#125;
&#125;)(SearchComponent)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后补充下react没有像vue中的v-model我们自己实现</p>
<pre><code class="hljs language-js copyable" lang="js"> <input type=<span class="hljs-string">"text"</span>  onChange=&#123;<span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;<span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">searchKeyword</span>: event.target.value.trim()&#125;)&#125;&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16ca72d8a1094afeb07c5555ca3b8f48~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-08-21 at 16.25.45.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            