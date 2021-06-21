
---
title: '从Vue2.0到React17——React中实现Vue指令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5637'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 03:48:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=5637'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”</p>
<h2 data-id="heading-0">前言</h2>
<p>Vue提供了一些列的指令，帮助我们快速开发组件，如最常用的<code>v-model</code>、<code>v-show</code>、<code>v-if</code>、<code>v-for</code>，这些指令的功能在React中是如何提供的。</p>
<h2 data-id="heading-1">1、React中的v-model</h2>
<p>在Vue中的<code>v-model</code>的作用是实现数据双向绑定。这里要特别注意，Vue和React都是单向数据流的，数据双向绑定和数据流是两个独立的概念。</p>
<p>因为在Vue中<code>v-model</code>只能在表单元素<code><input></code>、<code><textarea></code>、<code><select></code>和组件Components上使用，故分表单元素和组件两种使用场景来介绍React中的<code>v-model</code>。</p>
<h3 data-id="heading-2">1.1 表单元素的v-model</h3>
<p>在React中是用<strong>受控组件</strong>的概念来实现表单元素上的<code>v-model</code>。</p>
<p>那什么是受控组件呢？我是这么理解的。在表单元素<code><input></code>、<code><textarea></code> 和 <code><select></code>中通常是自己维护数据，并根据用户输入来更新数据。假如我们用React的state来替换这个数据会怎样呢？例如：</p>
<pre><code class="copyable">import React from 'react';
export default class Input extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state=&#123;
      value:'请输入内容',
    &#125;
  &#125;
  render() &#123;
    return (
      <input type="text" value=&#123;this.state.value&#125;/>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会发现Input输入框无法输入内容了，这是因为<code><input/></code>标签的<code>value</code>属性是可读写的，当我们在Input输入框输入内容时其实是在改变<code>value</code>的值。</p>
<p>这是因为<code>this.state.value</code>在React类组件中只能通过<code>this.setState()</code>来修改。那么在<code><input/></code>标签的<code>value</code>属性被<code>this.state.value</code>赋值后，在Input输入框输入内容时，js内部无法修改<code>this.state.value</code>，导致无法修改<code>value</code>的值，从而造成Input输入框无法输入内容。</p>
<p>相当于Input输入框被<code>this.state.value</code>这个state给控制了，React将这种类型的Input输入框称为<strong>受控组件</strong>。</p>
<p>那如何恢复Input输入框的输入功能呢？这要借助React的合成事件<code>onChange</code>来监听Input输入框的输入，获取输入值，再用<code>this.setState()</code>来把输入值赋值给<code>this.state.value</code>，间接来改变<code>value</code>的值。</p>
<pre><code class="copyable">import React from 'react';
export default class Input extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      value: '请输入内容',
    &#125;
    this.handleChange = this.handleChange.bind(this);
  &#125;
  handleChange(e) &#123;
    this.setState(&#123; value: e.target.value &#125;);
  &#125;
  render() &#123;
    return (
      <>
        <input
          type="text"
          value=&#123;this.state.value&#125;
          onChange=&#123;this.handleChange&#125;
        />
        <span>&#123;this.state.value&#125;</span>
      </>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>this.state.value</code>和Input输入框绑定在一起，随着Input输入框输入内容的改变，<code>this.state.value</code>也会跟着改变，当<code>this.state.value</code>改变时，Input输入框的内容也会改变，这就是数据双向绑定。</p>
<p>以上实现的是不是和<code>v-modle</code>的功能一模一样。下面来看一下函数组件如何实现<code>v-modle</code>。</p>
<pre><code class="copyable">import &#123; useState &#125; from "react";
export default function Index() &#123;
  const [value, setValue] = useState('请输入内容');
  const handleChange = (e) => &#123;
    setValue(e.target.value)
  &#125;
  return (
    <>
    <input type="text" value=&#123;value&#125; onChange=&#123;handleChange&#125; />
    <span>&#123;value&#125;</span>
    </>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.2 React组件的v-model</h3>
<p>Vue组件的<code>v-model</code>是个语法糖，本质上是利用名为value的prop和名为input的事件。</p>
<p>例如在组件上使用<code>v-model="info"</code>时，其实是把<code>info</code>数据传递给<code>value</code>，当<code>info</code>数据改变时组件的<code>value</code>也跟着改变。</p>
<p>双向数据绑定要求组件的<code>value</code>改变时<code>info</code>数据也得跟着改变，可以在组件的<code>value</code>改变时执行<code>this.$emit('input',data)</code>，触发名为 input 的事件，该事件绑定函数<code>(data) => &#123; this.info = data&#125;</code>，其中<code>data</code>是<code>value</code>改变后的值，执行后就实现了双向数据绑定。</p>
<p>那么在React中也可以按这个思路来实现<code>v-model</code>。</p>
<pre><code class="copyable">import React from 'react';
export default class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
  &#125;
  render() &#123;
    return (
      <>
        <div>&#123;this.props.value&#125;</div>
        <button
          onClick=&#123;this.props.onChange.bind(this, '子组件改变info的值')&#125;
        >
          子组件改变info的值
        </button>
      </>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import React from 'react';
import HelloWorld from './HelloWorld';
export default class Input extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      info: '父组件改变info的值',
    &#125;
    this.handleChange = this.handleChange.bind(this);
  &#125;
  handleChange(data) &#123;
    this.setState(&#123; info: data &#125;);
  &#125;
  render() &#123;
    return (
      <>
        <button
          onClick=&#123;() =>&#123;this.setState(&#123;info:'父组件改变info的值'&#125;)&#125;&#125;
        >
          父组件改变info的值
        </button>
        <HelloWorld
          value=&#123;this.state.info&#125;
          onChange=&#123;this.handleChange&#125;
        >
        </HelloWorld>
      </>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件的写法：</p>
<pre><code class="copyable">export default function HelloWorld(props) &#123;
  const &#123; value, onChange &#125; = props
  return (
    <>
      <div>&#123;value&#125;</div>
      <button
        onClick=&#123;() => &#123; onChange('子组件改变info的值') &#125;&#125;
      >
        子组件改变info的值
       </button>
    </>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import &#123; useState &#125; from 'react';
import HelloWorld from './HelloWorld';
export default function Input() &#123;
  const [info, setInfo] = useState('父组件改变info的值');
  const handleChange = (data) => &#123;
    setInfo(data)
  &#125;
  return (
    <>
      <button
        onClick=&#123;() => &#123; setInfo('父组件改变info的值') &#125;&#125;
      >
        父组件改变info的值
        </button>
      <HelloWorld
        value=&#123;info&#125;
        onChange=&#123;handleChange&#125;
      >
      </HelloWorld>
    </>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">2、React中的v-show</h2>
<p>Vue的<code>v-show</code>本质是设置所添加指令的元素的css属性<code>display</code>的值，当<code>v-show="true"</code>时，把<code>display</code>设为<code>block</code>，当<code>v-show='false'</code>设为<code>none</code>。</p>
<p>React中这样实现<code>v-show</code>，分类组件和函数组件来介绍。</p>
<p>类组件的写法：</p>
<pre><code class="copyable">import React from 'react';
export default class Index extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      show: true
    &#125;
  &#125;
  render() &#123;
    return (
      <div 
        style=&#123;&#123; 'display': this.state.show ? 'block' : 'none' &#125;&#125;
      >
        hello world
      </div>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件的写法：</p>
<pre><code class="copyable">import &#123; useState &#125; from "react";

export default function Index() &#123;
  const [show, setShow] = useState(false);
  return (
    <div
      style=&#123;&#123; 'display': show ? 'block' : 'none' &#125;&#125;
    >
      hello world
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React中实现的<code>v-show</code>比Vue中更灵活，假如元素的css属性<code>display</code>的值为<code>flex</code>，使用<code>v-show</code>会导致样式错乱，而在React可以这样解决。</p>
<pre><code class="copyable"><div
  style=&#123;&#123; 'display': show ? 'flex' : 'none' &#125;&#125;
>
  hello world
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3、React中的v-if和v-else</h2>
<p>Vue中用<code>v-if</code>和<code>v-else</code>来控制元素是否被渲染。</p>
<p>在JSX语法中，JavaScript 表达式可以被包裹在<code>&#123;&#125;</code>中作为子元素，另外函数也可以被包裹在<code>&#123;&#125;</code>中作为子元素，该函数执行后必须返回React元素。同时在JSX语法中<code>false</code>、<code>null</code>、<code>undefined</code>、<code>true</code> 是合法的子元素，但它们并不会被渲染，故可以依据此特性来决定是否要渲染其他的 React 元素，来实现React中的<code>v-if</code>和<code>v-else</code>。</p>
<p>类组件的写法：</p>
<ul>
<li>用JavaScript表达式包裹在<code>&#123;&#125;</code>中来实现：</li>
</ul>
<pre><code class="copyable">import React from 'react';
export default class Index extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      show: false
    &#125;
  &#125;
  render() &#123;
    return (
      <React.Fragment>
        &#123;this.state.show ? <div>hello world</div> : <div>hello React</div>&#125;
      </React.Fragment>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React组件返回的元素和Vue一样必须有个根元素，所以用<code><React.Fragment></code>来包裹，<code><React.Fragment></code>不会在DOM中渲染出额外的元素，跟Vue中的<code><template></code>元素一样。</p>
<ul>
<li>用函数包裹在<code>&#123;&#125;</code>中来实现：</li>
</ul>
<pre><code class="copyable">import React from 'react';
export default class Index extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      show: false
    &#125;
  &#125;
  render() &#123;
    return (
      <React.Fragment>
        &#123;
          (() => &#123;
            if (this.state.show) &#123;
              return (
                <div>hello world</div>
              )
            &#125; else &#123;
              return (
                <div>hello world</div>
              )
            &#125;
          &#125;)()
        &#125;
      </React.Fragment>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件的写法：</p>
<ul>
<li>用JavaScript表达式包裹在<code>&#123;&#125;</code>中来实现：</li>
</ul>
<pre><code class="copyable"> import &#123; useState &#125; from "react";

export default function Index() &#123;
  const [show, setShow] = useState(false);
  return (
    <>
      &#123;show ? <div>hello world</div> : <div>hello React</div>&#125;
    </>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code><></></code>相当<code><React.Fragment></React.Fragment></code>。</p>
<ul>
<li>用函数包裹在<code>&#123;&#125;</code>中来实现：</li>
</ul>
<pre><code class="copyable">import &#123; useState &#125; from "react";

export default function Index() &#123;
  const [show, setShow] = useState(false);
  const Title = () => &#123;
    if (show) &#123;
      return (
        <div>hello world</div>
      )
    &#125; else &#123;
      return (
        <div>hello React</div>
      )
    &#125;
  &#125;
  return (
    <>
      &#123;Title()&#125;
    </>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4、React中的v-for</h2>
<p>在Vue中用<code>v-for</code>来渲染列表形式的组件，在Reacr中可以用<code>map()</code>函数来实现，但是要注意在<code>map()</code>方法中的元素需要设置<code>key</code>属性，否值会引起警告错误。</p>
<p>类组件的写法：</p>
<pre><code class="copyable">import React from 'react';
export default class Index extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123;
      list: ['小明', '小红', '小东']
    &#125;
  &#125;
  render() &#123;
    return (
      <React.Fragment>
        &#123;this.state.list.map((item, index) => &#123;
          return (
            <div key=&#123;index&#125;>&#123;item&#125;</div>
          )
        &#125;)&#125;
      </React.Fragment>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当数组类型的数据中每一项没有唯一性<code>id</code>的时候，可以使用索引<code>index</code>作为<code>key</code>，如果数据的顺序可能会变化，不要使用索引<code>index</code>作为<code>key</code>，因为这样做会导致性能变差，还可能引起组件状态的问题，此时可以要求服务端给每项数据添加一个唯一值<code>key</code>，或者用随机数作为<code>key</code>。</p>
<p>函数组件的写法：</p>
<pre><code class="copyable">import &#123; useState &#125; from "react";

export default function Index() &#123;
  const [list, setList] = useState(['小明', '小红', '小东']);
  return (
    <>
      &#123;list.map((item, index) => &#123;
          return (
            <div key=&#123;index&#125;>&#123;item&#125;</div>
          )
        &#125;)&#125;
    </>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">小结</h2>
<p>本文介绍了Vue开发中常用的指令在React中是如何实现的。读完本文，你应该会按原先用Vue开发一些复杂组件的UI界面及UI交互的思路去用React来开发一些复杂组件的UI界面及UI交互。然而组件的业务交互一般是在组件的生命周期钩子函数中去处理的，比如从服务端请求数据等等。所以下一篇文章将介绍React组件的生命周期。</p></div>  
</div>
            