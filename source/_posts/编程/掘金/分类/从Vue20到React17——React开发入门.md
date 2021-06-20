
---
title: '从Vue2.0到React17——React开发入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6852'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 05:17:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=6852'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”</p>
<h2 data-id="heading-0">前言</h2>
<p>找工作时发现有一些公司是以React作为技术栈的，而且薪资待遇都不错，为了增加生存的筹码，所以还是得去学一下React，增加一项求生技能。因为我用Vue2.0开发项目已经四年了，故用Vue2.0开发项目的思路来学习React。</p>
<p>前端项目是由一个个页面组成的，对于Vue来说，一个页面是由多个组件构成的，页面本身也是一个路由组件。对于React来说也是如此。Vue会提供一系列技术支持来完成一个组件的开发，可以从这一系列技术支持出发，去React中寻找对应的技术支持来入门React，比如React中如何开发组件的UI，React中如何使用组件，React中如何定义组件数据等等。</p>
<p>本专栏将按照这个思路带领你从Vue2.0入门React17。</p>
<h2 data-id="heading-1">1、脚手架</h2>
<p>首先得选择一个脚手架搭建一个React工程，React有很多脚手架，为什么选择UmiJS这个脚手架，不为什么，这个脚手架和Vue Cli比较类似，至少路由配置和Vue Router很类似。</p>
<p>在学习前，先用UmiJS搭建一个React工程，步骤很简单：</p>
<ul>
<li>先找个地方建个空目录，打开命令行工具，执行命令 <code>mkdir myapp && cd myapp</code>；</li>
<li>执行命令<code>npm create @umijs/umi-app</code>创建一个React工程；</li>
<li>执行命令<code>npm install</code>安装依赖；</li>
<li>依赖安装成功后，执行命令<code>npm run start</code>启动项目，在浏览器上打开 <a href="http://localhost:8000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8000</a> 访问项目。</li>
</ul>
<p>可以看见myapp这个React工程的目录结构如下所示：</p>
<pre><code class="copyable">.
├── package.json
├── .umirc.ts
├── .env
├── dist
├── mock
├── public
└── src
    ├── .umi
    ├── layouts/index.tsx
    ├── pages
        ├── index.less
        └── index.tsx
    └── app.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开 .umirc.ts 文件，其内容如下所示</p>
<pre><code class="copyable">import &#123; defineConfig &#125; from 'umi';

export default defineConfig(&#123;
  nodeModulesTransform: &#123;
    type: 'none',
  &#125;,
  routes: [
    &#123; path: '/', component: '@/pages/index' &#125;,
  ],
  fastRefresh: &#123;&#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其路由是在<code>routes</code>选项中配置，配置和Vue Router非常相似，具体如何配置放在后面介绍路由跳转和传参中一并介绍。</p>
<p>接下来在<em>src/pages/index.tsx</em>文件中书写demo来学习React。</p>
<h2 data-id="heading-2">2、React中如何开发组件的UI</h2>
<p>Vue和React中所开发的都是组件，其页面也是一个路由组件。在Vue中组件是定义在后缀为<code>.vue</code>的文件中，在React中组件是定义在后缀为<code>.js</code>的文件中，若使用TypeScript来开发React，则其组件是定义在后缀为<code>.tsx</code>的文件中。</p>
<p>那如何开发一个组件的UI部分，例如开发一个 HelloWorld 组件在浏览器页面上展示<strong>hello world</strong>，一个组件的UI包括HTML部分和CSS部分。</p>
<h3 data-id="heading-3">2.1 HTML部分</h3>
<p>组件的HTML部分，Vue推荐使用template模板，React推荐使用JSX语法。</p>
<p>在工程的<em>src/pages</em>文件夹中创建一个<em>HelloWorld.js</em>文件，在其中开发HelloWorld组件。</p>
<p>此外React组件有两种定义方法，一种是函数形式，一种是ES6的class形式。</p>
<p>函数形式，称为函数组件：</p>
<pre><code class="copyable">export default function HelloWorld() &#123;
  return (
    <div>hello world</div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6的class形式，称为类组件：</p>
<pre><code class="copyable">import React from 'react';
export default class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
  &#125;

  render() &#123;
    return (
      <div>hello world</div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这里要注意函数名的首字母要大写</strong>。在函数中的<code>return</code>后面用JSX语法来开发组件的UI部分。</p>
<p>另外还要注意在<code>return</code>后面的内容最外面要用<code>()</code>括起来，否则在<code>return</code>同一行后面最少跟一个<code><</code>才可以，如下所示：</p>
<pre><code class="copyable">export default function HelloWorld() &#123;
  return <
    div>hello world</div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样看起来是不是怪怪的，所以最好加个<code>()</code>。</p>
<h3 data-id="heading-4">2.2 绑定 Class 和 Style</h3>
<p>关于组件的CSS部分，其最重要的是绑定 Class 和 Style，才能给组件的HTML添加样式。</p>
<p>先来看一下 Class 与 Style 是固定不变，React 中是怎么绑定的。</p>
<pre><code class="copyable">export default function HelloWorld() &#123;
  return (
    <div 
      className="title head"
      style=&#123;&#123;color:'red',fontSize:'16px'&#125;&#125;
    >
      hello world
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React中是用<code>className</code>来绑定 Class，用<code>style</code>来绑定 Style。其中<code>style</code>接受的值是一个对象，且用<code>&#123;&#125;</code>中括号传入，而且对象的属性名只能用驼峰式 (camelCase) 来命名。</p>
<p>在来看一下 Class 与 Style 是变量，在React中是怎么绑定的。</p>
<ul>
<li>类组件的写法：</li>
</ul>
<pre><code class="copyable">import React from 'react';
export default class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      styleData: &#123; color: 'red', 'fontSize': "16px" &#125;,
      isHead: true,
      className: 'title'
    &#125;;
  &#125;

  render() &#123;
    return (
      <div
        className=&#123;`$&#123;this.state.className&#125; $&#123;this.state.isHead ? 'head' : ''&#125;`&#125;
        style=&#123;this.state.styleData&#125;
      >
        hello world
      </div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数组件的写法：</li>
</ul>
<pre><code class="copyable">import &#123; useState &#125; from 'react';
export default function HelloWorld() &#123;
  const [styleData] = useState(&#123; color: 'red', 'fontSize': "16px" &#125;);
  const [isHead] = useState(true);
  const [className] = useState('title');
  return (
    <div
      className=&#123;`$&#123;className&#125; $&#123;isHead ? 'head' : ''&#125;`&#125;
      style=&#123;styleData&#125;
    >
      hello world
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在React中是使用<code>&#123;&#125;</code>给属性赋值变量，且<code>className</code>只接受字符串，不接受数组或者对象，可以用ES6的模板字符串功能来拼接变量生成字符串。</p>
<p>在函数组件的写法中用<code>useState</code>这个React Hook定义了一些变量，<code>useState</code>的作用放在后面介绍。</p>
<h2 data-id="heading-5">3、React中如何使用组件</h2>
<p>HelloWorld 组件写好了，要如何使用呢？先回顾一下在Vue中是如何使用组件的，在使用组件前要先注册，可以注册为全局组件或局部组件。</p>
<p>在React中是没有注册组件的概念，因为组件相当一个函数，只有引入组件的概念，也没有全局组件的概念。使用组件前必须用<code>import</code>先把组件引入并命名。</p>
<pre><code class="copyable">import HelloWorld from './HelloWorld.js'

export default function Index()&#123;
  return (
    <HelloWorld/>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在React中组件的命名必须以大写字母开头，因为 React 会将以小写字母开头的组件视为原生 DOM 标签</strong>。</p>
<h2 data-id="heading-6">4、React中如何定义组件数据</h2>
<p>从开发Vue组件的经验来说，一个组件的数据，可以分为内部数据和参数数据两种。对于React也是如此，在React中把内部数据称为state，把参数数据称为props。</p>
<h3 data-id="heading-7">4.1 定义内部数据state</h3>
<p>在上面介绍React中如何绑定变量形式的 Class 和 Style 的过程已经定义了<code>styleData</code>、<code>isHead</code>、<code>className</code>这些内部数据。</p>
<ul>
<li>在类组件中是在<code>this.state</code>这个对象中定义数据：</li>
</ul>
<pre><code class="copyable">this.state = &#123;
  styleData: &#123; color: 'red', 'fontSize': "16px" &#125;,
  isHead: true,
  className: 'title'
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在函数组件的写法中使用<code>useState</code>这个React Hook定义了数据：</li>
</ul>
<pre><code class="copyable">const [styleData] = useState(&#123; color: 'red', 'fontSize': "16px" &#125;);
const [isHead] = useState(true);
const [className] = useState('title');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>个人推荐使用函数形式来开发React组件，可以使用React Hook，来避免去学习 ES6 中 的 class 语法，还有烦人的<code>this</code>指向问题，从而来降低入门难度。</p>
<p>关于的React Hook 可以看<a href="https://zh-hans.reactjs.org/docs/hooks-intro.html" target="_blank" rel="nofollow noopener noreferrer">这里</a> 。</p>
<h3 data-id="heading-8">4.2 定义参数数据props</h3>
<p>props用来接收外部传递给组件的数据。例如在 HelloWorld 组件中定义<code>title</code>一个参数数据。</p>
<ul>
<li>类组件的写法：</li>
</ul>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
  &#125;

  render() &#123;
    return (
      <div>&#123;this.props.title&#125;</div>
    );
  &#125;
&#125;
HelloWorld.defaultProps = &#123;
  title: 'hello world'
&#125;;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在类组件中的构造函数<code>constructor</code>接受<code>props</code>作为传入组件的参数数据集合，并调用<code>super(props)</code>把<code>props</code>传给<code>React.Component</code>构造函数，这样类组件才能接受参数数据集合<code>props</code>，再用<code>this.props.title</code>来读取<code>title</code>参数数据的值，另外可以用<code>defaultProps</code>来定义<code>title</code>参数数据的默认值。</p>
<ul>
<li>函数组件的写法：</li>
</ul>
<pre><code class="copyable">import &#123; useState &#125; from 'react';
export default function HelloWorld(props) &#123;
  const &#123;title = 'hello world'&#125; = props;
  return (
    <div>&#123;title&#125;</div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件接收一个<code>props</code>作为传入组件参数数据的集合，利用 ES6 解构赋值的功能，来获取组件的参数数据，并可以给参数数据设置默认值。</p>
<p><strong>这里要注意了</strong>，在Vue的template模板中是用<code>&#123;&#123;&#125;&#125;</code>（双大括号）来使用数据的，而在React中是统一用<code>&#123;&#125;</code>（单大括号）来使用数据的。</p>
<p>参数数据Props是用接收外部传递给组件的数据，那React中如何向组件传递数据呢？</p>
<h2 data-id="heading-9">5、React中如何向组件传递数据</h2>
<p>在Vue中规定了动态数据和字符串、数字、布尔值、数组、对象类型的静态数据如何传递给组件，我们一一对应去寻找React中如何传递。</p>
<ul>
<li>传递动态数据</li>
</ul>
<pre><code class="copyable">import &#123; useState &#125; from 'react';
import HelloWorld from './HelloWorld.js';
export default function Index()&#123;
  const [styleData] = useState(&#123; color: 'red', 'fontSize': "16px" &#125;);
  const [isHead] = useState(true);
  const [className] = useState('title');
  return (
    <HelloWorld 
       styleData=&#123;styleData&#125; 
       isHead=&#123;isHead&#125; 
       className=&#123;className&#125;
    />
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>传递字符串类型的静态数据</li>
</ul>
<pre><code class="copyable"><HelloWorld title="hello vue"></HelloWorld>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>传递数字类型的静态数据</li>
</ul>
<pre><code class="copyable"><HelloWorld num=&#123;1&#125;></HelloWorld>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>传递布尔值类型的静态数据</li>
</ul>
<pre><code class="copyable"><HelloWorld isHead=&#123;false&#125;></HelloWorld>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>传递数组类型的静态数据</li>
</ul>
<pre><code class="copyable"><HelloWorld className=&#123;['title','head']&#125;></HelloWorld>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>传递对象类型的静态数据</li>
</ul>
<pre><code class="copyable"><HelloWorld styleData=&#123;&#123;color:'red','fontSize':"16px"&#125;&#125;></HelloWorld>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见在React中，除了传递字符串类型的静态数据，都要用<code>&#123;&#125;</code>包裹数据再赋值给组件标签上的属性来传递数据给组件。</p>
<h2 data-id="heading-10">6、React中如何监听DOM事件</h2>
<h3 data-id="heading-11">6.1 监听DOM元素的DOM事件</h3>
<ul>
<li>类组件的写法：</li>
</ul>
<pre><code class="copyable">import React from 'react';
export default class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    // 为了在回调中使用 `this`，这个绑定是必不可少的
    this.handleClick = this.handleClick.bind(this);
  &#125;
  
  handleClick() &#123;
    console.log('点击事件');
  &#125;

  render() &#123;
    return (
      <div onClick=&#123;this.handleClick&#125;>hello world</div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数组件的写法：</li>
</ul>
<pre><code class="copyable">export default function HelloWorld() &#123;
  const handleClick = ()=>&#123;
     console.log('点击事件');
  &#125;
  return (
    <div onClick=&#123;handleClick&#125;>hello world</div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React中用<code>onClick</code>来监听点击事件，用<code>&#123;&#125;</code>包裹点击事件触发时执行的函数，再赋值给<code>onClick</code>。</p>
<p>其中<code>onClick</code>是一个合成事件，在Vue中<code>@</code>后面跟着是DOM的原生事件，而React中<code>on</code>后面跟着并不是DOM的原生事件。例如Vue中监听双击事件 <code>@dblclick</code>，而React中监听双击事件 <code>onDoubleClick</code>。</p>
<p>React中的合成事件具体可以看<a href="https://zh-hans.reactjs.org/docs/events.html#mouse-events" target="_blank" rel="nofollow noopener noreferrer">这里</a>。</p>
<h3 data-id="heading-12">6.2 监听React组件的DOM事件</h3>
<p>在Vue中用<code>.native</code>修饰符来监听组件上的DOM事件，而在React中监听组件上的DOM事件要这样实现。</p>
<p>例如在组件上监听click事件，先要把click事件触发时要执行的函数当作Props给组件传递进去，在组件的根元素上监听click事件，click事件触发时执行该Props，这样来间接监听组件上的click事件。具体实现如下所示：</p>
<ul>
<li>类组件的写法：</li>
</ul>
<pre><code class="copyable">import React from 'react';
export default class HelloWorld extends React.Component &#123;
  constructor(props:any) &#123;
    super(props);
    console.log(this.props)
    this.handleClick = this.handleClick.bind(this);
  &#125;

  handleClick() &#123;
    this.props.onClick();
  &#125;

  render() &#123;
    return (
      <div onClick=&#123;this.handleClick&#125;>hello world</div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import React from 'react';
import HelloWorld from './HelloWorld';
export default class Grandfather extends React.Component &#123;
  handleClick() &#123;
    console.log('点击事件');
  &#125;
  render() &#123;
    return (
      <HelloWorld onClick=&#123;() => &#123; this.handleClick() &#125;&#125;>
      </HelloWorld>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数组件的写法：</li>
</ul>
<pre><code class="copyable">export default function HelloWorld(props) &#123;
  const &#123; onClick &#125; = props
  const handleClick = () => &#123;
    onClick();
  &#125;
  return (
    <div onClick=&#123;handleClick&#125;>hello world</div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import HelloWorld from './HelloWorld';
export default function Index()&#123;
  const handleClick = ()=>&#123;
    console.log('点击事件');
  &#125;
  return (
    <HelloWorld onClick=&#123;() => &#123; handleClick() &#125;&#125;>
    </HelloWorld>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">7、React中组件如何改变数据</h2>
<p>上面介绍了，React组件的数据分为内部数据state和参数数据props，对应的改变方法也不一样。</p>
<h3 data-id="heading-14">7.1 改变内部数据state</h3>
<p>比如要改变组件中定义的内部数据<code>title</code>。</p>
<ul>
<li>类组件的写法：</li>
</ul>
<pre><code class="copyable">import React from 'react';
export default class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      title: 'hello world',
      className: 'title'
    &#125;;
    // 为了在回调中使用 `this`，这个绑定是必不可少的
    this.handleClick = this.handleClick.bind(this);
  &#125;
  
  handleClick() &#123;
    this.setState(state => (&#123;
      title: 'hello react',
      className: 'title active'
    &#125;));
  &#125;

  render() &#123;
    return (
      <div 
        className=&#123;className&#125;
        onClick=&#123;this.handleClick&#125;
      >&#123;title&#125;</div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>this.setState()</code>中可以传递一个函数或一个对象，建议传递一个函数<code>(state,props) =>&#123;&#125;</code>，函数可以接受内部数据state和参数数据props作为参数，而且<code>state</code>和<code>props</code>只读无法修改，每次调用<code>this.setState</code>时读取到的state和Props都是最新，特别适用多次调用<code>this.setState</code>修改同一个state的场景。最后函数放回一个对象，对象的内容为要修改的state。</p>
<ul>
<li>函数组件的写法：</li>
</ul>
<pre><code class="copyable">import &#123; useState &#125; from 'react';
export default function HelloWorld() &#123;
  const [title,setTitle] = useState('hello world');
  const [className,setClassName] = useState('title');
  const handleClick = () =>&#123;
    setTitle('hello react');
    setClassName('title active')
  &#125;
  return (
    <div 
      className=&#123;className&#125; 
      onClick=&#123;handleClick&#125;
    >
      &#123;title&#125;
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在React中称内部数据为state，使用<code>useState(param)</code>定义一个state时，可以通过参数<code>param</code>设置state的默认值，其返回一个数组，数组的第一个值是state，数组的第二个值是改变state的函数，可以调用该函数来改变state。</p>
<p>另外用<code>useState</code>定义的数据是响应式的，若页面有使用该数据，该数据改变后页面会重新渲染。</p>
<h3 data-id="heading-15">7.2 改变参数数据props</h3>
<p>跟Vue一样，在组件中是不能直接改变props，假如要改变props，只能通过在父组件中改变传递给子组件的数据来间接改变props，那在子组件中怎么让父组件改变传递给子组件的数据呢，将在React中父子组件如何通讯介绍。</p>
<h2 data-id="heading-16">8、React中父子组件如何通讯</h2>
<p>用一个例子来介绍，假如 HelloWorld 组件的 “hello world” 是用参数数据props中的<code>title</code>展示，点击组件中的改变标题按钮时变成 “hello React” 。</p>
<ul>
<li>类组件的写法：</li>
</ul>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.handleChangeTitle=this.handleChangeTitle.bind(this);
  &#125;
  handleChangeTitle()&#123;
    this.props.changeTitle('hello React');
  &#125;
  render() &#123;
    return (
      <div>
        &#123;this.props.title&#125;
        <button 
          onClick=&#123;this.handleChangeTitle.bind(this)&#125;>
          改变标题
        </button>
      </div>
    );
  &#125;
&#125;
HelloWorld.defaultProps = &#123;
  title: 'hello world'
&#125;;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import HelloWorld from './HelloWorld.js'
import React from 'react'
class Index extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state=&#123;
      info:'hello world'
    &#125;;
    this.handleChangeTitle=this.handleChangeTitle.bind(this);
  &#125;
  handleChangeTitle(data)&#123;
    this.setState(state =>&#123;
      return &#123;
        info:data
      &#125;
    &#125;)
  &#125;
  render() &#123;
    return (
      <HelloWorld 
        title=&#123;this.state.info&#125; 
        changeTitle=&#123;this.handleChangeTitle&#125;>
      </HelloWorld>
    );
  &#125;
&#125;
export default Index;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数组件的写法：</li>
</ul>
<pre><code class="copyable">export default function HelloWorld(props: any) &#123;
  const &#123; title = 'hello world', changeTitle &#125; = props;
  const handleChangeTitle = () => &#123;
    changeTitle('hello React')
  &#125;
  return (
    <div>
      &#123;title&#125;
      <button onClick=&#123;handleChangeTitle&#125;>改变标题</button>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import &#123; useState &#125; from 'react'
import HelloWorld from './HelloWorld.js'

export default function Index()&#123;
  const [info,setInfo] = useState('hello world');
  const handleChangeTitle = (data)=>&#123;
    setInfo(data);
  &#125;
  return (
    <HelloWorld title=&#123;info&#125; changeTitle=&#123;handleChangeTitle&#125;/>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在父组件中定义一个<code>info</code>数据传递给子组件的<code>title</code>参数数据，同时也定义了一个回调函数<code>handleChangeTitle</code>来改变<code>info</code>数据，并把回调函数也传递给子组件的<code>changeTitle</code>参数数据。</p>
<p>这样子组件的<code>changeTitle</code>参数数据可以作为一个函数来调用，调用<code>changeTitle</code>时相当调用<code>handleChangeTitle</code>回调函数，可以把要改变的值通过<code>data</code>函数参数传递出来，再执行<code>setInfo(data)</code>改变<code>info</code>数据，再传递给子组件的<code>title</code>参数数据，间接改变了<code>title</code>参数数据，实现了React中组件如何改变参数数据。</p>
<p>在父组件中也可以调用<code>setInfo</code>改变传递给子组件的<code>title</code>参数数据的<code>info</code>数据，以上就是React中父子组件通讯的一个方法。</p>
<h2 data-id="heading-17">9、React中如何监听组件数据的变化</h2>
<p>在Vue中可以用简单地用<code>watch</code>来监听数据的变化，而在React中比较复杂，子组件的类型不同实现方法也不同。</p>
<ul>
<li>类组件的写法：</li>
</ul>
<p>在类组件中用<code>componentDidUpdate</code>这个生命周期方法来实现，该方法首次渲染时<code>componentDidUpdate</code>不会执行，在后续props和state改变时会触发<code>componentDidUpdate</code>，其接受的第一个参数<code>prevProps</code>代表改变前的props，第二参数<code>prevState</code>代表改变前的state。</p>
<pre><code class="copyable">componentDidUpdate(prevProps, prevState)&#123;
  if(prevProps.title !== this.props.title)&#123;
     console.log('props中的title数据改变了');
  &#125;
  if(prevState.info !== this.state.info)&#123;
     console.log('state中的info数据改变了');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数组件的写法</li>
</ul>
<p>在函数组件中，可以<code>useEffect</code>这个React Hook监听数据的变化，但是无法像Vue的<code>watch</code>能够获取改变前的旧数据。所以要自定义一个Hook来实现类似Vue的<code>watch</code>的功能。自定义Hook是一个函数，其名称以 “use” 开头，函数内部可以调用其他的 Hook。故把这个自定义Hook称为<code>useWatch</code>。</p>
<p>如何获取改变前的旧数据，可以在第一次数据改变时触发<code>useWatch</code>时用一个容器把旧数据存储起来，下次再触发<code>useWatch</code>时通过读取容器中的值就可以获取改变前的旧数据。容器可以用<code>useRef</code>这个 Hook 来创建。</p>
<blockquote>
<p>useRef 返回一个可变的 ref 对象，其 .current 属性被初始化为传入的参数（initialValue）。返回的 ref 对象在组件的整个生命周期内保持不变。</p>
</blockquote>
<pre><code class="copyable">import &#123;useEffect,useRef&#125; from 'react';
export function useWatch(value,callback)&#123;
  const oldValue = useRef();
  useEffect(() =>&#123;
    callback(value,oldValue.current);
    oldValue.current=value;
  &#125;,[value])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是<code>useEffect</code>会在组件初次渲染后就会调用一次，导致<code>callback</code>回调函数会被执行一次，另外在Vue的<code>watch</code>是用<code>immediate</code>配置来控制在组件初次渲染后马上执行<code>callback</code>回调函数，且默认不会在组件初次渲染后执行<code>callback</code>回调函数，接着在<em>hook.js</em>中定义一个<code>useWatch</code>。</p>
<p>首先实现一下组件初次渲染不执行<code>callback</code>回调函数。</p>
<pre><code class="copyable">import &#123;useEffect,useRef&#125; from 'react';
export function useWatch(value,callback)&#123;
  const oldValue = useRef();
  const isInit = useRef(false);
  useEffect(() =>&#123;
    if(!isInit.current)&#123;
      isInit.current = true;
    &#125;else&#123;
      callback(value,oldValue.current);
    &#125;
    oldValue.current=value;
  &#125;,[value])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再添加<code>immediate</code>配置来控制在组件初次渲染后是否马上执行<code>callback</code>回调函数。</p>
<pre><code class="copyable">import &#123;useEffect,useRef&#125; from 'react';
export function useWatch(value,callback,config=&#123;immediate: false&#125;)&#123;
  const oldValue = useRef();
  const isInit = useRef(false);
  useEffect(() =>&#123;
    if(!isInit.current)&#123;
      isInit.current = true;
      if(config.immediate)&#123;
        callback(value,oldValue.current);
      &#125;
    &#125;else&#123;
      callback(value,oldValue.current);
    &#125;
    oldValue.current=value;
  &#125;,[value])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外Vue的<code>watch</code>还返回一个<code>unwatch</code>函数，调用<code>unwatch</code>函数可以停止监听该数据。</p>
<pre><code class="copyable">import &#123; useEffect, useRef &#125; from 'react';
export function useWatch(value, callback, config = &#123; immediate: false &#125;) &#123;
  const oldValue = useRef();
  const isInit = useRef(false);
  const isWatch = useRef(true);
  useEffect(() => &#123;
    if (isWatch.current) &#123;
      if (!isInit.current) &#123;
        isInit.current = true;
        if (config.immediate) &#123;
          callback(value, oldValue.current);
        &#125;
      &#125; else &#123;
        callback(value, oldValue.current);
      &#125;
      oldValue.current = value;
    &#125;
  &#125;, [value])

  const unwatch =  () => &#123;
    isWatch.current = false;
  &#125;;
  return unwatch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useWatch</code> 这个Hook 定义好后，这么使用。</p>
<pre><code class="copyable">export &#123;useState&#125; from 'react';
export &#123;useWatch&#125; from './hook.js';
export default function HelloWorld() &#123;
  const [title,setTitle] = useState('hello world')
  useWatch(title, (value, oldValue) => &#123;
    console.log(value);
    console.log(oldValue)
  &#125;)
  const handleChangeTitle = () => &#123;
    setTitle('hello React')
  &#125;
  return (
    <div onClick=&#123;handleChangeTitle&#125;>&#123;title&#125;</div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">10、React中父组件如何调用子组件的方法</h2>
<p>在Vue中是使用<code>ref</code>给子组件赋予一个标识 ID ，再使用<code>this.$refs[ID]</code>访问到这个子组件的实例对象，然后通过实例对象去调用子组件的方法。而在React中比较复杂，子组件的类型不同实现方法也不同。</p>
<ul>
<li>类子组件的写法：</li>
</ul>
<pre><code class="copyable">import React from 'react';
export default class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      title:'hello World'
    &#125;;
  &#125;
  handleChangeTitle()&#123;
    this.setState(&#123;
      title:'hello React'
    &#125;);
  &#125;
  render() &#123;
    return (
      <div>
        &#123;this.state.title&#125;
      </div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import React from 'react';
import HelloWorld from './HelloWorld.js';

class Index extends React.Component &#123;
  constructor(props) &#123;
    super(props)
    this.myCom = React.createRef();
    this.changeTitle = this.changeTitle.bind(this);
  &#125;
  changeTitle() &#123;
    this.myCom.current.handleChangeTitle();
  &#125;
  render() &#123;
    return (
      <div>
        <HelloWorld ref=&#123;this.myCom&#125; />
        <button onClick=&#123;this.changeTitle&#125;>改变标题</button>
      </div>
    )
  &#125;
&#125;
export default Index;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数组件的写法：</li>
</ul>
<p><code>useRef()</code>无法使用在函数组件上使用，在函数组件中要先使用 <code>useImperativeHandle</code> 定义要暴露给父组件的实例值，另外要把函数组件传入<code>forwardRef</code>处理后再导出。</p>
<pre><code class="copyable">import &#123; useState, forwardRef, useImperativeHandle &#125; from 'react';

const HelloWorld = (props, ref) => &#123;
  const [title, setTitle] = useState('hello World');
  useImperativeHandle(ref, () => (&#123;
    handleChangeTitle: () => &#123;
      setTitle('hello React')
    &#125;,
  &#125;));
  return (
    <div>&#123;title&#125;</div>
  );
&#125;
export default forwardRef(HelloWorld)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import &#123; useRef &#125; from 'react'
import HelloWorld from './HelloWorld.js'

export default function Index() &#123;
  const myCom = useRef();
  const changeTitle = () => &#123;
    myCom.current.handleChangeTitle();
  &#125;
  return (
    <div>
      <HelloWorld ref=&#123;myCom&#125; />
      <button onClick=&#123;changeTitle&#125;>改变标题</button>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">11、React中组件插槽怎么实现</h2>
<h3 data-id="heading-20">11.1 普通插槽</h3>
<p>其实React中是没有插槽的概念，不过可以用<code>props.children</code>来实现插槽的功能。</p>
<blockquote>
<p>每个组件都可以获取到 props.children。它包含组件的开始标签和结束标签之间的内容。</p>
</blockquote>
<p>例如开发一个 HelloWorld 组件用来展示 “ hello World ” ，也可以用插槽的形式来实现，通过<code>props.children</code>把 “ hello World ” 从父组件传递进去。</p>
<p>类组件的写法：</p>
<pre><code class="copyable">import React from 'react';
export default class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
  &#125;
  render() &#123;
    return (
      <div>
        &#123;this.props.children&#125;
      </div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import React from 'react';
import HelloWorld from './HelloWorld.js';
class Index extends React.Component&#123;
  constructor(props) &#123;
    super(props);
  &#125;
  render() &#123;
    return (
      <HelloWorld>hello World</HelloWorld>
    )
  &#125;
&#125;
export default Index;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件的写法：</p>
<pre><code class="copyable">export default function HelloWorld(props)&#123;
  const &#123;children&#125;=props;
  return (
    <div>
      &#123;children&#125;
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import HelloWorld from './HelloWorld.js';
export default function Index()&#123;
  return (
    <HelloWorld>hello World</HelloWorld>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">11.2 具名插槽</h3>
<p>可以通过props给子组件传递一个函数，如果这个函数最后返回React元素，其React元素是用JSX语法编写的，这样就间接实现具名插槽的功能。</p>
<p>例如开发一个 HelloWorld 组件用来展示 “ hello World ” ，用具名插槽的形式来实现。</p>
<p>类组件的写法：</p>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.Component&#123;
  constructor(props)&#123;
    super(props)
    this.elementSlot = "";
    if (this.props.element) &#123;
      this.elementSlot = this.props.element();
    &#125;
  &#125;
  render()&#123;
    return (
      <div>
        &#123;this.elementSlot&#125;
      </div>
    );
  &#125;
&#125;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import React from 'react';
import HelloWorld from './HelloWorld.js';
class Index extends React.Component&#123;
  constructor(props) &#123;
    super(props);
  &#125;
  info()&#123;
    return(
      <span>hello World</span>
    )
  &#125;
  render() &#123;
    return (
      <HelloWorld element=&#123;this.info&#125;></HelloWorld>
    )
  &#125;
&#125;
export default Index;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件的写法：</p>
<pre><code class="copyable">export default function HelloWorld(props) &#123;
  const &#123; children, element &#125; = props;
  let elementSlot = "";
  if (element) &#123;
    elementSlot = element();
  &#125;
  return (
    <div>
      &#123;elementSlot&#125;
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import HelloWorld from './HelloWorld.js';

export default function Index()&#123;
  const info = () =>&#123;
    return (
      <span>hello World</span>
    )
  &#125;
  return (
    <HelloWorld element=&#123;info&#125;></HelloWorld>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">11.3 作用域插槽</h3>
<p>Vue的作用域插槽的作用是用子组件中的数据在父组件中写插槽内容。</p>
<p>回顾上面具名插槽的实现过程，先在父组件中定义一个函数，该函数能返回一个React元素，再通过props把该函数传递给子组件，在子组件中执行该函数，把执行结果添加到子组件的React元素中。</p>
<p>如果在子组件中执行该函数时，把子组件的数据当作参数传递进去，那么在父组件中就可以用该函数接收子组件的数据来写React元素（插槽的内容）。这样就实现了作用域插槽。</p>
<p>例如开发一个 HelloWorld 组件用来展示 “ 用子组件的数据写具名插槽 hello World ” ，用作用域插槽的形式来实现。</p>
<p>类组件的写法：</p>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.Component&#123;
  constructor(props)&#123;
    super(props)
    this.state = &#123;
      info:'用子组件的数据写具名插槽 hello World'
    &#125;
    this.elementSlot = "";
    if (this.props.element) &#123;
      this.elementSlot = this.props.element(this.state.info);
    &#125;
  &#125;
  render()&#123;
    return (
      <div>
        &#123;this.elementSlot&#125;
      </div>
    );
  &#125;
&#125;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import React from 'react';
import HelloWorld from './HelloWorld.js';
class Index extends React.Component&#123;
  constructor(props) &#123;
    super(props);
  &#125;
  info(data)&#123;
    return(
      <span>&#123;data&#125;</span>
    )
  &#125;
  render() &#123;
    return (
      <HelloWorld element=&#123;this.info&#125;>
      </HelloWorld>
    )
  &#125;
&#125;
export default Index;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件的写法</p>
<pre><code class="copyable">import &#123; useState &#125; from "react";

export default function HelloWorld(props) &#123;
  const &#123; children, element &#125; = props;
  const [info] = useState('用子组件的数据写具名插槽 hello World')
  let elementSlot = "";
  if (element) &#123;
    elementSlot = element(info);
  &#125;
  return (
    <div>
      &#123;elementSlot&#125;
      &#123;children&#125;
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import HelloWorld from './HelloWorld.js';

export default function Index()&#123;
  const info = (data) =>&#123;
    return (
      <span>&#123;data&#125;</span>
    )
  &#125;
  return (
    <HelloWorld element=&#123;info&#125;></HelloWorld>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">小结</h2>
<p>以上从Vue开发一个组件会用到的技术，在React中寻找对应的实现方案的角度来入门React，读完你应该会用React开发一些简单的页面，并能把页面分割成一个个组件，并在组件之间进行数据交互。下一篇文章将介绍开发组件时在Vue中那些常用的指令在React中是如何实现的。</p></div>  
</div>
            