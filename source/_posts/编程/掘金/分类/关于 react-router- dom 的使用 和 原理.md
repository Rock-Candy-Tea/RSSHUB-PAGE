
---
title: '关于 react-router- dom 的使用 和 原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3588'
author: 掘金
comments: false
date: Sat, 15 May 2021 09:02:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=3588'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">react-router</h1>
<h4 data-id="heading-1">使用</h4>
<p>1、 安装</p>
<pre><code class="copyable">npm i react-router-dom
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;
  HashRouter,
  BrowserRouter,
  Route,
  Link,
  Switch,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用最大的  HashRouter / BrowserRouter 来包裹组件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">'/list'</span>></span>显示列表<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">'/Clock'</span>></span>显示时间<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        &#123;/* exact 精准匹配 */&#125;
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/list'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;List&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/ContextTest'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;ContextTest&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/Clock'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Clock&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/reducer'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Reducer&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/reftest'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;RefTest&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/redux'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Redux&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/reactredux'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;ReactReduxPage&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
         <span class="hljs-tag"></<span class="hljs-name">div</span>></span>


<span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用switch组件的时候就会从上到下找到合适的组件  叫独占路由</p>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/list'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;List&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/ContextTest'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;ContextTest&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/Clock'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Clock&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/reducer'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Reducer&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不写 path 就是匹配任意值</p>
<p>子路由的渲染优先级是  children > component >　render</p>
<h2 data-id="heading-2">Redirect</h2>
<p>要重定向到的位置，其中 pathname 可以是 path-to-regexp 能够理解的任何有效的 URL 路径。</p>
<pre><code class="copyable"><Redirect 
    path=&#123;'/'&#125; 
    to=&#123;&#123; pathname: '/login', search: '?utm=your+face', state: &#123; referrer: currentLocation &#125;&#125;&#125; 
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中的 state 对象可以在重定向到的组件中通过 this.props.location.state 进⾏访问。⽽ referrer</p>
<p>键（不是特殊名称）将通过路径名 /login 指向的登录组件中的 this.props.location.state.referrer 进⾏访问。</p>
<p><br><br><br><br></p>
<h1 data-id="heading-3">实现  react-router</h1>
<p>暂定 实现一下组件</p>
<pre><code class="copyable">import &#123; Route, Link, Switch, BrowserRouter &#125; from '../react-router/index'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道 react 路由有 hashRouter、browerRouter、memoryRouter</p>
<p>这几个router的作用是传递不同的 historyApi 给 子组件去使用， 将三者api封装成统一的api</p>
<p><br><br><br><br></p>
<h4 data-id="heading-4">1、关于 BrowserRouter</h4>
<p>传递了 history 的 api给下层</p>
<pre><code class="copyable">export class BrowserRouter extends Component &#123;
  constructor(props) &#123;
    super(props)
    this.history = history.createBrowserHistory()
  &#125;

  render() &#123;
    return (
      <Router children=&#123;this.props.children&#125; history=&#123;this.history&#125;></Router>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br><br><br></p>
<h2 data-id="heading-5">2、 关于 Router</h2>
<p>这层组件 承接了 不同 路由方式的api的 中间层， 上层传递了history 的统一api 给这层使用</p>
<p>作用：</p>
<ol>
<li>监听路由变化 ，若路由发生改变，则重新渲染当前组件</li>
<li>通过 createContext 把 history api 传递给 子组件</li>
<li>把 location 也传给子组件</li>
<li>传递一个默认path 表示 根路径匹配</li>
</ol>
<pre><code class="copyable">import RouterContext from './context'

export class Router extends Component &#123;
  // 静态方法  传递一个默认path 表示 根路径
  static computeRootMatch(pathname) &#123;
    return &#123; path: '/', url: '/', params: &#123;&#125;, isExact: pathname === '/' &#125;
  &#125;

  constructor(props) &#123;
    super(props)
    this.state = &#123;
      location: props.history.location,
    &#125;
    // 提供监听
    this.unlisten = props.history.listen((obj) => &#123;
      this.setState(&#123; location: obj.location &#125;)
    &#125;)
  &#125;
  componentWillUnmount() &#123;
    this.unlisten() // 执行取消监听
  &#125;
  render() &#123;
    const &#123; children, history &#125; = this.props
    // 提供history跳转 ，和 location 的参数
    return (
      <RouterContext.Provider
        value=&#123;&#123;
          history,
          location: this.state.location,
          match: Router.computeRootMatch(this.state.location.pathname),
        &#125;&#125;
      >
        &#123;children&#125;
      </RouterContext.Provider>
    )
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们输出 History 看看</p>
<p>history 包含了以下方法</p>
<p>比如我们常使用 的 go、push、replace、back</p>
<pre><code class="copyable">action: (...)
back: ƒ ()
block: ƒ (a)
createHref: ƒ g(a)
forward: ƒ ()
go: ƒ r(a)
listen: ƒ (a)
location: Object
push: ƒ w(a, d)
replace: ƒ u(a, d)
get action: ƒ action()
get location: ƒ location()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">hash: ""
key: "h7fgir2z"
pathname: "/ContextTest"
search: "?fuck=true"
state: null
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br><br><br></p>
<h2 data-id="heading-6">3、 实现 Link</h2>
<p>其 只提供的 a 标签支持跳转，需屏蔽默认事件</p>
<p>history api 通过 useContext(RouterContext) 获取</p>
<pre><code class="copyable">// 组件 link

export function Link(&#123; children, to, ...restProps &#125;) &#123;
  const &#123; history &#125; = useContext(RouterContext)
  const handleClick = (e) => &#123;
    // 页面跳转
    e.preventDefault()
    history.push(to)
  &#125;

  return (
    <a href=&#123;''&#125; to=&#123;to&#125; onClick=&#123;handleClick&#125;>
      &#123;children&#125;
    </a>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br><br><br></p>
<h2 data-id="heading-7">4、Route</h2>
<p>1、 作用是显示 匹配路由的 children</p>
<p>2、 如果有个switch的组件，那computedMatch就会有值</p>
<p>3、 取值优先级 computedMatch > matchPath(location.pathname, this.props) > context.match
分别就是 取 switch组件给的匹配结果 =>  自己的匹配结果 => 根目录结果</p>
<p>4、children > component > render 除此之外children如果是个函数那么必渲染（上层有switch组件除外）</p>
<p>5、 通过测试发现 switch 组件会改变 它的children，只会渲染匹配的，没有使用switch组件时，所有 Route 都会渲染，只是渲染结果可能为null。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">import</span> matchPath <span class="hljs-keyword">from</span> <span class="hljs-string">'./matchPath'</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Route</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Consumer</span>></span>
        &#123;(context) => &#123;
          const &#123; location &#125; = context
          const &#123; children, component, render, path, computedMatch &#125; = this.props

          // 表示匹配的 结果
          const match = computedMatch 
            ? computedMatch
            : path
            ? matchPath(location.pathname, this.props)
            : context.match

          // 这里取值的优先顺序是
          
          // computedMatch > matchPath(location.pathname, this.props) > 默认的 match

          // console.log('match:', match)
          
          const props = &#123; ...context, match &#125;

          // 匹配 children,component，render null
          // 不匹配

          return match
            ? children // 1
              ? typeof children === 'function' // 2
                ? children(props)
                : children
              : component // 3
              ? React.createElement(component, props)
              : render // 4
              ? render()
              : null
            : typeof children === 'function' // 1
            ? children()
            : null
        &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">RouterContext.Consumer</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br><br><br></p>
<h2 data-id="heading-8">Switch 组件</h2>
<p>找出 匹配的组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Switch</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Consumer</span>></span>
        &#123;(context) => &#123;
          let match;
          let element;

          const &#123; location &#125; = context
          
          React.Children.forEach(this.props.children, (child) => &#123;
            if (match == null && React.isValidElement(child)) &#123;
              element = child
              match = matchPath(location.pathname, child.props) // 匹配出来的
            &#125;
          &#125;)

          return match
            ? React.cloneElement(element, &#123; computedMatch: match &#125;)
            : null
        &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">RouterContext.Consumer</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br><br><br></p>
<h2 data-id="heading-9">Redirect 组件</h2>
<p>该组件得和 Route 同级，得有 path 和 to 属性 ，path是为了 给 switch 去和 location.pathname，否则无论如何都会渲染</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Redirect</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Consumer</span>></span>
        &#123;(context) => &#123;
          const &#123; history &#125; = context
          const &#123; to, push = false &#125; = this.props
          return (
            <span class="hljs-tag"><<span class="hljs-name">LifeCycle</span>
              <span class="hljs-attr">onMount</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
                push ? history.push(to) : history.replace(to)
              &#125;&#125;
            ><span class="hljs-tag"></<span class="hljs-name">LifeCycle</span>></span>
          )
        &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">RouterContext.Consumer</span>></span></span>
    )
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LifeCycle</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.onMount) &#123;
      <span class="hljs-built_in">this</span>.props.onMount.call(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>)
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br><br><br></p>
<h2 data-id="heading-10">关于 withRouter</h2>
<p>该方法是一个高阶组件的用法</p>
<p>需在Route 组件包一层 修改下match的值， 通过 provider</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 高阶组件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> withRouter = <span class="hljs-function">(<span class="hljs-params">WrappedComponent</span>) =></span> <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Consumer</span>></span>
      &#123;(context) => &#123;
        return <span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> &#123;<span class="hljs-attr">...props</span>&#125; &#123;<span class="hljs-attr">...context</span>&#125; /></span>
      &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">RouterContext.Consumer</span>></span></span>
  )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br><br><br></p>
<h2 data-id="heading-11">Prompt 实现</h2>
<p>阻碍的原理是 调用 history.block(message)</p></div>  
</div>
            