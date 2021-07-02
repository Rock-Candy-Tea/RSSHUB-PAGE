
---
title: '01.Vue的生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47b8f22270534eef88642827b1984f82~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 03:13:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47b8f22270534eef88642827b1984f82~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一.Vue的生命周期原图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47b8f22270534eef88642827b1984f82~tplv-k3u1fbpfcp-zoom-1.image" alt="lifecycle" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">二.Vue生命周期理解图</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4210e00607534980a741c95f916618c9~tplv-k3u1fbpfcp-watermark.image" alt="VueLifeCycle.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">三.Vue的生命周期总结</h2>
<ul>
<li>什么是生命周期：从Vue实例创建、运行、到销毁期间，总是伴随着各种各样的事件，这些事件，统称为生命周期！</li>
<li>生命周期钩子：就是生命周期事件的别名而已；</li>
<li>生命周期钩子 = 生命周期函数 = 生命周期事件</li>
</ul>
<h3 data-id="heading-3">3.1 主要的生命周期函数分类：</h3>
<h4 data-id="heading-4">3.1.1 创建期间的生命周期函数：</h4>
<ul>
<li><strong>beforeCreate：实例刚在内存中被创建出来，此时，还没有初始化好 data 和 methods 属性</strong></li>
<li><strong>created：实例已经在内存中创建OK，此时 data 和 methods 已经创建OK，此时还没有开始 编译模板</strong></li>
<li><strong>beforeMount：</strong>
<ul>
<li><strong>所有对DOM节点操作，最终都不奏效</strong></li>
<li><strong>此时已经完成了模板的编译，但是还没有挂载到页面中</strong></li>
</ul>
</li>
<li><strong>mounted：</strong>
<ul>
<li><strong>此时，已经将编译好的模板，挂载到了页面指定的容器中显示</strong></li>
<li><strong>可以操作DOM节点；</strong></li>
<li><strong>此时组件已经脱离初始化阶段，进入运行阶段，一般在此阶段：开启定时器、发送网络请求等准备工作</strong></li>
</ul>
</li>
</ul>
<h4 data-id="heading-5"><strong>3.1.2 运行期间的生命周期函数：</strong></h4>
<ul>
<li><strong>beforeUpdate：状态更新之前执行此函数， ==此时 data 中的状态值是最新的，但是界面上显示的 数据还是旧的，==因为此时还没有开始重新渲染DOM节点</strong></li>
<li><strong>updated：实例更新完毕之后调用此函数，此时 data 中的状态值 和 界面上显示的数据，都已经完成了更新，界面已经被重新渲染好了！</strong></li>
</ul>
<h4 data-id="heading-6"><strong>3.1.3 销毁期间的生命周期函数：</strong></h4>
<ul>
<li><strong>beforeDestroy：</strong>
<ul>
<li><strong>实例销毁之前调用。</strong></li>
<li>==<strong>vm所有的data，methods，指令等等，都处于可用状态，马上要执行销毁过程，</strong>==</li>
<li><strong>一般在此钩子中：关闭定时器，取消订阅消息等收尾工作。</strong></li>
</ul>
</li>
<li><strong>destroyed：</strong>
<ul>
<li><strong>Vue 实例销毁后调用。</strong></li>
<li>==<strong>调用后，Vue 实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁.</strong>==</li>
</ul>
</li>
</ul>
<h2 data-id="heading-7">四.Vue生命周期实例分析</h2>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>02.分析Vue生命周期</title>
  </head>

  <body>
    <div id="app">
      <button @click="add" id="btn">+</button>
      <h1 id="h1">当前页面求和为:&#123;&#123;sum&#125;&#125;</h1>
      <button @click="decrease">-</button>
      <button @click="death">销毁</button>
    </div>

  </body>
  <script src="../js/vue.js"></script>
  <script>
    //配置Vue关闭生产环境配置
    Vue.config.productionTip = false;

    const vm = new Vue(&#123;
      el: "#app",
      data() &#123;
        return &#123;
          sum: 0
        &#125;
      &#125;,
      methods: &#123;
        add() &#123;
          console.log("你点了add按钮");
          this.sum += 1
        &#125;,
        decrease() &#123;
          this.sum -= 1
        &#125;,
        death() &#123;
          this.$destroy()
        &#125;
      &#125;,
      //vue实例初始化前
      beforeCreate() &#123;
        console.log("------beforeCreate------");
        console.log(this);
        console.log(this.sum) //undefined
        console.log(this.add) //undefined
      &#125;,
      //vue实例初始化完毕
      created() &#123;
        console.log("---------created---------");
        console.log(this);
        console.log(this.sum) //0
        console.log(this.add) //function add()&#123;&#125;
      &#125;,
      //Vue实例挂载之前:更新真实DOM之前（挂载前）
      // 此钩子中：1.所有对DOM节点操作，最终都不奏效
      // 2.无法获得解析后的DOM,因为还没有Mount
      beforeMount() &#123;
        console.log("-----------beforeMount---------------");
        //1.所有对DOM节点操作，最终都不奏效
        // let h1 = document.querySelector("#h1");
        // h1.innerHTML = "Vue";
        //2.无法获得解析后的DOM,因为还没有Mount
      &#125;,
      //Vue更新完真实DOM（挂载完毕）
      /* 
      此钩子中：
      1.可以操作DOM节点；
      2.此时组件已经脱离初始化阶段，进入运行阶段，
        一般在此阶段：开启定时器、发送网络请求等准备工作
      */
      mounted() &#123;
        console.log("--------------mounted------------");
        //1.可以操作DOM节点；
        let h1 = document.querySelector("#h1");
        let btn = document.querySelector("#btn");
        h1.innerHTML = "哈哈";
        btn.innerHTML = "哈哈"
        console.log(h1);
        console.log(btn);
      &#125;,
      //Vue实例将要更新页面
      // 此钩子中：数据是新的,但是页面是旧的， 即:页面尚未和数据保持同步
      beforeUpdate() &#123;
        console.log("---------beforeUpdate-----------");
        // console.log(this.sum); //1,显示出来的是1，但是页面呈现出来的是0
        // debugger;
      &#125;,
      // vue实例完成数据更新
      // 此钩子中：数据是新的，页面也是新的。即：页面和数据保持同步了
      updated() &#123;
        console.log("--------updated------");
        // console.log(this.sum);
      &#125;,
      //Vue实例在销毁前
      // 此钩子中： 
      // 1. vm所有的data,methods,指令等等，都处于可用状态，马上要执行销毁过程， 
      // 2. 一般在此钩子中：关闭定时器，取消订阅消息等收尾工作。
      // 移除所有的数据监视，移除所有子组件和事件监听
      beforeDestroy() &#123;
        console.log("--------beforeDestroy------------");
        console.log(this.sum); //可以获取
        console.log(this.add); //可以获取
      &#125;,
      // Vue实例销毁完毕
      destroyed() &#123;
        console.log("----------destroyed-----------");
        console.log("我已经移除了所有数据的监视，不会再更新页面了");
      &#125;
    &#125;)
  </script>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">4.1.beforeCreate()</h3>
<p><em>vue实例初始化前</em>:</p>
<p>1.此钩子中:<strong>无法</strong>通过vm访问到data里面的数据，和methods里面的方法</p>
<pre><code class="copyable"> //vue实例初始化前
      beforeCreate() &#123;
        console.log("------beforeCreate------");
        console.log(this);
        console.log(this.sum) //undefined
        console.log(this.add) //undefined
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9335ce0be46549419207e65ac836bbdd~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701151317377" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8529c053f60e441c8544caea82b35689~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701152158201" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">4.2.created()</h3>
<p><em>vue实例初始化完毕</em>:</p>
<p>1.此钩子中:<strong>可以</strong>通过vm访问到data里面的数据，和methods里面的方法</p>
<p>2.没有解析模板，数据<strong>没有</strong>展示在页面上</p>
<pre><code class="copyable">  //vue实例初始化完毕
      created() &#123;
        console.log("---------created---------");
        console.log(this);
        console.log(this.sum) //0
        console.log(this.add) //function add()&#123;&#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1a8cb2c2b524bb38c9e882adb1229ec~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701151911452" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbe1d8ed47bb4780aed05dee58bf7241~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701152018539" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">4.3. beforeMount()</h3>
<p><em>Vue实例挂载之前</em>:</p>
<p>此钩子中：</p>
<p>1.所有对DOM节点操作，最终都不奏效</p>
<p>2.无法获得解析后的DOM,因为还没有Mount</p>
<pre><code class="copyable"> beforeMount() &#123;
 console.log("-----------beforeMount---------------");
     //1.所有对DOM节点操作，最终都不奏效
     let h1 = document.querySelector("#h1");
     h1.innerHTML = "Vue";
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbd1e310317a464298b466284d66fb6a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701154732456" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">4.4.mounted()</h3>
<p><em>Vue更新完真实DOM（挂载完毕）</em></p>
<p>此钩子中：
1.可以操作DOM节点；
2.此时组件已经脱离初始化阶段，进入运行阶段，
一般在此阶段：开启定时器、发送网络请求等准备工作</p>
<pre><code class="copyable"> /* 
      此钩子中：
      1.可以操作DOM节点；
      2.此时组件已经脱离初始化阶段，进入运行阶段，
        一般在此阶段：开启定时器、发送网络请求等准备工作
      */
      mounted() &#123;
        console.log("--------------mounted------------");
        //1.可以操作DOM节点；
        /* let h1 = document.querySelector("#h1");
        let btn = document.querySelector("#btn");
        h1.innerHTML = "哈哈";
        btn.innerHTML = "哈哈"
        console.log(h1);
        console.log(btn); */
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3d59d46a8824d4dbe4a45607d91f8c9~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701175441926" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">4.5.beforeUpdate()</h3>
<p><em>Vue实例将要更新页面</em>:</p>
<p>此钩子中：<strong>数据是新的,但是页面是旧的， 即:页面尚未和数据保持同步</strong></p>
<pre><code class="copyable"> //Vue实例将要更新页面
      // 此钩子中：数据是新的,但是页面是旧的， 即:页面尚未和数据保持同步
      beforeUpdate() &#123;
        console.log("---------beforeUpdate-----------");
        console.log(this.sum);//1,显示出来的是1，但是页面呈现出来的是0
        debugger;
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>点击add()事件后，呈现的页面</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/354647a948a64762a4ba178ce1a525ff~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701171240517" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">4.6.updated()</h3>
<p>vue实例完成数据更新:</p>
<p>此钩子中：<strong>数据是新的，页面也是新的。即：页面和数据保持同步了</strong></p>
<pre><code class="copyable"> // vue实例完成数据更新
      // 此钩子中：数据是新的，页面也是新的。即：页面和数据保持同步了
      updated() &#123;
        console.log("--------updated------");
        console.log(this.sum);
        debugger
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>点击add()事件后，呈现的页面</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/752d0facbb6144a3a96e4aff9ee27a42~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701171852822" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">4.7.beforeDestroy()</h3>
<p>Vue实例在销毁前:</p>
<p>此钩子中：</p>
<ol>
<li>vm所有的data,methods,指令等等，都处于可用状态，马上要执行销毁过程，</li>
<li>一般在此钩子中：关闭定时器，取消订阅消息等收尾工作。</li>
</ol>
<p><em>移除所有的数据监视，移除所有子组件和事件监听</em></p>
<pre><code class="copyable">//Vue实例在销毁前
      // 此钩子中： 
      // 1. vm所有的data,methods,指令等等，都处于可用状态，马上要执行销毁过程， 
      // 2. 一般在此钩子中：关闭定时器，取消订阅消息等收尾工作。
      beforeDestroy() &#123;
        console.log("--------beforeDestroy------------");
        console.log(this.sum);
        console.log(this.add);
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ac09d81e1ed4fd39ecbbc628200c782~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701173208473" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c91bfa0f4ce4ba7813f10f3817b7885~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701174200155" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">4.8.destroyed()</h3>
<p><em>Vue实例销毁完毕</em></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e165e5b176143f4838a99cff8a3a067~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701174729510" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            