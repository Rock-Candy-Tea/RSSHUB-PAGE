
---
title: 'Taro爬坑血泪史'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4167'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 17:18:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=4167'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Taro爬坑血泪史</h1>
<h2 data-id="heading-1">一、介绍</h2>
<ul>
<li>Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发 微信 / 京东 / 百度 / 支付宝 / 字节跳动 / QQ 小程序 / H5 等应用。现如今市面上端的形态多种多样，Web、React Native、微信小程序等各种端大行其道，当业务要求同时在不同的端都要求有所表现的时候，针对不同的端去编写多套代码的成本显然非常高，这时候只编写一套代码就能够适配到多端的能力就显得极为需要。</li>
<li>Taro 2.X 支持react</li>
<li>Taro 3.0 支持vue/vue3</li>
</ul>
<h2 data-id="heading-2">二、安装</h2>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 使用 npm 安装 CLI</span>
<span class="hljs-meta">$</span><span class="bash"> npm install -g @tarojs/cli</span>
<span class="hljs-meta">#</span><span class="bash"> 使用命令创建模板项目</span>
<span class="hljs-meta">$</span><span class="bash"> taro init myApp</span>
<span class="hljs-meta">#</span><span class="bash"> 安装依赖</span>
<span class="hljs-meta">$</span><span class="bash"> npm install</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>++注意：依赖版本保持一致++</p>
<h2 data-id="heading-3">三、编译以及打包</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"build:weapp"</span>: <span class="hljs-string">"taro build --type weapp"</span>, <span class="hljs-comment">//微信</span>
    <span class="hljs-string">"build:swan"</span>: <span class="hljs-string">"taro build --type swan"</span>, <span class="hljs-comment">// 百度</span>
    <span class="hljs-string">"build:alipay"</span>: <span class="hljs-string">"taro build --type alipay"</span>, <span class="hljs-comment">//阿里</span>
    <span class="hljs-string">"build:tt"</span>: <span class="hljs-string">"taro build --type tt"</span>,  <span class="hljs-comment">//字节</span>
    <span class="hljs-string">"build:h5"</span>: <span class="hljs-string">"taro build --type h5"</span>,  <span class="hljs-comment">//H5</span>
    <span class="hljs-string">"build:qq"</span>: <span class="hljs-string">"taro build --type qq"</span>,  <span class="hljs-comment">//qq</span>
    <span class="hljs-string">"build:quickapp"</span>: <span class="hljs-string">"taro build --type quickapp"</span>,
    <span class="hljs-string">"dev:weapp"</span>: <span class="hljs-string">"npm run build:weapp -- --watch"</span>,
    <span class="hljs-string">"dev:nopre:weapp"</span>: <span class="hljs-string">"set NODE_ENV=devNoPre && npm run build:weapp -- --watch"</span>,
    <span class="hljs-string">"dev:swan"</span>: <span class="hljs-string">"npm run build:swan -- --watch"</span>,
    <span class="hljs-string">"dev:alipay"</span>: <span class="hljs-string">"npm run build:alipay -- --watch"</span>,
    <span class="hljs-string">"dev:tt"</span>: <span class="hljs-string">"npm run build:tt -- --watch"</span>,
    <span class="hljs-string">"dev:h5"</span>: <span class="hljs-string">"npm run build:h5 -- --watch"</span>,
    <span class="hljs-string">"dev:rn"</span>: <span class="hljs-string">"npm run build:rn -- --watch"</span>,
    <span class="hljs-string">"dev:qq"</span>: <span class="hljs-string">"npm run build:qq -- --watch"</span>,
    <span class="hljs-string">"dev:quickapp"</span>: <span class="hljs-string">"npm run build:quickapp -- --watch"</span>,
    <span class="hljs-string">"lint-staged"</span>: <span class="hljs-string">"lint-staged"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">四、项目目录结构</h2>
<pre><code class="copyable">├── dist                   编译结果目录
├── config                 配置目录
|   ├── dev.js             开发时配置
|   ├── index.js           默认配置
|   └── prod.js            打包时配置
├── src                    源码目录
|   ├── pages              页面文件目录
|   |   ├── index          index 页面目录
|   |   |   ├── index.js   index 页面逻辑
|   |   |   └── index.css  index 页面样式
|   ├── app.css            项目总通用样式
|   └── app.js             项目入口文件
└── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">五、多端编译</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> pages = []
<span class="hljs-keyword">if</span> (process.env.TARO_ENV === <span class="hljs-string">'weapp'</span>) &#123;
  pages = [
    <span class="hljs-string">'/pages/index/index'</span>
  ]
&#125;
<span class="hljs-keyword">if</span> (process.env.TARO_ENV === <span class="hljs-string">'swan'</span>) &#123;
  pages = [
    <span class="hljs-string">'/pages/indexswan/indexswan'</span>
  ]
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  pages
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">六、单位转化</h2>
<blockquote>
<p>小程序、H5尺寸单位统一</p>
</blockquote>
<ul>
<li>把rpx替换成px</li>
<li>run dev:h5后，会自动编译成rem单位（行内样式无法自动转换，一些Taro-ui框架内的scss无法自动转化，需要手动调整，原因未知）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">/config/index.js
<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-attr">projectName</span>: <span class="hljs-string">'myProject'</span>,
  <span class="hljs-attr">date</span>: <span class="hljs-string">'2018-4-18'</span>,
  <span class="hljs-attr">designWidth</span>: <span class="hljs-number">640</span>,
  ....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">七、优化</h2>
<h3 data-id="heading-8">1.分包</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">config:[
    pages:[],
    <span class="hljs-attr">subpages</span>:[]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.预渲染</h3>
<ul>
<li>将页面初始化的状态直接渲染为无状态(dataless)的 wxml，在框架和业务逻辑运行之前执行渲染流程。经过 Prerender 的页面初始渲染速度通常会和原生小程序一致甚至更快。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> config = &#123;
  ...
  <span class="hljs-attr">mini</span>: &#123;
    <span class="hljs-attr">prerender</span>: &#123;
      <span class="hljs-attr">match</span>: <span class="hljs-string">'pages/shop/**'</span>, <span class="hljs-comment">// 所有以 `pages/shop/` 开头的页面都参与 prerender</span>
      <span class="hljs-attr">include</span>: [<span class="hljs-string">'pages/any/way/index'</span>], <span class="hljs-comment">// `pages/any/way/index` 也会参与 prerender</span>
      <span class="hljs-attr">exclude</span>: [<span class="hljs-string">'pages/shop/index/index'</span>] <span class="hljs-comment">// `pages/shop/index/index` 不用参与 prerender</span>
    &#125;
  &#125;
&#125;;

<span class="hljs-built_in">module</span>.exports = config
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.长列表渲染</h3>
<ul>
<li>只渲染当前可视区域(visible viewport)的视图</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><VirtualList
    <span class="hljs-attribute">height</span>=&#123;<span class="hljs-number">500</span>&#125; <span class="hljs-comment">/* 列表的高度 */</span>
    <span class="hljs-attribute">width</span>='<span class="hljs-number">100%</span>' <span class="hljs-comment">/* 列表的宽度 */</span>
    itemData=&#123;data&#125; <span class="hljs-comment">/* 渲染列表的数据 */</span>
    itemCount=&#123;dataLen&#125; <span class="hljs-comment">/*  渲染列表的长度 */</span>
    itemSize=&#123;<span class="hljs-number">100</span>&#125; <span class="hljs-comment">/* 列表单项的高度  */</span>
>
    &#123;Row&#125; <span class="hljs-comment">/* 列表单项组件，这里只能传入一个组件 */</span>
</VirtualList>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">八、技术选型</h2>
<p>React、Typescript、Mobx、Hooks</p>
<h2 data-id="heading-12">九、小程序</h2>
<h3 data-id="heading-13">1.第三方H5网页跳转</h3>
<ul>
<li>需要配置第三方https证书，且第三方服务器需要添加一个业务域名校验文件，并小程序后台配置业务域名，详情查看小程序后台开发配置</li>
</ul>
<h3 data-id="heading-14">2.input卡顿问题</h3>
<blockquote>
<p>输入框快速输入，或者快速删除数据卡顿闪屏问题</p>
</blockquote>
<ul>
<li>绑定旧值，监听onChange事件设置旧值的拷贝值，==避免组件依赖值更新==，即可解决方法</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> [formData, setFormData] = useState(initState)
<span class="hljs-keyword">const</span> [selfFormState, setSelfFormState] = useState(initState)
<span class="hljs-keyword">const</span> handleChange = <span class="hljs-function">(<span class="hljs-params">type, value</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> newState = &#123;
      ...selfFormState,
      [type]: value,
    &#125;
      setSelfFormState(newState)
      <span class="hljs-comment">//小程序需要return value</span>
      <span class="hljs-keyword">return</span> value
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">AtInput</span>
  <span class="hljs-attr">name</span>=<span class="hljs-string">'name'</span>
  <span class="hljs-attr">title</span>=<span class="hljs-string">'名称'</span>
  <span class="hljs-attr">type</span>=<span class="hljs-string">'text'</span>
  <span class="hljs-attr">required</span>
  <span class="hljs-attr">disabled</span>
  <span class="hljs-attr">placeholder</span>=<span class="hljs-string">'请输入名称'</span>
  <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;formData.name&#125;</span>
  <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(val)</span> =></span> &#123;
    handleChange('name', val)
  &#125;&#125;
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">3.textArea层级最高，涉及到弹窗覆盖问题</h3>
<blockquote>
<p>弹窗被textArea遮挡的奇怪现象</p>
</blockquote>
<ul>
<li>控制textArea的显示隐藏</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">AtForm</span> <span class="hljs-attr">onSubmit</span>=<span class="hljs-string">&#123;onSubmit&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">visibility:</span> <span class="hljs-attr">show</span> ? '<span class="hljs-attr">hidden</span>' <span class="hljs-attr">:</span> '<span class="hljs-attr">visible</span>' &#125;&#125;></span>
        <span class="hljs-tag"><<span class="hljs-name">AtTextarea</span>
          <span class="hljs-attr">count</span>=<span class="hljs-string">&#123;false&#125;</span>
          <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;formData.tel&#125;</span>
          <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(val)</span> =></span> &#123;
            handleChange('tel', val)
          &#125;&#125;
          maxLength=&#123;1000&#125;
          placeholder=&#123;'请输入联系电话'&#125;
        />
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">AtForm</span>></span>
  &#123;show && (
    <span class="hljs-tag"><<span class="hljs-name">View</span>></span>
      弹窗内容
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
  )&#125;
<span class="hljs-tag"></<span class="hljs-name">View</span>></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">4.小程序后退页面刷新问题</h3>
<blockquote>
<p>例如从详情页进入编辑页，编辑完成后返回的情况下，小程序是不会重新请求新的数据。如果继续前进，会涉及到页面栈最大层级问题</p>
</blockquote>
<ul>
<li>小程序返回的页面会触发==useDidshow==</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Index</span> (<span class="hljs-params"></span>) </span>&#123;
  useDidShow(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 校验用户状态</span>
    checkUserStatus()
  &#125;)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
      测试
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span> 
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">5.弹窗打开时，固定背景隐藏背景滚动条</h3>
<ul>
<li>弹窗打开时背景添加css，隐藏滚动条</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.at-modal__content</span> &#123;
  <span class="hljs-attribute">overflow-y</span>: hidden;
  ::-webkit-scrollbar&#123;
    width: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">color</span>: transparent;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">6.用户数据获取</h3>
<blockquote>
<p>授权操作弹窗，首次拒绝后 不会再次弹出</p>
</blockquote>
<ul>
<li>非必要情况下建议使用开放组件==openData==展示用户头像及昵称</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">OpenData</span> <span class="hljs-attr">type</span>=<span class="hljs-string">'userAvatarUrl'</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">十、H5</h2>
<h3 data-id="heading-20">1.Taro.request()H5端不返回数据</h3>
<ul>
<li>用axios重新封装</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateTaroReq</span> (<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">async</span> (data?: AjaxData) => &#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> Taro.request(&#123;
      ...config,
      data,      
    &#125;)
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: resData &#125; = res
    <span class="hljs-keyword">return</span> resData.data
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateTaroReq</span>(<span class="hljs-params">axiosConfig:axiosConfig,config?:<span class="hljs-built_in">any</span></span>): <span class="hljs-title">Function</span></span>&#123;
  <span class="hljs-keyword">const</span> dataName = axiosConfig.method&&axiosConfig.method.toLowerCase() == <span class="hljs-string">'post'</span> ? <span class="hljs-string">'data'</span> : <span class="hljs-string">'params'</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">data?: <span class="hljs-built_in">Object</span></span>) =></span>&#123;
    <span class="hljs-keyword">return</span> axios(&#123;
      <span class="hljs-attr">method</span>:axiosConfig.method,
      <span class="hljs-attr">url</span>:<span class="hljs-string">'/xxxx/'</span>+axiosConfig.url,
      [dataName]:&#123;
        ...data
      &#125;
    &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      <span class="hljs-keyword">return</span> res.data
    &#125;)
  &#125;
&#125;

<span class="hljs-keyword">const</span> reqBankInfo = generateTaroReq(&#123;
  <span class="hljs-attr">url</span>: <span class="hljs-string">'wx/api/weixin/jrManage/editBankInfo'</span>,
  <span class="hljs-attr">method</span>: <span class="hljs-string">'POST'</span>
&#125;)
reqBankInfo(_ajaxData)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">2.登录Taro.login()不可用</h3>
<blockquote>
<p>H5端无法调用</p>
</blockquote>
<ul>
<li>替换成其他登录形式</li>
</ul>
<h3 data-id="heading-22">3.position:fixed状态下ScrollView无法滚动</h3>
<blockquote>
<p>顶部tabs超出屏幕宽度时无法左右滑动</p>
</blockquote>
<ul>
<li>如固定再头部的导航菜单左右滚动，则设置需要设置css属性(left和right)</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.className</span>&#123;
    <span class="hljs-attribute">position</span>:fixed;
    <span class="hljs-attribute">top</span>:<span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>:<span class="hljs-number">0</span>;
    <span class="hljs-attribute">right</span>:<span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">4.Taro.uploadFile()</h3>
<ul>
<li>H5端需要多加一个参数：fileName:'xxxx.png',不加接口会报错</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-attr">url</span>: <span class="hljs-string">'/xxxxx/uploadxImage'</span>,<span class="hljs-comment">//上传接口</span>
  <span class="hljs-attr">filePath</span>: path,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'file'</span>,
  <span class="hljs-attr">fileName</span>:<span class="hljs-string">'file.'</span> + type,
  <span class="hljs-attr">header</span>: &#123;
    <span class="hljs-attr">Authorization</span>: Taro.getStorageSync(<span class="hljs-string">'token'</span>),
  &#125;,
&#125;
Taro.uploadFile(config)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">5.tabs切换报错</h3>
<blockquote>
<p>Failed to execute 'replaceChild' on 'Node': The node to be replaced is not a child of this node.</p>
</blockquote>
<ul>
<li>原因是用了同一套数据，把list和showData分开就行</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">AtTabs</span> <span class="hljs-attr">current</span>=<span class="hljs-string">&#123;current&#125;</span> <span class="hljs-attr">tabList</span>=<span class="hljs-string">&#123;tabList&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">AtTabsPane</span> <span class="hljs-attr">current</span>=<span class="hljs-string">&#123;current&#125;</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;0&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>
        &#123;
        showData&&!loading?(
          view.map(item => &#123;
            return <span class="hljs-tag"><<span class="hljs-name">JinrongItem</span> <span class="hljs-attr">item</span>=<span class="hljs-string">&#123;item&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">JinrongItem</span>></span>
          &#125;)):empty
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">AtTabsPane</span>></span>
<span class="hljs-tag"></<span class="hljs-name">AtTabs</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>==改成==</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">AtTabs</span> <span class="hljs-attr">current</span>=<span class="hljs-string">&#123;current&#125;</span> <span class="hljs-attr">tabList</span>=<span class="hljs-string">&#123;tabList&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">AtTabsPane</span> <span class="hljs-attr">current</span>=<span class="hljs-string">&#123;current&#125;</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;0&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>
        &#123;showData&&!loading?(
          list.map((item, i) => &#123;
            return <span class="hljs-tag"><<span class="hljs-name">JirongItem</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;item&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">JirongItem</span>></span>
          &#125;)):empty
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">AtTabsPane</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">AtTabsPane</span> <span class="hljs-attr">current</span>=<span class="hljs-string">&#123;current&#125;</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;1&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>
        &#123;showData2&&!loading?(
          list2.map((item, i) => &#123;
            return <span class="hljs-tag"><<span class="hljs-name">XuqiuLow</span> <span class="hljs-attr">xuqiukey</span>=<span class="hljs-string">&#123;_keys[current]&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.id&#125;</span> <span class="hljs-attr">isedit</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;item&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">XuqiuLow</span>></span>
          &#125;)):empty
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">AtTabsPane</span>></span>
<span class="hljs-tag"></<span class="hljs-name">AtTabs</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">6.Taro.getCurrentPages()在H5和小程序中表现不同</h3>
<ul>
<li>H5中没有setData方法</li>
</ul>
<h3 data-id="heading-26">7.Picker组件</h3>
<p>onChange钩子，选择下标的取值方法</p>
<ul>
<li>小程序：const value = event.detail.value[0]</li>
<li>H5：const value = event.detail.value</li>
</ul>
<h3 data-id="heading-27">8.Editor组件替换为zx-editor</h3>
<h3 data-id="heading-28">9.Testarea组件绑定的value不能为null，否则会报length of null错误</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">AtTextarea</span>
    <span class="hljs-attr">className</span>=<span class="hljs-string">"AtTextareaFix"</span>
    <span class="hljs-attr">count</span>=<span class="hljs-string">&#123;false&#125;</span>
    <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;textareaProps.value&#125;</span>
    <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;textareaProps.onChange&#125;</span>
    <span class="hljs-attr">maxLength</span>=<span class="hljs-string">&#123;textareaProps.maxLength&#125;</span>
    <span class="hljs-attr">placeholder</span>=<span class="hljs-string">&#123;textareaProps.placeholder&#125;</span>
/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">10.微信浏览器项目更新后拿不到最新的js文件</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">h5: &#123;
    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].[hash].js'</span>,
      <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'js/[name].[chunkhash].js'</span>
    &#125;,
    <span class="hljs-attr">miniCssExtractPluginOption</span>: &#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/[name].[hash].css'</span>,
      <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'css/[name].[chunkhash].css'</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            