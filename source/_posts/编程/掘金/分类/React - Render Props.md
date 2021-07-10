
---
title: 'React - Render Props'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: '/cat.jpg'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 19:53:47 GMT
thumbnail: '/cat.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文是对React官网<a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2Fdocs%2Frender-props.html" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/docs/render-props.html" ref="nofollow noopener noreferrer">Render Props</a>的学习总结。</p>
<h3 data-id="heading-0">Render Props</h3>
<p>Render Props是指 <code>React 组件之间使用一个值作为函数的 prop 共享代码</code>的简单技术。</p>
<p>具有 render prop 的组件接受一个<code>函数</code>，该函数返回一个 <code>React 元素</code>并调用它而不是实现自己的渲染逻辑。</p>
<pre><code class="copyable"><DataProvider 
    render=&#123; data => (<h1>Hello &#123;data.target&#125;</h1>) &#125;
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">使用Render Props 解决横切关注点（Cross-Cutting Concerns）</h3>
<p>组件是 React 代码复用的主要单元，但如何将一个<code>组件封装的状态或行为共享给其他需要相同状态的组件</code>并不总是显而易见。</p>
<p>例如，以下组件跟踪 Web 应用程序中的鼠标位置：</p>
<pre><code class="copyable">class MouseTracker extends React.Component &#123;
    constructor(props) &#123;
        super(props);
        this.handleMouseMove = this.handleMouseMove.bind(this);
        this.state = &#123; x: 0, y: 0 &#125;;
    &#125;
    
    handleMouseMove(event) &#123;
        this.setState(&#123;
            x: event.clientX,
            y: event.clientY
        &#125;);
    &#125;
    render() &#123;
        return (
            <div style=&#123;&#123; height: '100vh' &#125;&#125; onMouseMove=&#123;this.handleMouseMove&#125;>
                <h1>移动鼠标!</h1>
                <p>当前的鼠标位置是 (&#123;this.state.x&#125;, &#123;this.state.y&#125;)</p>
            </div>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当光标在屏幕上移动时，组件在 < p > 中显示其（x，y）坐标。</p>
<p><strong>如果此时，其他组件也想获取（x, y）坐标，就需要把这一部分代码逻辑封装起来。</strong> 可以试着在 Mouse 组件中封装我们需要共享的行为。</p>
<pre><code class="copyable">class Mouse extends React.Component &#123;
    constructor(props) &#123;
        super(props);
        this.handleMouseMove = this.handleMouseMove.bind(this);
        this.state = &#123; x: 0, y: 0 &#125;;
    &#125;
    handleMouseMove(event) &#123;
        this.setState(&#123;
            x: event.clientX,
            y: event.clientY
        &#125;);
    &#125;
    render() &#123;
        return (
            <div style=&#123;&#123; height: '100vh' &#125;&#125; onMouseMove=&#123;this.handleMouseMove&#125;>

                &#123;/* ...但我们如何渲染 <p> 以外的东西? */&#125;
                <p>The current mouse position is (&#123;this.state.x&#125;, &#123;this.state.y&#125;)</p>
            </div>
        );
    &#125;
&#125;

class MouseTracker extends React.Component &#123;
    render() &#123;
        return (
            <>
                <h1>移动鼠标!</h1>
                <Mouse />
            </>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在 < Mouse > 组件封装了所有关于监听 mousemove 事件和存储鼠标 (x, y) 位置的行为，但其仍不是真正的可复用。</p>
<p>举个例子，假设我们有一个 < Cat > 组件，它可以呈现一张在屏幕上追逐鼠标的猫的图片。我们或许会使用
< Cat mouse = &#123;&#123; x, y &#125;&#125; /> 通过 prop 来告诉组件鼠标的坐标以让它知道图片应该在屏幕哪个位置。</p>
<p>首先, 尝试在 < Mouse > 内部的渲染方法渲染 < Cat > 组件：</p>
<pre><code class="copyable">class Cat extends React.Component &#123;
    render() &#123;
        const mouse = this.props.mouse;
        return (
            <img 
                src="/cat.jpg" 
                style=&#123;&#123; position: 'absolute', left: mouse.x, top: mouse.y &#125;&#125; 
            />
        );
    &#125;
&#125;

class MouseWithCat extends React.Component &#123;
    constructor(props) &#123;
        super(props);
        this.handleMouseMove = this.handleMouseMove.bind(this);
        this.state = &#123; x: 0, y: 0 &#125;;
    &#125;
    handleMouseMove(event) &#123;
        this.setState(&#123;
            x: event.clientX,
            y: event.clientY
        &#125;);
    &#125;
    render() &#123;
        return (
            <div style=&#123;&#123; height: '100vh' &#125;&#125; onMouseMove=&#123;this.handleMouseMove&#125;>
                &#123;/*
                    我们可以在这里换掉 <p> 的 <Cat>   ......
                    但是接着我们需要创建一个单独的 <MouseWithSomethingElse>
                    每次我们需要使用它时，<MouseWithCat> 是不是真的可以重复使用.
                */&#125;
                <Cat mouse=&#123;this.state&#125; />
            </div>
        );
    &#125;
&#125;

class MouseTracker extends React.Component &#123;
    render() &#123;
        return (
            <div>
                <h1>移动鼠标!</h1>
                <MouseWithCat />
            </div>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法仅仅适用于我们的特定用例，但我们还没有达到以可复用的方式真正封装行为的目标。现在，每当我们想要鼠标位置用于不同的用例时，我们必须创建一个新的组件（本质上是另一个 < MouseWithCat > ），它专门为该用例呈现一些东西。</p>
<p>这也是 render prop 的来历：相比于直接将 < Cat > 写死在 < Mouse > 组件中，并且有效地更改渲染的结果，我们可以为 < Mouse > 提供一个函数 prop 来动态的确定要渲染什么 —— 一个 render prop。</p>
<pre><code class="copyable">class Cat extends React.Component &#123;
    render() &#123;
        const mouse = this.props.mouse;
        return (
            <img 
                src="/cat.jpg" 
                style=&#123;&#123; position: 'absolute', left: mouse.x, top: mouse.y &#125;&#125;
            />
        );
    &#125;
&#125;

class Mouse extends React.Component &#123;
    constructor(props) &#123;
        super(props);
        this.handleMouseMove = this.handleMouseMove.bind(this);
        this.state = &#123; x: 0, y: 0 &#125;;
    &#125;
    handleMouseMove(event) &#123;
        this.setState(&#123;
            x: event.clientX,
            y: event.clientY
        &#125;);
    &#125;
    render() &#123;
        return (
            <div style=&#123;&#123; height: '100vh' &#125;&#125; onMouseMove=&#123;this.handleMouseMove&#125;>

                &#123;/*
                    使用 render prop 动态决定要渲染的内容，
                    而不是给出一个 <Mouse> 渲染结果的静态表示
                */&#125;
                &#123;this.props.render(this.state)&#125;
            </div>
        );
    &#125;
&#125;

class MouseTracker extends React.Component &#123;
    render() &#123;
        return (
            <div>
                <h1>移动鼠标!</h1>
                <Mouse render=&#123;mouse => (
                    <Cat mouse=&#123;mouse&#125; />
                )&#125;/>
            </div>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们提供了一个 render 方法 <code>让 < Mouse > 能够动态决定什么需要渲染，而不是克隆 < Mouse > 组件然后硬编码来解决特定的用例。</code></p>
<p>具体的说，<strong>render prop 是一个用于告知组件需要渲染什么内容的函数 prop。</strong></p>
<p>这项技术使我们共享行为非常容易。要获得这个行为，只要渲染一个带有 render prop 的 < Mouse > 组件就能够告诉它当前鼠标坐标 (x, y) 要渲染什么。</p>
<p>关于 render prop 一个有趣的事情是你可以使用带有 render prop 的常规组件来实现大多数高阶组件 (HOC)。 例如，如果你更喜欢使用 withMouse HOC 而不是 < Mouse > 组件，你可以使用带有 render prop 的常规   < Mouse > 轻松创建一个：</p>
<pre><code class="copyable">// 如果你出于某种原因真的想要 HOC，那么你可以轻松实现
// 使用具有 render prop 的普通组件创建一个！
function withMouse(Component) &#123;
    return class extends React.Component &#123;
        render() &#123;
            return (
                <Mouse render=&#123;mouse => (
                    <Component &#123;...this.props&#125; mouse=&#123;mouse&#125; />
                )&#125;/>
            );
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">使用 Props 而非 render</h3>
<p>重要的是要记住，render prop 是因为模式才被称为 render prop，你不一定要用名为 render 的 prop 来使用这种模式。事实上，<strong>任何被用于告知组件需要渲染什么内容的函数 prop 在技术上都可以被称为 “render prop”。</strong></p>
<p>尽管之前的例子使用了 render，我们也可以简单地使用 children prop。</p>
<pre><code class="copyable"><Mouse children=&#123;mouse => (
    <p>鼠标的位置是 &#123;mouse.x&#125;，&#123;mouse.y&#125;</p>
)&#125;/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>children prop 并不真正需要添加到 JSX 元素的 “attributes” 列表中。相反，可以直接放置到元素的内部。</p>
<pre><code class="copyable"><Mouse>
    &#123;mouse => (
        <p>鼠标的位置是 &#123;mouse.x&#125;，&#123;mouse.y&#125;</p>
    )&#125;
</Mouse>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于这一技术的特殊性，当你在设计一个类似的 API 时，你或许会要直接地在你的 propTypes 里声明 children 的类型应为一个函数。</p>
<pre><code class="copyable">Mouse.propTypes = &#123;
    children: PropTypes.func.isRequired
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">注意事项</h3>
<h4 data-id="heading-4">将 Render Props 与 React.PureComponent 一起使用时要小心</h4>
<p>如果你在 render 方法里创建函数，那么使用 render prop 会抵消使用 React.PureComponent 带来的优势。因为浅比较 props 的时候总会得到 false，并且在这种情况下每一个 render 对于 render prop 将会生成一个新的值。</p>
<p>例如，继续我们之前使用的 < Mouse > 组件，如果 Mouse 继承自 React.PureComponent 而不是 React.Component，我们的例子看起来就像这样：</p>
<pre><code class="copyable">class Mouse extends React.PureComponent &#123;
    // 与上面相同的代码......
&#125;

class MouseTracker extends React.Component &#123;
    render() &#123;
        return (
            <div>
                <h1>Move the mouse around!</h1>

                    &#123;/*
                        这是不好的！
                        每个渲染的 `render` prop的值将会是不同的。
                    */&#125;
                    <Mouse render=&#123;mouse => (
                        <Cat mouse=&#123;mouse&#125; />
                    )&#125;/>
            </div>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这样例子中，每次 < MouseTracker > 渲染，它会生成一个新的函数作为 < Mouse render > 的 prop，因而在同时也抵消了继承自 React.PureComponent 的 < Mouse > 组件的效果！</p>
<p>为了绕过这一问题，有时你可以定义一个 prop 作为实例方法，类似这样：</p>
<pre><code class="copyable">class MouseTracker extends React.Component &#123;
    // 定义为实例方法，`this.renderTheCat`始终
    // 当我们在渲染中使用它时，它指的是相同的函数
    renderTheCat(mouse) &#123;
        return <Cat mouse=&#123;mouse&#125; />;
    &#125;

    render() &#123;
        return (
            <div>
                <h1>Move the mouse around!</h1>
                <Mouse render=&#123;this.renderTheCat&#125; />
            </div>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你无法静态定义 prop（例如，因为你需要控制组件 props 和/或 state 的暴露程度），则 < Mouse > 应该继承自 React.Component。</p></div>  
</div>
            