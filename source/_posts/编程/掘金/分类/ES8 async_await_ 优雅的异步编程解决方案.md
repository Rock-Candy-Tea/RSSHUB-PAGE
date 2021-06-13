
---
title: 'ES8 async_await_ 优雅的异步编程解决方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1001'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 07:28:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=1001'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我相信, 在我们平时的开发过程当中, 大家或多或少的都会遇到要处理异步逻辑的情况, 最常见的情形比如是一个页面需要请求两个或者多个接口, 然后等这几个接口都返回之后再渲染页面, 这样的逻辑我们可以用<code>回调函数</code>的方式去完成, 以及<code>ES6</code>里的<code>generator</code>函数, 当然啦, 还有目前大家使用最多的, 也是<code>ES6</code>提供的另一个解决方案: <code>promise</code>对象, <code>回调函数</code>的方式如果嵌套层数一多则会造成传说中的<code>回调地狱</code>问题, 代码冗余的同时不易维护, 而<code>generator</code>则被<code>promise</code>的光环盖过了, 目前在使用率上个人觉得是低于<code>promise</code>的, 不过<code>蚂蚁金服</code>的<code>redux</code>的框架<a href="https://dvajs.com/" target="_blank" rel="nofollow noopener noreferrer">dvajs</a>还在使用, 个人推测是历史遗留问题, 但仅仅是推测, 但话又说回来, <code>dvajs</code>使用<code>generator</code>来解决异步逻辑并没有什么不妥, 目前这套体系已经很成熟, 使用<code>promise</code>来重构duck不必</p>
<p>接下来就是<code>promise</code>, 说起<code>promise</code>想必大家都不陌生, 它是目前<code>js</code>异步逻辑最成熟的解决方案<del>之一</del>, 但如果聊到<code>promis</code>, 那么就一定离不开我们今天要聊的<code>async/await</code>, 因为没有它们, <code>promise</code>只是异步编程解决方案, 但有了它们才是优雅的异步编程解决方案</p>
<h1 data-id="heading-0">promise</h1>
<p>这不是本篇的重点, 但还是稍微聊一聊, 相信大多数的朋友对于这个语法已经很熟悉了, 如有不了解的童鞋可以查阅阮一峰老师的<a href="https://es6.ruanyifeng.com/#docs/promise" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 6 入门_Promise 对象</a>, 个人认为这是一篇不可多得的学习<code>ES6</code>相关语法的好文章</p>
<p>首先, <code>Promise</code>是一个<code>构造函数</code>, 需要我们使用<code>new</code>操作符调用, 从而生成一个<code>promise</code>对象, <code>Promise</code>接收一个<code>函数</code>作为参数, 同时这个函数还有两个参数, 这两个参数也是函数, 这两个函数依次是<code>resolve</code>和<code>reject</code>, 分别表示<code>成功</code>和<code>失败</code>:</p>
<pre><code class="copyable">const promise = new Promise(
  (resolve, reject) => &#123;
    //...
    if(/* 异步操作成功 */) &#123;
      //返回异步操作的结果
      resolve(value);
    &#125;else&#123;
      //异步操作失败, 返回错误或者其他内容
      reject(error);
    &#125;
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的<code>promise</code>对象上有一个<code>then</code>的方法, 这是<code>成功</code>的回调, 还有一个<code>catch</code>的方法, 这个方法则是<code>失败</code>的回调, 同时<code>then</code>方法会返回一个<code>promise</code>对象, 意味着我们可以使用<code>jQuery</code>那样的<code>链式</code>写法书写我们的代码:</p>
<pre><code class="copyable">promise
  .then(
    value => &#123;
      //...
    &#125;
  )
  .catch(
    error => &#123;
      //...
    &#125;
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大多数情况我们会把<code>promise</code>对象当做一个函数的返回值来使用:</p>
<pre><code class="copyable">const handlePromise = () => (
  new Promise(
    (resolve, reject) => &#123;
      //...
      if(/* 异步操作成功 */) &#123;
        //返回异步操作的结果
        resolve(value);
      &#125;else&#123;
        //异步操作失败, 返回错误或者其他内容
        reject(error);
      &#125;
    &#125;
  )
);

handlePromise()
  .then(
    value => &#123;
      //...
    &#125;
  )
  .catch(
    error => &#123;
      //...
    &#125;
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">async/await</h1>
<h1 data-id="heading-2">语法</h1>
<p>接下来就是我们今天的主角: <code>async/await</code>, 这两个关键字是<code>ES8</code>的关键字, 配合<code>ES6</code>的<code>promies</code>就组成了目前<code>js</code>中最优雅的异步解决方案, 在此之前我们先来看看它们的语法是怎样的, 它们的语法很简单:</p>
<ol>
<li><code>async</code>将一般的函数变成了<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function" target="_blank" rel="nofollow noopener noreferrer">异步函数</a></li>
<li><code>await</code>只能在<code>异步函数</code>中使用, 同时它可以放在任何函数调用之前(这里主要是放在返回<code>promise</code>对象的函数调用之前)</li>
<li>当<code>await</code>后面的函数有返回值, 那么我们将可以使用这个函数的返回值(如果那个函数返回的是<code>promise</code>对象, 则返回值是<code>promise</code> <code>resolve</code>返回的值, 也就是异步操作成功之后返回的值)</li>
</ol>
<p>也就说它们是一起出现, 同时我们只能在<code>async</code>函数里面使用<code>await</code>关键字来接收函数的返回值</p>
<h2 data-id="heading-3">async的用法</h2>
<p>了解了语法, 那么我们来看看它们在实际业务中的写法, 首先看看<code>async</code>怎么用的, <code>async</code>是<code>asynchronous</code>的缩写, <code>异步</code>的意思, 它会将普通函数改为<code>异步函数</code>, 写法有两种</p>
<h3 data-id="heading-4">函数声明/定义</h3>
<p>就是使用<code>function</code>关键字声明一个函数, 将<code>async</code>写在<code>函数声明</code>之前, 那么这个普通的函数就变成了<code>异步函数</code></p>
<pre><code class="copyable">async function foo() &#123;
  //...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后是模块化的写法:</p>
<pre><code class="copyable">export async function foo() &#123;
  //...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">export default async function foo() &#123;
  //...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我个人的习惯是在导出<code>class</code>和<code>组件</code>的时候使用<code>export default</code>, 当只是一个<code>util</code>一个工具类函数的时候则使用<code>export</code>, 这个因人而异, 没有对错之分, 习惯使然, 只要注意<code>export default</code>和<code>export</code>的区别即可, 关于这两种导出方式的区别可以查看这篇文章: <a href="https://juejin.cn/post/6965482913857028127" target="_blank">ES6模块化import export的用法</a></p>
<h3 data-id="heading-5">函数表达式的写法</h3>
<p>使用了<code>ES6</code>之后, <code>函数表达式</code>就变成了我们写函数时最常用的方式了, 由于没有了<code>function</code>关键字, 此时<code>异步函数</code>的写法就稍有不同了:</p>
<pre><code class="copyable">const foo = async () => &#123;
  //...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相应的模块化的语法则为:</p>
<pre><code class="copyable">export const foo = async () => &#123;
  //...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">await的用法</h2>
<p>聊完了<code>async</code>的用法, 接下来我们聊聊<code>await</code>的用法, <code>await</code>这个单词的意思就是<code>等待</code>的意思</p>
<h3 data-id="heading-7">写在普通函数调用之前</h3>
<p>无论写在什么函数调用的前面, 都要留意它必须用在<code>异步函数</code>内:</p>
<pre><code class="copyable">const bar = () => &#123;
  console.log(123);
&#125;

const foo = async () => &#123;
  await bar();
&#125;;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有在<code>async</code>函数中写<code>await</code>, 而是在普通函数中写<code>await</code>:</p>
<pre><code class="copyable">const bar = () => &#123;
  console.log(123);
&#125;

const foo = () => &#123;
  await bar();
&#125;;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时将报错: <code>await is only valid in async function</code></p>
<p>输出结果<code>123</code>, 倘若我们用一个变量去接收<code>bar</code>函数的返回值, 那结果是什么呢? 看代码我们会发现, <code>bar</code>函数并没有返回值, 所以结果是<code>undefined</code>:</p>
<pre><code class="copyable">const bar = () => &#123;
  console.log(123);
&#125;

const foo = async () => &#123;
  const res = await bar();
  console.log(res);
&#125;;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时先输出了<code>123</code>, 然后输出了<code>undefined</code>, 那如果我们让<code>bar</code>函数有一个返回值呢? 比如:</p>
<pre><code class="copyable">const bar = () => &#123;
  console.log(123);
  return 1;
&#125;

const foo = async () => &#123;
  const res = await bar();
  console.log(res);
&#125;;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时则是先输出<code>123</code>, 然后再输出<code>1</code>, 我们发现我们接收到了<code>bar</code>函数的返回值, 然而平时我们在不写<code>await</code>的时候也能正常的获取某个函数的返回值:</p>
<pre><code class="copyable">const bar = () => &#123;
  console.log(123);
  return 1;
&#125;

const foo = async () => &#123;
  const res = bar();
  console.log(res);
&#125;;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种情况下使用<code>await</code>似乎就没意义了, 这也解释了为何单独使用<code>await</code>会报错, 因为它只在返回<code>promise</code>的时候使用才有意义</p>
<h3 data-id="heading-8">写在promise函数调用之前</h3>
<p>确切的说是写在返回<code>promise</code>对象的函数调用之前:</p>
<pre><code class="copyable">const bar = () => (
  new Promise(
    resolve => &#123;
      resolve(123);
    &#125;
  )
)

const foo = async () => &#123;
  const res = await bar();
  console.log(res);
&#125;;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时变量<code>res</code>的值是<code>123</code>, 也就是说我们的<code>await</code>会等待<code>promise</code>执行<code>成功</code>也就是执行<code>resolve</code>方法, 从而接收<code>resolve</code>方法的返回值, 如果不使用<code>await</code>, 那么我们就只是接收到一个<code>promise</code>对象而已</p>
<h1 data-id="heading-9">实现交通信号灯</h1>
<p>回到最初的问题, <code>async/await</code>究竟优雅在什么地方呢? 那我们就要先看看单独使用<code>promise</code>不优雅在哪些地方, 上面的<code>promise</code>的代码其实还是使用了<code>回调函数</code>的写法, 也就是说如果有多个异步操作, 那么就会矫枉过正了, 会再回到我们的<code>回调地狱</code>中去, 得不偿失</p>
<p>比如我们要实现一个交通信号灯, 3秒之后绿灯, 1秒之后黄灯, 2秒之后红灯, 依次对比两种方法</p>
<h2 data-id="heading-10">promise+then</h2>
<pre><code class="copyable">const trafficLight = (duration, color) => (
  new Promise(
    resolve => &#123;
      setTimeout(
        () => &#123;
          console.log(color);
          resolve();
        &#125;,
        duration
      )
    &#125;
  )
)

const main = () => &#123;
  trafficLight(3000, 'green').then(
    () => &#123;
      trafficLight(1000, 'yellow').then(
        () => &#123;
          trafficLight(2000, 'red').then(
            () => &#123;
              main();
            &#125;
          )
        &#125;
      )
    &#125;
  )
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看着我们的<code>main</code>函数中的回调, 我整个人都开始不好了...</p>
<h2 data-id="heading-11">async/await+promise</h2>
<p>接下来我们把上面的写法改造一下:</p>
<pre><code class="copyable">const trafficLight = (duration, color) => (
  new Promise(
    resolve => &#123;
      setTimeout(
        () => &#123;
          console.log(color);
          resolve();
        &#125;,
        duration
      )
    &#125;
  )
)

const main = async () => &#123;
  await trafficLight(3000, 'green');
  await trafficLight(1000, 'yellow');
  await trafficLight(2000, 'red');
  main();
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果一样, 但此时我们再看<code>main</code>函数中的写法, 一行接着一行, 用同步的写法实现了异步的逻辑, 看起来代码'清爽'了不少, 最重要的是逻辑更加清晰, '等待'一行执行结束再执行下一行, 再'等待', 再执行...代码量更少, 更易于维护, 这便是它的优雅之处了</p>
<p>参考文章:</p>
<blockquote>
<ol>
<li><a href="https://es6.ruanyifeng.com/#docs/promise" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 6 入门_Promise 对象</a></li>
</ol>
</blockquote>
<blockquote>
<ol start="2">
<li><a href="https://es6.ruanyifeng.com/#docs/async" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 6 入门_async 对象</a></li>
</ol>
</blockquote>
<blockquote>
<ol start="3">
<li><a href="https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Async_await" target="_blank" rel="nofollow noopener noreferrer">async和await:让异步编程更简单</a></li>
</ol>
</blockquote></div>  
</div>
            