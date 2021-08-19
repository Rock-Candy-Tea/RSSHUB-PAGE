
---
title: 'React全家桶学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3640'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 01:50:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=3640'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"></h3>
<blockquote>
<p>用了大概12天时间对react有了一个初步的认识，相比vue感觉还是复杂一些尤其是redux，学的时候挺懵逼的.....可能是我太菜了。建议学react的小伙伴还是要结合官方文档，而且不要看一些很老的视频，尤其是16版本以前的，因为那时候还没有hooks，对于菜鸡的我来说hooks真是救命了！</p>
<p>本人参考的是coderwhy老师的视频，感觉讲的很好还有源码的细节等等。只是自己的吸收能力有点弱，还需要多巩固一下！</p>
<p>学了有半年多的前端，这是随手写的笔记，很多地方肯定还有不足，希望大佬们多指正</p>
<p>如果这篇文章能帮到你，那写的也有点意义了哈哈哈哈</p>
</blockquote>
<h3 data-id="heading-1">1、Hello React</h3>
<p>​ <strong>UI = render(state)</strong></p>
<p>图片加载优化：后端传图片的时候要传大小，虽然样式能改，但是大图消耗性能</p>
<p>命令式编程：每做一个操作，都会给计算机一步步的命令去执行</p>
<p>声明式编程：</p>
<h4 data-id="heading-2">1.1 JSX语法</h4>
<p>​ 注意事项：使用jsx代码，必须在script必须添加text/babel</p>
<p>​ render函数里只能有一个根节点，JSX语法也是，外层包一个小括号</p>
<p>​ 单标签必须以/>结尾，/不能省略</p>
<p>​ 写注释必须在 &#123;/</p>
<p>我是一段注释</p>
<p>/&#125; 里</p>
<p>​ 在&#123;&#125;里不能显示的属性：null、undefined、boolean都不显示</p>
<p>​ 如果想显示null可用tostring()，或者在后面加一个空字符串</p>
<p>​ 也不能在&#123;&#125;里放一个对象</p>
<p>​ 可以放运算符表达式列入字符串拼接 加减乘除</p>
<p>​ 可以放 三元表达式</p>
<p>​ 可以放函数表达式，逻辑与或 都可以</p>
<h4 data-id="heading-3">1.2 JSX绑定属性</h4>
<p>​ 可以在标签的属性也用&#123;&#125;来绑定</p>
<p>​ 但是不能给标签加class，因为js里有class怕冲突，所以必须要写成className</p>
<p>​ 如果要动态添加class属性，需要用&#123;&#125;，如果加样式需要再嵌套一个对象</p>
<pre><code class="copyable"><div className=&#123;"box title" + (this.state.active ? "active" : "")&#125;>

<div style=&#123;&#123;color:"red", fontSize:"50px"&#125;&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">1.3 JSX绑定事件</h4>
<p>react内部使用按钮点击，自身会绑定一个call(undefined)，所以直接在render用this找方法是不行的，必须用Bind call apply来绑定this。</p>
<p>第一种方案：在constructor里直接绑定this this.click = this.click.bind(this)</p>
<p>第二种方案：箭头函数，永远不绑定this，会自己找上层作用域，就是类组件本身</p>
<p>第三种方案(推荐)：直接传入一个箭头函数，在箭头函数里调用需要执行的函数</p>
<p>函数传参就使用第三种方案，在() => &#123;onclick(参数)&#125;</p>
<h4 data-id="heading-5">1.4 条件渲染</h4>
<p>第一种方案可以用if else判断</p>
<p>第二种用三元表达式</p>
<p>第三种用逻辑与&&</p>
<h4 data-id="heading-6">1.5 JSX本质</h4>
<p>通过babel把 React.createElement("div",&#123; className:"header"&#125;, "hello world")转为JSX，所以写JSX代码必须需要依赖babel</p>
<h4 data-id="heading-7">1.6 虚拟DOM的创建过程</h4>
<p>React.createElement的本质最终创建出一个对象，利用这个对象组成了一个JS对象树，Rea.crea里面又有很多其他Rea.crea对象。</p>
<p>再通过render函数映射到真实DOM</p>
<h4 data-id="heading-8">1.7 为什么使用虚拟DOM</h4>
<p>很难跟踪状态发生的改变</p>
<p>操作真实DOM性能很低：document.createElement本身创建的是一个非常复杂的对象</p>
<p>而且会引起浏览器的回流和重绘</p>
<p>例如：真实DOM在ul后面加五个li，循环遍历，那就要操作5次真实DOM。</p>
<h3 data-id="heading-9">2、React组件化</h3>
<p>组件化思想：树结构</p>
<p>类组件：不能写大写的标签，大写的会被当成组件。</p>
<p>​ 类组件必须继承React.Component</p>
<p>​ 类组件必须实现render函数</p>
<h4 data-id="heading-10">2.1 组件传参</h4>
<p>函数式组件用 ChildCpn.propTypes=&#123;name:PropTypes.string.isRequired&#125;来声明参数类型，</p>
<p>​ 用 ChildCpn.defaultProps =&#123;name:"why"&#125;来设置默认值</p>
<p>类组件用内部的 static propTypes=&#123;&#125; 和 static defaultProps=&#123;&#125;来声明和设置默认</p>
<p>如果声明了参数类型，但没有传入，可能会因为NaN报错，react里的属性&#123;&#125;里不允许有NaN</p>
<p>组件通信发送自定义事件时要注意普通函数this指向的是undefined，三种方法：</p>
<p>使用箭头函数，会自己寻找this</p>
<p>在子组件标签里传递事件使用箭头函数 &#123;e => this.increment()&#125;</p>
<p>使用bind绑定this</p>
<h4 data-id="heading-11">2.2 跨组件通信</h4>
<p>第一种：一层一层往上传，用props，在子组件标签后面&#123;...props&#125;</p>
<p>第二种：1.1、使用context，先创建context实例</p>
<pre><code class="copyable">const UserContext = React.createContext(&#123;  nickname: "aaaa", //默认值  level: -1 //默认值&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 1.2、使用provider API将需要传值的子组件放里面，相当于一个大容器</p>
<pre><code class="copyable"><UserContext.Provider value=&#123;this.state&#125;>   <Profile /></UserContext.Provider>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 1.3、子组件使用自身contextType API来指向需要传值的context，取值直接用this.context</p>
<pre><code class="copyable">ProfileHeader.contextType = UserContext;<h2>用户昵称: &#123;this.context.nickname&#125;</h2><h2>用户等级: &#123;this.context.level&#125;</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 2.1、以上是类组件，函数式组件就需要，再子组件需要context的地方包一层consumer，返回值是一个回调 ,就不需要contextType了。</p>
<pre><code class="copyable">function ProfileHeader() &#123;  return (    <UserContext.Consumer>      &#123;        value => &#123;          return (            <div>              <h2>用户昵称: &#123;value.nickname&#125;</h2>              <h2>用户等级: &#123;value.level&#125;</h2>            </div>          )        &#125;      &#125;    </UserContext.Consumer>  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 2.2、多个context嵌套调用的话，就先创建context，然后在App组件里再包一层就行了，需要调用值的子组件需要再返回一个回调。</p>
<pre><code class="copyable"> return (    <UserContext.Consumer>      &#123;        value => &#123;          return (            <ThemeContext.Consumer>              &#123;                theme => &#123;                  return (                    <div>                      <h2 style=&#123;&#123;color: theme.color&#125;&#125;>用户昵称: &#123;value.nickname&#125;</h2>                      <h2>用户等级: &#123;value.level&#125;</h2>                      <h2>颜色: &#123;theme.color&#125;</h2>                    </div>                  )                &#125;              &#125;            </ThemeContext.Consumer>          )        &#125;      &#125;    </UserContext.Consumer>  )
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3、setState解析</h3>
<h4 data-id="heading-13">3.1 setState异步更新</h4>
<p>​ 1、可以显著提升性能，因为会调用很多setstate，每次render函数会频繁调用，效率很低</p>
<p>​ 最好是应该获取到多个更新，放入到一个队列，之后进行批量更新</p>
<p>​ 2、如果同步更新state，但是还没有执行render函数（虚拟DOM和Diff算法会慢一点），那么state和props不能保持同步。</p>
<p>​ 3、如果想拿到异步结果，setState第二个参数是一个回调，可以在里面拿，类似于nextTick</p>
<p>​ 4、执行完setState完，会执行componentDidUpdate生命周期，里面也可也拿更新的数据</p>
<h4 data-id="heading-14">3.2 setState同步更新</h4>
<p>​ 1、放到定时器里会变成同步</p>
<p>​ 2、放到componentDidMount() 里原生DOM会变成同步，以及合成事件</p>
<h4 data-id="heading-15">3.3 数据合并</h4>
<p>​ 原理是 使用object.assign(&#123;&#125;,&#123;this.state&#125;,&#123;this.setState&#125;)，更新属性会覆盖没有的不会清除</p>
<p>​ setState是会合并的，调用多次会合并成一次</p>
<p>​ setState((prevState, props) => &#123;return &#123;&#125; &#125;)，就不会合并，会累加</p>
<h4 data-id="heading-16">3.4 组件嵌套的render调用</h4>
<p>​ 一般情况下，父组件内有多个子组件，但是调用其中一个子组件的方法，比如按钮点击执行setState，那么整个父组件会重新调用render，里面每个子组件都会重新执行render，浪费性能</p>
<h4 data-id="heading-17">3.5 ShouldComponentUpdate</h4>
<p>​ 该生命周期可以阻断页面的render重新调用，使用if判断，直接返回true或false</p>
<pre><code class="copyable">  shouldComponentUpdate(nextProps, nextState) &#123;    if (this.state.counter !== nextState.counter)&#123;return true;&#125;    return false;  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 但是每个组件去调用，里面还有if，如果有十个属性值改变，冗余代码太多。</p>
<h4 data-id="heading-18">3.6 PureComponent</h4>
<p>​ 在类组件里，所以类组件继承时候，不再继承Component，而是继承PureComponent，里面会自动调用shouldComponentUpdate生命周期</p>
<p>​ PureComponent的原理是根据类组件本身是否依赖和改变props和state，如果改变return true，重新渲染render，反之亦然</p>
<p>​ 不要在shouldComponentUpdate做深层比较，非常消耗性能，做浅层比较就可以</p>
<h4 data-id="heading-19">3.7 Memo</h4>
<p>​ 函数式组件里，memo是一个函数也是一个高阶组件(可以对其他组件操作)，使用方法</p>
<pre><code class="copyable">const MemoHeader = memo(函数组件)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 本质和PureComponent操作一样，根据函数式组件本身是否依赖和改变props和state，如果改变return true，重新渲染render，反之亦然</p>
<h4 data-id="heading-20">3.8 SetState不可变的力量</h4>
<p>​ 1、不要这样做</p>
<pre><code class="copyable">    const newData = &#123;name:"Tom", age:33&#125;    this.state.friends.push(newData)    this.setState(&#123;friends:this.state.friends&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 2、推荐做法</p>
<pre><code class="copyable">    const newFriends = [...this.state.friends]    newFriends.push(&#123;name:"tom" , age:33&#125;)    this.setState(&#123;friends:newFriends&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原因是因为，第二种重新开辟了一个内存空间，有点类似于深拷贝，此时shouldComponentUpdate在比较的时候，是两个对象在比较，如果是第一种，那么是两个相同的对象比较。</p>
<h3 data-id="heading-21">4、高阶组件</h3>
<p>高阶组件本质是一个函数，参数是一个组件，相当于包装、强化组件，增强复用性，可以应用在登录授权、生命周期劫持得到组件执行时间等等。</p>
<p>内部render内容一般为，传过来的组件</p>
<pre><code class="copyable">render() &#123; return <WrappedComponent &#123;...this.props &#125;/>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">4.1 Ref转发</h4>
<p>类组件：通过ref来传递参数，使用createRef函数通过props接受，在父组件的constructor里去声明</p>
<pre><code class="copyable">this.titleRef = createRef()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件：通过forwardRef函数（本质是一个高阶组件，所以返回值是一个组件），调用时会多一个参数ref，就可以在标签里使用ref</p>
<pre><code class="copyable">const Profile = forwardRef(function(props, ref) &#123;  return <p ref=&#123;ref&#125;>Profile</p>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">4.2 Portal的使用</h4>
<p>把当前组件可以渲染当前任意一个位置，默认挂载root上</p>
<pre><code class="copyable">class Modal extends PureComponent &#123;  render() &#123;    return ReactDOM.createPortal(      this.props.children,      document.getElementById("modal")    )  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">4.3 Fragments的使用</h4>
<p>可以把多余没用的div节点在删掉，如果fragment没有属性就可以直接省略，但是有的话不能省略</p>
<pre><code class="copyable">return ( <Fragment key=&#123;item.name&#125;>   <div>&#123;item.name&#125;</div>   <p>&#123;item.age&#125;</p>  <hr/> </Fragment>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">4.4 StrictMode的使用</h4>
<p>开启严格模式，为后代元素触发额外的检查和警告</p>
<p>​ 1、识别不安全的生命周期</p>
<p>​ 2、使用过时的ref API 例如字符串声明ref="title"的形式</p>
<p>​ 3、constructor会被调用两次，找副作用</p>
<p>​ 4、使用早期废弃的findDOMNode方法，后面ref已经代替</p>
<p>​ 5、检测过时的context API</p>
<h3 data-id="heading-26">5、React中的css样式</h3>
<p>​ 1、可以编写局部css，具备自己的作用域，不会污染其他组件</p>
<p>​ 2、编写动态的css，例如根据不同布尔值显示不同样式</p>
<h4 data-id="heading-27">5.1 内联样式</h4>
<p>​ 优点：样式不会冲突，可以获取state中的状态</p>
<p>​ 缺点：需要驼峰标识、没代码提示，代码冗余，不能写伪类元素</p>
<h4 data-id="heading-28">5.2 普通css</h4>
<p>​ 写单独的css文件，然后直接引入使用</p>
<p>​ 缺点：容易产生冲突的覆盖、为了不冲突需要写多个选择器去选中一个className</p>
<h4 data-id="heading-29">5.3 Css modules</h4>
<p>​ 声明css文件为style.module.css，组件内部引入之后在render里className=&#123;&#125;当成对象直接取对应的css类名，类名必须是驼峰</p>
<p>​ 缺点：难以获取动态样式，比如在state里有动态的 color，还需要结合内联样式</p>
<h4 data-id="heading-30">5.4 Css in JS（推荐）</h4>
<h4 data-id="heading-31">5.5 Styled-components</h4>
<p>​ 先引入，使用标签模板字符串，返回的是一个组件，直接用组件代替对应的标签就可以了</p>
<pre><code class="copyable">const HYButton = styled.button`  padding: 10px 20px;  border-color: red;  color: red;`

const HYPrimaryButton = styled(HYButton)`  color: #fff;  background-color: green;`

const HYInput = styled.input.attrs(&#123;  placeholder: "coderwhy",  bColor: "red"&#125;)`  background-color: lightblue;  border-color: $&#123;props => props.bColor&#125;;  color: $&#123;props => props.color&#125;;`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 使用主题属性，先引入，在父组件定义，然后子组件可以通过props直接获取到</p>
<pre><code class="copyable"><ThemeProvider theme=&#123;&#123;themeColor: "red", fontSize: "30px"&#125;&#125;/>​export const TitleWrapper = styled.h2`  text-decoration: underline;  color: $&#123;props => props.theme.themeColor&#125;;  font-size: $&#123;props => props.theme.fontSize&#125;;`
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">5.6 Classnames库</h4>
<p>可以类似于vue绑定动态属性，只要返回值是false都不会添加到标签属性中</p>
<pre><code class="copyable"> const &#123;isActive&#125; = this.state; const isBar = false; const errClass = "error"; const warnClass = 10; //传数字的话会直接添加转化为字符串 添加一个 10的类名​ <h2 className=&#123;"foo bar active title"&#125;>我是标题1</h2> <h2 className=&#123;"title" + (isActive ? " active": "")&#125;>我是标题2</h2> <h2 className=&#123;["title", (isActive ? "active": "")].join(" ")&#125;>我是标题3</h2>​ &#123;/* classnames库添加class */&#125;  <h2 className="foo bar active title">我是标题4</h2>  <h2 className=&#123;classNames("foo", "bar", "active", "title")&#125;>我是标题5</h2>  <h2 className=&#123;classNames(&#123;"active": isActive, "bar": isBar&#125;, "title")&#125;>我是标题6</h2>  <h2 className=&#123;classNames("foo", errClass, warnClass, &#123;"active": isActive&#125;)&#125;>我是标题7</h2>  <h2 className=&#123;classNames(["active", "title"])&#125;>我是标题8</h2>  <h2 className=&#123;classNames(["active", "title", &#123;"bar": isBar&#125;])&#125;>我是标题9</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">6、AntDesign组件库</h3>
<p>craco：配置修改antd的默认蓝色主题样式，在craco.config.js里改webpack配置</p>
<p>​ 引入样式文件要换成less</p>
<pre><code class="copyable">const CracoLessPlugin = require('craco-less');const path = require("path");const resolve = dir => path.resolve(__dirname, dir);​module.exports = &#123;  plugins: [    &#123;      plugin: CracoLessPlugin,      options: &#123;        lessLoaderOptions: &#123;          lessOptions: &#123;            modifyVars: &#123; '@primary-color': '#1DA57A' &#125;,            javascriptEnabled: true,          &#125;,        &#125;,      &#125;,    &#125;  ],  webpack: &#123;    alias: &#123;      "@": resolve("src"),      "components": resolve("src/components")    &#125;  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">7、Css过渡动画</h3>
<pre><code class="copyable">#### 7.1  CssTransition
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 先引入，在需要使用动画的标签外面包一层，里面的timeout不能省略，再根据className，写对应的样式，分为三个，enter是进入，active是执行中，end是结束后，unmountOnExit是隐藏时卸载。如果需要第一次加载组件需要动画时，需要添加appear属性，并且在css写对应的动画。</p>
<pre><code class="copyable">import &#123; CSSTransition &#125; from 'react-transition-group';

<CSSTransition in=&#123;isShow&#125;               classNames="card"               timeout=&#123;5000&#125;               unmountOnExit=&#123;true&#125;              appear/>

.card-enter, .card-appear &#123;  opacity: 0;  transform: scale(.6);&#125;​.card-enter-active, .card-appear-active &#123;  opacity: 1;  transform: scale(1);  transition: opacity 300ms, transform 300ms;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">7.2 SwitchTransition</h4>
<p>​ 这是切换效果，cssTransition是直接用来显示和隐藏。</p>
<p>​ 一般用法为，在cssTransition外面包一层SwitchTransition。out-in是先隐藏再出现，而且这里面in换成了key，记得也要有timeout，外面的timeout属性是切换class需要的时间，css里的timeout才是决定动画执行时间</p>
<pre><code class="copyable"><SwitchTransition mode="out-in">          <CSSTransition key=&#123;isOn ? "on": "off"&#125;                         classNames="btn"                         timeout=&#123;1000&#125;>            <button onClick=&#123;e => this.setState(&#123;isOn: !isOn&#125;)&#125;>              &#123;isOn ? "on": "off"&#125;            </button>          </CSSTransition></SwitchTransition>

.btn-enter &#123;  opacity: 0;  transform: translateX(100%);&#125;​.btn-enter-active &#123;  opacity: 1;  transform: translateX(0);  transition: opacity 1000ms, transform 1000ms;&#125;​.btn-exit &#123;  opacity: 1;  transform: translateX(0);&#125;​.btn-exit-active &#123;  opacity: 0;  transform: translateX(-100%);  transition: opacity 1000ms, transform 1000ms;&#125;​
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">7.3 TransitionGroup</h4>
<p>主要做给某一组元素添加动画，例如列表，用法是在最外层把div换成TransitionGroup组件。</p>
<p>​ 注意：如果是循环必须给一个key，不添加会因为diff算法，会把class添加到diff算法比较后，删除的位置。例如，三个数据删除第一个，diff算法比较后前两个能找到对应的值，最后一个被删掉，所以会给最后一个添加class动画。</p>
<pre><code class="copyable"><TransitionGroup>          &#123;            this.state.names.map((item, index) => &#123;              return (                <CSSTransition key=&#123;item&#125;                  timeout=&#123;500&#125;                  classNames="item">                  <div>                    &#123;item&#125;                    <button onClick=&#123;e => this.removeItem(index)&#125;>-</button>                  </div>                </CSSTransition>)&#125;)          &#125;</TransitionGroup><button onClick=&#123;e => this.addName()&#125;>+name</button>

.item-enter &#123;opacity: 0;transform: scale(.6);&#125;.item-enter-active &#123;opacity: 1;transform: scale(1);transition: opacity 300ms, transform 300ms;&#125;.item-enter-done &#123; color: red;&#125;​.item-exit &#123;opacity: 1;transform: scale(1);&#125;.item-exit-active &#123;opacity: 0;transform: scale(.6); transition: opacity 300ms,transform 300ms&#125;.item-exit-done &#123;opacity: 0;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">8、Redux状态管理</h3>
<h4 data-id="heading-38">8.1 JavaScript纯函数</h4>
<p>​ 确定的输入，一定会产生确定的输出，例如输入5，返回得到10，不能改变必须是10</p>
<p>​ 函数在执行过程中，不能产生副作用，例如传入一个对象，不能对对象进行修改</p>
<pre><code class="copyable">    function sum(num1, num2) &#123;      return num1 + num2;    &#125;​    sum(20, 30);    sum(20, 30);  //这是一个纯函数

let foo = 10;    function add(num) &#123;      return foo + num;    &#125;​    add(5); // 15    foo = 20;    add(5); // 25 //不是一个纯函数，每次输入是5但是值变了        //能否将上面函数改成一个纯函数？    const bar = 10;    function add2(num) &#123;      return bar + num;    &#125;​    bar = 11;

    const baz = &#123;      count: 10    &#125;    function add3(num) &#123;      return baz.count + num    &#125;​    baz.count = 20; //不是一个纯函数，baz里的值能改，输入相同值结果可能不一样
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>所有React组件都必须像纯函数一样保护他们的Props不被更改</strong></p>
<p>比如说，父组件用props给子组件传数据，子组件只能用，但是不能改例如props.info.name="why"</p>
<h4 data-id="heading-39">8.2 Redux的三大原则</h4>
<p>​ 单一数据源：整个应用程序state都被存储在一个object tree中</p>
<p>​ State是只读的：唯一修改State的方法一定是触发了action，不要在其他地方改</p>
<p>​ 使用纯函数来执行修改：通过reducer将旧state和 action联系在一起，改变时返回新的state</p>
<h4 data-id="heading-40">8.3 基本使用流程</h4>
<p>​ 1、定义一个唯一的store的库，里面的index.js为唯一出口，这里做的事是把总的仓库导入出去，别的组件想使用时可以直接导入</p>
<pre><code class="copyable">import &#123;createStore&#125; from 'redux'import reducer from './reducer.js'​const store = createStore(reducer)​export default store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 2、声明对应的reducer文件，先声明默认的state值，里面的reducer方法是为了根据不同的派发事件action的类型type来执行对应的操作（例如对数据的增删改查，类似于回调），记得要用拷贝的方式保证纯函数。</p>
<pre><code class="copyable">const defaultState =&#123;  counter: 0&#125;​function reducer(state = defaultState, action)&#123;  switch(action.type)&#123;    case ADD_NUMBER:      return &#123;...state, counter: state.counter +action.num&#125;;    case SUB_NUMBER:      return &#123;...state, counter: state.counter -action.num&#125;;    default:      return state  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 3、在actionCreators文件里，根据类型，声明对应的派发事件action，记得要返回的是对象</p>
<pre><code class="copyable">export const addAction = (num) => &#123;  return &#123;    type:ADD_NUMBER,    num  &#125;&#125;​export const subAction = num => (&#123;  type:SUB_NUMBER,  num&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 4、然后在需要用的组件里，直接派发定义好的事件，用store.dispatch，同时要在加载完的声明周期里用store.subscribe来监听派发事件的结果</p>
<pre><code class="copyable">store.subscribe(() => &#123;  console.log(store.getState());&#125;)store.dispatch(addAction(10))store.dispatch(addAction(10))store.dispatch(subAction(15))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-41">8.4 在React中使用Redux</h4>
<p>​ 1、在需要用的组件引入redux和actioncreator，在组件内部state临时保存store的state</p>
<pre><code class="copyable">    this.state = &#123;      counter: store.getState().counter    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 2、声明函数里面写对应的action事件用dispatch派发，这些action是已经在actioncreator定义好的</p>
<p>​ 3、派发完事件后会在reducer根据类型执行对应的方法</p>
<p>​ 4、在didmount声明周期监听state的改变</p>
<pre><code class="copyable"> componentDidMount()&#123;    this.unsubscribe = store.subscribe(() => &#123;      this.setState(&#123;        counter:store.getState().counter      &#125;)    &#125;)  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 5、在willunmount生命周期取消订阅监听</p>
<pre><code class="copyable">  componentWillUnmount()&#123;    this.unsubscribe()  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-42">8.5 后端数据存到Redux思路</h4>
<p>​ 前提：先封装对应的react-redux</p>
<pre><code class="copyable">import &#123; Provider &#125; from 'react-redux'ReactDOM.render(  <Provider store=&#123;store&#125;>    <App />  </Provider>,  document.getElementById('root'));  //在总出口文件添加context，传入store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 需要使用的地方引入以及添加connect函数的高阶组件</p>
<pre><code class="copyable">import &#123; connect &#125; from 'react-redux';​export default connect(mapStateToProps, mapDispatchToProps)(Home);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 1、先用axios在componentDidMount里请求数据</p>
<p>​ 2、在reducer里的默认数据里，临时保存需要到存store的数据</p>
<p>​ 3、在constants里声明action的type变量名</p>
<p>​ 4、在actionCreators里先导入tyoe变量名，再设置对应的action函数，记得返回的是一个对象</p>
<p>​ 5、在reducer里，根据action的type添加case，返回的是纯函数</p>
<p>​ 6、在请求数据的组件里，引入刚刚声明好的action</p>
<p>​ 7、在mapDispatchToProps函数返回的对象里添加映射，添加dispatch里面是派发的事件</p>
<pre><code class="copyable">  changeBanners(banners) &#123;    dispatch(changeBannersAction(banners));  &#125;,  changeRecommends(recommends) &#123;    dispatch(changeRecommendAction(recommends));  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 8、在componentDidMount里存储用axios请求到的数据</p>
<pre><code class="copyable">  this.props.changeBanners(data.banner.list);  this.props.changeRecommends(data.recommend.list);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 9、此时数据已经存到store里的state了，在另一个组件就可以使用</p>
<pre><code class="copyable">const mapStateToProps = state =>（&#123;    banners: state.banners,    recommends: state.recommends&#125;）
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-43">8.6 Redux-thunk中间件</h4>
<p>​ 请求数据也是一个状态管理的地方所以最好放到redux里，在dispatch和reducer之间添加一个中间件，目的是让dispatch直接返回一个函数而不是对象</p>
<p>​ 1、在创建store时传入应用了middleware的enhance函数 2、通过applyMiddleware来结合多个Middleware, 返回一个enhancer； 3、将enhancer作为第二个参数传入到createStore中；</p>
<pre><code class="copyable">const storeEnhancer = applyMiddleware(thunkMiddleware, sagaMiddleware);const store = createStore(reducer, storeEnhancer);

// redux-thunk中定义的action函数export const getHomeMultidataAction = (dispatch, getState) => &#123;  axios(&#123;    url: "http://123.207.32.32:8000/home/multidata",  &#125;).then(res => &#123;    const data = res.data.data;    dispatch(changeBannersAction(data.banner.list));    dispatch(changeRecommendAction(data.recommend.list));  &#125;)&#125; //先在组件派发，再到请求数据里派发，然后找对应的reducer进行处理

  componentDidMount() &#123;    this.props.getHomeMultidata();  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要用redux-devtools，先引入compose，需要把强化后的中间件做一个合并</p>
<pre><code class="copyable">const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__(&#123;trace: true&#125;) || compose;

const store = createStore(reducer, composeEnhancers(storeEnhancer));
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-44">8.7 Redux-saga中间件</h4>
<pre><code class="copyable">import createSagaMiddleware from 'redux-saga' //引入函数

const sagaMiddleware = createSagaMiddleware() //创建中间件

const storeEnhancer = applyMiddleware(thunkMiddleware, sagaMiddleware)//应用中间件

sagaMiddleware.run(saga)  //拦截action，传入生成器函数

function* mySaga() &#123;  // takeLatest takeEvery区别:  // takeLatest: 依次只能监听一个对应的action  // takeEvery: 每一个都会被执行  yield all([    takeLatest(FETCH_HOME_MULTIDATA, fetchHomeMultidata),    // takeLatest(ADD_NUMBER, fetchHomeMultidata),  ]);&#125;  //监听对应的action type，监听到会执行第二个参数 生成器函数

function* fetchHomeMultidata(action) &#123;  const res = yield axios.get("http://123.207.32.32:8000/home/multidata");  const banners = res.data.data.banner.list;  const recommends = res.data.data.recommend.list;  // yield put(changeBannersAction(banners));  // yield put(changeRecommendAction(recommends));  yield all([    yield put(changeBannersAction(banners)),    yield put(changeRecommendAction(recommends))  ])&#125; //生成器函数内具体的逻辑
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-45">8.8 CombineReducer</h4>
<p>如果我们自己封装的reducer，返回一个对象，里面为子reducer</p>
<p>缺点在于如果传过来的action值里的state没有更改，那还要重新return一个相同的新的子reducer合并的对象，浪费性能。</p>
<p>combineReducer的好处就是会判断action，如果是有数据改变的时候返回新的对象，如果数据没改变就返回原来的对象</p>
<pre><code class="copyable">const reducer = combineReducers(&#123;  counterInfo: counterReducer,  homeInfo: homeReducer&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-46">8.9 单向数据流</h4>
<p>vue和react都有单向数据流，指的是通过props进行数据的传递。</p>
<p>ui视图区域 -> 发送一个事件 -> 发送dispatch执行action ->修改state ->修改ui</p>
<p>redux中的单向数据流：</p>
<p>ui组件发生事件 -> dispatch一个action -> action传递给reducer返回新的state ->state的改变引起ui的改变</p>
<p>不能跨级传递数据，例如直接store.getState() = newValue 这是不符合单向数据流的规范</p>
<h3 data-id="heading-47">9、React路由</h3>
<p>第一阶段：后端路由</p>
<p>​ 一个页面有自己对应的网址, 也就是URL. URL会发送到服务器, 服务器会通过正则对该URL进行匹配, 并且最后交给一个Controller进行处理. Controller进行各种处理, 最终生成HTML或者数据, 返回给前端. 这就完成了一个IO操作. 上面的这种操作, 就是后端路由. 当我们页面中需要请求不同的路径内容时, 交给服务器来进行处理, 服务器渲染好整个页面, 并且将页面返回给客户顿. 这种情况下渲染好的页面, 不需要单独加载任何的js和css, 可以直接交给浏览器展示, 这样也有利于SEO的优化.</p>
<p>第二阶段：前后端分离</p>
<p>​ 每次请求涉及到的静态资源都会从静态资源服务器获取； 这些资源包括HTML+CSS+JS，然后在前端对这些请求回来的资源进行渲染；</p>
<p>​ 然后在另一台API服务器上写接口请求对应的数据，拿到数据做一个展示就可以了</p>
<p>第三阶段：单页面富应用</p>
<p>​ 整个Web应用只有实际上只有一个页面，当URL发生改变时，并不会从服务器请求新的静态资源； 而是通过JavaScript监听URL的改变，并且根据URL的不同去渲染新的页面； 如何可以应用URL和渲染的页面呢？前端路由 前端路由维护着URL和渲染页面的映射关系； 路由可以根据不同的URL，最终让我们的框架（比如Vue、React、Angular）去渲染不同的组件；</p>
<h4 data-id="heading-48">9.1 前端路由的原理</h4>
<p>​ 1、改变URL，但是页面不要强制刷新（a元素不行）</p>
<p>​ 2、自己来监听URL的改变，并且改变之后自己改变页面的内容</p>
<p>hash路由</p>
<pre><code class="copyable"> window.addEventListener("hashchange", () => &#123;      switch (location.hash) &#123;        case "#/home":          routerViewEl.innerHTML = "首页";          break;        case "#/about":          routerViewEl.innerHTML = "关于";          break;        default:          routerViewEl.innerHTML = "";&#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>history路由</p>
<pre><code class="copyable"> el.addEventListener("click", e => &#123;        e.preventDefault(); //阻止默认事件        const href = el.getAttribute("href");        history.pushState(&#123;&#125;, "", href);        urlChange();//点击改变URL&#125;)  //history接口六种模式改变URL不会刷新页面

    // 执行返回操作时, 依然来到urlChange    window.addEventListener('popstate',urlChange);    // 监听URL的改变    function urlChange() &#123;      switch (location.pathname) &#123;        case "/home":          routerViewEl.innerHTML = "首页";          break;        case "/about":          routerViewEl.innerHTML = "关于";          break;        default:          routerViewEl.innerHTML = "";    &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-49">9.2 switch组件</h4>
<p>默认情况下，react-router中只要是路径被匹配到的Route对应的组件都会被渲染；但是实际开发中，我们往往希望有一种排他的思想：只要匹配到了第一个，那么后面的就不应该继续匹配了；这个时候我们可以使用Switch来将所有的Route进行包裹即可</p>
<p>NavLink是在active情况下是否显示特殊的内容，link是要加额外的active属性</p>
<h4 data-id="heading-50">9.3 按钮点击路由跳转</h4>
<p>如果是app的子组件，因为这个组件是app通过路由创造出的组件所以有history,push,go等属性，子组件可以直接通过this.props.history.push可以直接拿到history属性然后跳转</p>
<p>但是APP不行，因为APP外层是index.js是没有路由来帮APP创造组件，此时需要引入withRouter</p>
<p>并且在最外层包Browser组件，才能调用this.props.history</p>
<h3 data-id="heading-51">10、React Hooks</h3>
<h4 data-id="heading-52">10.1 useState</h4>
<p>​ 对于简单的state，直接用解构赋值定义数据</p>
<p>​ 注意：如果想要添加state的value，不能直接push，必须拷贝，因为usestate会判断state是否更新来渲染render，就跟setState类似</p>
<pre><code class="copyable">      <button onClick=&#123;e => setFriends([...friends, "tom"])&#125;>添加朋友</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-53">10.2 useEffect</h4>
<p>代替类组件里，一些生命周期的执行</p>
<pre><code class="copyable">  useEffect(() => &#123;    console.log("订阅事件"); //类似于componentDidMount生命周期    return () => &#123;      console.log("取消订阅"); //类似于componentWillUnmount    &#125;  &#125;,[]) //第二个参数为数组，为了优化
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般情况下，只要组件渲染或者更新，useEffect就会重新执行一遍，但有些请求我们只需要执行一次就可以了类似于订阅事件、网络请求</p>
<p>第二个参数为数组，里面可以放想要处理的state，只是在该state执行后才会重新调用该useEffect</p>
<h4 data-id="heading-54">10.3 useContext</h4>
<p>类组件可以通过 类名.contextType = MyContext方式，在类中获取context；多个Context或者在函数式组件中通过 MyContext.Consumer 方式共享context；</p>
<p>使用useContext后</p>
<pre><code class="copyable">export default function Cpn1(props) &#123;  const user = useContext(UserContext);  const theme = useContext(ThemeContext)  console.log(user, theme);  return (    <div>      <h2>ContextHookDemo</h2>      <h2>&#123;user.name&#125;</h2>      <h2>&#123;user.age&#125;</h2>    </div>  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：当组件上层最近的<Context.provider/> 更新时，该 Hook 会触发重新渲染，并使用最新传递给 MyContext provider 的 context value 值</p>
<h4 data-id="heading-55">10.4 useReducer</h4>
<p>在某些场景下，如果state的处理逻辑比较复杂，我们可以通过useReducer来对其进行拆分</p>
<p>或者这次修改的state需要依赖之前的state时，也可以使用，reducer是纯函数，所以要拷贝</p>
<pre><code class="copyable">export default function Home() &#123;  // const [count, setCount] = useState(0);  const [state, dispatch] = useReducer(reducer, &#123;counter: 0&#125;);​  return (    <div>      <h2>Home当前计数: &#123;state.counter&#125;</h2>      <button onClick=&#123;e => dispatch(&#123;type: "increment"&#125;)&#125;>+1</button>      <button onClick=&#123;e => dispatch(&#123;type: "decrement"&#125;)&#125;>-1</button>    </div>  )&#125;

export default function reducer(state, action) &#123;  switch(action.type) &#123;    case "increment":      return &#123;...state, counter: state.counter + 1&#125;;    case "decrement":      return &#123;...state, counter: state.counter - 1&#125;;    default:      return state;  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-56">10.5 useCallback</h4>
<p>useCallback实际的目的是为了对函数 进行性能的优化</p>
<p>使用场景：在将一个组件中的函数，传递给子组件进行回调使用时，使用useCallback对函数进行处理</p>
<pre><code class="copyable">  const increment1 = () => &#123;    console.log("执行increment1函数");    setCount(count + 1);  &#125;​  const increment2 = useCallback(() => &#123;    console.log("执行increment2函数");    setCount(count + 1);  &#125;, [count]);  

const HYButton = memo((props) => &#123;  console.log("HYButton重新渲染: " + props.title);  return <button onClick=&#123;props.increment&#125;>HYButton +1</button>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时increment2，值是相同的，memo浅层比较后组件就不会重新渲染</p>
<h4 data-id="heading-57">10.6 useMemo</h4>
<p>目的也是性能优化，针对于state，也可也是函数，主要看返回值</p>
<p>如果子组件引用着父组件的state，那么就算包层memo还是会重新渲染，因为每次传过来的对象是一个新值，此时需要用useMemo</p>
<pre><code class="copyable">  const info = &#123; name: "why", age: 18 &#125;;//子组件会重新渲染    const info = useMemo(() => &#123;    return &#123; name: "why", age: 18 &#125;;&#125;, []); //子组件不会重新渲染
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-58">10.7 useRef</h4>
<p>​ 1、操作DOM</p>
<pre><code class="copyable">const titleRef = useRef();  const inputRef = useRef();  const testRef = useRef();  const testRef2 = useRef();​  function changeDOM() &#123;    titleRef.current.innerHTML = "Hello World";    inputRef.current.focus();    console.log(testRef.current);    console.log(testRef2.current);  &#125;​
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​ 2、记录上一次的值，按钮点击完执行render后会调用useEffect，会把执行+10后的count传给numRef的current，改变numRef是不会重新渲染界面的</p>
<pre><code class="copyable">export default function RefHookDemo02() &#123;  const [count, setCount] = useState(0);​  const numRef = useRef(count);​  useEffect(() => &#123;    numRef.current = count;  &#125;, [count])​  return (    <div>      &#123;/* <h2>numRef中的值: &#123;numRef.current&#125;</h2>      <h2>count中的值: &#123;count&#125;</h2> */&#125;      <h2>count上一次的值: &#123;numRef.current&#125;</h2>      <h2>count这一次的值: &#123;count&#125;</h2>      <button onClick=&#123;e => setCount(count + 10)&#125;>+10</button>    </div>  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-59">10.8 useImperativeHandle</h4>
<p>通过useImperativeHandle可以只暴露固定的操作，而不是子组件把整个ref暴露给父组件： 通过useImperativeHandle的Hook，将传入的ref和useImperativeHandle第二个参数返回的对象绑定到了一起； 所以在父组件中，使用 inputRef.current时，实际上使用的是返回的对象； 比如我调用了 focus函数，甚至可以调用 printHello函数</p>
<pre><code class="copyable">const HYInput = forwardRef((props, ref) => &#123;  const inputRef = useRef();​  useImperativeHandle(ref, () => (&#123;    focus: () => &#123;      inputRef.current.focus();    &#125;  &#125;), [inputRef])​  return <input ref=&#123;inputRef&#125; type="text"/>&#125;)//上面是子组件export default function UseImperativeHandleHookDemo() &#123;  const inputRef = useRef();​  return (    <div>      <HYInput ref=&#123;inputRef&#125;/>      <button onClick=&#123;e => inputRef.current.focus()&#125;>聚焦</button>    </div>  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件调用focus实际上是调用子组件里useImperativeHandle的focus函数</p>
<h4 data-id="heading-60">10.9 useLayoutEffect</h4>
<p>当render渲染完，在这个hook里面执行完，再次判断state是否变化，如果变化就把最新的state进行渲染。</p>
<pre><code class="copyable">export default function EffectCounterDemo() &#123;  const [count, setCount] = useState(10);​  useEffect(() => &#123;    if (count === 0) &#123;      setCount(Math.random() + 200)    &#125;  &#125;, [count]);​  return (    <div>      <h2>数字: &#123;count&#125;</h2>      <button onClick=&#123;e => setCount(0)&#125;>修改数字</button>    </div>  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正常执行过程是：</p>
<p>​ 1、先点击修改数字把10set为0</p>
<p>​ 2、一旦调用render函数，且count改变那么就会执行useEffect hook</p>
<p>​ 3、判断count === 0 ，返回一个随机数</p>
<p>​ 4、调用render，count又改变又调用useEffect，但此时不是0，直接渲染页面渲染的结果是会先闪一下变成0，然后变为随机数，这时把useEffect换成useLayoutEffect，就不会闪一下的过程</p>
<h4 data-id="heading-61">10.10 自定义hook</h4>
<p>自定义Hook本质上只是一种函数代码逻辑的抽取，严格意义上来说，它本身并不算React的特性</p>
<p>声明的函数必须是use开头</p>
<h3 data-id="heading-62">11、Fiber作用</h3>
<p>Fiber可以理解为执行单元（碎片），浏览器要在一帧之内加载js单线程所有的任务，浏览器一有空余时间就会执行fiber碎片，根据函数requestIdleCallback()</p></div>  
</div>
            