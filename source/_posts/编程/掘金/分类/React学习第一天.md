
---
title: 'React学习第一天'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b05800b3813e487892a222d9e5ed721d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 16:35:07 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b05800b3813e487892a222d9e5ed721d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>这是我参与8月更文挑战的第17天，活动详情查看：</code><a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">更文挑战</a></p>
<h3 data-id="heading-0">介绍react</h3>
<h4 data-id="heading-1">特点</h4>
<p>高效：React通过对DOM的模拟，最大限度地减少与DOM的交互</p>
<p>组件化：React采取组件化开发，极大限度的使组件得到复用，便于开发管理与维护</p>
<p>适用多端：一处开发，多端适用，将颠覆整个互联网行业</p>
<h4 data-id="heading-2">github</h4>
<p>点击进入react的github网站 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react" ref="nofollow noopener noreferrer">react</a></p>
<p>演示的当前版本是16版本，</p>
<p>我们基于ES6语法，讲解16版本的react</p>
<p>在16版本中，只支持ES6开发。</p>
<h4 data-id="heading-3">两个库</h4>
<p>React为了实现多端适配，将整个库拆分成两个库</p>
<p>核心库：react.js，负责创建组件和虚拟DOM</p>
<p>渲染库：我们讲解web端，使用react-dom，将创建的组件或者虚拟DOM，在该端能够渲染。</p>
<h4 data-id="heading-4">核心库</h4>
<p>核心库提供了createElement方法，创建虚拟DOM</p>
<p>第一个参数表示虚拟DOM名称，也可以是组件类</p>
<p>第二个参数表示属性对象</p>
<p>从第三个参数开始，表示子虚拟DOM</p>
<p>也要用createElement方法来创建，但是文本节点可以直接写</p>
<p>返回值就是虚拟DOM</p>
<h4 data-id="heading-5">虚拟DOM</h4>
<p>虚拟DOM就是一个js对象</p>
<p>key 表示虚拟DOM的id</p>
<p>props 表示虚拟DOM的属性对象</p>
<p>ref 用来在js中，引用虚拟DOM</p>
<p>type 表示虚拟DOM类型</p>
<h4 data-id="heading-6">渲染库</h4>
<p>例如在web端，我们使用react-dom渲染库，提供了render方法，用来渲染虚拟DOM</p>
<p>第一个参数表示虚拟DOM</p>
<p>第二个参数表示容器元素</p>
<p>第三个参数是回调函数，表示渲染成功时候执行的函数。</p>
<pre><code class="hljs language-react copyable" lang="react">// 引入react
import &#123; createElement &#125; from 'react'
// 引入渲染库
import &#123; render &#125; from 'react-dom';
// import * as A from 'react'
// console.log(A)
// 创建虚拟DOM
 var h1 = createElement('h1', &#123; title: 'hello' &#125;, '菜鸟学习')
console.log(h1)
 // 将虚拟DOM渲染到页面中
 render(h1, document.getElementById('app'), (...args) => &#123;
  console.log(args)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">组件</h4>
<p>虚拟DOM是对真实DOM模拟，因此开发项目要定义很多的虚拟DOM，为了复用虚拟DOM，react提供了组件。</p>
<p>从16版本开始，只能使用ES6语法开发项目</p>
<p>在ES5开发中，定义组件，使用React.createClass方法</p>
<p>在ES6开发中，组件就是一个类，因此定义组件就是定义一个类，为了让组件类具有组件的行为，我们要让组件类继承组件基类Component</p>
<p>语法 class 类名 extends Component &#123;&#125;</p>
<p>使用父组件的目的是为了复用虚拟DOM，因此我们可以通过render方法去渲染虚拟DOM</p>
<p>返回值就是渲染的虚拟DOM树</p>
<p>为了将虚拟DOM渲染到页面在，我们使用render方法，但是render方法的第一个参数是虚拟DOM不是组件。因此我们要将组件转换成虚拟DOM</p>
<p>可以通过createElement方法将组件转化成虚拟DOM</p>
<p>注意：</p>
<p>组件是类，因此首字母要大写</p>
<p>render方法返回值是虚拟DOM树，只能有且只有一个根节点。</p>
<pre><code class="hljs language-react copyable" lang="react">class Demo extends Component &#123;
  // 渲染虚拟DOM
  render() &#123;
  // 返回值就是虚拟DOM
  return createElement(
  'ul',
  null,
  createElement('li', null, '教你学习'),
  )
  &#125;
 &#125;
 // 将组件转换成虚拟DOM
 var demo = createElement(Demo);
 // 渲染
 // 通过id名称访问该元素
render(demo, app)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">jsx语法</h4>
<p>react团队认为定义虚拟DOM使用createElement方法，太麻烦了。因此参考了xhtml语法规范，实现了jsx语法。来简化定义虚拟DOM</p>
<p>在xhtml中定义div： </p><div></div><p></p>
<p>在jsx中定义div： </p><div></div><p></p>
<p>在xhtml中定义input: <input type="checkbox" disabled></p>
<p>在jsx中定义input: <input type="checkbox" disabled></p>
<p>在jsx语法中，定义虚拟DOM跟定义真实的DOM是一样的，不过浏览器不允许我们在js中使用jsx语法，所以我们要编译。（jsx语法已经纳入es7规范了）</p>
<p>jsx语法被纳入es规范，因此也可以通过babel工具编译。</p>
<p>为了编译jsx语法，我们要引入babel-presets-react插件</p>
<p>我们基于es6语法开发项目，因此为了编译es6语法，要引入babel-preset-es2015插件</p>
<p>所以在es6中使用jsx语法，我们要引入这两个插件</p>
<p>为了区别使用jsx语法，还是使用js语法，建议我们将文件的拓展名定义成.jsx</p>
<p>有时候，也可以在es6中使用jsx语法，可以在拓展名后面添加x来区分</p>
<p>例如：.jsx, .esx, .es6x</p>
<p>在react开发中，建议使用jsx。</p>
<p>jsx语法就是为了提到createElement方法的</p>
<p>编译结果</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b05800b3813e487892a222d9e5ed721d~tplv-k3u1fbpfcp-watermark.image" alt="图片1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3201b6c1c01f4a74bcd7e6b7bf5692c5~tplv-k3u1fbpfcp-watermark.image" alt="图片2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-react copyable" lang="react"> class Demo extends Component &#123;
  // 渲染
  render() &#123;
  // jsx语法中，开发虚拟DOM，跟写DOM的方式是一样的
 return (
  <ul>
  <li>教你学习</li>
  </ul>
  )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">插值</h4>
<p>我们已经学过的插值语法：</p>
<p>ejs： <code><%=%></code></p>
<p>MVC: <code><%%></code></p>
<p>es6： <code>$&#123;&#125;</code></p>
<p>less: <code>@&#123;&#125;</code></p>
<p>scss: <code>#&#123;&#125;</code></p>
<p>微信： <code>&#123;&#123;&#125;&#125;</code></p>
<p>vue: <code>&#123;&#123;&#125;&#125;</code></p>
<p>在一个非js环境下，想使用js中的表达式，我们可以使用插值语法</p>
<p>jsx环境不是js环境，在jsx语法中，我们无法使用js表达式，因此想在jsx语法中使用js表达式，我们就要使用插值语法： &#123;&#125;</p>
<p>插值语法提供了真实的js环境，因此可以使用js表达式</p></div>  
</div>
            