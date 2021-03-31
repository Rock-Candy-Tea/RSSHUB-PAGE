
---
title: '通过Chrome插件自动生成骨架屏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94f4b461d7ae410f9f38762ab618563e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 29 Mar 2021 18:36:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94f4b461d7ae410f9f38762ab618563e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文/墨筝</p>
</blockquote>
<h2 data-id="heading-0">背景</h2>
<p>目前大多数前端应用其渲染方式主要还是客户端渲染，渲染的大致过程如下图所示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94f4b461d7ae410f9f38762ab618563e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过这个渲染过程我们可以看出，在js加载完成前如果页面HTML的body中没有dom元素存在，则页面会有一段时间的白屏。并且如果这段渲染内容还依赖于后端数据，那么白屏时间还会更长。目前业界针对这种白屏的处理主要有添加loading和添加骨架屏两种技术方案。</p>
<p>loading方案的主要优点在于技术实现简单，但是对于用户的加载体验仍然不够顺滑。骨架屏方案的主要优点是加载体验对于用户感知来说更加友好和流畅，但是具备更高的技术实现成本，通常需要开发者手动编写代码。关于什么是骨架屏以及为什么要使用骨架屏可以参考 medium 上的这篇文章(需要翻墙)：<a href="https://link.zhihu.com/?target=https%3A//medium.com/better-programming/the-what-why-and-how-of-using-a-skeleton-loading-screen-e68809d7f702" target="_blank" rel="nofollow noopener noreferrer">medium.com/better-prog…</a></p>
<p>目前业界也有一些自动生成页面骨架屏的方案，其核心实现原理是在页面运行起来后，通过无头浏览器 <strong><em><a href="https://link.zhihu.com/?target=https%3A//www.google.com/search%3Fsxsrf%3DALeKk01WjKdek7vtYI9MG4l4wyeYHzoGMg%3A1614061281313%26q%3Dpuppeteer%26spell%3D1%26sa%3DX%26ved%3D2ahUKEwjStMXqrv_uAhVHrZ4KHV1tBjYQkeECKAB6BAgaEDY" target="_blank" rel="nofollow noopener noreferrer">puppeteer</a></em></strong> 在node.js服务中来运行该页面并获取其dom结构然后生成页面的骨架屏html与css。这种方案的缺点在于：</p>
<ul>
<li>难以对页面中某一个区块单独生成骨架屏，在目前大行其道的单页应用(spa)或者各种微前端框架的场景下就更难落地。</li>
<li>存在比较高的工程化成本，需要部署和维护相应的node服务或者在本地调试服务中添加相应的webpack插件</li>
<li>puppeteer包本身是很大的，安装和更新过程非常耗时，如果是在本地调试过程中添加也会一定程度降低开发效率。</li>
</ul>
<p>本篇文章介绍的自动生成页面骨架屏的方案主要通过Chrome插件来实现，使用体验上整体更加轻量化和定制化，能完美解决上述问题，可以先来看看具体效果。</p>
<h2 data-id="heading-1">效果展示</h2>
<p>以我的个人GitHub主页为例</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec8bdaddfae34984a6d35d6a156708c8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>该Chrome插件在浏览器开发者工具栏中增加了一个skeleton的面板用于控制骨架屏生成，填写某个区块的样式选择器后即可为这个区块生成对应的骨架屏代码，并且可以在控制台中一键进行效果预览。</p>
<h2 data-id="heading-2">使用姿势</h2>
<p>由于chrome插件的发布代价不菲，因此目前我暂且没有将其发布到chrome插件市场，开发者如果想要使用，可以通过clone我在GitHub上的代码仓库到本地，然后在本地安装扩展即可。步骤如下：</p>
<h3 data-id="heading-3">第一步，完成Chrome插件的本地安装</h3>
<ol>
<li>
<p>clone插件仓库克隆(<a href="https://link.zhihu.com/?target=https%3A//github.com/NealST/skeleton-chrome-extension" target="_blank" rel="nofollow noopener noreferrer">github.com/NealST/skel…</a>)</p>
<p>git clone <a href="https://github.com/NealST/skeleton-chrome-extension.git" target="_blank" rel="nofollow noopener noreferrer">github.com/NealST/skel…</a></p>
</li>
</ol>
<p>2, 在Chrome地址栏中输入地址 chrome://extensions, 进入扩展程序管理页面</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61910afac00c42aca968acdc6f14e5e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>3，开启开发者模式，然后点击左上角的加载已解压的扩展程序按钮，选择chrome-skeleton-extension所在目录下的build文件夹，点击选择按钮之后便安装完成。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96f38e8b35c641d19a534946bd4870f7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">第二步，选择页面，打开控制台进入使用</h3>
<p>还是以刚才的GitHub页面作为示例</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08aac5a130e141b5bbdda2f2a8318103~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">第三步，选择元素，生成骨架屏，拷贝骨架屏代码</h3>
<p>按照面板表单中提示的输入容器元素的选择器，然后点击生成按钮就可以生成该元素的骨架屏HTML和css，同时面板中同时也提供了react组件的封装。除了容器元素可以自由选择，你还可以定制骨架屏的颜色。</p>
<p>骨架屏生成之后你需要做的就是拷贝HTML和css代码，然后放入到该页面的HTML模板中. 或者直接使用其react组件。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4afd84dfc1bc4a788ebaf4547994dff3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">实现原理</h2>
<p>整个插件的实现原理其核心在于三个部分，分别是浏览器devtool中的面板开发，devtool面板与内容脚本(即插件的content-script)之间的通信以及通过内容脚本生成指定dom的骨架屏结构和样式。</p>
<h3 data-id="heading-7">Devtool面板的开发</h3>
<p>Chrome插件提供了devtool 面板创建的API，你需要做的是为面板生成一个HTML进行渲染，核心代码如下所示：</p>
<pre><code class="copyable">// 创建 devtool 面板 
chrome.devtools.panels.create("Skeleton", "icon-34.png", "devtools-panel.html", (panel) => &#123;
  panel.onShown.addListener(onPanelShown);
  panel.onHidden.addListener(onPanelHidden);
&#125;);

function onPanelShown () &#123;
  chrome.runtime.sendMessage('skeleton-panel-shown');
&#125;

function onPanelHidden() &#123;
  chrome.runtime.sendMessage('skeleton-panel-hidden');
&#125;

// 面板HTML内容的渲染
import React from 'react';
import &#123; render &#125; from 'react-dom';
import &#123; processMessageFromBg, buildConnectionWithBg &#125; from './utils'
import App from './app';

// 建立通信连接
const connection = buildConnectionWithBg();
connection.onMessage.addListener((message) => processMessageFromBg(message));

render(<App />, document.getElementById('app-container'));

// app.jsx的实现
import React, &#123; useState &#125; from 'react';
// 输入表单
import SkeletonForm from './components/skeleton-form';
// 骨架屏HTML展示
import SkeletonHtml from './components/skeleton-html';
// 骨架屏样式展示
import SkeletonCss from './components/skeleton-css';
import './app.css';
export default function() &#123;
  const [ codeInfo, setCodeInfo ] = useState(&#123;
    html: '',
    css: '',
    isMobile: false
  &#125;);
  function getSkeletonCode(retCode) &#123;
    console.log("code info", retCode);
    setCodeInfo(retCode);
  &#125;

  return (
    <div className="devtools-panel">
      <div className="panel-header">
        <SkeletonForm getSkeletonCode=&#123;getSkeletonCode&#125; />
      </div>
      <div className="panel-code">
        <div className="code-html">
          <SkeletonHtml code=&#123;codeInfo.html&#125; isMobile=&#123;codeInfo.isMobile&#125;/>
        </div>
        <div className="code-css">
          <SkeletonCss code=&#123;codeInfo.css&#125; />
        </div>
      </div>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Devtool面板与内容脚本的通信</h3>
<p>devtool面板与内容脚本之间的通信主要通过中间商Chrome插件的background来进行，background运行在Chrome后台，会贯穿插件的整个生命周期，且拥有最高的权限，几乎可以调用一切Chrome插件的API。通信方式的核心实现代码如下所示：</p>
<pre><code class="copyable">// devtool-panel.js 部分
let processFnMap = &#123;&#125;;
// 建立与background页面的链接
export const buildConnectionWithBg = function () &#123;
  const connection = chrome.runtime.connect(&#123;
    name: `skeleton-panel-$&#123;tabId&#125;`,
  &#125;);
  connection.postMessage(&#123;
    type: "init",
    tabId,
  &#125;);
  return connection;
&#125;;

// 处理来自后台网页的响应
export const processMessageFromBg = function (message) &#123;
  console.log("get message", message);
  const processFn = processFnMap[message.type];
  processFn && processFn(message.info);
&#125;;

// 与content脚本进行通信
export const sendMsgToContent = function (info, cb) &#123;
  processFnMap[info.type] = processFnMap[info.type] || cb;
  chrome.runtime.sendMessage(&#123;
    tabId,
    isToContent: true,
    info,
  &#125;);
&#125;;

// background.js 部分
// 通过connections建立长连接
let connections = &#123;&#125;;

chrome.runtime.onConnect.addListener(function (port) &#123;
  var extensionListener = function (message, sender, sendResponse) &#123;
    // 原始的连接事件不包含开发者工具网页的标签页标识符，
    // 所以我们需要显式发送它。
    const &#123; type, tabId &#125; = message || &#123;&#125;;
    if (type == "init") &#123;
      connections[tabId] = port;
      return;
    &#125;
    
  &#125;;

  // 监听开发者工具网页发来的消息
  port.onMessage.addListener(extensionListener);

  port.onDisconnect.addListener(function (port) &#123;
    port.onMessage.removeListener(extensionListener);
    var tabs = Object.keys(connections);
    for (var i = 0, len = tabs.length; i < len; i++) &#123;
      if (connections[tabs[i]] == port) &#123;
        delete connections[tabs[i]];
        break;
      &#125;
    &#125;
  &#125;);
&#125;);

// 接收消息
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) &#123;
  console.log("request", request);
  const &#123; isToContent, tabId, info = &#123;&#125; &#125; = request;
  if (isToContent) &#123;
    // 如果是传给内容脚本
    chrome.tabs.sendMessage(tabId, info, function (response) &#123;
      console.log("response from content", response);
      const thePort = connections[tabId];
      thePort.postMessage(&#123;
        type: info.type,
        info: response
      &#125;);
    &#125;);
  &#125;
  
  // 实现文本复制能力
  if (info.type === 'copy') &#123;
    const copyTextarea = document.getElementById('app-textarea');
    copyTextarea.value = info.data;
    copyTextarea.select();
    document.execCommand( 'copy');
    const thePort = connections[tabId];
    thePort.postMessage(&#123;
      type: info.type,
      info: ''
    &#125;);
  &#125;
&#125;);


// content-script.js部分
chrome.runtime.onMessage.addListener(async function(req, sender, sendRes) &#123;
  switch (req.type) &#123;
    case 'generate':
      const &#123; containerId &#125; = req.data;
      queryInfo = req.data;
      containerEl = document.querySelector(containerId);
      // 如果找不到元素，就返回null
      if (!containerEl) &#123;
        sendRes(null);
        return
      &#125;
      displayStyle = window.getComputedStyle(containerEl).display;
      clonedContainerEl = getClonedContainerEl(containerEl, containerId);
      await genSkeletonCss(clonedContainerEl, req.data);
      const &#123; style, cleanedHtml &#125; = await getHtmlAndStyle(clonedContainerEl);
      const isMobile = window.navigator.userAgent.toLowerCase().indexOf('mobile') > 0;
      skeletonInfo = &#123;
        html: htmlFilter(cleanedHtml),
        css: style,
        isMobile
      &#125;;
      sendRes(skeletonInfo);
      break;
    case 'show':
      containerEl.style.display = 'none';
      clonedContainerEl.style.display = displayStyle;
      break;
    case 'hide':
      containerEl.style.display = displayStyle;
      clonedContainerEl.style.display = 'none';
      break;
    case 'query':
      sendRes(&#123;
        isInPreview: clonedContainerEl && clonedContainerEl.style.display !== 'none',
        queryInfo,
        skeletonInfo
      &#125;);
      break;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">ContentScript的骨架屏生成</h3>
<p>Chrome插件的content-script可以获取并操作当前页面的dom结构，因此在获取到devtool面板发送过来的选择器信息后，所需要做的工作是根据选择器搜索到对应dom并遍历该dom节点下的子元素内容，根据dom节点的不同类型执行对应的骨架屏样式处理算法即可。核心代码如下所示：</p>
<pre><code class="copyable">import svgHandler from "./svg-handler";
import textHandler from "./text-handler";
import listHandler from "./list-handler";
import buttonHandler from "./button-handler";
import backgroundHandler from "./background-handler";
import imgHandler from "./img-handler";
import pseudosHandler from "./pseudos-handler";
import grayHandler from "./gray-handler";
import blockTextHandler from './block-text-handler';
import inputHandler from "./input-handler";
import &#123;
  getComputedStyle,
  checkHasPseudoEle,
  checkHasBorder,
  checkHasTextDecoration,
  isBase64Img,
  $$,
  $,
  checkIsTextEl,
  checkIsBlockEl
&#125; from "./utils";
import &#123; DISPLAY_NONE, EXT_REG, GRADIENT_REG, MOCK_TEXT_ID, Node, DEFAULT_COLOR &#125; from "./constants";
import &#123; transparent, removeElement, styleCache &#125; from "./dom-action";

// 查找并处理元素
function traverse(containerEl, options) &#123;
  const &#123; excludes = [], cssUnit = "px", containerId, color &#125; = options;
  const themeColor = color || DEFAULT_COLOR;
  const excludesEle =
    excludes && excludes.length ? Array.from($$(excludes.join(","))) : [];
  const svg = &#123;
    color: themeColor,
    shape: "circle",
    shapeOpposite: [],
  &#125;;
  const text = themeColor;
  const button = &#123;
    color: themeColor
  &#125;;
  const image = &#123;
    shape: "rect",
    color: themeColor,
    shapeOpposite: [],
  &#125;;
  const pseudo = &#123;
    color: themeColor,
    shape: "circle",
    shapeOpposite: [],
  &#125;;
  const decimal = 4;
  const texts = [];
  const buttons = [];
  const hasImageBackEles = [];
  let toRemove = [];
  const imgs = [];
  const svgs = [];
  const inputs = [];
  const pseudos = [];
  const gradientBackEles = [];
  const grayBlocks = [];
  (function preTraverse(ele) &#123;
    const styles = getComputedStyle(ele);
    const hasPseudoEle = checkHasPseudoEle(ele);
    if (
      !ele.classList.contains(`mz-sk-$&#123;containerId&#125;-clone`) &&
      DISPLAY_NONE.test(ele.getAttribute("style"))
    ) &#123;
      return toRemove.push(ele);
    &#125;

    if (~excludesEle.indexOf(ele)) return false; // eslint-disable-line no-bitwise

    if (hasPseudoEle) &#123;
      pseudos.push(hasPseudoEle);
    &#125;

    if (checkHasBorder(styles)) &#123;
      ele.style.border = "none";
    &#125;
    let styleAttr = ele.getAttribute("style");
    if (styleAttr) &#123;
      if (/background-color/.test(styleAttr)) &#123;
        styleAttr = styleAttr.replace(
          /background-color:([^;]+);/,
          "background-color:#fff;"
        );
        ele.setAttribute("style", styleAttr);
      &#125;
      if (/background-image/.test(styleAttr)) &#123;
        styleAttr = styleAttr.replace(/background-image:([^;]+);/, "");
        ele.setAttribute("style", styleAttr);
      &#125;
    &#125;

    if (ele.children && ele.children.length > 0 && /UL|OL|TBODY/.test(ele.tagName)) &#123;
      listHandler(ele);
    &#125;
    
    // 如果是块级文本元素
    if (checkIsTextEl(ele) && checkIsBlockEl(ele)) &#123;
      blockTextHandler(ele)
    &#125;

    if (ele.children && ele.children.length > 0) &#123;
      Array.from(ele.children).forEach((child) => preTraverse(child));
    &#125;

    // 将所有拥有 textChildNode 子元素的元素的文字颜色设置成背景色，这样就不会在显示文字了。
    if (
      ele.childNodes &&
      Array.from(ele.childNodes).some((n) => n.nodeType === Node.TEXT_NODE)
    ) &#123;
      transparent(ele);
    &#125;
    if (checkHasTextDecoration(styles)) &#123;
      ele.style.textDecorationColor = TRANSPARENT;
    &#125;
    // 隐藏所有 svg 元素
    if (ele.tagName === "svg") &#123;
      return svgs.push(ele);
    &#125;

    // 输入框元素
    if (ele.tagName === "INPUT") &#123;
      return inputs.push(ele);
    &#125;

    if (
      EXT_REG.test(styles.background) ||
      EXT_REG.test(styles.backgroundImage)
    ) &#123;
      return hasImageBackEles.push(ele);
    &#125;
    if (
      GRADIENT_REG.test(styles.background) ||
      GRADIENT_REG.test(styles.backgroundImage)
    ) &#123;
      return gradientBackEles.push(ele);
    &#125;
    if (ele.tagName === "IMG" || isBase64Img(ele) || ele.tagName === "FIGURE") &#123;
      return imgs.push(ele);
    &#125;
    if (
      ele.nodeType === Node.ELEMENT_NODE &&
      (ele.tagName === "BUTTON" ||
        (ele.tagName === "A" && ele.getAttribute("role") === "button"))
    ) &#123;
      return buttons.push(ele);
    &#125;
    if (checkIsTextEl(ele)) &#123;
      return texts.push(ele);
    &#125;
  &#125;)(containerEl);

  svgs.forEach((e) => svgHandler(e, svg, cssUnit, decimal));
  inputs.forEach(e => inputHandler(e, themeColor));
  texts.forEach((e) => textHandler(e, text, cssUnit, decimal));
  buttons.forEach((e) => buttonHandler(e, button));
  hasImageBackEles.forEach((e) => backgroundHandler(e, image));
  imgs.forEach((e) => imgHandler(e, image));
  pseudos.forEach((e) => pseudosHandler(e, pseudo));
  gradientBackEles.forEach((e) => backgroundHandler(e, image));
  grayBlocks.forEach((e) => grayHandler(e, button));
  // remove mock text wrapper
  const offScreenParagraph = $(`#$&#123;MOCK_TEXT_ID&#125;`);
  if (offScreenParagraph && offScreenParagraph.parentNode) &#123;
    toRemove.push(offScreenParagraph.parentNode);
  &#125;
  toRemove.forEach((e) => removeElement(e));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">结语</h2>
<p>目前该插件已经在我们内部的工作台应用中完成落地实践，以肉眼可见的效果提升了页面的加载体验。欢迎你在项目中使用它，如果你对该插件或骨架屏有兴趣，或者在使用上有任何的问题和新需求的反馈都可以随时联系我。</p>
<p>公司邮箱：<a href="mailto:mozheng.sh@alibaba-inc.com">mozheng.sh@alibaba-inc.com</a></p>
<p>个人邮箱：<a href="mailto:m13710224694@163.com">m13710224694@163.com</a></p>
<p>ps：我们业务平台-体验技术星环团队正在广招前端和客户端的人才，团队和谐友爱，技术氛围浓厚(leader们倡导no code, no bb)，业务和技术场景也都非常广阔，欢迎与我联系。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            