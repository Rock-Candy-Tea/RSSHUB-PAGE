
---
title: 'React项目使用styled-components后的几点感受'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59e274a42658480fbce9f10dd6feb120~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 02:54:07 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59e274a42658480fbce9f10dd6feb120~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在项目里使用了 styled-components 来写 CSS，感觉有一些好处，但也遇到了一些问题，本文简单记录一下这一个多月的使用感受。</p>
<p>首先，简单介绍一下 styled-components，它是一种 CSS-in-JS 的实现，它<a href="https://styled-components.com/" target="_blank" rel="nofollow noopener noreferrer">官网</a>的介绍是：</p>
<blockquote>
<p>Utilising tagged template literals (a recent addition to JavaScript) and the power of CSS, styled-components allows you to write actual CSS code to style your components. It also removes the mapping between components and styles – using components as a low-level styling construct could not be easier!</p>
</blockquote>
<p>简而言之，它是利用 ES6 的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Template_literals#%E5%B8%A6%E6%A0%87%E7%AD%BE%E7%9A%84%E6%A8%A1%E6%9D%BF%E5%AD%97%E7%AC%A6%E4%B8%B2" target="_blank" rel="nofollow noopener noreferrer">tagged template literals</a> 创建 React 纯样式组件。</p>
<p>简单看一个例子：</p>
<pre><code class="copyable">import styled from 'styled-components'

const Button = styled.button`
  color: red;
`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <em>styled.button``</em> 语法其实就是一个 tagged template literals，它实际上相当于调用了一个 button 函数。得到的 Button 组件和其他的一般的 React 组件的用法是一样的：</p>
<pre><code class="copyable"><Button>Click Me!</Button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一段时间使用下来，感觉是 styled-components 还是很容易上手的，学习曲线很平缓，它还有以下一些优点。</p>
<h1 data-id="heading-0">好的方面</h1>
<h2 data-id="heading-1">1. 没有想样式名的烦恼了</h2>
<p>不用再想每个样式对应的 className 了，有 JSX 组件名就行，消除了开发人员想合适的 className 的烦恼。而且，它会生成全局唯一类名，不用担心冲突。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59e274a42658480fbce9f10dd6feb120~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，我们不用为 DOM 元素定义 className 了，只需要想一个语义化的组件名就好了。</p>
<h2 data-id="heading-2">3. 很容易找到组件对应的样式代码</h2>
<p>因为用 styled-components 定义的组件是一个 JS 变量，可以很容易的在定义和使用的地方之间相互跳转，用起来很方便。</p>
<p>即使引用了一些定义在别的文件的公共组件（比如 Typography 字体），也能很快跳转过去。</p>
<p>不会像以前一样，如果样式文件很大以后，需要通过搜索 className 才能找到相应的样式。</p>
<h2 data-id="heading-3">4. 不会有没用到的样式代码</h2>
<p>以前用 SASS/LESS 之类的库时，因为代码结构的调整很容易造成一些嵌套的样式代码最终变成 dead code，尤其是大项目里修改别人的代码很容易出现这类问题。</p>
<p>使用了 styled-components 之后，如果项目中用了 Typescript，并且启用了 no-unused-vars 检查，那么我们就能保证项目里不会因为改来改去造成没有用到的样式代码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d970bcf37cf4d4aab602f01a8680b24~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面再来列举一下目前使用下来感觉 styled-components 一些不太好的地方。</p>
<h1 data-id="heading-4">不太好的方面</h1>
<h2 data-id="heading-5">1. 生成的 className 是随机字符串，不方便 debug</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3899347991a54641a5ad3a8453f4fb73~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上文说了 styled-components 的一大好处就是不用我们想 className 了，但是这样也带来了一个麻烦，就是它自动生成的 className 都是一些随机字符串，在浏览器 console 里很不方便调试。</p>
<p>不过可以安装 <a href="https://styled-components.com/docs/tooling#better-debugging" target="_blank" rel="nofollow noopener noreferrer">babel-plugin-styled-components</a> 解决这个问题。</p>
<p>设置好后，就可以在浏览器里看到可读的class名，像这样：</p>
<pre><code class="copyable"><div class="Title-gvPLgb">...</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2. createGlobalStyle 里引用字体文件造成每次重新渲染都需要重新下载字体文件</h2>
<p>之前项目里遇到了一个很奇怪的 bug，在一个输入框里打字的时候，输入框上面 label 文字会闪烁。</p>
<p>最后才发现是因为我们在 styled-components 的 createGlobalStyle 里面用 @font-face 引用了自定义的字体文件，这会导致每一次页面刷新时字体文件都会重新下载，所以看到的就是文字从一种字体变为另一种字体，看起来就是闪烁了一下。</p>
<pre><code class="copyable">import &#123; createGlobalStyle &#125; from 'styled-components';

const GlobalStyle = createGlobalStyle`
  @font-face &#123;
    font-family: "MyFont";
    src: url("static/fonts/Std-Regular.otf");
  &#125;
  @font-face &#123;
    font-family: "MyFont";
    font-weight: bold;
    src: url("static/fonts/Std-Bold.otf");
  &#125;
  @font-face &#123;
    font-family: "MyFont";
    font-weight: 600;
    src: url("static/fonts/Std-SemiBold.otf");
  &#125;
  
`;

export default GlobalStyle;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们的解决方案是，还是用普通 CSS 的方式（index.css）引入字体文件。</p>
<h2 data-id="heading-7">3. 默认没有 CSS 语法高亮和提示</h2>
<p>用 styled-components 写 CSS 代码时，默认是没有语法高亮和提示的，这样写起来就会比较痛苦，而且即使有时候不小心写错了 CSS 属性名或属性值，它也不会报错，只是样式不生效而已。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4d6760481d54c638ce3f78b226ec094~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如上面这个例子里，width 就是不生效的，应该写成 10px，但是默认是不会报错的。</p>
<p>不过，这个问题可以通过一些插件解决，比如 intellij 里可以安装 Styled Components & Styled JSX 这个插件。</p>
<h2 data-id="heading-8">4. 重写组件样式不生效</h2>
<p>刚开始用 styled-components 的人，很容易遇到重写样式不生效的问题，比如下面的例子，StyledLink 想要重写 Link 上的颜色和字体粗细，结果发现并不生效。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88cf8c6fce1944479eb1068876d1a2b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查了文档才发现，必须要把 className 传递给组件才生效（如果是 React Native 组件，需要把 style 传递下去）。</p>
<blockquote>
<p>The styled method works perfectly on all of your own or any third-party component, as long as they attach the passed className prop to a DOM element.</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c35fdc6bef0b4084b024a8face391489~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">总结</h1>
<p>就我目前这短暂的使用经历来说，我自己还是比较喜欢用 styled-components 的，提高了一点儿我的开发效率。</p></div>  
</div>
            