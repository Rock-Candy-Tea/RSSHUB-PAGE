
---
title: 'React学习笔记(二)'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 18:31:18 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>类组件生命周期钩子函数</p>
<p>constructor(props)</p>
<p>类组件的构造函数，是第一步执行的，这里可以进行state的初始化以及对事件绑定this</p>
<pre><code class="copyable">constructor(props) &#123;
    super(props)
    this.state = &#123;
      name: 'tom'
    &#125;
    this.eventHandler = this.eventHandler.bind(this)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>getDerivedStateFromProps(props, state)</p>
<p>会在 render 方法之前调用，无论是挂载阶段还是更新阶段，它的存在只有一个目的：让组件在 props 变化时更新 state</p>
<pre><code class="copyable">static getDerivedStateFromProps(props, state) &#123;
    console.log('这里可以获得变化后的props')
    console.log('首次渲染 和 props 变化时就会触发')
    return state
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>shouldComponentUpdate(nextProps, nextState)</p>
<p>只在更新阶段，首次渲染不会调用，render之前调用，函数返回一共布尔值，决定是否继续进行render</p>
<pre><code class="copyable">shouldComponentUpdate(nextProps, nextState) &#123;
    console.log('如果返回false 就不会进行render更新')
    return true
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>render()</p>
<p>组件生命周期渲染阶段执行的函数，返回值为组件要渲染VirtualDOM</p>
<pre><code class="copyable">render() &#123;
    return (
        <div>hello</div>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>getSnapshotBeforeUpdate(prevProps, prevState)</p>
<p>在 render() 之后，但是在输出到 DOM 之前执行，用来获取渲染之前的快照。当我们想在当前一次更新前获取上次的 DOM 状态，可以在这里进行处理，返回值可以在 componentDidUpdate 方法中的第三个参数中获取，就是说在组件更新之后可以拿到这个值再去做其他事情。</p>
<pre><code class="copyable">getSnapshotBeforeUpdate(prevProps, prevState) &#123;
    console.log('getSnapshotBeforeUpdate render之后 dom更新之前')
    console.log('可以在这里获取到更新前的dom 这个钩子不常用')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>componentDidUpdate()</p>
<p>会在 DOM 更新后立即调用，首次渲染不会调用该方法。我们可以在这个函数中对渲染后的 DOM 进行操作</p>
<pre><code class="copyable">componentDidUpdate() &#123;
    console.log('componentDidUpdate DOM 更新后执行 首次渲染不会执行')
    console.log('这里可以获取到更新后的DOM')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>componentDidMount()</p>
<p>在组件挂载后调用</p>
<pre><code class="copyable">componentDidMount() &#123;
    console.log('组件第一次挂载后')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>componentWillUnmount()</p>
<p>会在组件卸载及销毁前调用，我们可以在这里做一些清理工作，如：组件内的定时器、未完成的请求等</p>
<pre><code class="copyable">componentWillUnmount() &#123;
    console.log('组件销毁前')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>受控表单、非受控表单</p>
<p>根据表单和state数据的状态关联关系，分为受控组件和非受控组件</p>
<ul>
<li>
<p>受控表单 ：表单控件中的值由组件的 state 对象来管理，state对象中存储的值和表单控件中的值时同步状态的</p>
</li>
<li>
<p>非受控表单：表单元素的值由 DOM 元素本身管理</p>
</li>
</ul>
<p>受控表单类似于Vue的双向绑定</p>
<p>双向数据绑定是指，组件类中更新了状态，DOM 状态同步更新，DOM 更改了状态，组件类中同步更新。组件 <=> 视图。</p>
<p>要实现双向数据绑定需要用到表单元素和 state 状态对象。</p>
<p>受控表单</p>
<p>表单控件中的值由组件的 state 对象来管理，state对象中存储的值和表单控件中的值时同步状态的，当表单变化时state状态也会同步变化。</p>
<pre><code class="copyable">class App extends Component &#123;
  constructor () &#123;
    this.state = &#123; username: "" &#125;
    this.nameChanged = this.nameChanged.bind(this)
  &#125;
  
  nameChanged (e) &#123;
    this.setState(&#123;username: e.target.value&#125;)
  &#125;
  render() &#123;
    return (
      <form>
        <p>&#123;this.state.username&#125;</p>
        &#123;/*  */&#125;
        <input type="text" value=&#123;this.state.username&#125; onChange=&#123;this.nameChanged&#125;/>
      </form>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非受控表单</p>
<p>表单元素的值由 DOM 元素本身管理。</p>
<pre><code class="copyable">class App extends Component &#123;
  constructor () &#123;
    this.onSubmit = this.onSubmit.bind(this)
  &#125;
  onSubmit(e) &#123;
    console.log(this.username.value)
    e.preventDefault();
  &#125;
  render(
    <form onSubmit=&#123;this.onSubmit&#125;>
      <input type="text" ref=&#123;username => this.username = username&#125;/>
    </form>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取组件实例</p>
<p>通过ref和createRef()可以获取到组件实例，可以用来获取标签DOM</p>
<pre><code class="copyable">class Input extends Component &#123;
  constructor() &#123;
    super()
    this.inputRef = React.createRef()
  &#125;
  render() &#123;
    return (
      <div>
        <input type="text" ref=&#123;this.inputRef&#125; />
        <button onClick=&#123;() => console.log(this.inputRef.current)&#125;> button </button>
      </div>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路由</p>
<p>依赖 <code>cnpm install react-router-dom</code></p>
<p>必须引入路径组件(BrowserRouter或者HashRouter)，使用BrowserRouter或者HashRouter包括起全部内容</p>
<p>这两个组件在开发环境中没有任何区别，在生产环境中的区别是hash在路径上会有一个#号，而browser没有</p>
<pre><code class="copyable">import React from 'react';
import &#123; BrowserRouter, Route, Link &#125; from 'react-router-dom';
function Index() &#123;
 return <div>首页</div>;
&#125;
function News() &#123;
 return <div>新闻</div>;
&#125;
function App() &#123;
  return (
    <BrowerRouter>
      <div>
        <Link to="/index">首页</Link>
        <Link to="/news">新闻</Link>
      </div>
      <div>
        <Route path="/index" component=&#123;Index&#125;/>
        <Route path="/news" component=&#123;News&#125;/>
      </div>
    </BrowerRouter>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路由嵌套</p>
<p>子路由组件通过<code>props.match.path</code>获取到父级路由组件的路径</p>
<pre><code class="copyable">function News(props) &#123;
  return (
    <div>
      <div>
        <Link to=&#123;`$&#123;props.match.url&#125;/company`&#125;>公司新闻</Link>
        <Link to=&#123;`$&#123;props.match.url&#125;/industry`&#125;>行业新闻</Link>
      </div>
      <div>
        <Route path=&#123;`$&#123;props.match.path&#125;/company`&#125; component=&#123;CompanyNews&#125; />
        <Route path=&#123;`$&#123;props.match.path&#125;/industry`&#125; component=&#123;IndustryNews&#125;/>  
      </div> 
    </div>
  );
&#125;

function CompanyNews() &#123;
 return <div>公司新闻</div>
&#125;
function IndustryNews() &#123;
 return <div>行业新闻</div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路由传参</p>
<pre><code class="copyable">&#123;/* 父级路由组件 */&#125;
<Link to=&#123;`/detail?id=$&#123;item.id&#125;`&#125;>&#123;item.title&#125;</Link>
&#123;/* 子路由组件 */&#125;
import url from 'url'
class Detail extends Component &#123;
  constructor(props) &#123;
    super(props);
    const &#123; query &#125; = url.parse(this.props.location.search, true);
    console.log(this.props.location.serach); // ?id=1
    console.log(query); // &#123;id: 1&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路由重定向</p>
<p>用Redirect组件</p>
<pre><code class="copyable">import &#123; Redirect &#125; from 'react-router-dom';

class Login extends Component &#123;
  render() &#123;
    if (this.state.isLogin) &#123;
      return <Redirect to="/"/>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exact</p>
<p>exact 属性表示路由使用 精确匹配模式，非 exact 模式下 '/' 匹配所有以 '/' 开头的路由</p>
<p>如果不使用exact，/about 会匹配到 index和about两个组件都会显示了</p>
<pre><code class="copyable"><Route path="/" exact component=&#123;IndexPage&#125; />
<Route path="/about" exact component=&#123;AboutPage&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Link组件</p>
<p>Link 组件用来处理 a 链接 类似的功能（它会在页面中生成一个 a 标签），但设置这里需要注意的，react-router-dom 拦截了实际 a 标签的默认动作，然后根据所有使用的路由模式（Hash 或者 HTML5）来进行处理，改变了 URL，但不会发生请求，同时根据 Route 中的设置把对应的组件显示在指定的位置 </p>
<p> to 属性类似 a 标签中的 href</p>
<p>NavLink</p>
<p>NavLink 与 Link 类似，但是它提供了两个特殊属性用来处理页面导航</p>
<h3 data-id="heading-0">activeStyle</h3>
<p>当前 URL 与 NavLink 中的 to 匹配的时候，激活 activeStyle 中的样式<code>也就是说被选中的时候</code></p>
<h3 data-id="heading-1">activeClassName</h3>
<p>与 activeStyle 类似，但是激活的是 className</p>
<pre><code class="copyable"><NavLink to="/" exact
  activeStyle=&#123;&#123;
     color: 'red'
  &#125;&#125;
>首页</NavLink>

<NavLink to="/about" exact
  activeClassName="active-class"
>关于</NavLink>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            