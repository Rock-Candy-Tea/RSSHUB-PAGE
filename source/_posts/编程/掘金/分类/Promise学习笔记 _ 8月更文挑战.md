
---
title: 'Promise学习笔记 _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5559'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 18:58:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=5559'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">准备工作</h1>
<h2 data-id="heading-1">实例对象和函数对象</h2>
<pre><code class="copyable">function Fn()&#123;
​
&#125;
const fn=new Fn();//fn是实例对象，简称为对象
console.log(Fn.prototype);//Fn是函数对象，将一个函数作为对象使用
​
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你写在括号的左边的东西肯定是函数，比如你写<code>a()</code>，那我们知道a肯定是个函数。在点的左边，必然是对象。</p>
<p>看到代码，你要知道数据类型，先看懂语法，再看懂功能。</p>
<h2 data-id="heading-2">两种类型的回调函数 同步回调和异步回调</h2>
<p>什么样的函数是回调函数？要三个条件同时满足：</p>
<ol start="0">
<li>回调函数要是你自己定义的</li>
<li>回调函数我没有亲自调用</li>
<li>但是他最后执行了</li>
</ol>
<pre><code class="copyable">//同步回调函数
const arr=[1,3,5];
arr.forEach(item=>&#123; //这就是同步回调函数，不会放入队列，执行完了才会执行后面的
  console.log(item); //他先打印
&#125;);
console.log('forEach()之后'); //他后打印
​
//异步回调函数
setTimeout(()=>&#123; //这就是异步回调函数，会放入队列中将来执行
    console.log('aaa'); //他后打印
&#125;,0);
console.log('bbb'); //他先打印
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">JS中的error处理</h2>
<h3 data-id="heading-4">常见的内置错误</h3>
<ol start="0">
<li>ReferenceError 引用的变量不存在</li>
<li>TypeError 数据类型不正确的错误</li>
<li>RangeError 数据值不在其所允许的范围内</li>
<li>SyntaxError 语法错误</li>
</ol>
<p>错误不捕获，下面的代码不会执行</p>
<h3 data-id="heading-5">错误的处理（捕获与抛出）</h3>
<p>捕获用try ... catch</p>
<pre><code class="copyable">try&#123;
  let d;
  console.log(d.xxx);
&#125; catch (error)&#123;  //在这里有个调试的技巧，如果你不知道error里有什么属性，可以在这行打个断点，然后运行到这里时，在source里鼠标hover上去就可以看到
  console.log(error.message);
&#125;
console.log('出错之后');  //在这行就能输出了，因为错误被处理了
<span class="copy-code-btn">复制代码</span></code></pre>
<p>抛出错误 throw error 自己去抛出的</p>
<pre><code class="copyable">function something()&#123;
  if(Date.now()%2===1)&#123;
    console.log('111');
  &#125; else &#123;  //如果时间是偶数，抛出异常，由调用者来处理
    throw new Error('222');
  &#125;
&#125;
try &#123;
  something();
&#125; catch (error) &#123;
  console.log(error.message);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">promise的理解和使用</h1>
<p>学技术的基本流程，拿到一个新东西，<strong>这个东西是什么？为什么要用这个？怎么用这个？</strong> 前两个绝对不能忘，语法可以忘</p>
<h2 data-id="heading-7">promise是什么</h2>
<p>承诺将来给你一个数据，只不过成功的数据还是失败的数据我一开始不知道</p>
<p>讲抽象一点：是js中执行异步编程的新的解决方案，旧的是纯回调的形式，为啥要说纯，因为promise里也有回调</p>
<p>讲具体一点：Promise是一个构造函数，promise对象用来封装一个异步操作并可以获取其结果</p>
<h2 data-id="heading-8">promise的状态改变</h2>
<ol start="0">
<li>pending变为resolved</li>
<li>pending变为rejected</li>
</ol>
<p><strong>只有</strong>这两种变化，而且一个promise对象只能改变一次，无论是变为成功还是失败，都会有一个结果数据</p>
<h2 data-id="heading-9">promise的基本流程</h2>
<p>新建一个promise对象，new Promise()，这个promise对象是pending状态，这个promise在创建的时候要传进去参数，参数是函数（启动异步任务的函数），执行异步任务成功，就执行resolve()，promise对象会变成resolved状态，一旦变成这个状态，就会去调用成功的回调函数，then()可以指定成功和失败的回调函数；执行异步任务失败，就执行reject()，promise对象会变成rejected状态，一旦变成这个状态，就会去调用失败的回调函数，catch()可以指定失败的回调函数；then()和catch()都会返回新的promise对象。</p>
<h2 data-id="heading-10">promise的基本使用</h2>
<p>你要好好理解下“返回一个promise”这句话是什么意思</p>
<pre><code class="copyable">const p=new Promise((resolve,reject)=>&#123;  //执行器函数，同步回调，执行异步操作任务
  setTimeout(()=>&#123;
    const time=Date.now();
    if(time%2==0)&#123;
      resolve('succcess');
    &#125;
    else&#123;
      reject('fail');
    &#125;
  &#125;,1000)
&#125;);
p.then(
  //成功的回调函数
  value=>&#123;  //value不是我自己去取的，而是他自己交给我的，下面的reason也一样
    
  &#125;,
  //失败的回调函数
  reason=>&#123;
  
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">为什么要用promise</h2>
<p>假设现在有一个名为 <code>createAudioFileAsync()</code> 的函数，它接收一些配置和两个回调函数，然后异步地生成音频文件。一个回调函数在文件成功创建时被调用，另一个则在出现异常时被调用。</p>
<pre><code class="copyable">// 成功的回调函数
function successCallback(result) &#123;
  console.log("音频文件创建成功: " + result);
&#125;
​
// 失败的回调函数
function failureCallback(error) &#123;
  console.log("音频文件创建失败: " + error);
&#125;
​
//以前你就要这么写,你必须在你真正执行异步操作前就要指定好成功和失败的回调函数,你是先指定了回调函数，后启动了异步任务
createAudioFileAsync(audioSettings, successCallback, failureCallback)
​
//用promise就这么写
//如果已经得到了一个promise对象，异步任务肯定是已经启动了，做没做完我先不管
const promise = createAudioFileAsync(audioSettings);
promise.then(successCallback, failureCallback);
//而且就算你这个异步任务执行需要2s，而我是在3s之后才给你指定了then的回调函数，我一样可以正常执行回调
//也就是说我可以在你异步任务执行完成之后才指定回调函数，异步任务启动和执行完成是两码事，不要搞混
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说promise相对于传统的纯回调函数的第一个优势在于<strong>指定回调函数的方式更加灵活</strong>，promise：启动异步任务=》返回promise对象=》给promise对象指定回调函数</p>
<p>接下来是第二个优势，<strong>promise支持链式调用，可以解决回调地狱问题，其实回调地狱的终极解决方法是async,await，因为这两个就没有回调函数了</strong></p>
<pre><code class="copyable">//先搞第一个，再搞第二个，后一个异步任务依赖前一个异步任务的结果的场景
//纯回调函数嵌套调用，不便于阅读，也不便于异常处理
doSomething(function(result) &#123;
  doSomethingElse(result, function(newResult) &#123;
    doThirdThing(newResult, function(finalResult) &#123;
      console.log('Got the final result: ' + finalResult);
    &#125;, failureCallback);
  &#125;, failureCallback);
&#125;, failureCallback);
​
//用promise就这么写了
doSomething().then(function(result) &#123;
  return doSomethingElse(result);  //这一行好好看
&#125;)
.then(function(newResult) &#123;
  return doThirdThing(newResult);
&#125;)
.then(function(finalResult) &#123;
  console.log('Got the final result: ' + finalResult);
&#125;)
.catch(failureCallback); //如果上面三个任何一个出了异常，都会跳到这里，异常传透
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">async function foo() &#123;
  try &#123;
    const result = await doSomething();
    const newResult = await doSomethingElse(result);
    const finalResult = await doThirdThing(newResult);
    console.log(`Got the final result: $&#123;finalResult&#125;`);
  &#125; catch(error) &#123;
    failureCallback(error);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">Promise如何使用</h2>
<p>语法上不要有障碍，感觉看不懂自己想办法</p>
<p>API自己去看MDN</p>
<p><code>Promise.prototype.then()</code>方法返回一个新的promise对象</p>
<pre><code class="copyable">new Promise((resolve,reject)=>&#123; //你也不是非得叫这两个名字，可以随便取
 
&#125;)
​
// 产生一个成功值或失败值为几几几的promise对象，你要是以前就要这么写
const p1=new Promise((resolve,reject)=>&#123;
    resolve(1);
&#125;)
//现在有语法糖，写起来就简单多了
const p2=Promise.resolve(2);
const p3=Promise.reject(3);
​
p1.then(value=>&#123;console.log(value)&#125;);
p2.then(value=>&#123;console.log(value)&#125;);
p3.catch(reason=>&#123;console.log(reason)&#125;);
​
const pAll=Promise.all([p1,p2,p3]);
pAll.then(
  values=>&#123;&#125;,
  reason=>&#123;
      console.log(reason); //3
  &#125;
)
​
const pRace=Promise.race([p1,p2,p3]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">Promise的几个关键问题</h2>
<p>1.如何改变promise的状态？除了resolve(value)和reject(reason)，还可以<strong>抛出异常</strong>，如果当前是pendding，就会变成rejected</p>
<pre><code class="copyable">const p=new Promise((resolve,reject)=>&#123;
  throw new Error('aaa');  //reason为抛出的error
  //你直接抛出一个3都行
  //throw 3; reason为3
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.一个promise指定多个成功/失败的回调函数，都会调用吗？</p>
<p>是的</p>
<pre><code class="copyable">//promise改变为对应状态时都会调用的
p.then(
  value=>&#123;...&#125;,
  reason=>&#123;...&#125;
)
p.then(
  value=>&#123;...&#125;,
  reason=>&#123;...&#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.改变promise状态和指定回调函数谁先谁后？</p>
<p>都有可能，你先指定回调函数或者先改变promise状态都行。</p>
<pre><code class="copyable">new Promise((rosolve,reject)=>&#123;
  setTimeout(()=>&#123;
    resolve(1);  //后改状态(同时指定了数据)，异步指定回调函数，问题是他到时候怎么知道回调函数在哪？
  &#125;,1000)
&#125;).then(  //先指定回调函数  所以在这里会先保存当前指定的回调函数
  value=>&#123;&#125;,
  reason=>&#123;console.log(reason)&#125;
)
​
//先改状态再指定回调，可以在执行器中直接调用resolve()/reject()，或者延迟更长时间才调用then()
new Promise((rosolve,reject)=>&#123;
    resolve(1);  //先改状态(同时指定了数据)，这时候是把状态存起来
&#125;).then(  //后指定回调函数，异步执行回调函数,注意：then是同步，then里面的回调函数是异步执行
  value=>&#123;&#125;,
  reason=>&#123;console.log(reason)&#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.promise.then()返回的新promise的结果状态由什么决定？</p>
<p>（插一句，then可以串联多个操作任务，这是他的一个用途）</p>
<p>简单说：由then()指定的回调函数执行的结果决定</p>
<p>详细说：（1） 如果抛出异常，新promise变为rejected，reason为抛出的异常，你抛出啥，后面的就接啥，不管抛出的是Error对象还是一个数字</p>
<p>（2） 如果返回的是非promise的任意值，新promise变为resolved，value为返回的值（比如你在then里写同步操作就可以这么写）</p>
<p>（3）如果返回的是一个新的promise，此promise的结果就会成为新promise的结果（比如你在then里写异步操作就可以这么写）</p>
<pre><code class="copyable">new Promise((resolve,reject)=>&#123;
  resolve(1)
&#125;).then(
  value=>&#123;
    console.log(value);
    //return 2;
    //return Promise.resolve(3);
    //return Promise.reject(4);
    //throw 5;
  &#125;,
  reason=>&#123;
    console.log(reason);
  &#125;
).then(
  value=>&#123;console.log(value)&#125;,
  reason=>&#123;console.log(reason)&#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.链式调用，每个链就只看他前面的的一环返回的是个啥，不要越级看；而且，你不要把then/catch本身和里面指定的函数搞混了，不是说catch返回的东西就一定 是失败的promise，要看他里面写的函数到底返回的是个啥</p>
<p>6.promise异常传透</p>
<p>异常传透不是一步跳过去的，也是一级一级传过去的</p>
<pre><code class="copyable">new Promise((resolve,reject)=>&#123;
  reject(1)
&#125;).then(
  value=>&#123;
    console.log(value);
  &#125;,
  // reason=>&#123;throw reason&#125; 其实我在这里没写失败的处理函数，但是相当于写了
).then(
 value=>&#123;
    console.log(value);
  &#125;,
  // 这里省略了，其实跟上面一样
).catch( // 这样就会一级一级传过来
  reason=>&#123;
    console.log(reason);
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7.中断promise链怎么中断？</p>
<pre><code class="copyable">new Promise((resolve,reject)=>&#123;
  reject(1)
&#125;).then(
  value=>&#123;
    console.log(value);
  &#125;
).catch(
 reason=>&#123; 
    console.log(reason);
    //如果我在这里不想往下传了
    return new Promise(()=>&#123;&#125;) //返回一个pending状态的promise
  &#125;
).then( // 就不会调用这里的回调
  value=>&#123;
    console.log(value);
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">手写Promise</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFZZZ1996%2FPromise-fzzz" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FZZZ1996/Promise-fzzz" ref="nofollow noopener noreferrer">见代码</a></p>
<h1 data-id="heading-15">async与await</h1>
<pre><code class="copyable">//async函数的返回值是promise对象
//这个promise对象的结果由async函数执行的返回值决定
async function fn1()&#123;
  //return 1;
  //throw 2;
  return Promise.resolve(3);
&#125;
​
const result=fn1();
result.then(
  value=>&#123;
      console.log('onResolved()',value);
  &#125;,
  reason=>&#123;
      console.log('onRejected()',reason);
  &#125;
)
​
function fn2()&#123;
    return new Promise((resolve,reject)=>&#123;
        setTimeout(()=>&#123;
            resolve(5);
        &#125;,1000)
    &#125;)
&#125;
​
async function fn3()&#123;
    //await所在的函数必须声明为async，但是async函数中可以没有await
    try&#123; //如果await的promise失败，就会抛出异常，需要通过try...catch来捕获处理
        const value=await fn2();// await右边跟表达式，取到的value就是promise里成功的数据
        //const value=await 3;//await右边也可以不写promise，得到的结果就是表达式的结果
    &#125;catch(error)&#123;
        console.log('得到失败的结果',error);
    &#125;
&#125;
fn3();
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">宏队列和微队列</h1>
<p>宏队列：dom事件回调，ajax回调，定时器回调</p>
<p>微队列：promise回调，mutation回调</p>
<p>将所有的同步代码执行完以后，才会去执行队列里面的回调函数，每次准备取出第一个宏任务执行前，都要将所有的微任务一个一个取出来执行。</p></div>  
</div>
            