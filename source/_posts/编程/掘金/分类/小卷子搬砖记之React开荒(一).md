
---
title: '小卷子搬砖记之React开荒(一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b035b212f704d989a4e3f946d2ca5bc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 19:35:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b035b212f704d989a4e3f946d2ca5bc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>react白菜一颗，人老了脑子不好用，就多写一写，愿能坚持更新下去</p>
<h2 data-id="heading-0">背景和特性</h2>
<ol>
<li>传统ui操作关注细节太多</li>
<li>程序状态多，不好跟踪和维护</li>
</ol>
<p><strong>react：始终整体刷新页面，无需关心细节</strong></p>
<ul>
<li>
<p>一个新概念</p>
<p>组件：react用组件的方式去描述ui</p>
</li>
<li>
<p>四个API</p>
</li>
<li>
<p>单向数据流</p>
</li>
<li>
<p>完善错误提示</p>
</li>
</ul>
<p><strong>解决了ui问题，如何解决数据模型问题?</strong></p>
<p>传统的MVC模式中Model和View的使用关系复杂，出问题之后很难追踪问题，由此提出了Flux架构：单向数据流</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b035b212f704d989a4e3f946d2ca5bc~tplv-k3u1fbpfcp-zoom-1.image" alt="单向数据流" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当view上产生了用户操作会生成一个action，action通过Dispatcher dispatch出去交给Store处理，view绑定在store上，整体建立在状态之上进行ui的更新。这里个人理解MVC框架的劣势本身其实并不是数据的双向绑定而是内部事件机制的暗箱操作不可控，事实上VUE框架本身也通过v-model实现双向数据绑定，而当我们不关心表单交互过多下的业务无关代码时双向绑定可以压缩很多人工code，不好的就是黑盒下的错误debug难度提升，单向数据流的优缺就是镜像关系了，所以，no silver bullet</p>
<h2 data-id="heading-1">组件构建UI</h2>
<p>传统构建表单页面一般流程是，定义HTML模版，JS拿数据并填充，提交表单时用form绑定事件完成。</p>
<p>react示例：</p>
<pre><code class="hljs language-react copyable" lang="react">class CommentBox extends Component &#123;
    render() &#123;
        return &#123;
            <div className="comment-box">
            <h1>Comments</h1>
                <CommentList/>
                <CommentForm/>
            </div>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CommentBox、CommentList、CommentForm就是组件，组件 = props + state ----> view，react组件的特点：</p>
<ul>
<li>不提供方式，相当于状态机</li>
<li>组件类似于纯函数</li>
<li>单向的数据绑定</li>
</ul>
<p>相应的创建一个组件需要考虑：</p>
<ul>
<li>静态UI：具体使用什么HTML tag</li>
<li>组件状态组成：state来自外部or内部？</li>
<li>组件交互方式：内部如何操作？如何暴露给外部使用者</li>
<li>一个组件只做一件事(设计模式中的单一职责原则)，如果复杂，应该做拆分</li>
<li>状态能计算就不存储</li>
</ul>
<h2 data-id="heading-2">JSX</h2>
<p>不是模版引擎，是一种语法糖，可以在js中直接写HTML标记，</p>
<pre><code class="hljs language-react copyable" lang="react">const element = <h1>hello, &#123;name&#125;</h1>;
//相当于
const element = React.creatElement('h1', null, 'Hello, ', name);

//属性中用表达式 
<MyComponent foo=&#123;1+2+3+4&#125; />;
//延展属性(ES6中也有)
const props = &#123;firtName: 'Ben', lastName: 'Hector'&#125;;
const greeting = <Greeting &#123;...props&#125; />;
//表达式作为子元素
const element = <li>&#123;props.message&#125;</li>
/**
* 小写tag为原生，自定义大写开头
**/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用声明方式描述动态创建组件过程，可以依然使用js特性和熟悉的语法</p>
<h2 data-id="heading-3">React生命周期</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e0f2fb4b69b4b9dac4ce3586b96401e~tplv-k3u1fbpfcp-watermark.image" alt="reactLifeCircle.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>三个阶段</p>
<ul>
<li>render阶段：计算状态</li>
<li>pre-commit阶段：读取DOM内容</li>
<li>commit阶段：状态映射到DOM，更新节点</li>
</ul>
<p>三个类型</p>
<ul>
<li>mounting
<ul>
<li>constructor: 构造函数
<ul>
<li>唯一可以直接修改state的阶段</li>
</ul>
</li>
<li>getDerivedStateFromProps（version 16.3）: 外部属性初始化内部状态
<ul>
<li>state从props初始化时使用，需要维护一致性，每次render都会调用（典型场景：表单默认输入）</li>
</ul>
</li>
<li>render：必定义，描述UI DOM结构</li>
<li>componentDIdMount
<ul>
<li>UI渲染完成时调用，只执行一次</li>
</ul>
</li>
</ul>
</li>
<li>updating（new props: 传进新属性， setState：内部修改状态，forceUpdate：强制刷新）
<ul>
<li>getDerivedStateFromProps</li>
<li>shouldComponentUpdate：是否真的需要render（可优化部分，一般由PureComponent自动实现）</li>
<li>render：diff，虚拟dom计算</li>
<li>getSnapshotBeforeUpdate
<ul>
<li>render之前调用，state已经更新（场景：获取render之前的DOM状态）</li>
</ul>
</li>
<li>componentDidUpdate
<ul>
<li>每次UI更新时调用（场景：重新获取变化后的props）</li>
</ul>
</li>
</ul>
</li>
<li>Unmounting（组件消失时，销毁，做一些资源释放的操作）</li>
</ul>
<p>这里对比VUE框架两者的流程是相似的，都是经历了初始化、创建、挂载、销毁、更新，稍有不同的一点，更新过程挂载阶段react使用componentDidUpdate，vue依然会用mounted</p>
<h2 data-id="heading-4">virtual DOM</h2>
<p>不管是vue还是react都是经过了虚拟DOM的创建和局部更新来达到更快地渲染体验（分层比较，BFS，复杂度为O(n) ）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/025a624e583f4ba9994b1a90ef5af9fb~tplv-k3u1fbpfcp-watermark.image" alt="reactDiff.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图的一次更新中，涉及到几个主要的差异</p>
<ul>
<li>A  B顺序交换</li>
<li>D的层级变换</li>
<li>C节点的消失</li>
<li>G的节点的格式修改</li>
</ul>
<p>react的处理方法（这里的diff不会关心删除的某个节点有没有在其他地方用到，即认为DOM结构相对稳定）</p>
<ul>
<li>第二层，获取A B唯一标识获知顺序变化，交换位置</li>
<li>第三层，F 变为 G 类型变化，删除F，append一个新节点到A上；删除D</li>
<li>第四层，重新创建一个D（这里想当于放弃检查，因为真实情况跨层级的节点移动并不多，可忽略）</li>
</ul>
<h2 data-id="heading-5">组件设计</h2>
<p>高阶组件（HOC）：接收组件作为参数，返回新组件</p>
<pre><code class="hljs language-react copyable" lang="react">//一个简单的计时器HOC
import React from "react";

export default function withTimer(WrappedComponent) &#123;
  return class extends React.Component &#123;
    state = &#123; time: new Date() &#125;;
    componentDidMount() &#123;
      this.timerID = setInterval(() => this.tick(), 1000);
    &#125;

    componentWillUnmount() &#123;
      clearInterval(this.timerID);
    &#125;

    tick() &#123;
      this.setState(&#123;
        time: new Date()
      &#125;);
    &#125;
    render() &#123;
      return <WrappedComponent time=&#123;this.state.time&#125; &#123;...this.props&#125; />;
    &#125;
  &#125;;
&#125;
//之后将withTimer imoport到想使用的js中，并export withTimer(&#123;xxxApp&#125;)，即可在xxxApp中用this.porps.time
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数作为子组件（组件如何render由使用组件的人来决定，降低scope，增加灵活性）：</p>
<pre><code class="hljs language-react copyable" lang="react">//MyComponent将一个函数作为children，是一种通用的设计模式思想 
class MyComponent extends React.Component &#123;
    render() &#123;
        return (
        <div>
            &#123;this.props.children('Nate Wang')&#125;
        </div>
        )
    &#125;
&#125;

<MyComponent>
&#123;(name) => (
    <div>&#123;name&#125;</div> //这里可以写任何UI
    )&#125;
</MyComponent>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">context API（version16.3新特性）</h2>
<p>常用场景：组件树共享全局上下文数据，不需要一层层传递。 <code>const Context = React.creatContext('shareData');</code></p>
<p>通过Provider value="" 来提供值，Consumer state.name来获取值</p></div>  
</div>
            