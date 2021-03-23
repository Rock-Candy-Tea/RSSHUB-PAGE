
---
title: 'React学习笔记(一)'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 18:31:02 GMT
thumbnail: '&#123;user.avatarUrl&#125;'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">React和JSX语法</h2>
<p>在 React 中使用 JSX 语法描述用户界面，它是一种 JavaScript 语法扩展。</p>
<p>在 React 代码执行之前，Babel 会将 JSX 语法转换为标准的 JavaScript API。</p>
<p>JSX 语法就是一种语法糖，让开发人员使用更加舒服的代码构建用户界面。</p>
<h2 data-id="heading-1">JSX 语法</h2>
<p>可以在JSX中使用表达式，JSX本身其实也是一种表达式，可以将它赋值给变量，当作参数传递，作为返回值</p>
<pre><code class="copyable">const user = &#123;
  name: 'tom',
  age: 10
&#125;
const element = <h1>hello &#123;user.name&#125; </h1>

function userInfo () &#123;
  return <div>&#123;element&#125;<div>age: &#123;user.age&#125;</div></div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">插值表达式</h3>
<p>插值表达式中各种数据的插值状态(备注：<code>插值只能执行表达式，不能执行语句</code>)</p>
<ul>
<li>
<p>number——正常输出</p>
</li>
<li>
<p>true / false——不输出</p>
</li>
<li>
<p>undefined——不输出</p>
</li>
<li>
<p>null——不输出</p>
</li>
<li>
<p>数组——去掉逗号后渲染在页面</p>
</li>
<li>
<p>对象——需要调用属性名，不然会报错</p>
<p>function App () &#123;  const booleanVal = true  const numberVal = 10  const nullVal = null  const undefinedVal = undefined  const arrayVal = [1, 2, 3, 4]  const ObjectVal = &#123;    name: 'tom'  &#125;  return (    </p><div>      <div>&#123;booleanVal&#125;</div> &#123;/* 不输出 <em>/&#125;      <div>&#123;numberVal&#125;</div> &#123;/</em> 输出  10 <em>/&#125;      <div>&#123;nullVal&#125;</div> &#123;/</em> 不输出 <em>/&#125;      <div>&#123;undefinedVal&#125;</div> &#123;/</em> 不输出 <em>/&#125;      <div>&#123;arrayVal&#125;</div> &#123;/</em> 输出  1234 <em>/&#125;      &#123;/</em> &#123;ObjectVal&#125; 报错 <em>/&#125;      <div>&#123;ObjectVal.a&#125;</div> &#123;/</em> 输出  tom */&#125;    </div>  )&#125;<p></p>
</li>
</ul>
<h3 data-id="heading-3">列表渲染</h3>
<pre><code class="copyable">function test2 () &#123;  const arrayVal = [1, 2, 3, 4, 5]  return (    <ul>      &#123;        arrayVal.map(item => &#123;          return <li>itemVal: &#123;item&#125;</li>        &#125;)      &#125;    </ul>  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JSX中属性值为字符串类型要加上引号，属性名称最好用驼峰式命名法；属性值式Javascript表达式时，属性值不用引号，要用大括号；类名必须使用className，不能用class；JSX中的标签必须闭合，不然会报错</p>
<pre><code class="copyable">const element1 = <div greeting="普通属性值" ></div>
const element2 = <img src=&#123;user.avatarUrl&#125; /> &#123;/* 值是表达式用大括号 */&#125;
const element3 = <input type="text" /> &#123;/* 标签必须闭合 */&#125;
const element4 = <div className="user-avatar round">类目属性一定要用className</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">标签中的事件</h3>
<p>JSX中事件的绑定涉及this的指向，需要注意</p>
<pre><code class="copyable">&#123;/* 第一个参数即是事件对象 不需传递 */&#125;
<button onClick=&#123;this.eventHandler&#125;>按钮</button>
&#123;/* 需要传递事件对象 */&#125;
<button onClick=&#123;e=>this.eventHandler('arg',e)&#125;>按钮</button>
&#123;/* 最后一个参数即是事件对象 不需传递 */&#125;
<button onClick=&#123;this.eventHandler.bind(null, 'arg')&#125;>按钮</button>
&#123;/* 绑定this的指向 */&#125;
constructor () &#123;
  &#123;/* 在构造函数中将当前eventHandler进行强绑定 指向当前类组件实例 */&#125;
  this.eventHandler = this.eventHandler.bind(this)
&#125;
eventHandler () &#123;&#125;
<button onClick=&#123;this.eventHandler&#125;>按钮</button>
&#123;/* 另一种方式是用箭头函数 */&#125;
addAge = ()=>&#123;
  console.log(this)
&#125;
<button onClick=&#123;this.addAge&#125;>按钮</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">组件</h2>
<p>React中组件分为 类组件 和 函数组件</p>
<p>组件名称首字母必须大写，用来区分组件和普通标签</p>
<p>在JSX语法的外层必须有一个根元素</p>
<ol>
<li>函数式组件
<ul>
<li>函数的名称就是组件的名称</li>
<li>函数的返回值就是组件要渲染的内容</li>
<li>函数组件中没有this</li>
</ul>
</li>
<li>类式组件
<ul>
<li>组件类必须继承<code>React.Component</code></li>
<li>组件类必须有<code>render</code>方法</li>
<li>类组件中this指向实例本身</li>
</ul>
</li>
</ol>
<h3 data-id="heading-6">类组件</h3>
<pre><code class="copyable">import React, &#123; Component &#125; from 'react';
class App extends Component &#123;
    constructor() &#123;&#125;
    render () &#123;
        return <div>Hello, 我是类组件</div>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">函数组件</h3>
<pre><code class="copyable">const Person = () => &#123;
     return <div>Hello, 我是函数型组件</div>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">组件props传递</h3>
<p>在调用组件时可以向组件内部传递数据，在组件中可以通过props获取外部传递进来的数据</p>
<ol>
<li>
<p>props 对象中存储的数据是只读的，不能在组件内部被修改。</p>
</li>
<li>
<p>当 props 数据源中的数据被修改后，组件中的接收到的 props 数据会被同步更新。( 数据驱动DOM )</p>


<p>// 类组件
class Person extends Component &#123;
constructor(props) &#123;
super(props) // 会将props挂载到当前实例的this上
// 这里可以拿到props 也可以用this.props
&#125;
render() &#123;
return (
</p><div>
<h3 data-id="heading-9">姓名：&#123;this.props.name&#125;</h3>
<h4 data-id="heading-10">年龄：&#123;this.props.age&#125;</h4>
</div>
);
&#125;
&#125;<p></p>
<p>// 函数组件
// 通过函数的参数接收props
const Person = props => &#123;
return (
</p><div>
<h3 data-id="heading-11">姓名：&#123;props.name&#125;</h3>
<h4 data-id="heading-12">年龄：&#123;props.age&#125;</h4>
</div>
);
&#125;<p></p>
</li>
</ol>
<h3 data-id="heading-13">设置props默认值</h3>
<pre><code class="copyable">// 类组件
class App extends Component &#123;
    // 作为props的默认值  和传入props重复时，传入props值覆盖
    static defaultProps = &#123;
        defaultName: 'tom'
    &#125;
&#125;
// 函数组件
function ThemedButton(props) &#123;
&#125;
ThemedButton.defaultProps = &#123;
  theme: "secondary",
  label: "Button Text"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件children</p>
<p>通过props.children可以获取到在调用时填充到组件标签内部的内容（类似Vue的slot）</p>
<pre><code class="copyable"><Person>组件内部的内容</Person>
const Person = (props) => &#123;
    return (
     <div>&#123;props.children&#125;</div> &#123;/* 组件内部的内容 */&#125;
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">单向数据流</h3>
<ol>
<li>
<p>在React中, 关于数据流动有一条原则, 就是单向数据流动, 自顶向下, 从父组件到子组件.</p>
</li>
<li>
<p>单向数据流特性要求我们共享数据要放置在上层组件中.</p>
</li>
<li>
<p>子组件通过调用父组件传递过来的方法更改数据.</p>
</li>
<li>
<p>当数据发生更改时, React会重新渲染组件树.</p>
</li>
<li>
<p>单向数据流使组件之间的数据流动变得可预测. 使得定位程序错误变得简单.</p>
</li>
</ol>
<h3 data-id="heading-15">类组件state</h3>
<p>类组件除了能够从外部 (props) 接收状态数据以外还可以拥有自己的状态 (state)，此状态在组件内部可以被更新，状态更新 DOM 更新。</p>
<p>组件内部的状态数据被存储在组件类中的 state 属性中，state 属性值为对象类型，state 这个属性名称固定不可更改。</p>
<pre><code class="copyable">class App extends Component &#123;
  constructor () &#123;
    super()
    this.state = &#123;
      person: &#123; name: '张三', age: 20 &#125;,
    &#125;
  &#125;
  render () &#123;
    return (
      <div>
        &#123;this.state.person.name&#125;
        &#123;this.state.person.age&#125;
      </div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">更改组件状态</h3>
<p>state 状态对象中的数据不可直接更改，如果直接更改 DOM 不会被更新，要更改 state 状态数据需要使用 setState方法。</p>
<pre><code class="copyable">class App extends Component &#123;
  constructor () &#123;
    this.state = &#123;
      person: &#123; name: '张三', age: 20 &#125;,
    &#125;
    this.changePerson = this.changePerson.bind(this)
  &#125;
 changePerson () &#123;
    this.setState(&#123;
      person: &#123;
        name: '李四',
        age: 15
      &#125;
    &#125;)
  &#125;
  render() &#123;
    return (
      <div>
        &#123;this.state.person.name&#125;
        &#123;this.state.person.age&#125;
        <button onClick=&#123;this.changePerson&#125;>按钮</button>
      </div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">state和props区别</h3>
<ol>
<li>state 的主要作用是用于组件保存、控制、修改 自己 的可变状态，在组件内部进行初始化，也可以在组件内部进行修改，但是组件外部不能修改组件的 state</li>
<li>props 的主要作用是让使用该组件的父组件可以传入参数来配置该组件，它是外部传进来的配置参数，组件内部无法控制也无法修改 </li>
<li>state 和 props 都可以决定组件的外观和显示状态。通常，props 做为不变数据或者初始化数据传递给组件，可变状态使用 state</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            