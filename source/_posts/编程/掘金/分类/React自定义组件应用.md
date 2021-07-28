
---
title: 'React自定义组件应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fa8671b32b4db49367daff91e7b2cf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 10:15:07 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fa8671b32b4db49367daff91e7b2cf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">React自定义组件应用</h2>
<blockquote>
<p>今天在学习React自定义组件的时候就联想到了之前在学小程序的时候写的自定义组件，不过它们子向父传递数据和父向子传递数据的方式是有所不同的。</p>
</blockquote>
<h3 data-id="heading-1">组件化编码流程</h3>
<p>这里通过一个案例来演示。</p>
<ol>
<li>拆分组件: 拆分界面,抽取组件</li>
<li>实现静态组件: 使用组件实现静态页面效果</li>
<li>实现动态组件：动态显示初始化数据(数据类型、数据名称)</li>
<li>交互(绑定事件监听等)</li>
</ol>
<p>比如实现下面这个<code>todos</code>，因为这里主要是要讲组件，所以对这些样式什么的就不做详细的解释了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fa8671b32b4db49367daff91e7b2cf~tplv-k3u1fbpfcp-watermark.image" alt="todos.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将这一整个看成<code>App</code>组件，里面分成4个小组件，分别为<code>Header</code>、<code>List</code>、<code>Item</code>、<code>Footer</code>。下面通过这个案例来说一下<strong>子向父传递数据</strong>和<strong>父向子传递数据</strong>的方法。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f5d2f115594d4e8e465477a3f411cf~tplv-k3u1fbpfcp-watermark.image" alt="todos zujian.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">1. 父向子传递数据</h3>
<h4 data-id="heading-3">动态渲染List</h4>
<p>首先，Item 是 List 的子组件，在动态渲染的过程中，要用一个 List 向 Item 传递列表的值让 Item 渲染出来，此时我们没办法直接让列表的数据直接从List传递到Item，因此应该把此时的状态<code>state</code>中的数据<code>todos</code>定义在<code>App</code>组件中，通过<code>App</code>组件传给<code>App</code>组件的子组件List，再由List将值传递给Item从而将<code>todos</code>渲染出来。子组件再从<code>this.props</code>取出从父组件传过来的值。</p>
<p>简单讲，这里的涉及到的知识点就是父向子传递数据。</p>
<pre><code class="copyable">// App.jsx
export default class App extends Component &#123;
    state = &#123;
        todos: [
            &#123; id: '1', name: '吃饭', done: true &#125;,
            &#123; id: '2', name: '睡觉', done: false &#125;,
            &#123; id: '3', name: '打代码', done: false &#125;,
        ]
    &#125;
    render() &#123;
        const &#123; todos &#125; = this.state;
        return (
            <div className="todo-container">
                <div className="todo-wrap">
                    <Header></Header>
                    <List todos=&#123;todos&#125;></List>
                    <Footer></Footer>
                </div>
            </div>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之前学习小程序的时候，也有这个知识点(<a href="https://juejin.cn/post/6986576247484579854" target="_blank" title="https://juejin.cn/post/6986576247484579854">微信小程序——自定义组件</a>)，不过<code>React</code>中的子向父传递数据中，我们是要对<code>props</code>进行类型限制，在小程序中，还需要子组件在<code>json</code>文件中的<code>properties</code>中定义从父组件传递的数据。</p>
<p>注意点：</p>
<ul>
<li>表示是否完成的<code>checkbox</code>的<code>checked</code>属性值应为<code>defalutChecked</code>，否则<code>checked</code>值无法通过点击改变</li>
<li>在渲染<code>todos</code>要给每一个Item添加一个key值(<code>key=&#123;todos.id&#125;</code>)</li>
</ul>
<h3 data-id="heading-4">2. 子向父传递数据</h3>
<h4 data-id="heading-5">input添加<code>todos</code></h4>
<p><code>Header</code>要将用户输入的值传递给List需要经过这个数据传递的过程：Header -> <code>App</code> -> List；</p>
<p>也就是说，这个的传递数据方式与上面的动态渲染相比，多了一个子向父传递数据。这个的实现方式是通过<code>props</code>从父组件<code>App</code>给子组件<code>List</code>传递一个函数(<code>addTodos</code>)。也就是说，在<code>React</code>中，子向父传递数据是通过函数来建立关系的。</p>
<pre><code class="copyable">addTodos = (todoObj) => &#123;
    const &#123; todos &#125; = this.state;
    const newTodos = [todoObj, ...todos];
    this.setState(&#123; todos: newTodos &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，在子组件(Header)中调用这个函数，当键盘按回车键的时候调用这个函数，然后把用户输入的东西给父组件中定义的函数。</p>
<pre><code class="copyable">handleKeyUp = (e) => &#123;
    const &#123; keyCode, target &#125; = e;
    if (keyCode !== 13) return;
    if (target.value.trim() === '') return;
    const todoObj = &#123; id: nanoid(), name: target.value, done: false &#125;
    this.props.addTodos(todoObj)
    target.value = '';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有一个库(<code>uuid</code>)能够获取唯一标识，给id赋值，让每一个item都有一个独一无二的id值作为key，进行遍历。在终端输入<code>npm install uuid</code>或者<code>npm add nanoid</code>都可以下载这个库，前者的文件比较大，建议下载第二个。在要调用的时候记得在引入<code>import &#123;nanoid&#125; from 'nanoid'</code>。</p>
<h3 data-id="heading-6">对props进行限制</h3>
<p>对<code>props</code>传递的属性类型进行必要性的限制。设置了类型之后，如果在传的值不是这个类型的话，就会报错</p>
<p>引入<code>prop-types</code>库：在终端输入<code>npm add prop-types</code>。 引入<code>import PropTypes from 'prop-types'</code></p>
<pre><code class="copyable">static propTypes &#123;
    addTodos: PropTypes.func.isRequired
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">总结</h3>
<ol>
<li>
<p>拆分组件、实现静态组件。注意：<code>className</code>、<code>style</code>的写法</p>
</li>
<li>
<p>动态初始化列表，如果是在某个组件使用就将state放在自身，如果是在多个组件使用就放在父组件中(<strong>状态提升</strong>)</p>
</li>
<li>
<p>【父组件】给【子组件】传递数据：通过<code>props</code>传递</p>
<p>【子组件】给【父组件】传递数据：通过<code>props</code>传递，要求父提前给子一个函数</p>
</li>
<li>
<p>注意<code>defaultChecked</code>和<code>checked</code>的区别。类似的还有：<code>defaultValue</code>和<code>value</code></p>
</li>
<li>
<p>状态改变记得<code>setState</code></p>
</li>
</ol></div>  
</div>
            