
---
title: 'Vue2.0的笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17c71d9986724b87a54d6a34a97e4be0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 00:56:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17c71d9986724b87a54d6a34a97e4be0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vue2.0</h2>
<pre><code class="hljs language-css copyable" lang="css">声明式编程，命令式编程
响应式： 数据改，界面自动改
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17c71d9986724b87a54d6a34a97e4be0~tplv-k3u1fbpfcp-watermark.image" alt="image-20210329231033315.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d925701741e43b786b89cc63e84d900~tplv-k3u1fbpfcp-watermark.image" alt="image-20210329231349374.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.stop</span> 阻止子元素的监听  触发父元素
<span class="hljs-selector-class">.prevent</span> 阻止默认事件发生，<span class="hljs-selector-tag">form</span>-<span class="hljs-selector-tag">input</span>

<span class="hljs-selector-tag">input</span>-text,<span class="hljs-keyword">@keyup</span>类似<span class="hljs-keyword">@click</span>

    @keyup.enter=<span class="hljs-string">"函数名"</span> 监听特定键帽的点击（这里为enter）

    @click.once=<span class="hljs-string">"函数名"</span> 只触发一次
    /******************************************************/
v-if=<span class="hljs-string">"变量名"</span> 控制标签是否要渲染出来，true，false
对应的有v-else-if,v-else。
    用v-if和v-else，做一个切换输入用户名和用户邮箱界面
    div-> 两个v-if/else的span，-> label for=<span class="hljs-string">"xx"</span>和input id=<span class="hljs-string">"xx"</span> placeholder
    你会发现输入点东西后，再点切换，input栏内的内容保留，没有清空
    /*  label for=<span class="hljs-string">"xxx"</span> 点击文字，会选中id为xxx的input type=<span class="hljs-string">"radio"</span> name=<span class="hljs-string">"sex/age..."</span> */
    为什么？（vue-底层）
    vue会把我们将要显示的东西放到内存里面，在内存中创建vdom（virtual dom），在进行dom渲染时，出于性能考虑，会尽可能复用已经  存在的元素，而不是创建新的。所以我们还是用的原来的label和input，只是对比渲染，把除了用户输入的内容外，都清空替换了。
    解决方案：
    给相应的input添加key，并且保证key的不同，就不会进行复用
    /*****************************************************/
    v-if 和 v-show 都可以选择是否显示页面元素
    但是false的时候，元素消失方式不同
    v-if 完全消失，不存在于dom中--创建和删除
    v-show  只是加了个<span class="hljs-attribute">display</span>:none; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image-20210403194017905" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">在数组中间插入一个新的元素
比如我们有<span class="hljs-number">4</span>个li，对应内容含有A B C D。这时候，我们要在BC中间插入E
我们可以假设目前在vdom中为 <span class="hljs-number">0</span>-A <span class="hljs-number">1</span>-B <span class="hljs-number">2</span>-C <span class="hljs-number">3</span>-D  （vue底层） 在dom中为 A B C D
这时候，在vdom中插入，<span class="hljs-number">0</span>-A <span class="hljs-number">1</span>-B <span class="hljs-number">2</span>-E <span class="hljs-number">3</span>-C <span class="hljs-number">4</span>-D
vdom中，在E插入后，<span class="hljs-number">3</span>号位置变为原先<span class="hljs-number">2</span>号C，创建<span class="hljs-number">4</span>号位置变为D
dom中， 依据diff算法，A B C D变成A B E C D变化的次序和上一行类似，(也是一个个从上往下变C变E，D变C，最后插入D)
效率十分的低

这时候，我们需要设置key来给每个节点做一个 唯一 标识。--如果多个li的key相同会报错
<span class="hljs-attr">eg</span>:  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in array"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item"</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
加入了key之后的数组插入，就如上图With Keys所示，有一一对应那种感觉，<span class="hljs-number">0</span>对A，<span class="hljs-number">1</span>对B等等。
要插入的E在原数组配对好后，会到合适的位置上去，而不是让数据一个个的变
<span class="hljs-comment">/***********************************************************************/</span>
push--- 尾部添加 unshift ---首部添加   (添加都可以传多个值)
pop--- 尾部删除  shift--- 首部删除
可变参数   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">...num</span>) </span>&#123;
    clg(num);  &#125;
splice(起始位置，删除个数，用于替换的元素)       删除/插入/替换
splice(<span class="hljs-number">1</span>)删除<span class="hljs-number">1</span>以及后面所有

Vue.set(<span class="hljs-built_in">this</span>.array,<span class="hljs-number">0</span>,<span class="hljs-string">'xxx'</span>) 第一个参数是数组对象，第二个为index，第三个是修改成的值
上述都是响应式，而<span class="hljs-built_in">this</span>.array[index]=<span class="hljs-string">'xxx'</span>,会修改值，但不是响应式，页面不变
<span class="hljs-comment">/***********************************************************************/</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1"><code>filter/map/reduce</code></h3>
<pre><code class="hljs language-js copyable" lang="js">filter / map /reduce

过滤器： filter中的回调函数有一个要求：必须返回一个boolean类型的值
    <span class="hljs-keyword">const</span> nums = [<span class="hljs-number">10</span>,<span class="hljs-number">20</span>,<span class="hljs-number">123</span>,<span class="hljs-number">450</span>,<span class="hljs-number">45</span>]
    <span class="hljs-keyword">let</span> newNums = nums.filter(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>)</span>&#123;
        <span class="hljs-keyword">return</span> n<<span class="hljs-number">100</span>; &#125;   )
返回<span class="hljs-literal">true</span>，函数内部会自动将：“此次回调的n” (满足条件的数组元素) 加入到新的数组中  
 <span class="hljs-comment">/*这个新的数组自动创建，我们负责接收就行 */</span>
<span class="hljs-attr">false</span>: 会过滤掉此次的n

map函数:  映射操作
    <span class="hljs-keyword">const</span> nums = [<span class="hljs-number">10</span>,<span class="hljs-number">20</span>,<span class="hljs-number">123</span>,<span class="hljs-number">450</span>,<span class="hljs-number">45</span>]
    <span class="hljs-keyword">let</span> newNums = nums.map(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>)</span>&#123;
        <span class="hljs-keyword">return</span> n*<span class="hljs-number">2</span>; &#125;   )
会把返回的值作为，数组中原位置的，新值。

reduce函数：对数组中所有的内容进行汇总
<span class="hljs-comment">/*(这个函数定义用的是ts)有函数重载功能，可以写两个函数，同名不覆盖,参数数量不同使得功能有所差异*/</span>
    <span class="hljs-keyword">const</span> nums = [<span class="hljs-number">10</span>,<span class="hljs-number">20</span>,<span class="hljs-number">123</span>,<span class="hljs-number">450</span>,<span class="hljs-number">45</span>]    
<span class="hljs-keyword">let</span> total = nums.reduce(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">preValue,n</span>)</span>&#123;
        <span class="hljs-keyword">return</span> preValue+ n
    &#125;,<span class="hljs-number">0</span>)
 两个参数，参数一本身为一个函数，参数二为初始化值。
 参数一作为一个函数，有两个参数 preValue为前一次<span class="hljs-keyword">return</span>的值，n为每一次数组遍历的值，第一次preValue为  reduce的参数二初始值。
 <span class="hljs-comment">/* 第一次  preValue==0，n==10 . 第二次 preValue==0+10==10，n==20  第三次preValue==20+10==30依次类推。。return preValue+n 可以得出数组所有数的和， 最终结果返回，用total接收。*/</span>
 
 综合：函数式编程
     <span class="hljs-keyword">const</span> nums = [<span class="hljs-number">10</span>,<span class="hljs-number">20</span>,<span class="hljs-number">123</span>,<span class="hljs-number">450</span>,<span class="hljs-number">45</span>]
     <span class="hljs-keyword">let</span> total = nums.filter(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>)</span>&#123;
         <span class="hljs-keyword">return</span> n<<span class="hljs-number">100</span>
     &#125;).map(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>)</span>&#123;
         <span class="hljs-keyword">return</span> n*<span class="hljs-number">2</span>
     &#125;).reduce(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">preVaule,n</span>)</span>&#123;
         <span class="hljs-keyword">return</span> preValue + n
     &#125;,<span class="hljs-number">0</span>)
     箭头函数
     <span class="hljs-keyword">let</span> total =nums.filter(<span class="hljs-function"><span class="hljs-params">n</span>=></span>n<<span class="hljs-number">100</span>).map(<span class="hljs-function"><span class="hljs-params">n</span>=></span>n*<span class="hljs-number">2</span>).reduce(<span class="hljs-function">(<span class="hljs-params">pre,n</span>)=></span>pre+n);
这里reduce的参数二默认初始值为<span class="hljs-number">0</span>了

    <span class="hljs-comment">/***********************************************************************/</span>

    编程范式--命令式编程/声明式编程
    编程范式--面向对象编程（第一公民：对象）/函数式编程（第一公民：函数）

    <span class="hljs-comment">/***********************************************************************/</span>
以后监听事件(@)函数别加括号了，可能出错，@input有问题，@click没问题
     v-model原理:
           语法糖，<span class="hljs-number">1.</span>v-bind绑定一个value属性
             <span class="hljs-number">2.</span>v-on 指令给当前元素绑定input事件  
        <input type=<span class="hljs-string">"text"</span> v-model=<span class="hljs-string">"message"</span>>
           等同于
        <input type=<span class="hljs-string">"text"</span> v-bind:value=<span class="hljs-string">"message"</span> v-on:input=<span class="hljs-string">"message=$event.target.value"</span>>
      
   <span class="hljs-comment">/////////////////////////////////////////////////////////////////////////</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span> /*只能输入数字 加上*/  <span class="hljs-attr">v-model</span>=<span class="hljs-string">"age"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;age&#125;&#125;--&#123;&#123;typeof age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    Vue中
    age:0  ---> 一开始为0和number
    在input框中输入东西后，显示为： 输入的数字和string

    也就是说双向绑定，实时传过去的值，是作为一个string类型传的
    要想变成number，直接 
    v-model.number="age"    即可解决问题

    .lazy 懒加载 input失去焦点后显示变化后的value
    .trim 去除空格 
/*即使数据string中 有很多空格，浏览器显示的时候，会忽略的，但是数据处理时候可以用trim去除空格*/
/////////////////////////////////////////////////////////////////////////
</span><span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-2">组件化</h2>
<p>组件：一个封闭的空间，我可以有自己的数据，有自己的方法</p>
<pre><code class="hljs language-js copyable" lang="js">component -- 缩写cpn
ES6补充，<span class="hljs-string">` 这里面可以包含换行 `</span> 而<span class="hljs-string">''</span>以及<span class="hljs-string">""</span>如果要换行需要分两部分加引号，中间加+
    
可以把Vue实例当作一个根上的组件(root组件)
要想使用某个组件，必须要保证它在作用域注册过，要么是全局，要么是对应父组件的components中注册过
不然就会报错，Unknow custom element <标签名>

<span class="hljs-comment">//例子：</span>
 <span class="hljs-keyword">const</span> cpnC1=Vue.extend(&#123;
     <span class="hljs-attr">template</span>:<span class="hljs-string">`<div><span>nothing1</span></div>`</span>,
 &#125;)
 <span class="hljs-keyword">const</span> cpnC2=Vue.extend(&#123;
     <span class="hljs-attr">template</span>:<span class="hljs-string">`<div><span>nothing1</span></div>`</span>,
     <span class="hljs-attr">components</span>:&#123;
         <span class="hljs-attr">cpn1</span>:cpnC1
     &#125;
 &#125;)
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">components</span>:&#123;
        <span class="hljs-attr">cpn2</span>:cpnC2
    &#125;
&#125;)
<div id=<span class="hljs-string">"app"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">cpn2</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn2</span>></span></span> <span class="hljs-comment">//直接调用了组件2</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">cpn1</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn1</span>></span></span> <span class="hljs-comment">// 报错，因为cpnC1是在cpnC2组件内部注册的，作用域就是组件cpnC2</span>
</div>
<span class="hljs-comment">// 解决办法</span>
<span class="hljs-comment">// 组件可以注册多次，在Vue实例中components中再注册一次</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">组件中代码与html分离
<span class="hljs-number">1.</span> script type=<span class="hljs-string">"text/x-template"</span>
<span class="hljs-number">2.</span> 外层套个 template 标签
注意不管是script还是template标签都要加个id
然后在js代码中，template:<span class="hljs-string">'#id'</span>
<span class="hljs-comment">////////////////////////////////////////////////////////////////////////////</span>


组件内部不能访问Vue实例data数据
所以组件内部有一个data属性，但是不能是对象类型，
应该是个<span class="hljs-function"><span class="hljs-keyword">function</span>，并且返回一个对象，对象内部保存着数据
<<span class="hljs-title">template</span> <span class="hljs-title">id</span>="<span class="hljs-title">theid</span>">
<<span class="hljs-title">div</span>> <span class="hljs-title">h2</span>.....<span class="hljs-title">p</span>....</span>&#123;&#123;title&#125;&#125; </div>
</template>
Vue.component(<span class="hljs-string">'cpn'</span>,&#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">'#theid'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">title</span>:<span class="hljs-string">'abc'</span>
        &#125;
    &#125;
&#125;)

组件对象也有methods等属性，有声明周期函数，很像一个Vue实例，组件的原型就是指向Vue的

<span class="hljs-comment">////////////////////////////////////////////////////////////////////////////</span>

为什么Vue组件中data必须是一个函数？

每次函数执行时候都会在栈空间创建新变量
    <span class="hljs-comment">// 例子</span>
     <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">abc</span>(<span class="hljs-params"></span>)</span>&#123;
         <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">name</span>:<span class="hljs-string">'whe'</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">18</span>&#125;
     &#125;
    <span class="hljs-keyword">let</span> obj1= abc() <span class="hljs-keyword">let</span> obj2=abc()
    obj1和obj2是两个不同的对象 
    测试： obj1.name=<span class="hljs-string">"mmmm"</span> <span class="hljs-built_in">console</span>.log(obj2.name)
 
    你做一个模块，功能就是计时器，一个count的div，一个加和一个减的按钮
    你引用了<span class="hljs-number">2</span>次模块，那么两次模块里，count是两个不同的变量。
    
总结：用函数每次返回的都是新的对象，可以避免-多个组件实例共用变量的情况

要想人为共用变量，可以<span class="hljs-keyword">const</span> obj=&#123; <span class="hljs-attr">count</span>:<span class="hljs-number">0</span> &#125;
Vue.component中 <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-keyword">return</span> obj &#125;, 这样就共用了obj的count

<span class="hljs-comment">////////////////////////////////////////////////////////////////////////////</span>

HTML是不区分大小写的。而JS区分。所以一般情况下，JS的大小写变量放到HTML中，会将大写改成小写，并在前面添加短杠。
    所以我们事件命名时候不要使用 camelCase 和 PascalCase 来命名了，
    因为就算你使用该命名，在DOM模板中还是会被自动转化为全小写,
    如 <input type=<span class="hljs-string">"text"</span> v-on:keyup.F2=<span class="hljs-number">113</span>>  会被自动转换为
       <input type=<span class="hljs-string">"text"</span> v-on:keyup.f2=<span class="hljs-number">113</span>>
以及：vue中v-bind/on等等。不支持驼峰命名---》 父子组件通信，变量别用驼峰命名,会显示默认值
除非，把大小写自己做个转换，eg:
子组件cpn中数据textMyMessage  在写到html的cpn标签中时
    转换为: text-my-message

<span class="hljs-comment">////////////////////////////////////////////////////////////////////////////</span>

定义子组件模板的时候，引用数据
<template>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;cmessage&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;aamessage&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>
</template>
会报错，需要在两个数据引用的外层套一个div
<template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;cmessage&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;aamessage&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="hljs-comment">///////////////////////////////////////////////////////////////////////////////////</span>

前面说了组件中v-bind不用驼峰命名，为什么在.vue文件中就可以
.vue文件中的 template script style标签会编译成一个组件对象,且这个对象中没有template
它会把组件对象渲染成一个render函数,在这个渲染的过程中解析驼峰命名的名字，是能正常进行的
html则是大写变小写

<span class="hljs-comment">///////////////////////////////////////////////////////////////////////////////////</span>

父传子: props ---子组件构造器中写，常写成对象形式,cpn标签中对应赋值父组件中值
子传父: events  ---子组件 $emit()触发事件，父组件 v-on、@ 监听子组件事件

补充： 父传子，父组件(一个Vue实例)中
Vue(&#123;
<span class="hljs-attr">data</span>:&#123;  
        <span class="hljs-attr">num1</span>:<span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">components</span>:&#123;
        <span class="hljs-comment">//子组件--语法糖</span>
       <span class="hljs-attr">cpn</span>:&#123;
         <span class="hljs-attr">props</span>:&#123;
             <span class="hljs-attr">number1</span>:<span class="hljs-built_in">Number</span> <span class="hljs-comment">// 定义变量名和类型</span>
         &#125;
       &#125;     
    &#125;,
&#125;)
 
在template标签中：
 
 如果要input  v-model双向绑定数据的话，不要绑定到number1去
    虽然这样你仍然可以实现，但是会报错的，为什么？ 
    因为：number1本身的值，就是从父组件那里拿来的，你不能既被父组件数据改，又被input改
<span class="hljs-comment">// Instead, use a data or computed property based on the prop's value</span>
    因此做法可以为: 在子组件中，利用data或者computed来整个新变量
<span class="hljs-attr">eg</span>: 在上面的component中
   <span class="hljs-attr">cpn</span>:&#123;
     <span class="hljs-attr">props</span>:&#123;
         <span class="hljs-attr">number1</span>:<span class="hljs-built_in">Number</span>
     &#125;,
     <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
         <span class="hljs-keyword">return</span> &#123;
             <span class="hljs-attr">dnumber1</span>: <span class="hljs-built_in">this</span>.number1,
         &#125;
     &#125;
   &#125;  
然后input text v-model=<span class="hljs-string">"dnumber1"</span> 这样才是合理的做法
之后只有dnumber1和input内的输入双向绑定,而number1 不变，还是拿的父组件的num1


    *如果要改变num1的值，那么：
先不选择v-model，或者说，换种写法，变成 @和v-on
    template标签中：
    <input :value=<span class="hljs-string">"dnumber1"</span> @input=<span class="hljs-string">"num1Input"</span>> <span class="hljs-comment">// 监听事件num1Input</span>
<span class="hljs-comment">//  到子组件去定义函数 num1Input</span>
子组件：methods:&#123;
<span class="hljs-function"><span class="hljs-title">num1Input</span>(<span class="hljs-params">event</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.dnumber1 = event.target.value; <span class="hljs-comment">// 这个只改变了dnumber1</span>
    <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'num1change'</span>,<span class="hljs-built_in">this</span>.dnumber1) <span class="hljs-comment">// 每次input，发射数据给父组件</span>
    &#125;
&#125;
然后：
div id=<span class="hljs-string">"app"</span>中， cpn标签，
<cpn :number1=<span class="hljs-string">"num1"</span> @num1change=<span class="hljs-string">"parent_num1change"</span> />

父组件：
<span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">parents_num1change</span>(<span class="hljs-params">value</span>)</span>&#123; <span class="hljs-comment">// 这里的value就是子组件发射传来的 dnumber1</span>
        <span class="hljs-built_in">this</span>.num1= <span class="hljs-built_in">parseInt</span>(value) <span class="hljs-comment">// 传过来的是string</span>
    &#125;
&#125;
  <span class="hljs-comment">//字符串转number ，一：乘以1.   二： parseInt(string) </span>
再在之后input内输入值，会改变 dnumber1，也会改变num1，然后改变 number1

假如有个num2，number2，dnumber2，要改变num2且为num1的<span class="hljs-number">100</span>倍，在子组件的methods中最后加上：
<span class="hljs-built_in">this</span>.dnumber2 = <span class="hljs-built_in">this</span>.denumber1*<span class="hljs-number">100</span>;
<span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'num2change'</span>,<span class="hljs-built_in">this</span>.dnumber2);

在组件中，与data，template,props,methods,computed同级的还有 watch
作用：监听变量的变化----注意：如果是子组件，返回的一个对象中的数据也可以监听
<span class="hljs-attr">eg</span>:
<span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">dnumber1</span>:<span class="hljs-built_in">this</span>.number1;
        &#125;
    &#125;,
<span class="hljs-attr">watch</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">dnumber1</span>(<span class="hljs-params">newValue</span>)</span>&#123;
            <span class="hljs-built_in">this</span>.dnumber1 = newValue*<span class="hljs-number">10</span>;
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'num1change'</span>,newValue);
            <span class="hljs-comment">// 比如这里有个 this.denumber2=0;</span>
        &#125;
        <span class="hljs-comment">// 如果在上面改变一个变量，下面也可以监听到的</span>
        <span class="hljs-function"><span class="hljs-title">dnumber2</span>(<span class="hljs-params">newValue</span>)</span>&#123;
            <span class="hljs-comment">// 会因监听到dnumber2的改变而运行</span>
        &#125;
    &#125;
<span class="hljs-comment">// 除了newValue，还可以有第二个参数，oldValue</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/551609fd4167476b960cf77552489c73~tplv-k3u1fbpfcp-watermark.image" alt="image-20210411232934442.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">父子组件的访问方式</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件访问子组件</span>
$children 或者 $refs (reference 引用)
<span class="hljs-comment">//  子组件访问父组件</span>
$parent



比如，现在 在一个Vue实例里边，有一个子组件cpn，


子组件  methods里面定义了一个方法showMessage
<span class="hljs-function"><span class="hljs-title">showMessage</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'showMessage'</span>);
&#125;

父组件  methods里面定义了一个方法btnClick <span class="hljs-comment">// 通过div #app中的一个button的click触发 </span>
<span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children);
    <span class="hljs-comment">// 返回一个数组，数组中放着VueComponent类型-组件对象</span>
<span class="hljs-built_in">this</span>.$children[<span class="hljs-number">0</span>].showMessage(); <span class="hljs-comment">// 控制台打印 showMessage，引用了子组件方法</span>
&#125;
<span class="hljs-comment">// 如果在html中引用多次的cpn标签（即便相同），那么返回的数组就会多个VueComponent对象</span>
<span class="hljs-comment">// 有index的一般应变性不行，比如突然要你在前面加一个组件，index就全变了。故$children一般不用</span>

而开发常用的 $refs 初始就是一个空的对象
在组件标签中加： <cpn ref=<span class="hljs-string">"aa"</span>></cpn>
即可通过, <span class="hljs-built_in">this</span>.$refs.aa来引用这个VueComponent对象


<span class="hljs-comment">////////////////////////////////////////////////////////////////</span>

$parent 一般用的很少，因为会使得组件的复用性降低
$root 访问根组件---最高级组件-Vue实例，但是一般这个组件data为空。

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">组件化高级</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 插槽</span>
在template标签中，使用slot标签可以表示预留插槽
之后在<span class="hljs-string">`div #app`</span> 中cpn标签中间就可以加入若干个标签，比如p，div，button等，多个
这些标签会渲染在slot标签的位置上
如果slot标签中带了其他标签，表示： 当cpn标签中没设置其他标签时的默认

<span class="hljs-comment">// 具名插槽</span>
<template id=<span class="hljs-string">"cpn"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>左边<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>右边<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>            
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>            
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"left"</span>></span>替换文字<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    //  如果没有加slot属性，那么会把上面的两个slot的span改为”替换文字“
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>


<span class="hljs-comment">// 补充作用域</span>
<span class="hljs-string">`template`</span>标签内属于cpn子组件作用域
<span class="hljs-string">`div #app`</span>标签内属于vue父组件作用域
测试的话，标签v-show，组件内data定义boolean变量ishow

官方准则： 父组件模板的所有东西都会在父级作用域内编译；子组件模板的所有东西都会在子级作用域内编译


<span class="hljs-comment">////////////////////////////////////////////////////////////////////////</span>

作用域插槽---目的： <span class="hljs-string">`父组件替换插槽的标签，但是内容由子组件来提供`</span>
-- 父组件对子组件的展示的数据不满意，要以另一种方式展示，所以需要从子组件拿数据


eg： 子组件的data内有一个数组array，我希望把内容展示出来
<templat id=<span class="hljs-string">"cpn"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span>></span> ul <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in array"</span> ></span>&#123;&#123;item&#125;&#125; <span class="hljs-tag"></<span class="hljs-name">li</span>></span> /ul <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

在div #app中
    <cpn><cpn>
    <cpn><cpn>
为了使第二次的组件显示中，array数据的展示有所变化, 
        比如： 显示在一行，中间用 - 隔开
这时候需要在第二个cpn中拿到子组件的数据array
直接在cpn中类似li标签进行v-for是不行的，为什么：看上面的 组件作用域
  
那要怎么做？  首先想办法让子组件把数据传给父组件


<templat id="cpn">
    <div>  // 在slot标签中加入一个属性(可自命名)这里叫dat了,等于要的数组array
    <slot :dat="array"> ul <li v-for="item in array" >&#123;&#123;item&#125;&#125; </li> /ul </slot>
</div> 
</template>

第二个cpn中
<cpn>
<template slot-scope="slot">
//        <span v-for="item in slot.dat">&#123;&#123;item&#125;&#125; - </span>
          <span>&#123;&#123;slot.dat.join(' - ')&#125;&#125;</span>
</template>
</cpn>

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-5">Webpack</h2>
<h3 data-id="heading-6">ES6模块化补充</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 先是ES6一些模块化的东西</span>
在 script标签中加入 type=<span class="hljs-string">"module"</span> 可以使得.js文件模块化
其他文件无法直接访问
通过 <span class="hljs-keyword">export</span>导出， <span class="hljs-keyword">import</span>导入 
<span class="hljs-comment">// 法一</span>
<span class="hljs-keyword">export</span>&#123;
变量名<span class="hljs-number">1</span>,变量名<span class="hljs-number">2.</span>..
&#125;

<span class="hljs-keyword">import</span> &#123;变量名<span class="hljs-number">1</span>,变量名<span class="hljs-number">2</span>&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./文件名.js"</span>;
<span class="hljs-comment">// 法二：</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> num1=<span class="hljs-number">1000</span>;

<span class="hljs-keyword">import</span> &#123;num1&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./文件名.js"</span>;

<span class="hljs-comment">// 默认导出</span>
<span class="hljs-keyword">const</span> address = <span class="hljs-string">'guanzhou'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> address     <span class="hljs-comment">//  export default 可以有，但也只能有一个</span>
导入的时候： <span class="hljs-keyword">import</span> add <span class="hljs-keyword">from</span> <span class="hljs-string">"./文件名.js"</span>   <span class="hljs-comment">// 这里的 add就是其他人给address的重命名</span>

如果变量太多了，可以直接
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> info <span class="hljs-keyword">from</span> <span class="hljs-string">'./文件名.js'</span>
<span class="hljs-comment">// 会把其他模块的导出，全部存到info这个对象中（对象自己命名），之后通过属性引用</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">简介</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Webpack is a static module bundler for modern javascript application</span>
<span class="hljs-comment">// Webpack 是现代JavaScript应用的静态模块打包工具-----前端模块化打包工具</span>
相比，grunt/gulp和webpack，
grunt/gulp的核心是Task，更加强调的是前端流程的自动化，模块化不是它的核心
webpack更加强调模块化开发管理，而文件压缩合并，预处理等功能，是它附带的功能


文件夹名字
src 源码 --- 开发的东西
dist (distribution发布) --- 打包的要发布的东西
<span class="hljs-comment">/////////////////////////////////////////////////////////////////////////</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba4fd1f6f33b46b19f7e2d9a6839bd53~tplv-k3u1fbpfcp-watermark.image" alt="image-20210413221640550.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8"><code>JavaScript</code>处理</h3>
<pre><code class="hljs language-js copyable" lang="js">你有多个<span class="hljs-string">`.js`</span>文件-组件化，他们直接有相互的依赖（调用其他组件方法/变量）
你不需要再通过<span class="hljs-string">`script`</span>一个个引入，可以直接<span class="hljs-string">`webpack`</span>打包到<span class="hljs-string">`dist`</span>文件夹中
而且打包的时候，只需要指定个别的即可，
组件间的依赖（其他用到的组件）<span class="hljs-string">`webpack`</span>会帮你处理好一块打包
最后直接引入在<span class="hljs-string">`dist`</span>生成的文件即可
<span class="hljs-attr">eg</span>: 打开到文件目录， <span class="hljs-string">`webpack ./src/main.js ./dist/bundle.js`</span>
<span class="hljs-comment">// 上面那行代码，把main.js组件打包到dist文件夹，名字 bundle.js</span>

<span class="hljs-comment">////////////////////////////////////////////////////////////////////////////</span>

如果现在要想直接打个 webpack 就实现上面的打包功能
创建一个文件, <span class="hljs-string">`webpack.config.js`</span> 名字暂时固定
代码：
    <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
    <span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-attr">entry</span>:<span class="hljs-string">'./src/main.js'</span>,
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname,<span class="hljs-string">'dist'</span>), <span class="hljs-comment">// path其实是一个函数，可以对两个路径进行拼接，__dirname（全局变量，保存当前文件的路径）   dist (放到'dist')</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>
      &#125;,
    &#125;
这个path--动态获取路径，需要在本文件下，终端输入:
    <span class="hljs-string">`npm init`</span> <span class="hljs-comment">// 初始化，生成package.json，其文件中，开源才需要license属性</span>
   
    <span class="hljs-string">`npm install`</span> <span class="hljs-comment">// 生成 package-lock.json</span>
    
    
<span class="hljs-comment">/////////////////////////////////////////////////////////////////////////</span>
    
    但是如果我要想只通过<span class="hljs-string">`npm run 名字`</span>来运行呢？

    
全局和本地的webpack，版本不同，只有本地的和项目版本相同

安装本地的webpack:
<span class="hljs-string">`npm install webpack@3.6.0`</span>
---webpack的作用就是打包文件成包，之后发给服务器，webpack在打包之后就没用了

如果使用：
<span class="hljs-string">`npm install webpack@3.6.0 --save-dev`</span>
<span class="hljs-comment">// 在package.json文件会多出 "devDependencies": &#123; "webpack": '^3.6.0' &#125;</span>
<span class="hljs-comment">// devDependencies: 开发时依赖</span>

只要是在终端里面敲命令webpack，用的都是全局的webpack
所以需要在<span class="hljs-string">`package.json`</span> / <span class="hljs-string">`node_modules 的 library root `</span>中
的<span class="hljs-string">`scripts`</span>中配置脚本，加入webpack以及自定义名字  (类似设置快捷键)
然后 通过<span class="hljs-string">`npm run 自定义名字`</span> 来打包，这样会优先使用本地的<span class="hljs-string">`webpack`</span>版本

（package.json中的script脚本在执行的时候，会按照一定的顺序寻找命令对应的位置，
  首先，找本地的 node_modules/bin 路径中对应的命令，如果没有再去全局）
  
  <span class="hljs-comment">/////////////////////////////////////////////////////////////////////////</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><code>CSS</code>和<code>less</code>处理</h3>
<pre><code class="hljs language-js copyable" lang="js">  直接在main.js对css文件<span class="hljs-built_in">require</span>进行依赖，之后 npm run serve/webpack
  打包出错，需要安装loader
  npm run install --save-dev css-loader

<span class="hljs-comment">//   "css-loader": "^2.0.2",   "style-loader": "^0.23.1", "webpack": "^3.6.0"</span>
    <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
    <span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-attr">entry</span>:<span class="hljs-string">'./src/main.js'</span>,
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname,<span class="hljs-string">'dist'</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>
      &#125;,
      <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
          &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
            use: [ <span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span> ] <span class="hljs-comment">//  使用多个loader时，从右向左读</span>
          &#125;
        ]
      &#125;
    &#125;
<span class="hljs-comment">// css-loader 只负责将css文件进行加载，不负责解析</span>
<span class="hljs-comment">// css-loader负责将样式添加到DOM</span>

<span class="hljs-comment">// npm install style-loader --save-dev 或者 npm install --save-dev style-loader</span>
<span class="hljs-comment">//  在组件后边加个@和版本号就可以改版本信息 </span>


  <span class="hljs-comment">/////////////////////////////////////////////////////////////////////////</span>

如果想要打包 <span class="hljs-string">`.less`</span>文件
npm install --save-dev less-loader@<span class="hljs-number">4.1</span><span class="hljs-number">.0</span> less
注意最后的 <span class="hljs-string">`less`</span> 不能少，不然出错，它是一个包，npm利用的，真正起作用的工具

    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
          &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
            use: [ <span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span> ]     
          &#125;,
          &#123;
            <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
            use:[&#123;
              <span class="hljs-attr">loader</span>:<span class="hljs-string">"style-loader"</span>
            &#125;,&#123;
              <span class="hljs-attr">loader</span>:<span class="hljs-string">"css-loader"</span>
            &#125;,&#123;
              <span class="hljs-attr">loader</span>:<span class="hljs-string">"less-loader"</span>
            &#125;]
          &#125;
        ]
      &#125;
<span class="hljs-comment">// 第二个test也可以写作数组，不过写成对象的话，之后可以加入细节</span>
<span class="hljs-comment">// 记得三个 loader 的顺序， 也是反着来</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">图片资源处理</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  在css中通过url引入文件中的图片，npm run serve 报错。</span>
安装
npm install --save-dev url-loader

webpack.config.js   配置代码

<span class="hljs-built_in">module</span>--rules数组中
&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif|jpeg)$/</span>,
        use:[&#123;
            <span class="hljs-attr">loader</span>:<span class="hljs-string">"url-loader"</span>,
            <span class="hljs-attr">options</span>:&#123;  <span class="hljs-comment">// options记得加s</span>
                <span class="hljs-attr">limit</span>: <span class="hljs-number">16000</span>
            &#125;
        &#125;]
&#125;
<span class="hljs-comment">//  打包后，会把图片大小小于limit的图片，转换为 base64格式的东西，</span>
<span class="hljs-comment">//  通过服务器请求base64的字符串，放到url中</span>
<span class="hljs-comment">// 比如图片为10K，那么就应该填10240或者更大，如果图片大小大于limit,需要使用file-loader模块进行加载</span>

file-loader
npm install --save-dev file-loader 
这个就不用配置代码了
<span class="hljs-comment">// 运行后，会在dist中重新打包图片(并且重新命名，32位哈希值防止重复)，将来打包发行,我们用的也是dist中的图片，而不是打代码时文件夹里那张</span>

<span class="hljs-comment">// 接下里的问题就是，我们如何在html中的url使用dist中的图片路径</span>
我们需要在 webpack.config.js 文件中，
    <span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-attr">entry</span>:<span class="hljs-string">'./src/main.js'</span>,
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname,<span class="hljs-string">'dist'</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>,
        <span class="hljs-attr">publicPath</span>:<span class="hljs-string">'dist/'</span>  <span class="hljs-comment">// 这里加publicPath，以后url都会在前面加个dist路径，去那找</span>
      &#125;,
      <span class="hljs-attr">module</span>: &#123; 
          <span class="hljs-attr">rules</span>: [ 
              &#123; <span class="hljs-attr">text</span>:<span class="hljs-string">''</span>,<span class="hljs-attr">use</span>:[] &#125;,
              &#123; <span class="hljs-attr">text</span>:<span class="hljs-string">''</span>,<span class="hljs-attr">use</span>:[&#123;<span class="hljs-attr">loader</span>:<span class="hljs-string">" "</span>&#125;,&#123;<span class="hljs-attr">loader</span>:<span class="hljs-string">" "</span>&#125;,&#123;<span class="hljs-attr">loader</span>:<span class="hljs-string">" "</span>&#125;]
          ] &#125;
    &#125;
<span class="hljs-comment">// 最后 因为index.html也要放到dist拿去发行，最后publicPath不需要，记得删除</span>
<span class="hljs-comment">// 但是不可能最后，所有图片堆在dist文件里面，如果采取 放到 img/name 文件里面，可以知道图片名字，但是也可能重复，所以还是要加hash值 ---->    img/name.hash:8.ext     (:8 表示截取八位, 扩展名ext：extension) </span>
 解决方法：
        webpack.config.js   配置代码

        <span class="hljs-built_in">module</span>--rules数组中
        &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif|jpeg)$/</span>,
                use:[&#123;
                    <span class="hljs-attr">loader</span>:<span class="hljs-string">"url-loader"</span>,
                    <span class="hljs-attr">options</span>:&#123;  <span class="hljs-comment">// options记得加s</span>
                        <span class="hljs-attr">limit</span>: <span class="hljs-number">16000</span>,
                  <span class="hljs-attr">name</span>:<span class="hljs-string">"img/[name].[hash:8].[ext]"</span>
                    &#125;
                &#125;]
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11"><code>ES6转ES5</code></h3>
<pre><code class="hljs language-js copyable" lang="js">npm install --save-dev babel-loader@<span class="hljs-number">7</span> babel-core babel-preset-es2015
<span class="hljs-comment">// 其中babel-loader类似less安装时候的‘less’，也要安装</span>
webpack.config.js 配置代码
&#123;
    <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.js$/</span>,
        <span class="hljs-comment">// exclude 排除,</span>
        <span class="hljs-comment">// 局部环境install webpack生成的文件夹中.js文件不需要转换</span>
        exclude: <span class="hljs-regexp">/(node_modules|bower_components)/</span>,
            use:&#123;
                <span class="hljs-attr">loader</span>:<span class="hljs-string">'babel-loader'</span>,
                    <span class="hljs-attr">options</span>:&#123;
                        <span class="hljs-comment">//presets:['@babel/preset-env']</span>
                        <span class="hljs-attr">presets</span>:[<span class="hljs-string">'es2015'</span>]
                    &#125;
            &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">配置Vue</h3>
<pre><code class="hljs language-js copyable" lang="js">以前是把 vue.js 下载成文件引入，这不是模块化的方法：
现在直接
 npm install vue --save  <span class="hljs-comment">// 不-dev因为运行时也依赖，而不只是开发时依赖</span>
<span class="hljs-comment">// 会在 node_modules 中 export default Vue</span>
 
 之后要使用的时候，在.js文件中通过 <span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
 这里的<span class="hljs-string">'vue'</span>没有加路径，因为直接到node_modules 中去找了

<span class="hljs-comment">// 但是在div中加入#app显示&#123;&#123;message&#125;&#125;，那个简单安利，</span>
<span class="hljs-comment">// 直接npm run serve 后还是报错 用的runtime-only版本</span>
 runtime-only  代码中不允许有template
 runtime-compiler  代码中允许有template，因为compiler可以用于编译template

解决方案：声明使用runtime-compiler版本
webpack.config.js 配置代码

<span class="hljs-built_in">module</span>.exports =&#123;
    <span class="hljs-attr">entry</span>:<span class="hljs-string">'./src/main.js'</span>,
    <span class="hljs-attr">output</span>:&#123;&#125;,
    <span class="hljs-built_in">module</span>&#123;&#125;,
    <span class="hljs-attr">resolve</span>:&#123;
        <span class="hljs-comment">// alias: 别名</span>
        <span class="hljs-comment">// 好比 git commit -m '注释' 可以起别名成 git c '注释'</span>
        <span class="hljs-attr">alias</span>:&#123;
            <span class="hljs-string">'vue$'</span>:<span class="hljs-string">'vue/dist/vue.esm.js'</span>
            <span class="hljs-comment">// 表示：以后imp ort Vue from ‘vue’ 按照文件目录去找vue</span>
            <span class="hljs-comment">// 会到node_modules 找vue，里面的dist，找到vue.esm.js </span>
            <span class="hljs-comment">// vue.esm.js 里面就有compiler</span>
            <span class="hljs-comment">// 默认的就是使用相同路径下的 vue.runtime.js</span>
        &#125;
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/703ff43685d84e1c8ebc2127fb608cb8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210428174113927.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">补充</h3>
<pre><code class="hljs language-js copyable" lang="js">SPA（simple page web application）单页Web应用--> 多页面通过vue-router(前端路由跳转)
<span class="hljs-comment">// 如果我们希望 data中数据展示，那就得修改html代码，但是我们不希望频繁的改动html</span>
<span class="hljs-comment">// 所以：我们需要使用 el和template</span>
<span class="hljs-comment">// 在Vue中定义template属性,template中的html标签，会在之后替换到el挂载的div的位置</span>

<span class="hljs-comment">// 但是我们进一步分离 </span>
html中就一个div id=<span class="hljs-string">'app'</span>
在main.js文件中
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">const</span> App=&#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">`
<div @click="btnClick">&#123;&#123;message&#125;&#125;</div>
`</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">message</span>:<span class="hljs-string">'!!!'</span>,
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">template</span>:<span class="hljs-string">'<App/>'</span>,
    <span class="hljs-attr">components</span>:&#123;
        App
    &#125;
&#125;)
<span class="hljs-comment">// 在src下建立文件夹 vue, vue 下创建文件app.js 里面</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">`
<div @click="btnClick">&#123;&#123;message&#125;&#125;</div>
`</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">message</span>:<span class="hljs-string">'!!!'</span>,
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
        &#125;
    &#125;
&#125;
之后在原来的main.js文件中，直接
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./vue/app'</span> 就可以引用上面的代码
<span class="hljs-comment">// 这样就把组件的数据，方法，内容分离了出来，但是模板没有分离出来(template)</span>

在vue文件中创建，app.vue文件
将 app.js 文件中的数据分块移动到 app.vue 文件, app.js文件之后不用了
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
<span class="hljs-attr">name</span>:<span class="hljs-string">'App'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">message</span>:<span class="hljs-string">'!!!'</span>,
    &#125;
&#125;,
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
        &#125;
    &#125;
&#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.title</span> &#123;
            <span class="hljs-attribute">color</span>:green;
        &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="hljs-comment">// main.js中</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./vue/app.vue'</span>

<span class="hljs-comment">// 之后因为引入了新的文件--vue文件，下面要安装配置</span>
npm install vue-loader vue-template-compiler --save-dev
安装后 npm run serve 报错，因为 vue-loader <span class="hljs-number">14.</span>几之后的版本，需要安装插件
这里就webpack.config.js改一下版本到<span class="hljs-number">13</span> 然后 npm install 一下

<span class="hljs-comment">// 组件调用组件，在一个组件的.vue文件中的script标签中加入</span>
  <span class="hljs-keyword">import</span> 用组件时的标签名 <span class="hljs-keyword">from</span> <span class="hljs-string">'./组件名'</span> (./   一般同文件下)
<span class="hljs-comment">// 然后export default中组件注册，记得components,有个s 有个s</span>
<span class="hljs-comment">// 记得组件名/文件名，首个字母大写</span>

<span class="hljs-comment">// 测试了下，.vue文件中</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>中的name可以不要，按文件名来，
template中对组件标签的引用两种都可以 
<span class="hljs-comment">//eg:     <Omg></Omg>  或者 <Omg/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">plugin--插件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 插件: 对某个现有的架构进行扩展</span>
<span class="hljs-attr">loader</span>: 转换器/加载器,主要用于转换某些类型的模块
<span class="hljs-attr">plugin</span>: 扩展器，对webpack本身的扩展 --打包优化，文件压缩

<span class="hljs-comment">// 首先: 添加版权Plugin</span>
webpack.config.js文件中
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    ..
    <span class="hljs-attr">plugins</span>:[
    <span class="hljs-keyword">new</span> webpack.BannerPlugin(<span class="hljs-string">'xxxxxx'</span>)
    ]
&#125;
重新打包，在dist文件夹内的bundle.js首部加了xxxx信息

<span class="hljs-comment">// 打包html的Plugin</span>
自动生成index.html文件---可以指定模板
将打包的.js文件自动通过script标签插入到body中
<span class="hljs-comment">//npm install html-webpack-plugin --save-dev （注意版本案例用：3.2.0）</span>
然后 webpack.config.js 中
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>:<span class="hljs-string">'./src/main.js'</span>,
    <span class="hljs-attr">output</span>:&#123;&#125;,
    <span class="hljs-attr">plugins</span>:[
        <span class="hljs-keyword">new</span> webpack.BannerPlugin(<span class="hljs-string">'最终版权归Kuoc所有'</span>),
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>:<span class="hljs-string">'index.html'</span>
        &#125;)
    ],
    ...
&#125;
<span class="hljs-comment">// npm run serve</span>
    
<span class="hljs-comment">// 对JS进行压缩，uglify-丑化，开发阶段不需要丑化，发行才需要</span>
<span class="hljs-comment">//    npm install uglifyjs-webpack-plugin@1.1.1 --save-dev</span>
    
然后 webpack.config.js 中
<span class="hljs-keyword">const</span> UglifyjsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'uglifyjs-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>:<span class="hljs-string">'./src/main.js'</span>,
    <span class="hljs-attr">output</span>:&#123;&#125;,
    <span class="hljs-attr">plugins</span>:[
        <span class="hljs-keyword">new</span> webpack.BannerPlugin(<span class="hljs-string">'最终版权归Kuoc所有'</span>),
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>:<span class="hljs-string">'index.html'</span>
        &#125;),
        <span class="hljs-keyword">new</span> UglifyjsWebpackPlugin()
    ],
    ...
&#125;
<span class="hljs-comment">// npm run serve</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">搭建本地服务器</h3>
<pre><code class="hljs language-js copyable" lang="js">不需要每次都npm run serve 生成发行文件dist(放在磁盘中)
每次修改代码会自动刷新----更新内存中代码
<span class="hljs-comment">//npm install --save-dev webpack-dev-server@2.9.1</span>

然后 webpack.config.js 中

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>:<span class="hljs-string">'./src/main.js'</span>,
    <span class="hljs-attr">output</span>:&#123;&#125;,
    <span class="hljs-attr">plugins</span>:[
        <span class="hljs-keyword">new</span> webpack.BannerPlugin(<span class="hljs-string">'最终版权归Kuoc所有'</span>),
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>:<span class="hljs-string">'index.html'</span>
        &#125;),
        <span class="hljs-keyword">new</span> UglifyjsWebpackPlugin()
    ],
    <span class="hljs-attr">devServer</span>:&#123;
        <span class="hljs-attr">contentBase</span>:<span class="hljs-string">'./dist'</span>,
        <span class="hljs-attr">inline</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 是否实时监听</span>
        <span class="hljs-comment">//port 端口号，默认8080</span>
    &#125;
    ...
&#125;
<span class="hljs-comment">// 这里直接 webpack-dev-server 会报错，因为这相当于是命令行全局查找，但是这个插件是局部安装的</span>
所以：
法一： <span class="hljs-comment">//   .\node_modules\.bin\webpack-dev-server </span>
法二： package.json 文件中,script对象加属性，<span class="hljs-string">"dev"</span>:<span class="hljs-string">"webpack-dev-server --open"</span> 
       之后  npm run dev  即可<span class="hljs-comment">// 加--open自动打开网页</span>
最后，Ctrl + C ，  Y 推出当前操作，但是服务器仍然搭好了

开发的时候，需要 devServer，但是发行的时候就不需要了（JS丑化相反），所以我们可以做一个分离
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">Webpack配置分离</h3>
<pre><code class="hljs language-js copyable" lang="js">有部分的插件，你在开发时需要，但是发行之后不需要了
建立一个config文件夹，
内部建立：开发时的 dev.config.js  发行时的 prod.config.js  公共部分 base.config.js
将对应代码分块到文件内，比如
JS Uglifyjs放到prod.config.js   本地服务器搭建devServer放在dev.config.js
<span class="hljs-comment">// 解下来就是拼接了</span>
<span class="hljs-comment">//npm install webpack-merge@4.1.5 --save-dev</span>

dev.config.js文件
    <span class="hljs-comment">// 开发时依赖</span>
    <span class="hljs-keyword">const</span> webpackMerge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)
    <span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./base.config'</span>)

    <span class="hljs-built_in">module</span>.exports = webpackMerge(baseConfig,&#123;
      <span class="hljs-attr">devServer</span>:&#123;
        <span class="hljs-attr">contentBase</span>:<span class="hljs-string">'./dist'</span>,
        <span class="hljs-attr">inline</span>:<span class="hljs-literal">true</span> <span class="hljs-comment">// 是否实时监听</span>
        <span class="hljs-comment">//port 端口号，默认8080</span>
      &#125;
    &#125;)


prod.config.js文件
<span class="hljs-comment">// 发行时依赖</span>
    <span class="hljs-keyword">const</span> UglifyjsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'uglifyjs-webpack-plugin'</span>)
    <span class="hljs-keyword">const</span> webpackMerge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)
    <span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./base.config'</span>)

    <span class="hljs-built_in">module</span>.exports = webpackMerge(baseConfig,&#123;
      <span class="hljs-attr">plugins</span>:[
        <span class="hljs-keyword">new</span> UglifyjsWebpackPlugin()
      ]
    &#125;)
<span class="hljs-comment">// webpack.config.js文件可以删除了，然后到  package.json文件中</span>


scripts中,修改serve，添加dev
 <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>,
    <span class="hljs-string">"serve"</span>: <span class="hljs-string">"webpack --config ./config/prod.config.js"</span>, <span class="hljs-comment">// 发行</span>
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server --open --config ./config/dev.config.js"</span> <span class="hljs-comment">// 开发</span>
  &#125;,
<span class="hljs-comment">// 之后直接npm run serve，打包发行的的dist文件夹在config文件夹的下面，</span>
<span class="hljs-comment">// 而不是在整个项目文件夹的下面</span>
解决方法：
base.config.js文件中
    <span class="hljs-built_in">module</span>.exports = &#123;
      <span class="hljs-attr">entry</span>:<span class="hljs-string">'./src/main.js'</span>,
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname,<span class="hljs-string">'../dist'</span>), <span class="hljs-comment">// 这里的dist前面加../跳到上一级目录，不新生成</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>,
        <span class="hljs-attr">publicPath</span>:<span class="hljs-string">'dist/'</span>
      &#125;,.......
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-17">Vue CLI</h2>
<pre><code class="hljs language-js copyable" lang="js">脚手架---CLI--Command-Line-Interface 命令行界面
依赖node和webpack
<span class="hljs-comment">// 安装cmd中:  npm install -g @vue/cli</span>
<span class="hljs-comment">// vue --version 查看版本</span>
脚手架<span class="hljs-number">2.</span>x模板的拉取
<span class="hljs-comment">// npm install -g @vue/cli-init</span>

(my-project-项目名称-自己取)
<span class="hljs-comment">// CLI---2.x初始化项目： vue init webpack my-project</span>
<span class="hljs-comment">// CLI---3.x初始化项目： vue create my-project</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">Vue CLI2</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b450751f3c742018ceb0a1ddb36659b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210423153504724.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css">Lint --限制
ESLint ES限制,即：js代码不规范则报错--比如函数 function sun () &#123; &#125;以及最后不加分号;还有函数要被使用
config文件夹index<span class="hljs-selector-class">.js</span>文件，useEslint:false;关闭
e2e -> end <span class="hljs-selector-tag">to</span> end 端到端测试

build 和 config 都是项目配置,后者插件配置，前者变量定义以及文件merge

在static文件(静态资源,该文件的图片和数据会原封不动的复制到dist文件中)，package<span class="hljs-selector-class">.json</span>文件中，
    "dev": <span class="hljs-string">"webpack-dev-server --inline --progress --config build/webpack.dev.conf.js"</span>,
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"npm run dev"</span>,
两者一样的
    <span class="hljs-string">"lint"</span>: <span class="hljs-string">"eslint --ext .js,.vue src"</span>, 限制
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"node build/build.js"</span> 打包项目

 // 补充：node（c++开发，谷歌开源：核心V8引擎）为js提供了运行环境,
 // 以前js只能跑浏览器上, 在服务器上跑不起来
    
 // extract 抽离
    
 直接 node test.js  可以运行js代码，且会显示console.log 内容


.editorconfig文件-对项目代码规范进行约束
package-lock.json文件：是node_modules文件和package.json文件之间的映射关系
eg：---package.json中loader的版本 ^<span class="hljs-number">4.0</span>.<span class="hljs-number">1</span>表示大于等于<span class="hljs-number">4.0</span>.<span class="hljs-number">1</span>版本。但是我们不知道安装的哪个版本在node_modules所以需要 package-lock.json文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9f2177ca1cc4c8ba43827df7e20e6df~tplv-k3u1fbpfcp-watermark.image" alt="image-20210428195002333.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19"><code>runtimecompiler / runtimeonly</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 区别在main.js文件</span>

公共部分
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
Vue.config.productionTip = <span class="hljs-literal">false</span>

区别部分
<span class="hljs-attr">runtimecompiler</span>:
<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">template</span>: <span class="hljs-string">'<App/>'</span>,
    <span class="hljs-attr">components</span>: &#123;App&#125;
&#125;)

runtimeonly：
<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span>=></span>h(App)
  <span class="hljs-comment">/*  相当于
  render: function(h)&#123;
  return h(App)
  &#125;
  */</span>
&#125;)
差比的解释：先看 Vue程序运行过程图
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5934eb84dee94824b4bc60f5dbe70538~tplv-k3u1fbpfcp-watermark.image" alt="image-20210428210518051.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// template---> AST---> render ---> Virtual dom ---> Dom(UI)</span>
runtimeonly直接： render--> Vdom--> UI
相比于 runtime-compiler，runtimeonly 性能更高 代码更少
而且 runtimeonly中 .vue文件的 template标签，也都不会被解析成 AST，那么由谁处理？
<span class="hljs-comment">// .vue文件 被解析成对象，这个对象里面没有template的信息，</span>
<span class="hljs-comment">//  所有template都被vue-template-compiler转成了render函数</span>
所以我们不需要 template 转换为AST 再通过 compiler转换为 render函数
直接 runtimeonly
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20"><code>npm run build/dev</code></h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8a7cd73e3434c0a9c04318917211265~tplv-k3u1fbpfcp-watermark.image" alt="image-20210429001045103.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc6af0b1906a41ba8763e5cf1f6e0a50~tplv-k3u1fbpfcp-watermark.image" alt="image-20210429001052551.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">Vue CLI3</h4>
<p>版本差异</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  Vue2.5.21 -> Vue2.x -> flow-type类型检测(facebook)</span>
<span class="hljs-comment">//  Vue3.x -> TypeScript(microsoft)</span>

<span class="hljs-comment">//  vue-cli2 基于 webpack3 打造</span>
<span class="hljs-comment">//  vue-cli3 基于 webpack4 打造</span>

Vue-CLI3 -- <span class="hljs-number">0</span>配置，移除配置文件根目录下的 build和config等目录
提供了 vue ui 命令，提供了可视化配置
移除了<span class="hljs-keyword">static</span>文件夹，新增了public文件夹，而且index.html移动到public中
(其实可以把 public  看作是 <span class="hljs-keyword">static</span> -- [ˈstæ^tɪk]  )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建过程</p>
<pre><code class="hljs language-js copyable" lang="js">vue create testvuecli3(项目名)
终端弹出：
please pick a preset:<span class="hljs-comment">// preset：配置 [ˌpriːˈset]</span>
<span class="hljs-comment">// Manually 手动的 [ˈmænjuəli]</span>
选手动之后：多项选择--按空格选中
回车提交

<span class="hljs-comment">// vcs --> version control system (git/svn) </span>
git init 生成本地git仓库
git add . 进行一次提交
git commit -m <span class="hljs-string">'注释'</span> 提交到本地仓库
git push  到远程仓库
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a53c186f1dd74e17bd58d9826779e0c2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210429094236972.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae7415869f3e4477bed2b48f7caf613c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210429203943714.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>项目运行</p>
<pre><code class="hljs language-js copyable" lang="js">npm run build <span class="hljs-comment">// 最终打包发行版本</span>
npm run serve <span class="hljs-comment">//  开发时运行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">Vue Router</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff4be275137a4e3aa04278a7035b8667~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501193524377.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">前端 / 后端渲染</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-number">1</span>. 后端（服务端）渲染
早期浏览器开发：
<span class="hljs-selector-tag">html</span>，css没有js，用的jsp（java server page）/php ，写出一个网页传到浏览器，让浏览器展示
没有ajax，在服务器那里网页已经通过jap技术渲染好了
( <span class="hljs-selector-tag">html</span>+css+java，java从数据库动态读取数据并且放在页面中）
 服务器里就是最终的网页，传给浏览器时，只有<span class="hljs-selector-tag">html</span>和css
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20dc1515ec2a484897f38a7c6d7445b2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501193020452.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">2.</span>前后端分离阶段-前端渲染-jquery开发模式
通过ajax去请求数据
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11bc71daf853436f86b58a99a8915606~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501202248955.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-number">3</span><span class="hljs-selector-class">.SPA</span>页面
SPA：simple page web application--单页面富应用
在前后端分离阶段，静态资源服务器上保存的为  多套的 <span class="hljs-selector-tag">html</span>+css+js，以及对应的url
但是在静态资源服务器上只有一个index<span class="hljs-selector-class">.html</span>，有一些或者是一个 css，js
（请求一次拿到全部）这不代表只有一个网站
比如一个网站他有三个页面，但是在静态资源服务器里面只有一个<span class="hljs-selector-tag">html</span>，css，js
你必须依靠前端路由技术来分离页面的代码
你点击按钮，前端路由生成url，这时候不会向服务器请求资源，
而是通过js代码的判断，从全部代码中抽取页面代码（一个个的组件）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前端路由中url和组件的关系（一个页面就是一个大的组件）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f999eb5693c6472eb13843b88408c160~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501203849794.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">URL的hash 和 H5的history</h3>
<pre><code class="hljs language-css copyable" lang="css">URL:  scheme:// host:port/path?query #fragment
       协议     主机  端口  路径  查询

如何改变了url但页面不刷新？（F12-Network，查看资源请求知道刷新与否）
法<span class="hljs-number">1</span>. location.hash = <span class="hljs-string">'foo'</span>，后面<span class="hljs-string">'foo'</span>随意
法<span class="hljs-number">2</span>.  history.<span class="hljs-built_in">pushState</span>(&#123;&#125;,'','foo'),控制台返回undefined，并修改url，可以返回/back()
法<span class="hljs-number">3</span>.  history<span class="hljs-selector-class">.replaceState</span>(&#123;&#125;,'','foo'),不能返回

history<span class="hljs-selector-class">.go</span>(-<span class="hljs-number">1</span>)等同于 一个history<span class="hljs-selector-class">.back</span>(),   go(-<span class="hljs-number">2</span>),等同于两个，也可以为正数
history<span class="hljs-selector-class">.go</span>(<span class="hljs-number">1</span>)等同于 一个 history<span class="hljs-selector-class">.forward</span>()

法<span class="hljs-number">123</span>三个接口等同于浏览器界面的前进后退

href: hyper reference 超链接
<span class="copy-code-btn">复制代码</span></code></pre>
<p>history.pushState的 入栈和出栈</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be65cb312ea647d9bffa867c1f4555a8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210501205640295.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// redirect 重定向</span>
<span class="hljs-comment">// parameters 参数---params</span>
打包后的三个js文件
<span class="hljs-comment">// app 应用程序开发的所有代码--业务代码</span>
<span class="hljs-comment">// vendor 提供方，第三方vue</span>
<span class="hljs-comment">// manifest 为打包的代码做底层支撑的(import,export....)</span>


导入导出
<span class="hljs-comment">// commonjs的导入  const &#123;a,b,c&#125; = require('./xxx.js')</span>
<span class="hljs-comment">// es6的导入   import &#123;a,b,c&#125; from './xxx'</span>


$route 和 $router
$route -- 哪个组件处于活跃，就拿到哪个
$router -- 在App.vue 中创建的那个对象
<span class="hljs-attr">eg</span>:
computed: &#123;
    <span class="hljs-function"><span class="hljs-title">userId</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$route.params.useId        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">懒加载</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [
    &#123;
        <span class="hljs-attr">path</span>:<span class="hljs-string">'/home'</span>,
        <span class="hljs-attr">component</span>:<span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Home'</span>)
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>:<span class="hljs-string">'/about'</span>,
        <span class="hljs-attr">component</span>:<span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/About'</span>)
    &#125;,
];
<span class="hljs-comment">//  为了好管理，还是选择下面的写法</span>
<span class="hljs-keyword">const</span> Home = <span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Home'</span>)
<span class="hljs-keyword">const</span> About = <span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/About'</span>)
<span class="hljs-keyword">const</span> HomeNews = <span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/HomeNews'</span>)

<span class="hljs-keyword">const</span> routes = [
    &#123;
        <span class="hljs-attr">path</span>:<span class="hljs-string">'/home'</span>,
        <span class="hljs-attr">component</span>: Home,
        <span class="hljs-attr">children</span>:[
            &#123;
            <span class="hljs-attr">path</span>:<span class="hljs-string">'news'</span> <span class="hljs-comment">// news前不要加/</span>
                <span class="hljs-attr">component</span>:HomeNews
            &#125;,
        ]
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>:<span class="hljs-string">'/about'</span>,
        <span class="hljs-attr">component</span>:About
    &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a96767fe9dfb42a3bc0b6ca1709f293b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210502195706998.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">Profile <span class="hljs-comment">// 档案----我的页面</span>

在router文件夹中的index.js文件，
<span class="hljs-number">1.</span><span class="hljs-comment">//////////////////////</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> User <span class="hljs-keyword">from</span> <span class="hljs-string">'./User.vue'</span> <span class="hljs-comment">// 路由</span>
<span class="hljs-comment">//////////////////</span>
<span class="hljs-number">2.</span>
Vue.use(VueRouter)
<span class="hljs-comment">//////////////////</span>
<span class="hljs-number">3.</span> 
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>:<span class="hljs-string">''</span>,
    <span class="hljs-attr">redirect</span>:<span class="hljs-string">'/home'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>:<span class="hljs-string">'/user/:userId'</span>,
    <span class="hljs-attr">component</span>:User
  &#125;
]
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;  <span class="hljs-comment">// VueRouter含有push，replace，back等方法</span>
  routes,
  <span class="hljs-attr">mode</span>:<span class="hljs-string">'history'</span>,
  <span class="hljs-attr">linkActiveClass</span>:<span class="hljs-string">'active'</span>
&#125;)
<span class="hljs-comment">//////////////////</span>
<span class="hljs-number">4.</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="hljs-comment">//////////////////</span>
其中第二部分Vue.use(VueRouter)，实际是VueRouter.install，对插件进行安装
而在打包文件node_modules中，找到src，找到util，找到install.js看源码
可以知道，有一行意义代表：（以及全局注册的 RouterView 和 RouterLink ）
<span class="hljs-comment">// Vue.prototype.$router = return this._routerRoot._rooter;</span>
<span class="hljs-comment">// 补充说明，所有的组件都继承自 Vue类的原型!!!,这样所有组件都有$router属性</span>
<span class="hljs-comment">// defineProperty(obj,属性名，属性值) 定义属性</span>
而这个  _router，就是我们在项目的 main.js中挂载进去的 router

<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'app'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'router'</span>

Vue.config.productionTip=<span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span>=></span>h(App)
&#125;)

<span class="hljs-comment">////////////////////////////////////////////</span>
而 <span class="hljs-built_in">this</span>.$route 表示的是我们配置的活跃中的路由（<span class="hljs-keyword">new</span> VueRouter创建的router对象中的映射）
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">导航守卫</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义：</span>
对路由跳转的过程进行监听,在监听函数里做操作
<span class="hljs-comment">// 引入：</span>
当我们点击 导航栏上的首页，新闻，信息时候，希望<span class="hljs-built_in">document</span>.title能够改变
我们可以利用组件中的生命周期函数：<span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-built_in">document</span>.title=<span class="hljs-string">'xxx'</span>&#125;
但是，一个个的改，效率低，麻烦
因为每次点击跳转，其实都是路由的跳转
所以：我们考虑能不能监听路由的跳转，在跳转的过程中操作
<span class="hljs-comment">// 方法:</span>
在routes数组 的路由对象中 加入 meta
&#123;
    <span class="hljs-attr">path</span>:<span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">component</span>:Home,
<span class="hljs-attr">meta</span>:&#123;   <span class="hljs-comment">// meta: 元数据 -- 描述数据的数据</span>
        <span class="hljs-attr">title</span>:<span class="hljs-string">'首页'</span>
    &#125;,
    <span class="hljs-attr">children</span>:[
        &#123;
            <span class="hljs-attr">path</span>:<span class="hljs-string">'xxx'</span>.......
        &#125;
    ]
&#125;
<span class="hljs-comment">// 前置钩子(hook/guard守卫) -- 钩子：回调</span>
<span class="hljs-comment">// 前置：在路由跳转之前, 同理有后置钩子，afterEach(hook)路由跳转后--不需要主动调用next </span>
router.afterEach(<span class="hljs-function">(<span class="hljs-params">to,<span class="hljs-keyword">from</span></span>)=></span>&#123;
    
&#125;)
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to,<span class="hljs-keyword">from</span>,next</span>) =></span> &#123;
    <span class="hljs-built_in">document</span>.title = to.meta.title
    next() <span class="hljs-comment">// 这里next调用,一定不能少,调用后才能进入下一个钩子</span>
&#125;)

但是有个问题，如果是涉及到路由嵌套
比如 首页home 内部 新闻 信息 也有路由的跳转，那么首页的title显示<span class="hljs-literal">undefined</span>
打印to，可以看到 home的 title不存在， 改进：

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to,<span class="hljs-keyword">from</span>,next</span>) =></span> &#123;
    <span class="hljs-built_in">document</span>.title = to.matched[<span class="hljs-number">0</span>].meta.title  <span class="hljs-comment">// 这样就没任何问题了</span>
    next()
&#125;)
<span class="hljs-comment">// 上述两个都是全局守卫 还有路由独享守卫，组件内守卫</span>
前置钩子，可以用于判断用户是否登录了，如果登录了，那么就执行next
否则 next(<span class="hljs-literal">false</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">保存路由状态</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入：</span>
Home同级有Profile，子级(嵌套路由有<span class="hljs-keyword">new</span>和message)
Home默认显示<span class="hljs-keyword">new</span>，用户在Home点击了message，之后去到Profile，
回来Home时，变成了<span class="hljs-keyword">new</span>，而不是原来的message

每次路由的跳转，都是一次旧的销毁和新的创建，
可以通过生命周期函数：<span class="hljs-function"><span class="hljs-title">destoryed</span>(<span class="hljs-params"></span>)</span>&#123; &#125; 检测  <span class="hljs-comment">// destoryed销毁后</span>

keep-alive: Vue 内置组件
router-view 也是一个组件，如果直接被包在keep-alive里面，所以路径匹配到的视图组件都会被缓存

<span class="hljs-comment">// 解决方案</span>
在App.vue中直接
<keep-alive> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">route-view</span>/></span></span> </keep-alive> 
keep-alive保证 组件不会被销毁

在Home.vue组件中，有<span class="hljs-keyword">new</span>和message两个嵌套路由，对应首页的新闻和信息
<span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">message</span>:<span class="hljs-string">'hello'</span>,
        <span class="hljs-attr">path</span>:<span class="hljs-string">'/home/news'</span>
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-title">activated</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.$router.push(<span class="hljs-built_in">this</span>.path);
&#125;
<span class="hljs-function"><span class="hljs-title">beforeRouteLeave</span>(<span class="hljs-params">to,<span class="hljs-keyword">from</span>,next</span>)</span>&#123;
<span class="hljs-built_in">this</span>.path = <span class="hljs-built_in">this</span>.$route.path
    next()
&#125;
<span class="hljs-comment">/*为什么不能用 activated 和 deactivated 
deactivated()&#123;
    this.path = this.$route.path;
&#125;
因为$route始终指向的是活跃的路由，activated为如果当前路由活跃的回调函数 deactivated就是不活跃时候调用，此时当前路由都不活跃了，$route自然不会指向自己，而是指向活跃的一边
当点击 用户界面的时候，this.$route已经是user了，而不是首页的信息
而beforeRouteLeave表示在路由跳转前回调

activated 和 deactivated 这两个函数只有在router-view使用了keep-alive包裹时才有效
*/</span>

<span class="hljs-comment">// 引入' :</span>
router-view被keep-alive包裹，相当于所有的路由对应组件都keep-alive缓冲不被销毁，
也就是说，每个路由的生命周期函数的created回调只有一次
但是如果要人为的给单独一个路由设置多次呢？

<keep-alive exclude=<span class="hljs-string">"组件名(.vue文件中export default中的name属性)"</span>>....</keep-alive>
<span class="hljs-comment">// exclude排除什么什么，include包括什么。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">TabBar案例</h3>
<pre><code class="hljs language-css copyable" lang="css">首先TabBar<span class="hljs-selector-class">.vue</span>给<span class="hljs-number">1</span>个插槽，该组件实现了，动态的内部插槽布局(<span class="hljs-attribute">flex</span>)样式
在TabBarItem<span class="hljs-selector-class">.vue</span>文件中给插槽 slot v-if v-else没有问题
这里的slot终将会被App<span class="hljs-selector-class">.vue</span>中插槽内容取代
因为v-if/else是先判断，然后选择要取代的其中一个slot（另一个插槽无效）
但是：
你如果在插槽上写动态的class，不行
<slot :class=<span class="hljs-string">"&#123;active: isActive&#125;"</span> name=<span class="hljs-string">"item-text"</span>></slot>
直接被 App.vue中的插槽内容替代了，而替代后的内容，没有动态class

解决方法：
    <div :class=<span class="hljs-string">"&#123;active: isActive&#125;"</span>>
      <slot name=<span class="hljs-string">"item-text"</span>></slot>
    </div>
为了保险起见，以后所有插槽如果有v-if/else，动态class等等，
都外包裹一个div，相关操作加 到div上
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">在案例中会用到svg图片，如果在抽离的过程中没有注意文件路径，很容易出错，而且改起来麻烦
所以，可以选择对文件起别名，
在项目文件build中的webpack<span class="hljs-selector-class">.base</span><span class="hljs-selector-class">.conf</span><span class="hljs-selector-class">.js</span>文件中，
resolve:&#123;
    <span class="hljs-string">'@'</span>:<span class="hljs-built_in">resolve</span>(<span class="hljs-string">'src'</span>)  代表给src路径起别名,叫做@
&#125;
所以我们可以这样改下，引入@作为src路径，之后就不用该路径了
import TabBar from <span class="hljs-string">'@/components/tabbar/TabBar'</span>

为了更方便,<span class="hljs-attribute">eg</span>:  CLI2
  <span class="hljs-attribute">alias</span>: &#123;
     '@': resolve(<span class="hljs-string">'src'</span>),
     <span class="hljs-string">'assets'</span>:resolve(<span class="hljs-string">'src/assets'</span>),    直接用@表示src,<span class="hljs-string">'@/assets'</span>---CLI3
     <span class="hljs-string">'components'</span>: resolve(<span class="hljs-string">'src/components'</span>),
     <span class="hljs-string">'views'</span>: resolve(<span class="hljs-string">'src/views'</span>),
  &#125;

该配置后，重新npm run dev

注意：
用别名的方法只能 直接 用在import的from上，如果要使用在img的src上。需要：
src=<span class="hljs-string">"~assets/img/tabbar/home.svg"</span>，在最前面加上符号 ~
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">Promise</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span> 是Es6一个特性，是异步编程的一种解决方案
<span class="hljs-comment">// 什么是同步？ 我们写的代码，一行行下来按顺序执行，就是一种同步。</span>
<span class="hljs-comment">// 同理，如果同步，我们发出网络请求，之后，无法响应用户的操作，必须等到收到请求资源/回应后</span>
才能响应用户的操作。
<span class="hljs-comment">// 因此：我们处理网络请求，需要异步，也就是响应用户操作的同时，发出网络请求，</span>
之后，继续响应用户操作，而网络请求--数据请求成功，则将数据通过传入的函数回调出去
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回调地狱</p>
<pre><code class="hljs language-js copyable" lang="js">但是如果网络请求十分复杂，就会出现回调地狱
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bdb72335e8543c0af3dd8b7fdac0cff~tplv-k3u1fbpfcp-watermark.image" alt="image-20210506104017376.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// executor 执行.exe </span>
具体内容 Vue-Day8，上课代码
<span class="hljs-comment">// sync 同步 synchronization</span>
<span class="hljs-comment">// async 异步 asynchronization</span>

<span class="hljs-comment">// fulfilled 满足的</span>
<span class="hljs-comment">// pending 等待的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Promise.all</p>
<pre><code class="hljs language-js copyable" lang="js">引入，如果有两个异步请求，用ajax去接，但是你不知道哪个请求先到，
而只有两个请求都到的时候，你才能进行操作。
不用<span class="hljs-built_in">Promise</span>.all的话，你只能定义两个boolean类型变量到处理函数handleResult()中,都接收到了<span class="hljs-literal">true</span>&&<span class="hljs-literal">true</span>

<span class="hljs-comment">// 例子</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span> 中，参数为函数
<span class="hljs-built_in">Promise</span>.all() 中为一数组，数组中放可迭代(可遍历)的对象
<span class="hljs-built_in">Promise</span>.all([
    <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>) =></span> &#123;
        $ajax(&#123;
            <span class="hljs-attr">url</span>:<span class="hljs-string">'url1'</span>,
            <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                resolve(data)
            &#125;
        &#125;)
    &#125;),
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>) =></span> &#123;
        $ajax(&#123;
            <span class="hljs-attr">url</span>:<span class="hljs-string">'url2'</span>,
            <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                resolve(data)
            &#125;
        &#125;)
    &#125;)
]).then(<span class="hljs-function"><span class="hljs-params">results</span> =></span> &#123; <span class="hljs-comment">// 这样两个请求的回馈都保存在了 results 数组中</span>
    <span class="hljs-comment">// 这里代码为：当两个数据都接收到后执行</span>
    results[<span class="hljs-number">0</span>]******
    results[<span class="hljs-number">1</span>]******
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">Vuex</h2>
<pre><code class="hljs language-js copyable" lang="js">Vuex 组件的状态管理 (大管家)
也就是，多个组件之间，他们的状态(目前理解为：变量,变量一般用来保存状态)希望可以共享
依据组件树，底层要向高层，隔层太多，请求麻烦
可以建立一个对象，作为中间人集中管理状态---vuex还是响应式的
<span class="hljs-comment">// 响应式是关键，当对象中的变量发生改变，相应的，应用了这个变量的组件也会进行刷新</span>
如果不是响应式，那么就其他的实现方法了，比如：
<span class="hljs-keyword">const</span> ShareObj = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'why'</span>,
&#125;
Vue.prototype.ShareObj = ShareObj
之后Vue实例组件以及在其中注册的组件，都可以通过
<span class="hljs-built_in">this</span>.ShareObj.name来访问
<span class="hljs-comment">// 但是没有响应式，你把name改了，相应组件中变量不会发生相应的变化</span>

管理的状态：
token证书，用户信息，登录状态，地理位置
商品收藏，购物车等等
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">最基本的使用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// npm install vuex --save</span>

类似与router,要先 
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span> 然后 
Vue.use(Vuex)
为了防止main.js过大，另外放到一个文件夹
创建文件夹, 不要命名为vuex，而是 store <span class="hljs-comment">// store 仓库</span>

在store文件夹下创建index.js
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
Vue.use(Vuex)
<span class="hljs-comment">// 创建对象，这里有点不同</span>
<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-attr">state</span>: &#123;
        <span class="hljs-comment">// 保存状态</span>
        <span class="hljs-attr">counter</span>:<span class="hljs-number">1000</span> <span class="hljs-comment">// 其他.vue组件的template标签中可以通过 $store.state.counter引用（响应式）</span>
    &#125;,
    <span class="hljs-attr">mutations</span>: &#123;
       <span class="hljs-comment">// 方法</span>
        <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params">state</span>)</span>&#123; <span class="hljs-comment">// 这里的state直接默认就是上面的state对象，不需要加this</span>
            state.counter++
        &#125;,
        <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params">state</span>)</span>&#123;
            state.counter--
        &#125;
    &#125;,
    <span class="hljs-attr">actions</span>: &#123;
        
    &#125;,
    <span class="hljs-attr">getters</span>: &#123;
        
    &#125;,
    <span class="hljs-attr">modules</span>: &#123;
        
    &#125;
&#125;)
<span class="hljs-comment">// 导出store对象</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store

<span class="hljs-comment">// 最后在main.js中挂载一下</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
    store, <span class="hljs-comment">// 本质上为 Vue.prototype.$store = store 全局属性，和router很像</span>
    <span class="hljs-attr">methods</span>: &#123;
<span class="hljs-comment">// <button @click="addition">++</button></span>
<span class="hljs-comment">// <button @click="subtraction">--</button>        </span>
        <span class="hljs-function"><span class="hljs-title">addition</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'increment'</span>)
        &#125;,
        <span class="hljs-function"><span class="hljs-title">subtraction</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'decrement'</span>)
        &#125;,
    &#125;
        <span class="hljs-comment">// 如果函数有参数 count</span>
        <span class="hljs-function"><span class="hljs-title">subtraction</span>(<span class="hljs-params">count</span>)</span>&#123;
            <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'decrement'</span>,count)
    &#125;
        <span class="hljs-comment">// 对应的mutation中</span>
<span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params">state,count</span>)</span>&#123;
            state.counter -= count
        &#125;
<span class="hljs-comment">// 最后在App.vue的template组件中<button @click="decrement(5)" >-5</button></span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2d66401342143ba81fdea9d28d1c3f8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210506210525874.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css">Devtools 可以记录每一次State的状态
因为要按着图中顺序来，所以上文中，如果
<<span class="hljs-selector-tag">div</span>>&#123;&#123;$store<span class="hljs-selector-class">.state</span><span class="hljs-selector-class">.counter</span>&#125;&#125;</<span class="hljs-selector-tag">div</span>>
<<span class="hljs-selector-tag">button</span> <span class="hljs-keyword">@click</span>="$store.state.counter++">
相当于直接从Vue Components连接到State，虽然能改变counter的值，但是逆向了
    Devtools不能跟踪State的状态了
所以要想修改 State。一定通过Mutations,不然调试的时候，devtools里你显示不出来state的变化
    
但是允许跳过Action，直接从Vue Components到Mutation
    Action的作用：当你修改Mutation的时候，如果你有异步操作,一定先到Action里面做
    (Devtools只能跟踪同步操作)
    而异步操作通常为：发送网络请求,所以连接到Backend API（<span class="hljs-attribute">backend</span>:后端，frontend：前端）
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">核心的概念</h3>
<h4 data-id="heading-33">getters</h4>
<pre><code class="hljs language-css copyable" lang="css">State单一状态树: 英文名 Sing Source of Truth----单一数据源

Getters:类似单个组件的计算属性（当某一个数据需要经过一系列变化后显示到页面，就用计算属性）

state: &#123;counter: <span class="hljs-number">1000</span>&#125;
getters: &#123;
        <span class="hljs-built_in">powerCounter</span>(state)&#123;
            return state.counter * state.counter
        &#125;,
        // 你不需要在每一个组件中写相应的 methods函数，直接$store<span class="hljs-selector-class">.getters</span><span class="hljs-selector-class">.powerCounter</span>即可
&#125;
<<span class="hljs-selector-tag">h2</span>>&#123;&#123;$store<span class="hljs-selector-class">.getters</span><span class="hljs-selector-class">.powerCounter</span>&#125;&#125;

补充：
<span class="hljs-number">1</span>.
getters中的函数也可以调用getters中的函数，比如：
    powerCounter2(state,getters)&#123; return getters<span class="hljs-selector-class">.powerCounter</span><span class="hljs-selector-class">.length</span>&#125;
所有函数的第二个参数，不管叫什么，都是代表的getters
<span class="hljs-number">2</span>. 
如果要让 别人在template标签中传入数据，而自己函数在getters中又没有新参数去容纳数据
就return一个函数,函数内部再return
比如：
    moreAgeStu(state)&#123;
        return age => &#123;
            return state<span class="hljs-selector-class">.students</span><span class="hljs-selector-class">.filter</span>(s => s<span class="hljs-selector-class">.age</span>>age)
        &#125;
    &#125;
<<span class="hljs-selector-tag">h2</span>>&#123;&#123;$store<span class="hljs-selector-class">.getters</span><span class="hljs-selector-class">.moreAgeStu</span>(<span class="hljs-number">8</span>)&#125;&#125;</<span class="hljs-selector-tag">h2</span>>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">mutations</h4>
<pre><code class="hljs language-css copyable" lang="css">Mutation: Vuex的store状态的唯一更新方式：提交Mutation
当我们更新数据的时候，可能希望携带一些额外的参数（mutation的载荷/负载 Payload）
这里就引入了 提交的方式，在App.vue中，methods: 
第一种   <span class="hljs-built_in">addCount</span>(count)&#123; 
    this.$store.<span class="hljs-built_in">commit</span>(<span class="hljs-string">'incrementCount'</span>,count)
&#125;
第二种   addCount(count)&#123; 
    this.$store<span class="hljs-selector-class">.commit</span>(&#123;
        type:<span class="hljs-string">'incrementCount'</span>,
        count,
    &#125;)
&#125;
如果传给函数的参数count为 数字<span class="hljs-number">5</span>， 按照第一种，传过去的是Number <span class="hljs-number">5</span>
但是按照第二种，count无论如何都是作为参数---一个对象payload--的属性存在，如下
mutations:&#123;
        <span class="hljs-built_in">incrementCount</span>(state,payload) &#123;
            state.counter += payload.count
        &#125;
    &#125;

官方建议mutations的写法： 
在store文件夹下，创建一个mutations-types<span class="hljs-selector-class">.js</span> 文件里面放置 函数名
eg:  export const INCREMENT =<span class="hljs-string">'increment'</span>

在store文件夹的index.js文件中，
import &#123;
    INCREMENT
&#125; <span class="hljs-selector-tag">from</span> './store/mutations-types'
mutations: &#123;
    [INCREMENT](state)&#123; state.counter++  &#125;,
&#125;

在App<span class="hljs-selector-class">.vue</span>文件中， 
import &#123;
    INCREMENT
&#125; <span class="hljs-selector-tag">from</span> './store/mutations-types'



如果在mutations中的函数updateInfo中，加入
    setTimeout(()=>&#123;
        state<span class="hljs-selector-class">.info</span><span class="hljs-selector-class">.name</span>='xxxx'
    &#125;,<span class="hljs-number">1000</span>)
state的数据会改变的，但是，调试的时候，因为你是异步操作，而不是同步操作
即使页面上显示的是修改之后的数据，但是调试工具显示的值，是未修改的

那么，就需要 actions 了
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">actions</h4>
<pre><code class="hljs language-css copyable" lang="css">Action
actions: &#123;
    内部的函数也都有默认的参数，getters和mutations都有默认的state，
    而actions的默认参数为 context ----上下文，
    可以暂时将context理解为 store对象  (const store=new Vuex.<span class="hljs-built_in">Store</span>(&#123;......&#125;))
&#125;
现在要解决上面的那个异步问题
mutations: &#123;
    <span class="hljs-built_in">updateInfo</span>(state) &#123;
        state.info.name = <span class="hljs-string">"xxx"</span>
    &#125;
&#125;,
actions: &#123;
    <span class="hljs-built_in">For_UpdateInfo</span>(context) &#123;
        <span class="hljs-built_in">setTimeout</span>(() => &#123;
            context.<span class="hljs-built_in">commit</span>(<span class="hljs-string">'updateInfo'</span>)
        &#125;,<span class="hljs-number">1000</span>)
    &#125;
&#125;,
App<span class="hljs-selector-class">.vue</span>中，methods: &#123;
    <span class="hljs-built_in">updateInfo</span>() &#123;
        this.$store.<span class="hljs-built_in">dispatch</span>(<span class="hljs-string">'For_UpdateInfo'</span>)
    &#125;
&#125;

actions:中也是可以传递参数的，payload，原理和前面同

技巧：
你在App.vue 中的this.$store.<span class="hljs-built_in">dispatch</span>(<span class="hljs-string">'For_UpdateInfo'</span>，<span class="hljs-string">'aaa'</span>)
这里调用了 For_UpdateInfo函数,

如果该函数返回一个promise对象，eg:
在store的index.js中：

<span class="hljs-built_in">For_UpdateInfo</span>(context,payload) &#123;
        return new <span class="hljs-built_in">Promise</span>((resolve,reject) => &#123; 
            <span class="hljs-built_in">setTimeout</span>(() => &#123;
                context.<span class="hljs-built_in">commit</span>(<span class="hljs-string">'updateInfo'</span>);
                console<span class="hljs-selector-class">.log</span>(payload); //  aaa
                resolve(<span class="hljs-number">111</span>)
            &#125;,<span class="hljs-number">1000</span>)
        &#125;)   
    &#125;

那么相当于，会把return的 new Promise((resolve,reject) => &#123;....<span class="hljs-selector-class">.resolve</span>(<span class="hljs-number">111</span>).... &#125;)
返回到App<span class="hljs-selector-class">.vue</span>中this.$store<span class="hljs-selector-class">.dispatch</span>('For_UpdateInfo'，'aaa')的位置，并替代原代码
那么你大可在App<span class="hljs-selector-class">.vue</span>文件中：

this.$store
<span class="hljs-selector-class">.dispatch</span>('For_UpdateInfo'，'aaa')
<span class="hljs-selector-class">.then</span>( res => &#123;
    console<span class="hljs-selector-class">.log</span>(res);   // <span class="hljs-number">111</span>
&#125;)


而较为差一点的方法，就是在App<span class="hljs-selector-class">.vue</span>文件中，
updateInfo()&#123;
    this.$store<span class="hljs-selector-class">.dispatch</span>('For_UpdateInfo',&#123;
        第二个参数传入一个对象
        message:<span class="hljs-string">'aaaa'</span>,
        success: () => &#123;
            console.<span class="hljs-built_in">log</span>(<span class="hljs-string">'xxxx'</span>)
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">modules</h4>
<pre><code class="hljs language-css copyable" lang="css">Module
一个store变得臃肿的时候，可以将store分割成模块Module，每个模块有自己的state，mutations，actions...
eg:
    const moduleA = &#123; state: &#123;....&#125;, mutations:&#123;...&#125;, ....&#125;
    const store = new Vuex<span class="hljs-selector-class">.Store</span>(&#123;
        state: &#123;....&#125;,
        modules: &#123;
            a: moduleA,
        &#125;
    &#125;)
但是本质上，<span class="hljs-selector-tag">a</span>: moduleA 最后是被放到了 state里面，
在template中： &#123;&#123;$store.state.a&#125;&#125;
modules中定义的mutations，在App<span class="hljs-selector-class">.vue</span>文件中正常commit就行

在模块modules中的方法，可以有第三个参数，rootState，可以访问最大的，非modules的state
模块modules中actions:的方法的参数，context不是指的最大的store，
这里的context.commit只会提交自己的mutations
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">响应式补充</h3>
<pre><code class="hljs language-js copyable" lang="js">要想响应式，前提是你的变量要在state提前声明好，才能添加到响应式系统，
而不是后期动态加入(会增加到state中，但是无响应式)

<span class="hljs-comment">// 非响应式</span>
<span class="hljs-built_in">this</span>.letter[<span class="hljs-number">0</span>]=<span class="hljs-string">'aaa'</span> 

<span class="hljs-keyword">delete</span> state.info.age


<span class="hljs-comment">// 响应式</span>
<span class="hljs-built_in">this</span>.letter.splice(<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-string">'aaa'</span>)
Vue.set(<span class="hljs-built_in">this</span>.letter, <span class="hljs-number">0</span>,<span class="hljs-string">'aaa'</span>) ---> 此方法也可应用于对象

Vue.delete(state.info,<span class="hljs-string">'age'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">抽离</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 首先，语法补充</span>
 <span class="hljs-keyword">const</span> obj = &#123;
     <span class="hljs-attr">name</span>:<span class="hljs-string">'xxx'</span>,
     <span class="hljs-attr">age</span>:<span class="hljs-number">18</span>,
     <span class="hljs-attr">height</span>:<span class="hljs-number">1.8</span>,
     <span class="hljs-attr">address</span>:<span class="hljs-string">'china'</span>
 &#125;
<span class="hljs-comment">// 解构,obj对象我只拿两个属性</span>
 <span class="hljs-keyword">const</span> &#123;name,height&#125; = obj;
 
<span class="hljs-comment">// 数组的解构</span>
 <span class="hljs-keyword">const</span> names = [<span class="hljs-string">'why'</span>,<span class="hljs-string">'kobe'</span>,<span class="hljs-string">'james'</span>]
 <span class="hljs-keyword">const</span> [name1,name2,name3] = names;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b6aeab9761c485cb5350c95e2a8e0c6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210511200511649.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4294c547e55d46b2a3b142e0daf6119b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210511201137211.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-39">axios网络模块封装</h2>
<pre><code class="hljs language-css copyable" lang="css">axios---可暂时理解为: ajax io system
测试用的网站:  httpbin.org
项目用服务器： <span class="hljs-number">123.207</span>.<span class="hljs-number">32.32</span>:<span class="hljs-number">8000</span>
接口： http://<span class="hljs-number">123.207</span>.<span class="hljs-number">32.32</span>:<span class="hljs-number">8000</span>/home/multidata
  http://<span class="hljs-number">123.207</span>.<span class="hljs-number">32.32</span>:<span class="hljs-number">8000</span>/home/data?type=sell&page=<span class="hljs-number">3</span>
status:<span class="hljs-number">200</span> 请求成功


安装--- npm install axios --save
main.js中
import axios from <span class="hljs-string">'.......'</span>
<span class="hljs-built_in">axios</span>(&#123;
    url:<span class="hljs-string">'http://123.207.32.32:8000/home/multidata'</span>   // 只传url，默认get请求
    method: <span class="hljs-string">'get'</span>  // 手动修改模式get/put
&#125;)<span class="hljs-selector-class">.then</span>(res => &#123;      // 因为会直接返回一个Promise对象，所以<span class="hljs-selector-class">.then</span>
    console<span class="hljs-selector-class">.log</span>(res);
&#125;)
axios(&#123;
    url:<span class="hljs-string">'http://123.207.32.32:8000/home/data'</span>
    params:&#123;     // 专门针对get请求的参数拼接
    type: <span class="hljs-string">'sell'</span>,
        page: <span class="hljs-number">3</span>
    &#125;  // 相当于 url:<span class="hljs-string">'http://123.207.32.32:8000/home/data?type=sell&page=3'</span>
&#125;)<span class="hljs-selector-class">.then</span>(res => &#123;
    console<span class="hljs-selector-class">.log</span>(res);
&#125;)
也可以：
axios<span class="hljs-selector-class">.get</span>(....)


结果: console.<span class="hljs-built_in">log</span>(res)这个res是一个Object, 服务器返回的数据都在data里面
其他的属性都是axios框架生成的

axios.all可以对多个网络请求进行合并,axios.all---传入数组，数组里面写要发出的请求
axios.<span class="hljs-built_in">all</span>([<span class="hljs-built_in">axios</span>(&#123;
    url: <span class="hljs-string">'http://123.207.32.32:8000/home/data'</span>
&#125;),axios(&#123;
    url:<span class="hljs-string">'http://123.207.32.32:8000/home/data'</span>
    params: &#123;
    type:<span class="hljs-string">'sell'</span>,
        page:<span class="hljs-number">5</span>
    &#125;
&#125;)])  // axios返回一个数组，可以用axios<span class="hljs-selector-class">.spread</span>展开
<span class="hljs-selector-class">.then</span>(axios<span class="hljs-selector-class">.spread</span>((res1,res2) => &#123;
    console<span class="hljs-selector-class">.log</span>(res1);
    console<span class="hljs-selector-class">.log</span>(res2);
&#125;))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">全局配置</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">main</span><span class="hljs-selector-class">.js</span>
// 记得： default + s
axios<span class="hljs-selector-class">.defaults</span><span class="hljs-selector-class">.baseURL</span> = '....' 
axios<span class="hljs-selector-class">.defaults</span><span class="hljs-selector-class">.timeout</span> = <span class="hljs-number">5000</span>  // 毫秒，超时
axios<span class="hljs-selector-class">.defaults</span><span class="hljs-selector-class">.headers</span><span class="hljs-selector-class">.post</span><span class="hljs-selector-attr">[<span class="hljs-string">'Content-Type'</span>]</span> ='application/x-www-<span class="hljs-selector-tag">form</span>-urlencoded'
等等
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4c7e9f5fed641809ec57054cb731c32~tplv-k3u1fbpfcp-watermark.image" alt="image-20210511235941074.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-41">改进</h4>
<pre><code class="hljs language-js copyable" lang="js">当业务多的时候，全局配置就不适用了

<span class="hljs-comment">// 创建对应的axios的实例</span>

<span class="hljs-keyword">const</span> instance1 = axios.create(&#123;
    <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://123.207.32.32:8000'</span>,
    <span class="hljs-attr">timeout</span>:<span class="hljs-number">5000</span>
&#125;)



<span class="hljs-comment">// 利用实例instance1给几个发送的网络请求设置相同的baseURL</span>

instance1(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/home/multidata'</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res);
&#125;)

instance1(&#123;
    <span class="hljs-attr">url</span>:<span class="hljs-string">'/home/data'</span>,
    <span class="hljs-attr">params</span>:&#123;
        <span class="hljs-attr">type</span>:<span class="hljs-string">'pop'</span>,
        <span class="hljs-attr">page</span>: <span class="hljs-number">1</span>
    &#125;
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res);
&#125;)

<span class="hljs-comment">// 同理，之后就 onst instance2 = axios.create(&#123; baseURL:'http://222.......' &#125;)</span>

也可以在每一个.vue组件中，<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span> 然后 
利用生命周期钩子，<span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123; axios(&#123;<span class="hljs-attr">ulr</span>:<span class="hljs-string">'http:.....'</span>&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;<span class="hljs-built_in">this</span>.data里面数据=res&#125;) &#125;
拿到请求数据，但是不好，对第三方框架依赖性太强了

以后但凡是一个项目里面要用到第三方的框架，绝对，要有封装的思想
涉及到网络层的东西都封装到src文件的network文件夹下
axios都整到，network的request.js下
为了导出多个实例，不用 <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>
而是 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params"></span>)</span>&#123; &#125; <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">instance</span>(<span class="hljs-params"></span>)</span>&#123; &#125; ....

<span class="hljs-comment">// request.js</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-keyword">const</span> instance = axios.create(&#123;
        <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://123.207.32.32:8000'</span>
        <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>
    &#125;)
    <span class="hljs-comment">// 发送真正的网络请求</span>
    instance(config).then( <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-comment">// 结果应该传出去，而不是在这里处理</span>
    &#125;).catch( <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-comment">// 这里也是，想办法回调出去</span>
    &#125;)
&#125;

<span class="hljs-comment">// 把结果回调出去的方式</span>
<span class="hljs-comment">///////////////////////////////////////////////////////////</span>
<span class="hljs-number">1.</span> 
<span class="hljs-comment">// 传入的参数success和failure为函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config, success, failure</span>)</span>&#123;
    <span class="hljs-keyword">const</span> instance = axios.create(&#123;
        <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://123.207.32.32:8000'</span>
        <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>
    &#125;)
instance(config).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        success(res) <span class="hljs-comment">// 把收到的数据res作为参数传入 main.js中传过来的函数success</span>
    &#125;)
    .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        failure(err)
    &#125;)
&#125;

<span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> &#123;request&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./network/request'</span>;
request(&#123;
    <span class="hljs-attr">url</span>:<span class="hljs-string">'/home/multidata'</span>
&#125;, <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;   <span class="hljs-comment">// 相当于 传过去给了success一个匿名函数，参数为res</span>
    <span class="hljs-built_in">console</span>.log(res);
&#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)

<span class="hljs-comment">///////////////////////////////////////////////////////////</span>

<span class="hljs-number">2.</span> 
<span class="hljs-comment">// request.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-keyword">const</span> instance = axios.create(&#123;
        <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://123.207.32.32:8000'</span>
        <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>
    &#125;)
    instance(config.baseConfig)
    .then( <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        config.success(res);
    &#125;).catch( <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        config.failure(err);
    &#125;)
&#125;
<span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> &#123;request&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./network/request'</span>;
request(&#123;
    <span class="hljs-attr">baseConfig</span>: &#123;
        
    &#125;,
    <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>) </span>&#123;
        
    &#125;,
    <span class="hljs-attr">failure</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
        
    &#125;
&#125;)

<span class="hljs-comment">/////////////////////////////////////////////////////////////////////</span>

<span class="hljs-comment">// 第三种，最终方案</span>
<span class="hljs-comment">// request.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> instance = axios.create(&#123;
            <span class="hljs-attr">baseURL</span>:<span class="hljs-string">'http://123.207.32.32:8000'</span>,
            <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>
        &#125;)
        instance(config)
        .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            resolve(res)
        &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            reject(err)
        &#125;)
    &#125;)
&#125;
<span class="hljs-comment">// 或者--> 最好这个</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-comment">// 1.创造axios实例</span>
    <span class="hljs-keyword">const</span> instance = axios.create(&#123;
        <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://123.207.32.32:8000'</span>,
        <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>
    &#125;)
    <span class="hljs-comment">// 3. 发送真正的网络请求</span>
    <span class="hljs-keyword">return</span> instance(config) <span class="hljs-comment">// instance(config)调用后本身就返回一个promise</span>
&#125;

<span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> &#123;request&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./network/request'</span>;
request(&#123;
    <span class="hljs-attr">url</span>:<span class="hljs-string">'/home/multidata'</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">拦截</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  request.js</span>
请求成功/失败，响应成功/失败，一共四种拦截

<span class="hljs-comment">// 请求拦截</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-comment">// 1.创造axios实例</span>
    <span class="hljs-keyword">const</span> instance = axios.create(&#123;
        <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://123.207.32.32:8000'</span>,
        <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>
    &#125;)
    <span class="hljs-comment">// 2. axios的拦截器</span>
    <span class="hljs-comment">// use两个参数，一个代表请求/响应成功，另一个代表..失败</span>
    axios.interceptors.request.use();  <span class="hljs-comment">//全局的</span>
    
    instance.interceptors.request.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(config);
        <span class="hljs-keyword">return</span> config <span class="hljs-comment">// 如果没有return，这里就把数据拦截了，那你main.js相应操作会报错</span>
    &#125;,<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(err);
    &#125;);  <span class="hljs-comment">//只给instance的请求</span>
    <span class="hljs-comment">// 这里可以看出use第一个参数为config,第二个为err</span>
    
    instance.interceptors.response.use();  <span class="hljs-comment">//只给instance的响应    </span>
 <span class="hljs-comment">// 请求拦截的几个适用情况：</span>
    <span class="hljs-number">1.</span> config中一些信息不符合服务器的要求，需要修饰一下
    <span class="hljs-number">2.</span> 每次发送网络请求的时候，界面中显示的一个请求的图标
    <span class="hljs-number">3.</span> 某些网络请求（比如登录token），必须携带一些特殊信息
    
    <span class="hljs-comment">// 3. 发送真正的网络请求</span>
    <span class="hljs-keyword">return</span> instance(config) <span class="hljs-comment">// instance(config)调用后本身就返回一个promise</span>
&#125;

<span class="hljs-comment">// 响应拦截</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;
    
    <span class="hljs-keyword">const</span> instance = axios.create(&#123;
        <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://123.207.32.32:8000'</span>,
        <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>
    &#125;)
    
    instance.interceptors.response.use(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res); <span class="hljs-comment">// 真正要用的，只是res.data</span>
        <span class="hljs-keyword">return</span> res.data
    &#125;,<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(err);
    &#125;);
    
    <span class="hljs-keyword">return</span> instance(config)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr></div>  
</div>
            