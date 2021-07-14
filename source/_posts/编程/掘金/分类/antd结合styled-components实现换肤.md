
---
title: 'antd结合styled-components实现换肤'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a7c0c833f5d477db1d12734835e4d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 02:01:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a7c0c833f5d477db1d12734835e4d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>项目地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fleonwgc%2Fantd-admin-tpl" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/leonwgc/antd-admin-tpl" ref="nofollow noopener noreferrer">github.com/leonwgc/ant…</a></p>
<ol>
<li>定义不同的主题色 , 如下绿，红，蓝，紫，黄， 分别定义颜色名称和颜色值</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> colors = [
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'green'</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">'#08bc63'</span> &#125;, <span class="hljs-comment">// 绿</span>
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'red'</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">'#f5222d'</span> &#125;, <span class="hljs-comment">//红</span>
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'blue'</span>,  <span class="hljs-comment">// 蓝</span>
    <span class="hljs-attr">color</span>: <span class="hljs-string">'#004bcc'</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'purple'</span>, <span class="hljs-comment">//紫</span>
    <span class="hljs-attr">color</span>: <span class="hljs-string">'#9254de'</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'yellow'</span>, <span class="hljs-comment">// 黄</span>
    <span class="hljs-attr">color</span>: <span class="hljs-string">'rgb(250, 173, 20)'</span>,
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>根据<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40emeks%2Fantd-custom-theme-generator" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@emeks/antd-custom-theme-generator" ref="nofollow noopener noreferrer"> antd-custom-theme-generator </a> 生成相应css主题 用来动态替换 antd默认主题</li>
</ol>
<ul>
<li>
<p>安装 antd-custom-theme-generator</p>
</li>
<li>
<p>定义 custom-theme.less ，以黄色为例：b</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">@primary-color: rgb(<span class="hljs-number">250</span>, <span class="hljs-number">173</span>, <span class="hljs-number">20</span>);
@link-color: rgb(<span class="hljs-number">250</span>, <span class="hljs-number">173</span>, <span class="hljs-number">20</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>执行 npx generate-theme ./custom-theme.less ./custom-theme-yellow.css ,将生成custom-theme-yellow.css样色文件</p>
</li>
<li>
<p>将生成的css主题文件拷贝到 public目录</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a7c0c833f5d477db1d12734835e4d92~tplv-k3u1fbpfcp-watermark.image" alt="theme.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>修改webpack devServer 配置 （当然也可以传到cdn引用）</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> devServer: &#123;
      <span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">headers</span>: &#123; <span class="hljs-string">'Access-Control-Allow-Origin'</span>: <span class="hljs-string">'*'</span> &#125;,
      <span class="hljs-attr">setup</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">app, server</span>) </span>&#123;
        app.use(express.static(path.join(__dirname, <span class="hljs-string">`public`</span>)));
      &#125;,
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>定义redux store , 将颜色信息存储到redux</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> &#123; Provider, configureStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'simple-redux-store'</span>;
<span class="hljs-keyword">import</span> &#123; getSetting &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'~/utils/helper'</span>;
<span class="hljs-keyword">import</span> &#123; getEnv &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'~/utils/host'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;

<span class="hljs-keyword">const</span> colors = [
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'green'</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">'#08bc63'</span> &#125;,
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'red'</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">'#f5222d'</span> &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'blue'</span>,
    <span class="hljs-attr">color</span>: <span class="hljs-string">'#004bcc'</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'purple'</span>,
    <span class="hljs-attr">color</span>: <span class="hljs-string">'#9254de'</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'yellow'</span>,
    <span class="hljs-attr">color</span>: <span class="hljs-string">'rgb(250, 173, 20)'</span>,
  &#125;,
];

type Color = &#123;
  <span class="hljs-attr">name</span>: string;
  color: string;
&#125;;

type StoreData = &#123;
  <span class="hljs-attr">menuCollapsed</span>: boolean;
  isSettingVisile: boolean;
  colors: Color[];
  color: string; <span class="hljs-comment">//当前颜色名称</span>
&#125;;

<span class="hljs-keyword">const</span> initData: StoreData = &#123;
  <span class="hljs-attr">menuCollapsed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">isSettingVisile</span>: <span class="hljs-literal">false</span>,
  colors,
  <span class="hljs-attr">color</span>: <span class="hljs-string">'blue'</span>, <span class="hljs-comment">//默认取蓝色</span>
  ...getSetting(),
&#125;;

<span class="hljs-keyword">const</span> store = configureStore(initData, getEnv() === <span class="hljs-string">'test'</span>);

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
);

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>定义换肤设置面板， 这里用antd drawer 组件</li>
</ol>
<p>读取redux colors数组， 动态生成颜色块 , 点击颜色块， 更新redux color颜色名， 动态下载对应css皮肤</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e2e56926ccc4b50a3c41b09477ff016~tplv-k3u1fbpfcp-watermark.image" alt="drawer.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; Menu, Avatar, Dropdown, Space, Button, Drawer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> &#123; useSelector, useUpdateStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'simple-redux-store'</span>;
<span class="hljs-keyword">import</span> &#123; useHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>;
<span class="hljs-keyword">import</span> &#123; loadResource, saveSetting &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'~/utils/helper'</span>;
<span class="hljs-keyword">import</span> &#123;
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  SettingOutlined,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@ant-design/icons'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> storage <span class="hljs-keyword">from</span> <span class="hljs-string">'simple-browser-store'</span>;
<span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>;

<span class="hljs-keyword">const</span> StyledColorBlock = styled.div<span class="hljs-string">`
  width: 20px;
  height: 20px;
  margin-top: 8px;
  margin-right: 8px;
  color: #fff;
  font-weight: 700;
  text-align: center;
  border-radius: 2px;
  cursor: pointer;
`</span>;

<span class="hljs-keyword">const</span> StyledHeader = styled.header<span class="hljs-string">`
  display: flex;
  height: 48px;
  background: <span class="hljs-subst">$&#123;(props) => props.theme.color&#125;</span>; // 读取Styled Component的主题色
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  border-bottom: 1px solid #f5f5f5;

  .folder &#123;
    font-size: 16px;
    color: rgba(0, 0, 0, 0.65);
    &:hover &#123;
      color: #004bcc;
    &#125;
  &#125;
`</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Header</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> history = useHistory();
  <span class="hljs-keyword">const</span> &#123; color = <span class="hljs-string">''</span>, colors &#125; = useSelector(<span class="hljs-function">(<span class="hljs-params">state</span>) =></span> state.app);
  <span class="hljs-keyword">const</span> updateStore = useUpdateStore();

  <span class="hljs-comment">// color改变，动态加载新主题</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (color) &#123;
      <span class="hljs-comment">// eslint-disable-next-line no-undef</span>
      loadResource(<span class="hljs-string">`<span class="hljs-subst">$&#123;__webpack_public_path__&#125;</span>custom-theme-<span class="hljs-subst">$&#123;color&#125;</span>.css`</span>);
    &#125;
  &#125;, [color]);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">StyledHeader</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Drawer</span>
        <span class="hljs-attr">title</span>=<span class="hljs-string">"主题色设置"</span>
        <span class="hljs-attr">placement</span>=<span class="hljs-string">"right"</span>
        <span class="hljs-attr">closable</span>=<span class="hljs-string">&#123;false&#125;</span>
        <span class="hljs-attr">onClose</span>=<span class="hljs-string">&#123;()</span> =></span> updateStore(&#123; isSettingVisile: false &#125;)&#125;
        visible=&#123;isSettingVisile&#125;
      >
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Space</span>></span>
            //动态生成颜色块
            &#123;colors.map((c, i) => (
              <span class="hljs-tag"><<span class="hljs-name">StyledColorBlock</span>
                <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
                  updateStore(&#123; color: c.name &#125;);
                  saveSetting(&#123; color: c.name &#125;);
                &#125;&#125;
                style=&#123;&#123; backgroundColor: c.color &#125;&#125;
                key=&#123;i&#125;
              />
            ))&#125;
          <span class="hljs-tag"></<span class="hljs-name">Space</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Drawer</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">StyledHeader</span>></span></span>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>Styled component 通过ThemeProvider 同步redux主题色 ，** 处理非antd组件的换肤 **</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; color = <span class="hljs-string">''</span>, colors &#125; = useSelector(<span class="hljs-function">(<span class="hljs-params">state</span>) =></span> state.app);

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ThemeProvider</span> <span class="hljs-attr">theme</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> <span class="hljs-attr">colors.find</span>((<span class="hljs-attr">c</span>) =></span> c.name === color).color &#125;&#125;>
      <span class="hljs-tag"><<span class="hljs-name">ConfigProvider</span> <span class="hljs-attr">locale</span>=<span class="hljs-string">&#123;zhCN&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">Spin</span> <span class="hljs-attr">spinning</span> /></span>&#125;>
            <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Redirect</span> <span class="hljs-attr">to</span>=<span class="hljs-string">&#123;</span>'/<span class="hljs-attr">user</span>/<span class="hljs-attr">add</span>'&#125; /></span>
              <span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
              &#123;routes.map((route, idx) => (
                <span class="hljs-tag"><<span class="hljs-name">Route</span>
                  <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;idx&#125;</span>
                  <span class="hljs-attr">path</span>=<span class="hljs-string">&#123;route.path&#125;</span>
                  <span class="hljs-attr">exact</span>=<span class="hljs-string">&#123;route.exact&#125;</span>
                  <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;route.component&#125;</span>
                /></span>
              ))&#125;
            <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Router</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">ConfigProvider</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ThemeProvider</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果如图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd01c3825cce452dbfee2ecfefeaf9f6~tplv-k3u1fbpfcp-watermark.image" alt="c1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b04fa7d7725944bc8fa274018a0fa371~tplv-k3u1fbpfcp-watermark.image" alt="c2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2a396660cf746ae8079ebfe33a7501d~tplv-k3u1fbpfcp-watermark.image" alt="c3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/789ba3896cdc43a28d18018a9a3e1716~tplv-k3u1fbpfcp-watermark.image" alt="c4.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            