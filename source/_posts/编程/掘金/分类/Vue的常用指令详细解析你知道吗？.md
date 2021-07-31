
---
title: 'Vue的常用指令详细解析你知道吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=62'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 02:11:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=62'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>总结一笔</strong>：</p>
<h2 data-id="heading-0">1.自定义事件的事件名字大小写问题</h2>
<p>跟组件和 prop 不同，事件名不存在任何自动化的大小写转换。而是触发的事件名需要完全匹配监听这个事件所用的名称。举个例子，如果触发一个 camelCase 名字的事件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'myEvent'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>则监听这个名字的 kebab-case 版本是不会有任何效果的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><my-component v-on:my-event=<span class="hljs-string">"doSomething"</span>></my-component>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跟组件和 prop 不同，事件名不会被用作一个 JavaScript 变量名或属性名，所以就没有理由使用 camelCase 或 PascalCase 了。并且 v-on 事件监听器在 DOM 模板中会被自动转换为全小写 (因为 HTML 是大小写不敏感的)，所以 v-on:myEvent 将会变成 v-on:myevent——导致 myEvent 不可能被监听到。</p>
<p>因此，推荐你始终使用 kebab-case 的事件名。</p>
<h2 data-id="heading-1">2. vue几种常用的指令</h2>
<p><strong>v-bind</strong>: 行间属性绑定 或者用冒号 :</p>
<p><strong>v-bind:title</strong>  鼠标移上的显示</p>
<p><strong>v-bind</strong>:src  绑定图片路径</p>
<p><strong>v-bind</strong>:html 绑定HTML文本和标签</p>
<p><strong>v-bind</strong>:text 绑定文本 （字符串）</p>
<p><strong>v-bind</strong>:class 绑定类样式（数组）</p>
<p><strong>v-bind</strong>:style  动态绑定样式 （对象）</p>
<p><strong>v-for</strong>: 1.x 和 2.x是不一样的</p>
<p><strong>v-fo</strong>r="i in json"</p>
<p><strong>v-for="(key, value) in json"</strong></p>
<h2 data-id="heading-2">3. vue中 key 值的作用？</h2>
<ul>
<li>当 Vue.js 用 v-for 正在更新已渲染过的元素列表时，它默认用“就地复用”策略。如果数据项的顺序被改变，Vue 将不会移动
DOM 元素来匹配数据项的顺序，
而是简单复用此处每个元素，并且确保它在特定索引下显示已被渲染过的每个元素。key的作用主要是为了高效的更新虚拟DOM。</li>
</ul>
<h2 data-id="heading-3">4. 描述vuex</h2>
<p>vuex用于组件之间共享数据 以store作为容器 <strong>state</strong>：用来存储共享数据， 数据池 <strong>getters</strong>：用来获取处理过后的数据，具有缓存的作用 <strong>mutations</strong>： 同步提交状态的更改 <strong>actions</strong>:异步提交状态的更改 <strong>module</strong>：当状态管理多了， 使用module来划分多个模块</p>
<h2 data-id="heading-4">5. $watch</h2>
<p>监听对象中的data里面的数据的变化
var vue = new Vue ( &#123; el:'#root', data:&#123; a:"", b:"" &#125; &#125;); 开启监控：， 返回值是停止监控的函数 var watchA = vue.$watch('a', function(newValue, oldValue)&#123; vue.c = vue.a // 这样a改变就会执行函数 &#125;); 停止监控： watchA()</p>
<h2 data-id="heading-5">6. 全局组件</h2>
<p>组件输出 -> 打包（给包组件命名，作为标签名使用） -> 输出打包后的模块 -> Vue.use(模块名) -> <全局组件名字 /></p>
<p>打包组件的js文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> cp1 <span class="hljs-keyword">from</span> <span class="hljs-string">'./cp1.vue'</span>
<span class="hljs-keyword">import</span> cp1 <span class="hljs-keyword">from</span> <span class="hljs-string">'./cp1.vue'</span>
<span class="hljs-keyword">let</span> package = &#123;
    <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">vue</span>)</span>&#123;
        vue.component(<span class="hljs-string">'cp1'</span>, cp1)
        vue.component(<span class="hljs-string">'cp2'</span>, cp2)
    &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> package;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> package <span class="hljs-keyword">from</span> <span class="hljs-string">"globalCp"</span>
Vue.use(package)
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他vue文件直接使用即可</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><cp1></cp1>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">7.单选下拉框</h2>
<pre><code class="copyable">1、通过select定义下拉框，通过option定义选项，，默认是一个单选下拉框
2、可以通过v-model指令，实现数据双向绑定，V-model指令绑定给select元素，由于单选框默认只能选中一个值，因3、此我们绑定一个字符串Option选项的值，没有value属性，是内容值，有value属性，就是value
注：1.0 版本中selected优先级高于绑定的数据； 2.0 版本中selected优先级低于绑定的

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="app">
        <select v-model="colors">
            <option value="isRed">red</option>
            <option value="isGreen">green</option>
            <option value="isBlue">blue</option>
        </select>
        <h1>查看结果 &#123;&#123;colors&#125;&#125;</h1>
    </div>
    <script type="text/javascript" src="vue.js"></script>
    <script type="text/javascript">
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                colors: 'isGreen'
            &#125;
        &#125;)
    </script>
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">8.多选下拉框</h2>
<pre><code class="copyable">1、将单选下拉框变成多选下拉框，只需要给select元素添加multiple属性
2、此时下拉框的值将变成给一个数组了，每一个成员代表一个选中的选项
3、选项的值：没有value属性，就是内容值、有value属性，就是value值
注：1.0 版本中selected优先级高于绑定的数据； 2.0 版本中selected优先级低于绑定的数据、

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="app">
        <select v-model="colors" multiple>
            <option value="isRed">red</option>
            <option value="isGreen">green</option>
            <option value="isBlue">blue</option>
        </select>
        <h1>查看结果 &#123;&#123;colors&#125;&#125;</h1>
    </div>
    <script type="text/javascript" src="vue.js"></script>
    <script type="text/javascript">
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                colors: ['isRed','isGreen']
            &#125;
        &#125;)
    </script>
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            