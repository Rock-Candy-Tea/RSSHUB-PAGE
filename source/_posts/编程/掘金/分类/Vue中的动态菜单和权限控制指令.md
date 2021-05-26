
---
title: 'Vue中的动态菜单和权限控制指令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eea55191d0354318ba9a06ff13244c69~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 18:44:39 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eea55191d0354318ba9a06ff13244c69~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h1 data-id="heading-0">业务场景</h1>
<p>需求可具体描述为如下内容:</p>
<ul>
<li>根据权限动态筛选路由</li>
<li>根据权限控制组件的是否展示</li>
</ul>
<p>我们默认后端权限接口可用, 且返回的是权限实体平铺数组, 并非树形结构</p>
<h1 data-id="heading-1">技术栈</h1>
<ul>
<li>Vue</li>
<li>Vuex</li>
<li>Vue Router</li>
<li>TypeScript</li>
</ul>
<p>都2021年啦, 不要再问用js怎么写了</p>
<h1 data-id="heading-2">方案</h1>
<h2 data-id="heading-3">使用Vuex获取并保存用户权限</h2>
<p>第一步, 定义权限实体类型, types/index.d.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> Permission &#123;
  <span class="hljs-attr">code</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步, 创建vuex的user模块, store目录结构如下:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eea55191d0354318ba9a06ff13244c69~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>store/modules/user.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; MutationTree, GetterTree, ActionTree, Module &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;

<span class="hljs-comment">// 第一步定义的权限实体类型</span>
<span class="hljs-keyword">import</span> &#123; Permission &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/types'</span>;
<span class="hljs-comment">// 请求后端接口</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> authApi <span class="hljs-keyword">from</span> <span class="hljs-string">'@/apis/auth'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> UserState &#123;
  <span class="hljs-attr">permissions</span>: Permission[];
&#125;

<span class="hljs-keyword">const</span> state: UserState = &#123;
  <span class="hljs-attr">permissions</span>: []
&#125;;

<span class="hljs-keyword">const</span> getters: GetterTree<UserState, <span class="hljs-built_in">any</span>> = &#123;
  permissions(state): Permission[] &#123;
    <span class="hljs-keyword">return</span> state.permissions;
  &#125;
&#125;;

<span class="hljs-keyword">const</span> mutations: MutationTree<UserState> = &#123;
  <span class="hljs-function"><span class="hljs-title">SET_PERMISSIONS</span>(<span class="hljs-params">state, permissions</span>)</span> &#123;
    state.permissions = permissions;
  &#125;
&#125;;

<span class="hljs-keyword">const</span> actions: ActionTree<UserState, <span class="hljs-built_in">any</span>> = &#123;
  <span class="hljs-function"><span class="hljs-title">permissions</span>(<span class="hljs-params">&#123; commit &#125;</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      authApi
        .permissions()
        .then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
          commit(<span class="hljs-string">'SET_PERMISSIONS'</span>, result);
          resolve(result);
        &#125;)
        .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          reject(err);
        &#125;);
    &#125;);
  &#125;
&#125;;

<span class="hljs-keyword">const</span> user: Module<UserState, <span class="hljs-built_in">any</span>> = &#123;
  state,
  getters,
  mutations,
  actions
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> user;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>store/index.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;

<span class="hljs-keyword">import</span> user <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/user'</span>;

Vue.use(Vuex);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;&#125;,
  <span class="hljs-attr">mutations</span>: &#123;&#125;,
  <span class="hljs-attr">actions</span>: &#123;&#125;,
  <span class="hljs-attr">modules</span>: &#123;
    user
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">根据权限动态筛选路由</h2>
<p>第一步, 我们来改造下router, 文件结构如下:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e9caa2136c74399b0c0524a543ed3fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建动态和静态配置, router/config.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; RouteConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;

<span class="hljs-comment">// 动态路由配置</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> asyncRoutes: RouteConfig[] = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'menu.home'</span> &#125;,
    <span class="hljs-attr">component</span>: (): <span class="hljs-function"><span class="hljs-params">any</span> =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/layouts/index.vue'</span>),
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'home'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
        <span class="hljs-attr">component</span>: (): <span class="hljs-function"><span class="hljs-params">any</span> =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/Home.vue'</span>),
        <span class="hljs-comment">// permissions就是这个菜单的权限代码</span>
        <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'home'</span>, <span class="hljs-attr">permissions</span>: [<span class="hljs-string">'home'</span>] &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'about'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
        <span class="hljs-attr">component</span>: (): <span class="hljs-function"><span class="hljs-params">any</span> =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/About.vue'</span>),
        <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'about'</span>, <span class="hljs-attr">permissions</span>: [<span class="hljs-string">'about'</span>] &#125;
      &#125;
    ]
  &#125;
];

<span class="hljs-comment">// 静态路由配置</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> constantRoutes: RouteConfig[] = [];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步, 我们调整下router/index.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;

<span class="hljs-comment">// 导入静态路由配置, 不需要控制权限</span>
<span class="hljs-keyword">import</span> &#123; constantRoutes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router/config'</span>;

Vue.use(VueRouter);

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">routes</span>: constantRoutes
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三步, 创建路由前置守卫, router/guard.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router'</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store'</span>;

<span class="hljs-keyword">import</span> &#123; asyncRoutes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router/config'</span>;
<span class="hljs-keyword">import</span> &#123; Permission &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/types'</span>;
<span class="hljs-keyword">import</span> &#123; RouteConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (to.path === <span class="hljs-string">'/user/login'</span>) &#123;
    next(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span> &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 如果vuex中的权限数组为空, 则从后台接口重新获取一次</span>
    <span class="hljs-keyword">if</span> (store.getters.permissions.length === <span class="hljs-number">0</span>) &#123;
      store
        .dispatch(<span class="hljs-string">'permissions'</span>)
        .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          router.addRoutes(filterAsyncRouters(asyncRoutes, res));
          next();
        &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      next();
    &#125;
  &#125;
&#125;);

<span class="hljs-comment">/**
 * 筛选动态路由
 *
 * <span class="hljs-doctag">@param </span>routers 动态路由配置
 * <span class="hljs-doctag">@param </span>permissions 权限实体数组
 * <span class="hljs-doctag">@returns </span>筛选后的路由配置数组
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">filterAsyncRouters</span>(<span class="hljs-params">
  routers: RouteConfig[],
  permissions: Permission[]
</span>): <span class="hljs-title">RouteConfig</span>[] </span>&#123;
  <span class="hljs-keyword">const</span> result: RouteConfig[] = [];
  routers.forEach(<span class="hljs-function">(<span class="hljs-params">route</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> newRoute = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, route);
    <span class="hljs-keyword">if</span> (hasPermission(newRoute, permissions)) &#123;
      result.push(newRoute);
      <span class="hljs-keyword">if</span> (newRoute.children && newRoute.children.length) &#123;
        newRoute.children = filterAsyncRouters(newRoute.children, permissions);
      &#125;
    &#125;
  &#125;);
  <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-comment">/**
 * 判断是否拥有路由权限
 *
 * <span class="hljs-doctag">@param </span>route 路由实体
 * <span class="hljs-doctag">@param </span>permissions 权限实体数组
 * <span class="hljs-doctag">@returns </span>boolean 是否拥有权限 true 是, false 否
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasPermission</span>(<span class="hljs-params">route: RouteConfig, permissions: Permission[]</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">let</span> flag = <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">if</span> (route.meta && route.meta.permissions) &#123;
    flag = <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> permission <span class="hljs-keyword">of</span> permissions) &#123;
      <span class="hljs-keyword">if</span> (route.meta.permissions.includes(permission.code)) &#123;
        flag = <span class="hljs-literal">true</span>;
        <span class="hljs-keyword">break</span>;
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> flag;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一步, 需要在main.ts中让这个守卫生效:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'@/App.vue'</span>;

<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store'</span>;

<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router'</span>;
<span class="hljs-comment">// 导入守卫代码</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@/router/guard'</span>;

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h</span>) =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">根据权限控制组件的是否展示</h2>
<p>第一步, 创建指令相关内容, 结构如下:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0048f127884344f39c43a4b6cecbe4db~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二步, 编写权限指令, directives/permission.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store'</span>;

<span class="hljs-comment">// 最早定义的权限实体类型</span>
<span class="hljs-keyword">import</span> &#123; Permission &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/types'</span>;

<span class="hljs-keyword">const</span> permission = Vue.directive(<span class="hljs-string">'permission'</span>, &#123;
  <span class="hljs-attr">inserted</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">el, binding, vnode</span>) </span>&#123;
    <span class="hljs-keyword">const</span> permissionCode = binding.arg || <span class="hljs-string">''</span>;
    <span class="hljs-keyword">const</span> permissionCodes: <span class="hljs-built_in">string</span>[] = store.getters.permissions.map(
      <span class="hljs-function">(<span class="hljs-params">permission: Permission</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> permission.code;
      &#125;
    );
    <span class="hljs-keyword">if</span> (!permissionCodes.includes(permissionCode)) &#123;
      (el.parentNode && el.parentNode.removeChild(el)) ||
        (el.style.display = <span class="hljs-string">'none'</span>);
    &#125;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一步, 和router中类似, 我们要加载这个指令, main.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'@/App.vue'</span>;

<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store'</span>;

<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router'</span>;

<span class="hljs-keyword">import</span> <span class="hljs-string">'@/router/guard'</span>;

<span class="hljs-comment">// 导入指令</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@/directives/action'</span>;

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h</span>) =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用指令很简单, App.vue:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
      <span class="hljs-comment"><!-- v-permision为指令名称, about为权限代码 --></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">v-permission:about</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目所有源码可以在<a href="https://github.com/Houtaroy/vue-koala" target="_blank" rel="nofollow noopener noreferrer">Github</a>上查看</p></div>  
</div>
            