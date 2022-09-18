
---
title: '11-react-context上下文'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5e4e79cc624cf685005a8fc62861f9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 05:44:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5e4e79cc624cf685005a8fc62861f9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:23px;margin-bottom:5px;font-weight:700;padding-left:10px;border-left:5px solid #773098&#125;.markdown-body h2&#123;font-size:19px;font-weight:700;padding-left:10px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:17px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;font-size:14px;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:1em 0;border-radius:6px;box-shadow:2px 4px 7px #999;user-select:none&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;font-weight:400;font-size:.9em;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8;scroll-behavior:smooth&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:14px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5;border-collapse:collapse&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;border:1px solid #916dd5&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">上下文</h2>
<p>上下文(Context) 提供了一种通过组件树传递数据的方法，无需在每个级别手动传递 props 属性。非常之方便。</p>
<p>在典型的 React 应用程序中，数据通过 props 自上而下（父到子）传递，但对于应用程序中许多组件所需的某些类型的 props（例如环境偏好,UI主题），这可能很麻烦。 上下文(Context) 提供了在组件之间共享这些值的方法，而不必在树的每个层级显式传递一个 prop 。</p>
<h3 data-id="heading-1">何时用Context?</h3>
<p>顶层数据改变，让下面所有的都改变,例如，点击按钮，使子组件的主题都进行交换。注意：不使用props传值。</p>
<p>在源码中，容器提供了proviser consumer，创建两个组件，且可以传入默认值以备用。</p>
<h3 data-id="heading-2">正文：</h3>
<p>定义两个主题：</p>
<pre><code class="hljs language-css copyable" lang="css"> const themes = &#123;
            light: &#123;
                <span class="hljs-attribute">color</span>: <span class="hljs-string">"pink"</span>,
                background: <span class="hljs-string">"pink"</span>
            &#125;,
            dark: &#123;
                <span class="hljs-attribute">color</span>: <span class="hljs-string">'white'</span>,
                background: <span class="hljs-string">"white"</span>
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后创建一个 <code>&#123; Provider, Consumer &#125;</code> 对。当 React 渲染 context <code>Consumer</code> 时，它将从组件树中匹配最接近的 <code>Provider</code> 中读取当前的 context 值。</p>
<p><code>defaultValue</code> 参数 <strong>仅</strong> 当 Consumer(使用者) 在树中没有匹配的 Provider(提供则) 时使用它。这有助于在不封装它们的情况下对组件进行测试。注意：将 <code>undefined</code> 作为 Provider(提供者) 值传递不会导致 Consumer(使用者) 使用 <code>defaultValue</code> 。</p>
<p>在这里，我们定义默认为粉色主题：</p>
<pre><code class="hljs language-php copyable" lang="php"> <span class="hljs-keyword">const</span> &#123; Provider, Consumer &#125; = React.<span class="hljs-title function_ invoke__">createContext</span>(&#123; <span class="hljs-attr">theme</span>: themes.light &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先去定义一个根组件，在根组件中嵌套一个A作为子组件，B也作为子组件，但不同的是，一个会用于provider的使用，另一个不会。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title function_">render</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">A</span>></span>A组件<span class="hljs-tag"></<span class="hljs-name">A</span>></span></span>
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ThemeButton</span> /></span></span>
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">B</span>/></span></span>
    )
&#125;
 <span class="hljs-keyword">function</span> <span class="hljs-title function_">ThemeButton</span>(<span class="hljs-params"></span>) &#123;
   <span class="hljs-keyword">return</span> (
       <button>change theme<button/>
   )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当点击按钮时，进行主题切换。</p>
<h3 data-id="heading-3">方法，用到一个三元：</h3>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">handleTheme = () => &#123;
                <span class="hljs-keyword">const</span> theme = <span class="hljs-keyword">this</span>.state.theme === themes.light ? themes.dark : themes.light
                <span class="hljs-keyword">this</span>.setState(&#123;
                    theme
                &#125;)
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义好方法，就可以在provider中设置value了。</p>
<p>（<strong>注意为什么在一个构造函数中，是因为在该构造函数中的方法，会等到非构造函数中的方法挂载完再运行，这样就避免了里面的方法是undefined的现象。</strong>）</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"> <span class="hljs-keyword">constructor</span>() &#123;
                <span class="hljs-keyword">super</span>();
                <span class="hljs-comment">// 在这里能拿到箭头函数，在外面拿不到</span>
                <span class="hljs-keyword">this</span>.state = &#123; theme: themes.light, handleTheme: <span class="hljs-keyword">this</span>.handleTheme &#125;
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面，回到根组件中的provider中，传入value给consumer。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
                <span class="hljs-keyword">return</span> (
                    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state&#125;</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">A</span> ></span>A 组件，我被包裹了<span class="hljs-tag"></<span class="hljs-name">A</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">ThemeButton</span> /></span>
                        <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">B</span> /></span>
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
                )
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，包裹在provider中的组件才会被掌控，组件B的主题始终都会是默认值。</p>
<p>已经将值传给子组件，下面用Consumer来接收并使用:</p>
<p>通过一个回调的方式拿到对象，对象里包含balue传过来的所有数据，有主题和方法，可以拆解出来的。
另外要注意consumer只能是后面接&#123;&#125;的格式，不可以中间隔div，亲测报错。来到A组件中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">function</span> <span class="hljs-title function_">A</span>(<span class="hljs-params"></span>) &#123;
            <span class="hljs-keyword">return</span> (
                <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Consumer</span>></span>
                    &#123;
                        //拿到这个 通过函数传过来 值
                        (obj) => &#123;
                            console.log(obj);
                            const &#123;theme,handleTheme&#125; = obj
                            return (
                                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                                    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">...theme</span> &#125;&#125;></span>A Component,我被包裹了<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>                               
                                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                            )
                        &#125;
                    &#125;

                <span class="hljs-tag"></<span class="hljs-name">Consumer</span>></span></span>

            )
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来到按钮组件中,同样的方法，回调解构取值</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">function</span> <span class="hljs-title function_">ThemeButton</span>(<span class="hljs-params"></span>) &#123;
            <span class="hljs-keyword">return</span> (
                <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Consumer</span>></span>&#123;
                    (obj) => &#123;
                        const &#123;theme,handleTheme&#125; = obj
                        return (
                            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleTheme</span>
                            &#125; <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">...theme</span> &#125;&#125; ></span>change theme<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                        )

                    &#125;
                &#125;
                <span class="hljs-tag"></<span class="hljs-name">Consumer</span>></span></span>

            )
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5e4e79cc624cf685005a8fc62861f9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>真的很方便吧。</p>
<h2 data-id="heading-4">多个context</h2>
<p>为了保持 context 的快速重新渲染，React 需要使每个 context Consumer 成为树中的一个独立节点。</p>
<h3 data-id="heading-5">设置provider:</h3>
<pre><code class="hljs language-scala copyable" lang="scala">const <span class="hljs-type">MoneyContext</span> = <span class="hljs-type">React</span>.createContext(<span class="hljs-number">0</span>)
const <span class="hljs-type">HouseContext</span> = <span class="hljs-type">React</span>.createContext(<span class="hljs-string">""</span>)
        <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">F</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
            state = &#123;
                money: <span class="hljs-number">50</span>,
                house: <span class="hljs-string">"apartment"</span>
            &#125;
            render() &#123;
                <span class="hljs-keyword">return</span> (
                    <span class="hljs-comment">// 区分provider</span>
                    <<span class="hljs-type">MoneyContext</span>.<span class="hljs-type">Provider</span> value=&#123;<span class="hljs-keyword">this</span>.state.money&#125;>
                        <<span class="hljs-type">HouseContext</span>.<span class="hljs-type">Provider</span> value=&#123;<span class="hljs-keyword">this</span>.state.house&#125;>
                            <<span class="hljs-type">S</span> />
                        </<span class="hljs-type">HouseContext</span>.<span class="hljs-type">Provider</span>>
                    </<span class="hljs-type">MoneyContext</span>.<span class="hljs-type">Provider</span>>
                )
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">使用consumer:</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-keyword">return</span> (
                    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MoneyContext.Consumer</span>></span>
                        &#123;
                            (money) => &#123;
                                return (
                                    <span class="hljs-tag"><<span class="hljs-name">HouseContext.Consumer</span>></span>
                                        &#123;
                                            (house) => &#123;
                                                return (
                                                    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                                                        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;money&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                                                        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;house&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                                                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                                                )
                                            &#125;
                                        &#125;
                                    <span class="hljs-tag"></<span class="hljs-name">HouseContext.Consumer</span>></span>
                                )
                            &#125;
                        &#125;
                    <span class="hljs-tag"></<span class="hljs-name">MoneyContext.Consumer</span>></span></span>
                )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就完成数据的展示了！yeah.</p></div>  
</div>
            