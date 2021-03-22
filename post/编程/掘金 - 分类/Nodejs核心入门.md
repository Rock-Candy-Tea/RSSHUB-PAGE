
---
title: 'Node.js核心入门'
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 18:37:00 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言：</h2>
<p>因为以前学习Node.js并没有真正意义上的去学习它，而是粗略的学习了npm的常用命令和Node.js一些模块化的语法，因此昨天花了一天的时间看了《Node.js开发指南》一书。通过这本书倒是让我对Node.js的认识更为全面，但由于这本书出版时间过早，有些API已经发生了变化或已经被废弃，而对于学习Node.js来说，核心部分又是最为重要的一环，因此我配合官方文档对这本书的第四章-Node.js核心进行了总结与梳理，由于水平有限，如有疏漏与错误，请指正。</p>
<h2 data-id="heading-1">正文</h2>
<p>核心模块是Node.js的心脏，主要是有一些精简高效的库组成（这方面和Python有很大的相似之处），为Node.js提供了基础的API。主要内容包括：</p>
<p><strong>Node.js核心入门（一）</strong></p>
<p>全局对象
常用工具
事件机制</p>
<p><strong>Node.js核心入门（二）</strong></p>
<p>文件系统访问
HTTP服务器与客户端</p>
<h2 data-id="heading-2">全局对象</h2>
<p>全局对象我想学过JavaScript的都知道在浏览器是window，在程序的任何地方都可以访问到全局对象，而在Node.js中，这个全局对象换成了global，所有的全局变量（除了global本身）都是global对象的属性。而我们在Node.js中能够直接访问的对象通常都是global的属性，如：console，process等。</p>
<p>##全局对象与全局变量</p>
<p>global最根本的作用就是作为全局变量的宿主。按照ECMAScript规范，满足以下条件的变量即为全局变量：</p>
<ul>
<li>在最外层定义的变量（在Node.js中不存在，因为Node.js的代码在模块中执行，不存在在最外层定义变量）</li>
<li>全局对象的属性</li>
<li>隐式定义的变量（即未定义而直接进行赋值的变量）</li>
</ul>
<p>当我们定义一个全局变量的时候，这个全局变量会自动成为全局变量的属性。</p>
<h2 data-id="heading-3">process</h2>
<p>process 对象是一个全局变量，它提供当前 Node.js 进程的相关信息，以及控制当前 Node.js 进程。通常我们在写本地命令行程序的时候，少不了和它打交道。下面是它的最常用的成员方法：</p>
<p><strong>1.process.argv</strong></p>
<p>process.argv 属性返回一个数组，这个数组包含了启动Node.js进程时的命令行参数。第一个元素为process.execPath，第二个元素为当前执行的JavaScript文件路径，剩余的元素为其他命令行参数。</p>
<p>例如存储一个名为argv.js的文件：</p>
<pre><code class="copyable">// print process.argv
process.argv.forEach((val, index) => &#123;
 console.log(`$&#123;index&#125;: $&#123;val&#125;`);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>则命令行运行时这样的：</p>
<pre><code class="copyable">$ node process-args.js one two=three four

0: /usr/local/bin/node
1: /Users/mjr/work/node/process-args.js
2: one
3: two=three
4: four
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.process.stdout</strong></p>
<p>process.stdout是标准输出流，通常我们使用的console.log()输出打印字符，而process.stdout.write()函数提供了更为底层的接口。</p>
<p><code>process.stdout.write('请输入num1的值：'); </code></p>
<p><strong>3.process.stdin</strong></p>
<p>process.stdin是标准输入流，初始时它是暂停的，要想从标准输入读取数据，我们必须恢复流，并手动编写流的事件响应函数。</p>
<pre><code class="copyable">/*1:声明变量*/
var num1, num2;
/*2：向屏幕输出，提示信息，要求输入num1*/
process.stdout.write('请输入num1的值：');
/*3：监听用户的输入*/
process.stdin.on('data', function (chunk) &#123;
   if (!num1) &#123;
       num1 = Number(chunk);
       /*4：向屏幕输出，提示信息，要求输入num2*/
       process.stdout.write('请输入num2的值');
   &#125; else &#123;
       num2 = Number(chunk);
       process.stdout.write('结果是：' + (num1 + num2));
   &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.process.nextTick(callback[, ...args])</strong></p>
<p>...args  调用 callback时传递给它的额外参数
process.nextTick()方法将 callback 添加到"next tick 队列"。 一旦当前事件轮询队列的任务全部完成，在next tick队列中的所有callbacks会被依次调用。
这种方式不是setTimeout(fn, 0)的别名。它更加有效率，因此别用setTimeout去代替process.nextTick。事件轮询随后的ticks 调用，会在任何I/O事件（包括定时器）之前运行。</p>
<pre><code class="copyable">console.log('start');
process.nextTick(() => &#123;
 console.log('nextTick callback');
&#125;);
console.log('scheduled');

// start
// scheduled
// nextTick callback
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>console</strong></p>
<p>console 模块提供了一个简单的调试控制台，类似于 Web 浏览器提供的 JavaScript 控制台。该模块导出了两个特定的组件：</p>
<ul>
<li>一个 Console 类，包含 console.log() 、 console.error() 和 console.warn() 等方法，可以被用于写入到任何 Node.js 流。</li>
<li>一个全局的 console 实例，可被用于写入到 process.stdout 和 process.stderr。 全局的 console 使用时无需调用 require('console')。(注意：全局的 console 对象的方法既不总是同步的（如浏览器中类似的 API），也不总是异步的（如其他 Node.js 流)。</li>
</ul>
<p>比如全局下的常见的console实例：</p>
<pre><code class="copyable">console.log('hello，world');
// hello，world
console.log('hello%s', 'world');
// helloworld
console.error(new Error('错误信息'));
//  Error: 错误信息
const name = '描述';
console.warn(`警告$&#123;name&#125;`);
// 警告描述
console.trace() // 向标准错误流输出当前的调用栈
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常见的Console类：</p>
<pre><code class="copyable">const out = getStreamSomehow();
const err = getStreamSomehow();
const myConsole = new console.Console(out, err);

myConsole.log('hello，world');
// hello，world
myConsole.log('hello%s', 'world');
// helloworld
myConsole.error(new Error('错误信息'));
// Error: 错误信息
const name = '描述';
myConsole.warn(`警告$&#123;name&#125;`);
//警告描述
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">常用工具 util</h2>
<p>util 模块主要用于支持 Node.js 内部 API 的需求。 大部分实用工具也可用于应用程序与模块开发者，用于弥补核心JavaScript的功能的不足。它的可以这样调用：</p>
<p><code>const util = require('util'); </code></p>
<p><strong>1.util.inspect(object[, options])</strong></p>
<p>util.inspect() 方法返回 object 的字符串表示，主要用于调试和错误输出。 附加的 options 可用于改变格式化字符串的某些方面。它至少接受一个参数objet，即要转换的参数，而option则是可选的，可选内容如下：</p>
<ul>
<li>showHidden  如果为 true，则 object 的不可枚举的符号与属性也会被包括在格式化后的结果中。 默认为 false。</li>
<li>depth  指定格式化 object 时递归的次数。 这对查看大型复杂对象很有用。 默认为 2。 若要无限地递归则传入 null。</li>
<li>colors  如果为 true，则输出样式使用 ANSI 颜色代码。 默认为 false，可自定义。</li>
<li>customInspect  如果为 false，则 object 上自定义的 inspect(depth, opts) 函数不会被调用。 默认为 true。</li>
<li>showProxy  如果为 true，则 Proxy 对象的对象和函数会展示它们的 target 和 handler 对象。 默认为 false。</li>
<li>maxArrayLength  指定格式化时数组和 TypedArray 元素能包含的最大数量。 默认为 100。 设为 null 则显式全部数组元素。 设为 0 或负数则不显式数组元素。</li>
<li>breakLength  一个对象的键被拆分成多行的长度。 设为 Infinity 则格式化一个对象为单行。 默认为 60。</li>
</ul>
<p>例如，查看 util 对象的所有属性：</p>
<pre><code class="copyable">const util = require('util');
console.log(util.inspect(util, &#123; showHidden: true, depth: null &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.util.callbackify(original)</strong></p>
<p>util.callbackify(original)方法将 async 异步函数(或者一个返回值为 Promise 的函数)转换成遵循 Node.js 回调风格的函数。 在回调函数中, 第一个参数 err 为 Promise rejected 的原因 (如果 Promise 状态为 resolved , err为 null ),第二个参数则是 Promise 状态为 resolved 时的返回值。例如：</p>
<pre><code class="copyable">const util = require('util');

async function fn() &#123;
 return await Promise.resolve('hello world');
&#125;
const callbackFunction = util.callbackify(fn);

callbackFunction((err, ret) => &#123;
 if (err) throw err;
 console.log(ret);
&#125;);
// hello world
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：</p>
<ul>
<li>回调函数是异步执行的, 并且有异常堆栈错误追踪. 如果回调函数抛出一个异常, 进程会触发一个 'uncaughtException' 异常, 如果没有被捕获, 进程将会退出。</li>
<li>null 在回调函数中作为一个参数有其特殊的意义, 如果回调函数的首个参数为 Promise rejected 的原因且带有返回值, 且值可以转换成布尔值 false, 这个值会被封装在 Error 对象里, 可以通过属性 reason 获取。</li>
</ul>
<pre><code class="copyable">function fn() &#123;
 return Promise.reject(null);
&#125;
const callbackFunction = util.callbackify(fn);

callbackFunction((err, ret) => &#123;
   // 当Promise的rejecte是null时，它的Error与原始值都会被存储在'reason'中。
 err && err.hasOwnProperty('reason') && err.reason === null;  // true
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">事件驱动 events</h2>
<p>events是Node.js最重要的模块，原因是Node.js本身架构就是事件式的，大多数 Node.js 核心 API 都采用惯用的异步事件驱动架构，而它提供了唯一的接口，因此堪称Node.js事件编程的及时。events 模块不仅用于用户代码与 Node.js 下层事件循环的交互，还几乎被所有的模块依赖。</p>
<p>所有能触发事件的对象都是 EventEmitter 类的实例。 这些对象开放了一个 eventEmitter.on() 函数，允许将一个或多个函数绑定到会被对象触发的命名事件上。 事件名称通常是驼峰式的字符串，但也可以使用任何有效的 JavaScript 属性名。对于每个事件， EventEmitter支持若干个事件监听器。当事件发射时，注册到这个事件的事件监听器被依次调用，事件参数作
为回调函数参数传递。</p>
<p>例如：</p>
<pre><code class="copyable">const EventEmitter = require('events');

class MyEmitter extends EventEmitter &#123;&#125;

const myEmitter = new MyEmitter();
// eventEmitter.on() 方法用于注册监听器
myEmitter.on('event', () => &#123;
 console.log('触发了一个事件！');
&#125;);
// eventEmitter.emit() 方法用于触发事件
myEmitter.emit('event');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面让我们来看看EventEmitter最常用的API：</p>
<p>-EventEmitter.on(event, listener) 方法可以添加 listener 函数到名为 eventName 的事件的监听器数组的末尾。不会检查 listener 是否已被添加。多次调用并传入相同的 eventName 和 listener 会导致 listener 被添加与调用多次。
-emitter.prependListener(eventName, listener)方法可以添加 listener 函数到名为 eventName 的事件的监听器数组的开头。 不会检查 listener 是否已被添加。 多次调用并传入相同的 eventName 和 listener 会导致 listener 被添加与调用多次。
-eventEmitter.emit() 方法允许将任意参数传给监听器函数。当一个普通的监听器函数被 EventEmitter 调用时，标准的 this 关键词会被设置指向监听器所附加的 EventEmitter。</p>
<pre><code class="copyable">// 实例：
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// 打印:
//   b
//   a
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>EventEmitter.once(event, listener) 为指定事件注册一个单次监听器，即监听器最多只会触发一次，触发后立刻解除该监听器。</li>
</ul>
<pre><code class="copyable">server.once('connection', (stream) => &#123;
  console.log('首次调用！');
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>EventEmitter.removeListener(event, listener) 移除指定事件的某个监听器， listener 必须是该事件已经注册过的监听器。（注意：removeListener 最多只会从监听器数组里移除一个监听器实例。 如果任何单一的监听器被多次添加到指定 eventName 的监听器数组中，则必须多次调用 removeListener 才能移除每个实例。）</li>
</ul>
<pre><code class="copyable">const callback = (stream) => &#123;
  console.log('有连接！');
&#125;;
server.on('connection', callback);
// ...
server.removeListener('connection', callback);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>EventEmitter.removeAllListeners([event]) 移除所有事件的所有监听器，如果指定 event ，则移除指定事件的所有监听器。</li>
</ul>
<pre><code class="copyable">const callback = (stream) => &#123;
  console.log('有连接！');
&#125;;
server.on('connection', callback);
// ...
server.removeListener('connection', callback);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">error 事件</h2>
<p>EventEmitter 定义了一个特殊的事件 error ，它包含了“错误”的语义，我们在遇到异常的时候通常会发射 error 事件。当 error被发射时，EventEmitter规定如果没有响
应的监听器，Node.js 会把它当作异常，退出程序并打印调用栈。我们一般要为会发射 error 事件的对象设置监听器，避免遇到错误后整个程序崩溃。</p>
<pre><code class="copyable">var events = require('events');
var emitter = new events.EventEmitter();
emitter.emit('error');
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">继承EventEmitter</h2>
<p>大多数情况下，我们不会直接使用EventEmitter，而是在对象中继承它，包括fs,http在内的只要是支持事件响应的核心模块都是EventEmitter的子类。这样做的原因有以下两个：</p>
<ul>
<li>具有某个实体功能的对象实现事件符合语义，事件的监听和发射应该是一个对象的方法。</li>
<li>JavaScript 的对象机制是基于原型的，支持部分多重继承，继承 EventEmitter 不会打乱对象原有的继承关系。</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            