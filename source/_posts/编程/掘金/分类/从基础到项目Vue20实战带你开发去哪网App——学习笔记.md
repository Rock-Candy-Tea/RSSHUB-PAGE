
---
title: '从基础到项目Vue2.0实战带你开发去哪网App——学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9101'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:19:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=9101'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">第2章 课程介绍</h1>
<h2 data-id="heading-1">2.1 课程学习方法</h2>
<h3 data-id="heading-2">1.官方文档的阅读</h3>
<h3 data-id="heading-3">2.Vue实例的练习</h3>
<h3 data-id="heading-4">3.实战</h3>
<h2 data-id="heading-5">2.2 hello world</h2>
<h3 data-id="heading-6">1.Vue不支持IE8及以下的浏览器（支持所有兼容ECMAScript5的浏览器）</h3>
<h3 data-id="heading-7">2.<code><script></code>引入js的方式进行学习（开发版本）</h3>
<h3 data-id="heading-8">3.el：限制Vue处理Dom的范围  data：定义数据  &#123;&#123;&#125;&#125;:插值表达式</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>2.2节Hello World</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">&#123;&#123; content &#125;&#125;</div>
    <script>
        // 直接操作DOM写法
        // var dom = document.getElementById('app');
        // dom.innerHTML = 'hello Vuejs';
        // setTimeout(function() &#123;
        //     dom.innerHTML = 'bye Vue.js'
        // &#125;, 2000)

        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                content: 'hello Vuejs'
            &#125;
        &#125;)
        setTimeout(function() &#123;
            app.$data.content = 'bye Vue.js'
        &#125;, 2000)
        
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">2.3 开发TodoList（v-model、v-for、v-on）</h2>
<h3 data-id="heading-10">1.TodoList参考：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.todolist.cn" target="_blank" rel="nofollow noopener noreferrer" title="http://www.todolist.cn" ref="nofollow noopener noreferrer">www.todolist.cn</a></h3>
<h3 data-id="heading-11">2.v-for:用来循环数据</h3>
<p><code><li v-for="item in list">&#123;&#123; item &#125;&#125;</li></code></p>
<h3 data-id="heading-12">3.v-on:click:绑定click事件</h3>
<p><code><button v-on:click="handleBtnClick">提交</button></code></p>
<h3 data-id="heading-13">4.v-model:数据的双向绑定</h3>
<p><code><input type="text" v-model="inputValue"></code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>2.3节TodoList-V1.0部分功能</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <!-- v-model:数据的双向绑定 -->
        <input type="text" v-model="inputValue">
        <!-- v-on:click:绑定click事件 -->
        <button v-on:click="handleBtnClick">提交</button>
        <ul>
            <!-- v-for:用来循环数据 -->
            <li v-for="item in list">&#123;&#123; item &#125;&#125;</li>
        </ul>
    </div>
    <script>
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                list: [],
                inputValue: ''
            &#125;,
            methods: &#123;
                handleBtnClick: function()&#123;
                    this.list.push(this.inputValue)
                    this.inputValue = ''
                &#125;
            &#125;
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">2.4 MVVM（设计）模式</h2>
<h3 data-id="heading-15">1.MVP -> 使用jQuery完成TodoList：面向DOM</h3>
<p><code>View->Presenter->Model</code></p>
<p><code>View<-Presenter<-Model</code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>2.4节TodoList-jquery部分功能</title>
    <script src="../jquery.js"></script>
</head>
<body>
    <div>
        <input id="input" type="text">
        <button id="btn">提交</button>
        <ul id="list"></ul>
    </div>
    <script>
        // MVP设计模式 M:模型层 (无);V:视图;P:控制器;
        function Page() &#123;   
        &#125;
        $.extend(Page.prototype, &#123;
            init: function () &#123;
                var btn = $('#btn');
                btn.on('click', $.proxy(this.handleBtnClick, this))
            &#125;,
            handleBtnClick: function () &#123;
                var inputEle = $('#input');
                var inputValue = $('#input').val();
                var ulEle = $('#list');
                ulEle.append('<li>' + inputValue + '</li>');
                inputEle.val('');
            &#125;
        &#125;)
        var page = new Page();
        page.init();
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">2.MVVM -> 通过操作数据来改变视图：面向数据</h3>
<p><code>View->ViewModel->Model</code></p>
<p><code>View<-ViewModel<-Model</code></p>
<h4 data-id="heading-17">2.1 View:DOM    Model:Plain JavaScript Objects  ViewModel:Vue</h4>
<blockquote>
<h4 data-id="heading-18">2.2 ES5中的API：<code>①：Object.define.protype   ①：虚拟DOM</code></h4>
</blockquote>
<h2 data-id="heading-19">2.5 前端组件化</h2>
<h3 data-id="heading-20">1.一个整体切分为不同的部分，每个部分就是一个组件</h3>
<h3 data-id="heading-21">2. 一个组件就是页面上的一个区域</h3>
<h2 data-id="heading-22">2.6 使用组件改造TodoList</h2>
<h3 data-id="heading-23">1.全局组件</h3>
<h3 data-id="heading-24">1.1创建全局组件：</h3>
<pre><code class="copyable">Vue.component("TodoItem", &#123;
    props: ['content'],
    template: "<li>&#123;&#123;content&#125;&#125;</li>"
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">1.2使用全局组件：</h3>
<pre><code class="copyable"><todo-item v-bind:content="item"  v-for="item in list"></todo-item>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>2.6节TodoList-V2.0部分功能组件化-全局组件</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <!-- v-model:数据的双向绑定 -->
        <input v-model="inputValue" type="text">
        <!-- v-on:click:绑定click事件 -->
        <button v-on:click="handleBtnClick">提交</button>
        <!-- v-for:用来循环数据 -->
        <!-- v-bind:把数据绑定到组件 -->
        <ul>
            <!-- <li v-for="item in list">&#123;&#123; item &#125;&#125;</li> -->
            <todo-item v-bind:content="item"  v-for="item in list"></todo-item>
        </ul>
    </div>
    <script>
        // component:创建全局组件
        Vue.component("TodoItem", &#123;
            props: ['content'],
            template: "<li>&#123;&#123;content&#125;&#125;</li>"
        &#125;)
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                list: [],
                inputValue: ''
            &#125;,
            methods: &#123;
                handleBtnClick: function()&#123;
                    this.list.push(this.inputValue)
                    this.inputValue = ''
                &#125;
            &#125;
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">2. 局部组件</h3>
<h3 data-id="heading-27">2.1创建局部组件：</h3>
<pre><code class="copyable">var TodoItem = &#123;
    props: ['content'],
    template: "<li>&#123;&#123;content&#125;&#125;</li>" 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">2.2注册局部组件：</h3>
<pre><code class="copyable">components: &#123; TodoItem &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">2.2使用局部组件：</h3>
<pre><code class="copyable"><todo-item v-bind:content="item"  v-for="item in list"></todo-item>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>2.6节TodoList-V2.0部分功能组件化-局部组件</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <!-- v-model:数据的双向绑定 -->
        <input v-model="inputValue" type="text">
        <!-- v-on:click:绑定click事件 -->
        <button v-on:click="handleBtnClick">提交</button>
        <!-- v-for:用来循环数据 -->
        <!-- v-bind:把数据绑定到组件 -->
        <ul>
            <!-- <li v-for="item in list">&#123;&#123; item &#125;&#125;</li> -->
            <todo-item v-bind:content="item"  v-for="item in list"></todo-item>
        </ul>
    </div>
    <script>
        var TodoItem = &#123;
            props: ['content'],
            template: "<li>&#123;&#123;content&#125;&#125;</li>" 
        &#125;
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                list: [],
                inputValue: ''
            &#125;,
            components: &#123;
                TodoItem
            &#125;,
            methods: &#123;
                handleBtnClick: function()&#123;
                    this.list.push(this.inputValue)
                    this.inputValue = ''
                &#125;
            &#125;
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">2.7 简单的组件间传值</h2>
<h3 data-id="heading-31">1.父组件--->子组件</h3>
<p>父组件:在使用子组件时使用v-bind属性</p>
<pre><code class="copyable">v-bind: content="item"  
v-bind: index="index"  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件:在使用子组件中使用props属性接受父组件传过来值</p>
<pre><code class="copyable">props:['content', 'index'],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">2.子组件--->父组件</h3>
<p>子组件:在子组件的method方法中使用$emit方法向外触发一个事件</p>
<pre><code class="copyable">this.$emit("delete", this.index)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件:在使用子组件的标签上使用v-on监听delete事件然后触发自身的handleItemDelete方法</p>
<pre><code class="copyable">v-on:delete="handleItemDelete"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">3.简写：v-bind：---》： v-on---》@</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>2.7节TodoList-V3.0完整功能</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <!-- v-model:数据的双向绑定 -->
        <input v-model="inputValue" type="text">
        <!-- v-on:click:绑定click事件 -->
        <button v-on:click="handleBtnClick">提交</button>
        <!-- v-for:用来循环数据 -->
        <!-- v-bind:把数据绑定到组件 -->
        <ul>
            <!-- <li v-for="item in list">&#123;&#123; item &#125;&#125;</li> -->
            <todo-item v-bind:content="item" v-bind:index="index"  v-for="(item, index) in list" 
            v-on:delete="handleItemDelete"></todo-item>
        </ul>
    </div>
    <script>
        var TodoItem = &#123;
            props: ['content', 'index'],
            template: "<li v-on:click='handleItemClick'>&#123;&#123;content&#125;&#125;</li>" ,
            methods: &#123;
                handleItemClick: function() &#123;
                    // $.emit:向父组件触发事件
                    this.$emit("delete", this.index)
                &#125;
            &#125;
        &#125;
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                list: [],
                inputValue: ''
            &#125;,
            components: &#123;
                TodoItem
            &#125;,
            methods: &#123;
                handleBtnClick: function()&#123;
                    this.list.push(this.inputValue);
                    this.inputValue = '';
                &#125;,
                handleItemDelete: function (index) &#123;
                    this.list.splice(index, 1);
                &#125;
            &#125;
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">2.8 本章小结</h2>
<h3 data-id="heading-35">Vue官网阅读‘基础’--->‘介绍’</h3>
<hr>
<h1 data-id="heading-36">第3章 Vue基础精讲</h1>
<h2 data-id="heading-37">3.1 Vue实例</h2>
<h3 data-id="heading-38">1.Vue实例的创建</h3>
<pre><code class="copyable">var vm = new Vue(&#123;&#125;)
// 这是一个根实例
Vue.component('item', &#123;
    template: '<div>hello</div>'    
&#125;)
// 组件也是一个实例
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-39">2.Vue实例的属性</h3>
<p>el data method
可以在控制台用<code>vm.$el</code>、<code>vm.$data</code>、<code>vm.$method</code></p>
<h2 data-id="heading-40">3.2 Vue实例的生命周期</h2>
<h3 data-id="heading-41">1.生命周期函数定义：Vue实例在某一时间点会自动执行的函数（共11个）</h3>
<p>8个常用的生命周期函数：beforeCreate ---> created ---> (判断el) ---> (判断template) ---> beforeMount ---> mounted ---> (执行vm.$destory) ---> beforeDestory ---> destoryed ---> (当data改变时) ---> beforeUpdate ---> update
3个（不常用）：activated、 deactivated、 errorCaptured</p>
<h3 data-id="heading-42">2.Vue官网阅读‘Vue实例’</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue的生命周期</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">&#123;&#123; test &#125;&#125;</div>
    <script>
        // 生命周期函数就是Vue实例在某一个时间点自动执行的函数
        var vm = new Vue(&#123;
            el: '#app',
            data: &#123;
                test: 'hell Vue'
            &#125;,
            //页面渲染时执行beforeCreate、created、beforeMount、mounted
            beforeCreate: function () &#123;
                console.log("beforeCreate")
            &#125;,
            created: function () &#123;
                console.log("created")
            &#125;,
            beforeMount: function () &#123;
                console.log("beforeMount")
            &#125;,
            mounted: function () &#123;
                console.log("mounted")
            &#125;,
            //when vm.$destroy() is called
            beforeDestroy: function () &#123;
                console.log("beforeDestroy")
            &#125;,
            destroyed: function () &#123;
                console.log("destroyed")
            &#125;,
            //when data changes
            beforeUpdate: function () &#123;
                console.log("beforeUpdate")
            &#125;,
            updated: function () &#123;
                console.log("updated")
            &#125;,
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-43">3.3 Vue的模板语法</h2>
<h3 data-id="heading-44">1.插值表达式：&#123;&#123;&#125;&#125;（与v-text作用完全相同）</h3>
<h3 data-id="heading-45">2.v-text：不解析html语法</h3>
<h3 data-id="heading-46">3.v-html：解析html语法</h3>
<h3 data-id="heading-47">4.插值表达式与v-text和v-html中的语法都时JavaScript表达式</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>模板语法</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <div>&#123;&#123; content &#125;&#125;</div>
        <!-- 此处content为JS表达式 -->
        <div v-text="content"></div>
        <!-- v-html:不进行转义直接解释输出 -->
        <div v-html="'Hello' + content"></div>
    </div>
    <script>
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                content: '<h1>Vue</h1>'
            &#125;
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">3.4 计算属性、方法、侦听器</h2>
<h3 data-id="heading-49">1.计算属性</h3>
<p>特点：内置缓存,依赖值无变化就不会进行计算</p>
<h3 data-id="heading-50">2.方法</h3>
<p>特点：无内置缓存,只要页面重新渲染就要重新执行</p>
<h3 data-id="heading-51">3.侦听器</h3>
<p>特点：侦听的变量变化时才会执行程序</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>计算属性、方法、监听器</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        &#123;&#123; fullName &#125;&#125;
        <!-- 方法：&#123;&#123; fullName() &#125;&#125; -->
        &#123;&#123; age &#125;&#125;
    </div>
    <script>
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                firstName: 'vience',
                lastName: 'tang',
                fullName: 'vience tang',//watch
                age: 23
            &#125;,
            //计算属性(推荐使用)
            //内置缓存,依赖值无变化就不会进行计算
            // computed: &#123;
            //     fullName: function() &#123;
            //         console.log("计算属性");
            //         return this.firstName + " " + this.lastName;
            //     &#125;
            // &#125;
            //方法
            //无内置缓存只要刷新就要重新执行
            // methods: &#123;
            //     fullName: function () &#123;
            //         console.log("方法");
            //         return this.firstName + " " + this.lastName;
            //     &#125;
            // &#125;
            //侦听的变量变化时才会执行程序
            watch: &#123;
                firstName: function () &#123;
                    console.log("监听firstName");
                    this.fullName = this.firstName + " " + this.lastName;
                &#125;,
                lastName: function () &#123;
                    console.log("监听lastName");
                    this.fullName = this.firstName + " " + this.lastName;
                &#125;
            &#125;
        &#125;)   
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-52">3.5 计算属性的setter和getter</h2>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>计算属性的setter和getter</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        &#123;&#123; fullName &#125;&#125;
    </div>
    <script>
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                firstName: 'vience',
                lastName: 'tang',
            &#125;,
            computed: &#123;
                fullName: &#123;
                    get: function() &#123;
                        return this.firstName + " " + this.lastName;
                    &#125;,
                    set: function(value) &#123;
                        var arr = value.split(" ");
                        this.firstName = arr[0];
                        this.lastName = arr[1];
                    &#125;
                &#125;
            &#125;
        &#125;)   
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-53">3.6 Vue中的样式绑定</h2>
<h3 data-id="heading-54">1.class样式绑定</h3>
<p>对象方式：<code>:class="&#123;activated: isActivated&#125;"</code>
数组方式：<code>:class="[activated]"</code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue中的样式绑定-class</title>
    <script src="../vue.js"></script>
    <style>
        .activated &#123; color: red; &#125;
    </style>
</head>
<body>
    <div id="app">
        <!-- <div :class="&#123;activated: isActivated&#125;" @click="handleDivClick">
            Hello world
        </div> -->
        <div :class="[activated]" @click="handleDivClick">
            Hello world
        </div>
    </div>
    <script>
        var vm = new Vue(&#123;
            el: '#app',
            data: &#123;
                // isActivated: false,
                activated: ''
            &#125;,
            methods: &#123;
                handleDivClick: function () &#123;
                    // this.isActivated = !this.isActivated
                    this.activated = this.activated ===  'activated' ? '' : 'activated'
                &#125;
            &#125;
        &#125;)   
    </script> 
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-55">2.style样式绑定</h3>
<p>对象方式：<code>:style="styleOBj"</code>
数组方式：<code>:style="[styleOBj, &#123;fontSize: '20px'&#125;]"</code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue中的样式绑定-style</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <!-- <div :style="styleOBj" @click="handleDivClick">
            Hello world
        </div> -->
        <div :style="[styleOBj, &#123;fontSize: '20px'&#125;]" @click="handleDivClick">
            Hello world
        </div>
    </div>
    <script>
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                styleOBj: &#123;
                    color: 'black'
                &#125;
            &#125;,
            methods: &#123;
                handleDivClick: function () &#123;
                   this.styleOBj.color = this.styleOBj.color === 'black' ? 'red' : 'black' 
                &#125;
            &#125;
        &#125;)   
    </script> 
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-56">3.7 Vue中的条件渲染</h2>
<h3 data-id="heading-57">1.v-if：值为true时显示，值为false时消失</h3>
<p>特点：通过DOM的生成与删除实现，比较耗费性能</p>
<h3 data-id="heading-58">2.v-show：值为true时显示，值为false时消失</h3>
<p>特点：通过CSS中display的值为none来进行隐藏，节省性能</p>
<h3 data-id="heading-59">3.v-if v-else-if v-else</h3>
<p>注意点1：必须连在一起进行使用
注意点2：若在v-if和v-else（v-else-if）中同事使用input标签时一定要定义不同的key值，若无则会复用已经再在的input标签</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue中的条件渲染</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <!-- 连在一起写 -->
        <!-- <div v-if="show === 'a'">This is A</div>
        <div v-else-if="show === 'b'">This is B</div>
        <div v-else>This is others</div> -->
        <!-- 删除新加DOM -->
        <div v-if="show">&#123;&#123;msg&#125;&#125;</div>
        <div v-else>Bye World</div>
        <!-- 若v-if下与v-else下都有一个input输入框时，需要使用不同的key值进行区别，因为VUE会默认减少不必要的渲染而默认使用之前的input -->
        <!-- 使用display：none 优先使用 减少DOM的删除与渲染-->
        <div v-show="show">&#123;&#123;msg&#125;&#125;</div>
    </div>
    <script>
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                show: false,
                // show: 'a',
                msg: 'Hello world'
            &#125;
        &#125;)   
    </script> 
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-60">3.8 Vue中的列表渲染</h2>
<h3 data-id="heading-61">1.数组的列表渲染</h3>
<p><strong>注意点:使用后端放回的唯一值作为key值</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue中的列表渲染</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <!-- <div v-for='item in list'>&#123;&#123;item&#125;&#125;</div> -->
        <!-- 不推荐使用index做为key值，因为使用index作为key值时会存在相同的情况，而且还比较耗费性能 -->
        <!-- <div v-for='(item, index) of list' :key='index'>&#123;&#123;index&#125;&#125;---&#123;&#123;item&#125;&#125;</div> -->
        <div v-for='item of list' :key='item.id'>&#123;&#123;item.id&#125;&#125;---&#123;&#123;item.text&#125;&#125;</div>
    </div>
    <script>
        var app = new Vue(&#123;
            el: '#app',
            data: &#123;
                // list: ["hello", "vience", "nice", "to", "meet", "you"]
                list: [ &#123; id: '000001', text: 'hello' &#125;, &#123; id: '000002', text: 'vience' &#125;, &#123; id: '000003', text: 'nice' &#125;, &#123; id: '000004', text: 'to' &#125;, &#123; id: '000005', text: 'meet' &#125;, &#123; id: '000006', text: 'you' &#125; ]
            &#125;
        &#125;)   
    </script> 
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-62">2.操作数组</h3>
<p><strong>注意点：通过数组下标来操作数组，页面不会发生重新渲染，若想发生重新渲染则应该使用下面的两种方法</strong></p>
<h4 data-id="heading-63">1.操作数组的方法(变异方法7个)：push pop shift unshift splice sort reserve</h4>
<p>控制台操作：
<code>vm.list.splice(1, 1, &#123;id: '222222', text: 'Tang'&#125;)</code></p>
<h4 data-id="heading-64">2.数组是引用类型，直接改变引用即可</h4>
<p>控制台操作：
<code>vm.list = [ &#123; id: '000001', text: 'hello' &#125;, &#123; id: '222222', text: 'Tang' &#125;, &#123; id: '000003', text: 'nice' &#125;, &#123; id: '000004', text: 'to' &#125;, &#123; id: '000005', text: 'meet' &#125;, &#123; id: '000006', text: 'you' &#125; ]</code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue中的列表渲染---操作数组</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <!-- <div v-for='item in list'>&#123;&#123;item&#125;&#125;</div> -->
        <!-- 不推荐使用index做为key值，因为使用index作为key值时会存在相同的情况，而且还比较耗费性能 -->
        <!-- <div v-for='(item, index) of list' :key='index'>&#123;&#123;index&#125;&#125;---&#123;&#123;item&#125;&#125;</div> -->
        <div v-for='item of list' :key='item.id'>&#123;&#123;item.id&#125;&#125;---&#123;&#123;item.text&#125;&#125;</div>
        <!-- 注意点：通过数组下标来操作数组，页面不会发生重新渲染，若想发生重新渲染则应该使用下面的两种方法 -->
        <!-- 1.操作数组的方法：push pop shift unshift splice sort reserve -->
        <!-- 控制台操作：vm.list.splice(1, 1, &#123;id: '222222', text: 'Tang'&#125;) -->
        <!-- 2.数组是引用类型，直接改变引用即可 -->
        <!-- 控制台操作：vm.list = [ &#123; id: '000001', text: 'hello' &#125;, &#123; id: '222222', text: 'Tang' &#125;, &#123; id: '000003', text: 'nice' &#125;, &#123; id: '000004', text: 'to' &#125;, &#123; id: '000005', text: 'meet' &#125;, &#123; id: '000006', text: 'you' &#125; ] -->
    </div>
    <script>
        var vm = new Vue(&#123;
            el: '#app',
            data: &#123;
                // list: ["hello", "vience", "nice", "to", "meet", "you"]
                list: [ &#123; id: '000001', text: 'hello' &#125;, &#123; id: '000002', text: 'vience' &#125;, &#123; id: '000003', text: 'nice' &#125;, &#123; id: '000004', text: 'to' &#125;, &#123; id: '000005', text: 'meet' &#125;, &#123; id: '000006', text: 'you' &#125; ]
            &#125;
        &#125;)   
    </script> 
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>###3.对象循环渲染
<code><div v-for='(item, key, index) of userInfo'>&#123;&#123;index&#125;&#125;---&#123;&#123;key&#125;&#125;---&#123;&#123;item&#125;&#125;</div></code>
<strong>注意点:若想给对象增加属性，则需要改变对象的引用</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue中的列表渲染---对象</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <div v-for='(item, key, index) of userInfo'>&#123;&#123;index&#125;&#125;---&#123;&#123;key&#125;&#125;---&#123;&#123;item&#125;&#125;</div>
        <!-- 若想给对象增加属性，则需要改变对象的引用 -->
        <!-- 控制台输入:vm.userInfo =  &#123; id: '000001', name: 'vience', age: 23, salary: 'secret', address: '南京' &#125; -->
    </div>
    <script>
        var vm = new Vue(&#123;
            el: '#app',
            data: &#123; userInfo: &#123; id: '000001', name: 'vience', age: 23, salary: 'secret' &#125; &#125;
        &#125;)   
    </script> 
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-65">3.9 Vue中的set方法</h2>
<p><code>Vue.set(vm.userInfo, 'address', '南京')</code>
<code>vm.$set(vm.userInfo, 'address', '南京')</code></p>
<h3 data-id="heading-66">1.对象中的set方法</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue中的set方法---对象</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <div v-for='(item, key, index) of userInfo'>&#123;&#123;index&#125;&#125;---&#123;&#123;key&#125;&#125;---&#123;&#123;item&#125;&#125;</div>
        <!-- 若想给对象增加属性，则需要改变对象的引用 -->
        <!-- 控制台输入:vm.userInfo =  &#123; id: '000001', name: 'vience', age: 23, salary: 'secret', address: '南京' &#125; -->
        <!-- 使用set方法也可以改变对象 -->
        <!-- 控制台输入:Vue.set(vm.userInfo, 'address', '南京') 或者 vm.$set(vm.userInfo, 'address', '南京')  -->
    </div>
    <script>
        var vm = new Vue(&#123;
            el: '#app',
            data: &#123; userInfo: &#123; id: '000001', name: 'vience', age: 23, salary: 'secret' &#125; &#125;
        &#125;)   
    </script> 
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-67">2.数组中的set方法</h3>
<p><code>Vue.set(vm.userInfo, 1, 5)</code>
<code>vm.$set(vm.userInfo, 2, 10)</code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue中的set方法---数组</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <div v-for='(item, index) of userInfo'>&#123;&#123;index&#125;&#125;---&#123;&#123;item&#125;&#125;</div>
        <!-- 使用set方法改变数组 -->
        <!-- 控制台输入:Vue.set(vm.userInfo, 1, 5) 或者 vm.$set(vm.userInfo, 2, 10)  -->
    </div>
    <script>
        var vm = new Vue(&#123;
            el: '#app',
            data: &#123; userInfo: ['1', '2', '3', '4'] &#125;
        &#125;)   
    </script> 
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-68">第4章 深入理解Vue组件</h1>
<h2 data-id="heading-69">4.1 组件使用的细节点</h2>
<h3 data-id="heading-70">1.通过is="row"解决table、ul、ol、select中出现的bug</h3>
<p><code><tr is="row"></tr></code></p>
<h3 data-id="heading-71">2.子组件之中的data必须是一个函数，返回一个对象，而不是一个对象</h3>
<pre><code class="copyable">data: function() &#123;
    return &#123;
        content: 'This is a row'
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.1节组件使用中的细节点</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
        <!-- 通过is="row"解决table、ul、ol、select中出现的bug -->
        <!-- <table>
            <tbody>
                <tr is="row"></tr>
                <tr is="row"></tr>
                <tr is="row"></tr>
            </tbody>
        </table> -->
        <!-- <table>
            <tbody>
                <tr is="row"></tr>
                <tr is="row"></tr>
                <tr is="row"></tr>
            </tbody>
        </table> -->
        <div ref='hello' @click="handleClick" >
            hello world
        </div>
    </div>
    <script>
        // Vue.component('row', &#123;
        // 子组件之中的data必须是一个函数，返回一个对象，而不是一个对象
        // data: function() &#123;
        //     return &#123;
        //         content: 'This is a row'
        //     &#125;
        // &#125;,
        //     template: '<tr><td>&#123;&#123;content&#125;&#125;</td></tr>'
        // &#125;)
        var vm = new Vue(&#123;
            el: '#root',
            methods: &#123;
                handleClick: function() &#123;
                    console.log(this.$refs.hello.innerHTML)
                    // alert('123')
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-72">3.ref的使用</h3>
<h4 data-id="heading-73">3.1 ref使用div标签上时，通过this.$refs.XXX获取的是该标签对应的DOM元素</h4>
<h4 data-id="heading-74">3.1 ref使用子组件上时，通过this.$refs.XXX获取的是子组件的引用</h4>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.1节组件使用中的细节点---ref的用法</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
        <!-- ref使用div标签上时，通过this.$refs.XXX获取的是该标签对应的DOM元素 -->
        <!-- ref使用子组件上时，通过this.$refs.XXX获取的是子组件的引用 -->
        <counter ref='one' @change='handleChange'></counter>
        <counter ref='two' @change='handleChange'></counter>
        <div>&#123;&#123; total &#125;&#125;</div>
    </div>
    <script>
        Vue.component('counter', &#123;
            template: '<div @click="handleClick">&#123;&#123; number &#125;&#125;</div>',
            data: function() &#123;
                return &#123; number: 0 &#125;
            &#125;,
            methods: &#123;
                handleClick: function() &#123;
                    this.number ++
                    this.$emit('change')
                &#125;
            &#125;
        &#125;)
        var vm = new Vue(&#123;
            el: '#root',
            data: &#123; total: 0 &#125;,
            methods: &#123;
                handleChange: function() &#123;
                    this.total = this.$refs.one.number + this.$refs.two.number
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-75">4.2 父子组件之间的数据传递</h2>
<h3 data-id="heading-76">1.父组件 ---> 子组件</h3>
<p>父组件通过属性的形式向子组件传递数据
<code><counter :count='2'></counter></code>
子组件使用props接收父组件传来的数组
<code>props: ['count'],</code></p>
<h3 data-id="heading-77">2.子组件 ---> 父组件</h3>
<p>子组件使用this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi>m</mi><mi>i</mi><mi>t</mi><msup><mo stretchy="false">(</mo><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mi>i</mi><mi>n</mi><msup><mi>c</mi><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mo separator="true">,</mo><mn>2</mn><mo separator="true">,</mo><mn>2</mn><mo stretchy="false">)</mo><mtext>方法向父组件传递一个触发事件</mtext><mo stretchy="false">(</mo><mtext>可以携带一个或多个参数</mtext><mo stretchy="false">)</mo><mi mathvariant="normal">‘</mi><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">emit('inc', 2, 2)方法向父组件传递一个触发事件(可以携带一个或多个参数) `this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal">m</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mopen"><span class="mopen">(</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mord mathnormal">i</span><span class="mord mathnormal">n</span><span class="mord"><span class="mord mathnormal">c</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord">2</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord">2</span><span class="mclose">)</span><span class="mord cjk_fallback">方</span><span class="mord cjk_fallback">法</span><span class="mord cjk_fallback">向</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">传</span><span class="mord cjk_fallback">递</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">触</span><span class="mord cjk_fallback">发</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mopen">(</span><span class="mord cjk_fallback">可</span><span class="mord cjk_fallback">以</span><span class="mord cjk_fallback">携</span><span class="mord cjk_fallback">带</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">或</span><span class="mord cjk_fallback">多</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">参</span><span class="mord cjk_fallback">数</span><span class="mclose">)</span><span class="mord">‘</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>emit('inc', 2)<code>父组件通过对事件进行监听来接收子组件传过来的值</code><counter :count='2' @inc='hanleIncrease'>`</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.2节父子组件间的数据传递</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
        <counter :count='2' @inc='hanleIncrease'></counter>
        <counter :count='3' @inc='hanleIncrease'></counter>
        <div>&#123;&#123; total &#125;&#125;</div>
    </div>
    <script>
        var counter = &#123;
            props: ['count'],
            data: function() &#123;
                return &#123; number: this.count &#125;
            &#125;,
            template: '<div @click="handleClick">&#123;&#123; number &#125;&#125;</div>',
            methods: &#123;
                handleClick: function() &#123;
                    // 单向数据流:子组件不能修改父组件传递过来的值,可以通过clone一个副本进行修改
                    this.number = this.number + 2
                    // 子组件通过this.$emit('inc', 2,2)方法向父组件传递一个触发事件(可以携带一个或多个参数)
                    this.$emit('inc', 2)
                &#125;
            &#125;
        &#125;
        var vm = new Vue(&#123;
            el: '#root',
            data: &#123; total: 5 &#125;,
            components: &#123; counter &#125;,
            methods: &#123;
                hanleIncrease: function(val) &#123;
                    this.total += val
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-78">4.3 组件参数校验与非props特性</h2>
<h3 data-id="heading-79">1.组件参数校验</h3>
<p><code>props: ['content']</code>
<code>props: &#123; content: String &#125;</code>
<code>props: &#123; content: [String, Number] &#125;</code></p>
<pre><code class="copyable">props: &#123;
    content: &#123;
        type: String,
        // required: true,
        // default: 'default value'
        validator: function(value) &#123;
            return (value.length > 5)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-80">2.非props特性</h3>
<p>非props特性: 子组件没有接受对应的值,而组件使用了,就会报错;父组件调用子组件时,传值的属性会显示在DOM中</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.3节组件参数校验与非props特性</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
        <child content='hello world'></child>
    </div>
    <script>
        Vue.component('child',&#123;
            // props特性:父组件传值,子组件要接收对应的值,父组件调用子组件时,传值的属性不会显示在DOM中
            // 非props特性: 子组件没有接受对应的值,而组件使用了,就会报错;父组件调用子组件时,传值的属性会显示在DOM中
            // props: ['content']
            // props: &#123; content: String &#125;
            // props: &#123; content: [String, Number] &#125;
            props: &#123;
                content: &#123;
                    type: String,
                    // required: true,
                    // default: 'default value'
                    validator: function(value) &#123;
                        return (value.length > 5)
                    &#125;
                &#125;
            &#125;,
            template: '<div>&#123;&#123; content &#125;&#125;</div>'
        &#125;)
        var vm = new Vue(&#123; el: '#root', &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-81">4.4 给组件绑定原生事件</h2>
<p><code><child @click.native='handleClick'></child></code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.4节给组件绑定原生事件</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
        <!-- 在子组件上绑定的事件属于自定义事件 -->
        <!-- <child @click='handleClick'></child> -->
        <child @click.native='handleClick'></child>
    </div>
    <script>
        Vue.component('child',&#123;
            // 在div元素上绑定的时间属于原生事件
            // template: '<div @click="handleClick">Child</div>',
            // methods: &#123;
            //     handleClick: function() &#123;
            //         this.$emit('click')
            //     &#125;
            // &#125;
            template: '<div>Child</div>',
        &#125;)
        var vm = new Vue(&#123;
            el: '#root',
            methods: &#123;
                handleClick: function() &#123;
                    alert('click')
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-82">4.5 非父子组件间的传值</h2>
<h3 data-id="heading-83">1. Vuex</h3>
<h3 data-id="heading-84">2. Bus/总线/发布订阅模式/观察者模式</h3>
<h4 data-id="heading-85">Bus创建：</h4>
<p><code>Vue.prototype.bus = new Vue()</code></p>
<h4 data-id="heading-86">事件触发：</h4>
<p><code>this.bus.$emit('change', this.selfContent)</code></p>
<h4 data-id="heading-87">事件监听（单向数据流，不能直接改变父组件传来的值，通过clone改变副本）：</h4>
<pre><code class="copyable">this.bus.$on('change', function(msg)&#123;
    this_ .selfContent = msg
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.5节非父子组件间的传值</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
        <!-- Bus/总线/发布订阅模式/观察者模式 -->
        <child content='vience'></child>
        <child content='tang'></child>
    </div>
    <script>
        Vue.prototype.bus = new Vue()
        Vue.component('child',&#123;
            data: function() &#123;
                return &#123;
                    selfContent: this.content
                &#125;
            &#125;,
            props: &#123; content: String &#125;,
            template: '<div @click="handleClick">&#123;&#123;selfContent&#125;&#125;</div>',
            methods: &#123;
                handleClick: function() &#123;
                    this.bus.$emit('change', this.selfContent)
                &#125;
            &#125;,
            mounted: function() &#123;
                var this_ = this
                this.bus.$on('change', function(msg)&#123;
                    this_ .selfContent = msg
                &#125;)
            &#125;
        &#125;)
        var vm = new Vue(&#123;
            el: '#root',
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-88">4.6 在vue中使用插槽（slot）</h2>
<h3 data-id="heading-89">1. 插槽一般用于父组件向子组件传递一段DOM结构（）</h3>
<h3 data-id="heading-90">2. 默认内容</h3>
<h3 data-id="heading-91">3. 具名插槽(支持默认内容)</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.6节在vue中使用插槽</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
        <!-- slot:用于父组件向子组件传递DOM结构 -->
        <!-- <child content='<p>vience</p>'></child> -->
        <child>
            <!-- 当传入的DOM结构为空时slot显示默认内容 -->
            <!-- <p>vience</p> -->
            <!-- 具名插槽(支持默认内容) -->
            <div class="header" slot="header">header</div>
            <div class="footer" slot="footer">footer</div>
        </child>
    </div>
    <script>
        Vue.component('child',&#123;
            props: &#123; content: String &#125;,
            // template: `<div>
            //                 <p>hello</p>
            //                 <div v-html='this.content'></div>
            //             </div>`,
            // template: `<div>
            //                 <p>hello</p>
            //                 <slot>默认内容</slot>
            //             </div>`,
            template: `<div>
                            <slot name='header'></slot>
                            <div>content</div>
                            <slot name='footer'></slot>
                        </div>`,
        &#125;)
        var vm = new Vue(&#123; el: '#root', &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-92">4.7 作用域插槽</h2>
<h3 data-id="heading-93">使用场景：当子组件做循环或者某一部分显示的DOM由外部传入时使用作用域插槽</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.7节作用域插槽</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
        <child>
            <template slot-scope="props">
                <!-- <li> &#123;&#123;props.item&#125;&#125; - hello </li> -->
                <h1> &#123;&#123;props.item&#125;&#125; </h1>
            </template>
        </child>
    </div>
    <script>
        Vue.component('child',&#123;
            data: function() &#123;
                return &#123; list: [1, 2, 3, 4] &#125;
            &#125;,
            template: `<div><ul> <slot v-for='item of list' :item=item></slot> </ul></div>`,
        &#125;)
        var vm = new Vue(&#123; el: '#root' &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-94">4.8 动态组件与v-once指令</h2>
<h3 data-id="heading-95">1. 动态组件：<code><component :is='type'></component></code></h3>
<h3 data-id="heading-96">2. v-once：放在缓存中重复使用</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4.8节动态组件与v-once指令</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="root">
            <child-one v-if="type=== 'child-one'"></child-one>
            <child-two v-if="type=== 'child-two'"></child-two>
            <!-- <component :is='type'></component> -->
            <button @click="handleBtnClick">change</button>
    </div>
    <script>
        Vue.component('child-one',&#123;
            template: `<div v-once>child-one</div>`,
        &#125;)
        Vue.component('child-two',&#123;
            template: `<div v-once>child-two</div>`,
        &#125;)
        var vm = new Vue(&#123; 
            el: '#root',
            data: &#123;
                type: 'child-one'
            &#125;,
            methods: &#123;
                handleBtnClick: function() &#123;
                    this.type = (this.type === 'child-one' ? 'child-two' : 'child-one')
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-97">第5章 Vue中的动画特效</h1>
<h2 data-id="heading-98">5.1 Vue中的CSS动画原理</h2>
<h3 data-id="heading-99">1. 过渡动画效果</h3>
<p>通过某一时刻往标签上增加或者移除clss来实现动画效果</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>5.1节Vue中的CSS动画原理</title>
    <script src="../vue.js"></script>
    <style>
        .v-enter, .v-leave-to  &#123; opacity: 0; &#125;
        .v-enter-active, .v-leave-active &#123; transition: opacity 3s; &#125;
    </style>
</head>
<body>
    <div id="root">
        <!-- 通过某一时刻往标签上增加或者移除clss来实现动画效果 -->
        <!-- 过渡动画效果 -->
        <transition>
            <!-- <div v-if='show'>hello world</div> -->
            <div v-show='show'>hello world</div>
        </transition>
        <button @click="handleBtnClick">切换</button>
    </div>
    <script>
        var vm = new Vue(&#123; 
            el: '#root',
            data: &#123; show: true &#125;,
            methods: &#123;
                handleBtnClick: function() &#123;
                    this.show = !this.show
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-100">5.2 Vue中使用animate.css库</h2>
<h3 data-id="heading-101">1. 使用link引入animate.css文件</h3>
<p><code><link rel="stylesheet" href="../animate.css"></code></p>
<h3 data-id="heading-102">2. 给transition1标签增加enter-active-class和leave-active-class属性并对这两个属性赋值为animated和所需动画效果即可</h3>
<pre><code class="copyable"><transition name='fade' enter-active-class='animated swing' leave-active-class='animated shake'>
    <div v-show='show'>hello world</div>
</transition>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>5.1节Vue中使用animate.css库</title>
    <script src="../vue.js"></script>
    <link rel="stylesheet" href="../animate.css">
    <!-- <style>
        @keyframes bounce-in &#123;
            0% &#123; transform: scale(0); &#125;
            50% &#123; transform: scale(1.5); &#125;
            100% &#123; transform: scale(1); &#125;
        &#125;
        .active &#123;  transform-origin: left center; animation: bounce-in 1s; &#125;
        .leave &#123; transform-origin: left center; animation: bounce-in 1s reverse; &#125;
    </style> -->
</head>
<body>
    <div id="root">
        <!-- <transition name='fade' enter-active-class='active' leave-active-class='leave'>
            <div v-show='show'>hello world</div>
        </transition> -->
        <transition name='fade' enter-active-class='animated swing' leave-active-class='animated shake'>
                <div v-show='show'>hello world</div>
            </transition>
        <button @click="handleBtnClick">切换</button>
    </div>
    <script>
        var vm = new Vue(&#123; 
            el: '#root',
            data: &#123; show: true &#125;,
            methods: &#123;
                handleBtnClick: function() &#123;
                    this.show = !this.show
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-103">5.3 在Vue中同时使用过渡和动画</h2>
<h3 data-id="heading-104">1. 第一次显示时出现时显示动画</h3>
<p><code>appear appear-active-class='animated swing' </code></p>
<h3 data-id="heading-105">2. 在Vue中同时使用过渡和动画</h3>
<pre><code class="copyable"><style>
    .fade-enter, .fade-leave-to  &#123; opacity: 0; &#125;
    .fade-enter-active, .fade-leave-active &#123; transition: opacity 3s; &#125;
</style>
 <transition type='transition' name='fade' appear appear-active-class='animated swing' enter-active-class='animated swing fade-enter-active' leave-active-class='animated shake fade-leave-active'>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-106">3. 在Vue中同时使用过渡和动画时动画时长设置</h3>
<p>动画时长以transition为准(3s)
<code>type='transition' </code>
自定义动画时长
<code>:duration='1000'</code>
<code>:duration='&#123;enter:5000, leave:10000&#125;'</code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>5.1节在Vue中同时使用过渡和动画</title>
    <script src="../vue.js"></script>
    <link rel="stylesheet" href="../animate.css">
    <style>
        .fade-enter, .fade-leave-to  &#123; opacity: 0; &#125;
        .fade-enter-active, .fade-leave-active &#123; transition: opacity 3s; &#125;
    </style>
</head>
<body>
    <div id="root">
        <!-- appear appear-active-class='animated swing' 第一次显示时出现动画 -->
        <!-- type='transition' 动画时长以transition为准(3s) -->
        <!-- :duration='1000' 自定义动画时长 :duration='&#123;enter:5000, leave:10000&#125;' -->
        <transition type='transition' name='fade' appear appear-active-class='animated swing' enter-active-class='animated swing fade-enter-active' leave-active-class='animated shake fade-leave-active'>
                <div v-show='show'>hello world</div>
            </transition>
        <button @click="handleBtnClick">切换</button>
    </div>
    <script>
        var vm = new Vue(&#123; 
            el: '#root',
            data: &#123; show: true &#125;,
            methods: &#123;
                handleBtnClick: function() &#123;
                    this.show = !this.show
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-107">5.4 Vue中JS动画与Velocity.jsde结合</h2>
<h3 data-id="heading-108">1. JS动画钩子</h3>
<p>入场：before-enter，enter，after-enter
离场：before-leave，leave，after-leave</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>5.4节Vue中JS动画与Velocity.jsde结合</title>
    <script src="../vue.js"></script>
    <script src="../velocity.js"></script>
</head>
<body>
    <div id="root">
        <!-- 离场动画同理 -->
        <transition name='fade' @before-enter='handleBeforeEnter' @enter='handleEnter' @after-enter='handleAfterEnter'>
                <div v-show='show'>hello world</div>
            </transition>
        <button @click="handleBtnClick">切换</button>
    </div>
    <script>
        var vm = new Vue(&#123; 
            el: '#root',
            data: &#123; show: true &#125;,
            methods: &#123;
                handleBtnClick: function() &#123;
                    this.show = !this.show
                &#125;,
                // handleBeforeEnter: function(el) &#123; el.style.color = 'red' &#125;,
                // handleEnter: function(el, done) &#123;
                //     setTimeout(() => &#123; el.style.color = 'green' &#125;, 2000)
                //     setTimeout(() => &#123; done() &#125;, 4000)
                // &#125;,
                // handleAfterEnter: function(el) &#123; el.style.color = '#000000' &#125;
                handleBeforeEnter: function(el) &#123;
                    el.style.opacity = 0
                &#125;,
                handleEnter: function(el, done) &#123;
                    Velocity(el, &#123;opacity: 1&#125;, &#123;duration: 1000, complete: done&#125;)
                &#125;,
                handleAfterEnter: function(el) &#123;
                    console.log('动画结束')
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-109">5.5 Vue中多个元素或组件间的过渡</h2>
<h3 data-id="heading-110">1. 多个元素之间</h3>
<p>mode='in-out':先进入后隐藏 mode='out-in':先隐藏后进入</p>
<h3 data-id="heading-111">2. 多个组件之间</h3>
<p><code><component :is='type'></component></code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>5.5节Vue中多个元素或组件间的过渡</title>
    <script src="../vue.js"></script>
    <style>
        .v-enter, .v-leave-to  &#123; opacity: 0; &#125;
        .v-enter-active, .v-leave-active &#123; transition: opacity 1s; &#125;
    </style>
</head>
<body>
    <div id="root">
        <!-- mode='in-out':先进入后隐藏 mode='out-in':先隐藏后进入 -->
        <!-- <transition mode='out-in'>
            <div v-if='show' key='hello'>hello world</div>
            <div v-else key='bye'>bye world</div>
        </transition> -->
        <!-- <transition mode='out-in'>
            <child v-if='show'></child>
            <child-one v-else></child-one>
        </transition> -->
        <transition mode='out-in'>
            <component :is='type'></component>
        </transition>
        <button @click="handleBtnClick">切换</button>
    </div>
    <script>
        Vue.component('child', &#123;
            template: '<div>child</div>'
        &#125;)
        Vue.component('child-one', &#123;
            template: '<div>child-one</div>'
        &#125;)
        var vm = new Vue(&#123; 
            el: '#root',
            data: &#123; 
                // show: true,
                type: 'child'
            &#125;,
            methods: &#123;
                handleBtnClick: function() &#123;
                    // this.show = !this.show
                    this.type = this.type === 'child' ? 'child-one' : 'child'
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-112">5.6 Vue中的列表过渡</h2>
<p>对循环的div外部添加transition-group标签
<code><transition-group></transition-group></code></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>5.6节Vue中的列表过渡</title>
    <script src="../vue.js"></script>
    <style>
        .v-enter, .v-leave-to  &#123; opacity: 0; &#125;
        .v-enter-active, .v-leave-active &#123; transition: opacity 1s; &#125;
    </style>
</head>
<body>
    <div id="root">
        <transition-group>
            <div v-for='item of list' :key='item.id'>&#123;&#123; item.title &#125;&#125;</div>
        </transition-group>
        <button @click="handleBtnClick">Add</button>
    </div>
    <script>
        var count = 0;
        var vm = new Vue(&#123; 
            el: '#root',
            data: &#123; list: [] &#125;,
            methods: &#123;
                handleBtnClick: function() &#123;
                    this.list.push(&#123; id: count++, title: 'hello world' &#125;)
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-113">5.7 Vue中的动画封装</h2>
<h3 data-id="heading-114">1. 封装模板，写CSS样式</h3>
<pre><code class="copyable"><style>
    .v-enter, .v-leave-to  &#123; opacity: 0; &#125;
    .v-enter-active, .v-leave-active &#123; transition: opacity 1s; &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-115">2. 用JS动画封装在组件中（推荐使用方式）</h3>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>5.7节Vue中的动画封装</title>
    <script src="../vue.js"></script>
    <!-- <style>
        .v-enter, .v-leave-to  &#123; opacity: 0; &#125;
        .v-enter-active, .v-leave-active &#123; transition: opacity 1s; &#125;
    </style> -->
</head>
<body>
    <div id="root">
        <fade :show='show'>
            <div>hello world</div>
        </fade>
        <fade :show='show'>
            <h1>hello world</h1>
        </fade>
        <button @click="handleBtnClick">toggle</button>
    </div>
    <script>
        Vue.component('fade', &#123;
            props: ['show'],
            template: `<transition @before-enter='handleBeforeEnter' @enter='handleEnter' @after-enter='handleAfterEnter'><slot v-if='show'></slot></transition>`,
            methods: &#123;
                handleBeforeEnter: function(el) &#123; el.style.color = 'red' &#125;,
                handleEnter: function(el, done) &#123;
                    setTimeout(() => &#123; el.style.color = 'green' &#125;, 2000)
                    setTimeout(() => &#123; done() &#125;, 4000)
                &#125;,
                handleAfterEnter: function(el) &#123; el.style.color = '#000000' &#125;
            &#125;
        &#125;)
        var vm = new Vue(&#123; 
            el: '#root',
            data: &#123; show: false &#125;,
            methods: &#123;
                handleBtnClick: function() &#123;
                    this.show = !this.show
                &#125;
            &#125;
        &#125;)  
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-116">第6章 Vue 项目预热</h1>
<h2 data-id="heading-117">6.1 环境配置</h2>
<h3 data-id="heading-118">1.配置vue开发环境</h3>
<p>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F134149147ca6" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/134149147ca6" ref="nofollow noopener noreferrer">www.jianshu.com/p/134149147…</a></p>
<h3 data-id="heading-119">2.在gitee上创建项目方便管理</h3>
<h4 data-id="heading-120">2.1 在gitee上创建项目</h4>
<h4 data-id="heading-121">2.2 安装git</h4>
<h4 data-id="heading-122">2.3 git clone 线上代码并在线下创建vue项目，并上传至线上</h4>
<h2 data-id="heading-123">6.2 项目代码介绍</h2>
<h2 data-id="heading-124">6.3 单文件组件与Vue中的路由</h2>
<p><code><router-view/></code>：显示的是当前路由地址所对应的内容</p>
<h2 data-id="heading-125">6.4 单页应用VS多页应用</h2>
<h3 data-id="heading-126">1.多页应用（页面跳转--->返回HTML）</h3>
<p>特点：首屏时间快，SEO效果好，页面切换慢</p>
<h3 data-id="heading-127">2.单页应用（页面跳转--->JS渲染）</h3>
<p>特点：页面切换快，首屏时间稍慢，SEO效果差</p>
<h2 data-id="heading-128">6.4 项目代码初始化</h2>
<h3 data-id="heading-129">1.修改index.html的mate标签</h3>
<pre><code class="copyable"><meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no">
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-130">2.重置CSS样式</h3>
<p><code>import '@/assets/styles/reset.css'</code></p>
<h3 data-id="heading-131">3.解决1像素边框问题</h3>
<p><code>import '@/assets/styles/border.css'</code></p>
<h3 data-id="heading-132">4.解决300毫秒点击延迟问题</h3>
<pre><code class="copyable">npm install fastclick --save
import FastClick from 'fastclick'
FastClick.attach(document.body)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-133">开发实战</h1>
<h2 data-id="heading-134">知识点1</h2>
<h3 data-id="heading-135">1.git 切换新的分支开发并最后合并到主分支</h3>
<h4 data-id="heading-136">①：在gitee上创建新的分支（index-nnn）</h4>
<h4 data-id="heading-137">②：在项目下面的git Bash中执行git pull</h4>
<h4 data-id="heading-138">③：继续执行git checkout 'index-nnn'</h4>
<h4 data-id="heading-139">④：继续执行git status 查看所在分支</h4>
<h4 data-id="heading-140">⑤：开发完成后执行git status 查看代码变更内容</h4>
<h4 data-id="heading-141">⑥：执行git add . 把修改的代码提交到本地缓存中</h4>
<h4 data-id="heading-142">⑦：执行git commit -m 'XXX' 填写备注XXX</h4>
<h4 data-id="heading-143">⑧：执行git push 把修改的代码提交到线上的新建分支上</h4>
<h4 data-id="heading-144">⑨：执行git checkout master 切换所在分支为主分支</h4>
<h4 data-id="heading-145">⑩：执行git merge origin/index-nnn 查看新建分支与主分支内容差别</h4>
<p>####十一：执行git push 把新建分支的内容提交到主分支上</p></div>  
</div>
            