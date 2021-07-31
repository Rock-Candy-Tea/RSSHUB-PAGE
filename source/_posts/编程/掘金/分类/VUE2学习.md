
---
title: 'VUE2学习'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7229'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 01:35:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=7229'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">MVVM模式</h1>
<p>视图与模型的双向绑定，即数据的变动会导致页面的变化。视图与模型分开。</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
view --> viewmodel --> model --> viewmodel --> view
</code></pre>
<h1 data-id="heading-1">vue初体验</h1>
<p>将其引入html中即可使用vue相关语法。</p>
<pre><code class="copyable"><!-- 开发环境版本，包含了有帮助的命令行警告 --> <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<!-- 生产环境版本，优化了尺寸和速度 --> <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">实例与数据绑定</h3>
<pre><code class="copyable">//app代表Vue实例
var app = new Vue(&#123;
    el:'#dom' // 页面存在的DOM元素
    data：&#123;&#125; // 数据绑定，值为一个js对象
&#125;)
console.log(app.$el,app.data对象的对象key) // 访问方式
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">插值和表达式</h3>
<p>双大括号&#123;&#123;&#125;&#125;是文本插值方法，可以实现数据双向绑定，可以使用三元运算计算结果，可以使用管道符计算结果&#123;&#123;data | formatDate&#125;&#125;（通过右边的函数计算结果）</p>
<h3 data-id="heading-4">标签属性（指令和事件）</h3>
<ul>
<li>v-html 直接输出html（需要xss处理）</li>
<li>v-pre 跳过编译过程</li>
<li>v-bind 动态更新html元素上的属性=语法糖 :html元素属性</li>
<li>
<ul>
<li>设置对象，可以动态切换值:class="&#123;'active':isActive&#125;"</li>
</ul>
</li>
<li>
<ul>
<li>设置方法，可以使用计算属性来getter值</li>
</ul>
</li>
<li>
<ul>
<li>设置数组，:class="[activecss,errorcss]"</li>
</ul>
</li>
<li>
<ul>
<li>:style="以上三种" 设置内联样式方法</li>
</ul>
</li>
<li>v-on 绑定事件监听器=语法糖 @js事件</li>
<li>v-cloak 会在实例结束编译时从绑定的html元素上移除</li>
<li>v-once 元素或组件只会渲染一次</li>
<li>key属性会使元素重新渲染</li>
<li>v-if/v-show show适合频繁切换条件，if适合不经常改变的场景</li>
<li>v-for 改变原始数组值的方法都会导致元素的重新渲染</li>
<li>@click 点击事件语法糖 如果有参数会将event传入方法。vue特殊变量$event用于访问原生dom事件</li>
<li>v-model 表单元素双向绑定数据，其值是表单的默认值；默认找的是它的value属性，如果没有就找text的值</li>
<li>v-model.lazy 只会在离开焦点时渲染</li>
<li>v-model.trim 去掉字符串头尾空格</li>
<li>:value 表单值的动态修改</li>
</ul>
<pre><code class="copyable"><div id ="app">
<select v-model ="selected">
<option : value ="&#123; number : 123 &#125;"> 123</option>
</select>
&#123;&#123; selec;ted.number &#125;&#125;
</div>
<script>
var app =new Vue (&#123;
el :'#app',
data : &#123;
   selected :''
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>@input 处理输入框</li>
</ul>
<h3 data-id="heading-5">自定义指令</h3>
<p>有如下钩子函数</p>
<ul>
<li>bind:只调用一次，可以用在初始化动作</li>
<li>inserted:被绑定元素插入父节点时调用</li>
<li>update:被绑定元素所在模板更新时调用</li>
<li>componentUpdate:被绑定元素所在模板完成一次更新周期时调用</li>
<li>unbind:只调用一次，指令与元素解绑时调用</li>
</ul>
<p>每个钩子函数有如下参数</p>
<ul>
<li>el 指令绑定的元素</li>
<li>binding（对象。以下面的demo为例）
<ul>
<li>name 指令名 test</li>
<li>value 指令绑定的值 message的值</li>
<li>oldValue 执行绑定前一个值</li>
<li>expression 绑定值的字符串形式 message</li>
<li>arg 传给指令的参数 msg</li>
</ul>
</li>
<li>vnode 虚拟节点</li>
<li>oldVnode 上一个虚拟节点</li>
</ul>
<pre><code class="copyable">// test是指令名，message的值就是指令值，
<div v-test:msg.a.b="message"></div>
Vue.directive('test',&#123;
    bind:function(el,binding,vnode)&#123;&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">修饰符</h3>
<p>它的值可以是一个方法，也可以为空。</p>
<pre><code class="copyable"><!--阻止冒泡-->
<a @click.stop ="handle"></a>
<!--提交事件不再重新加载-->
<a @submit.prevent ="handle"></a>
<a @click.stop.prevent ="handle"></a>
<!--添加事件侦听器时使用事件捕获模式-->
<div @click.capture ="handle ”> ... </div>
<!--只触发一次-->
<div @click.once ="handle ”> ... </div>
<!--回车时触发-->
<div @key.13 ="handle ”> ... </div>
<!--配置具体的按键。使用方式@keyup.fl-->
Vue.config.keyCodes.fl = 112;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">组件</h3>
<ol>
<li>关于组件的props类型验证有：String、Number、Boolean、Object、Array、Function。同时支持自定义验证validator:(data)=>&#123;return data>10&#125;</li>
</ol>
<pre><code class="copyable">//全局组件声明方式
<div id ="app" >
    <my-component maessage="父级"></my-component>
</div>
<script>
var child = &#123;template:'<div>局部</div>'&#125;
Vue.component ('my-component',&#123;
    props:['message'],与data return的区别就是，它的值来自于父级，而data的数据是属于它本身。它们的传递是单向的，只能是父到子
    template:'<div>test</div>',// template必须由一个html元素包裹
    data:()=>&#123;// 与实例的区别就是 组件data必须是函数，而且有返回值
        return &#123;...&#125;
    &#125;
)&#125;
var app = new Vue(&#123;
    el :'#app',
    components:&#123;'my-component':child&#125; // 局部组件声明方式
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>组件通信</li>
</ol>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
子1 --> 子2 --> 子1  -->父--> 子2 
</code></pre>
<ul>
<li>子组件通过$emit()来触发（创建）自定义组件上的定义事件</li>
<li>父组件通过$on()来监听子组件的事件</li>
<li>$refs在父组件中获取子组件索引集合</li>
<li>$parent在自定义组件中获取父组件集合</li>
</ul>
<pre><code class="copyable">//展示计数结果
<my-component @increase="getTotal"></my-component>

//my-component组件内方法定义
template:'<button @click="handleClick">+l</button>'
methods:&#123;
    handleIncrease:()=>&#123;
    //在自定义组件内部触发外部定义的increase事件
        this.$emit('increase',this.counter)
    &#125;
&#125;

//父类实例
var app = new Vue(&#123;
methods:&#123;
    getTotal:(total)&#123;&#125;
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一种总线模式的子父组件通信方式。即在父子的通信通过一个总线bus连接</p>
<pre><code class="copyable"><component-a></component-a>
//总线
var bus = new Vue();

template:'<button @click="handle"></button>',
methods:&#123;
    handle:()=>&#123;
    //通过bus触发on-message事件
        bus.$emit('on-message','信息')
    &#125;
&#125;

mounted:()=>&#123;
//监听on-message事件
    bus.$on('on-message',(data)=>&#123;&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">计算属性</h3>
<ul>
<li>处理复杂逻辑处理时，使用计算属性。即将数据与逻辑分开，只返回结果就可以了</li>
<li>计算属性可以在多个vue实例中交替使用，当一个实例数据发生变动时，另一个实例将发生变化</li>
<li>计算属性具有缓存性，数据发生时，它才会重新取值计算。而不是重新渲染，它就会被计算</li>
</ul>
<pre><code class="copyable">var app =new Vue(&#123;
    computed:&#123;
        processText:()=>&#123;&#125; // processText作为返回值，反应到页面中。默认使用getter方法。
     fullName:&#123;
         get:()=>&#123;&#125;,
         set:(value)=>&#123;&#125; //app.fullName将调用该处方法
     &#125;
    &#125;
&#125;)
console.log(processText)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">生命周期</h1>
<pre><code class="copyable">var app = new Vue(&#123;
    created:()=>&#123;&#125; //实例创建完成后调用。阶段完成了数据的观测等，但尚未挂载，$el还不可用。需要初始化处理一些数据时会比较有用
    mounted:()=>&#123;&#125; //el挂载到实例上后调用，一般我们的第一个业务逻辑会在这里开始
    beforeDestroy:()=>&#123;&#125;//实例销毁之前调用
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">slot(插槽)</h1>
<p>组件标签内部的内容称为插槽。该插槽定义在组件内容。插槽内容的获取可以使用<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>s</mi><mi>l</mi><mi>o</mi><mi>t</mi><mi>s</mi><mtext>对象。</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">slots对象。this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal">t</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">对</span><span class="mord cjk_fallback">象</span><span class="mord cjk_fallback">。</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>slots.default</p>
<pre><code class="copyable"><child-component>
// slot
    <template scope="props"> // props变量，用于获取插槽定义的数据
        <p slot="指定内容在插槽显示的位置">父内容</p>
        <p>&#123;&#123;props.msg&#125;&#125;</p> // props.msg=子内容
    </template>
</child-component>

Vue.component('child-component',&#123;
    template:'<div><slot msg="子内容"></slot>
    <slot name="指定内容在插槽显示的位置"></slot></div>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">vue-router用法</h1>
<p>关于使用html5的history路由模式时，webpack-dev-server也需要配置支持该模式<code>webpack-dev-server --open --history-api-fallback --config webpack.config.js</code></p>
<ol>
<li>
<p>安装组件<code>npm install --save vue-router</code></p>
</li>
<li>
<p>引入并使用<code>import VueRouter from 'vue-router'; Vue.use(VueRouter)</code></p>
</li>
<li>
<p>路由方式</p>
<ul>
<li>静态路径</li>
</ul>
<pre><code class="copyable">const Routers =[&#123;
    path:'/index',
    component:(resolve) => require(['./index.vue'],resolve)
    &#125;,&#123;
    path:'/user/:id',// :id在user.vue可以使用$route.param.id获取值
    component:(resolve) => require(['./user.vue'],resolve)
    &#125;,
]
const RouterConfig =&#123;
    mode:'history'//使用html5 history路由模式
    routes:Routers
&#125;
const router = new VueRouter(RouterConfig)
new Vue(&#123;router:router&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>路由跳转
<ul>
<li><code><router-link to="调转配置好的静态路由path" tag="渲染时的标签" ></code>另外，repalce属性会导致无法使用后退；active-class属性会修改默认匹配路由后的class的名称</li>
<li>js代码</li>
</ul>
</li>
</ul>
<pre><code class="copyable">this.$router.push('调转配置好的静态路由path') // 执行js时候的跳转
this.$router.replace('调转配置好的静态路由path')// 无法使用后退
this.$router.go(-1) //后退1页
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>导航钩子</li>
</ul>
<p>针对修改每一个跳转后的title，可以同一使用beforeEach钩子。在离开页面前执行。
跳转后的新页面可以使用afterEach钩子，使页面跳转到顶部。进入页面后执行。</p>
<pre><code class="copyable">const router = new VueRouter(RouterConfig)
router.beforeEach((to,from,next) =>&#123;
    to 将进入目标的路由对象
    from 当前即将离开的路由对象
    next 进入下一个钩子
    to和from对象可以通过meta获取信息
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h1 data-id="heading-12">vuex用法</h1>
<p>核心变化是使用了观察者模式，将逻辑代码进行了拆分，同时将变量数据全局化。
安装、引入、启用vuex <code>npm install --save vuex; import VueRouter from 'vuex';  Vue.use(Vuex);</code></p>
<pre><code class="copyable">const store = new Vuex.Store(&#123;
    state:&#123;
        count:0，
        list:[1,2,3,4,5]
    &#125;,
    // 同步方式，可以些执行逻辑
    mutations:&#123;
        increment (state,可以扩展基础类型参数/对象)&#123;
            state.count++;
        &#125;
    &#125;,
    // 获取变量get方法
    getters:&#123;
        filterList:state=>&#123;
            return state.list.filter(item=>item>2)
        &#125;,
        //该方法的默认参数有state对象变量本地，getter对象
        listCount:(state,getters)=>&#123;
            return getters.filterList.length
        &#125;
    &#125;,
    actions:&#123;
    // context就是store对象
        incrementAsyn (context)&#123;
            context.commit('increment')
        &#125;
    &#125;
&#125;)
new Vue(&#123;store:store&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在页面中可以直接使用<code>&#123;&#123;$store.state.count&#125;&#125;</code>获取值</li>
<li>在页面中可以使用<code>this.$store.commit('increment',传入increment的参数)</code>increment为vuex中定义的逻辑方法</li>
<li>在页面使用<code>this.$store.getters.filterList</code>获取过滤后的数组</li>
<li>在页面actions块的调用方式是<code>this.$store.dispath('incrementAsyn')</code>,另外，可以actions块的逻辑块return promise对象，这样在调用的地方可以自定义回调响应</li>
</ul>
<h1 data-id="heading-13">JavaScript的事件循环机制</h1>
<p>调用同步js方法时：</p>
<ol>
<li>生成运行环境（context，含有该方法的作用域、参数、this、引用）</li>
<li>发现内部方法，将其同上放入执行栈，返回结果后销毁，回到上一个运行环境</li>
</ol>
<p>调用含有异步js方法时：</p>
<ol>
<li>生成运行环境</li>
<li>发现有异步方法，将其放入一个队列中，并将结果放入一个队列中。主线程继续执行执行中的内容</li>
<li>当执行栈执行完毕后，再查找队列中的内容</li>
<li>取出排列第一位的事件，将其放入执行栈中</li>
</ol>
<p>而vue异步更新dom的原理就是监听变量值的改变，将其值放入要给去重的队列中，等待下一个循环刷新队列并执行。<strong>$nextTick</strong>对象会立刻刷新队列（他的回调函数执行响应）</p>
<h1 data-id="heading-14">虚拟节点</h1>
<ul>
<li>正常ul li渲染方式：创建一个ul节点，然后将字节点一个一个的渲染出来</li>
<li>虚拟节点渲染方式：创建一个虚拟ul节点，再创建li的子节点，然后一次新渲染出来。</li>
</ul>
<h1 data-id="heading-15">手动挂载实例</h1>
<p>依靠Vue.extend和$mount两个方法挂载实例</p>
<pre><code class="copyable">var myComponent = Vue.extend(&#123;
    template:'<div>&#123;&#123;name&#125;&#125;</div>',
    data:()=>&#123;
        retrun &#123;name:'test'&#125;
    &#125;
&#125;)
new myComponent().$mount('#mount-div')
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">vue对jsx的支持</h1>
<pre><code class="copyable">new Vue(
    el:'#app',
    render ()&#123;
        retrun (<h1>test<h1>)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">webpack基础</h1>
<ul>
<li>重要也是必选的两项是入口（Entry）和出口（Output）。入口的作用是告诉webpack从哪里开始寻找依赖，并且编译，出口则用来配置编译后的文件存储位置和文件名。</li>
<li>output.path存放打包后文件的输出目录</li>
<li>output.publicPath指定资源文件引用目录</li>
<li>ooutput.filename指定输出文件名称</li>
<li>module对象的rules可以指定一系列加载器</li>
<li>module.test 正则表示式。编译过程中遇到的每一个import导入的css文件都用使用css-loader转换，然后style-loader转换</li>
<li>module.use 编译顺序是从后往前</li>
<li>plugins是一个定制的插件功能。</li>
<li>webpack就是一个js文件：webpack.config.js</li>
</ul>
<pre><code class="copyable">var ExtractTextPlugin = require('extract-text-webpack-plugin')
var config =&#123;
    entry:&#123;
        main:'./main'
    &#125;,
    output:&#123;
        path:path.join(_driname,'./dist'),
        publicPath:'/dist/',
        filename:'main.js'
    &#125;,
    module:&#123;
        rules:[&#123;
            test:/\.css$/,
            use:['style-loader','css-loader']
        &#125;,&#123;
        rules:[&#123;
            test:/\.css$/,
            use:ExtractTextPlugin.extract(&#123;
                use:'css-loader',
                fallback:'style-loader'
            &#125;)
        &#125;]
    &#125;,
    plugins:[new ExtractTextPlugin('mian.css')]
&#125;
module.exports= config;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装webpack与webpack-dev-server</p>
<pre><code class="copyable">npm install webpack --save-dev //开发版
npm install webpack-dev-server --save-dev //提供启动一个服务器、热更新、接口dialing等
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装CSS样式加载器</p>
<pre><code class="copyable">npm install css-loader --save-dev
npm install style-loader --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装将所有css合并到一个css的插件</p>
<pre><code class="copyable">npm install extract-text-webpack-plugin --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动webpack-dev-server服务脚本
<code>webpack-dev-server --open --config webpack.config.js</code></p>
<p>生成环境编译命令
<code>webpack --progress --hide-modules</code></p>
<h1 data-id="heading-18">webpack Vue Demo</h1>
<ul>
<li>针对生成环境<code>新建webpack.prod.config.js</code>,同时增加<code>"build":"webpack --progress --hide-modules --config webpack.prod.config.js"</code></li>
<li>开发环境的scripts命令 <code>"build":"webpack-dev-server --open --config webpack.config.js"</code></li>
</ul>
<pre><code class="copyable">npm install --save vue
npm install --save-dev vue-loader
npm install --save-dev vue-style-loader
npm install --save-dev vue-template-compiler
npm install --save-dev vue-hot-reload-api
npm install --save-dev babel
npm install --save-dev babel-loader
npm install --save-dev babel-core
npm install --save-dev babel-plugin-transform-runtime
npm install --save-dev babel-preset-es2015
npm install --save-dev babel-runtime
npm install --save-dev url-loader // 文件支持
npm install --save-dev file-loader // 图片支持
npm install --save-dev webpack-merge //打包支持
npm install --save-dev html-webpack-plugin //打包支持
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack.config.js</strong><br>
module.options是进一步对不同语言进行配置。因为vue的内容含有<template>、<script>、<style>，如果编译含有css就先使用css-loader加载，再使用vue-style-loader加</p>
<pre><code class="copyable">var path=require('path');
var ExtractTextPlugin=require('extract-text-webpack-plugin');
var config=&#123;
entry:&#123;
main:'./main'
&#125;,
output:&#123;
path:path.join(_dirname,'./dist'),
publicPath:'/dist/',
filename:'main.js'
&#125;,
module:&#123;
rules:[&#123;
test:/\.vue$/,
loader：'vue-1oader',
options:&#123;
loaders:&#123;
css:ExtractTextPlugin.extract(&#123;
use:'css-loader',
fallback:'vue-style-loader'
&#125;)
&#125;
&#125;
&#125;,
                &#123;
test:/\.(gif|jpg|png|woff|svg|eot|ttf)\??.*$/,
loader：'url-loader?limit=1024' //小于1kb 使用base64加载
&#125;,
&#123;
test:/\.js$/,
loader：'babel-loader',
exclude:/nodemodules/
&#125;,
&#123;
test:/\.css$/,
use:ExtractTextPlugin.extract(&#123;
use:'css-loader',
fallback:'style-loader'
&#125;)
&#125;]
&#125;,
plugins:[
newExtractTextPlugin(”main.css”)
]
&#125;
module.exports = config
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack.prod.config.js</strong><br>
主是将开发环境的配置和生成环境进行合并，即prod是webpack.config.js的扩展</p>
<pre><code class="copyable">var webpack =require('webpack');
var HtmlwebpackPlugin = require('html-webpack-plugin');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var merge = require('webpack-merge');
var webpackBaseConfig =require ('./webpack.config.js');

webpackBaseConfig.plugin=[]

module.exports=merge(webpackBaseConfig,&#123;
output:&#123;
publicPath:'/dist/',
//将入口文件重命名为带有20位hash值的唯一文件，解决线上缓存的问题
filename:'[name].[hash].js'
&#125;,
plugins:[
new ExtractTextPlugin(&#123;
filename : '[name].[hash].css',
allChunks:true
&#125;),
//定义当前node环境为生产环境
new webpack.DefinePlugin(&#123;
'process.env':&#123;
NODE_ENV:'"production"'
&#125;
&#125;),
new webpack.optimize.UglifyJsPlugin(&#123;
compress:&#123;
warings:false
&#125;
&#125;),
//提取模板，保存入口html文件
new HtmlwebpackPlugin(&#123;
filename:'../index_prod.html',
template:'./index.ejs', //是一个模板文件
inject:false
&#125;)
]
&#125;)

//index.ejs
<!DOC TYPE html>
<html lang＝"zh-CN">
<head>
<meta charset ="UTF-8">
<title>webpack App</title>
<link rel＝"stylesheet" href＝"<%=htmlwebpackPlugin.files.css[0]%>">
</head>
<body>
    <div id ="app"></div>
    <script type＝"text/javascript" src="<%=htmlwebpackPlugin.files.js[0]%>"></script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>.babelrc</strong><br>
在webpack同级目录建立.babelrc文件，写入babel配置，webpack会依赖此配置文件来使用babel编译es6代码</p>
<pre><code class="copyable">&#123;
    "presets":["es2015"],
    "plugins":["transorm-runtime"],
    "comments"false
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">Vue插件机制，可以全局添加一些功能</h1>
<pre><code class="copyable">MyPlugin.install = function(Vue,options)&#123;
    //全局组件注册
    Vue.component('component-name',&#123;&#125;)
    //添加实例方法
    Vue.prototype.$Notice = function()&#123;&#125;
    //添加全局方法或属性
    Vue.globalMethod = function()&#123;&#125;
    //添加全局混合
    Vue.mixin(&#123;mounted:function()&#123;&#125;&#125;)
&#125;
//使用插件
vue.use(myPlugin)

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">ES6扫盲</h1>
<pre><code class="copyable">data()&#123;&#125; 等同于 data:functoin()&#123;&#125;
h=>h('test') 等同于 function(h)&#123;return h('test')&#125; 也等同于 h=>&#123;return h('test')&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            