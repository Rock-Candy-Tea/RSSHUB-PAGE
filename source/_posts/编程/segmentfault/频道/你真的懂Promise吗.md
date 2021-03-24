
---
title: '你真的懂Promise吗'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/remote/1460000039694580'
author: segmentfault
comments: false
date: 2021-03-24 08:14:53
thumbnail: 'https://segmentfault.com/img/remote/1460000039694580'
---

<div>   
<h2>前言</h2><p>在异步编程中，Promise 扮演了举足轻重的角色，比传统的解决方案（回调函数和事件）更合理和更强大。有些朋友对于这个几乎每天都在打交道的“老朋友”，貌似全懂,但稍加深入就可能疑问百出，本文带大家深入理解这个熟悉的陌生人—— Promise.</p><h2>基本用法</h2><h3>1.语法</h3><p><code>new Promise( function(resolve, reject) &#123;...&#125; /* executor */  )</code></p><ul><li>构建 Promise 对象时，需要传入一个 executor 函数，主要业务流程都在 executor 函数中执行。</li><li>Promise构造函数执行时立即调用executor 函数， resolve 和 reject 两个函数作为参数传递给executor，resolve 和 reject 函数被调用时，分别将promise的状态改为fulfilled（完成）或rejected（失败）。<strong>一旦状态改变，就不会再变</strong>，任何时候都可以得到这个结果。</li><li>在 executor 函数中调用 resolve 函数后，会触发 promise.then 设置的回调函数；而调用 reject 函数后，会触发 promise.catch 设置的回调函数。</li></ul><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039694580" alt title referrerpolicy="no-referrer"></span></p><p>值得注意的是，<strong>Promise 是用来管理异步编程的，它本身不是异步的</strong>，new Promise的时候会立即把executor函数执行，只不过我们一般会在executor函数中处理一个异步操作。比如下面代码中，一开始是会先打印出2。</p><pre><code class="javascript">let p1 = new Promise(()=>&#123;
    setTimeout(()=>&#123;
      console.log(1)
    &#125;,1000)
    console.log(2)
  &#125;)
console.log(3) // 2 3 1</code></pre><p>Promise 采用了回调函数延迟绑定技术，在执行 resolve 函数的时候，回调函数还没有绑定，那么只能<strong>推迟回调函数的执行</strong>。这具体是啥意思呢？我们先来看下面的例子：</p><pre><code class="javascript">let p1 = new Promise((resolve,reject)=>&#123;
  console.log(1);
  resolve('JAVA_朴先生')
  console.log(2)
&#125;)
// then:设置成功或者失败后处理的方法
p1.then(result=>&#123;
 //p1延迟绑定回调函数
  console.log('成功 '+result)
&#125;,reason=>&#123;
  console.log('失败 '+reason)
&#125;)
console.log(3)
// 1
// 2
// 3
// 成功 JAVA_朴先生</code></pre><p>new Promise的时候先执行executor函数，打印出 1、2，Promise在执行resolve时，触发微任务，还是继续往下执行同步任务，<br>执行p1.then时，存储起来两个函数（此时这两个函数还没有执行）,然后打印出3，此时同步任务执行完成，最后执行刚刚那个微任务，从而执行.then中成功的方法。</p><h3>错误处理</h3><p>Promise 对象的错误<strong>具有“冒泡”性质，会一直向后传递</strong>，直到被 onReject 函数处理或 catch 语句捕获为止。具备了这样“冒泡”的特性后，就不需要在每个 Promise 对象中单独捕获异常了。</p><p>要遇到一个then，要执行成功或者失败的方法，但如果此方法并没有在当前then中被定义，则顺延到下一个对应的函数</p><pre><code class="javascript">function executor (resolve, reject) &#123;
  let rand = Math.random()
  console.log(1)
  console.log(rand)
  if (rand > 0.5) &#123;
    resolve()
  &#125; else &#123;
    reject()
  &#125;
&#125;
var p0 = new Promise(executor)
var p1 = p0.then((value) => &#123;
  console.log('succeed-1')
  return new Promise(executor)
&#125;)
var p2 = p1.then((value) => &#123;
  console.log('succeed-2')
  return new Promise(executor)
&#125;)
p2.catch((error) => &#123;
  console.log('error', error)
&#125;)
console.log(2)</code></pre><p>这段代码有三个 Promise 对象：p0～p2。无论哪个对象里面抛出异常，都可以通过最后一个对象 p2.catch 来捕获异常，通过这种方式可以将所有 Promise 对象的错误合并到一个函数来处理，这样就解决了每个任务都需要单独处理异常的问题。</p><p>通过这种方式，我们就消灭了嵌套调用和频繁的错误处理，这样使得我们写出来的代码更加优雅，更加符合人的线性思维。</p><h3>Promise链式调用</h3><p>我们都知道可以把多个Promise连接到一起来表示一系列异步骤。这种方式可以实现的关键在于以下两个Promise 固有行为特性：</p><ul><li>每次你对Promise调用then，它都会创建并返回一个新的Promise，我们可以将其链接起来；</li><li>不管从then调用的完成回调（第一个参数）返回的值是什么，它都会被自动设置为被链接Promise（第一点中的）的完成。</li></ul><p>先通过下面的例子，来解释一下刚刚这段话是什么意思，然后详细介绍下链式调用的执行流程</p><pre><code class="javascript">let p1=new Promise((resolve,reject)=>&#123;
    resolve(100) // 决定了下个then中成功方法会被执行
&#125;)
// 连接p1
let p2=p1.then(result=>&#123;
    console.log('成功1 '+result)
    return Promise.reject(1) 
// 返回一个新的Promise实例，决定了当前实例是失败的，所以决定下一个then中失败方法会被执行
&#125;,reason=>&#123;
    console.log('失败1 '+reason)
    return 200
&#125;)
// 连接p2 
let p3=p2.then(result=>&#123;
    console.log('成功2 '+result)
&#125;,reason=>&#123;
    console.log('失败2 '+reason)
&#125;)
// 成功1 100
// 失败2 1</code></pre><p>我们通过返回 Promise.reject(1) ，完成了第一个调用then创建并返回的promise p2。p2的then调用在运行时会从return Promise.reject(1) 语句接受完成值。当然，p2.then又创建了另一个新的promise，可以用变量p3存储。</p><p>new Promise出来的实例，成功或者失败，取决于executor函数执行的时候，<strong>执行的是resolve还是reject决定的</strong>，或<strong>executor函数执行发生异常错误</strong>，这两种情况都会把实例状态改为失败的。</p><p>p2执行then返回的新实例的状态，决定下一个then中哪一个方法会被执行，有以下几种情况：</p><ul><li>不论是成功的方法执行，还是失败的方法执行（then中的两个方法），凡是执行抛出了异常，则都会把实例的状态改为失败。</li><li>方法中如果返回一个新的Promise实例（比如上例中的Promise.reject(1)），返回这个实例的结果是成功还是失败，也决定了当前实例是成功还是失败。</li><li>剩下的情况基本上都是让实例变为成功的状态，上一个then中方法返回的结果会传递到下一个then的方法中。</li></ul><p>我们再来看个例子</p><pre><code class="javascript">new Promise(resolve=>&#123;
    resolve(a) // 报错 
// 这个executor函数执行发生异常错误，决定下个then失败方法会被执行
&#125;).then(result=>&#123;
    console.log(`成功：$&#123;result&#125;`)
    return result*10
&#125;,reason=>&#123;
    console.log(`失败：$&#123;reason&#125;`)
// 执行这句时候，没有发生异常或者返回一个失败的Promise实例，所以下个then成功方法会被执行
// 这里没有return，最后会返回 undefined
&#125;).then(result=>&#123;
    console.log(`成功：$&#123;result&#125;`)
&#125;,reason=>&#123;
    console.log(`失败：$&#123;reason&#125;`)
&#125;)
// 失败：ReferenceError: a is not defined
// 成功：undefined</code></pre><h3>async & await</h3><p>从上面一些例子，我们可以看出，虽然使用 Promise 能很好地解决回调地狱的问题，但是这种方式充满了 Promise 的 then() 方法，如果处理流程比较复杂的话，那么整段代码将充斥着 then，语义化不明显，代码不能很好地表示执行流程。</p><p>ES7中新增的异步编程方法，async/await的实现是基于 Promise的，简单而言就是async 函数就是返回Promise对象，是generator的语法糖。很多人认为async/await是异步操作的终极解决方案：</p><ul><li>语法简洁，更像是同步代码，也更符合普通的阅读习惯；</li><li>改进JS中异步操作串行执行的代码组织方式，减少callback的嵌套；</li><li>Promise中不能自定义使用try/catch进行错误捕获，但是在Async/await中可以像处理同步代码处理错误。</li></ul><p>不过也存在一些缺点，因为 await 将异步代码改造成了同步代码，如果多个异步代码没有依赖性却使用了 await 会导致性能上的降低。</p><pre><code class="javascript">async function test() &#123;
  // 以下代码没有依赖性的话，完全可以使用 Promise.all 的方式
  // 如果有依赖性的话，其实就是解决回调地狱的例子了
  await fetch(url1)
  await fetch(url2)
  await fetch(url3)
&#125;</code></pre><p>观察下面这段代码，你能判断出打印出来的内容是什么吗？</p><pre><code class="javascript">let p1 = Promise.resolve(1)
let p2 = new Promise(resolve => &#123;
  setTimeout(() => &#123;
    resolve(2)
  &#125;, 1000)
&#125;)
async function fn() &#123;
  console.log(1)
// 当代码执行到此行（先把此行），构建一个异步的微任务
// 等待promise返回结果，并且await下面的代码也都被列到任务队列中
  let result1 = await p2
  console.log(3)
  let result2 = await p1
  console.log(4)
&#125;
fn()
console.log(2)
// 1 2 3 4</code></pre><p>如果 await 右侧表达逻辑是个 promise，await会等待这个promise的返回结果，<strong>只有返回的状态是resolved情况</strong>，才会把结果返回,如果promise是失败状态，则await不会接收其返回结果，await下面的代码也不会在继续执行。</p><pre><code class="javascript">let p1 = Promise.reject(100)
async function fn1() &#123;
  let result = await p1
  console.log(1) //这行代码不会执行
&#125;</code></pre><p>我们再来看道比较复杂的题目：</p><pre><code class="javascript">console.log(1)
setTimeout(()=>&#123;console.log(2)&#125;,1000)
async function fn()&#123;
    console.log(3)
    setTimeout(()=>&#123;console.log(4)&#125;,20)
    return Promise.reject()
&#125;
async function run()&#123;
    console.log(5)
    await fn()
    console.log(6)
&#125;
run()
//需要执行150ms左右
for(let i=0;i<90000000;i++)&#123;&#125;
setTimeout(()=>&#123;
    console.log(7)
    new Promise(resolve=>&#123;
        console.log(8)
        resolve()
    &#125;).then(()=>&#123;console.log(9)&#125;)
&#125;,0)
console.log(10)
// 1 5 3 10 4 7 8 9 2 </code></pre><p>做这道题之前，读者需明白：</p><ul><li>基于微任务的技术有 MutationObserver、Promise 以及以 Promise 为基础开发出来的很多其他的技术，本题中resolve()、await fn()都是微任务。</li><li>不管宏任务是否到达时间，以及放置的先后顺序，每次主线程执行栈为空的时候，引擎会优先处理微任务队列，<strong>处理完微任务队列里的所有任务</strong>，再去处理宏任务。</li></ul><p>接下来，我们一步一步分析：</p><ul><li>首先执行同步代码，输出 1，遇见第一个setTimeout，将其回调放入任务队列（宏任务）当中，继续往下执行</li><li>运行run(),打印出 5，并往下执行，遇见 await fn()，将其放入任务队列（微任务）</li><li>await fn() 当前这一行代码执行时，fn函数会立即执行的,打印出3，遇见第二个setTimeout，将其回调放入任务队列（宏任务），await fn() 下面的代码需要等待返回Promise成功状态才会执行，所以6是不会被打印的。</li><li>继续往下执行，遇到for循环同步代码，需要等150ms,虽然第二个setTimeout已经到达时间，但不会执行，遇见第三个setTimeout，将其回调放入任务队列（宏任务），然后打印出10。值得注意的是，这个定时器 推迟时间0毫秒实际上达不到的。根据HTML5标准，setTimeOut推迟执行的时间，最少是4毫秒。</li><li>同步代码执行完毕，此时没有微任务，就去执行宏任务，上面提到已经到点的setTimeout先执行，打印出4</li><li>然后执行下一个setTimeout的宏任务，所以先打印出7，new Promise的时候会立即把executor函数执行，打印出8，然后在执行resolve时，触发微任务，于是打印出9</li><li>最后执行第一个setTimeout的宏任务，打印出2</li></ul><h2>常用的方法</h2><h3>1、Promise.resolve()</h3><p>Promise.resolve(value)方法返回一个以给定值解析后的Promise 对象。<br>Promise.resolve()等价于下面的写法:</p><pre><code class="javascript">Promise.resolve('foo')
// 等价于
new Promise(resolve => resolve('foo'))</code></pre><p>Promise.resolve方法的参数分成四种情况。</p><p>（1）参数是一个 Promise 实例</p><p>如果参数是 Promise 实例，那么Promise.resolve将<strong>不做任何修改、原封不动地</strong>返回这个实例。</p><pre><code class="javascript">const p1 = new Promise(function (resolve, reject) &#123;
  setTimeout(() => reject(new Error('fail')), 3000)
&#125;)
const p2 = new Promise(function (resolve, reject) &#123;
  setTimeout(() => resolve(p1), 1000)
&#125;)
p2
  .then(result => console.log(result))
  .catch(error => console.log(error))
// Error: fail</code></pre><p>上面代码中，p1是一个 Promise，3 秒之后变为rejected。p2的状态在 1 秒之后改变，resolve方法返回的是p1。由于p2返回的是另一个 Promise，导致p2自己的状态无效了，由p1的状态决定p2的状态。所以，后面的then语句都变成针对后者（p1）。又过了 2 秒，p1变为rejected，导致触发catch方法指定的回调函数。</p><p>（2）参数不是具有then方法的对象，或根本就不是对象</p><pre><code class="javascript">Promise.resolve("Success").then(function(value) &#123;
 // Promise.resolve方法的参数，会同时传给回调函数。
  console.log(value); // "Success"
&#125;, function(value) &#123;
  // 不会被调用
&#125;);</code></pre><p>（3）不带有任何参数</p><p>Promise.resolve()方法允许调用时不带参数，直接返回一个resolved状态的 Promise 对象。如果希望得到一个 Promise 对象，比较方便的方法就是直接调用Promise.resolve()方法。</p><pre><code class="javascript">Promise.resolve().then(function () &#123;
  console.log('two');
&#125;);
console.log('one');
// one two</code></pre><p>（4）参数是一个thenable对象</p><p>thenable对象指的是具有then方法的对象,Promise.resolve方法会将这个对象转为 Promise 对象，然后就立即执行thenable对象的then方法。</p><pre><code class="javascript">let thenable = &#123;
  then: function(resolve, reject) &#123;
    resolve(42);
  &#125;
&#125;;
let p1 = Promise.resolve(thenable);
p1.then(function(value) &#123;
  console.log(value);  // 42
&#125;);</code></pre><h3>2、Promise.reject()</h3><p>Promise.reject()方法返回一个带有拒绝原因的Promise对象。</p><pre><code class="javascript">new Promise((resolve,reject) => &#123;
    reject(new Error("出错了"));
&#125;);
// 等价于
 Promise.reject(new Error("出错了"));  

// 使用方法
Promise.reject(new Error("BOOM!")).catch(error => &#123;
    console.error(error);
&#125;);</code></pre><p>值得注意的是，调用resolve或reject以后，Promise 的使命就完成了，后继操作应该放到then方法里面，而<strong>不应该直接写在resolve或reject的后面</strong>。所以，最好在它们前面加上return语句，这样就不会有意外。</p><pre><code class="javascript">new Promise((resolve, reject) => &#123;
  return reject(1);
  // 后面的语句不会执行
  console.log(2);
&#125;)</code></pre><h3>3、Promise.all()</h3><pre><code class="javascript">let p1 = Promise.resolve(1)
let p2 = new Promise(resolve => &#123;
  setTimeout(() => &#123;
    resolve(2)
  &#125;, 1000)
&#125;)
let p3 = Promise.resolve(3)
Promise.all([p3, p2, p1])
  .then(result => &#123;
 // 返回的结果是按照Array中编写实例的顺序来
    console.log(result) // [ 3, 2, 1 ]
  &#125;)
  .catch(reason => &#123;
    console.log("失败:reason")
  &#125;)</code></pre><p>Promise.all 生成并返回一个新的 Promise 对象，所以它可以使用 Promise 实例的所有方法。参数传递promise数组中<strong>所有的 Promise 对象都变为resolve的时候</strong>，该方法才会返回， 新创建的 Promise 则会使用这些 promise 的值。</p><p>如果参数中的<strong>任何一个promise为reject的话</strong>，则整个Promise.all调用会<strong>立即终止</strong>，并返回一个reject的新的 Promise 对象。</p><h3>4、Promise.allSettled()</h3><p>有时候，我们不关心异步操作的结果，只关心这些操作有没有结束。这时，ES2020 引入Promise.allSettled()方法就很有用。如果没有这个方法，想要确保所有操作都结束，就很麻烦。Promise.all()方法无法做到这一点。</p><p>假如有这样的场景：一个页面有三个区域，分别对应三个独立的接口数据，使用 Promise.all 来并发请求三个接口，如果其中任意一个接口出现异常，状态是reject,这会导致页面中该三个区域数据全都无法出来，显然这种状况我们是无法接受，Promise.allSettled的出现就可以解决这个痛点：</p><pre><code class="javascript">Promise.allSettled([
  Promise.reject(&#123; code: 500, msg: '服务异常' &#125;),
  Promise.resolve(&#123; code: 200, list: [] &#125;),
  Promise.resolve(&#123; code: 200, list: [] &#125;)
]).then(res => &#123;
  console.log(res)
  /*
 0: &#123;status: "rejected", reason: &#123;…&#125;&#125;
 1: &#123;status: "fulfilled", value: &#123;…&#125;&#125;
 2: &#123;status: "fulfilled", value: &#123;…&#125;&#125;
 */
  // 过滤掉 rejected 状态，尽可能多的保证页面区域数据渲染
  RenderContent(
    res.filter(el => &#123;
      return el.status !== 'rejected'
    &#125;)
  )
&#125;)</code></pre><p>Promise.allSettled跟Promise.all类似, 其参数接受一个Promise的数组, 返回一个新的Promise, <strong>唯一的不同在于, 它不会进行短路</strong>, 也就是说当Promise全部处理完成后,我们可以拿到每个Promise的状态, 而不管是否处理成功。</p><h3>5、Promise.race()</h3><p>Promise.all()方法的效果是"谁跑的慢，以谁为准执行回调"，那么相对的就有另一个方法"谁跑的快，以谁为准执行回调"，这就是Promise.race()方法，这个词本来就是赛跑的意思。race的用法与all一样，接收一个promise对象数组为参数。</p><p>Promise.all在接收到的所有的对象promise都变为FulFilled或者Rejected状态之后才会继续进行后面的处理，与之相对的是Promise.race<strong>只要有一个promise对象进入FulFilled或者Rejected状态的话</strong>，就会继续进行后面的处理。</p><pre><code class="javascript">// `delay`毫秒后执行resolve
function timerPromisefy(delay) &#123;
    return new Promise(resolve => &#123;
        setTimeout(() => &#123;
            resolve(delay);
        &#125;, delay);
    &#125;);
&#125;
// 任何一个promise变为resolve或reject的话程序就停止运行
Promise.race([
    timerPromisefy(1),
    timerPromisefy(32),
    timerPromisefy(64)
]).then(function (value) &#123;
    console.log(value);    // => 1
&#125;);</code></pre><p>上面的代码创建了3个promise对象，这些promise对象会分别在1ms、32ms 和 64ms后变为确定状态，即FulFilled，并且在第一个变为确定状态的1ms后，.then注册的回调函数就会被调用。</p><h3>6、Promise.prototype.finally()</h3><p>ES9 新增 finally() 方法返回一个Promise。在promise结束时，无论结果是fulfilled或者是rejected，都会执行指定的回调函数。<strong>这为在Promise是否成功完成后都需要执行的代码提供了一种方式</strong>。这避免了同样的语句需要在then()和catch()中各写一次的情况。</p><p>比如我们发送请求之前会出现一个loading，当我们请求发送完成之后，不管请求有没有出错，我们都希望关掉这个loading。</p><pre><code class="javascript">this.loading = true
request()
  .then((res) => &#123;
    // do something
  &#125;)
  .catch(() => &#123;
    // log err
  &#125;)
  .finally(() => &#123;
    this.loading = false
  &#125;)</code></pre><p>finally方法的回调函数不接受任何参数，这表明，finally方法里面的操作，应该是与状态无关的，不依赖于 Promise 的执行结果。</p><h2>实际应用</h2><p>假设有这样一个需求：红灯 3s 亮一次，绿灯 1s 亮一次，黄灯 2s 亮一次；如何让三个灯不断交替重复亮灯？<br>三个亮灯函数已经存在：</p><pre><code class="javascript">function red() &#123;
    console.log('red');
&#125;
function green() &#123;
    console.log('green');
&#125;
function yellow() &#123;
    console.log('yellow');
&#125;</code></pre><p>这道题复杂的地方在于<strong>需要“交替重复”亮灯</strong>，而不是亮完一遍就结束的一锤子买卖，我们可以通过递归来实现：</p><pre><code class="javascript">// 用 promise 实现
let task = (timer, light) => &#123;
  return new Promise((resolve, reject) => &#123;
    setTimeout(() => &#123;
      if (light === 'red') &#123;
        red()
      &#125;
      if (light === 'green') &#123;
        green()
      &#125;
      if (light === 'yellow') &#123;
        yellow()
      &#125;
      resolve()
    &#125;, timer);
  &#125;)
&#125;
let step = () => &#123;
  task(3000, 'red')
    .then(() => task(1000, 'green'))
    .then(() => task(2000, 'yellow'))
    .then(step)
&#125;
step()</code></pre><p>同样也可以通过async/await 的实现：</p><pre><code class="javascript">//  async/await 实现
let step = async () => &#123;
  await task(3000, 'red')
  await task(1000, 'green')
  await task(2000, 'yellow')
  step()
&#125;
step()</code></pre><p>使用 async/await 可以实现用同步代码的风格来编写异步代码,毫无疑问，还是 async/await 的方案更加直观，不过深入理解Promise 是掌握async/await的基础。</p>  
</div>
            