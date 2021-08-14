
---
title: '从Vue2.0到React17——React路由入门(二)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/582e9d4a6f7c40159ca5597c452dd270~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 14:41:50 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/582e9d4a6f7c40159ca5597c452dd270~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“<strong>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<h2 data-id="heading-0">前言</h2>
<p>React作为一个MVVM框架，路由功能是必不可少的，回顾我们在使用Vue Router的过程中，最常用的一些功能是<strong>路由页面的渲染</strong>，<strong>路由页面内容的添加</strong>，<strong>路由地址的配置</strong>，<strong>路由跳转</strong>，<strong>路由传参</strong>、<strong>嵌套路由</strong>等等，本文将去React Router中寻找这些常用功能的是如何实现的，来带你入门 <strong>React Router5.0</strong>。</p>
<p>在上篇文章中介绍了路由页面如何渲染 、路由页面内容如何设置、如何设置路由地址，本文将继续介绍路由如何跳转、如何接收路由的传参、路由懒加载。</p>
<h2 data-id="heading-1">一、路由如何跳转</h2>
<p>在Vue Router中有两种方式进行路由跳转，一种是声明式，一种是编程式。</p>













<table><thead><tr><th>声明式</th><th>编程式</th></tr></thead><tbody><tr><td><code><router-link :to="..."></code></td><td><code>router.push(...)</code></td></tr></tbody></table>
<p>那React Router中是否也有声明式和编程式的路由跳转？举一个例子来介绍，例如：实现一个点击第一个页面跳转到第二个页面，点击第二个页面跳转到第一个页面。</p>
<h3 data-id="heading-2">1.1 声明式路由跳转</h3>
<p>使用 Link 组件来实现跳转，其属性<code>to</code>可设置要跳转的路由地址，<strong>切记 Link 组件必须在 Route 组件内使用</strong>。</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';
import &#123; BrowserRouter, Route ,Link&#125; from "react-router-dom";
ReactDOM.render(
  <div>
    <BrowserRouter>
      <Route
        path="/one"
        render=&#123;() => &#123;
          return (
            <div><Link to="/two">去第二个页面</Link></div>
          )
        &#125;&#125;
      >
      </Route>
      <Route
        path="/two"
        render=&#123;() => &#123;
          return (
            <div><Link to="/one">去第一个页面</Link></div>
          )
        &#125;&#125;
      ></Route>
    </BrowserRouter>
  </div>,
  document.getElementById('root')
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.2 编程式路由跳转</h3>
<p>在类组件和函数组件中的用法是不同的，分别来介绍。</p>
<h4 data-id="heading-4">1.2.1 函数组件中的编程式路由跳转</h4>
<p>执行<code>useHistory()</code> Hook 来获取<code>history</code>，然后调用<code>history.push(path)</code>进行路由跳转。</p>
<h4 data-id="heading-5">1.2.2 类组件中的编程式路由跳转</h4>
<p>在类组件中通过<code>props</code>获取到<code>history</code>，然后调用<code>history.push(path)</code>进行路由跳转。</p>
<p>具体实现看下面demo。</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';
import &#123;
  BrowserRouter,
  Route,
  useHistory
&#125; from "react-router-dom";
class OnePage extends React.Component &#123;
  constructor(props) &#123;
    super(props)
    const &#123; history &#125; = this.props;
    this.history = history;
    this.jump = this.jump.bind(this)
  &#125;
  jump = () => &#123;
    this.history.push('/two')
  &#125;
  render() &#123;
    return (
      <div>
        <div onClick=&#123;this.jump&#125;>去第二个页面</div>
      </div>
    )
  &#125;
&#125;
const TwoPage = () => &#123;
  const history = useHistory();
  const handleClick = () => &#123;
    history.push("/one");
  &#125;
  return (
    <div onClick=&#123;handleClick&#125;>去第一个页面</div>
  )
&#125;
ReactDOM.render(
  <div>
    <BrowserRouter>
      <Route
        path="/one"
        component=&#123;OnePage&#125;
      >
      </Route>
      <Route
        path="/two"
        component=&#123;TwoPage&#125;
      ></Route>
    </BrowserRouter>
  </div>,
  document.getElementById('root')
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">二、如何接收路由的传参</h2>
<p>在类组件和函数组件中的接收路由参数的做法是不同的，要分别来介绍。另外每一种接收路由的传参都对应着一种传递路由参数的方法，且在类组件和函数组件中是一致的，会穿插在每种接收路由的传参的方法中介绍。</p>
<h3 data-id="heading-7">2.1 在函数组件中接收路由传参</h3>
<p>在函数组件中有三个Hook（<code>useLocation</code>、<code>useParams</code>、<code>useRouteMatch</code>）可以接收路由参数，下面来详细介绍各自的使用方法。</p>
<h4 data-id="heading-8">2.1.1 useLocation</h4>
<pre><code class="copyable">const location = useLocation();
console.log(location)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先在函数组件中执行useLocation，并将结果打印出来，看一下结果，如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/582e9d4a6f7c40159ca5597c452dd270~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要关注结果中的<code>search</code>和<code>state</code>这个两个属性，这两个属性是用来接收路由的传参。</p>
<p>那要怎么传参，才能用useLocation返回的对象中的<code>search</code>和<code>state</code>接收到路由的传参。在上一小节可知路由的跳转有两种，一种是声明式，一种是编程式。</p>
<p><code>search</code>接收跳转地址的请求参数，如：<code>/one?id=1</code>时，<code>search</code>为<code>?id=1</code>，可以在声明式跳转中这样传参。</p>
<p><code>state</code>接收<code>history.push</code>中的第二参数作为传参，如：<code>history.push('/one',&#123;name:'第一个页面'&#125;)</code>，一般在编程式跳转中这样传参。</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';
import &#123;
  BrowserRouter, 
  Route,
  Link,
  useLocation,
  useHistory
&#125; from "react-router-dom";
const OnePage = () =>&#123;
  const location = useLocation();
  console.log('第一个页面',location)
  return (
    <div><Link to="/two?id=2">去第二个页面</Link></div>
  )
&#125;
const TwoPage= () =>&#123;
  const location = useLocation();
  console.log('第二个页面',location)
  const history = useHistory();
  const toOnePage = () =>&#123;
    history.push('/one',&#123;name:'第一个页面'&#125;)
  &#125;
  return (
    <div onClick=&#123;toOnePage&#125;>去第一个页面</div>
  )
&#125;
ReactDOM.render(
  <div>
    <BrowserRouter>
      <Route
        path="/one"
        component=&#123;OnePage&#125;
      >
      </Route>
      <Route
        path="/two"
        component=&#123;TwoPage&#125;
      ></Route>
    </BrowserRouter>
  </div>,
  document.getElementById('root')
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 OnePage 和 TwoPage 两个组件中的执行<code>useLocation()</code>的结果都打印出来，如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eea15086c7614827b257cb69b0d0c71f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当使用<code>history.push('/one',&#123;name:'第一个页面'&#125;)</code>跳转到第一个页面时，<code>useLocation()</code>的结果中的<code>state</code>的值为<code>&#123;name: "第一个页面"&#125;</code>。</p>
<p>当使用<code><Link to="/two?id=2">去第二个页面</Link></code>跳转到第二个页面时，<code>useLocation()</code>的结果中的<code>search</code>的值为<code>"?id=2"</code>。</p>
<h4 data-id="heading-9">2.1.2 useParams</h4>
<p><code>useParams</code>接收跳转地址的路径参数，如<code>/one/1</code>，其中<code>1</code>就是路径参数。</p>
<p>要先用特定的写法给 Route 组件的<code>path</code>属性添加路径，才能用<code>useParams</code>接收到路径参数。</p>
<p>例如<code>path</code>设置为<code>/one/:id/:num</code>，若路由跳转地址为<code>/one/2/3/4</code>，那么用<code>useParams</code>接收的值为<code>&#123;id:2,num:3&#125;</code>。</p>
<p>下面用一个例子具体演示一下，还是点击第一个页面跳转第二页面，点击第二个页面跳转第一页面，注意观察各自 Route 组件的<code>path</code>属性值、路由跳转地址和各自组件内执行<code>useParams()</code>的结果。</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';
import &#123; BrowserRouter,
  Route,
  Link,
  useHistory,
  useParams
&#125; from "react-router-dom";
const OnePage = () =>&#123;
  const params = useParams();
  console.log('第一个页面',params);
  return (
    <div><Link to="/two/2/3">去第二个页面</Link></div>
  )
&#125;
const TwoPage= () =>&#123;
  const params = useParams();
  console.log('第二个页面',params);
  const history = useHistory();
  const toOnePage = () =>&#123;
    history.push('/one/1/3')
  &#125;
  return (
    <div onClick=&#123;toOnePage&#125;>去第一个页面</div>
  )
&#125;
ReactDOM.render(
  <div>
    <BrowserRouter>
      <Route
        path="/one/:id/:num"
        component=&#123;OnePage&#125;
      >
    </Route>
      <Route
        path="/two/:id"
        component=&#123;TwoPage&#125;
      ></Route>
    </BrowserRouter>
  </div>,
  document.getElementById('root')
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将上面demo中各自组件内执行<code>useParams()</code>的结果打印出来，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/200b83cd024646ba910cbfbede534380~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>此外要特别注意，若给一个 Route 组件设置的<code>path</code>带路径参数的变量，设置几个，访问这个 Route 组件的URL也要有几个路径参数，否是访问不了。</strong></p>
<h4 data-id="heading-10">2.1.3 useRouteMatch</h4>
<p>执行<code>useRouteMatch()</code>可得到当前路由页面的路由数据。数据中有个<code>params</code>的字段，其值和执行<code>useParams()</code>得到数据一样。</p>
<p>所以使用<code>useRouteMatch</code>获取路由参数，也要先用特定的写法给 Route 组件的<code>path</code>属性添加路径，才能用<code>useRouteMatch</code>接收到路径参数。</p>
<p>例如将渲染“第一页面”的 Route 组件的<code>path</code>设置为<code>/one/:id/:num</code>，若路由跳转地址为<code>/one/2/3/4</code>，那么在“第一页面”路由页面组件中执行<code>useRouteMatch()</code>，</p>
<pre><code class="copyable">import &#123;
  useRouteMatch
&#125; from "react-router-dom";
const OnePage = () =>&#123;
  const match = useRouteMatch();
  console.log(match);
  return (
    <div>第一个页面</div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可得到当前路由页面的路由数据<code>match</code>如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71697d28ddf2461da24331ba77564aac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中红框部分就是路由参数，是不是和执行<code>useParams()</code>得到数据一样?</p>
<h3 data-id="heading-11">2.2 在类组件中接收路由传参</h3>
<p>在类组件中通过<code>props</code>获取到<code>location</code>和<code>match</code>，然后在其中获取到路由参数<code>search</code>（请求参数）、<code>params</code>（路径参数）和<code>state</code>。</p>
<p>在“第一页面”这个路由页面组件中把<code>props</code>打印出来。</p>
<pre><code class="copyable">class OnePage extends React.Component &#123;
  constructor(props) &#123;
    super(props)
    console.log(this.props)
  &#125;
  render() &#123;
    return (
      <div>
        <div>第一个页面</div>
      </div>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50d80393afd14b98b7e7740087751857~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于路由参数<code>search</code>（请求参数）、<code>params</code>（路径参数）和<code>state</code>如何传递已经在上小节【在函数组件中接收路由传参】中介绍过了。</p>
<h2 data-id="heading-12">三、路由懒加载</h2>
<p>使用<code>React.lazy</code>定义一个动态加载的组件，来实现路由懒加载。</p>
<blockquote>
<p>注意：<code>React.lazy</code>定义的组件必须被包裹在<code><React.Suspense></React.Suspense></code>中使用，且<code>React.Suspense</code>的属性<code>fallback</code>为必填属性。</p>
</blockquote>
<p>例如把OnePage这个路由页面组件进行懒加载，实现代码如下所示：</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';
import &#123;
  BrowserRouter,
  Route,
&#125; from "react-router-dom";
const OnePage = React.lazy(() => import('./OnePage'));
const Spinner = () => &#123;
  return (
    <div>加载中……</div>
  )
&#125;
ReactDOM.render(
  <div>
    <React.Suspense fallback=&#123;<Spinner/>&#125;>
      <BrowserRouter>
        <Route
          path="/"
          component=&#123;OnePage&#125;
        >
        </Route>
      </BrowserRouter>
    </React.Suspense>
  </div>,
  document.getElementById('root')
);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            