
---
title: '从0到1搭建React+TypeScript+webpack项目【2】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3936'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 18:01:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=3936'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">调整项目结构</h1>
<h2 data-id="heading-1">添加@types</h2>
<p>根目录添加上typescript 的全局类型定义文件架 <code>@types</code></p>
<h2 data-id="heading-2">src 里面添加结构</h2>
<p>assets、components、constants、layouts、utils、style、pages、hooks等</p>
<h3 data-id="heading-3">调整后的文件目录结构为：</h3>
<pre><code class="hljs language-js copyable" lang="js">my-app
├── .vscode          # vscode 配置目录
│   ├── extensions.json  #项目推荐使用安装的插件
│   ├── settings.json    #项目里面使用的vscode的配置内容，比如自动保存代码格式化等
│   ├── tsrc.code-snippets #代码片段配置
├── .@types          # 全局类型声明
├── node_modules 
├── public           # 公共文件
│   ├── favicon.ico
│   ├── index.html     #入口html
│   └── manifest.json
└── src             # 源码目录
│  ├── assets        # 静态资源
│  ├── components    # 公共业务组件
│  ├── constants     # 存储api 等公共的类型常量类的变动不大的文件
│  │     │── api       # 定义对接后台api 接口的文件
│  ├── layouts       # 布局
│  ├── models          # 存放state和actions模块
│  ├── pages           # 页面组件目录
│  ├── routers         # 页面路由相关的文件
│  ├── services        # model对应的api 调用函数
│  ├── style           # 全局样式
│  ├── utils           # 公用工具函数
│  ├── App.css
│  ├── App.js
│  ├── App.test.tsx
│  ├── index.css
│  ├── index.tsx
│   ├── logo.svg
│  └── reportWebVitals.ts
│  └── setupTests.ts
├── .eslintignore        # eslint忽略文件的配置
├── .eslintrc            #eslint 的配置文件
├── .gitignore           #git 的忽略文件的配置
├── .prettierrc          #prettier 插件的配置
├── .stylelintrc.json    #stylelint插件的配置
├── package.json        
├── README.md            
├── tsconfig.json        #typescript 的配置
├── yarn.lock            #yarn lock 文件
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">引入ant-design</h2>
<h3 data-id="heading-5">安装antd 推荐的craco 模块</h3>
<pre><code class="hljs language-js copyable" lang="js">yarn add antd @craco/craco
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">修改package.json 里面的启动指令</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* package.json */</span>
<span class="hljs-string">"scripts"</span>: &#123;
-   <span class="hljs-string">"start"</span>: <span class="hljs-string">"react-scripts start"</span>,
-   <span class="hljs-string">"build"</span>: <span class="hljs-string">"react-scripts build"</span>,
-   <span class="hljs-string">"test"</span>: <span class="hljs-string">"react-scripts test"</span>,
+   <span class="hljs-string">"start"</span>: <span class="hljs-string">"craco start"</span>,
+   <span class="hljs-string">"build"</span>: <span class="hljs-string">"craco build"</span>,
+   <span class="hljs-string">"test"</span>: <span class="hljs-string">"craco test"</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">根目录里面添加craco.config.js</h3>
<p>craco.config.js,主要是在create-react-app 不用eject暴露webpack 配置的情况下，方便在外部修改webpack 的配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* craco.config.js */</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">自定义主题</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* src/App.js */</span>
- <span class="hljs-keyword">import</span> <span class="hljs-string">'./App.css'</span>;
+ <span class="hljs-keyword">import</span> <span class="hljs-string">'./App.less'</span>;

<span class="hljs-comment">/* src/App.less */</span>
- @<span class="hljs-keyword">import</span> <span class="hljs-string">'~antd/dist/antd.css'</span>;
+ @<span class="hljs-keyword">import</span> <span class="hljs-string">'~antd/dist/antd.less'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">安装 craco-less</h4>
<pre><code class="hljs language-js copyable" lang="js">yarn add craco-less
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 craco.config.js 文件如下</p>
<pre><code class="hljs language-js copyable" lang="js">+ <span class="hljs-keyword">const</span> CracoLessPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'craco-less'</span>);

+ <span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-attr">plugins</span>: [
        &#123;
          <span class="hljs-attr">plugin</span>: CracoLessPlugin,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">lessLoaderOptions</span>: &#123;
              <span class="hljs-attr">lessOptions</span>: &#123;
                <span class="hljs-attr">modifyVars</span>: &#123; <span class="hljs-string">'@primary-color'</span>: <span class="hljs-string">'#1DA57A'</span> &#125;,
                <span class="hljs-attr">javascriptEnabled</span>: <span class="hljs-literal">true</span>,
              &#125;,
            &#125;,
          &#125;,
        &#125;,
      ],
   &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">支持装饰器</h4>
<pre><code class="hljs language-js copyable" lang="js">yarn add @babel/plugin-proposal-decorators --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 craco.config.js 文件如下</p>
<pre><code class="hljs language-js copyable" lang="js">babel:&#123;  
    <span class="hljs-attr">plugins</span>: [
      [<span class="hljs-string">"@babel/plugin-proposal-decorators"</span>, &#123; <span class="hljs-attr">legacy</span>: <span class="hljs-literal">true</span> &#125;]
    ]
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">配置代理</h4>
<p>修改 craco.config.js 文件如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//配置代理解决跨域</span>
<span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">proxy</span>: &#123;
         <span class="hljs-string">"/api"</span>: &#123;
             <span class="hljs-attr">target</span>: <span class="hljs-string">"http://baidu.com"</span>,  
             <span class="hljs-comment">//target: 'http://192.168.9.19:8080',</span>
             <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
             <span class="hljs-attr">pathRewrite</span>: &#123;
                 <span class="hljs-string">"^/api"</span>: <span class="hljs-string">""</span>
             &#125;
         &#125;
     &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">配置antd的less按需加载</h4>
<pre><code class="hljs language-js copyable" lang="js">yarn add babel-plugin-<span class="hljs-keyword">import</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 craco.config.js 文件如下</p>
<pre><code class="hljs language-js copyable" lang="js">babel:&#123;  
    <span class="hljs-attr">plugins</span>: [
      [<span class="hljs-string">"@babel/plugin-proposal-decorators"</span>, &#123; <span class="hljs-attr">legacy</span>: <span class="hljs-literal">true</span> &#125;],  <span class="hljs-comment">//装饰器</span>
      [   
        <span class="hljs-string">"import"</span>, 
        &#123;
          <span class="hljs-string">"libraryName"</span>: <span class="hljs-string">"antd"</span>,
          <span class="hljs-string">"libraryDirectory"</span>: <span class="hljs-string">"es"</span>,
           <span class="hljs-string">"style"</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">//设置为true即是less</span>
         &#125;
     ]
    ]
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>App.less文件去掉@import '~antd/dist/antd.less';</p>
<blockquote>
<p>按需加载后只需引入组件，无需再额外引入样式文件，babel会自动按需帮你完成样式的引入。这样打包出来的文件会更小。</p>
</blockquote>
<h4 data-id="heading-13">配置别名</h4>
<p>目的：让后续引用的地方减少路径的复杂度</p>
<p>修改 craco.config.js 文件如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
webpack: &#123;
    <span class="hljs-comment">// 别名</span>
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">"@"</span>: path.resolve(<span class="hljs-string">"src"</span>),
      <span class="hljs-string">"@utils"</span>: path.resolve(<span class="hljs-string">"src/utils"</span>),
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">添加antd 和ant 国际化</h3>
<pre><code class="hljs language-js copyable" lang="js">yarn add antd
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">index.tsx添加国际语言包</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;
<span class="hljs-keyword">import</span> zhCN <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/lib/locale/zh_CN'</span>;<span class="hljs-comment">//添加语言包支撑</span>
ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">index.tsx为组件提供统一的全局化配置</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;
<span class="hljs-keyword">import</span> zhCN <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/lib/locale/zh_CN'</span>; <span class="hljs-comment">// 添加语言包支撑</span>
<span class="hljs-keyword">import</span> &#123; ConfigProvider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>; <span class="hljs-comment">// 为组件提供统一的全局化配置</span>
ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ConfigProvider</span> <span class="hljs-attr">locale</span>=<span class="hljs-string">&#123;zhCN&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">ConfigProvider</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>),
);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            